# Lecture 11.4: Responsible AI — narration script

Section 11, Security, privacy, governance and responsible AI. About 12 minutes. The same text is in the speaker notes of `lecture-11.4.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Responsible AI

(About 40 seconds)

So far in this section, / we've locked down the infrastructure, / protected personal data / and put governance in place. [pause] Now the harder question. / Is the system **fair**, / **honest** about what it is, / and **safe** for the people who use it? [pause] That's responsible AI. / And on AWS, / it isn't a slogan. / It's a set of things you can measure and enforce. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Responsible AI means you **measure** fairness and safety like any other quality, / and you keep a **human** in charge of the decisions that matter. [long pause]

Transition: So, / what does responsible AI mean in practice?

## 2. Five ideas you can build and check

(About 1 min 30 seconds)

Five ideas, / and each one turns into something you can build or check. [pause]

▶ CLICK

First, / **transparency**. / People should know they're talking to AI, / where the answer came from, / and what the system can't do.


▶ CLICK

Second, / **fairness**. / The system shouldn't treat people differently because of who they are. / Their gender, / their age, / their name or their accent.


▶ CLICK

Third, / **safety and robustness**. / No toxic or harmful output, / and answers that don't fall apart when someone rephrases the question or makes a typo.


▶ CLICK

Fourth, / **policy compliance**. / The answers follow your company's rules, / and the regulations you're under.


▶ CLICK

And fifth, / **human oversight**. / For decisions with real impact, / a person reviews, / approves / or can step in. [pause] Keep these five in mind. / The rest of this lecture is how you put each one into practice. [long pause]

Transition: First, / transparency.

## 3. Tell people the truth about the system

(About 1 min 30 seconds)

Transparency is mostly about **telling people the truth** about the system. [pause]

▶ CLICK

First, / **disclose** that it's AI. / A label in the chat window, / or a line in the generated email. / Many regulations now expect it.


▶ CLICK

Second, / **show your sources**. / With Bedrock Knowledge Bases, / RetrieveAndGenerate returns **citations**, / so the user can check where an answer came from.


▶ CLICK

Third, / **document the model**. / SageMaker Model Cards record what the model is for, / how it was trained and evaluated, / and its known limits. / And AWS publishes AI Service Cards for its own models.


▶ CLICK

And fourth, / **state the limits**. / What the assistant can't do, / and when to ask a human instead. [pause]


▶ CLICK

Here's the point. / Transparency builds **trust**. / And it also protects you, / because users who know the limits are less likely to rely on a wrong answer. [long pause]

Transition: Next, / fairness. / How do you actually measure it?

## 4. Measure it by comparing outcomes

(About 2 minutes)

You measure fairness by **comparing outcomes** across groups. / Four steps. [pause]

▶ CLICK

First, / **check the data**. / If you train or fine-tune, / SageMaker Clarify can measure bias in the training data before you train, / for example when one group is badly under-represented.


▶ CLICK

Second, / **test the model**. / Clarify also runs foundation model evaluations, / including a **stereotyping** check that measures whether the model prefers biased sentences.


▶ CLICK

Third, / use **counterfactual pairs**. / Send the same prompt twice, / and change only one detail. / A woman's name instead of a man's, / say. / Then compare the answers. / A loan summary shouldn't change because the name changed.


▶ CLICK

Fourth, / let a **model judge** the pairs. / An LLM-as-a-judge compares the two answers, / and flags differences in tone, / in quality / or in the decision. / That scales to thousands of pairs, / which no human team could read.


▶ CLICK

And the key idea. / Fairness becomes a **number** you track, / like latency. / Set a threshold, / run it on every release, / and treat a drop as a failed test. [long pause]

Transition: What about safety and robustness?

## 5. Bedrock model evaluations do the heavy lifting

(About 1 min 30 seconds)

Here, / Amazon Bedrock's **model evaluations** do most of the work. [pause]

▶ CLICK

**Automatic** evaluations use built-in metrics and datasets. / Accuracy, / **robustness**, / which checks if small changes to the prompt change the answer, / and **toxicity**.


▶ CLICK

**Model as a judge** evaluations score your own prompts. / Besides correctness, / the judge can score responsible AI metrics, / like **harmfulness**, / **stereotyping** / and how often the model refuses.


▶ CLICK

**Human** evaluations bring in your own reviewers, / or an AWS-managed team, / for the things that need judgment.


▶ CLICK

And all three can use **your own dataset**. / Built-in datasets are a good start, / but your users' real questions are what matter. [pause]


▶ CLICK

Remember this. / Run these evaluations **before** you pick a model, / and again on **every change**. / A new model version can be more capable, / and still more toxic on your data. [long pause]

Transition: Then there's your company's own rulebook.

## 6. Turn the rulebook into controls

(About 1 min 30 seconds)

Policy compliance means the system follows **your rules**, / and you can prove it. [pause]

▶ CLICK

First, / **Bedrock Guardrails**. / Denied topics, / content filters / and word filters turn your content policy into something enforced on every request.


▶ CLICK

Second, / **automated reasoning checks**. / You turn a written policy, / like an HR or lending rulebook, / into logical rules, / and the guardrail checks if an answer is consistent with them.


▶ CLICK

Third, / a **release gate**. / Your policy test cases run in the pipeline, / and a change that breaks one doesn't ship.


▶ CLICK

And fourth, / an **audit trail**. / Model invocation logging, / CloudTrail, / and the guardrail's own intervention metrics show what was asked, / what was blocked / and who changed what.


▶ CLICK

So, / policy goes from a PDF that nobody reads, / to controls that run on **every request**. [long pause]

Transition: And finally, / the human.

## 7. The model assists, a person stays accountable

(About 1 min 30 seconds)

Some decisions are too important to leave to a model alone. [pause]

▶ CLICK

First, / a **human in the loop** for high-impact decisions. / Loans, / medical advice, / hiring. / Amazon Augmented AI sends low-confidence or high-risk cases to a reviewer.


▶ CLICK

Second, / **feedback from users**. / A thumbs up or down, / or a report button. / It's the cheapest signal you'll ever get.


▶ CLICK

Third, / an **escalation path**. / The assistant can always hand over to a person, / and the user knows how to ask for one.


▶ CLICK

And fourth, / **regular audits**. / Someone reviews a sample of real conversations, / and the fairness and safety numbers, / every month.


▶ CLICK

The pattern is simple. / The model **assists**. / A **person** stays accountable. [long pause]

Transition: Let's wrap up.

## 8. Lecture recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / be **transparent**. / Disclose the AI, / cite your sources, / and document the model with model cards.


▶ CLICK

Second, / **measure** fairness and safety. / Clarify, / counterfactual pairs, / a model as judge, / and Bedrock evaluations, / on every release.


▶ CLICK

And third, / **enforce** your policies, / and keep a **human** in charge. / Guardrails and automated reasoning on every request, / and Augmented AI for the decisions that matter. [pause]

So, / back to our one sentence. [pause] Responsible AI means you **measure** fairness and safety like any other quality, / and you keep a **human** in charge of the decisions that matter. [long pause]

Transition: In the next lecture, / we put every control from this domain into one picture.
