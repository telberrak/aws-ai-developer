# Lecture 10.2: Reducing hallucinations and structured outputs — narration script

Section 10, Safety controls. About 8 minutes. The same text is in the speaker notes of `lecture-10.2.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Reducing hallucinations and structured outputs

(About 45 seconds)

In the last lecture, / we built a guardrail that checks what goes in / and what comes out. [pause] Now we go after one problem in particular. / **Hallucinations**. / The model says something confident, / and it's simply **wrong**. [pause] And right next to that, / a second problem. / Your code needs the answer in a **fixed shape**, / and the model doesn't always give it. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] **Ground** the answer, / **force** its shape, / and **check** it / before you trust it. [long pause]

Transition: So, / why does a model make things up in the first place?

## 2. Why models make things up

(About 1 min 30 seconds)

There are four common causes. [pause]

▶ CLICK

First, / **no source**. / A model predicts likely text. / If the facts aren't in the prompt, / it still produces something that sounds right. / It fills the gap.


▶ CLICK

Second, / **old knowledge**. / Training stops at a date. / Your prices, / your policies, / your products, / all changed after that.


▶ CLICK

Third, / **pressure to answer**. / If nothing in the prompt says it's allowed to admit it doesn't know, / it tends to answer anyway.


▶ CLICK

And fourth, / **loose sampling**. / A high temperature makes the model pick less likely words. / Great for brainstorming. / Not great for facts.


▶ CLICK

And here's the honest part. / You **can't** remove hallucinations completely. / You **reduce** them, / and you **catch** the ones that get through, / before a user or a system acts on them. [long pause]

Transition: So, / how do you reduce them?

## 3. Give it facts, and permission to say no

(About 2 minutes)

Each fix matches one of those causes. [pause]

▶ CLICK

First, / **retrieve the facts**. / That's RAG. / You put your own documents into the prompt, / for example with Bedrock Knowledge Bases. / Now the model has a source, / and the knowledge is current.


▶ CLICK

Second, / **ask for citations**. / Each claim points to the chunk it came from. / You can show that to the user, / and you can check it in code. / An answer with no citation / is a warning sign.


▶ CLICK

Third, / give it **permission to say I don't know**. / In the system prompt, / tell it to answer only from the context, / and to say so when the context doesn't cover the question. / It sounds simple, / but it makes a real difference.


▶ CLICK

Fourth, / **check the grounding**. / That's the contextual grounding check from the last lecture. / You set a threshold, / and answers the source doesn't support / get blocked.


▶ CLICK

And fifth, / **lower the temperature**. / For facts and for extraction, / set it close to zero. / You lose creativity, / and you gain consistency. [pause] Notice that only the grounding check actually **catches** a hallucination. / The other four just make one less likely. [long pause]

Transition: Now, / the second problem. / Getting an answer your code can actually use.

## 4. Force the shape of the answer

(About 1 min 45 seconds)

When another system reads the answer, / free text isn't good enough. / You need **JSON**, / with the right fields, / every time. / There are three ways to ask for it. [pause]

▶ CLICK

The first is a **schema in the prompt**. / You show the JSON schema and an example, / and ask the model to follow it. / It's simple, / and it usually works. / But **usually** is the key word. / Nothing forces it.


▶ CLICK

The second is **forced tool use**. / You define a tool, / and the tool's input **is** your schema. / Then you tell the model it must call that tool. / So the answer comes back as the tool's input, / already shaped as JSON.


▶ CLICK

And third, / **native structured output**. / Some models on Bedrock also accept a JSON schema directly, / and keep the answer to it. / Check which models support it before you rely on it.


▶ CLICK

Here's forced tool use with the Converse API. / In the tool config, / you define a tool called record claim, / with an input schema that needs an amount and a date. / Then **tool choice** names that tool. / That's what forces the call. [pause] So if you see a question about getting reliable JSON from a model, / forced tool use with a schema / is the pattern to remember. [long pause]

Transition: But a valid shape / still isn't a correct answer.

## 5. Validate, then retry

(About 1 min 30 seconds)

So you check every answer, / in four steps. [pause]

▶ CLICK

First, / **parse**. / Is it valid JSON at all?


▶ CLICK

Second, / **validate**. / Check it against the schema first. / Then check your business rules. / Does the total add up? / Is the date in the past? / Is that product ID real?


▶ CLICK

Third, / if it fails, / **retry**. / And here's the trick. / Send the **error message** back to the model, / so it knows what to fix. / But cap it. / Two retries at most, / or a bad prompt becomes an expensive loop.


▶ CLICK

And fourth, / **fall back**. / Still wrong after the retries? / Return a safe default, / or send it to a person to review.


▶ CLICK

On AWS, / a **Lambda** function does the parsing and validation. / **Step Functions** runs the retry loop / and the human step. / And **CloudWatch** counts how often validation fails. / If that number jumps, / a prompt or a model changed, / and you want to know first. [long pause]

Transition: Let's wrap up.

## 6. Lecture recap

(About 50 seconds)

So, / let's bring it together. [pause]

▶ CLICK

First, / **ground it**. / Retrieved facts, / citations, / permission to say I don't know, / and a low temperature.


▶ CLICK

Second, / **shape it**. / A schema in the prompt, / forced tool use, / or native structured output.


▶ CLICK

And third, / **check it**. / Parse, / validate, / retry with the error, / and then fall back to a person. [pause]

So, / back to our one sentence. [pause] **Ground** the answer, / **force** its shape, / and **check** it / before you trust it. [long pause]

Transition: In the next lecture, / we look at people who **want** your app to misbehave, / and how to stop them with layers of defense.
