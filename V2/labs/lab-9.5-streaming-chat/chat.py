"""Streaming terminal chat on Amazon Bedrock with retries and model fallback.

  python chat.py                              # chat with the primary model
  python chat.py --simulate-throttle 2        # first 2 calls throttled, then it recovers
  python chat.py --simulate-throttle always   # primary always throttled, fallback answers
  python chat.py --offline --simulate-throttle always   # same, with no AWS calls at all
"""
import argparse
import sys
import time

from resilience import StreamBroken, chat_with_resilience, make_client
from fakes import FakeModelClient, ThrottlingClient

SYSTEM = "You are a concise assistant. Answer in three sentences or fewer."


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--region", default="us-east-1")
    p.add_argument("--model", default="us.amazon.nova-lite-v1:0", help="primary model or inference profile ID")
    p.add_argument("--fallback-model", default="us.amazon.nova-micro-v1:0")
    p.add_argument("--retries", type=int, default=3, help="our retries per model, on top of botocore's")
    p.add_argument("--simulate-throttle", default="0", help="N throttles on the primary model, or 'always'")
    p.add_argument("--offline", action="store_true", help="use a fake model: no AWS calls")
    p.add_argument("--once", help="ask one question and exit")
    a = p.parse_args()

    client = FakeModelClient(delay=0.05) if a.offline else make_client(a.region)
    n = 10**6 if a.simulate_throttle == "always" else int(a.simulate_throttle)
    if n:
        client = ThrottlingClient(client, {a.model: n})
    models = [a.model, a.fallback_model]

    messages = []
    print(f"Primary: {a.model}   Fallback: {a.fallback_model}   {'(offline)' if a.offline else ''}")
    while True:
        q = a.once or input("\nYou: ").strip()
        if not q or q.lower() in {"exit", "quit"}:
            return
        messages.append({"role": "user", "content": [{"text": q}]})
        print("Model: ", end="", flush=True)
        t0 = time.time()
        first = {}
        parts = []

        def on_text(piece):
            if not first:
                first["t"] = time.time() - t0
            parts.append(piece)
            print(piece, end="", flush=True)

        try:
            used, info = chat_with_resilience(client, models, messages, on_text, system=SYSTEM,
                                              retries_per_model=a.retries,
                                              log=lambda m: print("\n" + m, file=sys.stderr, flush=True))
        except StreamBroken as e:
            print(f"\n[error] {e}. Ask again to retry.")
            messages.pop()
            continue
        except Exception as e:
            print(f"\n[error] {type(e).__name__}: {e}")
            messages.pop()
            if a.once:
                sys.exit(1)
            continue
        messages.append({"role": "assistant", "content": [{"text": "".join(parts)}]})
        u = info.get("usage", {})
        print(f"\n[{used} | first token {first.get('t', 0):.2f}s | total {time.time() - t0:.2f}s | "
              f"tokens in {u.get('inputTokens')} out {u.get('outputTokens')}]")
        if a.once:
            return


if __name__ == "__main__":
    main()
