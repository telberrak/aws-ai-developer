# Lecture 2.5: Customizing models and managing their lifecycle — narration script

Section 3, Designing solutions and choosing models. About 10 minutes. The same text is in the speaker notes of `lecture-2.5.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Customizing models and managing their lifecycle

(About 40 seconds)

Sometimes a good prompt and good retrieval still aren't enough. / The model needs to **change**. [pause] In this lecture, / I'll cover the three ways to customize a model, / where a custom model runs, / and how you manage it over its whole life. / Versions, / approvals, / deployments, / rollbacks, / and finally, / retirement. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Customize **only** when you have to, / and treat every custom model like code. / Versioned, / approved / and **reversible**. [long pause]

Transition: So, / what are your options for changing a model?

## 2. Three ways to change the model

(About 2 min)

There are three ways to change what a model does, / and they differ in what you train it on. [pause]

▶ CLICK

**Fine-tuning**. / You train on **labeled** examples. / A prompt, / and the answer you want. / Hundreds or thousands of them. / You use it to teach a task, / a format, / or a style. / This is the behavior fix we talked about in Lecture 1.3.


▶ CLICK

**Continued pre-training**. / Here, / you train on a large amount of **unlabeled** text from your domain. / Medical notes, / legal contracts, / internal engineering docs. / No answers needed. / It teaches the model the language and knowledge of your field.


▶ CLICK

And **parameter-efficient fine-tuning**, / with techniques like LoRA and adapters. / Same labeled examples as fine-tuning, / but you only train a tiny set of extra weights. / So it's faster, / and much cheaper.


▶ CLICK

And one related option worth knowing. / **Distillation**. / A large model teaches a smaller one / to do one narrow task well. / You end up with a model that's cheaper and faster to run, / for that one job. [long pause]

Transition: Let's look closer at LoRA, / because it changes how you serve custom models.

## 3. Train a little, keep the base model

(About 1 min)

The idea behind LoRA and adapters is simple. / Train a little, / and keep the base model as it is. [pause]

▶ CLICK

It's **small**. / You train a tiny fraction of the weights, / so training is faster and cheaper.


▶ CLICK

It's **swappable**. / You keep one base model, / and you plug in a different adapter for each task, / or even for each customer.


▶ CLICK

And it's **efficient to serve**. / Many adapters can share the same endpoint and the same GPUs. / So instead of ten big endpoints for ten tasks, / you can run one. [long pause]

Transition: So, / once you have a custom model, / where does it actually run?

## 4. Bedrock or SageMaker AI

(About 1 min 30 seconds)

You've got the same two choices as before. / Bedrock, / or SageMaker AI. [pause] And a quick warning. / The serving options for custom models change often, / so always check the current documentation. [pause]

▶ CLICK

**Customizing**. / Bedrock runs managed customization jobs for the models that support it. / SageMaker AI lets you use any open model, / with any technique you like.


▶ CLICK

**Bringing your own model**. / In Bedrock, / that's Custom Model Import, / for supported model architectures. / In SageMaker AI, / it's any model you can put in a container.


▶ CLICK

**Serving**. / A custom model in Bedrock often needs **Provisioned Throughput**, / so plan for that cost. / In SageMaker AI, / it runs on endpoints, / and adapters can be served as inference components on a shared endpoint.


▶ CLICK

So which one is **best**? / Bedrock, / when you want it managed. / SageMaker AI, / when you need control, / or you're serving many adapters. [long pause]

Transition: Now, / a custom model has versions. / And versions need a home.

## 5. Every version, its status, its history

(About 1 min 30 seconds)

That home is the **SageMaker Model Registry**. / It keeps every version of a model, / its status, / and its history. [pause]

▶ CLICK

First, / you **train**. / A pipeline produces a new model version.


▶ CLICK

Then you **register** it. / It goes into a model package group, / with its version number and its evaluation metrics.


▶ CLICK

Then it waits for **approval**. / Its status is pending, / until a reviewer, / or an automated test, / approves it.


▶ CLICK

And approval triggers **deployment**. / The deployment pipeline picks up the approved version and ships it.


▶ CLICK

So the registry becomes your **single source of truth**. / What's approved, / what's in production, / and what you'd go back to if something breaks. [long pause]

Transition: So, / how do you get from new data to production, / without breaking anything?

## 6. From new data to production, safely

(About 1 min 15 seconds)

You automate it, / end to end, / with five steps. [pause]

▶ CLICK

First, / new data or new code / starts a **SageMaker Pipelines** run.


▶ CLICK

Second, / the pipeline trains the model and **evaluates** it. / And it compares it against the version that's in production right now.


▶ CLICK

Third, / it **registers** the new version, / but only if it beats the quality bar.


▶ CLICK

Fourth, / **approval**. / Automatically, / or by a person.


▶ CLICK

And fifth, / you **deploy gradually**. / A small share of traffic first, / with alarms watching. / Never everything at once. [long pause]

Transition: And if that gradual deployment goes wrong?

## 7. Make every release reversible

(About 1 min 15 seconds)

Then you roll back. / And the goal is simple. / Every release should be **reversible**. [pause]

▶ CLICK

**Blue/green**. / The new version runs on a new fleet. / If it fails, / you switch traffic straight back to the old one.


▶ CLICK

**Canary or linear**. / You shift a small share of traffic first, / then the rest, / step by step.


▶ CLICK

**Alarm-based rollback**. / CloudWatch alarms watch the deployment, / and if errors or latency go up, / the rollback happens **automatically**. / Nobody has to wake up.


▶ CLICK

And **keep the last good version**. / The registry knows exactly what to go back to. [long pause]

Transition: And finally, / every model, / even a good one, / reaches the end of its life.

## 8. Models have an end of life too

(About 1 min)

Models have an end of life too. / And you need a plan for it. [pause]

▶ CLICK

**Base models** on Bedrock / move through a lifecycle. / Active, / then Legacy, / then End-of-life. / Once a model is end-of-life, / calls to it stop working. / So watch for those notices.


▶ CLICK

**Your own models** need the same care. / Archive the old versions, / but keep their metrics and their lineage, / so you can always explain what ran, / and when.


▶ CLICK

And **be ready**. / Here's the good news. / If your model choice lives in configuration, / and you've got a test set, / a migration becomes routine. / You test the new model, / change one config value, / and you're done. / And that's exactly what we'll build in the next lecture. [long pause]

Transition: Let's wrap up.

## 9. Recap

(About 45 seconds)

So, / let's bring it together. [pause]

▶ CLICK

First, / three ways to change a model. / Fine-tuning on labeled examples, / continued pre-training on domain text, / and LoRA adapters to do it cheaply.


▶ CLICK

Second, / use Bedrock when you want it managed, / and SageMaker AI when you need control. / And plan for Provisioned Throughput.


▶ CLICK

And third, / manage the lifecycle. / Register and approve every version, / deploy gradually with alarms, / keep the last good version, / and plan for retirement. [pause]

So, / back to our one sentence. [pause] Customize **only** when you have to, / and treat every custom model like code. / Versioned, / approved / and **reversible**. [long pause]

Transition: In the next lecture, / we'll build a model router, / and switch models live, / without touching the code.
