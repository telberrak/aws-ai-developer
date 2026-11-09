"""Calls Bedrock Converse with the model ID it is given. Can simulate a primary failure."""
import boto3

bedrock = boto3.client("bedrock-runtime")


class SimulatedFailure(Exception):
    pass


def handler(event, context):
    if event.get("role") == "primary" and event.get("simulateFailure"):
        raise SimulatedFailure("Simulated failure of the primary model")

    resp = bedrock.converse(
        modelId=event["modelId"],
        messages=[{"role": "user", "content": [{"text": event["prompt"]}]}],
        inferenceConfig={"temperature": 0.2, "maxTokens": 200},
    )
    return {
        "path": event["role"],
        "modelId": event["modelId"],
        "text": resp["output"]["message"]["content"][0]["text"],
    }
