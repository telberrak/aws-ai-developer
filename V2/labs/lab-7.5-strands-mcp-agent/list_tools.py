"""Check the MCP server without any AWS call: start it over stdio, list its tools, call them once."""
import os
import sys

from mcp.client.stdio import StdioServerParameters, stdio_client
from strands.tools.mcp import MCPClient

here = os.path.dirname(os.path.abspath(__file__))
params = StdioServerParameters(command=sys.executable, args=[os.path.join(here, "order_server.py")])
with MCPClient(lambda: stdio_client(params)) as client:
    for t in client.list_tools_sync():
        spec = t.tool_spec
        print(f"- {spec['name']}: {spec['description'].splitlines()[0]}")
    for name, args in [("get_order_status", {"order_id": "ORD-1002"}),
                       ("check_refund_eligibility", {"order_id": "ORD-1004"}),
                       ("get_order_status", {"order_id": "ORD-1001; DROP TABLE orders"})]:
        r = client.call_tool_sync(tool_use_id="t1", name=name, arguments=args)
        print(f"{name}({args['order_id']!r}) -> {r['content'][0]['text']}")
