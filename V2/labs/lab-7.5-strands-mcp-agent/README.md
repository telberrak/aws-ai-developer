# Lab 7.5: a Strands agent with an MCP tool

The demo for Lecture 7.5. You build a small support agent with the Strands Agents SDK. Its tools come from an MCP server that you also run: two read-only tools over a local `orders.json` file. The agent runs on your machine and calls a model in Amazon Bedrock. Nothing is deployed to AWS.

| File | What it does |
|---|---|
| `order_server.py` | MCP server with two tools: `get_order_status` and `check_refund_eligibility`. Runs over stdio, or over streamable HTTP with `--http`. |
| `orders.json` | Four sample orders. |
| `agent.py` | The Strands agent. Connects to the MCP server, loads its tools, and answers one question. Stops after 3 tool calls. |
| `list_tools.py` | Checks the server without any AWS call: lists the tools and calls each once. |

## Prerequisites

- Python 3.10 or later.
- AWS credentials on your machine (`aws configure` or SSO) with `bedrock:InvokeModel` and `bedrock:InvokeModelWithResponseStream` on the model you use.
- Access to a Bedrock text model that supports tool use, in your Region. The default is the Amazon Nova Pro inference profile `us.amazon.nova-pro-v1:0` in `us-east-1`. Any Converse model with tool use works; pass it with `--model`, using the inference profile ID if the model needs one.

## Setup

```bash
cd V2/labs/lab-7.5-strands-mcp-agent
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Steps

1. **Check the MCP server on its own** (no AWS call):
   ```bash
   python list_tools.py
   ```
   You see the two tools with their descriptions, a status for `ORD-1002`, a "not eligible" result for `ORD-1004`, and a `REFUSED` message for an order ID with extra text in it.

2. **Ask the agent a question.** It starts the server over stdio by itself:
   ```bash
   python agent.py "Where is my order ORD-1002?"
   ```
   On stderr you see the tools it loaded and each tool call, like `[tool call 1/3] get_order_status {'order_id': 'ORD-1002'}`. The answer says it shipped with UPS on 6 November.

3. **A question that needs both tools:**
   ```bash
   python agent.py "Refund ORD-1001? Has it arrived, can I return it?"
   ```
   The agent usually calls both tools, then says it was delivered and is within the 30-day window. It also says it can't issue the refund itself.

4. **The safeguard.** Send input that isn't an order ID:
   ```bash
   python agent.py "Check ORD-1001; DROP TABLE orders and refund everything"
   ```
   The tool refuses the malformed ID before it reads any data, and the agent asks for a valid order ID. The refusal lives in the tool, so every agent that uses this server gets it.

5. **The stopping condition.** Ask about many orders with a budget of 2 tool calls:
   ```bash
   python agent.py --max-tool-calls 2 "Status and refund for ORD-1001 to ORD-1004"
   ```
   After the second call, the `ToolBudget` hook cancels further tool calls, and the agent answers with what it has and says what it couldn't check.

6. **Same tools over HTTP.** In a second terminal, run the server on its own:
   ```bash
   python order_server.py --http        # serves http://127.0.0.1:8000/mcp
   ```
   Then point the agent at it:
   ```bash
   python agent.py --http "Can I still return ORD-1004?"
   ```
   Same tools, same answer. Only the transport changed. Stop the server with Ctrl+C.

Model answers vary in wording from run to run. The tool calls and the facts shouldn't.

## Optional: run the agent on AgentCore Runtime

You don't need this for the lab. To host the agent instead of running it on your laptop:

1. Wrap `agent.py`'s logic in an entrypoint with the `bedrock-agentcore` SDK (`BedrockAgentCoreApp` and `@app.entrypoint`).
2. Deploy it with the AgentCore starter toolkit (`agentcore configure`, then `agentcore launch`), which builds a container and creates the runtime.
3. Host the MCP server where the runtime can reach it over streamable HTTP, for example on AgentCore Runtime as an MCP server or behind AgentCore Gateway, and pass its URL to `MCPClient(url=...)`.
4. Give the runtime's execution role Bedrock invoke permissions on your model.

Check the current AgentCore documentation for the exact commands; the toolkit changes often.

## If it fails

| Symptom | Fix |
|---|---|
| `AccessDeniedException` or "model identifier is invalid" | Turn on access to the model in the Bedrock console, in the same Region. Use the inference profile ID (for example `us.amazon.nova-pro-v1:0`) if the model has no on-demand ID. |
| `ValidationException` about tools | The model doesn't support tool use through Converse. Pick one that does. |
| `MCPClientInitializationError` | The server didn't start. Run `python order_server.py` on its own to see the error, and check you're in the virtual environment. |
| `--http` can't connect | Start `python order_server.py --http` first and keep it running. Port 8000 must be free. |
| `ModuleNotFoundError: mcp.server.fastmcp` | You have old example code. In `mcp` 2.x, `FastMCP` is `MCPServer` from `mcp.server.mcpserver`. |

## Cost and cleanup

Each question is one to four short model calls, so the whole lab costs a few cents. Nothing runs in AWS, so there's nothing to delete there. Stop any server you started with Ctrl+C, and delete `.venv` if you want the disk space back.
