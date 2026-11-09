"""Rolls back by pointing the "live" alias at an earlier flow version. Nothing is rebuilt.

Usage:  python rollback.py 1
"""
import sys

import boto3

from stack_outputs import outputs

version = sys.argv[1] if len(sys.argv) > 1 else "1"
out = outputs()
agent = boto3.client("bedrock-agent")
alias = agent.get_flow_alias(flowIdentifier=out["FlowId"], aliasIdentifier=out["FlowAliasId"])
agent.update_flow_alias(flowIdentifier=out["FlowId"], aliasIdentifier=out["FlowAliasId"], name=alias["name"],
                        routingConfiguration=[{"flowVersion": version}])
print(f"Alias 'live' now points at flow version {version}")
