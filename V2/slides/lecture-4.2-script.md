# Lecture 4.2: Formatting and improving inputs — narration script

Section 4, Data pipelines and vector stores. About 7 minutes. The same text is in the speaker notes of `lecture-4.2.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Formatting and improving inputs

(About 30 seconds)

In the last lecture, / we cleaned the data that goes **into** the vector store. / In this one, / we clean what goes **to the model**. / The request itself. [pause] You'll see the three request formats, / how Amazon Comprehend can read an input before the model does, / and how a small Lambda function keeps every input consistent. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] **Clean, structured input** gets you better answers / and costs you fewer tokens. [long pause]

Transition: So, / what shape does a request take?

## 2. Three ways to send a request

(About 1 min 30 seconds)

There are three ways to send a request to Bedrock. [pause]

▶ CLICK

The first is the **Converse API**. / You send a list of messages, / each with a role, / user or assistant. / Each message holds content blocks, / so text, / images / and documents can go in the same request. / Plus a system prompt, / and your inference settings. / And the big win is that it's the **same shape for every model**.


▶ CLICK

The second is **InvokeModel**. / Here you send the model's **own** JSON body. / Each provider has its own field names, / so you get full control, / but more code, / and switching models means changing that code.


▶ CLICK

The third is **batch inference**. / You put a JSONL file in S3, / one line per request, / each with a record ID and the model input. / Bedrock works through the whole file, / and writes the results back to S3. / It's for large jobs where nobody's waiting, / and it costs less than on-demand calls.


▶ CLICK

And inside the prompt, / structure helps too. / Put the **instructions**, / the **context** / and the **question** / in clearly marked sections, / for example with tags. / The model can then tell your rules apart from the retrieved text. [long pause]

Transition: But before the request is built, / it often pays to read the input first.

## 3. Amazon Comprehend reads the input first

(About 1 min 30 seconds)

That's where **Amazon Comprehend** comes in. / It's a natural language service, / not a generative model, / and it tells you things about the text before the model ever sees it. [pause]

▶ CLICK

It finds the **language**. / So you can route a French question / to a French prompt, / or to a model that handles French well.


▶ CLICK

It finds **personal data**, / like names, / addresses / and account numbers. / So you can **redact** it / before it goes into a prompt, / or into your index.


▶ CLICK

It finds **entities and key phrases**. / Products, / places, / organizations. / Those make great **metadata** for filtering later.


▶ CLICK

It finds **sentiment**. / So an angry customer / can go to a person / instead of a bot.


▶ CLICK

And with a **custom classifier**, / it sorts text into **your own** categories, / like the intent of a support ticket.


▶ CLICK

Why not just ask the LLM to do all this? / Because Comprehend is **fast** and **cheap**. / No prompt, / no generated text, / and you get the same kind of result every time. [long pause]

Transition: Then there's the plain, / boring cleanup. / And that matters more than people think.

## 4. Lambda cleans every input the same way

(About 1 min 30 seconds)

A small **Lambda function** / can clean every input the same way, / in five steps. [pause]

▶ CLICK

One. / **Strip the noise**. / HTML tags, / email signatures, / legal footers. / None of that helps the model.


▶ CLICK

Two. / **Fix the text**. / Broken encoding, / odd characters, / extra spaces.


▶ CLICK

Three. / **Standardize**. / One date format, / one set of units, / one name for each product. / So "the X200" and "X-200" / are the same thing.


▶ CLICK

Four. / **Remove duplicates**. / The same text pasted twice / just burns tokens.


▶ CLICK

Five. / **Fit the budget**. / Trim the input to the token limit you've set, / so one huge request can't blow up your costs.


▶ CLICK

And here's the part people miss. / Use the **same** cleaning / when you ingest documents / and when a question comes in. / If your chunks say "X200" / and the question says "X-200", / the search might not match them. [long pause]

Transition: So, / let's put the whole path together.

## 5. A clean path from request to model

(About 1 min 15 seconds)

Here's a clean path / from a raw request to the model. [pause]

▶ CLICK

It starts with the **request**. / Raw text, / from a user or another app.


▶ CLICK

**Normalize**. / The Lambda function cleans it / and trims it to the budget.


▶ CLICK

**Enrich**. / Comprehend finds the language / and redacts personal data.


▶ CLICK

**Template**. / The instructions, / the context / and the question / go into their marked sections.


▶ CLICK

And **Converse**. / One call to whichever model you've chosen.


▶ CLICK

Clean input pays you **twice**. / You get better answers, / and you send fewer tokens on every single call. [long pause]

Transition: Let's wrap up.

## 6. Recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / pick the request format. / Converse for one shape across models, / InvokeModel when you need the native fields, / and batch inference for big jobs where nobody's waiting.


▶ CLICK

Second, / enrich with Comprehend. / Language, / personal data, / entities, / sentiment / and your own categories, / fast and cheap.


▶ CLICK

And third, / normalize with Lambda. / And clean the same way / at ingestion and at query time. [pause]

So, / back to our one sentence. [pause] **Clean, structured input** gets you better answers / and costs you fewer tokens. [long pause]

Transition: In the next lecture, / we look at where your vectors live. / The vector store options on AWS, / compared side by side.
