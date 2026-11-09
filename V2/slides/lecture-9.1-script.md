# Lecture 9.1: Sync, async and streaming invocation — narration script

Section 9, FM APIs and application patterns. About 10 minutes. The same text is in the speaker notes of `lecture-9.1.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Sync, async and streaming invocation

(About 45 seconds)

Welcome to Section 9. [pause] So far, / we've designed the solution, / fed it data, / built agents / and deployed them. / Now we look at the code that actually **calls** the model. / How it calls, / how it survives failures, / how it reaches users, / and how you debug it. [pause] In this first lecture, / it's all about how you call the model, / and how the answer gets back to the person waiting for it. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Let **the wait** decide how you call the model. / Answer **directly** when it's quick, / **stream** when someone's reading, / and **queue** it when it's long. [long pause]

Transition: So, / what are your options?

## 2. Four ways to call a model

(About 1 min 45 seconds)

Bedrock gives you four ways to call a model. [pause]

▶ CLICK

**Converse**. / This is synchronous. / You send the request, / you wait, / and you get the whole answer back in one response. / Simple, / and fine for short answers.


▶ CLICK

**ConverseStream**. / Same request shape, / but the answer comes back in small pieces / as the model generates it.


▶ CLICK

**Async invoke**. / You start a long job, / you get an ID straight away, / and the output lands in an S3 bucket when it's done. / Only some models support this, / mostly the ones that generate big outputs, / like video.


▶ CLICK

And **batch inference**. / You put thousands of requests in a JSONL file in S3, / start a batch job, / and the results come back to S3. / Nobody's waiting, / so you get a **lower price** than on-demand. [pause] Notice the pattern. / As you go down the list, / the caller waits **less** / and cares **less** about speed. [long pause]

Transition: Streaming deserves a closer look, / because users notice it most.

## 3. Streaming changes what the user feels

(About 1 min 30 seconds)

Streaming changes what the user **feels**. [pause]

▶ CLICK

The number that matters is **time to first token**. / Without streaming, / the user stares at a spinner until the whole answer is ready. / With streaming, / the first words show up in a second or two.


▶ CLICK

Under the hood, / ConverseStream doesn't send one response. / It sends **events**. / A message start, / then lots of content deltas carrying the text, / then a message stop, / and finally a metadata event with the token usage. / Your code reads them one by one.


▶ CLICK

But here's the catch. / Streaming doesn't make the model **faster**. / The total time is about the same. / It just makes the wait feel shorter, / and it lets the user stop early if the answer is going the wrong way.


▶ CLICK

So here's the rule. [pause] Stream when a **person** is reading the answer. / If another program is consuming it, / don't bother. [long pause]

Transition: But how do those chunks actually reach the browser?

## 4. Getting the stream to the user

(About 1 min 30 seconds)

Here's the classic pattern. [pause]

▶ CLICK

The **browser** opens a WebSocket connection, / and sends the question.


▶ CLICK

**API Gateway**, / with a WebSocket API, / keeps that connection open in both directions.


▶ CLICK

A **Lambda** function picks up the message, / calls ConverseStream, / and as each chunk arrives, / it posts it back to the user's connection.


▶ CLICK

And **Bedrock** generates the answer, / piece by piece.


▶ CLICK

There's a simpler option too. / **Lambda response streaming**. / A Lambda function URL can stream the response straight back over HTTP, / and the browser reads it as it arrives. / It only goes one way, / but for a chat answer, / one way is all you need. / Just check which runtimes support it natively. [pause] WebSockets win when you need a **two-way** conversation on one connection. [long pause]

Transition: Now, / what about jobs that take minutes, / not seconds?

## 5. Long jobs go through a queue

(About 1 min 30 seconds)

Long jobs go through a **queue**. [pause]

▶ CLICK

First, / **API Gateway** accepts the request. / It validates it, / and returns a job ID straight away. / The caller isn't left hanging.


▶ CLICK

The job goes into an **SQS queue**. / The queue absorbs bursts, / and if something fails, / the message comes back and gets retried.


▶ CLICK

A **Lambda worker** pulls jobs off the queue, / and calls Bedrock at a pace your quotas allow.


▶ CLICK

**Bedrock** does the long generation.


▶ CLICK

And the **result** is stored, / say in DynamoDB, / under the job ID.


▶ CLICK

So how does the client find out it's done? / Two ways. / It **polls** with the job ID, / or you **push** a notification when the result is ready. [long pause]

Transition: So, / how do you choose between all of these?

## 6. Pick the pattern from the wait

(About 1 min 15 seconds)

You choose from **the wait**. [pause]

▶ CLICK

If a user waits a few seconds for a short answer, / use **Converse**. / The simplest code.


▶ CLICK

If a user reads the answer as it's written, / like in a chat, / use **ConverseStream**.


▶ CLICK

If a job takes **minutes**, / use a queue, / or async invoke for the models that support it. / Return an ID, / and deliver later.


▶ CLICK

And if you have thousands of records and no rush, / use **batch inference**, / for the lowest price per token. [pause] When a question describes how long someone can wait, / that's your clue. [long pause]

Transition: Let's wrap up.

## 7. Lecture recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / there are four ways to call a model. / Converse, / ConverseStream, / async invoke / and batch inference.


▶ CLICK

Second, / stream for **people**. / A WebSocket API or Lambda response streaming carries the chunks to the browser.


▶ CLICK

And third, / queue the long work. / Return an ID, / process from SQS, / and deliver the result later. [pause]

So, / back to our one sentence. [pause] Let **the wait** decide how you call the model. / Answer **directly** when it's quick, / **stream** when someone's reading, / and **queue** it when it's long. [long pause]

Transition: But calls fail. / In the next lecture, / we make them resilient, / and route each one to the right model.
