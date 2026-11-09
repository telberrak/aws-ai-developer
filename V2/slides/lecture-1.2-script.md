# Lecture 1.2: Amazon Bedrock, its APIs and pricing — narration script

Section 2, GenAI on AWS essentials. About 10 minutes. The same text is in the speaker notes of `lecture-1.2.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Amazon Bedrock, its APIs and pricing

(About 40 seconds)

In this lecture, / we meet the service you'll use more than any other in this course. / Amazon Bedrock. [pause] I'll cover what Bedrock gives you, / the four ways to call a model, / how you pay for it, / and when SageMaker AI is the better fit. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] **Start** with Bedrock, / and only move to SageMaker AI / when you have a **specific** reason. [long pause]

Transition: So, / what is Bedrock, / really?

## 2. Many foundation models, one serverless API

(About 2 min)

Bedrock is a fully managed, / serverless service / that gives you foundation models through one API. / No servers. / No GPUs to manage. / You send a request, / you get an answer. [pause]

▶ CLICK

Inside, / you'll find models from several providers. / Amazon's own Nova and Titan models, / Anthropic, / Meta, / Mistral AI, / Cohere, / and more. / And the list keeps growing.


▶ CLICK

Those models come in different types. / Text and chat. / Multimodal. / Embeddings. / Image generation. / And rerankers, / which you'll meet when we talk about retrieval.


▶ CLICK

Now, / before your first call works, / four things have to be in place. / First, / the **Region**. / Not every model is offered in every Region.


▶ CLICK

Second, / **model access**. / The model has to be available to your account in the Bedrock console.


▶ CLICK

Third, / **IAM**. / Your role needs permission to invoke the model.


▶ CLICK

And fourth, / the right **ID**. / Some models are called with a plain model ID. / Others need an **inference profile** ID, / which we'll come back to in a minute. [pause] And if you ever get an access denied error, / it's almost always number two or number three. / Model access, / or IAM. [long pause]

Transition: So, / once that's in place, / how do you actually call a model?

## 3. Four ways to call a model

(About 2 min)

There are four ways to call a model in Bedrock, / and each one fits a different job. [pause]

▶ CLICK

**Converse**. / This is your default. / One request shape that works across models, / so you can switch from one model to another / without rewriting your code. / It also handles multi-turn chat, / system prompts / and tool use.


▶ CLICK

**ConverseStream**. / Same thing, / but the answer comes back token by token, / as it's written. / That's what makes a chat app feel fast, / because the user sees the first words straight away.


▶ CLICK

**InvokeModel**. / The older, / lower-level call. / You send each provider's own native request body. / You'll still use it for things like embeddings, / and there's a streaming version too.


▶ CLICK

And a **batch inference job**. / You put thousands of prompts in a file in S3, / start a job, / and the results land back in S3. / No one's waiting, / so it's cheaper.


▶ CLICK

And one detail that trips people up. / There are two clients. / **bedrock-runtime** is for calling models, / so Converse, / InvokeModel, / all of that. / And **bedrock**, / without runtime, / is for managing things. / Listing models, / creating jobs, / setting up custom models. [long pause]

Transition: Now, / let's talk about money.

## 4. Four ways to pay, one way to pay less

(About 2 min)

You've got four main ways to pay for model calls, / plus one trick to pay less. [pause]

▶ CLICK

**On-demand**. / You pay per token, / with no commitment. / This is the default, / and it's right for variable or unpredictable traffic.


▶ CLICK

**Batch**. / Discounted compared with on-demand, / but it's offline. / You use it when nobody's waiting for the answer. / Overnight summaries, / classifying a big backlog, / that kind of thing.


▶ CLICK

**Provisioned Throughput**. / You buy model units by the hour, / with a commitment, / and you get guaranteed capacity. / It's for steady, / high-volume traffic. / And some custom models / can **only** be served this way.


▶ CLICK

**Cross-Region inference**. / Here, / you call an **inference profile** / instead of a single model in a single Region. / Bedrock then routes your request across several Regions. / So you get more capacity for bursts, / and better resilience. / And that's why some models ask for an inference profile ID.


▶ CLICK

And the trick. / **Prompt caching**. / If many requests start with the same long prefix, / like a big system prompt or a document, / Bedrock can cache it. / You pay less for those tokens, / and you get the answer faster. [long pause]

Transition: So, / Bedrock covers a lot. / But when should you use SageMaker AI instead?

## 5. Default to Bedrock, unless you need control

(About 2 min 30 seconds)

Let's compare them side by side, / on four points. [pause]

▶ CLICK

**Infrastructure**. / Bedrock is serverless. / SageMaker AI runs on instances / that you choose and manage.


▶ CLICK

**Models**. / Bedrock gives you a curated catalog. / SageMaker AI lets you run almost anything. / Models from JumpStart, / or a model you've built yourself.


▶ CLICK

**Customization**. / Bedrock gives you managed fine-tuning. / SageMaker AI gives you full control. / Your own training code, / techniques like LoRA, / your own pipelines.


▶ CLICK

**Pricing**. / Bedrock charges per token. / SageMaker AI charges per instance-hour, / whether the instance is busy or not.


▶ CLICK

So here's the rule. / Default to **Bedrock**. / It's the lowest operational effort. / And only move to SageMaker AI when you have a real reason. / The model isn't in Bedrock. / You need control over the hardware or the container. / You run your own fine-tuning pipeline and model registry. / Or a small, / task-specific model is simply cheaper to run. [pause] And one more thing. / If you've fine-tuned a model somewhere else, / **Custom Model Import** lets you bring it into Bedrock, / and still call it serverlessly. [long pause]

Transition: Let's wrap up.

## 6. Recap

(About 45 seconds)

So, / let's bring it together. [pause]

▶ CLICK

First, / Bedrock is serverless access to many foundation models. / Before your first call, / check the Region, / model access, / IAM / and the right model or inference profile ID.


▶ CLICK

Second, / Converse is your default call, / ConverseStream for live chat, / InvokeModel for native requests like embeddings, / and batch jobs for offline work.


▶ CLICK

And third, / pay on-demand for variable traffic, / batch when nobody's waiting, / Provisioned Throughput for steady volume, / and cross-Region inference for bursts. / And use SageMaker AI only when you need the control. [pause]

So, / back to our one sentence. [pause] **Start** with Bedrock, / and only move to SageMaker AI / when you have a **specific** reason. [long pause]

Transition: In the next lecture, / we'll look at the four architecture patterns / you'll build with these models.
