# Lecture 12.4: Demo: a CloudWatch dashboard for tokens, latency and cost — narration script

Section 12, Cost, performance and monitoring. About 18 minutes. The same text is in the speaker notes of `lecture-12.4.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next. [ON SCREEN: …] = what to show during the live demo.

## 1. A CloudWatch dashboard for tokens, latency and cost

(About 40 seconds)

[ON SCREEN: the title, with the AWS console open in another tab]

In this lecture, / we build a **CloudWatch dashboard** for a generative AI app. / We deploy it, / send it real traffic, / and read what it tells us about **tokens**, / **latency** / and **cost**. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] You don't need to build monitoring for Bedrock from scratch, / because Bedrock **already publishes** calls, / tokens, / latency / and errors, / and one dashboard turns them into **cost** you can see. [long pause]

Transition: So, / what are we deploying?

## 2. From model calls to one dashboard

(About 1 min 30 seconds)

Here's the whole stack. / Four parts in a line, / and one optional extra. [pause]

▶ CLICK

First, / **Amazon Bedrock**. / Every time your app calls a model, / Bedrock records it. / You don't add any code for that. / It just happens.


▶ CLICK

Second, / **CloudWatch metrics**. / Those numbers land in a namespace called **AWS/Bedrock**, / and they're split by **model ID**. / So each model you use gets its own numbers.


▶ CLICK

Third, / the **dashboard and the alarms**. / The dashboard puts tokens, / latency, / errors / and an estimated cost on one screen. / And the alarms watch for the two things that hurt you first, / **throttles** / and **slow calls**.


▶ CLICK

Fourth, / an **SNS topic**. / When an alarm fires, / it sends a message here. / And if you give the app your email address, / you get that message in your inbox.


▶ CLICK

And the optional extra. / If you turn on **model invocation logging**, / Bedrock writes every request to CloudWatch Logs. / Then a **Logs Insights** widget can show you something metrics can't, / which is **who** spent the tokens. [pause] And all of it, / is one CDK app. [long pause]

Transition: So, / which numbers do we actually get?

## 3. Six numbers Bedrock already publishes

(About 1 min 45 seconds)

Bedrock gives us six numbers for free. / Let's go through them one by one. [pause]

▶ CLICK

**Invocations**. / How many calls reached the model. / That's your traffic.


▶ CLICK

**InputTokenCount**. / The tokens you sent. / And that's not just the user's question. / It's the system prompt, / the retrieved context, / and the whole chat history too. / That's why it's often bigger than you'd expect.


▶ CLICK

**OutputTokenCount**. / The tokens the model wrote back. / On most models, / an output token costs **several times** more than an input token. / So this is often the pricier side of the bill.


▶ CLICK

**InvocationLatency**. / How many milliseconds each call took. / And here's the thing. / Don't just look at the average. / Look at the **p90**, / the time that ninety percent of calls beat. / Because the slow calls are the ones your users remember.


▶ CLICK

**InvocationThrottles**. / Calls Bedrock refused, / because you went over your quota.


▶ CLICK

And **client and server errors**. / A client error means **your** request was wrong, / say a bad parameter or a model you can't use. / A server error means the service had a problem. / The first one, / you fix in your code. / The second one, / you retry. [pause]

One more detail at the bottom. / All of these are split by **ModelId**. / And if you call through an **inference profile**, / the ModelId is the **profile ID**, / not the plain model ID. / Get that wrong, / and your dashboard stays empty. [long pause]

Transition: So, / how does the code build this?

## 4. Three choices in the CDK app

(About 1 min 30 seconds)

[ON SCREEN: app.py open in the editor, next to this code]

The CDK app is short, / but it makes three choices you should know about. [pause]

▶ CLICK

First, / **one metric per model ID**. / Every metric points at the AWS/Bedrock namespace, / with the ModelId dimension set to the exact ID you call. / You set that ID in **cdk.json**, / so you change it in one place.


▶ CLICK

Second, / **cost is just math**. / CloudWatch doesn't know what tokens cost. / So we use **metric math**. / Input tokens divided by a thousand, / times the input price, / plus output tokens divided by a thousand, / times the output price. / [pause] Now, / the prices in this lab are **examples**. / Look up the current price for your model and Region, / and put it in cdk.json. / And remember, / this is an **estimate**. / Your bill is the real number.


▶ CLICK

Third, / **alarms that notify**. / One alarm fires on **any** throttle. / The other fires when average latency stays above a threshold, / five seconds by default, / in two out of three five-minute periods. / Both send to the same SNS topic. [long pause]

Transition: Enough code. / Let's deploy it.

## 5. Deploy, send traffic, read the dashboard

(About 2 min 30 seconds, plus the live demo)

[ON SCREEN: a terminal in the lab folder, V2/labs/lab-12.4-genai-dashboard]

Three steps. / Deploy, / send traffic, / and read the dashboard. [pause]

▶ CLICK

[ON SCREEN: run cdk deploy, then open the DashboardUrl from the outputs]

Step one, / **cdk deploy**. / It creates a dashboard, / two alarms / and an SNS topic. / When it's done, / it prints a **DashboardUrl**. / Open it. / [pause] It's empty right now, / and that's fine. / Nothing has called the model yet.


▶ CLICK

[ON SCREEN: run python load.py and wait for the summary]

Step two, / **python load.py**. / It sends thirty Converse calls with short random questions. / At the end, / it prints what happened. / How many calls worked, / the tokens in and out, / the latency, / and an **estimated cost**. / Write those numbers down. / We'll check them in a minute.


▶ CLICK

[ON SCREEN: refresh the dashboard, point at the Calls, Tokens and Estimated cost tiles]

Step three. / Wait a few minutes, / because metrics take a little while to arrive. / Then **refresh the dashboard**. / The calls tile should say thirty. / The tokens should match what load.py printed. / And the cost tile should match too. / [pause] That's the check that matters. / The dashboard and your own script **agree**. / So now you can trust the dashboard when your script isn't there. [long pause]

Transition: Now let's push it a little harder.

## 6. Longer answers, more load

(About 2 min, plus the live demo)

[ON SCREEN: the same terminal, with the dashboard in the next tab]

Now we change one thing at a time, / and watch what moves. [pause]

▶ CLICK

[ON SCREEN: run python load.py --max-tokens 800, then refresh the dashboard]

First, / **longer answers**. / We raise max tokens to eight hundred. / Now watch the graphs. / Output tokens go up. / Latency goes up. / And cost per call goes up. / [pause] They all climb **together**. / Because a model writes one token at a time, / so more tokens means more time, / and more money.


▶ CLICK

[ON SCREEN: run python load.py --calls 100 --threads 16, then show the throttles graph and the alarm status]

Second, / **more load**. / A hundred calls, / sixteen at a time. / If that goes over your quota, / you'll see **throttles** on the graph, / load.py will print the retries it made, / and the throttle alarm goes to **ALARM**. / [pause] Now, / your quota might be high enough that nothing throttles. / That's fine too. / It just means you have room.


▶ CLICK

[ON SCREEN: the Tokens by caller widget, if invocation logging is on]

And third, / optional. / If you turned on invocation logging, / scroll down to the **Logs Insights** widget. / It shows **tokens by caller**. / Which role, / or which user, / spent the tokens. / The metrics can't tell you that. / They only give you totals. [long pause]

Transition: So, / what is the dashboard really telling us?

## 7. Four things it tells you

(About 1 min 30 seconds)

Four things to take away from that dashboard. [pause]

▶ CLICK

One. / **Tokens are the cost**. / If the bill is too high, / look at the tokens first. / Cap max tokens, / and trim the context you send. / That's where the money is.


▶ CLICK

Two. / **Watch the p90, not the average**. / An average can look fine / while one call in ten is painfully slow. / And that one call / is the one your user complains about.


▶ CLICK

Three. / **A throttle is a signal**. / The first answer is to **retry with backoff**, / like load.py does. / But if throttles keep coming, / you've outgrown your setup. / Ask for a higher quota, / use **cross-Region inference**, / or buy **provisioned throughput**.


▶ CLICK

And four. / **Logs give the detail**. / Metrics are cheap, / and they tell you **how much**. / Invocation logs cost more, / but they tell you **who** and **what**. / You want both. [long pause]

Transition: And if something doesn't work?

## 8. Three checks, then tear it down

(About 1 min 15 seconds)

Here are the three problems you're most likely to hit. [pause]

▶ CLICK

**The dashboard stays empty**. / First, / just wait a few minutes, / and check the time range at the top. / Still empty? / Then check that **model_id** in cdk.json is the **exact** ID load.py calls. / Remember, / an inference profile ID is different from the plain model ID.


▶ CLICK

**AccessDenied, or a ValidationException**. / Check that you have access to the model in this Region. / And some newer models can only be called through an **inference profile**, / so you have to use the profile ID.


▶ CLICK

**No alarm email**. / AWS sends you a confirmation email first. / Until you click it, / nothing gets delivered.


▶ CLICK

And when you're done, / **cdk destroy**. / The dashboard and alarms cost very little, / but there's no reason to keep them. / And if you turned on invocation logging just for this lab, / **turn it off** too. [long pause]

Transition: Let's wrap up.

## 9. Recap

(About 1 min 15 seconds)

So, / three things to remember. [pause]

▶ CLICK

**Bedrock already publishes the numbers**. / Calls, / tokens, / latency, / throttles / and errors, / per model ID, / in AWS/Bedrock. / You don't write any code to get them.


▶ CLICK

**Cost is tokens times price**. / Metric math turns token counts into an estimated cost, / per period / and per call.


▶ CLICK

And **alarms and logs close the loop**. / Alarms catch throttles and slow calls. / Invocation logs show you who spent the tokens. [pause]

So, / in one sentence. / You don't need to build monitoring for Bedrock from scratch, / because Bedrock **already publishes** calls, / tokens, / latency / and errors, / and one dashboard turns them into **cost** you can see. [pause]

And that closes this section on cost, / performance / and monitoring. / You can now make a GenAI app cheaper, / faster, / and visible. / [pause] But there's one question we haven't answered yet. / Are the answers actually **good**? / That's what the next section is about. / Evaluating and troubleshooting your app. [long pause]

Transition: Next, / we look at how to measure the quality of a model's answers, / with evaluation metrics / and Bedrock evaluations.
