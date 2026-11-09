# Lecture 9.2: Resilience and model routing — narration script

Section 9, FM APIs and application patterns. About 10 minutes. The same text is in the speaker notes of `lecture-9.2.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Resilience and model routing

(About 40 seconds)

In the last lecture, / we picked how to call the model. / But calls **fail**. / Models get busy, / quotas run out, / networks hiccup. [pause] In this lecture, / I'll show you which errors to retry, / how to retry them properly, / how to stay inside your quotas, / and how to route each prompt to the right model, / with a fallback when things go wrong. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Retry **only** what's worth retrying, / **spread** the load, / and always have somewhere to **fall back** to. [long pause]

Transition: So, / what actually goes wrong?

## 2. Four errors you'll see

(About 1 min 30 seconds)

There are four errors you'll see again and again. [pause]

▶ CLICK

**ThrottlingException**. / A 429. / You've sent too many requests, / or too many tokens, / for your quota. / This one you **retry**, / with backoff.


▶ CLICK

**Service unavailable**. / A 503. / The model is busy, / or not ready yet. / Also worth a retry, / with backoff.


▶ CLICK

**Timeouts**. / Your client gave up before the answer arrived. / Long answers take time, / so raise the read timeout, / or stream the response.


▶ CLICK

And **ValidationException**. / A 400. / The request itself is wrong. / Maybe the prompt is too long, / or a parameter is out of range. / **Don't** retry this one. / Retrying a broken request just gets you the same error, / faster. / Fix the request. [long pause]

Transition: So, / how do you retry properly?

## 3. Wait longer each time, and not all at once

(About 1 min 30 seconds)

Three rules. [pause]

▶ CLICK

First, / **exponential backoff**. / Wait one second, / then two, / then four, / then eight, / up to a cap. / Each retry gives the service more room to recover.


▶ CLICK

Second, / add **jitter**. / Randomize each wait. / Why? / Because if a thousand clients fail at the same moment, / and they all wait exactly two seconds, / they all come back at the same moment, / and fail together again.


▶ CLICK

Third, / **cap the attempts**. / After a few tries, / stop, / and fall back. / Endless retries just turn a small outage into a big one.


▶ CLICK

And one more thing. [pause] Retries must be **safe to repeat**. / If a call books, / charges / or sends something, / give it an **idempotency key**, / so a retry never does it twice. [long pause]

Transition: The good news? / You rarely write this yourself.

## 4. Let the SDK do the retrying

(About 1 min 30 seconds)

The AWS SDK already knows how to retry. / You just configure it. [pause]

Here's what that looks like in Python. [pause]

▶ CLICK

The **retry mode**. / Standard mode retries with backoff and jitter. / Adaptive mode does that too, / and it also slows the client down when it's being throttled.


▶ CLICK

**Max attempts**. / That's the total number of tries, / including the first one. / Keep it small.


▶ CLICK

And the **read timeout**. / A long answer can take a minute or more. / With a short default timeout, / a perfectly healthy call looks like a failure.


▶ CLICK

And if this code runs in **Lambda**, / keep the function timeout longer than all the retries put together. / Otherwise Lambda kills the function in the middle of a retry. [long pause]

Transition: But retries only help with short bumps. / What about steady, heavy traffic?

## 5. Know your limits, then raise them

(About 1 min 30 seconds)

For that, / you need to know your limits, / and raise them. [pause]

▶ CLICK

Bedrock has **per-model quotas**. / Requests per minute, / and tokens per minute, / per model, / per Region. / Check them early, / and ask for increases **before** launch day, / not during it.


▶ CLICK

**Cross-Region inference**. / An inference profile spreads your requests across several Regions, / so at peak, / you get more throughput than one Region alone would give you.


▶ CLICK

**Provisioned Throughput**. / Reserved capacity for steady, / high volume. / You pay for it whether you use it or not, / so it only makes sense when the traffic is really there.


▶ CLICK

And **smooth your traffic**. / A queue or a rate limit in front of the model turns spikes into a steady flow, / and a steady flow stays inside your quota. [long pause]

Transition: Now, / let's talk about sending each prompt to the right model.

## 6. Intelligent Prompt Routing

(About 1 min 30 seconds)

Bedrock has a feature for that. / **Intelligent Prompt Routing**. [pause]

▶ CLICK

Here's how it works. / Instead of a model ID, / you call a **prompt router's** ARN. / The router sits over two models from the same family. / One smaller, / one larger.


▶ CLICK

For each prompt, / it **predicts** the quality each model would give, / and sends the easy prompts to the smaller, / cheaper model. / The hard ones still go to the large one.


▶ CLICK

And **you set the trade-off**. / With your own router, / a quality threshold decides how much quality you're willing to give up / to save cost.


▶ CLICK

But it has limits. / If you need to route **across** model families, / or by your own business rules, / build a router yourself, / like the one we built in Section 3. [long pause]

Transition: And when everything else fails?

## 7. When retries run out, fall back

(About 1 min 15 seconds)

Then you **fall back**, / one step at a time. [pause]

▶ CLICK

First, / retry the **same model**, / with backoff and jitter, / a few times.


▶ CLICK

Second, / try **another Region**. / A cross-Region inference profile does this for you, / or you call a second Region yourself.


▶ CLICK

Third, / use a **different model**. / A smaller or older one that's good enough for now.


▶ CLICK

And last, / **degrade gracefully**. / Serve a cached answer, / switch to a simpler feature, / or tell the user honestly to try again soon. / A clear message beats a spinner that never stops. [long pause]

Transition: Let's wrap up.

## 8. Lecture recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / retry the right errors. / Throttling and 503s, / with backoff, / jitter / and a cap. / Never a 400.


▶ CLICK

Second, / respect your quotas. / Know them, / raise them, / spread the load across Regions, / and smooth the spikes.


▶ CLICK

And third, / route and fall back. / Prompt routing to save cost, / and other Regions, / other models / and cached answers for outages. [pause]

So, / back to our one sentence. [pause] Retry **only** what's worth retrying, / **spread** the load, / and always have somewhere to **fall back** to. [long pause]

Transition: Next, / we connect all this to users and to the business systems they already use.
