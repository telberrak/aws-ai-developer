"""A Strands agent that answers order questions using the MCP server's tools.

python agent.py "Where is my order ORD-1002?"
python agent.py --http "Can I get a refund for ORD-1001?"     # server already running with --http
"""
import argparse
import os
import sys

from mcp.client.stdio import StdioServerParameters, stdio_client
from strands import Agent
from strands.hooks import BeforeInvocationEvent, BeforeToolCallEvent, HookProvider, HookRegistry
from strands.models import BedrockModel
from strands.tools.mcp import MCPClient

SYSTEM = (
    "You are a customer support agent for an online shop. Use the tools to look up orders. "
    "Only answer about orders the tools return. If a tool refuses or finds nothing, say so and ask "
    "for a valid order ID. You can check refund eligibility but you cannot issue refunds."
)


class ToolBudget(HookProvider):
    """Stopping condition: at most N tool calls per question, then the agent must answer."""

    def __init__(self, max_calls: int):
        self.max_calls, self.calls = max_calls, 0

    def register_hooks(self, registry: HookRegistry, **kwargs) -> None:
        registry.add_callback(BeforeInvocationEvent, self.reset)
        registry.add_callback(BeforeToolCallEvent, self.count)

    def reset(self, event: BeforeInvocationEvent) -> None:
        self.calls = 0

    def count(self, event: BeforeToolCallEvent) -> None:
        self.calls += 1
        name = event.tool_use["name"]
        print(f"  [tool call {self.calls}/{self.max_calls}] {name} {event.tool_use['input']}", file=sys.stderr)
        if self.calls > self.max_calls:
            event.cancel_tool = "Tool budget reached. Answer with what you already know."


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("question")
    p.add_argument("--http", action="store_true", help="connect to http://127.0.0.1:8000/mcp instead of starting the server over stdio")
    p.add_argument("--model", default=os.environ.get("MODEL_ID", "us.amazon.nova-pro-v1:0"))
    p.add_argument("--region", default=os.environ.get("AWS_REGION", "us-east-1"))
    p.add_argument("--max-tool-calls", type=int, default=3)
    a = p.parse_args()

    if a.http:
        client = MCPClient(url="http://127.0.0.1:8000/mcp")
    else:
        here = os.path.dirname(os.path.abspath(__file__))
        params = StdioServerParameters(command=sys.executable, args=[os.path.join(here, "order_server.py")])
        client = MCPClient(lambda: stdio_client(params))

    with client:
        tools = client.list_tools_sync()
        print("Tools from the MCP server:", ", ".join(t.tool_name for t in tools), file=sys.stderr)
        agent = Agent(
            model=BedrockModel(model_id=a.model, region_name=a.region, temperature=0),
            tools=tools,
            system_prompt=SYSTEM,
            hooks=[ToolBudget(a.max_tool_calls)],
            callback_handler=None,
        )
        result = agent(a.question)
        print(str(result).strip())


if __name__ == "__main__":
    main()
