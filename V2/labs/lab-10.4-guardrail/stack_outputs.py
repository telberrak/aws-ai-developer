"""Reads the GuardrailDemo stack outputs so the scripts don't need IDs pasted in."""
import boto3

STACK = "GuardrailDemo"


def outputs(region=None):
    cfn = boto3.client("cloudformation", region_name=region)
    stack = cfn.describe_stacks(StackName=STACK)["Stacks"][0]
    return {o["OutputKey"]: o["OutputValue"] for o in stack.get("Outputs", [])}
