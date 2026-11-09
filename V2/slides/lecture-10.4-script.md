# Lecture 10.4: Demo: a guardrail that blocks injection and masks PII — narration script

Section 10, Safety controls. About 13 minutes. The same text is in the speaker notes of `lecture-10.4.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next. [ON SCREEN: …] = what to show during the live demo.

## 1. A guardrail that blocks injection and masks PII

(About 40 seconds)

In this lecture, / we build a guardrail and watch it work. [pause] We'll deploy one guardrail with CDK, / test it on its own, / and then put it in front of a model. / You'll see it stop a prompt injection, / refuse a topic we don't allow, / and mask personal data in an answer. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] A guardrail checks **both sides** of every model call, / so you decide what goes in and what comes out, / not the model. [long pause]

Transition: So, / where does the guardrail sit?

## 2. Two checks around every model call

(About 1 min 30 seconds)

Here's the flow. / Four steps in a line, / and one shortcut underneath. [pause]

▶ CLICK

First, / the **user** types a message. / Nothing special yet.


▶ CLICK

Second, / the **input check**. / Before the model sees anything, / the guardrail reads the prompt. / If it breaks a rule, / the request stops right here, / and the user gets our blocked message.


▶ CLICK

Third, / the **model**. / It only ever sees what passed the input check. / That's the point. / An injected instruction that's blocked / never reaches it.


▶ CLICK

And fourth, / the **output check**. / The guardrail reads the model's answer / before your app does. / That's where personal data gets masked, / and where a harmful answer gets stopped.


▶ CLICK

Now, / there are **two ways** to call it. / You can attach it to the Converse API with guardrailConfig, / and it wraps the model call for you. / Or you can call **ApplyGuardrail** on any piece of text, / with no model at all. [pause] That second one is great for testing, / and for text that comes from somewhere else, / like a model you host yourself. [long pause]

Transition: So, / what's inside our guardrail?

## 3. Four policies, one guardrail

(About 1 min 30 seconds)

One guardrail, / four policies. [pause]

▶ CLICK

First, / the **prompt attack filter**. / It's set to high, / on input. / It's trained to catch jailbreaks / and instructions hidden in the prompt, / like "ignore your rules and do this instead".


▶ CLICK

Second, / a **denied topic**. / Our assistant is for an online shop, / so it must not give investment advice. / And here's the nice part. / You define the topic in **plain words**, / with a few example questions. / No keyword lists.


▶ CLICK

Third, / we **mask contact details**. / Names, / emails / and phone numbers get replaced with placeholders. / And we add our own regex, / for internal order numbers.


▶ CLICK

And fourth, / we **block card numbers**. / If a card number shows up, / the whole request stops. / Nothing gets masked, / it just doesn't go through. [pause]

So how do you choose between masking and blocking? [pause] Mask when the answer is still **useful** without the value. / Block when the value should **never** be there at all. [long pause]

Transition: Let's see what that looks like in code.

## 4. Three choices in the CDK app

(About 1 min 15 seconds)

It's one CDK app, / and three choices matter. [pause]

▶ CLICK

First, / the prompt attack filter. / It only checks **input**, / so its output strength must be NONE. / If you set anything else, / the deploy fails. / It's an easy one to trip on.


▶ CLICK

Second, / mask or block, / chosen **per entity type**. / Email is ANONYMIZE, / which masks it. / Card number is BLOCK. / And the order number regex gets its own action too.


▶ CLICK

And third, / a **version**. / A guardrail has a working draft, / and you create numbered versions from it. / Your app calls version 1, / never the draft. / So when you change the rules, / you create version 2, / test it, / and switch. / And if it misbehaves, / you switch back. [long pause]

Transition: Time to run it.

## 5. Test it on its own with ApplyGuardrail

(About 2 min 30 seconds)

[ON SCREEN: terminal in the lab folder, virtual environment active, AWS credentials set for us-east-1] [pause]

First, / I deploy it. / It takes about a minute. [ON SCREEN: run cdk deploy and show the GuardrailId and GuardrailVersion outputs] [pause] And now I run the test script. / It sends five pieces of text through ApplyGuardrail. / No model is called, / so it's fast, / and it costs almost nothing. [ON SCREEN: run python test_guardrail.py]

▶ CLICK

The first one is a normal question. / Where's my parcel. / The action is **NONE**. / It passes untouched. / And that matters, / because a guardrail that blocks good questions / is just as broken as one that lets bad ones through.


▶ CLICK

The second one is the injection. / Ignore all previous instructions. / **Blocked**, / and the prompt attack filter is the one that fired.


▶ CLICK

Third, / should I buy shares in this company. / **Blocked**, / by the denied topic. / Notice it never says "investment advice". / The guardrail matched the **meaning**, / not a keyword.


▶ CLICK

Fourth, / a message with a card number. / **Blocked**, / by the sensitive information policy.


▶ CLICK

And the fifth one is an **output**, / the kind of text a model might write back. / It has a name, / an email, / a phone number / and an order number. / Look at what comes back. / Every one of them is replaced with a placeholder, / and the order number is masked by our own regex. [pause] [ON SCREEN: point at the returned text with the placeholders] That's the text your app would actually show. [long pause]

Transition: Now let's put it in front of a real model.

## 6. Put it in front of a model

(About 2 min)

[ON SCREEN: same terminal] [pause] This time, / chat.py calls the Converse API, / with the guardrail attached. [pause]

▶ CLICK

First, / the injection again. [ON SCREEN: run chat.py with the injection prompt] [pause] Look at stopReason. / It says **guardrail_intervened**. / And the answer is our blocked message. / The model never saw the request.


▶ CLICK

Now, / a harmless request that makes the model **write** personal data. / A thank-you note to Maria, / with her email. [ON SCREEN: run chat.py with the thank-you note prompt] [pause] The model writes the note, / and the output check masks the name and the email / before it gets back to us. / The exact wording changes from run to run, / but the masking doesn't.


▶ CLICK

And finally, / a normal question. / How do I return a jacket. [ON SCREEN: run chat.py with the return question] [pause] A normal answer, / and stopReason is end_turn. / Nothing was over-blocked. [pause]

And if you want to see exactly **which** policy fired, / and on which side, / add the trace flag. [ON SCREEN: rerun the first command with --trace and scroll the trace] [long pause]

Transition: And if something doesn't work for you, / here's what to check.

## 7. Three checks, then tear it down

(About 1 min)

Three problems cover most of what you'll hit. [pause]

▶ CLICK

If the deploy fails on the guardrail, / check that Guardrails is available in your **Region**. / And remember, / the prompt attack filter needs an output strength of NONE.


▶ CLICK

If chat.py gets an access denied error, / check that you have **model access** in that Region. / Some models need an inference profile ID / instead of the plain model ID.


▶ CLICK

And if something isn't blocked that you expected to be, / remember that detection is **probabilistic**. / First check you're calling the Region you deployed to. / Then try a higher strength, / and run your test cases again.


▶ CLICK

And when you're done, / **tear it down**. / Run cdk destroy. / A guardrail you don't call costs nothing, / but don't leave things lying around. [long pause]

Transition: Let's wrap up.

## 8. Three things to remember

(About 1 min 15 seconds)

So, / let's bring it together. [pause]

▶ CLICK

First, / check **both sides**. / The guardrail reads the prompt before the model, / and the answer after it.


▶ CLICK

Second, / mask or block, / **per type**. / Mask contact details, / block card numbers, / and add your own regex for your own identifiers.


▶ CLICK

And third, / test it **on its own** first. / ApplyGuardrail runs your test cases with no model call, / so you can check the rules / before any user ever sees them. [pause]

So, / back to our one sentence. [pause] A guardrail checks **both sides** of every model call, / so you decide what goes in and what comes out, / not the model. [pause] And that's the end of Section 10. / You know how guardrails work, / how to cut down hallucinations, / and how to defend against attacks in layers. [long pause]

Transition: In the next section, / we zoom out from the model / to the whole workload. / Security, / privacy, / governance / and responsible AI, / starting with how to lock down a foundation model workload.
