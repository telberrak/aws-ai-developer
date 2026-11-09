# Lecture 13.1: Evaluation metrics and Bedrock evaluations — narration script

Section 13, Evaluation and troubleshooting. About 12 minutes. The same text is in the speaker notes of `lecture-13.1.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Evaluation metrics and Bedrock evaluations

(About 50 seconds)

Welcome to Section 13, / the last technical section of the course. / This is Domain 5, / testing, / validation / and troubleshooting. [pause] You've built the app. / Now the question is simple. / How do you **know** it's good, / and what do you do when it isn't? [pause] In this first lecture, / I'll show you the qualities you can measure, / the scores that can fool you, / the three ways Amazon Bedrock can run the tests for you, / and why your test set matters more than any of them. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Pick the **qualities** that matter, / score them the **right way**, / and test on **your own data**. [long pause]

Transition: So, / what does "good" actually mean for a generated answer?

## 2. Six qualities you can measure

(About 2 min)

With classic machine learning, / you had one number. / Accuracy. / With generated text, / there's no single right answer, / so you measure several qualities. / Here are six. [pause]

▶ CLICK

**Correctness**. / Does the answer match the facts, / or the reference answer you wrote for that question?


▶ CLICK

**Relevance**. / Does it answer the question that was actually asked? / A correct answer to a different question / is still a bad answer.


▶ CLICK

**Faithfulness**. / Is every claim backed by the context the model was given? / This is your hallucination check, / and in RAG, / it's the one that matters most.


▶ CLICK

**Coherence and style**. / Is it clear, / well structured, / and in the tone your brand expects?


▶ CLICK

**Harm and toxicity**. / Does the answer contain anything unsafe, / biased / or offensive?


▶ CLICK

And **robustness**. / Does the answer stay correct / when the user makes a typo, / or asks the same thing in different words? [pause] You won't need all six for every app. / A support bot lives or dies on correctness and faithfulness. / A marketing writer cares a lot more about style. [long pause]

Transition: Now, / you've probably heard of scores like ROUGE and BLEU. / Can you trust them?

## 3. ROUGE, BLEU and BERTScore can mislead

(About 1 min 45 seconds)

These are the classic scores from language research. / They compare the model's answer / with a reference answer. [pause]

▶ CLICK

**ROUGE** counts the words and phrases the two texts share. / It was built for summaries.


▶ CLICK

**BLEU** looks for exact word sequences in common. / It was built for translation.


▶ CLICK

**BERTScore** is smarter. / It compares **meaning**, / using embeddings, / so a paraphrase can still score well.


▶ CLICK

And here's the trap. [pause] A perfectly correct answer, / written in different words, / can get a **low** ROUGE score. / And a fluent answer with one **wrong number** in it / can score **high**, / because almost every word matches. [pause] So use these scores to spot trends between versions. / But don't let them be the final word on whether an answer is right. [long pause]

Transition: So, / how do you get better scores, / at scale? / That's where Bedrock comes in.

## 4. Three ways to score a model

(About 2 min)

Amazon Bedrock has evaluation jobs built in, / and they come in three flavors. [pause]

▶ CLICK

**Automatic** evaluation. / Bedrock runs your prompts through a model / and scores the answers with built-in metrics, / like accuracy, / robustness / and toxicity. / You can use its built-in datasets, / or bring your own. / It's fast, / cheap / and repeatable, / but it can't judge nuance.


▶ CLICK

**Human** evaluation. / Your own reviewers rate the answers in a work portal, / using the criteria **you** define. / Maybe it's brand voice, / or whether a medical answer is safe to send. / This is the best way to judge nuance, / but it's slower, / and it costs people's time.


▶ CLICK

And **LLM-as-a-judge**. / A second model, / the judge, / reads each answer and scores it. / Bedrock gives you built-in metrics like correctness, / completeness, / faithfulness / and harmfulness, / and you can add your own. / You get close to human judgment, / at machine scale.


▶ CLICK

And all three work the same way. / Your dataset sits in S3. / You pick the models to test / and the metrics. / The job writes a report back to S3, / and you can compare runs side by side. / So when a new model comes out, / you just run the same job again. [long pause]

Transition: But a judge is only useful if you can trust it. / So how do you make sure of that?

## 5. Make the judge trustworthy

(About 1 min 30 seconds)

Four habits make a judge trustworthy. [pause]

▶ CLICK

First, / give it a **rubric**. / Clear criteria, / and a fixed scale. / "Rate correctness from one to five, / where five means every fact matches the reference." / Never just "is this answer good?"


▶ CLICK

Second, / use a **different**, / strong model as the judge. / A model tends to favor answers that sound like its own.


▶ CLICK

Third, / **check it against humans**. / Have people score a sample of the same answers. / If they often disagree with the judge, / fix the rubric before you trust the numbers.


▶ CLICK

And fourth, / watch for the **known biases**. / Judges can prefer longer answers, / or whichever option they see first. [pause] Do those four things, / and a judge model is one of the most useful tools you have. [long pause]

Transition: But every method we've seen depends on one thing. / The data you test with.

## 6. Your test set decides everything

(About 2 min)

Your test set, / sometimes called a golden set, / decides everything. / A great metric on bad data / still tells you nothing. / So what goes in it? [pause]

▶ CLICK

**Real prompts**. / Take them from your logs, / or from the people who'll actually use the app. / Not the questions **you** think they'll ask.


▶ CLICK

**Expected answers**. / A reference answer for each prompt, / written or approved by someone who knows the subject.


▶ CLICK

**Edge cases and attacks**. / Ambiguous questions, / questions where the answer isn't in the data, / and inputs that try to break your app.


▶ CLICK

And **categories**. / Tag each prompt by topic, / so when quality drops, / you can see **where** it dropped.


▶ CLICK

In Bedrock, / your own dataset is a JSONL file. / One JSON object per line, / with the prompt, / the reference response, / and the category.


▶ CLICK

And treat it like code. / Keep it **versioned**, / in S3 or in Git. / Every time you find a bug in production, / add it to the set, / so it can never come back unnoticed. / And never test on the same examples you put in your prompt. / That's like giving students the exam answers. [long pause]

Transition: Let's wrap up.

## 7. Lecture recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / measure the right qualities. / Correctness, / relevance, / faithfulness, / style, / harm / and robustness. / And treat overlap scores like ROUGE and BLEU as trends, / not truth.


▶ CLICK

Second, / choose how to score. / Automatic for speed, / humans for nuance, / and a judge model with a clear rubric / for scale.


▶ CLICK

And third, / build a real test set. / Real prompts, / reference answers, / edge cases, / and versioned like code. [pause]

So, / back to our one sentence. [pause] Pick the **qualities** that matter, / score them the **right way**, / and test on **your own data**. [long pause]

Transition: In the next lecture, / we apply all of this to RAG and agents, / and turn evaluation into a gate your pipeline can't skip.
