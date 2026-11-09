# Section 4: Selecting and Configuring FMs — narration script

One block per slide, in deck order. The same text is in the speaker notes of `section-04-selecting-and-configuring-fms.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. Lines starting "Transition:" are the spoken bridge into the next slide.

## Lecture 4.1: evaluating and choosing foundation models

### Slide 1: Selecting and configuring FMs

(About 80 seconds)

Welcome to Section 4. [pause] In Section 3, / we designed whole solutions. Now / we zoom in on the most **important** part of any of them: / the foundation model. [long pause]

This section answers five practical questions. How do you choose the right model, / with **evidence** rather than hype? How do you switch models later / without rewriting code? How do you keep running / when a model or a Region has problems? When should you customize a model, / with fine-tuning or adapters? And how do you version, / deploy / and roll back a custom model safely? [pause]

There are two labs. In Lab 2, / you'll build a model router that keeps its target model in configuration, / and switch models live without a redeploy. In Lab 3, / you'll add a circuit breaker that fails over **automatically**. [long pause]

This first lecture is about choosing a model, / in four steps: / what to compare, / where the evidence comes from, / a simple method, / and right-sizing. [pause] If I had to sum up this lecture in one sentence, / it would be this: / benchmarks build the shortlist, / but **your own data** picks the winner. [long pause]

Transition: So, / let's start with the six things that decide the choice.

### Slide 2: Six things decide the model

(About 95 seconds)

Six things decide which foundation model you pick. [pause] And in an exam scenario, / usually only one or two of them really matter.

First, / **capability**. How well does it reason, / write code, / follow instructions, / call tools, / or handle the languages you need?

Second, / **modality**. Can it take what you have, / and produce what you need? Text only, / text and images, / whole documents, / or vectors from an embedding model? [pause]

Third, / **context length**. How much input and output fits in one request? A model with a small context window / can't take a two-hundred-page contract, / no matter how clever it is.

Fourth, / **latency**. How fast is the first token, / and how many tokens per second does it produce? That matters a lot for chat, / and very little for an overnight batch job.

Fifth, / **price**. What do input and output tokens cost, / or what does a model unit cost? Larger models usually cost much more per token. [pause]

And sixth, / **limits**. Which Regions offer it? What are the quotas? How is your data handled? And where is the model in its lifecycle? A model that's marked as **legacy** / is a poor choice for a new application. [pause]

So when you read an exam question, / find the one or two deciding factors first. [long pause]

Transition: Now, / knowing what to compare is one thing. Let's look at where the evidence comes from.

### Slide 3: Benchmarks shortlist, your data decides

(About 85 seconds)

Here's the rule for this slide: / benchmarks shortlist, / **your data** decides. [long pause]

There are four sources of evidence. **Public benchmarks** give you a rough idea of general ability, / on things like reasoning or coding tests. They're useful for building a shortlist. But they may say little about your task, / your data / or your language.

**Provider model cards** tell you the context length, / the modalities, / the limits / and the intended uses. Read them. [pause] But remember who wrote them.

Then there's a way to run evaluation jobs on **your own** prompts. You can score with automatic metrics, / with a model acting as a judge, / or with human reviewers, / and compare several models side by side. That's **Amazon Bedrock model evaluation**. It does need a good dataset.

And your own test set, / the one from your proof of concept, / is the **strongest** evidence of all. It measures quality, / latency and cost / on the real work. Yes, / it takes effort to build. [pause]

On the exam, / an answer that evaluates candidate models on representative company data / beats an answer that just picks the best public benchmark score. [long pause]

Transition: So, / let's turn that evidence into a method you can actually follow.

### Slide 4: Choose a model in five steps

(About 85 seconds)

Choosing a model works best as a simple method / in five steps. [pause]

Step one: / filter on **hard limits**. If a model can't take your modality, / can't fit your context, / isn't in your Region, / or breaks your data rules, / it's out. However good it is.

Step two: / shortlist **two or three** candidates, / using the model cards and public benchmarks.

Step three: / run your test set against each one. Score the quality, / and record the latency and the token usage. [pause]

Step four: / compare cost **per task**, / not cost per token. Here's the thing. A cheaper model that needs a long prompt and two retries / can cost more per answer / than a pricier model that gets it right first time. So multiply by your real volume. [long pause]

Step five: / decide, / and plan to **revisit**. New models arrive on Bedrock regularly, / and older ones move to legacy status. Keep your test set, / so re-evaluating takes an afternoon, / not a project. [pause]

And that last step is why the next lecture matters. If switching models needs code changes, / you won't switch, / even when a better option appears. [long pause]

Transition: But first, / one more part of choosing well: / not buying more model than you need.

### Slide 5: Bigger isn’t always better

(About 85 seconds)

A big part of choosing well / is **not over-buying**. Bigger isn't always better. [pause]

For narrow, / high-volume tasks, / like classifying a ticket, / routing a request / or extracting fields, / a **small**, fast model is usually enough. It's far cheaper, / and quicker.

For chat on retrieved documents, / a **mid-size** model often works well. The retrieved context carries the facts, / so the model mostly needs to read and summarize.

For complex reasoning, / multi-step planning / or difficult code, / a **large** model earns its price. [pause]

And for search and retrieval, / you don't want a text-generation model at all. You want a model that turns text into vectors: / an **embedding** model.

A pattern you'll see on the exam, / and in real systems, / is **tiering**. A small model handles every request first, / and only the hard ones go to a large model. Bedrock also offers **intelligent prompt routing**, / which can route between models in the same family / based on the prompt. Either way, / you pay large-model prices / only when you need large-model quality. [long pause]

So, / back to our one sentence: / benchmarks build the shortlist, / but your own data picks the winner. [long pause]

Transition: Now you've chosen a model. In the next lecture, / we'll make sure you can **change** that choice later / without touching your code.

## Lecture 4.2: switching models without code changes

### Slide 6: Switching models without code changes

(About 35 seconds)

Lecture 4.2. [pause] A better or cheaper model arrives, / or yours is marked for retirement. How painful is the switch? [pause]

If the model ID is hard-coded, / it means code changes, / testing / and a redeploy everywhere. So we'll see the problem, / then build a model abstraction layer / with API Gateway, / Lambda / and AWS AppConfig, / with code.

If I had to sum up this lecture in one sentence, / it would be this: / keep the model choice in **configuration**, / not in code. [long pause]

Transition: So, / let's compare two ways to build this.

### Slide 7: A hard-coded model is a hidden cost

(About 70 seconds)

A hard-coded model is a **hidden cost**. Let's compare two ways to build this. [pause]

On the left, / the hard-coded way. The model ID, / the temperature / and the max tokens / live in the code. Changing models means editing code, / running tests / and redeploying. And often in **several** applications, / because every team calls Bedrock its own way. [pause]

On the right, / the abstracted way. Applications call **one** internal API / that simply means "generate an answer". Behind it, / a router reads the model choice and its settings / from configuration. So switching, / testing a new model on a slice of traffic, / or rolling back / becomes a configuration change / that takes **minutes**. [long pause]

And there's another benefit. The router is **one** place to add logging, / cost tracking, / guardrails and fallbacks, / instead of every team reinventing them.

When an exam question says the company wants to change models or providers / **without modifying application code**, / it's pointing straight at this pattern. [long pause]

Transition: So, / let's open up that router / and look at its four parts.

### Slide 8: A model router in four parts

(About 80 seconds)

The pattern has four parts, / and each one has a single job. [pause]

First, / the applications. They all call **one** internal endpoint. Something has to check who's calling, / limit how fast they call, / and give everyone one stable request and response contract. That's **Amazon API Gateway**.

Next, / API Gateway invokes a Lambda function: / the **router**. The router reads its configuration. Which model to use, / with which settings, / maybe different models for different use cases. Then it calls Bedrock. [pause]

Here's what makes this easy: / the **Converse API**. Converse uses one request shape for every chat model. So the router can switch models / just by changing the model ID, / with no other code changes. [long pause] And if you also need models from outside Bedrock, / the router is where you'd add an adapter for each provider, / behind the same contract.

Finally, / the configuration lives in **AWS AppConfig**, / and the router reads it at run time. That's the piece that turns a model switch / into a deployment of configuration, / not code. [pause]

Transition: Now, / you might ask: / why AppConfig, / and not just an environment variable? Let's look at that.

### Slide 9: Why AppConfig, not an environment variable

(About 80 seconds)

AppConfig gives you four things / that an environment variable doesn't. [pause]

First, / **validation**. AppConfig can check every new configuration / against a JSON schema, / or a Lambda validator, / before it's deployed. So a typo in a model ID gets rejected, / instead of breaking production.

Second, / **gradual rollout**. Deployment strategies roll a change out over time. Applications pick up the new configuration gradually, / so a problem shows up on a small share of traffic first. [pause]

Third, / **automatic rollback**. You can attach CloudWatch alarms to the environment. If an alarm fires during a deployment, / for example on errors or latency, / AppConfig rolls back to the previous configuration. [pause]

And fourth, / **no redeploy**. Changing a Lambda environment variable / is an update to the function itself. With AppConfig, / the function code and configuration don't change at all. It just reads the new values. And the AppConfig Lambda extension caches the configuration locally, / so reading it on every request / stays fast and cheap. [long pause]

Validated, / gradual, / reversible, / and decoupled from code. [pause] That's why it's the exam's answer. [long pause]

Transition: So, / let's see what this looks like in a few lines of code.

### Slide 10: The router reads, then calls

(About 80 seconds)

In practice, / it's a small JSON document / and a few lines of code. [pause]

The AppConfig profile, / here called model-routing, / has a **default** route, / with a model ID and settings. And it can have **named** routes for specific use cases. Here, / summarization goes to a smaller, / cheaper model.

The router reads the configuration. That read is **cached**, / so it doesn't call AppConfig on every request. It picks the route for this use case, / or the default. Then it calls Converse / with the model ID and settings from that route. [pause]

To switch the default model for every application, / you create a new version of the JSON / with a different model ID, / and deploy it through AppConfig. No code changes. No Lambda deployment. [pause] And if the new model misbehaves, / you roll back the configuration. [long pause]

You'll build exactly this in **Lab 2**, / deploy it with the AWS CDK, / and switch models live / while calling the API. The full code is in the course repo.

So, / back to our one sentence: / keep the model choice in configuration, / not in code. [long pause]

Transition: But switching doesn't help / if the model is failing. So, / next lecture: / resilience.

## Lecture 4.3: designing for resilience

### Slide 11: Designing for resilience

(About 30 seconds)

Lecture 4.3. [pause] Models get throttled. Regions have incidents. Models are retired. A production GenAI app has to keep working, / or fail **gracefully**. [pause]

We'll cover the failure modes, / then three tools: / Bedrock cross-Region inference, / a Step Functions circuit breaker, / and a graceful degradation plan.

If I had to sum up this lecture in one sentence, / it would be this: / decide in advance / what happens when a call **fails**. [long pause]

Transition: So, / first, / the four failure modes.

### Slide 12: Four ways a model call fails

(About 65 seconds)

There are four ways a model call fails, / and each one has a matching tool. [pause]

First, / **throttling**. Every account has quotas for each model in each Region. Go over them, / and calls fail with a throttling exception. The first defense is retries with exponential backoff and jitter, / and the AWS SDKs give you that.

Second, / **regional disruption**. Occasionally, / a service has problems in one Region. If all your calls go to that Region, / you go down with it. [pause]

Third, / **limited availability**. Not every model is offered in every Region. And a popular model can be short of capacity in one Region / at peak times.

And fourth, / a **slow or failing** model. Latency can spike, / or a model can return errors again and again. If you keep sending every request to it, / every user waits, / and then fails. [long pause]

Transition: So, / let's look at the tools, / starting with one that lets Bedrock spread the load for you.

### Slide 13: Let Bedrock spread the load

(About 80 seconds)

The first tool lets Bedrock spread your load / across several Regions. It's called **Amazon Bedrock cross-Region inference**. [pause]

Instead of calling a model with its plain model ID, / you call it with an **inference profile** ID. The profile defines a set of Regions, / for example within one geography, / like the US or Europe. Bedrock then sends each request / to a Region in that set / that has capacity.

You get higher throughput, / and resilience against capacity problems in a single Region. And there's no change to your code / beyond the ID. It's also how you use some models / that aren't offered in your own Region. [pause]

One thing to check. Your data may be processed in **any** Region in the profile. So if the scenario has strict data residency requirements, / choose a profile whose Regions stay within the allowed geography. [long pause]

On the exam, / watch for three signals: / throttling during peaks, / a model with limited Regional availability, / or a need for higher throughput without managing infrastructure. [pause] Cross-Region inference is very often the answer. [long pause]

Transition: But what if one model keeps failing anyway? That's where the second tool comes in.

### Slide 14: Stop calling what is failing

(About 85 seconds)

The second tool stops you calling something that's **failing**. It's a classic resilience pattern called a **circuit breaker**, / and the exam names it specifically with Step Functions. [pause]

The circuit has three states.

**Closed** is normal. Requests go to the primary model.

When failures cross a threshold, / say five errors in a minute, / the circuit **opens**. While it's open, / requests skip the primary entirely / and go straight to a fallback. That could be the same model through a cross-Region inference profile, / or a different model. So users stop waiting / for calls that are going to fail. [long pause]

After a cool-down period, / the circuit goes **half-open**. A few requests are allowed through to the primary / as a test. If they succeed, / the circuit closes again. If they fail, / it opens again. [pause]

On AWS, / a common build is a Step Functions workflow / that checks the circuit state stored in a **DynamoDB** table, / calls the primary or the fallback, / and updates the state when calls fail. Step Functions gives you retries, / error catching / and branching, / without writing that logic yourself. You'll build it in **Lab 3**. [long pause]

Transition: And when even the fallback isn't enough, / you need a plan. That's the third tool.

### Slide 15: Plan what happens when all else fails

(About 80 seconds)

The third tool is a **graceful degradation** plan. It's a ladder of fallbacks, / from least to most noticeable for the user. [pause]

First, / retry with exponential backoff. That handles short bursts of throttling, / and the user barely notices.

Second, / fail over. To a cross-Region inference profile, / to a deployment in another Region, / or to another model with similar quality.

Third, / use a **smaller** model. It's faster, / cheaper / and usually more available. The answers may be a bit less polished, / but the user still gets help. [pause]

Fourth, / serve from a **cache**. For common questions, / you may already have a good answer stored.

And finally, / tell the user honestly. Show a clear message, / and offer to queue the request / or hand them to a human. [long pause]

Which brings us back to our one sentence: / decide in advance / what happens when a call fails. Then the system follows the plan automatically. An exam option that just shows an error page / is rarely the best answer / when the scenario asks for **continuous** operation. [long pause]

Transition: So far, / we've used models as they are. In the next lecture, / we'll look at changing the model itself.

## Lecture 4.4: customizing foundation models

### Slide 16: Customizing foundation models

(About 40 seconds)

Lecture 4.4. [pause] Remember the ladder from Section 2: / prompt engineering, / then RAG, / then fine-tuning. Most problems stop at the first two rungs. But sometimes / the model itself must behave differently. A specialized vocabulary, / a strict output style, / or a cheap narrow task on a small model. [pause]

We'll compare the options, / LoRA, / and see where custom models run.

If I had to sum up this lecture in one sentence, / it would be this: / customize **only** when prompting and RAG aren't enough. [long pause]

Transition: Here are three ways to change the model.

### Slide 17: Three ways to change the model

(About 80 seconds)

There are three main ways / to change the model itself. [pause]

**Fine-tuning** trains the model further on labeled examples: / pairs of a prompt and the ideal answer. It's how you teach a specific task, / an output format / or a style. You might need hundreds to thousands / of high-quality examples.

**Continued pre-training** uses large amounts of unlabeled text from your domain. Things like medical notes, / legal contracts / or internal engineering documents. It teaches the model the language and background knowledge of that domain, / rather than a specific task. And it needs much more data and compute. [pause]

**Parameter-efficient** fine-tuning, / with techniques like LoRA and adapters, / is a cheaper form of fine-tuning. Instead of updating all of the model's weights, / you train a small set of extra weights. More on that on the next slide.

A related option is **distillation**. A large model generates training data / to teach a smaller model to do a narrow task well. Bedrock supports model distillation for some models. [long pause]

The exam usually tests one difference: / fine-tuning versus continued pre-training. [pause] **Labeled** task examples, / versus **unlabeled** domain text. [long pause]

Transition: Now, / let's look closer at LoRA, / because that's where customization gets cheap.

### Slide 18: Train a little, keep the base model

(About 80 seconds)

LoRA lets you train a **little**, / and keep the base model. LoRA stands for low-rank adaptation. Here's the idea / without the math. [pause]

A foundation model has billions of weights. Full fine-tuning updates **all** of them. That takes a lot of GPU memory and time, / and it produces a whole new copy of the model.

LoRA freezes the original weights, / and trains a small set of extra weights / that adjusts the model's behavior. We call that an **adapter**. And it's tiny, / compared with the model. [pause]

That gives you three big advantages. It's **small**, / so training is faster and cheaper. It's **swappable**. You keep one base model, / and train a separate adapter per task, / per department / or per customer. And it's **efficient to serve**. Many adapters can share one endpoint and its GPUs, / loading the right adapter for each request, / instead of hosting a full model copy for every variant. [long pause]

So when an exam scenario wants several customized variants of one model / with low hosting cost, / or customization with limited compute, / think parameter-efficient methods / like LoRA. [long pause]

Transition: So, / you've customized a model. Where does it actually run?

### Slide 19: Bedrock or SageMaker AI for custom models

(About 85 seconds)

Custom models run in one of two places, / depending on how much **control** you need. [pause]

In **Amazon Bedrock**, / you can run managed customization jobs / for the models that support them, / pointing at training data in S3. You can also bring in a model you customized elsewhere / with **Custom Model Import**, / for supported architectures. To serve a customized model, / Bedrock has often required **Provisioned Throughput**. But on-demand options exist for some models, / and serving options change often, / so check the current documentation. [pause]

In **Amazon SageMaker AI**, / you have full control. You can fine-tune any open model with any technique, / including LoRA, / using training jobs or JumpStart. You deploy to endpoints you size yourself. And with **inference components**, / one endpoint can host a base model plus many adapters, / scaling each one separately. [long pause]

Rule of thumb: / Bedrock when you want it managed / and your model is supported. SageMaker AI when you need control over the technique or the hardware, / or you're serving many adapters on shared infrastructure.

And remember our one sentence: / customize only when prompting and RAG aren't enough. [long pause]

Transition: But a custom model isn't a one-off. So, / in the next lecture, / we'll manage it / from release to retirement.

## Lecture 4.5: lifecycle management for custom models, then Labs 2 and 3

### Slide 20: Lifecycle management

(About 35 seconds)

Lecture 4.5. [pause] You'll retrain a custom model as data changes, / and one day replace it. Without discipline, / nobody knows what's in production, / or how to undo a bad release. [pause]

We'll cover versioning with SageMaker Model Registry, / automated deployment, / rollback, / and retirement, / including base models. Then Labs 2 and 3.

If I had to sum up this lecture in one sentence, / it would be this: / every version **traceable**, / every release **reversible**. [long pause]

Transition: So, / let's start with the registry.

### Slide 21: Every version, its status, its history

(About 80 seconds)

You need one place that knows every model version, / its status / and its history. That's **SageMaker Model Registry**, / the catalog of your models. [pause]

Each customized model belongs to a **model package group**. Every time you train, / you register a new version in that group, / along with its evaluation metrics / and where its artifacts are stored.

Each version has an **approval status**. New versions start as pending manual approval. A reviewer, / or an automated test, / sets it to approved / or rejected. [pause]

And approval is the trigger for deployment. An approved version can automatically start the deployment pipeline, / for example through an **Amazon EventBridge** rule / that reacts to the status change. [pause]

The result is that the registry becomes the **source of truth**. You can always answer: / which version is in production? Who approved it? What were its metrics? And what was the version **before** it? [pause] That last question is the key to rollback. [long pause]

On the exam, / when a scenario needs versioning, / approval workflows / or traceability for customized models, / the answer is SageMaker Model Registry. [long pause]

Transition: Now, / let's see the pipeline that feeds the registry.

### Slide 22: From new data to production, safely

(About 75 seconds)

An automated pipeline takes a model from new data to production, / **safely**, / and the same way every time. [pause]

It starts when new training data arrives, / or when the training code changes. That kicks off a **SageMaker Pipelines** run.

The pipeline trains the new version / and evaluates it on a held-out test set, / comparing it against the version currently in production.

It registers the new version **only** if it beats the quality bar. So a worse model never even becomes a candidate. [pause]

Then it's approved. Automatically for low-risk changes, / or by a reviewer for sensitive ones.

And then it's deployed **gradually**, / with canary or linear traffic shifting and alarms. More on that on the next slide. [long pause]

The value of the pipeline is **consistency**. Every model goes through the same steps, / with the same checks, / and every step is recorded. Exam scenarios that mention frequent retraining, / manual errors in deployments, / or the need for repeatable releases / are asking for this. [long pause]

Transition: So, / let's look at that last step, / and how you make every release reversible.

### Slide 23: Make every release reversible

(About 75 seconds)

Every model release should be **reversible**. And SageMaker AI gives you deployment guardrails for endpoints / that do this for you. [pause]

First, / **blue/green** deployment. The new version is deployed on a new fleet, / alongside the old one. Traffic moves to the new fleet, / and the old fleet stays ready / until you're sure.

Second, / **traffic shifting**. With canary, / a small share of traffic, / say ten percent, / goes to the new version first. After a baking period, / the rest follows. With linear, / traffic moves in equal steps. [pause]

Third, / **alarm-based rollback**. You attach CloudWatch alarms, / for example on errors, / latency / or a model quality metric. If an alarm fires during the deployment, / SageMaker rolls the traffic back to the old version / **automatically**.

And fourth, / keep the last good version. Because every version is in the registry, / you always know what to roll back to. [long pause]

On the exam, / when a scenario asks to minimize the impact of a bad model update, / look for gradual traffic shifting / with automatic rollback on alarms. [long pause]

Transition: And the last stage of the lifecycle / is the one people forget: / retirement.

### Slide 24: Models have an end of life too

(About 80 seconds)

Models have an end of life too. And retirement applies in **two** directions. [pause]

First, / the base models you depend on. In Amazon Bedrock, / models have a lifecycle: / **active**, / then **legacy**, / then **end of life**, / when they can no longer be called. AWS publishes the dates in advance. Track them. Because an application calling a model that reaches end of life / will simply stop working. [long pause]

Second, / your own model versions. Retire old versions in the registry, / archive their artifacts, / and keep their metrics and lineage. That way, / you can answer audit questions later / about what was running, / and when.

And then, / be ready for migration. This is where the whole section comes together. If your model choice lives in AppConfig, / and you keep your evaluation test set, / then moving off a retiring model is **routine**. Test the replacement, / update the configuration, / roll it out gradually, / and watch the alarms. [pause]

So that's the whole section in one breath. Choose with evidence. Switch through configuration. Survive failures. Customize carefully. And manage every version / from release to retirement. [long pause]

Transition: Now, / let's make some of this real with the labs, / starting with Lab 2.

### Slide 25: Switch models live, with no redeploy

(About 80 seconds)

In Lab 2, / you'll build the model router from Lecture 4.2, / and switch models live, / with **no** redeploy. [pause]

First, / deploy the stack with the AWS CDK. It creates an API Gateway endpoint, / the Lambda router, / and an AppConfig application / with a JSON configuration profile / holding the model ID and settings.

Second, / call the API a few times. Each response includes the model ID that answered, / so you can see which model is in use. [pause]

Third, / switch the model. Create a new version of the configuration / with a different model ID, / and deploy it through AppConfig / with the script in the lab folder. You won't touch the Lambda code, / and you won't redeploy the stack. [pause]

Fourth, / call the API again. Within a short time, / as the router's cache refreshes, / the responses come from the **new** model. Then roll back to the original configuration / the same way. [long pause]

The lab costs a few cents in model calls. When you're done, / run cdk destroy / to remove everything. Honestly, / that's the step people skip. [pause]

Transition: Next, / Lab 3, / where you'll watch a circuit breaker fail over on its own.

### Slide 26: Fail over automatically

(About 75 seconds)

In Lab 3, / you'll build the circuit breaker from Lecture 4.3, / and watch it fail over **automatically**. [pause]

Deploy the stack with the CDK. It creates a Step Functions workflow, / a DynamoDB table that stores the circuit state, / and a Lambda function that calls Bedrock / with whichever model ID it's given.

Run the workflow normally first. Requests use the primary model / with its in-Region model ID, / and the circuit stays **closed**. [pause]

Then simulate failures. The workflow input has a flag / that makes the primary call fail. Run it several times, / and watch the failure count rise in DynamoDB / until the circuit **opens**. [pause]

Now watch the failover. With the circuit open, / the workflow skips the primary / and calls the fallback, / a cross-Region inference profile. In the Step Functions console, / you can see exactly which path each run took. [long pause]

After the cool-down time passes, / the circuit lets the primary be tried again. And when it succeeds, / the circuit closes.

A few cents again, / and cdk destroy at the end. [pause]

Transition: So, / that's both labs done. Let's wrap up the section.

### Slide 27: Take the quiz, then prepare your data

(About 80 seconds)

That's the end of Section 4. Let's recap, / quickly. [pause]

You choose a model on six things: / capability, / modality, / context length, / latency, / price / and limits. Benchmarks shortlist, / your own test set decides, / and you compare cost **per task**, / not per token.

You keep the model choice in AWS AppConfig, / behind a Lambda router. So switching models is a validated, / gradual, / reversible configuration change. [pause]

You stay up with retries, / cross-Region inference, / a Step Functions circuit breaker / and a graceful degradation plan. You customize with fine-tuning, / continued pre-training / or LoRA adapters, / on Bedrock or SageMaker AI. And you manage custom models with Model Registry, / automated pipelines, / gradual deployment with automatic rollback, / and planned retirement. [pause]

And back to the one sentence from this last lecture: / every version traceable, / every release reversible. [long pause]

Your next step is the **twelve-question** quiz for this section, / and Labs 2 and 3 / if you haven't done them yet.

Transition: Then join me in Section 5, / where we prepare the data that goes into foundation models: / validating it, / processing text, / images and audio, / and formatting it the way each model expects. See you there.
