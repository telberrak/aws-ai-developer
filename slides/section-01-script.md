# Section 1: Welcome and exam strategy — narration script

One block per slide, in deck order. The same text is in the speaker notes of `section-01-welcome-and-exam-strategy.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. Lines starting "Transition:" are the spoken bridge into the next slide.

## Lecture 1.1: how this course maps to AIP-C01 and how to use it

### Slide 1: Welcome and exam strategy

(About 80 seconds)

Welcome to the course. / My goal is simple. [pause] I want to get you through the AWS Certified Generative AI Developer Professional exam, / code **AIP-C01**, / on your **first** attempt, / and make you a better GenAI builder / along the way. [long pause]

This first section is short, / about forty-five minutes. And honestly, / it's the one people are most tempted to skip. [pause] Please don't. Across its six lectures, / we'll look at what the exam measures, / how it's scored, / how professional-level questions are written, / which AWS services matter and which ones are traps, / and how to set up your AWS account / so the labs don't surprise you with a bill.

We'll finish with a thirty-question diagnostic test. It tells you where you're starting from, / so you can spend your study time / where it counts. [pause]

This lecture maps the course to the exam. First, / what you'll be able to do by the end. Then, / who the exam is for, / the course map, / how each section works, / and a realistic pace. And everything here / is mapped to the official exam guide. [long pause]

Transition: So, / let's start with what you'll be able to do by the end.

### Slide 2: By the end, you’ll be able to

(About 90 seconds)

These eight outcomes come straight from the official exam guide. / They're what AWS says this certification validates, / so they're also the **promise** of this course. [pause]

Read them as job tasks, / not exam topics. The exam is aimed at someone who puts generative AI into **production**. You design a system that looks up your own documents before the model answers. That's retrieval augmented generation, / or RAG. You wire foundation models into real apps, / and manage prompts like code. You build agents that call tools. And you keep all of it secure, / affordable, / observable, / and measurably good. [pause]

Notice what's **missing**. Nothing about training a model from scratch, / or inventing new architectures. This is a **builder's** exam. Almost every question asks which AWS services and patterns you'd combine / to solve a business problem / under some constraint. [long pause]

If I had to sum up this lecture in one sentence, / it would be this. [pause] This is a builder's exam, / so we study where the points are, / and we build everything we study. [long pause]

That's how the course is built. Each lecture explains a concept, / shows how AWS does it, / then you build it in a lab. By exam day, / most scenarios should feel **familiar**.

Transition: Now, / let's be honest about who this exam is actually written for.

### Slide 3: Who this exam is written for

(About 90 seconds)

This exam is written for someone who **uses and customizes** models, / not someone who builds them. [pause] So let's be honest about what AWS expects.

AWS describes the target candidate as someone with **two or more years** building production applications, / on AWS or with open-source technologies. Some general AI, / machine learning, / or data engineering experience. And about **one year** of hands-on work / implementing generative AI. [pause]

You also need working AWS knowledge. Compute, / storage and networking. IAM and security best practices. Infrastructure as code. Monitoring and observability. And cost optimization.

If you're lighter on experience than that, / you can still pass. [pause] Section 2 is a refresher that covers the minimum, / and the labs give you the hands-on hours. Just plan a bit more time for the labs.

Now, / on the right / is the good news. Model development and training, / advanced machine learning techniques, / and data and feature engineering / are **explicitly** out of scope. You won't be asked to derive a loss function / or tune a training loop. [pause] You **will** be asked when to fine-tune / versus when to use retrieval, / and how to deploy and manage a customized model. That distinction will come up / again and again. [long pause]

Transition: So, / with that in mind, / here's the map of the whole course.

### Slide 4: Study time follows the exam weighting

(About 95 seconds)

Here's the point of this map. / Your study time follows the exam **weighting**. [pause]

The exam has five content domains, / each with a published weight. That's the share of scored questions / that come from it.

Domain 1, / foundation model integration, / data management and compliance, / is the biggest, / at **thirty-one percent**. That's where RAG, / vector stores, / retrieval, / chunking, / embeddings and prompt engineering live. Domain 2, / implementation and integration, / is **twenty-six percent**. Agents, / MCP, / deployment, / enterprise integration, / and the Bedrock APIs. [pause] Together, / those two are **fifty-seven percent** of your score. So they get the most time in this course. [long pause]

Domain 3, / AI safety, / security and governance, / is twenty percent. Guardrails, / PII, / private networking, / audit, / and responsible AI. Domains 4 and 5, / optimization, / and then testing and troubleshooting, / are twelve and eleven percent.

I've sized the video hours to match, / from nine and a half hours for Domain 1 / down to three for Domain 5. [pause] That doesn't mean you can skip the small domains. The exam needs a passing **total**, / and an easy seven or eight questions from Domain 5 / can be the difference. But if you're short on time, / depth in Domains 1 and 2 / pays back the most.

Then Sections 23 to 26 add the capstone, / a service review, / and four practice exams. [long pause]

Transition: So that's what we cover. Now let's look at how each section actually works.

### Slide 5: Learn it, build it, test it

(About 80 seconds)

Every section follows the same rhythm. / Learn it, / build it, / test it. [pause] So you always know what's coming.

First, / short lectures. Usually five to twelve minutes, / and each one focuses on a **single** topic you need for the exam.

Second, / a lab. You'll build the thing for real, / in your own AWS account, / in Python with the AWS CDK. Every lab in the course repo has a README, / an estimated cost, / and a **teardown** command. [pause] Run the teardown **every single time**. I'll keep reminding you. [long pause]

Third, / a quiz of ten to fifteen questions, / written in the same style as the exam. Every option has a full explanation, / including why the wrong answers are wrong.

And finally, / at the end of each domain, / there's a **checkpoint**. That's a timed mini exam across everything in that domain. My rule of thumb: / get **seventy-five percent** or better / before you move on. [pause] If you don't, / the results show you which topics to revisit. And that review is usually only an hour or two. [long pause]

Transition: So how do you fit all of that into your week? Let me show you a realistic pace.

### Slide 6: Six weeks at 8–10 hours a week

(About 90 seconds)

Here's a realistic pace. / **Six weeks**, / at eight to ten hours a week. [pause] If you already build with Bedrock every day, / you can compress this. Newer to GenAI? / Stretch it to eight weeks, / and spend the extra time in the labs.

Week one covers this section, / the refresher, / and the first three Domain 1 sections, / and ends with the diagnostic done. Week two finishes Domain 1: / vector stores, / retrieval and prompt engineering. It's the **heaviest** week, / and the most valuable.

Week three is Domain 2, / agents. Week four is safety, / security and governance. Each domain ends with its checkpoint, / at seventy-five percent or more. Week five covers optimization, / monitoring, / evaluation and troubleshooting, / and you build the **capstone** / that pulls it all together.

Week six is the service review / and the four practice exams. Book your real exam when you've scored **eighty percent** or more / on **two** practice exams. [pause] Not one lucky run. Two. [long pause]

One tip. Put your study sessions in your calendar **now**, / like a meeting. Consistency beats intensity / for an exam this broad.

Back to our one sentence. This is a builder's exam, / so we study where the points are, / and we build everything we study. [long pause]

Transition: Next, / in Lecture 1.2, / let's look at the exam itself: / the format, / the question types, / and the scoring.

## Lecture 1.2: exam format, question types and scoring

### Slide 7: Exam format and scoring

(About 30 seconds)

Lecture 1.2. Before we study a single service, / let's understand the exam itself. [pause]

Three steps. First, / the exam in four numbers. Then, / the two question types. And finally, / how scoring works, / and what it means on the day.

It's quick, / but it changes how you answer questions. Especially the **multiple-response** ones, / which catch out a lot of experienced engineers. [long pause]

Transition: So, / let's start with four numbers.

### Slide 8: 75 questions, one pass mark

(About 90 seconds)

There are four numbers to remember. [pause]

**Sixty-five** scored questions. **Ten** extra unscored questions / that AWS is testing for future exams. They're mixed in and not marked, / so you can't tell which ones they are. Treat every question as if it counts. That's **seventy-five** questions in total. [pause]

**Seven fifty**. That's the pass mark, / on a scaled range from one hundred to one thousand. It's a **scaled** score, / not a percentage. Exam forms can be slightly harder or easier, / and scaling evens that out. So don't turn seven fifty / into an exact number of right answers. In practice, / aiming for around eighty percent on good practice exams / gives you a comfortable margin.

And **zero**. [pause] No penalty for guessing. An unanswered question is scored as wrong, / so never leave anything blank. If you're running out of time, / pick your best guess and flag it. [long pause]

If I had to sum up this lecture in one sentence, / it would be this. [pause] You pass on your **total**, / so answer every question, / and don't throw points away on multiple response. [long pause]

Before you book, / check the AWS Certification website for the current duration, / price and delivery options. Those details aren't in the exam guide, / and they can change.

Transition: Now, / let's look at the two question formats, / and the one trap inside them.

### Slide 9: Two formats, one trap

(About 80 seconds)

There are two question formats, / and one of them has a **trap**. [pause]

Multiple choice has one correct answer / and three incorrect ones. AWS calls those **distractors**. At the professional level, / distractors are rarely nonsense. They're usually real services or real patterns / that would work. [pause] They just aren't the **best** answer / for the constraint in the question, / like lowest cost, / or least operational overhead. So your job is to find the best fit, / not just something that works.

Multiple response has two or more correct answers, / out of five or more options. The question tells you how many to pick, / for example, / "Select TWO." [pause] And here's the trap. There's **no** partial credit. If you pick one right and one wrong, / you get **zero** for that question. [long pause]

So treat multiple response / as a set of independent true-or-false judgments. Go through each option on its own, / and ask: / does this meet **every** requirement in the scenario? Then pick exactly the number asked.

Our quizzes and practice exams include plenty of these, / about thirty percent, / so you'll get used to the rhythm. [pause]

Transition: And that brings me to how the whole exam is scored.

### Slide 10: You pass the exam, not each domain

(About 100 seconds)

You pass the **exam**, / not each domain. [pause] AWS calls this **compensatory** scoring. You need a passing score overall, / not in each domain. Your strengths can make up for your weaknesses.

Three practical points. [pause]

One. You don't need to be perfect everywhere. If you're excellent at RAG and agents, / but shakier on evaluation, / you can still pass comfortably. A strong Domain 1 can offset a weaker Domain 5.

Two. The domain weights tell you where the points are. Domains 1 and 2 are thirty-one and twenty-six percent. That's roughly **thirty-seven** of the sixty-five scored questions, / so they get the most time. [pause] Small domains still matter, though. Domain 5 is around seven questions, / and those are often very answerable / if you've done the labs.

Three. After the exam, / you may get a table showing how you did in each section. AWS warns you to read it with caution. With only seven or eight questions in a domain, / a couple of lucky or unlucky answers / swing the result a lot. [pause] The same goes for our checkpoints and practice exams. That's why I give you feedback on each topic area, / across many questions, / instead of one score. [long pause]

So, / back to our one sentence. You pass on your total, / so answer every question, / and don't throw points away on multiple response. [long pause]

Transition: Next, / Lecture 1.3, / and in my view the most important one in this section: / how to read professional-level scenarios.

## Lecture 1.3: reading professional-level scenarios

### Slide 11: Reading professional-level scenarios

(About 45 seconds)

Lecture 1.3. And this is the **most important** lecture in the section. [pause]

Professional-level AWS questions are long. They describe a company, / a system, / a problem, / and a set of requirements. Then they give you four or five answers / that **all** look plausible. Knowing the services is necessary, / but it isn't enough. You also need a **method** / for reading the question. [long pause]

So we'll go in four steps. First, / the anatomy of a scenario question. Then, / the constraint words that decide the answer. Then, / a four-step elimination method. And finally, / we'll walk through a full example together. [pause]

Transition: Let's start by taking one question apart.

### Slide 12: Every scenario has three parts

(About 95 seconds)

Every scenario has three parts, / and the last one decides the answer. [pause] Here's a sample question I wrote in the style of the exam. It isn't a real exam question, / but it's built the same way.

First, / the **context**, / in blue. A company runs a support assistant on Amazon Bedrock. Policy documents live in S3, / and they change several times a day. Context tells you what already exists. Some of it matters. A lot of it / is scenery.

Second, / the **problem**. Users get answers that quote outdated policies. That's the symptom you need to fix.

Third, / and most important, / the **constraints**, / in orange. Answers must reflect changes within **one hour**, / with the **least operational overhead**. [pause] Constraints separate a working answer / from the best answer. Several options here would technically fix stale answers. Only one does it within an hour, / with the least effort to run. [long pause]

So, / if I had to sum up this lecture in one sentence, / it would be this. [pause] The **constraints** decide the answer, / not the technology. [long pause]

My habit, / and I recommend it to you: / read the **last sentence** of the question first. It tells you what you're being asked to optimize. Then read the scenario with that in mind, / and mentally underline every constraint.

Transition: Now, / some constraint phrases come up again and again. Let's look at them.

### Slide 13: The constraint points to the answer

(About 80 seconds)

A handful of constraint phrases appear again and again. / And each one nudges you towards a **family** of answers. [pause]

"Least operational overhead" means prefer managed, / serverless features, / where AWS runs the plumbing for you. If Bedrock Knowledge Bases can do it, / it usually beats a hand-built pipeline on EC2.

"Most cost-effective" points at smaller or cheaper models, / caching, / batch inference for work that isn't real-time, / and on-demand rather than provisioned throughput, / unless usage is steady and high.

"Lowest latency" points at streaming responses, / caching, / latency-optimized inference, / and, / for steady heavy traffic, / provisioned throughput.

"Without code changes", / or "without redeploying", / points at configuration. AppConfig, / Prompt Management versions, / and routing driven by config.

"Must not traverse the public internet", / or "must stay private", / means private network endpoints. That's VPC interface endpoints through PrivateLink, / plus encryption with KMS / and tight IAM.

And "auditable" or "traceable" / points at CloudTrail, / Bedrock model invocation logging, / model cards, / and data lineage. [pause]

Now, / these are **heuristics**, / not rules. [pause] Always check the answer against **every** requirement in the question, / not just the loudest one. [long pause]

Transition: So how do you put this together on a real question? Here's the method.

### Slide 14: Four steps for every question

(About 80 seconds)

Here's the four-step method I want you to use on **every** question. / In quizzes, / in practice exams, / and on the day. [pause]

Step one: / **read the ask**. Go to the last sentence first. Is it asking for the most cost-effective option? The least operational overhead? The most secure? That's your scoring rule.

Step two: / **list the constraints**. Scan the scenario for every requirement. Time limits, / cost, / effort, / privacy, / scale, / regions, / compliance. Every one of them / has to be met by the right answer.

Step three: / **eliminate**. Go through the options, / and strike any that break even **one** constraint. Usually you can remove two options quickly.

Step four: / **pick the best fit** from what's left. When two options both work, / the exam usually prefers the simpler, / more managed one. Unless the question gives a reason not to, / like a need for custom control. [long pause]

And a time rule. [pause] If you've spent **two minutes** on a question and you're still stuck, / pick your best guess, / flag it for review, / and move on. You can come back with fresh eyes / at the end. [long pause]

Transition: So, / let's apply the method to our sample question.

### Slide 15: Within 1 hour, least overhead

(About 100 seconds)

Let's apply the method to our sample question, / and watch the constraints do the work. [pause]

Step one, / the ask: / which solution meets the requirements. Step two, / the constraints: / answers must reflect document changes within **one hour**, / with the **least operational overhead**.

Now, / eliminate. Option A: / fine-tune the model every night. Nightly can't meet a one-hour freshness requirement. And fine-tuning is the wrong tool for facts that change daily. That's retrieval's job. It's also expensive and effortful. [pause] Out.

Option D: / paste every policy document into every prompt. It might work for a tiny corpus. But it runs into context window limits, / and it burns tokens on every request. Out, / on cost and scale.

Option C: / a custom Lambda function that chunks documents / into a self-managed OpenSearch cluster on EC2. This would actually work. [pause] And that's exactly what makes it a **good distractor**. But you'd be running and patching your own cluster and pipeline. It fails "least operational overhead."

That leaves **B**. A managed index over your documents, / a Bedrock knowledge base, / with the S3 bucket as its data source, / and an ingestion job triggered whenever objects change. It's fully managed, / and updates show up in minutes. That's our answer. [long pause]

So, / back to our one sentence. The **constraints** decide the answer, / not the technology. You'll see this pattern constantly. [long pause]

Transition: Next, / Lecture 1.4: / which services are in scope, / and which look-alikes to ignore.

## Lecture 1.4: in-scope versus out-of-scope services

### Slide 16: In-scope versus out-of-scope services

(About 25 seconds)

Lecture 1.4. The exam guide lists more than a hundred services and features as in scope, / and dozens more as **out** of scope. [pause] That sounds overwhelming. But most of the exam leans on a much smaller core.

Two steps. First, / that core shortlist, / grouped by job. Then, / the out-of-scope services / that most often show up / as tempting wrong answers. [long pause]

Transition: Let's start with the shortlist.

### Slide 17: Know these six groups cold

(About 105 seconds)

If you only had time to master a few dozen services, / these are the ones. [pause] I've grouped them by the **job** they do in a GenAI application.

First, / and most important, / **Amazon Bedrock** and its family. The models themselves. Managed RAG, / which is Knowledge Bases. Safety controls, / which is Guardrails. Prompt Management and Prompt Flows, / for your prompts. And AgentCore, / for running agents. Expect Bedrock in a **large** share of questions.

Second, / orchestration. Step Functions, / Lambda, / API Gateway, / EventBridge, / SQS and AppConfig. These are the glue / that turns a model call into a workflow.

Third, / data and search. S3, / OpenSearch Service, / Aurora with pgvector, / DynamoDB and ElastiCache. That's where your documents, / vectors, / conversation history and caches live.

Fourth, / SageMaker AI, / for when you host or customize your own models. Endpoints, / JumpStart, / Model Registry, / Clarify and Model Monitor.

Fifth, / the language AI services. Comprehend, / Transcribe, / Textract, / Macie for PII in S3, / and Augmented AI for human review.

And sixth, / operate and secure. CloudWatch, / CloudTrail, / X-Ray, / IAM, / KMS, / and VPC endpoints. [pause]

Beyond AWS services, / the exam also covers **Strands Agents**, / **AWS Agent Squad**, / and the **Model Context Protocol**, / or MCP. Make sure you're comfortable with all three. We cover them in Section 9. [long pause]

If I had to sum up this lecture in one sentence, / it would be this. [pause] Know the core shortlist **cold**, / and never build an answer / around a service that's out of scope. [long pause]

Transition: Which brings me to the flip side: / the look-alikes.

### Slide 18: Don’t design with these

(About 100 seconds)

Now the flip side. / The exam guide also publishes a list of **out-of-scope** services. [pause] And honestly, / it's a gift, / because it tells you which tools to stop thinking about.

On the left, / out-of-scope services that sound relevant to GenAI work. On the right is the in-scope service the exam expects you to use for that job instead.

Amazon Redshift is out. For analytics and search, / think Athena, / OpenSearch Service and Aurora. AWS Budgets and Savings Plans are out. For cost questions, / reach for Cost Explorer and Cost Anomaly Detection. DevOps Guru is out. Use CloudWatch anomaly detection. [pause]

Direct Connect, / VPN and Transit Gateway are out. For private connectivity, / think PrivateLink and VPC endpoints, / and Outposts for on-premises. AWS Batch is out. For bulk inference, / think Bedrock batch inference and Step Functions. And Amazon SES is out. For notifications, / think SNS. [pause]

The guide says out-of-scope services **won't** appear on the exam at all. So the value of this list / is in your own head. When you design an answer to a scenario, / it stops you reaching for a tool the exam doesn't test, / and pushes you to the in-scope service it does. The full lists are in the downloadable cheat sheet for this lecture. [long pause]

So, / back to our one sentence. Know the core shortlist cold, / and never build an answer around a service that's out of scope. [long pause]

Transition: Next, / Lecture 1.5. Let's set up your lab account, / safely.

## Lecture 1.5: setting up your AWS account safely

### Slide 19: Setting up your lab account

(About 30 seconds)

Lecture 1.5. You'll do **twenty-three** labs in this course, / and you'll learn more from them than from any video. [pause] So let's set up an AWS account properly, / once, / and protect it from surprise bills.

Two steps: / a six-step setup checklist, / then three rules for cost safety. Pause the video and follow along. By the end, / you'll have made your first Bedrock call. [long pause]

Transition: Let's go through the checklist.

### Slide 20: Six steps before your first lab

(About 105 seconds)

Six setup steps. / I'll do each one on screen, / so pause and follow along. [pause]

One. Use a dedicated AWS account, / or a sandbox account in your organization. **Never** run course labs in a production account.

Two. Don't work as the root user. Turn on MFA for root, / then create an admin user through IAM Identity Center, / and use that from now on.

Three. Before anything else, / set a **billing alarm** at a low monthly amount you're comfortable with. Then turn on the service that flags unusual spending, / Cost Anomaly Detection. That's our first taste of a service that's on the exam.

Four. Pick **one** region and stay in it, / one where Bedrock offers a wide range of models. I'll show you how to check model availability in the console, / and the repo README lists the region I use.

Five. In the Bedrock console, / enable access to the models the labs use. The list is in the repo.

Six. Install the AWS CLI, / Python 3 and the AWS CDK, / and clone the course repo. The full guide is in the repo's setup README. [pause]

You're done when "aws sts get-caller-identity" returns your user, / and the repo's smoke test gets an answer back from a Bedrock model. [pause] Congratulations. That's your first FM integration. [long pause]

If I had to sum up this lecture in one sentence, / it would be this. [pause] Set up your account **once**, / properly, / and tear down every lab / the **same day**. [long pause]

Transition: And that brings us to three rules for cost safety.

### Slide 21: Three rules that keep labs cheap

(About 80 seconds)

Three rules keep the labs **cheap**. [pause]

Rule one: / tear down the **same day**. Every lab ships with a teardown command. Run it before you close your laptop, / even if you plan to continue tomorrow. Redeploying with CDK takes minutes. And paying for idle resources overnight / is the most common way students get a surprise bill. [long pause]

Rule two: / watch the **always-on** resources. Most of what we build is serverless, / and costs very little when idle. The exceptions are provisioned throughput in Bedrock, / OpenSearch clusters, / and SageMaker endpoints. They bill **by the hour**, / whether you use them or not. Whenever a lab uses one, / I'll put a warning on screen.

Rule three: / check your spend **weekly**. Open Cost Explorer, / group by service, / and make sure nothing's growing / that shouldn't be.

Every lab README states its estimated cost, / so you know what to expect before you deploy. Follow these three rules, / and the whole course stays affordable. [pause]

So, / back to our one sentence. Set up your account once, / properly, / and tear down every lab the same day. [long pause]

Transition: Next, / the last lecture in this section, / Lecture 1.6: / the diagnostic test.

## Lecture 1.6: the diagnostic test and what comes next

### Slide 22: Diagnostic test

(About 25 seconds)

Lecture 1.6, / the last in this section. Before you start studying, / you'll take a short **diagnostic** test. [pause]

I know. A test before you've learned anything sounds harsh. [pause] But it's the fastest way to find out what you already know, / so you can spend your time on what you don't.

Two steps: / how it works, / then reading your result. [long pause]

Transition: So, / here's how it works.

### Slide 23: 30 questions, no studying first

(About 95 seconds)

Here's how the diagnostic works. / Thirty questions, / and **no** studying first. [pause]

It's weighted like the real exam. Nine from Domain 1, / eight from Domain 2, / six from Domain 3, / four from Domain 4, / and three from Domain 5. Plan on about forty-five minutes, / but there's no timer. Don't look anything up. We want an **honest** baseline.

Answer every question, / even if you're guessing, / and use the **confidence** marker on each one. A correct guess and a confident correct answer / mean very different things for your study plan.

When you finish, / you'll see a score per domain. Use the table on the right. Under fifty percent: / every lecture in full, / and every lab. Between fifty and seventy-five: / lectures at one and a quarter speed, / but still **all** the labs, / because the labs build the exam-style intuition. Over seventy-five: / skim the lectures, / do the labs, / and go straight to the section quizzes to confirm. [pause]

If I had to sum up this lecture in one sentence, / it would be this. [pause] The diagnostic isn't a grade. / It's a **map** of where to spend your time. [long pause]

And please don't be discouraged by a low score. On a professional-level exam, / a low diagnostic score is completely **normal**. That's exactly why you're here.

Transition: So, / let's wrap up the section, / and see what comes next.

### Slide 24: Take the diagnostic, then meet Amazon Bedrock

(About 70 seconds)

That's the end of Section 1. / Let's recap quickly. [pause]

You know what the exam validates, / and who it's for. You know the format: / sixty-five scored questions, / a seven fifty pass mark, / compensatory scoring, / and no penalty for guessing. You have a four-step method for reading scenarios. You know the core service shortlist. And your lab account is set up / and safe. [long pause]

Your next step is the diagnostic test, / right after this video. Take it **now**, / while this section is fresh, / and note your **weakest** domain. [pause] Remember, / it isn't a grade. It's a map of where to spend your time.

Then join me in Section 2, / where we refresh the generative AI fundamentals on AWS. Tokens and inference parameters. A tour of Amazon Bedrock and the Converse API. When SageMaker AI fits instead. And the four core architecture patterns / you'll see across the whole exam. You'll also make your first Bedrock call from Python.

Transition: So, / take the diagnostic, / and I'll see you in Section 2, / where we meet Amazon Bedrock.
