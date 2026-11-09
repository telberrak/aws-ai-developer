# Lecture 2.4: Demo: your first Bedrock call — narration script

Section 2, GenAI on AWS essentials. About 6 minutes. The same text is in the speaker notes of `lecture-2.4.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next. [ON SCREEN: …] = what to show during the live demo.

## 1. Your first Bedrock call

(About 30 seconds)

Enough theory. / In this lecture, / we make our first call to a model on Bedrock. / First from Python, / then from the AWS CLI. / And we'll play with the settings you met in Lecture 2.1. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] **One** Converse request, / and you've built your first GenAI integration. [long pause]

Transition: Here's the plan.

## 2. Four steps, about five minutes

(About 45 seconds)

Four steps, / and the code is in the lab folder for this lecture, / so you can follow along. [pause]

▶ CLICK

First, / set two variables. / Your Region, / and the ID of the model you want to call. / You copy that from the Bedrock console. / And if the console says the model needs an inference profile, / use the profile ID instead.


▶ CLICK

Second, / run the Python script / and read the answer.


▶ CLICK

Third, / change the temperature, / and see what happens to the answers.


▶ CLICK

And fourth, / make the exact same call from the AWS CLI. [long pause]

Transition: Before we run it, / let's read the code.

## 3. One call, five parts

(About 1 min 30 seconds)

The whole script is short. / Let's go through it, / piece by piece. [pause]

▶ CLICK

First, / the client. / Notice it's **bedrock-runtime**, / because we're calling a model, / not managing one.


▶ CLICK

Then, / the messages. / A system prompt that sets the role, / "you are a concise AWS tutor", / and one user message with our question. / That's the same shape for every model in Bedrock.


▶ CLICK

Next, / the inference config. / Temperature and max tokens, / the settings you already know.


▶ CLICK

Then, / one call. / client dot converse, / with the model ID, / the system prompt, / the messages / and the config.


▶ CLICK

And finally, / we read the response. / The answer text is in output, / message, / content. / And just as useful, / **usage** tells you how many input and output tokens you just paid for, / and **stop reason** tells you why the model stopped. [long pause]

Transition: OK, / let's run it.

## 4. Run it, and read what comes back

(About 2 min)

[ON SCREEN: switch to the terminal, in the lab folder, with the two variables already set] [pause]

I'll run the script with the question, / "What is RAG?" [pause]

▶ CLICK

And there's our answer. / Now look underneath it. / The stop reason is **end turn**. / That means the model finished on its own. / And here's the usage. / Input tokens, / output tokens, / total. / That's your bill for this call. / A fraction of a cent.


▶ CLICK

Now, / let's play with the temperature. [ON SCREEN: run "Suggest a name for a GenAI study group" three times at 0.9, then three times at 0] [pause] At 0.9, / every answer is different. / At zero, / they're almost identical. / That's exactly what we said in Lecture 2.1. / Low temperature for a right answer, / higher for ideas. [pause] And watch this. / If I set max tokens to twenty, / the answer stops mid-sentence, / and the stop reason now says **max tokens**.


▶ CLICK

And finally, / the same call from the CLI. [ON SCREEN: run the aws bedrock-runtime converse command from the lab README] [pause] Same request, / same response shape. / Output, / stop reason, / usage. / So whatever language you use, / the API is the same. [long pause]

Transition: And if it doesn't work for you, / here's what to check.

## 5. Four errors, four fixes

(About 45 seconds)

Four errors cover almost everything you'll hit. [pause]

▶ CLICK

**Access denied**. / Model access isn't on for this model in this Region, / or your IAM role can't invoke it.


▶ CLICK

A **validation** error that mentions on-demand throughput or an inference profile. / Use the model's inference profile ID instead of the plain model ID.


▶ CLICK

**Resource not found**. / The model isn't offered in your Region. / Pick another model, / or another Region.


▶ CLICK

And **throttling**. / Wait a few seconds and try again. / On-demand quotas are per account and per Region. [pause] And the good news. / This lab creates nothing, / so there's nothing to tear down. [long pause]

Transition: Let's wrap up.

## 6. Recap

(About 45 seconds)

So, / let's bring it together. [pause]

▶ CLICK

First, / you need four things in place. / The Region, / model access, / IAM, / and the right model or inference profile ID.


▶ CLICK

Second, / one Converse call takes a system prompt, / messages / and an inference config. / And it's the same shape for every model.


▶ CLICK

And third, / always read the response's stop reason and usage. / They tell you why the answer ended, / and what it cost. [pause]

So, / back to our one sentence. [pause] **One** Converse request, / and you've built your first GenAI integration. [pause] And that's the end of Section 2. / You've got the vocabulary, / you know Bedrock, / and you've made your first call. [long pause]

Transition: In the next section, / we start the real work. / Designing a solution, / and choosing the right model for it.
