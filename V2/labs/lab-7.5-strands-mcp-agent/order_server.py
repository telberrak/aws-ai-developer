"""A tiny MCP server with two read-only tools over orders.json.

Run it over stdio (the agent starts it for you):   python order_server.py
Or over streamable HTTP on http://127.0.0.1:8000/mcp: python order_server.py --http
"""
import argparse
import json
import re
from datetime import date
from pathlib import Path

from mcp.server.mcpserver import MCPServer
from mcp.types import ToolAnnotations

ORDERS = json.loads((Path(__file__).parent / "orders.json").read_text())
ORDER_ID = re.compile(r"^ORD-\d{4}$")
RETURN_WINDOW_DAYS = 30
TODAY = date(2026, 11, 9)  # fixed so the lab gives the same answers every time

server = MCPServer(name="orders", instructions="Look up orders and check refund eligibility. Read-only.")
READ_ONLY = ToolAnnotations(readOnlyHint=True, destructiveHint=False, idempotentHint=True)


def _check_id(order_id: str) -> str | None:
    """Refuse anything that isn't a plain order ID, before touching any data."""
    if not ORDER_ID.match(order_id or ""):
        return "REFUSED: order_id must look like ORD-1234. Ask the customer for their order ID."
    if order_id not in ORDERS:
        return f"NOT FOUND: there is no order {order_id}."
    return None


@server.tool(annotations=READ_ONLY)
def get_order_status(order_id: str) -> str:
    """Get the status of one order.

    Args:
        order_id: The order ID, exactly in the form ORD-1234.
    """
    if (err := _check_id(order_id)):
        return err
    o = ORDERS[order_id]
    details = {k: v for k, v in o.items() if k != "customer"}
    return json.dumps({"order_id": order_id, **details})


@server.tool(annotations=READ_ONLY)
def check_refund_eligibility(order_id: str) -> str:
    """Check whether an order can be refunded. It never issues a refund.

    Args:
        order_id: The order ID, exactly in the form ORD-1234.
    """
    if (err := _check_id(order_id)):
        return err
    o = ORDERS[order_id]
    if o["status"] != "delivered":
        return json.dumps({"order_id": order_id, "eligible": False, "reason": f"Order is {o['status']}; it can be cancelled instead."})
    days = (TODAY - date.fromisoformat(o["delivered_on"])).days
    ok = days <= RETURN_WINDOW_DAYS
    return json.dumps({"order_id": order_id, "eligible": ok, "days_since_delivery": days,
                       "reason": f"Within the {RETURN_WINDOW_DAYS}-day window." if ok else f"Outside the {RETURN_WINDOW_DAYS}-day window."})


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--http", action="store_true", help="serve streamable HTTP on 127.0.0.1:8000/mcp instead of stdio")
    a = p.parse_args()
    if a.http:
        server.run(transport="streamable-http", host="127.0.0.1", port=8000)
    else:
        server.run()
