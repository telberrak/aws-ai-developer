# Lecture 12.2: Latency, throughput and parameter tuning — narration script

Section 12, Cost, performance and monitoring. About 12 minutes. The same text is in the speaker notes of `lecture-12.2.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Latency, throughput and parameter tuning

(About 45 seconds)

In the last lecture, / we followed the money. / Now let's talk about **speed**. / How fast does your app feel, / how many users can it serve at once, / and how do you prove it before launch? [pause]

Here's the whole lecture in one sentence. [pause] Users feel the **first token**, / so stream it, / shrink the tokens and the model, / and prove it with a load test at **real** peak. [long pause]

Transition: First, / what do we even mean by latency?

## 2. Time to first token, then the rest

(About 1 min 30 seconds)

When you call a model, / there are really two waits. [pause]

▶ CLICK

The first is **time to first token**. / The model reads your whole prompt, / and only then starts writing. / So the bigger the input, / the longer this wait.


▶ CLICK

The second is **generation time**. / The model writes one token after another, / at a certain number of tokens per second. / A longer answer takes longer, / and a bigger model usually writes more slowly.


▶ CLICK

Add them up, / and you get **total latency**. / Time to first token, / plus generation time.


▶ CLICK

And here's why that split matters. / A person in a chat window feels the **first token**. / A batch job or an API caller waits for the **total**. / So when a requirement says "fast", / ask which one it means. [long pause]

Transition: And for users, / there's a simple trick that changes how fast it feels.

## 3. Same total time, but it feels faster

(About 1 min 15 seconds)

That trick is **streaming**. [pause]

▶ CLICK

On Bedrock, / you call **ConverseStream** instead of Converse. / The model sends text back in chunks as it writes, / instead of one big response at the end.


▶ CLICK

So what does the user see? / Words start appearing within a second or two. / And the wait feels much shorter, / even when it isn't.


▶ CLICK

Because here's what **doesn't** change. / The total time, / the total tokens, / and the total cost. / Streaming improves how it **feels**, / not what it costs.


▶ CLICK

To push those chunks all the way to a browser, / you need a channel that stays open. / Use **WebSockets** through API Gateway, / or a Lambda function URL with **response streaming**. [long pause]

Transition: Streaming hides the wait. / Now let's actually make it shorter.

## 4. Five ways to cut latency

(About 1 min 30 seconds)

Here are five ways to cut latency for real. [pause]

▶ CLICK

First, / a **smaller model**. / Smaller models write more tokens per second. / It's often the biggest single win.


▶ CLICK

Second, / **fewer input tokens**. / A shorter prompt and fewer chunks mean less to read before the first token. / And prompt caching helps here too, / because the model doesn't reprocess the cached prefix.


▶ CLICK

Third, / **fewer output tokens**. / Lower the max tokens, / and ask for short, / structured answers. / Fewer tokens to write / means less time writing.


▶ CLICK

Fourth, / **latency-optimized inference**. / For selected models, / in some Regions, / Bedrock offers a faster way to serve them. / The list changes, / so check what's available for your model.


▶ CLICK

And fifth, / **work in parallel**. / If two calls don't depend on each other, / run them at the same time. / Same for retrieval. / Don't wait in line when you don't have to. [long pause]

Transition: Now, / a question that comes up all the time. / What do the inference settings do to speed?

## 5. What each setting really changes

(About 1 min 30 seconds)

Let's go through the main settings, / and what each one **really** changes. [pause]

▶ CLICK

**Temperature** controls randomness. / Keep it low for facts and code, / and raise it for creative ideas. / But it has **no** real effect on speed or cost.


▶ CLICK

**Top-p** and **top-k** limit which next tokens the model can pick from. / Again, / that shapes the answer, / not the speed.


▶ CLICK

**Max tokens** is different. / It's a hard cap on how long the answer can be. / A lower cap means a shorter answer, / so it's **faster and cheaper**.


▶ CLICK

And **stop sequences** end the answer at a marker you choose. / The model stops writing right there, / so again, / shorter and cheaper.


▶ CLICK

So remember it like this. / Tune **temperature** for quality. / Tune **max tokens** for speed and cost. [long pause]

Transition: So far we've talked about one request. / What happens when thousands arrive at once?

## 6. When too many requests arrive at once

(About 1 min 30 seconds)

At scale, / the question changes. / It's not how fast one call is, / it's how many you can run. [pause]

▶ CLICK

Every model on Bedrock has **quotas**. / Requests per minute / and tokens per minute, / per model, / per Region.


▶ CLICK

Go over the quota, / and calls fail with a **throttling** error. / The fix in your code is to **retry with backoff and jitter**. / Wait a bit, / then a bit longer, / with some randomness, / so all your clients don't retry at the same moment.


▶ CLICK

For more headroom, / use **cross-Region inference**. / It spreads your requests across Regions in the same geography. / And if you expect a big launch, / ask for a **quota increase** early, / not on launch day.


▶ CLICK

And when you need **guaranteed** capacity, / that's **Provisioned Throughput**. / It makes sense when your volume is steady and high enough to justify paying by the hour. [long pause]

Transition: So how do you know your app will hold up? / You test it.

## 7. Prove it before launch

(About 1 min 30 seconds)

Never find your limits on launch day. / Find them with a load test. [pause]

▶ CLICK

Start with **real prompts**. / Replay real traffic, / with real input lengths and real answer lengths. / Toy questions give toy results.


▶ CLICK

Then **ramp up**. / Raise the number of concurrent users step by step, / until you reach your expected peak, / and a bit beyond.


▶ CLICK

**Measure** as you go. / Latency at p50, / p95, / and p99. / Tokens per second. / And how many throttles and errors you get.


▶ CLICK

And **watch** it in **CloudWatch**. / The Bedrock metrics there show you exactly where things start to break.


▶ CLICK

One more thing. / Size for **p95**, / not the average. / If one answer in twenty is painfully slow, / that's the one your users will remember. [long pause]

Transition: Let's wrap up.

## 8. Lecture recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / there are **two latencies**. / Time to first token is what users feel. / Total time is what jobs wait for.


▶ CLICK

Second, / to get faster, / stream the answer, / use a smaller model, / send and ask for fewer tokens, / and run independent work in parallel.


▶ CLICK

And third, / **know your limits**. / Quotas, / backoff, / cross-Region inference, / and a load test at real peak. [pause]

So, / back to our one sentence. [pause] Users feel the **first token**, / so stream it, / shrink the tokens and the model, / and prove it with a load test at **real** peak. [long pause]

Transition: In the next lecture, / we'll see how to keep an eye on all of this in production, / with **observability**.
