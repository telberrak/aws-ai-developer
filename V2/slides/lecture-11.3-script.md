# Lecture 11.3: Governance and compliance — narration script

Section 11, Security, privacy, governance and responsible AI. About 15 minutes. The same text is in the speaker notes of `lecture-11.3.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Governance and compliance

(About 50 seconds)

So far in this section, / we've locked down the workload, / and protected personal data. [pause] But one day, / someone will ask you to **prove** it. / An auditor, / a regulator, / or your own risk team. / That's **governance**. [pause]

Here's the one sentence for this lecture. [pause] **Document** the model, / **trace** every answer, / and **prove** it continuously. [long pause]

Transition: So, / what will that auditor actually ask you?

## 2. Four questions an auditor will ask

(About 1 min 30 seconds)

It usually comes down to four questions. [pause]

▶ CLICK

First, / **what is this model for?** / What it's meant to do, / and what it's not meant to do. / That's what **model cards** answer.


▶ CLICK

Second, / **where did it come from?** / Which data, / which code, / which base model. / That's **lineage**.


▶ CLICK

Third, / **why did it give this answer?** / One specific answer, / to one specific customer, / last Tuesday. / That's **traceability**.


▶ CLICK

And fourth, / **is it still compliant today?** / Not when you launched it, / but right now. / That's **continuous monitoring**. [pause] We'll take them one at a time. [long pause]

Transition: First, / documenting the model.

## 3. Model cards describe what a model is for

(About 2 min 15 seconds)

A model card is a short document / that describes a model in plain terms. / There are three kinds you should know. [pause]

▶ CLICK

**SageMaker Model Cards** are for the models **you** build or customize. / You record the intended use, / and the uses to avoid. / A risk rating. / How it was trained, / and how it scored in evaluation. / Model cards are versioned, / so you can see how they changed over time, / and you can export one as a PDF / to hand to an auditor.


▶ CLICK

**AWS AI Service Cards** come from AWS. / They cover AWS's own AI services and models. / For each one, / you get its intended uses, / its limitations, / and the design choices AWS made for responsible AI. / You don't write these. / You read them, / and you point to them.


▶ CLICK

And then there are **model provider cards**. / Each foundation model in Bedrock comes with documentation from the company that built it. / How it was trained, / what it's not good at, / and the risks they know about.


▶ CLICK

So the rule is simple. / **You document what you build.** / AWS and the model providers document what **they** build. / An auditor wants both, / because your app sits on top of their model. [long pause]

Transition: Next, / where did the model come from?

## 4. Trace a model back to its data

(About 2 min 15 seconds)

This matters most when you train or fine-tune your own model. / You need to trace it all the way back. [pause]

▶ CLICK

It starts with the **training data**. / A versioned dataset in S3, / so you know exactly which version you used.


▶ CLICK

Then the **training job**. / The code, / the settings, / and the base model it started from.


▶ CLICK

The result goes into the **Model Registry**. / Every version of the model is stored there, / with an **approval status**. / Pending, / approved, / or rejected. / That's your control point. / Someone has to sign off.


▶ CLICK

And then the **endpoint**, / which serves the approved version to real traffic.


▶ CLICK

**SageMaker ML Lineage Tracking** links all of these steps together. / So you can start at the endpoint, / and walk back to the exact data, / code / and approval behind it. [pause] And because only an **approved** version in the registry gets deployed, / nothing reaches production without a sign-off. [long pause]

Transition: That covers the model. / But what about a single answer?

## 5. Record what produced every answer

(About 2 min 15 seconds)

When a customer complains about one answer, / you need to rebuild exactly what produced it. / So for every call, / record five things. [pause]

▶ CLICK

The **model ID**, / down to the version. / Models get updated, / and you need to know which one answered.


▶ CLICK

The **prompt version**. / If you manage templates in Bedrock Prompt Management, / each version has its own ID. / So you know exactly which instructions the model had.


▶ CLICK

The **guardrail and its version**. / Which guardrail ran, / and whether it stepped in.


▶ CLICK

The **documents retrieved**. / If it's a RAG app, / record the Knowledge Base sources the answer cited. / A wrong answer often comes from a wrong document.


▶ CLICK

And finally, / **one request ID** that ties all of it together, / across your invocation logs and your own application logs. [pause] With that, / you can answer "why did it say that?" / in minutes, / not days. [long pause]

Transition: So far that's evidence after the fact. / But compliance has to hold every day.

## 6. Prove it continuously, not once a year

(About 2 min 15 seconds)

An audit once a year isn't enough. / Things drift. / Someone turns off logging, / or creates a bucket without encryption. / So you **prove it continuously**. [pause]

▶ CLICK

**AWS Config** checks every resource, / all the time, / against rules you choose. / Is encryption on? / Is logging on? / Is this endpoint reachable from the internet? / You can bundle rules into **conformance packs**, / and apply them across accounts.


▶ CLICK

**AWS Audit Manager** collects the evidence for you. / It maps what Config and CloudTrail see / to the controls in a framework. / And there's a ready-made framework for **generative AI** best practices. / So when the auditor arrives, / the evidence is already there.


▶ CLICK

**AWS Security Hub** gives you one place for findings. / Config, / Macie, / and many other services send their findings there.


▶ CLICK

And **EventBridge** and **CloudWatch** close the loop. / Alarm on a change, / and trigger an automatic fix. / Say someone turns off encryption. / EventBridge catches it, / and a Lambda function turns it back on. [long pause]

Transition: Before we wrap up, / one more question. / Who's responsible for what?

## 7. Who owns what

(About 1 min 30 seconds)

It's the shared responsibility model, / with one extra party. [pause]

▶ CLICK

**AWS** owns the infrastructure and the service itself. / Security **of** the cloud. / And for its own models, / it publishes the AI Service Cards.


▶ CLICK

The **model provider** owns how the base model was trained, / its built-in safety training, / and its model card.


▶ CLICK

And **you** own everything you add. / Your data, / your prompts / and your guardrails. / Who can call what. / And your use case, / its documentation / and its audit trail. [pause] So even when you use someone else's model, / the way you use it is **your** responsibility. [long pause]

Transition: Let's wrap up.

## 8. Lecture recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / **document the model**. / Model cards for what you build. / Service Cards and provider cards for the rest.


▶ CLICK

Second, / **trace data and answers**. / Lineage back to the training data, / and one request ID across every answer.


▶ CLICK

And third, / **prove it continuously**. / Config, / Audit Manager / and Security Hub, / every day, / not once a year. [pause]

So, / back to our one sentence. [pause] **Document** the model, / **trace** every answer, / and **prove** it continuously. [long pause]

Transition: Next, / we go beyond rules and audits, / to responsible AI. / Fairness, / transparency, / and building systems people can trust.
