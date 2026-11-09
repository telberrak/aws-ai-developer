# Lecture 2.3: The four architecture patterns — narration script

Section 2, GenAI on AWS essentials. About 6 minutes. The same text is in the speaker notes of `lecture-2.3.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. The four architecture patterns

(About 30 seconds)

Almost every generative AI application you'll build / is one of four patterns, / or a mix of them. [pause] In this lecture, / I'll show you those four patterns, / how to choose between them, / and the one comparison that comes up again and again. / RAG or fine-tuning. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Start with the **simplest** pattern that works, / and only climb when you have to. [long pause]

Transition: So, / let's climb.

## 2. Climb only as high as you need

(About 2 min)

Think of the patterns as a ladder. / Each step up costs more effort, / more money, / and more maintenance. [pause]

▶ CLICK

Step one, / **prompt engineering**. / You use the model as it is, / and you get better results by writing better instructions and examples. / It's quick, / it's cheap, / and you'd be surprised how far it gets you.


▶ CLICK

Step two, / **RAG**, / retrieval-augmented generation. / At question time, / you find the relevant pieces of your own documents, / and you put them in the prompt. / So the model answers from **your** data, / and it can cite where the answer came from.


▶ CLICK

Step three, / **fine-tuning**. / You train the model a bit further, / on your own labeled examples. / That changes how the model **behaves**. / Its tone, / its format, / its style.


▶ CLICK

And the top step, / **training a model from scratch**. / Huge data, / huge cost, / months of work. / For this course, / and for the exam, / it's almost never the right answer.


▶ CLICK

And then there's **agents**. / An agent doesn't sit on the ladder. / It sits **beside** it. / An agent lets the model plan, / call tools / and take actions, / like looking up an order or opening a ticket. / And it can use any step of the ladder underneath. [pause] So the question to ask is simple. / Does the model just need to **answer**, / or does it need to **act**? [long pause]

Transition: Now, / the two middle steps are the ones people mix up the most.

## 3. What it knows, or how it answers

(About 1 min 45 seconds)

RAG or fine-tuning. / Here's how to tell them apart. [pause]

▶ CLICK

RAG solves a **knowledge** problem. / The model doesn't know your facts. / So look for the clues. / The data changes often. / You need citations. / You need answers grounded in your own documents. / All of those point to RAG.


▶ CLICK

Fine-tuning solves a **behavior** problem. / The model knows enough, / but it doesn't answer the way you want. / So the clues here are tone, / format, / style, / or a very specific task done the same way every time. / Those point to fine-tuning.


▶ CLICK

And here's the rule. / If the problem is **what** the model knows, / use RAG. / If the problem is **how** it answers, / fine-tune. [pause] And if a question asks for the **least** effort, / RAG almost always wins. / You don't retrain anything. / You just update the documents. [long pause]

Transition: Let's try that on a few examples.

## 4. Which pattern fits?

(About 1 min 15 seconds)

Here are four quick situations. / Try to answer before I do. [pause]

▶ CLICK

A support bot has to answer from product manuals / that change every week. / That's **RAG**. / Changing data, / and the answers come from documents.


▶ CLICK

All answers have to follow your brand's tone, / in a fixed format, / every single time. / Prompt engineering might get you there. / But if it doesn't, / that's **fine-tuning**. / It's a behavior problem.


▶ CLICK

An assistant has to check an order's status / and then issue a refund. / That's an **agent**. / It has to act, / not just answer.


▶ CLICK

And a team wants to summarize meeting notes. / Just a good **prompt**. / Don't climb the ladder for that. [long pause]

Transition: Let's wrap up.

## 5. Recap

(About 45 seconds)

So, / let's bring it together. [pause]

▶ CLICK

First, / the ladder. / Prompt engineering, / then RAG, / then fine-tuning. / Training from scratch is almost never the answer.


▶ CLICK

Second, / agents sit beside the ladder. / Use one when the model has to **act**, / not just answer.


▶ CLICK

And third, / RAG fixes what the model **knows**. / Fine-tuning fixes how it **answers**. / And RAG is usually the least effort. [pause]

So, / back to our one sentence. [pause] Start with the **simplest** pattern that works, / and only climb when you have to. [long pause]

Transition: In the next lecture, / we'll stop talking and make our first Bedrock call. / Have your account ready.
