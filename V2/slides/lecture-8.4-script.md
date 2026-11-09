# Lecture 8.4: CI/CD for GenAI and the GenAI gateway — narration script

Section 8, Deployment and enterprise integration. About 11 minutes. The same text is in the speaker notes of `lecture-8.4.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. CI/CD for GenAI and the GenAI gateway

(About 40 seconds)

This is the last lecture of Section 8. / Two ideas. [pause] First, / how you ship changes to a generative AI app **safely**, / when a one-word change to a prompt can change every answer. / And second, / the **GenAI gateway**, / one front door that sits in front of every model your company uses. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Test **behavior** before every release, / and send every model call through **one gateway**. [long pause]

Transition: So, / what actually changes in a GenAI app?

## 2. Four things can change, and each can break quality

(About 1 min 30 seconds)

In a normal app, / you ship code. / In a GenAI app, / four things can change, / and each one can break the quality of the answers. [pause]

▶ CLICK

First, / **code**. / Your app, / your Lambda functions, / the tools your agent calls.


▶ CLICK

Second, / **prompts**. / The templates, / the system prompts, / the few-shot examples. / Change one word, / and the answers change.


▶ CLICK

Third, / **models**. / A new model ID, / a new version, / or just a different temperature.


▶ CLICK

Fourth, / **retrieval**. / The source documents, / the chunking, / the embedding model. / New documents in a Knowledge Base can change answers too.


▶ CLICK

So here's the shift. / The pipeline has to test **behavior**, / not just code. / All four are versioned, / in Git or in configuration, / and all four go through the **same gate** before they reach users. [long pause]

Transition: So, / what does that pipeline look like?

## 3. Source, build, evaluate, deploy, release

(About 1 min 30 seconds)

Five stages, / from left to right. [pause]

▶ CLICK

First, / **source**. / Code, / prompts / and infrastructure all live in Git. / A pull request starts the pipeline.


▶ CLICK

Second, / **build**, / for example in AWS CodeBuild. / Unit tests, / plus a quick smoke test that calls the model once.


▶ CLICK

Third, / **evaluate**. / This is the new stage. / Run the golden test set, / score the answers, / and compare them with the version in production.


▶ CLICK

Fourth, / **deploy** to staging, / with infrastructure as code. / CloudFormation, / or the CDK on top of it.


▶ CLICK

And fifth, / **release** to production, / gradually, / for example with AWS AppConfig.


▶ CLICK

Now, / you can run this in AWS CodePipeline, / GitHub Actions / or GitLab. / It doesn't matter. / The stages are the same. / What's new for generative AI is that **evaluation gate** in the middle. [long pause]

Transition: So, / what does that gate check?

## 4. Fail the build if the answers get worse

(About 1 min 30 seconds)

The rule is simple. / If the answers get worse, / the build **fails**. / Four checks. [pause]

▶ CLICK

First, / **quality**. / Score the answers with a model as judge, / and compare with the version that's in production today.


▶ CLICK

Second, / **safety**. / Your red-team prompts, / the jailbreaks and the harmful requests, / must still be blocked or refused.


▶ CLICK

Third, / **format**. / If your code expects JSON, / the output must still match the schema. / A prompt change that breaks the format breaks the app.


▶ CLICK

Fourth, / **cost and latency**. / Tokens and response time per request must stay within budget. / A better answer that costs three times as much isn't always better.


▶ CLICK

No score, / no release. / Amazon Bedrock evaluations can run the test set for you, / and the pipeline just reads the result and decides. [long pause]

Transition: And once it passes, / how do you release it?

## 5. Canary or blue/green, with a fast way back

(About 1 min 30 seconds)

You never switch everyone at once without a way back. / Two patterns. [pause]

▶ CLICK

First, / **canary**. / You send a small share of traffic, / say five percent, / to the new version. / You watch the errors, / the latency, / the user feedback / and the quality scores. / Then you roll forward, / or roll back, / automatically.


▶ CLICK

Second, / **blue/green**. / You run the old and the new version side by side, / switch all the traffic at once, / and switch back if something breaks.


▶ CLICK

Either way, / the trigger is a **CloudWatch alarm**. / AWS AppConfig can shift a new prompt or model ID step by step, / and roll back when the alarm fires. / CodeDeploy does the same for Lambda aliases. [pause] And notice why this works so well. / The prompt version and the model ID are **configuration**, / so a rollback is just pointing back to the old value. [long pause]

Transition: Now, / the second big idea. / The gateway.

## 6. One front door for every model

(About 1 min 30 seconds)

Picture a company with twenty teams building with generative AI. / Without a plan, / every team calls the models in its own way. / Different keys, / different limits, / no idea who spent what. / The gateway fixes that. [pause]

▶ CLICK

On the left, / your **teams and apps**. / Chatbots, / internal tools, / batch jobs. / They all call the same API.


▶ CLICK

In the middle, / **the gateway**. / Usually Amazon API Gateway with Lambda behind it, / or a gateway service running on Amazon ECS. / It owns the policy, / so the apps don't have to.


▶ CLICK

On the right, / the **models**. / Amazon Bedrock, / SageMaker AI endpoints, / and other providers if you use them.


▶ CLICK

And here's what makes it work. / Only the gateway's **IAM role** is allowed to call the models. / The apps can't go around it, / so every single request gets the same checks. [long pause]

Transition: So, / what are those checks?

## 7. Five jobs in one place

(About 1 min 30 seconds)

The gateway does five jobs, / in one place. [pause]

▶ CLICK

First, / **authenticate**. / With Cognito or IAM, / it knows which team or app is calling.


▶ CLICK

Second, / **throttle and set quotas**. / API Gateway usage plans give each team its own rate limit and quota, / so one runaway job can't use up everyone's capacity.


▶ CLICK

Third, / **route**. / It picks the right model for the use case, / and falls back to another one when the first is throttled or down.


▶ CLICK

Fourth, / **apply guardrails**. / The same Bedrock Guardrails, / the same content filters and PII rules, / for every app.


▶ CLICK

And fifth, / **log and attribute cost**. / Tokens and cost per team, / stored in CloudWatch and DynamoDB, / so you can charge each team for what it uses. / Bedrock application inference profiles help here too, / because you can tag them per team. [pause] So when a question says "many teams", / "central control" / or "cost per team", / think **gateway**. [long pause]

Transition: Let's wrap up.

## 8. Lecture recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / test behavior, / not just code. / Code, / prompts, / models / and retrieval data all pass the same evaluation gate.


▶ CLICK

Second, / release gradually. / Canary or blue/green, / with a CloudWatch alarm that rolls back for you.


▶ CLICK

And third, / one gateway for every model. / Authentication, / quotas, / routing, / guardrails / and cost per team, / all in one place. [pause]

So, / back to our one sentence. [pause] Test **behavior** before every release, / and send every model call through **one gateway**. [pause] And that's the end of Section 8. / You can host models the right way, / plug them into the systems you already run, / secure them, / and ship changes safely. [long pause]

Transition: In the next section, / we go deeper into the model APIs themselves. / Sync, / async / and streaming calls, / and the patterns that keep your app fast and resilient.
