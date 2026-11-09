# Lecture 9.4: Developer tools and troubleshooting — narration script

Section 9, FM APIs and application patterns. About 10 minutes. The same text is in the speaker notes of `lecture-9.4.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Developer tools and troubleshooting

(About 40 seconds)

So far in this section, / we've called models, / made those calls resilient, / and plugged them into front ends and business systems. [pause] In this lecture, / we look at the developer's side. / The AI tools that help you build faster, / and the places you look when something goes wrong. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Let AI help you **write** the code, / but make sure every model call is **logged** and **traced**, / so you can see what really happened. [long pause]

Transition: So, / what's in the toolbox?

## 2. Two AI helpers for developers

(About 1 min 30 seconds)

AWS gives you two AI helpers for building. [pause]

▶ CLICK

The first is **Amazon Q Developer**. / It gives you chat and code suggestions inside your IDE, / and in the AWS console too. / It has agents that can write, / test / and refactor code across many files. / And when you hit an error, / it can explain what went wrong, / and help you fix it.


▶ CLICK

The second is **Kiro**. / It's an AI IDE from AWS, / and it's built around **specs**. / You describe what you want, / and it turns that into requirements, / a design, / and a list of tasks, / before it writes the code. / And with hooks and steering files, / you keep the agent following your team's rules.


▶ CLICK

But here's the thing to remember. [pause] These tools speed you up. / They don't replace you. / You still **review** every change, / and you still **own** what ships. [long pause]

Transition: Now, / let's say it's shipped, / and something breaks. / Where do you look?

## 3. Four places that explain most problems

(About 1 min 45 seconds)

Four places explain most of the problems you'll see. [pause]

▶ CLICK

First, / **model invocation logs**. / Bedrock can log every call. / The exact prompt, / the answer, / the model ID / and the token counts. / When an answer looks wrong, / this is where you see what the model actually received.


▶ CLICK

Second, / **CloudWatch metrics**. / Bedrock publishes them per model. / Invocations, / latency, / throttles, / errors / and tokens. / This is your health check at a glance.


▶ CLICK

Third, / **CloudWatch Logs Insights**. / It lets you query those logs. / Which model uses the most tokens? / Which calls were slowest? / Which app is failing? / A few lines of query, / and you've got the answer.


▶ CLICK

And fourth, / **AWS X-Ray**, / together with **CloudWatch Application Signals**. / They follow one request across API Gateway, / Lambda / and the model call, / so you can see where the time went. [long pause]

Transition: Let me show you what one of those queries looks like.

## 4. One query: where do the tokens go?

(About 1 min 30 seconds)

Here's a query you'll use again and again. / Where are my tokens going? [pause]

▶ CLICK

First, / you pick the fields. / Every logged call has the model ID, / and the input and output token counts.


▶ CLICK

Then, / you add them up. / The number of calls, / the input tokens, / and the output tokens, / grouped by model.


▶ CLICK

And then you sort, / so the biggest spender comes out on top. / In a few seconds, / you know which model, / and often which feature, / is driving your bill.


▶ CLICK

But there's a catch. [pause] Invocation logging is **off** by default. / You turn it on in the Bedrock settings, / once per Region, / and you send it to CloudWatch Logs, / to S3, / or to both. / If you don't turn it on, / there's nothing to query when you need it. [long pause]

Transition: Logs tell you what happened. / Traces tell you where the time went.

## 5. Follow one request end to end

(About 1 min 30 seconds)

Let's follow one slow request. [pause]

▶ CLICK

It comes in through **API Gateway**. / Forty milliseconds.


▶ CLICK

Then **Lambda** builds the prompt. / A hundred and twenty milliseconds.


▶ CLICK

And then the **Bedrock call**. / Four point two seconds. / There's your slow hop. / And it's usually the model, / because the model generates the answer one token at a time.


▶ CLICK

That picture comes from **AWS X-Ray**. / It records each hop as a segment, / including the SDK call to Bedrock, / so the slow part stands out straight away.


▶ CLICK

And **CloudWatch Application Signals** builds on the same traces. / It gives you service maps, / and latency and error goals, / so you see a problem before your users report it. [pause] And if the model call is the slow part, / look at how many output tokens you're asking for. / Long answers take longer. [long pause]

Transition: So, / let's put it all together. / Here's where to look first, / for the problems you'll actually hit.

## 6. Know where to look first

(About 2 min)

Five symptoms, / and the first place to look for each. [pause]

▶ CLICK

**Throttling errors**. / Check the throttles metric in CloudWatch, / then your quotas. / And make sure your code retries with backoff, / like we covered in the resilience lecture.


▶ CLICK

**Slow answers**. / Open an X-Ray trace, / then check latency and output tokens. / Long answers take longer, / so a lower max tokens setting, / or streaming, / often helps.


▶ CLICK

**Strange answers**. / Go to the invocation log, / and read the **exact** prompt the model received. / Very often, / the retrieved context is wrong, / or a template variable is empty.


▶ CLICK

**A cost spike**. / Run a Logs Insights query. / Tokens by model, / and by app. / You'll find the culprit fast.


▶ CLICK

And **access denied**. / Look in CloudTrail for the failed call, / then check the IAM policy, / and whether model access is turned on for that model. [pause] In the exam, / when a question describes a symptom, / ask yourself where you'd look first. / That usually points to the answer. [long pause]

Transition: Let's wrap up.

## 7. Lecture recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / use the AI helpers. / Amazon Q Developer and Kiro help you write code fast. / But you still review it.


▶ CLICK

Second, / log every model call. / Invocation logs and Logs Insights show you the prompts, / the tokens / and the cost.


▶ CLICK

And third, / trace to find the slow hop. / X-Ray and Application Signals follow one request from end to end. [pause]

So, / back to our one sentence. [pause] Let AI help you **write** the code, / but make sure every model call is **logged** and **traced**, / so you can see what really happened. [long pause]

Transition: In the next lecture, / we put this section into practice. / A streaming chat, / with retries built in.
