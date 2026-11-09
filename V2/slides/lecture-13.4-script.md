# Lecture 13.4: Reporting quality to stakeholders — narration script

Section 13, Evaluation and troubleshooting. About 9 minutes. The same text is in the speaker notes of `lecture-13.4.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Reporting quality to stakeholders

(About 40 seconds)

You've measured everything. / Faithfulness, / latency, / cost, / guardrail hits. [pause] But a dashboard full of numbers / doesn't help the people who decide what happens next. [pause] This lecture is about **reporting** quality, / so that each person gets the answer they need. [pause]

Here's the one sentence. [pause] A quality report works when every number answers **someone's** question, / in **their** words, / and shows the **trend**. [long pause]

Transition: So, / who are you reporting to?

## 2. Four audiences, four questions

(About 1 min 30 seconds)

Four audiences, / and each one asks a different question. [pause]

▶ CLICK

**Executives** ask, / is it worth it? / They want cost, / savings / and risk, / in one page.


▶ CLICK

**Product owners** ask, / are users getting what they need? / Task success, / satisfaction, / and where people give up.


▶ CLICK

**Engineers** ask, / what broke, / and where? / Latency, / errors, / token use, / and evaluation scores per component.


▶ CLICK

And **risk and compliance** ask, / is it safe, / fair / and within policy? / Guardrail interventions, / fairness checks / and audit evidence.


▶ CLICK

So it's the same data, / cut four ways. / Before you build a report, / ask **who** it's for, / and what **decision** they'll make with it. [long pause]

Transition: And then there's the language problem.

## 3. Translate every metric

(About 2 minutes)

Most of our metrics mean nothing outside the engineering team. / So you translate them. [pause]

▶ CLICK

A **faithfulness** score of 0.87 becomes, / almost **9 in 10** answers are backed by our own documents.


▶ CLICK

A **task success** rate of 78 percent becomes, / about **4 in 5** requests are solved without a person.


▶ CLICK

**Cost per resolved task**. / Not cost per token, / which nobody outside engineering can judge. / Each solved request costs **4 cents**, / and you can compare that with what a phone call costs.


▶ CLICK

**p95 latency** of 3.2 seconds becomes, / nearly everyone gets an answer in about **3 seconds**.


▶ CLICK

And a **guardrail intervention** rate of 1.2 percent becomes, / about **1 request in 80** was blocked or masked.


▶ CLICK

The rule is simple. / Lead with the **business outcome**, / and keep the technical number underneath, / for anyone who wants to check it. [long pause]

Transition: Now let's put those numbers on one page.

## 4. The quality scorecard

(About 1 min 30 seconds)

A **quality scorecard** is the one page most stakeholders will actually read. [pause]

▶ CLICK

Each row is one metric. / Then its **target**, / this month's **value**, / the **trend**, / and a status. / Green, / amber / or red. [pause] Look at task success. / It's below target, / and going down. / That's amber. / And wrong-answer reports are well above target. / That's red.


▶ CLICK

Here's what makes a scorecard useful. / Every amber or red row comes with an **owner** and a **date**. / Otherwise, / it's just a list of bad news. [long pause]

Transition: But one month is a snapshot. / What about trends?

## 5. Show where it's going, not just where it is

(About 1 min 30 seconds)

A single number tells you where you are. / A **trend** tells you where you're going. [pause]

▶ CLICK

For engineers, / **CloudWatch dashboards**. / Latency, / errors, / tokens / and guardrail metrics, / live, / with alarms.


▶ CLICK

For the business, / **Amazon Quick Sight**. / Weekly trends, / cost per task, / and satisfaction, / built from your logs and evaluation results.


▶ CLICK

Third, / a **weekly evaluation run** on the same golden dataset. / Same questions, / same judge, / so this week's score really compares with last week's.


▶ CLICK

And fourth, / **release annotations**. / Mark every model change, / prompt change / and knowledge base update on the chart. / Then when a line drops, / you can see what changed that day.


▶ CLICK

So remember, / one number is a **snapshot**. / A trend line, / with your releases marked on it, / is the **story**. [long pause]

Transition: And when something does go wrong?

## 6. When it goes wrong, report it like this

(About 1 min 30 seconds)

Sooner or later, / something goes wrong. / Say the assistant quoted an old price list for two days. / Here's how you report it. [pause]

▶ CLICK

**What happened**. / In plain words, / with the dates.


▶ CLICK

The **impact**. / How many users, / how many answers, / and what it cost.


▶ CLICK

The **root cause**. / Here, / the old document was never removed from the knowledge base.


▶ CLICK

The **fix**. / What you did to stop it, / and when.


▶ CLICK

And **prevention**. / A new test case in the golden dataset, / and an alarm, / so the same problem can't come back quietly.


▶ CLICK

Keep it **blameless** and short. / And always end with a new test. / That's how an incident makes the system better. [long pause]

Transition: Let's wrap up.

## 7. Lecture recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / know your **audience**. / Executives, / product owners, / engineers / and compliance each ask a different question.


▶ CLICK

Second, / **translate** the numbers. / Plain words, / cost per resolved task, / and a one-page scorecard with owners for anything red.


▶ CLICK

And third, / show **trends**, / not snapshots. / Dashboards, / weekly evaluations, / release annotations, / and incident reports that end with a new test. [pause]

So, / back to our one sentence. [pause] A quality report works when every number answers **someone's** question, / in **their** words, / and shows the **trend**. [pause]

That closes this section, / and the two domains on optimization, / testing / and troubleshooting. / Before you move on, / take the **Domains 4 and 5 checkpoint**. / Twenty questions, / and a good way to see what stuck. [long pause]

Transition: Next, / we start the final review, / with a drill on choosing the right service.
