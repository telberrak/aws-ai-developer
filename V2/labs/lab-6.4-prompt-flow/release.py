"""Releases a new prompt: new prompt version, new flow version, then moves the "live" alias.

Usage:  python release.py prompt-v2.txt
Nothing changes for callers until the last step, when the alias moves.
"""
import sys
import time

import boto3

from stack_outputs import outputs

new_text = open(sys.argv[1] if len(sys.argv) > 1 else "prompt-v2.txt", encoding="utf-8").read().strip()
out = outputs()
agent = boto3.client("bedrock-agent")
flow_id, alias_id, prompt_id = out["FlowId"], out["FlowAliasId"], out["PromptId"]

# 1. Edit the prompt's draft, then freeze it as a new prompt version.
prompt = agent.get_prompt(promptIdentifier=prompt_id)
variants = prompt["variants"]
variants[0]["templateConfiguration"]["text"]["text"] = new_text
agent.update_prompt(promptIdentifier=prompt_id, name=prompt["name"],
                    defaultVariant=prompt["defaultVariant"], variants=variants)
prompt_version = agent.create_prompt_version(promptIdentifier=prompt_id, description="Release from release.py")
print(f"1. Prompt version {prompt_version['version']} created")

# 2. Point the flow's draft at the new prompt version, and prepare it.
flow = agent.get_flow(flowIdentifier=flow_id)
definition = flow["definition"]
for node in definition["nodes"]:
    if node["name"] == "Triage":
        node["configuration"]["prompt"]["sourceConfiguration"]["resource"]["promptArn"] = prompt_version["arn"]
agent.update_flow(flowIdentifier=flow_id, name=flow["name"],
                  executionRoleArn=flow["executionRoleArn"], definition=definition)
agent.prepare_flow(flowIdentifier=flow_id)
while (status := agent.get_flow(flowIdentifier=flow_id)["status"]) not in ("Prepared", "Failed"):
    time.sleep(2)
if status == "Failed":
    sys.exit("The flow failed to prepare. Check the prompt variables still match the node inputs.")
print("2. Flow draft now uses the new prompt version, and is prepared")

# 3. Freeze the flow as a new version.
flow_version = agent.create_flow_version(flowIdentifier=flow_id, description="Release from release.py")
print(f"3. Flow version {flow_version['version']} created")

# 4. Move the alias. This is the release: callers get the new version on their next call.
alias = agent.get_flow_alias(flowIdentifier=flow_id, aliasIdentifier=alias_id)
previous = alias["routingConfiguration"][0]["flowVersion"]
agent.update_flow_alias(flowIdentifier=flow_id, aliasIdentifier=alias_id, name=alias["name"],
                        routingConfiguration=[{"flowVersion": flow_version["version"]}])
print(f"4. Alias 'live' moved from version {previous} to version {flow_version['version']}")
print(f"\nTo roll back:  python rollback.py {previous}")
