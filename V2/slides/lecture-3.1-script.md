# Lecture 3.1: From requirements to a reviewed architecture — narration script

Section 3, Designing solutions and choosing models. About 12 to 13 minutes. The same text is in the speaker notes of `lecture-3.1.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. From requirements to a reviewed architecture

(About 45 seconds)

Welcome to Section 3. [pause] This is where the real design work begins. / In this lecture, / I'll show you how to go from a business need / to an architecture you can defend. / We'll turn requirements into design choices, / prove the idea with a proof of concept, / and then review the design against AWS best practices. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Let the **requirements** pick the design, / and let **evidence** confirm it. [long pause]

Transition: So, / what does the business actually need?

## 2. Requirements come in two kinds

(About 1 min 30 seconds)

Every requirement you'll ever get / falls into one of two kinds. [pause]

▶ CLICK

The first kind is **what** the system must do. / Answer questions about company policies. / Summarize customer calls. / Draft replies. / Take actions in other systems. / These are the features.


▶ CLICK

The second kind is **how well** it must do it. / How fast. / How accurate. / How much each request can cost. / How many users at once. / Where the data is allowed to live, / and whether every answer has to be auditable.


▶ CLICK

And here's the thing. / The second list is the one that decides between designs. / Two solutions can both answer questions about policies. / But only one of them meets a two-second latency target / at a cost you can afford. [pause] So in a scenario, / always look for the **how well** words. / They're often hiding in the last sentence. [long pause]

Transition: Once you know the requirements, / you have to make three decisions.

## 3. Every design answers three questions

(About 1 min 30 seconds)

Every GenAI design answers the same three questions. [pause]

▶ CLICK

First, / **which model?** / You choose on capability, / modality, / context length, / latency / and price.


▶ CLICK

Second, / **which pattern?** / Prompting, / RAG, / fine-tuning, / agents, / or a mix of them. / That's the ladder from Lecture 2.3.


▶ CLICK

Third, / **how is it deployed?** / Bedrock on-demand, / batch, / or Provisioned Throughput, / or an endpoint on SageMaker AI.


▶ CLICK

And one rule ties the three together. / Pick the **simplest managed** option / that meets **every** requirement. / Not most of them. / Every one. [long pause]

Transition: So, / how do the requirements point to those choices?

## 4. Requirements point to design choices

(About 2 min)

Certain clues in a requirement / point straight to a design. / Here are six you'll see again and again. [pause]

▶ CLICK

The answers have to come from company documents. / That points to **RAG**, / and on AWS, / that usually means Bedrock Knowledge Bases.


▶ CLICK

The system has to take actions in other systems. / Book a meeting, / open a ticket, / update a record. / That's an **agent** with tools.


▶ CLICK

Every answer needs a consistent brand voice or format. / Start with **prompt templates**. / And if that isn't enough, / fine-tune.


▶ CLICK

Chat has to feel fast. / Think **streaming**, / a smaller model, / and caching.


▶ CLICK

Millions of documents have to be processed, / and nobody's waiting. / That's **batch inference**.


▶ CLICK

And the data must stay private. / That means **VPC endpoints**, / encryption with KMS, / and Guardrails. [pause] Now, / these are heuristics, / not laws. / So always check your choice against **every** requirement in the scenario. [long pause]

Transition: And whatever you choose, / most designs end up with the same backbone.

## 5. Most designs share one backbone

(About 1 min 30 seconds)

Most GenAI applications on AWS / share one shape, / in four layers. [pause]

▶ CLICK

At the front, / the **client**. / A web app, / a mobile app, / or a chat interface.


▶ CLICK

Then the **API layer**. / API Gateway, / with authentication through Cognito. / This gives every client one stable, secure entry point.


▶ CLICK

Then **orchestration**. / Lambda for simple flows, / Step Functions when there are several steps, / retries / or a human in the loop.


▶ CLICK

And at the back, / the **model and the data**. / Bedrock, / Knowledge Bases, / and Guardrails.


▶ CLICK

And across every layer, / the same four services. / IAM for permissions, / KMS for encryption, / CloudWatch for monitoring, / and CloudTrail for the audit trail. [pause] So when you see a new design, / look for this backbone first. / Then look at what's different. [long pause]

Transition: Now, / before you build all of that for real, / you prove it works.

## 6. Five steps to a useful PoC

(About 2 min)

A proof of concept answers three questions. / Is it feasible? / Is it fast enough? / And is it worth the money? / Here's how to run one, / in five steps. [pause]

▶ CLICK

First, / **define success**. / Quality, / latency / and cost targets, / agreed with the business **before** you start. / Otherwise, / any result can look like a success.


▶ CLICK

Second, / **build a test set**. / Somewhere between fifty and two hundred real examples, / each with the answer you expect.


▶ CLICK

Third, / **try models** in Bedrock. / The playground first, / then Converse calls in code, / so you can run the whole test set.


▶ CLICK

Fourth, / **measure**. / Score the answer quality, / record the latency, / and log the tokens for every request. / Then multiply the cost per request / by your real daily volume.


▶ CLICK

And fifth, / **decide**. / Go, / change the design, / or stop. / And stopping is a perfectly good outcome. / It's much cheaper to stop now than after launch.


▶ CLICK

And watch out for the classic mistakes. / Cherry-picked examples that hide the messy cases. / No baseline from the current process. / Ignoring what happens at ten thousand users. / And leaving security for later. [long pause]

Transition: The PoC proves it works. / But is the design **well built**?

## 7. Six pillars, applied to GenAI

(About 1 min 30 seconds)

That's what the AWS Well-Architected Framework is for. / It has six pillars, / and each one means something specific for GenAI. [pause]

▶ CLICK

**Operational excellence**. / Versioned prompts, / monitoring, / and evaluation built into your CI/CD pipeline.


▶ CLICK

**Security**. / Least privilege, / guardrails, / PII protection, / and private access to the model.


▶ CLICK

**Reliability**. / Handling throttling, / retries, / cross-Region inference, / and fallbacks. / We'll go deep on that in Lecture 3.4.


▶ CLICK

**Performance efficiency**. / The right model size, / streaming, / and caching.


▶ CLICK

**Cost optimization**. / Token budgets, / batch, / smaller models, / and prompt caching.


▶ CLICK

And **sustainability**. / Don't run an oversized model / for a job a small one can do. / Every wasted token is wasted energy too. [long pause]

Transition: And for GenAI, / AWS adds a lens on top of those pillars.

## 8. Review the design in the Well-Architected Tool

(About 1 min 45 seconds)

The **Generative AI Lens** adds GenAI-specific questions to the framework. / Is generative AI even the right fit? / Which model, / on what evidence? / Prompting, / RAG / or fine-tuning? / And you run the review in the **Well-Architected Tool**, / in five steps. [pause]

▶ CLICK

First, / **define the workload**. / Its name, / Region, / environment / and owners.


▶ CLICK

Second, / **apply the lenses**. / The core framework, / plus the Generative AI Lens.


▶ CLICK

Third, / **answer the questions**. / You tick the best practices you already follow, / and add notes.


▶ CLICK

Fourth, / **read the risks**. / The tool flags high and medium risks, / and links each one to guidance.


▶ CLICK

Fifth, / **plan and track**. / You build an improvement plan, / and save a milestone so you can see progress over time. / And the tool itself costs nothing.


▶ CLICK

And once a design passes, / turn it into **standard components**. / Shared infrastructure-as-code templates, / approved prompts in Prompt Management, / one shared Guardrails configuration, / and the lens as the checklist every new design passes. / That way, / every team's app starts consistent, / secure / and reviewable. [long pause]

Transition: Let's wrap up.

## 9. Recap

(About 45 seconds)

So, / let's bring it together. [pause]

▶ CLICK

First, / separate **what** the system must do / from **how well** it must do it. / The how-well requirements decide between designs.


▶ CLICK

Second, / every design answers three questions. / Which model, / which pattern, / and how it's deployed. / Pick the simplest managed option that meets every requirement.


▶ CLICK

And third, / prove it with a PoC that has targets agreed up front, / then review it with the Well-Architected Framework / and the Generative AI Lens. [pause]

So, / back to our one sentence. [pause] Let the **requirements** pick the design, / and let **evidence** confirm it. [long pause]

Transition: In the next lecture, / we'll zoom in on the most important choice of all. / The foundation model.
