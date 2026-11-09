# Lecture 9.5: Demo: streaming chat with retries — narration script

Section 9, FM APIs and application patterns. About 12 minutes. The same text is in the speaker notes of `lecture-9.5.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next. [ON SCREEN: …] = what to show during the live demo.

## 1. Streaming chat with retries

(About 40 seconds)

In this lecture, / we build a chat app that feels fast, / and doesn't fall over when Bedrock gets busy. [pause] We'll stream the answer as it arrives, / then throttle the model on purpose, / and watch the app retry, / back off, / and switch to a second model. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] **Stream** so the user starts reading sooner, / and **retry in layers**, / but never once the answer is already on screen. [long pause]

Transition: So, / what are we building?

## 2. A chat app with three layers of protection

(About 1 min 20 seconds)

Here's the whole thing. / Four parts in a line, / and one on the side. [pause]

▶ CLICK

First, / **chat.py**. / A small terminal chat. / It prints each piece of the answer the moment it arrives.


▶ CLICK

Second, / the **boto3 client**. / We create it in **adaptive** retry mode, / with a few attempts. / That's our first layer of protection, / and it costs one line.


▶ CLICK

Third, / our own **retry loop**. / It wraps the whole streaming call, / and waits a little longer each time, / with some randomness, / which we call jitter.


▶ CLICK

Fourth, / the **primary model**. / Nova Lite, / called through **ConverseStream**.


▶ CLICK

And on the side, / a **fallback model**. / Nova Micro. / If the primary keeps throttling, / the same question goes there instead. [pause] And there's nothing to deploy. / It all runs on your laptop. [long pause]

Transition: Let's look at those layers more closely.

## 3. Three layers, from inside out

(About 1 min 30 seconds)

There are three layers, / from the inside out. [pause]

▶ CLICK

Layer one, / **SDK retries**. / In adaptive mode, / botocore retries throttling on the first request for you. / And if throttling keeps happening, / it slows its own sending rate down.


▶ CLICK

Layer two, / **backoff with jitter**. / Our loop waits a random time, / up to half a second, / then up to one, / then up to two. [pause] Why random? / Because if a thousand clients were throttled together, / you don't want them all to retry at the same moment.


▶ CLICK

Layer three, / a **fallback model**. / After three failed tries, / we ask a second model, / and we log which one answered. / That's a product decision, / by the way. / The fallback might be cheaper, / and a bit weaker.


▶ CLICK

And there's one rule / that's easy to miss. [pause] **Never retry once text is on screen.** / If the stream breaks halfway, / a silent retry would print the answer twice. / So we report the error / and let the user ask again. [long pause]

Transition: Here's how that looks in code.

## 4. Three choices in resilience.py

(About 1 min 20 seconds)

The code is short. / Three choices matter. [pause]

▶ CLICK

First, / the client config. / Retries in **adaptive** mode, / three attempts. / That's all it takes to turn on the SDK's own retries.


▶ CLICK

Second, / the **started** flag. / The moment a piece of text is printed, / we set it. / If an error comes after that, / we raise StreamBroken / instead of retrying.


▶ CLICK

Third, / the wait. / A random number, / times a cap that doubles each attempt, / and never more than eight seconds. / That's what we call **full jitter**. [pause] And around all of it, / a loop over two models, / primary first, / then the fallback. [long pause]

Transition: Let's run it.

## 5. Stream it, and time the first token

(About 2 min)

[ON SCREEN: terminal in the lab folder, virtual environment active] [pause]

▶ CLICK

First, / the tests. [ON SCREEN: run python -m unittest -v] [pause] Seven tests, / all offline. / They check the retries, / the fallback, / the cap on the wait, / and that we never retry mid-answer. / No AWS call, / and no waiting either.


▶ CLICK

Now the app, / still offline. [ON SCREEN: run chat.py with --offline and --once] [pause] The words appear one by one, / from a fake model. / Same code path, / no AWS call.


▶ CLICK

And now the real thing. [ON SCREEN: run python chat.py and ask for a long answer, then point at the status line] [pause] Ask for something long. / Look at the status line at the end. / The **first token** came in well under a second. / The **total** took several. [pause] That gap is why we stream. / Streaming doesn't make the answer faster. / It makes the **wait** shorter. [long pause]

Transition: Now let's make Bedrock say no.

## 6. Throttle it on purpose

(About 2 min)

We can't easily make Bedrock throttle us on cue, / so the lab fakes it. [pause]

▶ CLICK

First, / two throttles, / then recovery. [ON SCREEN: run chat.py with --simulate-throttle 2] [pause] Two retry lines, / with growing, / random waits. / Then the primary model answers. / The user just sees a short pause. [pause] One note. / These fake throttles are thrown before any request, / so you only see **our** loop. / Real throttling is retried by the SDK first.


▶ CLICK

Now the primary never recovers. [ON SCREEN: run chat.py with --simulate-throttle always and point at the model name in the status line] [pause] Three retries, / then the fallback line. / And the status line tells you **Nova Micro** answered, / not Nova Lite.


▶ CLICK

And look at that status line one more time. [pause] The model, / the time to first token, / the total time, / and the tokens in and out. / In production, / log all four. / They're the numbers you'll put on a dashboard / and alarm on, / and we'll do exactly that in Section 12. [long pause]

Transition: And if something doesn't work for you, / here's what to check.

## 7. Three checks, then clean up

(About 1 min)

Three problems cover most of what you'll hit. [pause]

▶ CLICK

**AccessDeniedException** means you haven't turned on access to one of the two models in your Region, / or your role can't call InvokeModelWithResponseStream. / Check both models, / not just the first.


▶ CLICK

A **ValidationException** on the model ID / usually means it needs the inference profile ID, / the one that starts with us dot, / or the model isn't in your Region.


▶ CLICK

And if the text arrives all at once, / your terminal is buffering the output. / Run Python with the dash u flag.


▶ CLICK

And cleanup is easy. / Nothing is deployed. / Delete the virtual environment, / and you're done. / Each question costs a fraction of a cent. [long pause]

Transition: Let's wrap up.

## 8. Three things to remember

(About 1 min 10 seconds)

So, / let's bring it together. [pause]

▶ CLICK

First, / stream for the user. / ConverseStream cuts the wait to the **first token**, / not the total time.


▶ CLICK

Second, / retry in layers. / The SDK's adaptive retries, / your own backoff with jitter, / and then a fallback model.


▶ CLICK

And third, / never retry mid-answer. / Once text is on screen, / report the error / instead of repeating it. [pause]

So, / back to our one sentence. [pause] **Stream** so the user starts reading sooner, / and **retry in layers**, / but never once the answer is already on screen. [pause] And that's the end of Section 9, / and of Domain 2. / You can build agents, / deploy and integrate them, / and call models in a way that holds up. / Next comes the Domain 2 checkpoint, / twenty-five questions to check where you stand. [long pause]

Transition: After that, / we move to Domain 3, / safety and security, / starting with Bedrock Guardrails.
