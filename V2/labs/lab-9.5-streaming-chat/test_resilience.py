"""Offline self-check: python -m unittest -v  (no AWS calls, no waiting)."""
import unittest

from botocore.exceptions import ClientError

from fakes import FakeModelClient, ThrottlingClient
from resilience import StreamBroken, backoff_delay, chat_with_resilience

MSG = [{"role": "user", "content": [{"text": "hi"}]}]


def run(client, models=("primary", "fallback"), retries=3):
    out, logs, sleeps = [], [], []
    used, info = chat_with_resilience(client, list(models), MSG, out.append, retries_per_model=retries,
                                      sleep=sleeps.append, log=logs.append, rng=lambda: 1.0)
    return used, "".join(out), logs, sleeps, info


class Tests(unittest.TestCase):
    def test_streams_text(self):
        used, text, logs, _, info = run(FakeModelClient(answer="one two three"))
        self.assertEqual((used, text, logs), ("primary", "one two three", []))
        self.assertEqual(info["usage"]["outputTokens"], 3)

    def test_retries_then_recovers(self):
        used, text, logs, sleeps, _ = run(ThrottlingClient(FakeModelClient(answer="ok"), {"primary": 2}))
        self.assertEqual(used, "primary")
        self.assertEqual(len(logs), 2)
        self.assertEqual(sleeps, [0.5, 1.0])  # exponential: base * 2**attempt, jitter fixed at 1.0

    def test_falls_back(self):
        inner = FakeModelClient(answer="ok")
        used, _, logs, _, _ = run(ThrottlingClient(inner, {"primary": 99}))
        self.assertEqual(used, "fallback")
        self.assertTrue(any("[fallback]" in m for m in logs))
        self.assertEqual(inner.calls, ["fallback"])

    def test_gives_up(self):
        with self.assertRaises(ClientError):
            run(ThrottlingClient(FakeModelClient(), {"primary": 99, "fallback": 99}))

    def test_no_retry_on_validation_error(self):
        class Bad:
            def converse_stream(self, **kw):
                raise ClientError({"Error": {"Code": "ValidationException", "Message": "bad"}}, "ConverseStream")
        with self.assertRaises(ClientError):
            run(Bad())

    def test_mid_stream_failure_is_not_retried(self):
        class Breaks:
            def converse_stream(self, **kw):
                def gen():
                    yield {"contentBlockDelta": {"delta": {"text": "half"}}}
                    raise ClientError({"Error": {"Code": "ThrottlingException", "Message": "x"}}, "ConverseStream")
                return {"stream": gen()}
        with self.assertRaises(StreamBroken):
            run(Breaks())

    def test_jitter_is_capped(self):
        self.assertLessEqual(backoff_delay(20, rng=lambda: 1.0), 8.0)


if __name__ == "__main__":
    unittest.main()
