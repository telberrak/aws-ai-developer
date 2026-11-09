# Lecture 10.1: Bedrock Guardrails in depth — narration script

Section 10, Safety controls. About 12 minutes. The same text is in the speaker notes of `lecture-10.1.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Bedrock Guardrails in depth

(About 50 seconds)

Welcome to Section 10, / and the start of Domain 3. / This domain is about keeping a generative AI app **safe**, / **secure** / and **governed**. [pause] In this section, / we focus on the safety controls. / What the model is allowed to read, / and what it's allowed to say. [pause] And the main tool for that on AWS / is **Amazon Bedrock Guardrails**. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] A guardrail is one set of policies / that checks every **input** / and every **answer**, / whatever model you use. [long pause]

Transition: So, / where does a guardrail actually sit?

## 2. A guardrail checks both directions

(About 1 min 30 seconds)

A guardrail sits on **both sides** of the model. [pause]

▶ CLICK

First, / the **user input**. / The prompt the user typed, / plus any other text you choose to check.


▶ CLICK

Then the **input check**. / If the input breaks a policy, / it's blocked right here, / and the model is never called. / So you don't even pay for the model call.


▶ CLICK

If it's clean, / it goes to **the model**.


▶ CLICK

And then the **output check**. / The answer is checked before anyone sees it. / Because a clean question / can still get a bad answer.


▶ CLICK

So what happens when a policy triggers? / Three things. [pause] It can **block**, / and the user gets a blocked message that you write yourself. / It can **mask**, / where a name or an email is replaced with a tag, / and the flow carries on. / And you always get a **trace**, / which tells you exactly which policy fired. / Log that, / because that's how you tune the guardrail later. [long pause]

Transition: So, / what can a guardrail check?

## 3. Six policies in one guardrail

(About 2 minutes)

One guardrail can hold **six** kinds of policy. [pause]

▶ CLICK

First, / **content filters**. / Hate, / insults, / sexual content, / violence / and misconduct. / Plus a filter for **prompt attacks**, / which catches jailbreaks and injection attempts. / You set a strength for each one, / from none to high.


▶ CLICK

Second, / **denied topics**. / You describe a topic in plain words, / like investment advice, / and give a few examples. / The guardrail blocks anything on that topic, / even when it's phrased differently.


▶ CLICK

Third, / **word filters**. / Exact words and phrases, / like a competitor's name, / plus a managed list for profanity.


▶ CLICK

Fourth, / **sensitive information**. / Personal data, / like names and card numbers, / and your own patterns. / We'll come back to this one.


▶ CLICK

Fifth, / the **contextual grounding check**. / Is the answer actually backed by the source documents? / And does it answer the question?


▶ CLICK

And sixth, / **automated reasoning checks**. / These check an answer against rules taken from your own policy documents. [pause] Notice the pattern. / The first four are about **harmful** content. / The last two are about **wrong** content. [long pause]

Transition: So, / let's look closer at sensitive information.

## 4. Mask it or block it

(About 1 min 45 seconds)

Here's how the sensitive information policy works. [pause]

▶ CLICK

First, / there's a list of **built-in PII types**. / Names, / email addresses, / phone numbers, / card numbers, / account IDs / and many more.


▶ CLICK

Second, / **your own patterns**. / If you have an employee ID or a policy number with a known format, / you add it as a **regular expression**.


▶ CLICK

Third, / you pick an **action per type**. / **Block** stops the whole message. / **Mask** replaces just the value / and lets the rest through.


▶ CLICK

And fourth, / it works on **input and output**. / So users can't send it in, / and the model can't repeat it back.


▶ CLICK

Here's what masking looks like. / Before, / you see a real name, / an email / and a card number. / After, / you see tags. / Name, / email, / card number. / The answer still makes sense, / but the data is gone.


▶ CLICK

And one warning. / A guardrail protects the **conversation**. / But if you turned on model invocation logging, / those logs still hold the **raw** prompt. / So lock the logs down too, / or mask them with CloudWatch data protection. [long pause]

Transition: Now, / what about answers that are simply wrong?

## 5. Grounding checks and automated reasoning

(About 2 minutes)

Two policies deal with **wrong** answers, / and they work in different ways. [pause]

▶ CLICK

First, / the **contextual grounding check**. / It needs two things. / A **source**, / like the chunks your Knowledge Base retrieved, / and the user's **question**. / Then it gives the answer two scores. / A **grounding** score, / which asks whether the source backs up the answer. / And a **relevance** score, / which asks whether it answers the question at all. / You set a threshold for each, / and below the threshold, / the answer is blocked. / This is your main tool against hallucinations in RAG.


▶ CLICK

Second, / **automated reasoning checks**. / Here, / you upload a policy document, / like an HR handbook. / Bedrock turns it into **formal rules**, / and you can review and test them. / Then each answer is checked against those rules, / using **logic**, / not another model's opinion. / And you get findings, / such as valid or invalid, / with an explanation of why.


▶ CLICK

So here's how to tell them apart. / Grounding catches answers the **source** doesn't support. / Automated reasoning catches answers that break your **rules**. / If a question mentions mathematically verifying answers against policies, / think automated reasoning. [long pause]

Transition: So, / how do you actually attach a guardrail to your app?

## 6. One guardrail, many places to use it

(About 1 min 45 seconds)

You build a guardrail once, / and you can use it in many places. [pause]

▶ CLICK

First, / with **Converse and InvokeModel**. / You pass the guardrail ID and its version with the request, / and Bedrock checks the input and the output for you.


▶ CLICK

Second, / with **Knowledge Bases and Agents**. / You attach the guardrail in their configuration.


▶ CLICK

Third, / the **ApplyGuardrail API**. / This one is important. / It checks any text, / **without** calling a model. / So you can use the same guardrail with a model on SageMaker AI, / a model outside AWS, / or on retrieved documents before they reach the prompt.


▶ CLICK

Fourth, / **input tags**. / With InvokeModel, / you can wrap just the user's text in tags, / so the guardrail checks that part, / and not your own system prompt.


▶ CLICK

And finally, / **versions**. / You edit a working draft, / then you publish numbered versions. / Production always points at a **version**, / so a guardrail change is a release you control, / not a surprise. [long pause]

Transition: Let's wrap up.

## 7. Lecture recap

(About 50 seconds)

So, / let's bring it together. [pause]

▶ CLICK

First, / a guardrail checks **both directions**. / The input before the model, / and the answer before the user.


▶ CLICK

Second, / one guardrail holds **six policies**. / Content filters, / denied topics, / word filters, / sensitive information, / contextual grounding, / and automated reasoning.


▶ CLICK

And third, / you can **use it anywhere**. / With Bedrock calls, / or with the ApplyGuardrail API for any model. / And you always pin a version. [pause]

So, / back to our one sentence. [pause] A guardrail is one set of policies / that checks every **input** / and every **answer**, / whatever model you use. [long pause]

Transition: In the next lecture, / we go after hallucinations directly, / and make the model answer in a shape your code can trust.
