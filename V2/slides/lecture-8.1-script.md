# Lecture 8.1: Hosting choices and right-sizing — narration script

Section 8, Deployment and enterprise integration. About 12 minutes. The same text is in the speaker notes of `lecture-8.1.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Hosting choices and right-sizing

(About 45 seconds)

Welcome to Section 8. / So far, / we've designed the solution, / prepared the data / and written the prompts. / Now, / we put it into production, / and connect it to the systems your company already runs. [pause] In this first lecture, / I'll show you why hosting a large model is different, / the ways to run a model on Amazon Bedrock, / when SageMaker AI makes more sense, / and how to size the whole thing. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Pick the **platform** first, / then the **way to pay**, / and size it with **numbers**, / not guesses. [long pause]

Transition: So, / why is hosting a large model different?

## 2. Hosting an LLM isn't hosting a web app

(About 1 min 45 seconds)

If you've hosted web apps, / some of your instincts won't work here. / Four things are different. [pause]

▶ CLICK

First, / **GPU memory**. / The model's weights have to fit in it, / and on top of that, / there's the **KV cache**. / That's the memory each request uses for the tokens it's working on, / and it grows with every token in flight. / Run out of it, / and requests slow down or fail.


▶ CLICK

Second, / **latency per token**. / A web request has one latency. / A model has two. / The time to the **first** token, / and then the tokens per second after that. / So a long answer simply takes longer.


▶ CLICK

Third, / **long cold starts**. / Loading gigabytes of weights onto a GPU takes minutes, / not milliseconds. / So scaling from zero / isn't something you want on a live chat path.


▶ CLICK

And fourth, / **concurrency**. / The GPU works on many requests at once, / in batches. / More requests per batch means more throughput, / but each one can wait a bit longer. / That's the trade-off you're tuning. [long pause]

Transition: So, / how does Amazon Bedrock handle all of that for you?

## 3. Four ways to run a Bedrock model

(About 1 min 45 seconds)

With Bedrock, / AWS runs the GPUs. / Your choice is **how** you use them. / And you've got four options. [pause]

▶ CLICK

**On-demand**. / You pay per input and output token, / on shared capacity. / Your limit is your quotas, / in requests and tokens per minute. / This is where almost everyone starts.


▶ CLICK

**Cross-Region inference**. / You call an **inference profile** instead of a single model, / and Bedrock spreads your requests across Regions in the same geography. / You get more throughput, / at the same price, / and your data stays in that geography.


▶ CLICK

**Provisioned Throughput**. / You buy **model units**, / billed by the hour, / and that capacity is yours. / You'll need it for many custom models, / for example a model you've fine-tuned.


▶ CLICK

And **batch inference**. / You put your prompts in a JSONL file in S3, / start a job, / and the results land back in S3. / It's priced lower than on-demand, / so it's the right answer for big jobs that can wait. [long pause]

Transition: But what if the model you need isn't in Bedrock at all?

## 4. When you host the model yourself

(About 2 min)

That's when you host it yourself, / on Amazon SageMaker AI. / You pick the instance, / and you choose how the endpoint behaves. [pause]

▶ CLICK

A **real-time endpoint** is always on, / on the GPU instance you pick. / For a large model, / that's the usual choice.


▶ CLICK

An **asynchronous endpoint** puts requests in a queue. / It handles big payloads and long processing, / and it can scale down to zero when nothing's waiting. / Great for jobs, / not for live chat.


▶ CLICK

A **serverless endpoint** sounds tempting, / but it doesn't give you GPUs. / So it suits small models, / not large language models. / Keep that one in mind.


▶ CLICK

Now, / two features make GPU hosting cheaper. / First, / **inference components**. / Several models share one endpoint, / and each one gets its own slice of GPUs, / with its own scaling. / So you're not paying for a whole instance per model.


▶ CLICK

And second, / the **large model inference containers**. / They come with serving engines such as vLLM, / and they can split one model across several GPUs / when it doesn't fit on one. [long pause]

Transition: So, / how do you choose between the two platforms?

## 5. Bedrock or SageMaker AI?

(About 1 min 30 seconds)

Four questions settle it. [pause]

▶ CLICK

First, / **the model you need**. / If it's in the Bedrock catalog, / Bedrock is the easy path. / If it's an open-weights model that isn't there, / or your own model, / SageMaker AI.


▶ CLICK

Second, / **who runs the servers**. / With Bedrock, / AWS does, / fully managed. / With SageMaker AI, / you pick the instances, / and you own the scaling.


▶ CLICK

Third, / **how you pay**. / Bedrock charges per token, / or per model unit. / SageMaker AI charges per instance hour, / whether you send it one request or a million.


▶ CLICK

So the **best fit**? / Bedrock for most applications, / and the fastest start. / SageMaker AI when you need full control, / or steady, / high volume that keeps a GPU busy. [long pause]

Transition: And whichever you pick, / how much capacity do you actually need?

## 6. Size it with numbers, not guesses

(About 1 min 45 seconds)

Here's how to size it with numbers. [pause]

▶ CLICK

First, / **tokens per second**. / Take your peak requests per second, / and multiply by the output tokens per request. / That's the throughput you have to deliver.


▶ CLICK

Second, / **concurrency**. / How many requests are in flight / at the busiest minute of the day? / That drives your quotas, / or your number of instances.


▶ CLICK

Third, / **cost per task**. / Don't compare prices per token. / Work out what **one answer** costs, / at your real volume. / That's the number your business cares about.


▶ CLICK

And fourth, / **load test**. / Replay real prompts, / at real volume, / and watch latency, / errors / and throttling.


▶ CLICK

And here's the rule of thumb. [pause] **Start on demand**. / Move to Provisioned Throughput, / or your own endpoint, / only when the numbers show steady, / high volume. [long pause]

Transition: Let's wrap up.

## 7. Lecture recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / hosting a large model is different. / GPU memory, / latency per token, / long cold starts, / and batched concurrency.


▶ CLICK

Second, / pick the platform, / then the way to pay. / Bedrock for most apps, / with on-demand, / cross-Region, / provisioned / or batch. / And SageMaker AI when you need full control.


▶ CLICK

And third, / right-size with numbers. / Tokens per second, / concurrency, / cost per task, / and then a load test. [pause]

So, / back to our one sentence. [pause] Pick the **platform** first, / then the **way to pay**, / and size it with **numbers**, / not guesses. [long pause]

Transition: In the next lecture, / we connect all of this to the systems your company already runs.
