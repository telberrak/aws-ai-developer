# Lecture 1.1: Models, tokens and inference parameters — narration script

Section 2, GenAI on AWS essentials. About 8 minutes. The same text is in the speaker notes of `lecture-1.1.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Models, tokens and inference parameters

(About 40 seconds)

Welcome to Section 2. [pause] Before we touch a single AWS service, / we need a shared vocabulary. / So in this lecture, / I'll cover three things. / What a foundation model actually is, / what tokens and the context window mean for you, / and the settings that control how a model answers. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] **Everything** a model does, / you pay for, / limit / and tune / in **tokens**. [long pause]

Transition: So, / what exactly is a foundation model?

## 2. One pre-trained model, many tasks

(About 1 min 30 seconds)

A foundation model is a large model / that's been trained once, / on a huge amount of broad data. [pause]

▶ CLICK

First, / it's **pre-trained**. / Somebody else already spent the money and the months training it. / You don't train it. / You **use** it. / And that's the whole idea. / One model, / many tasks.


▶ CLICK

Second, / you **adapt** it to your job. / And you've got four ways to do that. / You can write a better prompt. / You can give it your own documents at question time, / which is retrieval. / You can let it call tools. / Or you can fine-tune it on your examples. / Keep those four in mind, / because they come back in Lecture 1.3, / and pretty much everywhere after that.


▶ CLICK

And third, / they come in different **types**. / Text and chat models. / Multimodal models, / which read images and documents as well as text. / And embedding models, / which don't write anything at all. / They turn text into a list of numbers, / so you can search by meaning. / You'll use those a lot when we get to RAG. [long pause]

Transition: Now, / every one of these models reads and writes in the same unit. / Tokens.

## 3. Tokens are the unit of cost and limits

(About 2 min)

Let's talk about tokens, / because this is where cost and limits come from. [pause]

▶ CLICK

A token is a word, / or a piece of a word. / A short common word is usually one token. / A long or rare word gets split into several. / As a rough rule, / a token is about three quarters of an English word. / But don't learn that number by heart. / It changes from model to model.


▶ CLICK

Now, / the **context window** is the total number of tokens the model can handle in one request. / And here's the thing most people miss. / It's **shared**. / Your system prompt takes a slice.


▶ CLICK

The conversation history takes a slice.


▶ CLICK

Any documents you retrieve take a slice. / And in a RAG application, / that's often the biggest one.


▶ CLICK

And the answer itself / has to fit in what's left. [pause] So if your answers suddenly get cut short in a long conversation, / this is usually why. / The window is full.


▶ CLICK

And then, / **cost**. / With on-demand pricing, / you pay per token. / Input tokens at one price, / output tokens at another, / and output usually costs more. / Limits and prices are different for every model, / so always check the current numbers in the console. [pause] Here's why that matters. / Every design choice you'll see in this course, / shorter prompts, / smaller chunks, / caching, / is really a choice about **tokens**. [long pause]

Transition: So, / we know what goes in. / Now let's control what comes out.

## 4. Five settings that shape every answer

(About 2 min)

There are five settings you'll see on almost every model call. / They're called inference parameters. [pause]

▶ CLICK

**Temperature**. / This controls randomness. / Close to zero, / the model picks the most likely words, / so you get focused, / repeatable answers. / Higher, / and you get more variety.


▶ CLICK

**Top P**. / This one limits the choice of next word / to the most likely ones, / until their probabilities add up to P. / So a top P of 0.9 / means the model ignores the unlikely tail.


▶ CLICK

**Top K**. / Similar idea, / but it keeps a fixed number of candidate words. / And here's a detail worth knowing. / Not every model supports it. / In the Converse API, / it doesn't have its own field. / You pass it through **additional model request fields**.


▶ CLICK

**Max tokens**. / The ceiling on the length of the answer. / Set it too low, / and the answer stops mid-sentence. / And when that happens, / the response tells you the stop reason was max tokens.


▶ CLICK

**Stop sequences**. / Text that tells the model to stop as soon as it writes it. / Handy when you want exactly one item, / or one section, / and nothing more.


▶ CLICK

And one tip. / Change temperature **or** top P. / Not both at the same time. / If you change both, / you can't tell which one made the difference. [long pause]

Transition: So, / which values should you actually use?

## 5. Match the temperature to the job

(About 1 min 15 seconds)

It really comes down to the job. [pause]

▶ CLICK

**Low** temperature, / close to zero, / for anything that has a right answer. / Extraction. / Classification. / Writing SQL or JSON. / And RAG, / where you want the model to stick to the documents.


▶ CLICK

**Moderate** temperature / for a normal chat assistant. / Natural, / but not wandering off.


▶ CLICK

**Higher** temperature / for creative work. / Marketing ideas, / names, / brainstorming.


▶ CLICK

And when something goes wrong, / two quick fixes. / If answers are **cut off**, / raise max tokens, / or free up room in the context window. / If answers are **inconsistent** / from one run to the next, / lower the temperature. [pause] You'll see that kind of problem a lot, / both in real projects and in exam questions. [long pause]

Transition: Let's wrap up.

## 6. Recap

(About 45 seconds)

So, / let's bring it together. [pause]

▶ CLICK

First, / a foundation model is pre-trained once, / and you adapt it with prompts, / retrieval, / tools / or fine-tuning.


▶ CLICK

Second, / tokens are the unit for everything. / The context window is shared by the prompt, / the history, / the documents / and the answer. / And you pay per input and output token.


▶ CLICK

And third, / temperature, / top P, / top K, / max tokens / and stop sequences / shape the answer. / Low temperature when there's a right answer, / higher when you want ideas. [pause]

So, / back to our one sentence. [pause] Everything a model does, / you pay for, / limit / and tune / in **tokens**. [long pause]

Transition: In the next lecture, / we'll meet Amazon Bedrock. / How you call these models on AWS, / and how you pay for them.
