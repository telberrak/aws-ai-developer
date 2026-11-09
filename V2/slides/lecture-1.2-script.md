# Lecture 1.2: The exam: format, scoring and reading the questions — narration script

Section 1, Welcome and exam strategy. About 9 to 10 minutes. The same text is in the speaker notes of `lecture-1.2.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. The exam: format, scoring and reading the questions

(About 45 seconds)

In this lecture, / we're going to look at the exam itself. [pause]

I'll cover three things. / First, / the format: / how many questions, / what kind, / and how you pass. / Then, / how a professional-level question is built. / And finally, / a simple method you can use on every single question. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] On this exam, / the **constraints** decide the answer, / not the technology. / Keep that in mind, / because it'll come back again and again. [long pause]

Transition: First, / the numbers you need to know.

## 2. 75 questions, one pass mark

(About 1 min 15 s)

There are four numbers worth remembering. [pause]

▶ CLICK

The first one is **sixty-five**. / That's the number of questions that count towards your score.

▶ CLICK

The second is **ten**. / On top of those sixty-five, / AWS adds ten questions it's testing for future exams. / They're mixed in, / and they're not marked, / so you can't tell which ones they are. / That's seventy-five questions in total. / My advice: / treat every question as if it counts.

▶ CLICK

The third is **seven hundred and fifty**. / That's the pass mark, / on a scale from one hundred to one thousand. / Now, / it's a **scaled** score, / not a percentage. / Different versions of the exam can be a little harder or easier, / and the scaling evens that out. / So don't try to turn it into an exact number of correct answers.

▶ CLICK

And the fourth is **zero**. / That's the penalty for guessing. [pause]

▶ CLICK

So, / answer **every** question. / A blank answer is always wrong. / If you're running out of time, / pick your best guess, / flag it, / and move on. [long pause]

Transition: Now, / those questions come in two formats.

## 3. Two formats, one trap

(About 1 min)

There are two kinds of questions, / and one of them has a trap. [pause]

▶ CLICK

The first kind is **multiple choice**. / One correct answer, / and three wrong ones. / AWS calls the wrong ones distractors. / And here's the thing: / at this level, / distractors are rarely silly. / They're usually real services that would actually work. / They're just not the **best** answer / for what the question asks.

▶ CLICK

The second kind is **multiple response**. / Two or more correct answers, / out of five or more options. / The question always tells you how many to pick, / for example, / "Select TWO." [pause]

▶ CLICK

And this is the trap. / There's **no** partial credit. / If you pick one right answer and one wrong one, / you get zero for the whole question. [pause] So I treat each option on its own, / like a true-or-false question. / Does it meet every requirement? / Yes or no. / Then I pick exactly the number they ask for. [long pause]

Transition: Next, / let's look at how your answers turn into a pass.

## 4. You pass the exam, not each domain

(About 1 min)

Here's something a lot of people don't know. / You don't need to pass each domain. / You need to pass the **exam**. [pause] AWS calls this compensatory scoring. / In plain words, / your strengths can make up for your weaknesses.

▶ CLICK

So, / first, / you don't need to be perfect everywhere. / If you're strong on retrieval and agents, / but a bit weaker on evaluation, / you can still pass comfortably.

▶ CLICK

Second, / the weights tell you where the points are. / Domains 1 and 2 hold about **thirty-seven** of the sixty-five scored questions. / That's why they get the most time in this course.

▶ CLICK

And third, / after the exam you may get a breakdown by domain. / Read it with care. / With only seven or eight questions in a small domain, / a couple of lucky or unlucky answers / can swing that result a lot. [long pause]

Transition: So, / now let's open up a question / and see how it's built.

## 5. Every scenario has three parts

(About 1 min 15 s)

Every scenario question has the same three parts. / Once you see them, / you can't unsee them. [pause] This is a sample question I wrote in the exam's style. / Let me read it. [pause]

A company runs a support assistant on Amazon Bedrock. / Policy documents live in Amazon S3, / and they change several times a day. / Users report answers that quote outdated policies. / Answers must reflect changes within one hour, / with the least operational overhead. [pause]

▶ CLICK

The first part is the **context**. / That's what exists today. / Some of it matters, / but a lot of it is just scenery.

▶ CLICK

The second part is the **problem**. / Users are getting outdated answers. / That's the symptom you need to fix.

▶ CLICK

And the third part, / the most important one, / is the **constraints**. / Within one hour, / and with the least operational overhead. [pause] Several answers could fix stale answers. / Only one does it within an hour, / with the least effort to run. [pause] So here's my habit. / I read the **last** sentence first, / because it tells me what I'm optimizing for. [long pause]

Transition: And those constraints tend to repeat.

## 6. The constraint points to the answer

(About 1 min 15 s)

You'll notice the same constraint words coming back again and again. / And each one nudges you towards a family of answers. [pause]

▶ CLICK

When you read "**least operational overhead**", / lean towards managed Bedrock features / rather than something you build and run yourself.

▶ CLICK

"**Most cost-effective**" / points to smaller models, / caching, / and batch inference for work that isn't real-time.

▶ CLICK

"**Lowest latency**" / points to streaming, / caching / and latency-optimized inference.

▶ CLICK

"**Without code changes**" / points to configuration. / For example, / AWS AppConfig, / or prompt versions in Bedrock Prompt Management.

▶ CLICK

"**Must stay private**" / means VPC endpoints through PrivateLink, / encryption with KMS, / and tight IAM.

▶ CLICK

And "**auditable**" or "traceable" / points to CloudTrail, / Bedrock invocation logging / and model cards. [pause] Now, / these are habits, / not rules. / Always check the answer against **every** requirement, / not just the loudest one. [long pause]

Transition: So, / let's turn all of this into a method.

## 7. Four steps for every question

(About 1 min)

I use the same four steps on every question. / In quizzes, / and on the day. [pause]

▶ CLICK

Step one: / read the ask. / Go to the last sentence first. / Is it asking for the cheapest option, / the least effort, / the most secure? / That's how you'll judge every answer.

▶ CLICK

Step two: / list the constraints. / Time, / cost, / effort, / privacy, / scale. / The right answer has to meet **all** of them.

▶ CLICK

Step three: / eliminate. / Strike out any option that breaks even **one** constraint. / Usually, / two options go quickly.

▶ CLICK

Step four: / pick the best fit. / When two options both work, / the exam usually prefers the simpler, / more managed one, / unless the question gives you a reason not to. [pause]

▶ CLICK

And one time rule. / If you've spent two minutes on a question and you're still stuck, / guess, / flag it, / and move on. / You can come back with fresh eyes at the end. [long pause]

Transition: Let's try the method on our sample question.

## 8. Worked example: within 1 hour, least overhead

(About 1 min 15 s)

Let's apply it. / The ask is simple: / which solution meets the requirements? / And the constraints are: / fresh within one hour, / and least operational overhead. / Now, / let's eliminate. [pause]

▶ CLICK

Option A: / fine-tune the model every night. / Nightly can't meet one hour. / And honestly, / fine-tuning is the wrong tool for facts that change every day. / That's a job for retrieval. / So, / A is out.

▶ CLICK

Option D: / paste every policy document into every prompt. / It might work for a tiny set of documents, / but you'll hit the context window, / and you'll pay for those tokens on every request. / Out.

▶ CLICK

Option C: / a custom Lambda function that chunks the documents into a self-managed OpenSearch cluster on EC2. / Now, / this would actually **work**. / And that's exactly why it's a good distractor. / But you'd be running and patching your own cluster. / It fails least operational overhead. / Out. [pause]

▶ CLICK

That leaves **B**. / A Bedrock knowledge base with the S3 bucket as its data source, / and an ingestion job that starts whenever a document changes. / It's fully managed, / and updates show up in minutes. / That's our answer. [pause] And notice what decided it. / Not the technology. / The **constraints**. [long pause]

Transition: Okay, / let's wrap up.

## 9. Lecture recap: three things to remember

(About 45 seconds)

So, / let's bring it together. [pause]

▶ CLICK

First, / seventy-five questions, / sixty-five of them scored, / and a pass mark of seven hundred and fifty. / There's no penalty for guessing, / so never leave a blank.

▶ CLICK

Second, / multiple response has **no** partial credit. / Judge each option on its own, / and pick exactly the number they ask for.

▶ CLICK

And third, / use the four steps. / Read the ask, / list the constraints, / eliminate, / and pick the best fit. [pause]

So, / back to our one sentence. [pause] On this exam, / the **constraints** decide the answer, / not the technology. [long pause]

Transition: In the next lecture, / we'll set up your AWS account, / safely and cheaply, / so you're ready for the demos.
