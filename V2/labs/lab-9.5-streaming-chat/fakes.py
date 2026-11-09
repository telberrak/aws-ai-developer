"""Offline stand-ins so the lab can show retries and fallback with no AWS calls."""
import time
from botocore.exceptions import ClientError


def throttle_error():
    return ClientError({"Error": {"Code": "ThrottlingException", "Message": "Too many requests (simulated)"}},
                       "ConverseStream")


class FakeModelClient:
    """Pretends to be bedrock-runtime. Streams a canned answer word by word."""

    def __init__(self, delay=0.0, answer="Streaming sends the answer piece by piece, so the first words appear "
                              "in well under a second instead of after the whole reply is ready."):
        self.answer = answer
        self.delay = delay
        self.calls = []

    def converse_stream(self, **kwargs):
        self.calls.append(kwargs["modelId"])
        words = self.answer.split(" ")
        events = [{"messageStart": {"role": "assistant"}}]
        events += [{"contentBlockDelta": {"delta": {"text": (w if i == 0 else " " + w)}, "contentBlockIndex": 0}}
                   for i, w in enumerate(words)]
        events += [{"contentBlockStop": {"contentBlockIndex": 0}}, {"messageStop": {"stopReason": "end_turn"}},
                   {"metadata": {"usage": {"inputTokens": 12, "outputTokens": len(words), "totalTokens": 12 + len(words)},
                                 "metrics": {"latencyMs": 420}}}]
        def gen():
            for e in events:
                if self.delay and "contentBlockDelta" in e:
                    time.sleep(self.delay)
                yield e
        return {"stream": gen()}


class ThrottlingClient:
    """Wraps a client and throws ThrottlingException on the first N calls to chosen models.

    throttle: dict of model_id -> number of calls to throttle (use a big number for "always").
    """

    def __init__(self, inner, throttle):
        self.inner = inner
        self.left = dict(throttle)

    def converse_stream(self, **kwargs):
        model = kwargs["modelId"]
        if self.left.get(model, 0) > 0:
            self.left[model] -= 1
            raise throttle_error()
        return self.inner.converse_stream(**kwargs)
