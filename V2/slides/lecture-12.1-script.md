# Lecture 12.1: Token economics and caching — narration script

Section 12, Cost, performance and monitoring. About 12 minutes. The same text is in the speaker notes of `lecture-12.1.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Token economics and caching

(About 45 seconds)

Welcome to Section 12. / Your application works, / it's secure, / and it's governed. / Now comes the question every manager asks next. / What does it **cost**, / how **fast** is it, / and how do we **know** it's healthy? [pause] In this first lecture, / we follow the money. / I'll show you where the cost of a GenAI app really comes from, / and five ways to spend less of it. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] You pay for **tokens**, / so send fewer of them, / to the **smallest** model that does the job, / and never pay twice for the same answer. [long pause]

Transition: So, / where does the money actually go?

## 2. You pay for tokens, in and out

(About 1 min 30 seconds)

On Bedrock's on-demand pricing, / you pay for tokens. / And four things drive how many you pay for. [pause]

▶ CLICK

First, / **input tokens**. / That's everything you send. / The system prompt, / the conversation history, / the retrieved chunks, / and the tool definitions. / And here's the thing. / You send all of it again / on **every** call.


▶ CLICK

Second, / **output tokens**. / On most models, / they cost several times more than input tokens. / So a chatty model / is an expensive model.


▶ CLICK

Third, / **calls per task**. / An agent might call the model five or six times / to answer one question. / Chains add steps, / and retries repeat calls. / So don't count calls. / Count calls **per answer**.


▶ CLICK

And fourth, / **model size**. / A large model can cost many times more per token / than a small one. [pause] Those four numbers multiply together. / Shrink any one of them, / and the bill goes down. [long pause]

Transition: And the biggest lever is usually the model itself.

## 3. Use the smallest model that's good enough

(About 1 min 30 seconds)

Here's the rule. / Use the **smallest** model that's good enough for each job. [pause]

▶ CLICK

A **small model** handles classification, / routing, / extraction / and short summaries. / It's fast, / and it's cheap.


▶ CLICK

A **mid-size model** handles answers grounded in retrieved documents. / It doesn't need to know everything, / because the context carries the facts.


▶ CLICK

And a **large model** handles hard reasoning, / planning / and code. / But only when you actually need it.


▶ CLICK

So **route**, / don't default. / A small model, / or even a simple rule, / decides where each request goes. / And Bedrock's **intelligent prompt routing** can do this for you, / picking between models in the same family / based on how hard the prompt looks. [pause] When you see a scenario with high cost / and simple requests going to a big model, / the answer is usually routing. [long pause]

Transition: The next lever is about the tokens you send again and again.

## 4. Don't pay full price for the same prefix twice

(About 1 min 30 seconds)

Think about a chatbot with a long system prompt. / Every single call sends that same prompt again. / **Prompt caching** fixes that. [pause]

▶ CLICK

**What gets cached?** / A long prefix that repeats across calls. / The system prompt, / a long document you ask questions about, / or your tool definitions.


▶ CLICK

**What do you save?** / Cached input tokens are billed at a discount. / And because the model doesn't reprocess them, / the first token arrives **sooner** too. / So you save money / and time.


▶ CLICK

**The catch?** / The cache expires after a few idle minutes. / And each model has a minimum prefix size / before it will cache anything. / Check the model's details before you count on it.


▶ CLICK

So structure your prompt for it. / Put the **stable** content first, / add a **cache point** right after it, / and keep the part that changes, / the user's question, / at the end. [long pause]

Transition: Prompt caching saves on the prefix. / But what if the whole question repeats?

## 5. Skip the model when you've answered it before

(About 1 min 45 seconds)

In a support app, / hundreds of people ask the same thing / in slightly different words. / **Semantic caching** answers them / without calling the model again. [pause]

▶ CLICK

A **question** comes in. / Let's say, / "How do I reset my password?"


▶ CLICK

You **embed** it, / with an embedding model on Bedrock. / Now it's a vector.


▶ CLICK

You **look it up** / in a vector store that's fast enough for a cache. / ElastiCache, / MemoryDB, / or OpenSearch all support vector search.


▶ CLICK

If there's **no** close match, / it's a miss. / You call the model as usual, / and you store the question and the answer / for next time.


▶ CLICK

But if there **is** a close match, / it's a hit. / You return the stored answer. / No model call, / almost no cost, / and very fast.


▶ CLICK

Two warnings. / Tune the **similarity threshold**. / Too loose, / and you'll return the wrong answer to a different question. / And never cache answers that depend on **who** is asking, / like account balances. [long pause]

Transition: Now, / let's look at how you pay for the calls you do make.

## 6. Match the price model to the work

(About 1 min 15 seconds)

The same tokens can cost different amounts, / depending on **how** you buy them. [pause]

▶ CLICK

**On-demand**. / Pay per token on shared capacity. / This is where you start.


▶ CLICK

**Batch inference**. / You put prompts in a JSONL file in S3, / and the results come back later. / It's priced lower than on-demand. / So for work that can wait, / like nightly summaries or tagging a backlog, / batch is the answer.


▶ CLICK

**Provisioned Throughput**. / You buy model units by the hour, / and that capacity is yours. / It pays off only with **steady, high** volume, / or when a custom model needs it.


▶ CLICK

And **service tiers**. / For some models, / Bedrock offers tiers that are faster / or cheaper than standard, / in exchange for priority or patience. / The options change often, / so check the pricing page for your model. [long pause]

Transition: The last lever is the simplest. / Just send less.

## 7. Fewer tokens, same answer

(About 1 min 30 seconds)

Most prompts carry tokens that don't change the answer. / Here's where to trim. [pause]

▶ CLICK

A **shorter system prompt**. / Cut repeated rules, / and long examples that don't change the results.


▶ CLICK

**Fewer, better chunks**. / Retrieve five good chunks, / not twenty average ones. / A reranker helps you pick the five.


▶ CLICK

**Summarize the history**. / Keep the last few turns as they are, / and a short summary of everything before.


▶ CLICK

**Cap the output**. / Set max tokens, / and ask for short, / structured answers. / Remember, / output tokens are the expensive ones.


▶ CLICK

And **measure each change**. / Re-run your test set every time you trim, / so that cheaper / doesn't quietly mean worse. [long pause]

Transition: And to know whether any of this worked, / you need to see the cost.

## 8. You can't cut what you can't see

(About 1 min 30 seconds)

You can't cut what you can't see. / So here's how to track it. [pause]

▶ CLICK

**Tag by team**. / Create an **application inference profile** for each team or app, / and give it cost allocation tags. / Now every call is labeled.


▶ CLICK

**Watch tokens**. / Bedrock sends input and output token counts per model / to **CloudWatch**. / That's your early signal.


▶ CLICK

**Split the bill**. / **Cost Explorer** shows spend by tag, / so you can see which team, / and which model, / is spending what.


▶ CLICK

**Alert early**. / **AWS Budgets** warns you / before a month goes over, / not after.


▶ CLICK

And when you report, / report **cost per task**. / Not cost per token. / Cost per answered question, / or per processed document, / is the number the business understands. [long pause]

Transition: Let's wrap up.

## 9. Lecture recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / know what you pay for. / Input and output tokens, / calls per task, / and the size of the model.


▶ CLICK

Second, / cache and right-size. / The smallest model that's good enough, / prompt caching for long prefixes, / and semantic caching for questions you've answered before.


▶ CLICK

And third, / pay the right way, / and track it. / Batch for work that can wait, / and tags and budgets / so every team sees its own spend. [pause]

So, / back to our one sentence. [pause] You pay for **tokens**, / so send fewer of them, / to the **smallest** model that does the job, / and never pay twice for the same answer. [long pause]

Transition: In the next lecture, / we look at the other side of the trade-off. / **Speed**.
