# Lab 3: circuit breaker with Step Functions

Section 4, Lecture 4.3.

You build a circuit breaker. When the primary model keeps failing, requests fail over automatically to a cross-Region inference profile. After a cool-down, the primary is tried again.

**Estimated cost:** a few cents. **Teardown:** `cdk destroy`.

## What gets deployed

- **DynamoDB table** holding the circuit state: a failure count and an `openUntil` time
- **Step Functions workflow** `lab03-circuit-breaker`:
  1. Get the circuit state.
  2. If the circuit is open (`openUntil` is in the future), call the fallback.
  3. Otherwise call the primary model, retrying throttling with backoff.
  4. On success, close the circuit (reset the count).
  5. On failure, record it (opening the circuit at 3 failures for 60 seconds), then call the fallback.
- **Lambda functions**: [`invoke.py`](lambda/invoke.py) calls Bedrock Converse, and [`circuit.py`](lambda/circuit.py) updates the circuit state

## Before you start

- Setup from [`setup/README.md`](../../setup/README.md) is done, and the CDK is bootstrapped.
- Pick a **primary** model ID that works in your Region, and a **fallback** cross-Region inference profile ID for the same or a similar model. Find inference profiles in the Bedrock console, or with `aws bedrock list-inference-profiles`.

## Steps

1. Deploy:

   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   cdk deploy -c primaryModelId=[in-region-model-id] -c fallbackModelId=[cross-region-inference-profile-id]
   ```

2. Run normally with `./run.sh`. The output shows `"path": "primary"`.
3. Simulate failures with `./run.sh fail` three times. Each run fails on the primary, records a failure and answers from the fallback (`"path": "fallback"`). Check the table in the DynamoDB console: after the third run, `openUntil` is set.
4. While the circuit is open, run `./run.sh`, without `fail`. The workflow skips the primary entirely and goes straight to the fallback. You can see the path in the Step Functions console graph.
5. Wait 60 seconds and run `./run.sh` again. The circuit is half-open: the primary is tried, succeeds and closes the circuit.

## Things to notice

- Users always get an answer. Only the path changes.
- While the circuit is open, nobody waits for a primary call that's likely to fail.
- Retries handle short throttling. The circuit breaker handles sustained failure. They complement each other.

## Teardown

```bash
cdk destroy
```
