"""Reads the outputs of the ChunkingDemo stack, so the scripts need no copy and paste."""
import boto3

STACK = "ChunkingDemo"
KBS = ("fixed", "semantic")


def outputs() -> dict:
    stack = boto3.client("cloudformation").describe_stacks(StackName=STACK)["Stacks"][0]
    return {o["OutputKey"]: o["OutputValue"] for o in stack.get("Outputs", [])}


def kb(out: dict, name: str) -> tuple:
    """Returns (knowledge base ID, data source ID) for 'fixed' or 'semantic'."""
    label = name.capitalize()
    return out[f"{label}KnowledgeBaseId"], out[f"{label}DataSourceId"]
