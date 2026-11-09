"""Lecture 12.4 demo: a CloudWatch dashboard for tokens, latency and cost.

One stack, GenAIDashboardDemo, with:
- a CloudWatch dashboard over the AWS/Bedrock metrics for one model ID
- an estimated cost widget built with metric math from per-1K-token prices
- two alarms (throttles and latency) that notify an SNS topic
- optionally, a Logs Insights widget over your model invocation logs

Settings come from CDK context (cdk.json, or -c key=value on the command line).
The prices in cdk.json are EXAMPLE values. Replace them with the current
on-demand prices for your model and Region from the Amazon Bedrock pricing page.
"""
import aws_cdk as cdk
from aws_cdk import Duration
from aws_cdk import aws_cloudwatch as cw
from aws_cdk import aws_cloudwatch_actions as cw_actions
from aws_cdk import aws_sns as sns
from aws_cdk import aws_sns_subscriptions as subs
from constructs import Construct

PERIOD = Duration.minutes(5)

# Same defaults as cdk.json, so the app also synths when run without the CDK CLI.
DEFAULTS = {
    "model_id": "us.amazon.nova-micro-v1:0",
    "price_in_per_1k": 0.000035,   # EXAMPLE price per 1K input tokens, replace it
    "price_out_per_1k": 0.00014,   # EXAMPLE price per 1K output tokens, replace it
    "latency_alarm_ms": 5000,
    "alert_email": "",
    "invocation_log_group": "",
}


class GenAIDashboardStack(cdk.Stack):
    def __init__(self, scope: Construct, cid: str, **kwargs) -> None:
        super().__init__(scope, cid, **kwargs)
        def ctx(key: str):
            value = self.node.try_get_context(key)
            return DEFAULTS[key] if value is None else value

        model_id = ctx("model_id")
        # Written as plain decimals (no 3.5e-05), which metric math and the dashboard text both read cleanly.
        price_in = format(float(ctx("price_in_per_1k")), ".10f").rstrip("0").rstrip(".")
        price_out = format(float(ctx("price_out_per_1k")), ".10f").rstrip("0").rstrip(".")
        latency_ms = float(ctx("latency_alarm_ms"))
        email = ctx("alert_email") or ""
        log_group = ctx("invocation_log_group") or ""

        def metric(name: str, stat: str = "Sum", label: str | None = None) -> cw.Metric:
            # Bedrock publishes runtime metrics in the AWS/Bedrock namespace, per ModelId.
            # When you call through an inference profile, the ModelId dimension is the profile ID.
            return cw.Metric(
                namespace="AWS/Bedrock",
                metric_name=name,
                dimensions_map={"ModelId": model_id},
                statistic=stat,
                period=PERIOD,
                label=label or name,
            )

        invocations = metric("Invocations")
        tokens_in = metric("InputTokenCount", label="Input tokens")
        tokens_out = metric("OutputTokenCount", label="Output tokens")
        latency_avg = metric("InvocationLatency", "Average", "Latency avg (ms)")
        latency_p90 = metric("InvocationLatency", "p90", "Latency p90 (ms)")
        throttles = metric("InvocationThrottles", label="Throttles")
        client_err = metric("InvocationClientErrors", label="Client errors")
        server_err = metric("InvocationServerErrors", label="Server errors")

        # Estimated cost = tokens / 1000 * price per 1K tokens, per period.
        cost = cw.MathExpression(
            expression=f"(tin / 1000) * {price_in} + (tout / 1000) * {price_out}",
            using_metrics={"tin": tokens_in, "tout": tokens_out},
            label="Estimated cost (USD)",
            period=PERIOD,
        )
        cost_per_call = cw.MathExpression(
            expression=f"IF(calls > 0, ((tin / 1000) * {price_in} + (tout / 1000) * {price_out}) / calls, 0)",
            using_metrics={"tin": tokens_in, "tout": tokens_out, "calls": invocations},
            label="Estimated cost per call (USD)",
            period=PERIOD,
        )

        # Alarms, both notifying one SNS topic.
        topic = sns.Topic(self, "AlertTopic", display_name="GenAI dashboard demo alerts")
        if email:
            topic.add_subscription(subs.EmailSubscription(email))

        throttle_alarm = cw.Alarm(
            self, "ThrottleAlarm",
            alarm_name="genai-demo-throttles",
            alarm_description=f"Bedrock is throttling {model_id}.",
            metric=throttles,
            threshold=1,
            comparison_operator=cw.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            evaluation_periods=1,
            treat_missing_data=cw.TreatMissingData.NOT_BREACHING,
        )
        latency_alarm = cw.Alarm(
            self, "LatencyAlarm",
            alarm_name="genai-demo-latency",
            alarm_description=f"Average latency for {model_id} is above {latency_ms:.0f} ms.",
            metric=latency_avg,
            threshold=latency_ms,
            comparison_operator=cw.ComparisonOperator.GREATER_THAN_THRESHOLD,
            evaluation_periods=3,
            datapoints_to_alarm=2,
            treat_missing_data=cw.TreatMissingData.NOT_BREACHING,
        )
        for alarm in (throttle_alarm, latency_alarm):
            alarm.add_alarm_action(cw_actions.SnsAction(topic))

        dash = cw.Dashboard(
            self, "Dashboard",
            dashboard_name="genai-tokens-latency-cost",
            default_interval=Duration.hours(3),
        )
        dash.add_widgets(
            cw.TextWidget(
                markdown=f"# GenAI: tokens, latency and cost\nModel: `{model_id}` · Cost uses example prices "
                f"(${price_in}/1K input, ${price_out}/1K output). Replace them with your real prices.",
                width=24, height=2,
            )
        )
        dash.add_widgets(
            cw.SingleValueWidget(title="Calls", metrics=[invocations], width=6, height=4, set_period_to_time_range=True),
            cw.SingleValueWidget(title="Tokens", metrics=[tokens_in, tokens_out], width=6, height=4, set_period_to_time_range=True),
            cw.SingleValueWidget(title="Estimated cost (USD)", metrics=[cost], width=6, height=4, set_period_to_time_range=True),
            cw.AlarmStatusWidget(title="Alarms", alarms=[throttle_alarm, latency_alarm], width=6, height=4),
        )
        dash.add_widgets(
            cw.GraphWidget(title="Calls", left=[invocations], width=8, height=6),
            cw.GraphWidget(title="Tokens in and out", left=[tokens_in, tokens_out], width=8, height=6, stacked=True),
            cw.GraphWidget(title="Latency (ms)", left=[latency_avg, latency_p90],
                           left_annotations=[cw.HorizontalAnnotation(value=latency_ms, label="Alarm threshold")],
                           width=8, height=6),
        )
        dash.add_widgets(
            cw.GraphWidget(title="Throttles and errors", left=[throttles, client_err, server_err], width=8, height=6),
            cw.GraphWidget(title="Estimated cost per 5 minutes (USD)", left=[cost], width=8, height=6),
            cw.GraphWidget(title="Estimated cost per call (USD)", left=[cost_per_call], width=8, height=6),
        )
        if log_group:
            # Needs model invocation logging turned on, with CloudWatch Logs as a destination.
            dash.add_widgets(
                cw.LogQueryWidget(
                    title="Tokens by caller (model invocation logs)",
                    log_group_names=[log_group],
                    query_lines=[
                        "fields identity.arn as caller, input.inputTokenCount as tin, output.outputTokenCount as tout",
                        "stats count(*) as calls, sum(tin) as inputTokens, sum(tout) as outputTokens by caller",
                        "sort inputTokens desc",
                    ],
                    width=24, height=6,
                )
            )

        cdk.CfnOutput(self, "DashboardName", value=dash.dashboard_name)
        cdk.CfnOutput(
            self, "DashboardUrl",
            value=f"https://{self.region}.console.aws.amazon.com/cloudwatch/home?region={self.region}#dashboards/dashboard/{dash.dashboard_name}",
        )
        cdk.CfnOutput(self, "AlertTopicArn", value=topic.topic_arn)


app = cdk.App()
GenAIDashboardStack(app, "GenAIDashboardDemo")
app.synth()
