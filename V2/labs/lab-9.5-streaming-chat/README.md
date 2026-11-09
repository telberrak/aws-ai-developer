# Lab 9.5: streaming chat with retries

A terminal chat on Amazon Bedrock that prints the answer as it streams in, and stays up when the model is throttled.

It shows three layers of resilience, from inside out:

1. **botocore retries** in `adaptive` mode, set on the client with `max_attempts`.
2. **Backoff with full jitter** around the whole streaming call (`resilience.py`).
3. **A fallback model** when the primary keeps throttling.

It also shows one rule that's easy to miss: **don't retry once text is on screen.** If the stream breaks mid-answer, a silent retry would repeat the answer, so the app reports the error instead.

## Files

| File | What it does |
|---|---|
| `chat.py` | The chat loop: streams with ConverseStream, prints time to first token, total time and token counts. |
| `resilience.py` | `make_client` (adaptive retries), `backoff_delay` (full jitter), `chat_with_resilience` (retry, then fall back). |
| `fakes.py` | Offline stand-ins: a fake streaming model and a wrapper that throws `ThrottlingException` on demand. |
| `test_resilience.py` | Offline tests. No AWS calls, no waiting. |

## Prerequisites

- Python 3.10 or later.
- For the online steps: AWS credentials, and model access in your Region for the primary and fallback models. The defaults are the US cross-Region inference profiles for Amazon Nova Lite (`us.amazon.nova-lite-v1:0`) and Nova Micro (`us.amazon.nova-micro-v1:0`) in `us-east-1`. Use any two text models you have access to with `--model` and `--fallback-model`.
- Your identity needs `bedrock:InvokeModelWithResponseStream` on both models (and the inference profiles).

## Setup

```bash
cd V2/labs/lab-9.5-streaming-chat
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m unittest -v          # 7 offline tests, all should pass
```

## Steps

1. **Offline first.** No AWS calls:
   ```bash
   python chat.py --offline --once "What does streaming buy me?"
   ```
   Words appear one by one, then a line with the model, time to first token and total time.

2. **Stream from Bedrock.**
   ```bash
   python chat.py
   ```
   Ask a question that needs a long answer. Compare *first token* with *total*: the user starts reading long before the answer is complete. Type `exit` to quit.

3. **Throttling that recovers.**
   ```bash
   python chat.py --simulate-throttle 2
   ```
   The first two calls to the primary model throw `ThrottlingException` before they reach AWS. You'll see two `[retry]` lines with growing, random waits, then the answer from the primary model.

4. **Throttling that doesn't recover.**
   ```bash
   python chat.py --simulate-throttle always
   ```
   After its retries, the app logs `[fallback]` and the answer comes from the fallback model. The status line names the model that answered.

5. **Look at the code.** In `resilience.py`, find `started`: once any text has been shown, a failure raises `StreamBroken` instead of retrying.

## What to notice

- **Time to first token** is the latency the user feels. Streaming doesn't make the whole answer faster; it makes the wait shorter.
- **Simulated throttles skip botocore.** They're thrown by `ThrottlingClient` before any request, so you see only our retry loop. Real throttling is retried by botocore first (adaptive mode, up to `max_attempts`), and only then reaches our loop.
- **Full jitter** spreads retries out, so many clients that were throttled together don't all retry at the same moment.
- **Fallback is a product decision.** The fallback model may be cheaper and weaker. Log which model answered, as the status line does.

## Troubleshooting

| Problem | Fix |
|---|---|
| `AccessDeniedException` | Turn on model access for both models in the Region, and check your IAM permissions include `bedrock:InvokeModelWithResponseStream`. |
| `ValidationException` about the model ID | The model needs an inference profile ID (such as `us.amazon.nova-lite-v1:0`), or isn't in your Region. |
| Real `ThrottlingException` that never clears | You've hit your account quota. Lower the request rate, use cross-Region inference, or ask for a quota increase. |
| Nothing prints until the end | Your terminal buffers output. Run with `python -u chat.py`. |

## Cost and cleanup

Nothing is deployed. The online steps cost a fraction of a cent per question with Nova Lite or Micro. The offline steps cost nothing. To clean up, deactivate and delete the `.venv` folder.

## Going further

- Serve the stream to a browser: wrap `stream_text` in a FastAPI endpoint that returns Server-Sent Events, or use API Gateway WebSockets with a Lambda function that posts each chunk to the connection.
- Add a circuit breaker: after several fallbacks in a row, go straight to the fallback model for a minute before trying the primary again.
