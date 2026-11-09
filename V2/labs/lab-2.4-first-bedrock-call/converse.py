"""Lecture 2.4 demo: your first Amazon Bedrock call with the Converse API.

Usage:
    export AWS_REGION=<your-region>
    export MODEL_ID=<model-id-or-inference-profile-id>
    python converse.py "What is RAG?" --temperature 0.2
"""
import argparse
import os

import boto3


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", nargs="?", default="What is RAG?")
    parser.add_argument("--temperature", type=float, default=0.2)
    parser.add_argument("--max-tokens", type=int, default=300)
    args = parser.parse_args()

    model_id = os.environ["MODEL_ID"]
    client = boto3.client("bedrock-runtime")

    response = client.converse(
        modelId=model_id,
        system=[{"text": "You are a concise AWS tutor."}],
        messages=[{"role": "user", "content": [{"text": args.prompt}]}],
        inferenceConfig={"temperature": args.temperature, "maxTokens": args.max_tokens},
    )

    print(response["output"]["message"]["content"][0]["text"])
    print()
    print("Stop reason:", response["stopReason"])
    print("Usage:", response["usage"])  # inputTokens, outputTokens, totalTokens
    print("Latency (ms):", response["metrics"]["latencyMs"])


if __name__ == "__main__":
    main()
