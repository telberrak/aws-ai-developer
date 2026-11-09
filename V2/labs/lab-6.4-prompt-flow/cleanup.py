"""Run before cdk destroy. Points the alias back at version 1, then deletes the versions that
release.py created, since CloudFormation only knows about the ones it made."""
import boto3

from stack_outputs import outputs

out = outputs()
agent = boto3.client("bedrock-agent")
flow_id, alias_id = out["FlowId"], out["FlowAliasId"]

alias = agent.get_flow_alias(flowIdentifier=flow_id, aliasIdentifier=alias_id)
agent.update_flow_alias(flowIdentifier=flow_id, aliasIdentifier=alias_id, name=alias["name"],
                        routingConfiguration=[{"flowVersion": "1"}])

for v in agent.list_flow_versions(flowIdentifier=flow_id)["flowVersionSummaries"]:
    if v["version"] not in ("DRAFT", "1"):
        agent.delete_flow_version(flowIdentifier=flow_id, flowVersion=v["version"])
        print(f"Deleted flow version {v['version']}")

prompt_id = out["PromptId"]
for p in agent.list_prompts(promptIdentifier=prompt_id)["promptSummaries"]:
    if p["version"] not in ("DRAFT", "1"):
        agent.delete_prompt(promptIdentifier=prompt_id, promptVersion=p["version"])
        print(f"Deleted prompt version {p['version']}")
print("Done. Now run: cdk destroy")
