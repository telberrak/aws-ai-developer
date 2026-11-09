# Lecture 13.2: Evaluating RAG and agents, and quality gates — narration script

Section 13, Evaluation and troubleshooting. About 12 minutes. The same text is in the speaker notes of `lecture-13.2.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Evaluating RAG and agents, and quality gates

(About 40 seconds)

In the last lecture, / we learned how to score a model's answers. / But most real apps aren't a single model call. / They're RAG pipelines, / and agents. [pause] So in this lecture, / I'll show you how to evaluate RAG in two halves, / how to judge an agent, / and how to turn all of it into a **gate** your releases have to pass, / before and after they go live. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Test **each part** on its own, / and make **passing the tests** the only way to ship. [long pause]

Transition: So, / why split a RAG answer in two?

## 2. Score the two halves separately

(About 1 min 45 seconds)

A RAG answer comes from two steps. / First, / the system **retrieves** some chunks. / Then the model **generates** an answer from them. / If you only score the final answer, / you can't tell which step failed. [pause]

▶ CLICK

So you score **retrieval** first. / **Context relevance**. / Are the chunks actually about the question? / And **context coverage**. / Do they hold everything the answer needs, / or is a piece missing?


▶ CLICK

Then you score **generation**. / **Correctness** and **completeness**, / against your reference answer. / And **faithfulness**. / Is every claim in the answer backed by those chunks, / or did the model add something of its own?


▶ CLICK

And now you know where to fix. [pause] If the retrieval scores are weak, / look at your chunking, / your embedding model, / or your filters. / If retrieval is good / but the answers aren't faithful, / the problem is the prompt, / or the model. / Two numbers, / two very different fixes. [long pause]

Transition: And the good news? / Bedrock can run this whole evaluation for you.

## 3. Bedrock evaluates your RAG for you

(About 1 min 30 seconds)

Amazon Bedrock has evaluation jobs made for Knowledge Bases. / Four steps. [pause]

▶ CLICK

First, / write the dataset. / Questions, / with reference answers, / as a JSONL file in S3.


▶ CLICK

Second, / pick what to test. / Retrieval only, / which checks the chunks. / Or retrieval **and** generation, / which checks the final answer too.


▶ CLICK

Third, / pick a **judge model**. / It scores the metrics we just saw, / relevance, / coverage, / correctness / and faithfulness.


▶ CLICK

And fourth, / compare the reports. / Change **one** setting, / say the chunk size, / run the same job again, / and put the two reports side by side. / That's how you tune a RAG system with evidence, / instead of gut feeling. [long pause]

Transition: Agents are harder, / because they take many steps. / So how do you judge them?

## 4. Judge an agent by its path, not just its answer

(About 2 min)

With an agent, / a right answer isn't enough. / It might have got there by luck, / or by calling twenty tools when two would do. / So you judge the **path**, / not just the answer. / Here are five things to score. [pause]

▶ CLICK

**Task success**. / Did it actually finish the job the user asked for?


▶ CLICK

**Tool-call accuracy**. / Did it pick the right tool, / with the right arguments, / in the right order?


▶ CLICK

**Trajectory**. / How many steps did it take? / Did it loop, / or make calls it didn't need?


▶ CLICK

**Safety**. / Did it refuse what it should refuse, / and stay inside its limits?


▶ CLICK

And **cost and latency**. / Tokens, / tool calls / and seconds, / per finished task.


▶ CLICK

To score any of this, / you need **traces**. / Record every model call and every tool call, / with its inputs and outputs, / for example in CloudWatch. / Then you can score the whole trajectory, / step by step, / and not only the final answer. [long pause]

Transition: So now you can measure quality. / How do you stop a bad change from reaching users?

## 5. No release without a passing score

(About 1 min 45 seconds)

You build a **quality gate** into your pipeline. [pause]

▶ CLICK

It starts with a **change**. / A new prompt, / a new model, / a new chunk size, / or new code. / They all go through the same pipeline, / for example in CodePipeline.


▶ CLICK

The pipeline runs your **test set**. / The same evaluation, / every time, / for example in a CodeBuild step.


▶ CLICK

Then it **scores** the results, / with a judge model and fixed metrics.


▶ CLICK

If the scores pass, / it deploys. / If they fail, / it **blocks** the release, / and reports what dropped.


▶ CLICK

And the key is to set the bar **before** you run. / A minimum score for each metric. / No drop against the version in production. / And zero failures on your safety cases. / If any rule fails, / the pipeline stops. / No discussion, / no "it's probably fine." [long pause]

Transition: But a test set is never the real world. / So you keep testing after you ship.

## 6. Keep testing once it's live

(About 1 min 30 seconds)

Four ways to validate a release with real traffic. [pause]

▶ CLICK

**Shadow**. / Send a copy of real requests to the new version, / and compare its answers with the current one. / Users only ever see the current version, / so there's zero risk.


▶ CLICK

**Canary**. / Give the new version to a small share of users. / If an alarm fires, / roll back. / AWS AppConfig does exactly this for a prompt or a model ID.


▶ CLICK

**A/B test**. / Split users between two versions, / and compare what they do. / Thumbs up, / edits, / escalations to a human.


▶ CLICK

And **online evaluation**. / Every day, / score a sample of live answers with your judge model, / and chart the scores in CloudWatch. / Quality can drift without any change on your side, / for example when your users start asking new kinds of questions. [long pause]

Transition: Let's wrap up.

## 7. Lecture recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / score RAG in two halves. / Retrieval relevance and coverage, / then correctness and faithfulness. / That tells you **where** to fix.


▶ CLICK

Second, / judge agents by their path. / Task success, / tool calls, / trajectory, / safety, / and cost per task, / using traces.


▶ CLICK

And third, / gate every release. / A test set in the pipeline with a bar set in advance, / then shadow, / canary / and live scoring once it ships. [pause]

So, / back to our one sentence. [pause] Test **each part** on its own, / and make **passing the tests** the only way to ship. [long pause]

Transition: But even with all these tests, / things will break. / In the next lecture, / we'll troubleshoot the problems you'll actually meet.
