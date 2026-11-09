# Lecture 12.4 demo: a CloudWatch dashboard for tokens, latency and cost

This is the code for the demo in Lecture 12.4. You deploy one CloudWatch dashboard that shows how a Bedrock model is used: calls, input and output tokens, latency, throttles and errors, and an estimated cost. Two alarms tell you when Bedrock throttles you or gets slow. Then you send traffic with `load.py` and watch the numbers arrive.

**Cost:** a few cents. The dashboard, two alarms and an SNS topic cost very little, and the traffic is a few dozen calls to a small model. **Teardown:** `cdk destroy`.

## What gets deployed

- **Dashboard** `genai-tokens-latency-cost`, over the `AWS/Bedrock` metrics for one model ID:
  - totals for the selected time range: calls, tokens, estimated cost, and alarm status
  - graphs: calls, tokens in and out, latency (average and p90, with the alarm threshold), throttles and errors, estimated cost per 5 minutes, estimated cost per call
  - optionally, a **Logs Insights** widget that adds up tokens by caller from your model invocation logs
- **Alarms**: `genai-demo-throttles` (any throttle in 5 minutes) and `genai-demo-latency` (average latency above the threshold in 2 of 3 periods)
- **SNS topic** for the alarms, with an optional email subscription

Nothing here touches your application. The dashboard only reads metrics that Bedrock already publishes.

## Settings

All settings are CDK context values in `cdk.json`. Change them there, or pass `-c key=value` to `cdk deploy`.

| Key | Default | What it is |
| --- | --- | --- |
| `model_id` | `us.amazon.nova-micro-v1:0` | The model ID, or inference profile ID, that your app calls. Bedrock reports metrics under the ID you call with, so if you call through an inference profile, use the profile ID here. |
| `price_in_per_1k` | `0.000035` | **Example** price per 1,000 input tokens, in USD. Replace it with the current on-demand price for your model and Region from the Amazon Bedrock pricing page. |
| `price_out_per_1k` | `0.00014` | **Example** price per 1,000 output tokens, in USD. Replace it too. |
| `latency_alarm_ms` | `5000` | Average latency, in milliseconds, that triggers the latency alarm. |
| `alert_email` | empty | Your email address, if you want alarm emails. You confirm the subscription from the email AWS sends you. |
| `invocation_log_group` | empty | The CloudWatch Logs group of your model invocation logs. Leave it empty to skip the Logs Insights widget. |

The cost widgets are an **estimate**: tokens times the prices you entered. They don't include discounts, batch or cached-token pricing, or anything outside the model calls. Your bill, or Cost Explorer, is the real number.

## Before you start

- Your account is set up as in Lecture 1.3, including the AWS CDK. Bootstrap the account and Region once with `cdk bootstrap`.
- Your account can use the model in `model_id` in your Region. The default is Amazon Nova Micro through the US inference profile, so use a US Region such as `us-east-1`, or change the ID.
- Optional, for the Logs Insights widget: turn on **model invocation logging** in the Bedrock console (Settings), with CloudWatch Logs as a destination, and note the log group name. It's off by default.

## Steps

1. Install and deploy:

   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   cdk deploy
   ```

   With alarm emails and the invocation log widget:

   ```bash
   cdk deploy -c alert_email=you@example.com -c invocation_log_group=<your-log-group>
   ```

   Open the `DashboardUrl` output. The graphs are empty until there's traffic.

2. Send some traffic:

   ```bash
   python load.py
   ```

   It sends 30 calls, one at a time, and prints the total tokens and latency for the run, plus an estimated cost with the same prices as the dashboard.

3. Wait a few minutes, then refresh the dashboard. Expect the calls and token counts to match what `load.py` printed, and the cost widget to match its estimate.

4. Make the answers longer and watch output tokens, latency and cost go up together:

   ```bash
   python load.py --max-tokens 800
   ```

5. Push harder to try to see throttling:

   ```bash
   python load.py --calls 100 --threads 16
   ```

   Whether you get throttled depends on your account's quotas, so you may not. If you do, `load.py` retries with backoff and jitter, the throttle graph shows them, and the throttle alarm goes into `ALARM`.

## Things to notice

- **Tokens are the cost.** The cost per call graph moves with output tokens, which is why capping `maxTokens` is a cost control.
- **Average hides the slow calls.** Compare the average and p90 lines on the latency graph. Users feel the p90.
- **A throttle is a signal, not just an error.** Retries with backoff hide it from users, but the dashboard still shows it, and it tells you when to ask for a higher quota, spread load across Regions with cross-Region inference, or buy Provisioned Throughput.
- **Metrics give totals, logs give detail.** The metrics can't tell you which team or user spent the tokens. Invocation logs can, which is what the Logs Insights widget shows.

## If it fails

| Problem | Fix |
| --- | --- |
| CDK says the bootstrap stack is missing | Run `cdk bootstrap` once for this account and Region, then deploy again. |
| `load.py` returns `AccessDeniedException` or `ValidationException` | Check that your account can use the model in this Region. Some models must be called through an inference profile ID, such as `us.<model-id>`. |
| The dashboard stays empty | Wait a few minutes after the traffic, and check the time range. Then check that `model_id` is exactly the ID `load.py` called with, because metrics are published per model ID. |
| The Logs Insights widget shows nothing | Check that model invocation logging is on, that it writes to CloudWatch Logs, and that `invocation_log_group` is that log group in this Region. |
| No alarm email | Confirm the SNS subscription from the email AWS sent you. |

## Teardown

```bash
cdk destroy
```

This removes the dashboard, the alarms and the SNS topic. If you turned on model invocation logging only for this lab, turn it off again in the Bedrock console, and delete the log group if you don't need it.
