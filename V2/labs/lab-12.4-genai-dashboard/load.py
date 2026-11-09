"""Sends a batch of Converse calls so the dashboard has traffic to show.

Examples:
  python load.py                          # 30 calls, one at a time
  python load.py --calls 60 --threads 8   # more calls in parallel, to try to see throttles
  python load.py --max-tokens 800         # longer answers: more output tokens, more latency, more cost

It prints the tokens and latency that Bedrock reports for every call, and an
estimated cost using the same example prices as cdk.json. Bedrock metrics
usually reach CloudWatch within a few minutes.
"""
import argparse
import json
import random
import time
from concurrent.futures import ThreadPoolExecutor

import boto3
from botocore.config import Config
from botocore.exceptions import ClientError

QUESTIONS = [
    "Explain what a context window is in two sentences.",
    "Give three tips for writing a clear system prompt.",
    "What is the difference between Retrieve and RetrieveAndGenerate?",
    "Summarize why prompt caching lowers cost.",
    "List four metrics to watch for a GenAI application.",
    "Explain exponential backoff with jitter to a new developer.",
]


def settings() -> dict:
    with open("cdk.json") as f:
        return json.load(f)["context"]


def call(client, model_id: str, max_tokens: int, retries: int = 5) -> dict:
    prompt = random.choice(QUESTIONS)
    for attempt in range(retries + 1):
        try:
            r = client.converse(
                modelId=model_id,
                messages=[{"role": "user", "content": [{"text": prompt}]}],
                inferenceConfig={"maxTokens": max_tokens, "temperature": 0.5},
            )
            return {"ok": True, "in": r["usage"]["inputTokens"], "out": r["usage"]["outputTokens"],
                    "ms": r["metrics"]["latencyMs"], "retries": attempt}
        except ClientError as e:
            code = e.response["Error"]["Code"]
            if code == "ThrottlingException" and attempt < retries:
                time.sleep(min(20, 2 ** attempt) * random.uniform(0.5, 1.0))  # backoff with jitter
                continue
            return {"ok": False, "error": code, "retries": attempt}


def main() -> None:
    ctx = settings()
    p = argparse.ArgumentParser()
    p.add_argument("--model", default=ctx["model_id"], help="model or inference profile ID (default from cdk.json)")
    p.add_argument("--calls", type=int, default=30)
    p.add_argument("--threads", type=int, default=1)
    p.add_argument("--max-tokens", type=int, default=300)
    a = p.parse_args()

    client = boto3.client("bedrock-runtime", config=Config(retries={"max_attempts": 1}))
    print(f"Sending {a.calls} calls to {a.model} with {a.threads} thread(s)...")
    with ThreadPoolExecutor(max_workers=a.threads) as pool:
        results = list(pool.map(lambda _: call(client, a.model, a.max_tokens), range(a.calls)))

    ok = [r for r in results if r["ok"]]
    failed = [r for r in results if not r["ok"]]
    tin = sum(r["in"] for r in ok)
    tout = sum(r["out"] for r in ok)
    lat = sorted(r["ms"] for r in ok)
    cost = tin / 1000 * float(ctx["price_in_per_1k"]) + tout / 1000 * float(ctx["price_out_per_1k"])
    print(f"Succeeded: {len(ok)}   Failed: {len(failed)}   Retried after throttling: {sum(r['retries'] for r in results)}")
    print(f"Tokens in: {tin}   Tokens out: {tout}")
    if lat:
        print(f"Latency ms: avg {sum(lat) / len(lat):.0f}   p90 {lat[int(0.9 * (len(lat) - 1))]}   max {lat[-1]}")
    print(f"Estimated cost with the example prices: ${cost:.6f}")
    for r in failed:
        print("  failed:", r["error"])
    print("Open the dashboard in a few minutes to see these numbers in CloudWatch.")


if __name__ == "__main__":
    main()
