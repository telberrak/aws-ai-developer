# Lecture 3.4: Designing for resilience — narration script

Section 3, Designing solutions and choosing models. About 8 minutes. The same text is in the speaker notes of `lecture-3.4.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Designing for resilience

(About 40 seconds)

Sooner or later, / a model call **will** fail. / The question is what your users see when it does. [pause] In this lecture, / I'll cover the four ways a model call fails, / and three tools to handle them. / Cross-Region inference, / the circuit breaker, / and graceful degradation. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Plan for failure, / so your users get an answer, / even when the model doesn't. [long pause]

Transition: So, / how does a model call actually fail?

## 2. Four ways a model call fails

(About 1 min 30 seconds)

There are four ways, / and you'll want to recognize each one. [pause]

▶ CLICK

First, / **throttling**. / You send more requests than your quota allows, / and Bedrock answers with a throttling error. / This is the most common one by far.


▶ CLICK

Second, / a **regional disruption**. / A service issue in one Region / affects every call you make there.


▶ CLICK

Third, / **limited availability**. / The model isn't offered in your Region, / or there just isn't enough capacity for it right now.


▶ CLICK

And fourth, / a **slow or failing model**. / Latency suddenly spikes, / or one model keeps returning errors. [pause] Each of these needs a slightly different answer. / So let's go through the tools. [long pause]

Transition: First, / the one that handles capacity for you.

## 3. Let Bedrock spread the load

(About 1 min 30 seconds)

That's cross-Region inference. / You met it briefly in Lecture 2.2. / Now let's see how it works. [pause]

▶ CLICK

Your application makes the same call as always. / The only difference is the ID. / Instead of a plain model ID, / it uses an **inference profile** ID.


▶ CLICK

The inference profile defines a set of Regions. / For example, / several Regions within one geography.


▶ CLICK

And Bedrock routes each request / to a Region in that set that has capacity. / So you get more throughput for bursts, / and better resilience, / with **no** change to your code.


▶ CLICK

But there's one thing you must check. / Your request may be processed in any Region in the profile. / So make sure those Regions meet your **data residency** rules. / If the data must stay in one country, / that matters. [long pause]

Transition: Now, / what if a model keeps failing, / again and again?

## 4. Stop calling what is failing

(About 1 min 30 seconds)

That's where the circuit breaker comes in. / It's a simple idea. / Stop calling what's failing. / And it has three states. [pause]

▶ CLICK

**Closed**. / This is normal. / Everything's healthy, / and every request goes to your primary model.


▶ CLICK

**Open**. / Too many failures in a row. / So the breaker opens, / and for a while, / requests skip the primary completely, / and go to a fallback instead. / You stop wasting time and money on calls that will fail.


▶ CLICK

**Half-open**. / After a wait, / the breaker lets a few test requests through to the primary. / If they work, / it closes again. / If they fail, / it opens again.


▶ CLICK

And how do you build it on AWS? / A common way is Step Functions for the flow, / and a DynamoDB table / to hold the state of the circuit. [long pause]

Transition: And when everything else fails, / what then?

## 5. Plan what happens when all else fails

(About 2 min)

Then you degrade **gracefully**. / You plan, / in advance, / what happens at each level. / Think of it as a ladder, / and you only go down a step / when the one above it fails. [pause]

▶ CLICK

Step one, / **retry with backoff**. / Wait a little, / then try again, / and wait a bit longer each time. / That handles short bursts of throttling.


▶ CLICK

Step two, / **fail over**. / Use a cross-Region inference profile, / another Region, / or another model.


▶ CLICK

Step three, / use a **smaller model**. / It's faster, / cheaper / and more available. / The answer may be a bit less capable, / but it's still an answer.


▶ CLICK

Step four, / **serve from cache**. / For common questions, / you may already have a good answer you generated earlier.


▶ CLICK

And step five, / **tell the user**. / A clear message, / and a way forward. / Put the request in a queue, / or hand it to a human. [pause] What you never want / is a blank screen, / or a cryptic error. [long pause]

Transition: Let's wrap up.

## 6. Recap

(About 45 seconds)

So, / let's bring it together. [pause]

▶ CLICK

First, / model calls fail in four ways. / Throttling, / a regional disruption, / limited availability, / or a slow or failing model.


▶ CLICK

Second, / cross-Region inference spreads the load with an inference profile, / and the circuit breaker stops calling a model that keeps failing.


▶ CLICK

And third, / degrade gracefully. / Retry, / fail over, / go smaller, / serve from cache, / and tell the user. [pause]

So, / back to our one sentence. [pause] Plan for failure, / so your users get an answer, / even when the model doesn't. [long pause]

Transition: In the next lecture, / we'll look at customizing models, / and managing them from first version to retirement.
