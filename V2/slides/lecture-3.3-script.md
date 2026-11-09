# Lecture 3.3: Switching models without code changes — narration script

Section 3, Designing solutions and choosing models. About 7 minutes. The same text is in the speaker notes of `lecture-3.3.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Switching models without code changes

(About 40 seconds)

In the last lecture, / you chose a model. / But here's the thing. / That choice won't last. / New models arrive all the time, / prices change, / and old models get retired. [pause] So in this lecture, / I'll show you how to build your application / so you can switch models / **without** touching the code. / The tool for that is AWS AppConfig. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Keep the model choice in **configuration**, / not in code. [long pause]

Transition: So, / what's actually wrong with hard-coding a model?

## 2. A hard-coded model is a hidden cost

(About 1 min 30 seconds)

Let's compare the two ways of doing it. [pause]

▶ CLICK

On the left, / the hard-coded way. / The model ID and its settings live in your code. / So every time you want to try a new model, / or change the temperature, / you edit code, / test it / and redeploy. / And if five teams each call Bedrock their own way, / you end up with five different integrations to change.


▶ CLICK

On the right, / the abstracted way. / Every application calls **one** internal API. / The model ID and the settings live in configuration. / So switching a model, / testing a new one / or rolling back / takes minutes, / not a release cycle.


▶ CLICK

And here's a phrase worth listening for in any scenario. / "Switch models **without** code changes." / Whenever you hear that, / think configuration, / and think AppConfig. [long pause]

Transition: So, / what does that abstracted design look like?

## 3. A model router in four parts

(About 1 min 30 seconds)

It's a simple pattern, / a model router, / and it has four parts. [pause]

▶ CLICK

First, / the **applications**. / They don't call Bedrock directly. / They call one internal endpoint.


▶ CLICK

Second, / **API Gateway**. / It gives every app one stable contract, / and it handles authentication and throttling.


▶ CLICK

Third, / a **Lambda router**. / It reads the configuration, / works out which model to use for this request, / and calls it.


▶ CLICK

And fourth, / **Bedrock**. / The router uses the Converse API, / so any supported model works / with the same request shape.


▶ CLICK

And underneath it all, / **AWS AppConfig**. / That's where the model ID and its settings live. / The router reads them at run time. / So when you change the configuration, / the very next request uses the new model. [long pause]

Transition: But why AppConfig? / Why not just an environment variable?

## 4. Why AppConfig, not an environment variable

(About 1 min 30 seconds)

It's a fair question, / and there are four good answers. [pause]

▶ CLICK

First, / it's **validated**. / You attach a JSON schema, / or a Lambda validator, / and a broken configuration is rejected / before it ever reaches production.


▶ CLICK

Second, / it's **rolled out gradually**. / A deployment strategy releases the new configuration / to a share of your traffic, / over time. / Not to everyone at once.


▶ CLICK

Third, / it's **rolled back automatically**. / You link a CloudWatch alarm to the deployment. / If errors go up while the change rolls out, / AppConfig puts the old configuration back on its own.


▶ CLICK

And fourth, / there's **no redeploy**. / Changing a Lambda environment variable / actually updates the function. / With AppConfig, / the function stays exactly as it is. / Only the configuration changes. [long pause]

Transition: So, / what does that look like in code?

## 5. The router reads, then calls

(About 1 min 30 seconds)

It's shorter than you might think. [pause]

▶ CLICK

At the top, / the configuration. / It's just JSON. / A default route, / with a model ID, / a temperature / and max tokens. / And a second route, / called summarize, / that uses a smaller, / cheaper model.


▶ CLICK

Then, / the router. / First, / it reads the configuration. / And that read is **cached**, / so you're not calling AppConfig on every single request.


▶ CLICK

Next, / it picks the route for this use case. / And if there isn't one, / it falls back to the default.


▶ CLICK

And finally, / one Converse call, / with the model ID and settings from that route. / Notice there isn't a single model ID in the code itself. [pause] And you'll build exactly this, / and switch models live, / in the demo in Lecture 3.6. [long pause]

Transition: Let's wrap up.

## 6. Recap

(About 45 seconds)

So, / let's bring it together. [pause]

▶ CLICK

First, / a hard-coded model means a redeploy for every change. / So put the model ID and settings in configuration.


▶ CLICK

Second, / the model router. / Apps call API Gateway, / a Lambda router reads AppConfig, / and calls the chosen model through Converse.


▶ CLICK

And third, / AppConfig over an environment variable. / It validates, / rolls out gradually, / rolls back on an alarm, / and needs no redeploy. [pause]

So, / back to our one sentence. [pause] Keep the model choice in **configuration**, / not in code. [long pause]

Transition: In the next lecture, / we'll make sure your application keeps answering / even when a model call fails.
