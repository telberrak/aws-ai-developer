# Lecture 13.3: Troubleshooting GenAI applications — narration script

Section 13, Evaluation and troubleshooting. About 13 minutes. The same text is in the speaker notes of `lecture-13.3.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Troubleshooting GenAI applications

(About 40 seconds)

So far in this section, / we've measured quality. / Now let's talk about what to do when something actually **breaks**. [pause] An error you don't recognize. / An answer that stops halfway. / A chatbot that suddenly can't find a document you know is there. [pause] In this lecture, / I'll give you a simple way to find the cause, / step by step, / and the tools that prove you found it.

If I had to sum it up in one sentence, / it would be this. [pause] **Read** what the system tells you, / **isolate** the step that broke, / and **prove** the fix with logs and traces. [long pause]

Transition: And the first thing the system tells you / is the error itself.

## 2. Read the error first

(About 2 minutes)

When a call to Amazon Bedrock fails, / the exception name already tells you most of the story. / There are five you'll see again and again. [pause]

▶ CLICK

**ValidationException**. / Your request is wrong. / The input is too long for the model, / the model ID is wrong, / or a parameter is out of range. / Retrying won't help. / You have to **fix the request**.


▶ CLICK

**ThrottlingException**. / You're sending too many requests, / or too many tokens, / too fast. / So you retry with **exponential backoff and jitter**. / You can spread the load with **cross-Region inference**. / And if it keeps happening, / you ask for a **higher quota**.


▶ CLICK

**ModelNotReadyException**. / The model isn't ready to serve your request yet. / This one is temporary, / and the AWS SDK retries it for you automatically.


▶ CLICK

**AccessDeniedException**. / Two usual causes. / Your IAM role doesn't allow the action, / for example InvokeModel on that model. / Or access to that model was never granted in your account. / Check **both**.


▶ CLICK

And **ModelTimeoutException**. / The model took too long to answer. / Send a shorter input, / ask for a shorter output, / or switch to the streaming API. [pause]

So here's the habit. / **Retry** the temporary ones, / like throttling. / **Fix** the permanent ones, / like validation and access. [long pause]

Transition: Now, / one ValidationException deserves its own story. / The input that's too long.

## 3. The context window overflows

(About 1 min 45 seconds)

Every model has a **context window**. / That's the maximum number of tokens it can take in one request, / your system prompt, / the chat history, / the retrieved chunks / and the question, / all added together. [pause]

▶ CLICK

So how do you know you've hit it? / Sometimes it's loud. / A ValidationException saying the input is too long. / Sometimes it's quiet. / In a long chat, / the model seems to forget what was said at the start. / And your **cost and latency** climb with every turn, / because you resend the whole history each time.


▶ CLICK

The first fix is to **count**. / The response tells you how many input tokens you used. / Watch that number, / and act before you reach the limit.


▶ CLICK

Second, / **trim the history**. / Keep the last few turns as they are, / and replace the older ones with a short summary.


▶ CLICK

Third, / **send less context**. / Fewer chunks, / shorter chunks, / better chunks. / A reranker helps you keep only the ones that matter.


▶ CLICK

And last, / if you really need all that text, / **pick a model with a bigger window**. / But try the other three first. / A bigger window also means a bigger bill. [long pause]

Transition: Now, / what if there's no error at all, / but the answer just stops in the middle of a sentence?

## 4. The answer stops mid-sentence

(About 1 min 45 seconds)

When you call the Converse API, / every response carries a field called **stopReason**. / It tells you **why** the model stopped. / So when an answer looks wrong, / look there first. [pause]

▶ CLICK

**end_turn**. / The model finished what it wanted to say. / That's the normal case.


▶ CLICK

**tool_use**. / The model wants you to run a tool / and send it the result. / If your code ignores this, / the conversation just stops.


▶ CLICK

And here's the one behind most cut-off answers. / **max_tokens**. / The model hit the output limit **you** set. / It didn't finish. / So you raise maxTokens, / or ask for a shorter answer. / And here's a tip. / Never show an answer to a user without checking this first.


▶ CLICK

**stop_sequence**. / The model produced one of the stop sequences you defined, / so it stopped there on purpose.


▶ CLICK

**guardrail_intervened**. / A Bedrock guardrail blocked the input or the output. / Check your guardrail's trace / to see which policy fired.


▶ CLICK

And **content_filtered**. / The model's own content filter stopped the answer. [pause] So one field, / six very different causes. / Always **log** it. [long pause]

Transition: Next, / the case where the request works / and the model finishes, / but the answer is still bad.

## 5. When the prompt is the problem

(About 1 min 30 seconds)

Very often, / the problem isn't the model. / It's the **prompt**. / Here are four symptoms, / and the fix for each. [pause]

▶ CLICK

The model **ignores your format**. / You asked for JSON / and got a friendly paragraph. / Show it an **example** of the output you want. / Or better, / define a **tool** with a schema, / and let the model fill it in. / That gives you structured output.


▶ CLICK

You get a **different answer every run**. / Lower the **temperature**. / And pin the exact prompt version you tested, / so nothing moves under you.


▶ CLICK

The model **makes things up**. / Ground it in your own data with RAG, / and tell it clearly that **"I don't know"** is an acceptable answer.


▶ CLICK

And the sneaky one. / It **broke after a quiet edit**. / Someone changed a word in the prompt, / and quality dropped. / Keep your prompts in **Bedrock Prompt Management**, / with versions. / Then you can see what changed, / and roll back in seconds. [long pause]

Transition: And in a RAG app, / there's one more place to look. / Retrieval.

## 6. When retrieval is the problem

(About 2 minutes)

In a RAG app, / a bad answer often means the right chunk / never reached the model. / Here are the five usual causes. [pause]

▶ CLICK

**The chunks split the answer**. / Half the answer sits at the end of one chunk, / and half at the start of the next. / Use bigger chunks with some **overlap**, / or try **semantic** chunking.


▶ CLICK

**Mismatched embeddings**. / Your documents were indexed with one embedding model, / and your queries use another. / The vectors don't speak the same language, / so search returns nonsense. / Query and index must use the **same** model.


▶ CLICK

**A filter that's too strict**. / Metadata filters are great, / but a wrong value silently drops the right chunks. / Loosen it, / and test again.


▶ CLICK

**Too few results**. / If you only ask for three chunks, / the right one might be number four. / Raise **numberOfResults**, / then use a reranker to keep the best.


▶ CLICK

And a **stale index**. / You added new documents to S3, / but they aren't searchable / until you **sync** the data source.


▶ CLICK

So here's the trick that saves hours. / Call the **Retrieve** API on its own, / with no generation. / Look at the chunks it returns. / If the right one isn't there, / the model never had a chance, / and no prompt change will fix it. [long pause]

Transition: All of these checks need evidence. / So, / where does that evidence come from?

## 7. Your evidence: logs and traces

(About 1 min 45 seconds)

You can't troubleshoot what you didn't record. / There are four sources of evidence. [pause]

▶ CLICK

First, / **model invocation logs**. / Bedrock can log the full request and response of every call, / to CloudWatch Logs, / to S3, / or both. / It's off by default. / So turn it on **before** you need it, / not after the incident.


▶ CLICK

Second, / **CloudWatch metrics**. / Bedrock publishes them for you. / Invocations, / InvocationLatency, / InvocationThrottles, / input and output token counts, / and client and server errors. / Put alarms on the ones that matter.


▶ CLICK

Third, / **traces**. / AWS X-Ray, / and AgentCore Observability for agents, / show every step of one request. / Retrieval, / the model call, / each tool call, / and how long each one took.


▶ CLICK

And fourth, / the **audit trail**. / AWS CloudTrail records who changed a prompt, / a model setting / or a permission, / and when. / When quality drops overnight, / that's often the first place to look. [long pause]

Transition: Let's wrap up.

## 8. Lecture recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / read the error, / and the stopReason. / They usually name the cause. / The request, / the quota, / access, / or a limit.


▶ CLICK

Second, / find the broken step. / Context size, / the prompt, / or retrieval. / Test each one on its own, / like calling Retrieve without generation.


▶ CLICK

And third, / prove it with evidence. / Invocation logs, / CloudWatch metrics, / traces, / and CloudTrail. [pause]

So, / back to our one sentence. [pause] **Read** what the system tells you, / **isolate** the step that broke, / and **prove** the fix with logs and traces. [long pause]

Transition: You now know how to measure quality / and how to fix it. / In the next lecture, / we'll see how to **report** that quality / to the people who depend on it.
