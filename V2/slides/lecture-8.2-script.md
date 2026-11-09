# Lecture 8.2: Integrating with legacy systems and microservices — narration script

Section 8, Deployment and enterprise integration. About 10 minutes. The same text is in the speaker notes of `lecture-8.2.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Integrating with legacy systems and microservices

(About 40 seconds)

In the last lecture, / we decided where the model runs. / In this one, / we plug it into the systems your company already has. / Old ones and new ones. [pause] I'll show you one front door for every caller, / when to go synchronous or asynchronous, / how events and workflows carry the slow work, / and how to protect the legacy side. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Give every caller **one front door**, / let **events** carry the slow work, / and put a **safe boundary** around the old systems. [long pause]

Transition: So, / what does that front door look like?

## 2. Put one API in front of the model

(About 1 min 30 seconds)

Here's the simplest pattern, / and you'll see it everywhere. [pause]

▶ CLICK

On the left, / your **callers**. / Legacy apps, / microservices, / internal tools. / They all call one internal API.


▶ CLICK

That API is **API Gateway**. / It handles authentication, / throttling / and usage plans, / and it gives every caller one stable contract.


▶ CLICK

Behind it, / a **Lambda adapter**. / It builds the prompt, / calls the model, / and shapes the reply into whatever the caller expects.


▶ CLICK

And then **Amazon Bedrock**, / through the Converse API, / so any model looks the same.


▶ CLICK

And here's why this matters. [pause] Callers **never** talk to the model directly. / So when you change a prompt, / switch a model, / or tighten a limit, / you do it in **one place**, / and nobody else has to change. [long pause]

Transition: But not every caller can wait for the model to answer.

## 3. Match the call to the wait

(About 1 min 30 seconds)

So the next question is simple. / How long can the caller wait? [pause]

▶ CLICK

**Synchronous** is for short tasks a user is waiting for. / A chat reply, / a quick summary. / API Gateway, / Lambda, / Bedrock, / and the answer comes back in the same call. / But mind the API Gateway integration timeout. / By default, / it's about thirty seconds, / and a long answer can blow through it.


▶ CLICK

**Asynchronous** is for long or bulk work. / A fifty-page report, / or a nightly batch. / You accept the request, / return an ID straight away, / do the work from a queue, / and then store or announce the result.


▶ CLICK

So here's the rule. [pause] If the model **might** take longer than the caller can wait, / go **asynchronous**. [long pause]

Transition: So, / what does asynchronous look like on AWS?

## 4. Let events carry the slow work

(About 1 min 45 seconds)

Here's an event-driven version, / end to end. [pause]

▶ CLICK

It starts with a **source system**. / Say, / your claims platform. / It emits an event. / A claim was filed.


▶ CLICK

**EventBridge** picks it up. / A rule matches the event, / and routes it to the right target.


▶ CLICK

That target is an **SQS queue**. / It absorbs bursts, / it retries failed messages, / and after a few failures, / it moves them to a **dead-letter queue**, / so nothing is lost.


▶ CLICK

A **Lambda worker** reads from the queue, / and calls Bedrock at a pace your quotas allow. / If Bedrock throttles, / the message simply goes back and waits.


▶ CLICK

And when the work is done, / the worker puts a **result event** back on the bus, / for whoever needs it. / The claims system, / a notification, / an audit log. [pause] Nobody waits on the model, / and a slow call never breaks anything upstream. [long pause]

Transition: And what if the job has several steps?

## 5. Step Functions for multi-step jobs

(About 1 min 30 seconds)

That's a job for **Step Functions**. / It runs a workflow, / step by step, / and it remembers where it is. [pause]

▶ CLICK

A step can **call Bedrock directly** from the state machine. / Extract the fields from a document, / or classify it, / with no extra code.


▶ CLICK

Another step **calls the legacy API**, / through a Lambda adapter that speaks the old system's format.


▶ CLICK

A step can **wait for a person**. / The workflow pauses, / sends an approval request, / and carries on when someone answers.


▶ CLICK

And every step gets **retries and catch**. / Retries with backoff are built in, / and if a step still fails, / the workflow takes a fallback path / instead of just stopping. [long pause]

Transition: Finally, / let's protect the old systems themselves.

## 6. A safe boundary around legacy

(About 1 min 45 seconds)

Legacy systems are fragile, / and they're usually the ones you can't change. / So you put a boundary around them. / Four things make it safe. [pause]

▶ CLICK

First, / an **anti-corruption layer**. / An adapter, / often a Lambda function, / translates between the old format and yours. / So the old system's quirks don't leak into your design, / and your changes don't break it.


▶ CLICK

Second, / **private connectivity**. / Reach the systems in your data center over **Direct Connect** / or a **Site-to-Site VPN**. / And reach Bedrock through **PrivateLink**, / so that traffic never crosses the public internet.


▶ CLICK

Third, / **idempotency**. / Every request carries a key, / and you store the keys you've already handled, / for example in DynamoDB. / So when a message is retried, / nothing gets booked, / charged / or sent twice.


▶ CLICK

And fourth, / **retries with backoff**. / Wait a little longer each time, / add some randomness, / cap the number of attempts, / and park what still fails in a dead-letter queue. / That way a struggling legacy system gets room to recover, / instead of a flood. [long pause]

Transition: Let's wrap up.

## 7. Lecture recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / one front door. / API Gateway and a Lambda adapter / sit between every caller and the model.


▶ CLICK

Second, / events for slow work. / EventBridge, / SQS / and Step Functions, / so nobody waits on the model.


▶ CLICK

And third, / protect the legacy side. / Adapters, / private links, / idempotency keys, / and retries with backoff. [pause]

So, / back to our one sentence. [pause] Give every caller **one front door**, / let **events** carry the slow work, / and put a **safe boundary** around the old systems. [long pause]

Transition: In the next lecture, / we look at who gets access, / where the data is allowed to live, / and how to run GenAI across cloud and on-premises.
