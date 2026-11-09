# Lecture 1.3: Setting up your AWS account safely — narration script

Section 1, Welcome and exam strategy. About 4 to 5 minutes. The same text is in the speaker notes of `lecture-1.3.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Setting up your AWS account safely

(About 40 seconds)

In this lecture, / we're going to get your AWS account ready for the demos and the labs. [pause]

I'll keep it practical. / First, / six setup steps, / in the order I'd do them. / Then, / three simple rules / that keep your bill small. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Set up **once**, / safely, / and you'll never worry about a surprise bill. / Keep that in mind, / because a surprise bill is the most common way people lose motivation. [long pause]

Transition: First, / the setup.

## 2. Six steps before your first demo

(About 2 min)

There are six steps, / and I'll go through them in order. [pause]

▶ CLICK

Step one: / use a **dedicated** account. / Either a fresh AWS account, / or a sandbox account in your organization. / Never run course work in a production account. / That's simply not an option.

▶ CLICK

Step two: / stop using the root user. / Turn on multi-factor authentication for root, / then create an admin user through IAM Identity Center, / and use that from now on.

▶ CLICK

Step three: / before you build anything, / set a **budget**. / Create an AWS Budgets alert at a low monthly amount you're comfortable with, / and turn on Cost Anomaly Detection. / And here's a bonus. / Cost Anomaly Detection is also something the exam can ask about.

▶ CLICK

Step four: / pick **one** Region, / and stay in it. / Choose one where Bedrock offers a wide choice of models. / That way, / everything you build in this course lives in one place.

▶ CLICK

Step five: / check your model access. / In the Bedrock console, / make sure the models we'll use are available to your account. / Some providers ask for a short use-case form the first time, / so do it now, / not in the middle of a demo.

▶ CLICK

Step six: / install your tools. / The AWS CLI, / Python 3 / and the AWS CDK. / Then download the course files. [pause]

▶ CLICK

So, / how do you know you're ready? / Two checks. / First, / run "aws sts get-caller-identity", / and you should see your admin user. / Second, / send a short prompt to a model in the Bedrock playground, / and get an answer back. [pause] If both work, / you're ready. / And honestly, / that second check is your first GenAI integration. [long pause]

Transition: Now, / let's make sure it stays cheap.

## 3. Three rules that keep the course cheap

(About 1 min)

Three rules keep the whole course affordable. [pause]

▶ CLICK

Rule one: / **tear down** the same day. / Every lab comes with a clean-up step. / Run it before you close your laptop, / even if you plan to continue tomorrow. / Rebuilding takes minutes. / Paying for idle resources overnight / is how most surprise bills happen.

▶ CLICK

Rule two: / watch the **always-on** resources. / Most of what we build is serverless, / so it costs very little when it's idle. / The exceptions are provisioned throughput in Bedrock, / OpenSearch clusters / and SageMaker endpoints. / They bill by the hour, / whether you use them or not. / Whenever we use one, / I'll warn you.

▶ CLICK

Rule three: / check your spend **every week**. / Open Cost Explorer, / group by service, / and make sure nothing is growing that shouldn't be. [long pause]

Transition: Okay, / let's wrap up this section.

## 4. Lecture recap: three things to remember

(About 45 seconds)

So, / let's bring it together. [pause]

▶ CLICK

First, / use a dedicated account, / with an admin user and MFA on root. / Never production.

▶ CLICK

Second, / set a budget alert and Cost Anomaly Detection / before you build anything. / Then pick one Region, / and check your model access.

▶ CLICK

And third, / tear down the same day, / watch the always-on resources, / and check your spend every week. [pause]

So, / back to our one sentence. [pause] Set up **once**, / safely, / and you'll never worry about a surprise bill. [pause] And that's the end of Section 1. / You know what the exam tests, / how to read its questions, / and your account is ready. [long pause]

Transition: In the next section, / we'll cover the GenAI essentials on AWS. / Foundation models, / tokens, / and how Amazon Bedrock works.
