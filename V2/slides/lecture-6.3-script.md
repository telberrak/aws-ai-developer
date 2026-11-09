# Lecture 6.3: Advanced techniques and Prompt Flows — narration script

Section 6, Prompt engineering and governance. About 10 minutes. The same text is in the speaker notes of `lecture-6.3.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Advanced techniques and Prompt Flows

(About 40 seconds)

In the last two lectures, / we wrote prompts / and put them under control. / In this one, / we make them **work harder**. [pause] I'll show you how to get better reasoning, / how to get output in a shape your code can trust, / how to stop paying twice for the same long prompt, / and how to wire prompts into a workflow with Prompt Flows. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Use the **right technique** for the hard parts, / and wire your prompts into a **versioned flow**, / so you can ship them like code. [long pause]

Transition: So, / how do you get a model to reason better?

## 2. Make the model think, then make it answer in shape

(About 1 min 30 seconds)

Three techniques, / and they fix two different problems. / Thinking, / and shape. [pause]

▶ CLICK

First, / **step by step**. / You ask the model to work through the reasoning / before it gives the answer. / It's simple, / and it helps on maths, / logic / and anything with several steps.


▶ CLICK

Second, / **extended thinking**. / Some models can reason on their own / before they answer. / You turn it on as a model setting, / and you give it a budget, / a maximum number of tokens it can spend thinking.


▶ CLICK

Third, / **structured output**. / When code reads the answer, / you need a reliable shape. / You can give a JSON schema in the prompt. / Or, / and this is the stronger option, / you define a tool with that schema, / and you **force** the model to call it. / The tool's input is your structured output.


▶ CLICK

But here's the catch. / Reasoning isn't free. / Every thinking token is an output token, / and it adds time. / So use it where the question is **hard**, / not on every request. [long pause]

Transition: What if one prompt isn't enough?

## 3. Split the work, then check it

(About 1 min 30 seconds)

When one prompt can't do it all, / you split the work, / and then you check it. [pause]

▶ CLICK

**Prompt chaining**. / One prompt extracts the facts. / The next one analyses them. / The last one writes the reply. / Each prompt does **one job**, / so you can test it, / log it / and swap it on its own.


▶ CLICK

**Self-consistency**. / You ask the same question several times, / and you keep the answer that comes up most often. / It's a good fit for questions with one right answer, / like a classification or a number.


▶ CLICK

**Critique and revise**. / A second prompt reviews the draft / against your rules. / And a third one fixes whatever it found.


▶ CLICK

Notice the pattern. / Every one of these adds **calls**. / More calls usually means better answers, / but also more latency and more cost. / So add steps only where quality needs them. [long pause]

Transition: And speaking of cost, / here's a quick win.

## 4. Don't pay twice for the same long prefix

(About 1 min 40 seconds)

A lot of requests start the same way. / Same system prompt, / same tools, / same long document. / So why pay for it every time? [pause]

▶ CLICK

Look at one request. / At the front, / there's a **stable prefix**. / The system prompt, / the tool definitions, / maybe a long document.


▶ CLICK

After it, / you place a **cache point**.


▶ CLICK

And after that comes the part that **changes** every time. / The user's question.


▶ CLICK

Here's what you get. / It's **cheaper**. / Tokens read from the cache cost much less than fresh input tokens.


▶ CLICK

It's **faster**. / The model skips the work on the cached part, / so the first token comes back sooner.


▶ CLICK

But it's **short-lived**. / The cache expires after a few idle minutes. / So it pays off with steady traffic, / not with one request an hour.


▶ CLICK

In the Converse API, / you add a **cachePoint** block right after the stable part. / Two limits to remember. / Only supported models can use it, / and the prefix needs a **minimum** number of tokens, / which depends on the model. [long pause]

Transition: So far, / every technique lives inside your code. / What if you want to wire the steps together without writing the glue yourself?

## 5. Wire prompts and services into one workflow

(About 1 min 40 seconds)

That's what **Prompt Flows** are for. / In Bedrock, / a flow wires prompts, / Knowledge Bases / and your own code / into one workflow. / You build it from nodes. [pause]

▶ CLICK

Every flow has an **input** node, / where the request comes in, / and at least one **output** node, / where the result leaves.


▶ CLICK

A **prompt** node runs a prompt on a model you choose. / The prompt can be written inline, / or pulled from **Prompt Management**, / so the versioned prompts from the last lecture plug straight in.


▶ CLICK

A **Knowledge Base** node retrieves from a Knowledge Base. / It can return the chunks, / or a generated answer.


▶ CLICK

A **Lambda function** node runs your code. / Call an API, / clean up data, / apply a business rule.


▶ CLICK

A **condition** node sends the data down different branches, / based on rules you set. / For example, / complaints go one way, / and questions go another.


▶ CLICK

And the **iterator** and **collector**. / The iterator runs the next nodes once per item in a list, / and the collector gathers the results back up.


▶ CLICK

There are more node types too, / such as agents, / inline code / and S3 storage. / And the idea is always the same. / Each node's outputs connect to the next node's inputs. [long pause]

Transition: So how do you get a flow from your screen into production?

## 6. Build in a draft, ship a version, call an alias

(About 1 min 30 seconds)

Flows have a lifecycle, / and it works just like the prompt versions you've already seen. [pause]

▶ CLICK

First, / the **working draft**. / That's where you edit the nodes and connections.


▶ CLICK

Second, / you **prepare** it. / Bedrock checks the flow / and makes the latest draft ready to test.


▶ CLICK

Third, / you create a **version**. / A version is an immutable snapshot. / It never changes.


▶ CLICK

Fourth, / an **alias**. / It's a name, / like prod, / that points to one version.


▶ CLICK

Your app calls **InvokeFlow** / with the flow ID, / the alias ID / and the inputs. / Notice it never names a version.


▶ CLICK

And that's the payoff. / To release, / or to roll back, / you point the alias at a different version. / **One change**. / The app's code stays exactly the same. [long pause]

Transition: Let's wrap up.

## 7. Lecture recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / reason, / then shape. / Use step by step or extended thinking for the hard questions, / and a schema or a forced tool call for the output.


▶ CLICK

Second, / chain, / check / and cache. / One job per prompt, / a review step where quality matters, / and a cache point after the stable prefix.


▶ CLICK

And third, / flows ship like code. / You build in a draft, / save an immutable version, / and your app calls an alias with InvokeFlow. [pause]

So, / back to our one sentence. [pause] Use the **right technique** for the hard parts, / and wire your prompts into a **versioned flow**, / so you can ship them like code. [long pause]

Transition: In the next lecture, / we do exactly that. / We take a versioned prompt, / put it in a Prompt Flow, / and call it through an alias.
