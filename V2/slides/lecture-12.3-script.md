# Lecture 12.3: Observability for GenAI — narration script

Section 12, Cost, performance and monitoring. About 13 minutes. The same text is in the speaker notes of `lecture-12.3.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Observability for GenAI

(About 45 seconds)

Your app is fast, / and it doesn't cost a fortune. / But how do you **know** it stays that way, / at three in the morning, / with real users? [pause] That's what observability is for. [pause]

Here's the lecture in one sentence. [pause] Measure **six signals**, / see them with metrics, / logs / and traces, / and **alarm** before your users notice. [long pause]

Transition: So, / what should you actually measure?

## 2. Six signals for a GenAI app

(About 1 min 30 seconds)

A GenAI app needs the usual health checks, / plus a few of its own. / I watch six signals. [pause]

▶ CLICK

**Tokens**. / Input and output, / per model, / per app, / and per team. / Tokens are your bill, / so this is the first number to watch.


▶ CLICK

**Latency**. / Time to first token, / and total time. / And look at p50 and p95, / not just the average.


▶ CLICK

**Errors**. / Failed calls, / timeouts, / and tool calls that went wrong inside an agent.


▶ CLICK

**Throttles**. / Calls that were rejected / because you hit a quota. / A rising throttle count is an early warning / that you need more capacity.


▶ CLICK

**Cost**. / Spend per task, / per team, / and per model.


▶ CLICK

And **quality**. / User feedback, / evaluation scores, / and how often your guardrails block something. / An app can be fast, / cheap, / and completely wrong. [long pause]

Transition: The good news is, / Bedrock gives you a lot of this for free.

## 3. Built in, with no code to write

(About 1 min 30 seconds)

Bedrock publishes metrics to **CloudWatch** automatically. / You don't write any code. / They're in the **AWS/Bedrock** namespace, / and you can split them by model. [pause]

▶ CLICK

**Invocations**. / How many calls each model gets.


▶ CLICK

**InvocationLatency**. / How long each call takes, / from start to finish.


▶ CLICK

**InputTokenCount** and **OutputTokenCount**. / The tokens in and out. / This is the basis of your bill, / so it's the metric your cost dashboard is built on.


▶ CLICK

**InvocationThrottles**. / Calls rejected for going over a quota.


▶ CLICK

And the **client and server errors**. / Client errors mean something's wrong with your request. / Server errors mean something failed on the service side.


▶ CLICK

But remember. / Metrics tell you **that** something changed. / They don't tell you **why**. / For that, / you need logs and traces. [long pause]

Transition: So let's look at the logs first.

## 4. Every prompt and answer, on record

(About 1 min 30 seconds)

**Model invocation logging** records every request to Bedrock, / with the prompt / and the answer. [pause]

▶ CLICK

First, / you **turn it on**. / It's a Bedrock setting, / per account and per Region, / and it's **off** by default. / So if nobody turned it on, / you have no record.


▶ CLICK

You can send the logs to **CloudWatch Logs**. / That's great for recent requests, / because you can search them with Logs Insights.


▶ CLICK

And you can send them to **Amazon S3**. / That's the place for large payloads, / like images, / and for long history at low cost.


▶ CLICK

Then you **analyze** them. / For logs in S3, / you can query them with **Athena**. / For example, / find every request that hit max tokens last week.


▶ CLICK

But be careful. / These logs hold **real** prompts and **real** answers. / That can include personal data. / So encrypt them, / limit who can read them, / and keep only what you need. [long pause]

Transition: Logs show you single calls. / But a real request often makes many calls.

## 5. Follow one request from end to end

(About 1 min 30 seconds)

A RAG app or an agent does several things for one question. / **Tracing** lets you follow that one request / from end to end. [pause]

▶ CLICK

**X-Ray** and **OpenTelemetry** give you the trace. / You see each step, / the retrieval, / the model call, / the tool call, / and how long each one took. / So when a request is slow, / you see exactly which step was slow.


▶ CLICK

CloudWatch also has **generative AI observability**. / It gives you ready-made views / of model calls, / agents / and traces, / right in the CloudWatch console. / So you don't have to build those views yourself.


▶ CLICK

And if your agents run on **AgentCore**, / **AgentCore Observability** captures their sessions, / traces / and spans, / and sends them to CloudWatch.


▶ CLICK

One tip. / **Add your own attributes** to your traces. / Things like the prompt version, / the model, / and the tenant. / Later, / when quality drops, / you can slice by prompt version / and see exactly which change caused it. [long pause]

Transition: There's one more component people forget to watch.

## 6. Watch the part that feeds the model

(About 1 min 15 seconds)

In a RAG app, / the vector store feeds the model. / If it's slow or out of date, / everything downstream suffers. [pause]

▶ CLICK

So watch **OpenSearch health**. / Search latency, / CPU and memory, / and indexing errors. / And if you use OpenSearch Serverless, / watch the capacity units it uses, / because that's also your cost.


▶ CLICK

Watch your **ingestion jobs**. / Is the knowledge base sync finishing? / Did any documents fail to ingest? / A failed sync means the model answers from old data.


▶ CLICK

And watch **retrieval results**. / How often does a search return nothing useful, / or only low scores? / That's often the first sign / that users are asking about something you haven't indexed.


▶ CLICK

Because a slow / or stale index / makes a good model / give bad answers. [long pause]

Transition: And that brings us to the hardest signal of all. / Quality.

## 7. Healthy isn't the same as good

(About 1 min 30 seconds)

Your dashboards can be green, / and your answers can still be bad. / Healthy isn't the same as good. / So here's how to watch quality in production. [pause]

▶ CLICK

**User feedback**. / Log the thumbs up and thumbs down **with** the trace. / Then, / when someone says an answer was bad, / you can see exactly what happened.


▶ CLICK

**Sampled evaluation**. / Take a sample of real traffic, / and score it with a judge model, / every day or every week. / You can't review everything, / but you can review a sample.


▶ CLICK

**Guardrail blocks**. / Bedrock Guardrails publishes metrics too. / They show how often inputs and outputs are blocked. / A sudden jump can mean an attack, / or a filter that's too strict.


▶ CLICK

And **drift**. / Compare your scores over time. / A sudden drop is easy to spot. / A slow decline over weeks / is the one that's easy to miss. [long pause]

Transition: Finally, / none of this helps / if nobody looks at it in time.

## 8. Know before your users do

(About 1 min 30 seconds)

You want to know about a problem / **before** your users tell you. / That's what alarms are for. [pause]

▶ CLICK

Start with **thresholds**. / A CloudWatch alarm on p95 latency, / on errors, / on throttles, / and on sudden spikes in tokens.


▶ CLICK

Then add **anomaly detection**. / CloudWatch learns what normal looks like, / including daily patterns, / and flags anything unusual. / That's useful for token usage, / where a fixed threshold is hard to pick.


▶ CLICK

When an alarm fires, / **notify** someone. / **Amazon SNS** sends the alert to your on-call team, / by email, / chat / or a paging tool.


▶ CLICK

And make it easy to **roll back**. / If you manage your prompt or model choice with a flag in **AppConfig**, / you can switch back to the last good version / in seconds, / without a redeploy.


▶ CLICK

And finally, / put it all on **one dashboard**. / That's exactly what we'll build in the next lecture. [long pause]

Transition: Let's wrap up.

## 9. Lecture recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / measure **six signals**. / Tokens, / latency, / errors, / throttles, / cost, / and quality.


▶ CLICK

Second, / use all three views. / Bedrock **metrics** in CloudWatch, / model invocation **logging**, / and **traces** for every step of a request.


▶ CLICK

And third, / **alarm and act**. / Watch retrieval and quality too, / and get an alarm / before your users notice. [pause]

So, / back to our one sentence. [pause] Measure **six signals**, / see them with metrics, / logs / and traces, / and **alarm** before your users notice. [long pause]

Transition: In the next lecture, / we'll build a CloudWatch dashboard / for tokens, / latency / and cost, / step by step.
