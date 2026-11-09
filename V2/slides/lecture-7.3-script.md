# Lecture 7.3: Model coordination and human in the loop — narration script

Section 7, Agents and tools. About 8 minutes. The same text is in the speaker notes of `lecture-7.3.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Model coordination and human in the loop

(About 30 seconds)

In the last lecture, / we gave agents structure and safeguards. / In this one, / we look at two more ways to keep them sharp and safe. [pause] Using the **right model** for each step, / and bringing in a **person** when the stakes are high. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Let **small models** do the routine work, / escalate what they're unsure about, / and keep a **human** in the loop for the decisions that matter. [long pause]

Transition: So, / why would one workflow use more than one model?

## 2. Not every step needs the same model

(About 1 min 15 seconds)

Here's the thing. / An agent doesn't have to send every step to the same model. / You can split the work into four roles. [pause]

▶ CLICK

First, / the **router**. / A small, / fast model reads the request / and decides which path it takes. / That's a cheap call, / and it happens on every request.


▶ CLICK

Second, / the **specialists**. / Models that do one narrow job well. / Pulling fields out of a document, / classifying a ticket, / writing code, / or a model you fine-tuned on your own domain.


▶ CLICK

Third, / the **generalist**. / A large model for open-ended reasoning, / and for anything the specialists don't cover.


▶ CLICK

And fourth, / the **orchestrator**. / One supervisor agent, / or one workflow, / that owns the plan / and passes work between the others. [pause] On Bedrock, / all of these are just different model IDs behind the same API. / So the rule is simple. / Small models for narrow, / high-volume steps, / and large models only where they **earn** their cost. [long pause]

Transition: And there's a neat pattern that builds on this. / The cascade.

## 3. Cheap first, escalate when unsure

(About 1 min 15 seconds)

A **cascade** tries the cheap option first, / and escalates only when it has to. [pause]

▶ CLICK

Step one. / A **small model** answers, / and it also gives you something to judge the answer by. / A confidence score, / or a quick self-check.


▶ CLICK

Step two. / A rule decides whether that's good enough. / It might be a score threshold, / a check that the output matches your schema, / or a judge model that grades the answer.


▶ CLICK

Step three. / If it's not good enough, / the request goes to a **large model**. / But only those cases.


▶ CLICK

And step four. / If the large model still can't settle it, / a **person** reviews it.


▶ CLICK

Here's why that matters. / Most requests stop at **step one**. / So you only pay large-model prices, / and human time, / for the hard cases. [long pause]

Transition: But when exactly should a person step in?

## 4. Four signals that a human should decide

(About 1 min)

There are four signals to watch for. [pause]

▶ CLICK

First, / **high impact**. / Moving money, / deleting data, / anything you can't undo. / A wrong answer there costs too much.


▶ CLICK

Second, / **low confidence**. / The model's score, / or one of your checks, / falls below your threshold.


▶ CLICK

Third, / **rules require it**. / Regulated decisions, / exceptions to a policy, / or legal wording often need a person to sign off.


▶ CLICK

And fourth, / **something new**. / Inputs that look nothing like your tests, / or that a guardrail flagged.


▶ CLICK

And one more tip. / **Sample the rest**. / Send a small random share of normal cases to review as well. / That's how you catch the errors the model is **confident** about, / which the other signals will miss. [long pause]

Transition: So, / how do you actually build that review on AWS?

## 5. A2I adds a human review loop

(About 1 min 15 seconds)

The managed answer is **Amazon Augmented AI**, / or A2I. / It adds a human review loop to a machine learning workflow. [pause]

▶ CLICK

It starts with a **model result**. / Your app gets an answer, / and a confidence score.


▶ CLICK

Then the **activation rule**. / In A2I, / you define a flow definition. / It says when to start a human loop, / for example when confidence is below a threshold, / and which review form reviewers see.


▶ CLICK

Next, / the **work team**. / That can be your own private reviewers, / a vendor, / or Amazon Mechanical Turk. / For sensitive data, / you'd use a private team.


▶ CLICK

And finally, / the **results**. / The reviewed answer lands in **S3** as JSON, / and your app picks it up from there.


▶ CLICK

Now, / A2I has built-in integrations for **Textract** and **Rekognition**. / For any other model, / Bedrock included, / you use a **custom task type**, / and start the human loop from your own code. [long pause]

Transition: A2I is great for reviewing answers. / But what about approving an action, / in the middle of a workflow?

## 6. Pause the workflow until someone approves

(About 1 min 15 seconds)

For that, / you use **Step Functions**, / and a pattern called wait for a callback. [pause]

▶ CLICK

Step one. / The agent **proposes** an action. / Say, / a refund of four hundred dollars.


▶ CLICK

Step two. / Step Functions runs a task that **waits**. / It gets a unique **task token**, / and the workflow pauses right there.


▶ CLICK

Step three. / The approver is **asked**. / A notification, / or an internal app, / shows them the request, / along with that token.


▶ CLICK

Step four. / The answer **resumes** the workflow. / Approve or reject sends the token back to Step Functions, / and the workflow either continues, / or stops.


▶ CLICK

And one rule you should never skip. / Always set a **timeout**. / If nobody answers, / the workflow should fail safe, / instead of waiting forever with a refund half done. [long pause]

Transition: Let's wrap up.

## 7. Lecture recap

(About 45 seconds)

So, / let's bring it together. [pause]

▶ CLICK

First, / match the model to the step. / A small router, / specialists for narrow jobs, / and a large model for everything else.


▶ CLICK

Second, / cascade, / then escalate. / Cheap first, / a bigger model when it's unsure, / and a person last.


▶ CLICK

And third, / put humans where it matters. / A2I review loops for answers, / and Step Functions task tokens, / with a timeout, / for approvals. [pause]

So, / back to our one sentence. [pause] Let **small models** do the routine work, / escalate what they're unsure about, / and keep a **human** in the loop for the decisions that matter. [long pause]

Transition: Next, / we look at the tools themselves. / How to design them, / and how to serve them with MCP.
