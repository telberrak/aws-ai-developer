# Lecture 11.5: How the controls fit together — narration script

Section 11, Security, privacy, governance and responsible AI. About 6 minutes. The same text is in the speaker notes of `lecture-11.5.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. How the controls fit together

(About 30 seconds)

Over the last two sections, / we've met a lot of controls. / Identity, / networking, / encryption, / guardrails, / governance, / responsible AI. [pause] Now let's put them in **one picture**. [pause]

Here's the sentence to hold on to. [pause] Security for generative AI isn't one service. / It's **layers**, / and every request passes through all of them. [long pause]

Transition: So, / what are the layers?

## 2. Six layers around one application

(About 2 minutes)

Picture your generative AI application in the middle, / with six layers around it. [pause]

▶ CLICK

The **identity** layer. / IAM Identity Center for your workforce, / Cognito for your customers, / and IAM roles with least privilege for the application itself. / It answers one question. / Who is calling, / and what may they do?


▶ CLICK

The **network** layer. / Your workloads sit in a VPC, / and VPC endpoints with PrivateLink keep calls to Bedrock off the public internet.


▶ CLICK

The **data** layer. / KMS encrypts everything at rest, / Macie finds personal data in your buckets, / and Lake Formation controls who sees which rows and columns.


▶ CLICK

The **model** layer. / Only approved models, / chosen after you've evaluated them, / on Bedrock or SageMaker AI.


▶ CLICK

The **prompt and output** layer. / Bedrock Guardrails check what goes in and what comes out, / and Comprehend can detect and mask personal data.


▶ CLICK

And the **monitoring and audit** layer. / CloudWatch for metrics and logs, / CloudTrail for every API call, / and Config to check your settings stay compliant. [pause] Six layers. / Each one does **one job**. [long pause]

Transition: Now let's follow one request through them.

## 3. Follow a question through every layer

(About 1 min 30 seconds)

A user asks your assistant a question. / Here's what happens. [pause]

▶ CLICK

First, / they **sign in**. / Cognito gives them a token, / and IAM decides what the application is allowed to call.


▶ CLICK

Second, / the request hits the **front door**. / API Gateway throttles and validates it, / and AWS WAF blocks known bad traffic.


▶ CLICK

Third, / the **input guardrail**. / Prompt attacks, / denied topics / and personal data are caught before the model ever sees them.


▶ CLICK

Fourth, / **private retrieval**. / The knowledge base is queried over a VPC endpoint, / and metadata filters return only the documents this user may see.


▶ CLICK

Fifth, / the **model** answers, / and the **output guardrail** checks the answer. / Is it grounded in the sources? / Is any personal data masked?


▶ CLICK

And sixth, / everything is **logged**. / Invocation logs, / CloudTrail events / and metrics.


▶ CLICK

Notice the design. / If one layer misses something, / the next one still has a chance to catch it. / That's **defense in depth**. [long pause]

Transition: Here's another way to use this picture.

## 4. Name the risk, name the control

(About 1 min 30 seconds)

When someone names a risk, / you should be able to name the control. [pause]

▶ CLICK

**Prompt injection**? / The guardrail's prompt attack filter, / plus your own input validation.


▶ CLICK

**Personal data** leaking out? / The guardrail's sensitive information filter, / Comprehend in your own pipeline, / and Macie on the data at rest.


▶ CLICK

Someone trying to **pull data out** of your account? / Least-privilege IAM, / VPC endpoints / and KMS key policies.


▶ CLICK

**Hallucination**? / The contextual grounding check, / and citations so users can verify.


▶ CLICK

**Unfair** output? / Clarify and model evaluations, / on every release.


▶ CLICK

And when the auditor asks, / **who did what**? / CloudTrail, / model invocation logging / and Config. [pause] One risk, / one control. / That's the habit to build. [long pause]

Transition: Let's wrap up.

## 5. Lecture recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / think in **six layers**. / Identity, / network, / data, / model, / prompt and output, / and monitoring.


▶ CLICK

Second, / **follow the request**. / Sign-in, / front door, / input guardrail, / private retrieval, / model and output guardrail, / and logs.


▶ CLICK

And third, / for every **risk**, / name the **control** that handles it. [pause]

So, / back to our one sentence. [pause] Security for generative AI isn't one service. / It's **layers**, / and every request passes through all of them. [pause]

That closes this section, / and the whole security and governance domain. / Before you move on, / take the **Domain 3 checkpoint**. / Twenty questions, / and a good way to see what stuck. [long pause]

Transition: Next, / we switch to cost and performance, / starting with token economics and caching.
