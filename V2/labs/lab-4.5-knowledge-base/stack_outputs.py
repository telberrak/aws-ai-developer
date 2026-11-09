"""Reads the outputs of the KnowledgeBaseDemo stack, so the scripts need no copy and paste."""
import boto3

STACK = "KnowledgeBaseDemo"


def outputs() -> dict:
    stack = boto3.client("cloudformation").describe_stacks(StackName=STACK)["Stacks"][0]
    return {o["OutputKey"]: o["OutputValue"] for o in stack.get("Outputs", [])}
