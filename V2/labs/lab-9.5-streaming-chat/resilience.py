"""Retries, backoff with jitter, and model fallback for Bedrock ConverseStream.

Three layers, from inside out:
1. botocore's own retries (adaptive mode) on the initial request.
2. Our backoff-with-jitter loop around the whole streaming call.
3. A fallback model when the primary keeps throttling.
"""
import random
import time

import boto3
from botocore.config import Config
from botocore.exceptions import ClientError

RETRYABLE = {"ThrottlingException", "ServiceUnavailableException", "InternalServerException",
             "ModelNotReadyException"}


def make_client(region, max_attempts=3):
    """Bedrock runtime client with adaptive retry mode.

    Adaptive mode retries throttling and transient errors with exponential backoff, and also
    slows the client down on its own when it keeps getting throttled.
    """
    cfg = Config(region_name=region, retries={"mode": "adaptive", "max_attempts": max_attempts},
                 read_timeout=120, connect_timeout=10)
    return boto3.client("bedrock-runtime", config=cfg)


def error_code(err):
    if isinstance(err, ClientError):
        return err.response.get("Error", {}).get("Code", "")
    return ""


def is_retryable(err):
    return error_code(err) in RETRYABLE


def backoff_delay(attempt, base=0.5, cap=8.0, rng=random.random):
    """Full jitter: a random wait between 0 and min(cap, base * 2**attempt) seconds."""
    return rng() * min(cap, base * (2 ** attempt))


class StreamBroken(Exception):
    """The stream failed after text was already shown. Retrying would repeat the answer."""


def stream_text(client, model_id, messages, system=None, max_tokens=512, temperature=0.5):
    """Yield text pieces from ConverseStream as they arrive, then a final dict with usage."""
    kwargs = {"modelId": model_id, "messages": messages,
              "inferenceConfig": {"maxTokens": max_tokens, "temperature": temperature}}
    if system:
        kwargs["system"] = [{"text": system}]
    resp = client.converse_stream(**kwargs)
    stop_reason = None
    for event in resp["stream"]:
        if "contentBlockDelta" in event:
            text = event["contentBlockDelta"]["delta"].get("text")
            if text:
                yield text
        elif "messageStop" in event:
            stop_reason = event["messageStop"].get("stopReason")
        elif "metadata" in event:
            yield {"usage": event["metadata"].get("usage", {}),
                   "latencyMs": event["metadata"].get("metrics", {}).get("latencyMs"),
                   "stopReason": stop_reason}


def chat_with_resilience(client, models, messages, on_text, system=None, retries_per_model=3,
                         sleep=time.sleep, log=print, rng=random.random):
    """Stream one answer. Retry with backoff, then fall back to the next model.

    models: list of model IDs, primary first.
    on_text: called with each text piece, so the caller can print it as it arrives.
    Returns (model_id_used, info_dict).
    """
    last_err = None
    for model_id in models:
        for attempt in range(retries_per_model):
            started = False
            try:
                info = {}
                for piece in stream_text(client, model_id, messages, system=system):
                    if isinstance(piece, dict):
                        info = piece
                    else:
                        started = True
                        on_text(piece)
                return model_id, info
            except ClientError as err:
                last_err = err
                if started:
                    # Text is already on screen. Don't retry silently and repeat it.
                    raise StreamBroken(f"stream failed mid-answer: {error_code(err)}") from err
                if not is_retryable(err):
                    raise
                wait = backoff_delay(attempt, rng=rng)
                log(f"[retry] {model_id}: {error_code(err)} on attempt {attempt + 1}/{retries_per_model}, "
                    f"waiting {wait:.2f}s")
                sleep(wait)
        log(f"[fallback] {model_id} kept failing, trying the next model")
    raise last_err
