"""Calls the flow through its "live" alias, the way an app would, and prints the answer.

Usage:  python invoke.py "My order arrived broken and nobody answers my emails."
"""
import sys

import boto3

from stack_outputs import outputs

TICKET = " ".join(sys.argv[1:]) or "My order arrived broken and nobody answers my emails."

out = outputs()
agent = boto3.client("bedrock-agent")
runtime = boto3.client("bedrock-agent-runtime")

alias = agent.get_flow_alias(flowIdentifier=out["FlowId"], aliasIdentifier=out["FlowAliasId"])
print(f"Alias 'live' points at flow version {alias['routingConfiguration'][0]['flowVersion']}\n")

response = runtime.invoke_flow(
    flowIdentifier=out["FlowId"],
    flowAliasIdentifier=out["FlowAliasId"],
    inputs=[{
        "nodeName": "FlowInput",
        "nodeOutputName": "document",
        "content": {"document": TICKET},
    }],
)
for event in response["responseStream"]:
    if "flowOutputEvent" in event:
        print(event["flowOutputEvent"]["content"]["document"])
    elif "flowCompletionEvent" in event:
        print(f"\n[{event['flowCompletionEvent']['completionReason']}]")
