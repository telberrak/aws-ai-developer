# Lecture 6.2: Prompt governance and QA — narration script

Section 6, Prompt engineering and governance. About 10 minutes. The same text is in the speaker notes of `lecture-6.2.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Prompt governance and QA

(About 40 seconds)

In the last lecture, / we moved prompts out of the code and into Prompt Management. / Now, / a prompt is something people can change. / And anything people can change / can break production. [pause] In this lecture, / you'll see how to version prompts, / control who changes them, / log what they do, / and test every change before it ships. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Treat a prompt like **code**. / Version it, / review it, / test it, / and release it in a way you can **roll back**. [long pause]

Transition: So, / what does that lifecycle look like?

## 2. Treat every prompt like code

(About 1 min 20 seconds)

Five steps. / And if you've shipped software before, / they'll look familiar. [pause]

▶ CLICK

**Draft**. / Authors edit the working draft freely. / Nothing here touches production.


▶ CLICK

**Review**. / A second person looks at the change / and the test results, / and approves it.


▶ CLICK

**Version**. / You freeze the approved draft / as a numbered version.


▶ CLICK

**Release**. / You point the app at the new version.


▶ CLICK

And **monitor**. / You watch the logs, / the quality / and the cost, / to make sure it behaves the way the tests said it would.


▶ CLICK

And the key detail. / Versions are **read-only**. / What you tested / is exactly what runs in production. / And the previous version is still there, / untouched, / if you need to go back. [long pause]

Transition: But who's allowed to do each of those steps?

## 3. Who can change a prompt

(About 1 min 10 seconds)

That's an **IAM** question. / You split the rights three ways. [pause]

▶ CLICK

**Authors** can create and edit drafts. / They get the prompt create and update actions, / and nothing more.


▶ CLICK

**Approvers** create versions, / after review. / In a mature setup, / that's a pipeline that only runs when the review and the tests pass, / not a person clicking a button.


▶ CLICK

And **applications** can only **call** approved versions. / Their role gets invoke rights / on specific version ARNs, / so an app can never pick up a half-finished draft.


▶ CLICK

And on top of that, / **AWS CloudTrail** records who changed what. / Every create, / update / and version call is logged, / with the caller and the time. / So when someone asks, / "who changed this prompt last Tuesday?", / you've got the answer. [long pause]

Transition: CloudTrail tells you who changed the prompt. / But what did the model actually see and say?

## 4. Log every prompt and every response

(About 1 min 30 seconds)

For that, / you log every prompt and every response. [pause]

▶ CLICK

The feature is called **model invocation logging**. / You turn it on in the Bedrock settings, / and it's set per Region. / And here's the catch. / It's **off** by default.


▶ CLICK

Once it's on, / it captures the full request / and the full response, / the model ID, / and the token counts. / So you can see exactly what the model was given, / and exactly what it said back.


▶ CLICK

You send it to **CloudWatch Logs**, / when you want to search and alert on it, / to **Amazon S3**, / when you want to keep it for a long time, / or to both.


▶ CLICK

And **protect** it. / These logs hold real user data. / Encrypt them with KMS, / and limit who can read them. / A log nobody secured / is just another place for a leak.


▶ CLICK

So remember there are two different logs. / Invocation logging records what the model **saw and said**. / CloudTrail records **who called which API**. / You need both. [long pause]

Transition: Logs tell you what happened after the fact. / So how do you catch a bad prompt **before** it ships?

## 5. Test every change before it ships

(About 1 min 30 seconds)

With a quality gate. / Every prompt change gets tested, / every time. [pause]

▶ CLICK

It starts with a **golden test set**. / Real questions, / the answers you expect, / the edge cases, / and a few attacks, / like prompt injection attempts.


▶ CLICK

Then you **score** the answers. / Simple rule checks for the format, / like "is this valid JSON?" / And a **model as judge** for the harder part, / like "is this answer correct and grounded?"


▶ CLICK

Then you **compare** with production. / The new version against the one that's running today, / on the same test set.


▶ CLICK

And you **promote only if it's no worse**. / Run all of this in your pipeline, / automatically, / on every prompt change. / A change that makes ten answers better / and three answers worse / shouldn't ship without someone deciding.


▶ CLICK

And you don't have to build the scoring yourself. / **Amazon Bedrock evaluations** can run your test set, / with a model as the judge, / or with human reviewers. [long pause]

Transition: So, / the new version passed. / How do you release it safely?

## 6. Switch versions, never edit in place

(About 1 min 10 seconds)

You switch versions. / You **never** edit in place. [pause]

▶ CLICK

The app stores a **pointer**. / The prompt version ARN lives in configuration, / for example in **AWS AppConfig**.


▶ CLICK

To **release**, / you change the pointer to the new version. / And ideally, / you roll it out gradually, / so a problem hits a few users, / not all of them.


▶ CLICK

To **roll back**, / you point back to the previous version. / There's nothing to rebuild, / and nothing to redeploy.


▶ CLICK

And if this sounds familiar, / it should. / It's the **same idea** as switching models in Section 3. / The change is a configuration update, / so it's fast, / it's auditable, / and it's easy to undo. [long pause]

Transition: Let's wrap up.

## 7. Lecture recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / prompts are **versioned artifacts**. / Draft, / review, / version, / release / and monitor. / And a version never changes.


▶ CLICK

Second, / **control and record**. / IAM decides who edits and who releases. / Invocation logging captures the prompts and responses, / and CloudTrail captures the changes.


▶ CLICK

And third, / **gate every change**. / A golden test set and a judge before release, / and a pointer you can move back if something goes wrong. [pause]

So, / back to our one sentence. [pause] Treat a prompt like **code**. / Version it, / review it, / test it, / and release it in a way you can **roll back**. [long pause]

Transition: Next, / we go beyond the basics. / Advanced prompting techniques, / and Prompt Flows, / which chain prompts and logic into one workflow.
