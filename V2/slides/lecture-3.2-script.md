# Lecture 3.2: Evaluating and choosing foundation models — narration script

Section 3, Designing solutions and choosing models. About 8 minutes. The same text is in the speaker notes of `lecture-3.2.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Evaluating and choosing foundation models

(About 30 seconds)

In the last lecture, / we said every design starts with three decisions. / In this one, / we zoom in on the first. / Which foundation model? [pause] I'll show you what to compare, / where the evidence comes from, / a simple method to choose, / and why bigger isn't always better. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Benchmarks **shortlist** the models, / but **your own data** picks the winner. [long pause]

Transition: So, / what do you actually compare?

## 2. Six things decide the model

(About 1 min 30 seconds)

Six things decide which model fits. [pause]

▶ CLICK

**Capability**. / How well it reasons, / writes code, / uses tools, / and handles the languages you need.


▶ CLICK

**Modality**. / Text only, / or images and documents too? / Or do you actually need an embedding model?


▶ CLICK

**Context length**. / How much input and output fits in one request. / A long contract needs a long window.


▶ CLICK

**Latency**. / Time to the first token, / and tokens per second after that. / For chat, / that's what the user feels.


▶ CLICK

**Price**. / Per input and output token, / or per model unit with Provisioned Throughput.


▶ CLICK

And **limits**. / Which Regions it's in, / your quotas, / the provider's data policies, / and where the model is in its lifecycle. / A model that's about to be retired / isn't a good choice for a new project. [pause] Notice that the first five are about the model. / The sixth is about whether you can actually **use** it. [long pause]

Transition: So, / where does the evidence for all of that come from?

## 3. Benchmarks shortlist, your data decides

(About 1 min 30 seconds)

You've got four sources of evidence, / and each one has a catch. [pause]

▶ CLICK

**Public benchmarks**. / They tell you how a model does on standard tasks. / The catch? / Those tasks might look nothing like yours.


▶ CLICK

**Provider model cards**. / They give you the context length, / the modalities, / the limits / and the intended use. / But remember, / the provider wrote them.


▶ CLICK

**Bedrock model evaluation**. / This runs your prompts through the models / and scores the results, / either automatically, / with a model as the judge, / or with human reviewers. / The catch is that you need a good dataset.


▶ CLICK

And **your own test set**. / Real work, / with expected answers, / so you get quality, / latency / and cost on **your** problem. / It takes effort to build, / but it's the only evidence that really counts.


▶ CLICK

So here's the rule. / Use benchmarks and model cards to **shortlist**. / Then let your own test set **pick the winner**. [long pause]

Transition: Let's turn that into a method.

## 4. Choose a model in five steps

(About 1 min 30 seconds)

Here's how to choose a model, / in five steps. [pause]

▶ CLICK

First, / **filter on hard limits**. / Modality, / context length, / Region, / and data rules. / Any model that fails one of these is out, / however good it is.


▶ CLICK

Second, / **shortlist two or three**. / Use the model cards and the public benchmarks. / Not ten. / Two or three.


▶ CLICK

Third, / **run your test set** on each of them. / Score the quality, / and record the latency and the tokens.


▶ CLICK

Fourth, / **compare the cost per task**. / Not per token. / Per answer, / at your real volume. / A cheaper model that needs twice the tokens / can end up costing more.


▶ CLICK

And fifth, / **decide, / and revisit**. / New models arrive all the time. / So keep that test set, / and re-run it whenever a new candidate shows up. [long pause]

Transition: And when you compare, / don't assume the biggest model wins.

## 5. Bigger isn't always better

(About 1 min 30 seconds)

Bigger isn't always better. / Match the size of the model to the task. [pause]

▶ CLICK

Classification, / routing / and extraction. / A **small**, / fast model is usually enough. / It's a narrow task at high volume, / so low cost matters most.


▶ CLICK

Chat over retrieved documents. / A **mid-size** model usually does the job, / because the context already carries the facts.


▶ CLICK

Complex reasoning, / planning / and code. / That's where a **large** model earns its price, / because quality matters more than cost.


▶ CLICK

And search and retrieval for RAG. / That's not a chat model at all. / It's an **embedding** model, / because you need vectors, / not generated text.


▶ CLICK

And here's a pattern you'll see a lot. / A **small** model looks at each request first / and routes it. / The **large** model only answers the hard cases. / You get most of the quality, / at a fraction of the cost. [long pause]

Transition: Let's wrap up.

## 6. Recap

(About 45 seconds)

So, / let's bring it together. [pause]

▶ CLICK

First, / compare six things. / Capability, / modality, / context length, / latency, / price, / and limits.


▶ CLICK

Second, / filter on hard limits, / shortlist two or three, / run your own test set, / and compare the cost per task, / not per token.


▶ CLICK

And third, / right-size the model. / Small for narrow, high-volume tasks, / large only for the hard cases. [pause]

So, / back to our one sentence. [pause] Benchmarks **shortlist** the models, / but **your own data** picks the winner. [long pause]

Transition: But once you've picked a model, / you'll want to change it later. / So in the next lecture, / we'll see how to switch models / without touching your code, / with AWS AppConfig.
