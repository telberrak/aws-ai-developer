# Lecture 5.3: Query expansion, decomposition and consistent retrieval — narration script

Section 5, Retrieval for RAG. About 10 minutes. The same text is in the speaker notes of `lecture-5.3.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Query expansion, decomposition and consistent retrieval

(About 40 seconds)

In the last lecture, / we made the **search** better. / Hybrid search, / and reranking. [pause] In this one, / we work on the other side. / The **question**. [pause] We'll rewrite and expand queries, / split complex questions into smaller ones, / and then give every app and agent **one** consistent way to retrieve. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Fix the **query** before you search, / and put retrieval behind **one** tool that everyone calls. [long pause]

Transition: So, / why isn't the user's question a good search query?

## 2. The question isn't a good query

(About 1 min 15 seconds)

Here's the thing. / People don't ask questions the way documents are written. / And that hurts retrieval in four ways. [pause]

▶ CLICK

First, / questions are **vague**. / "Is it covered?" / Covered by what? / The search has almost nothing to work with.


▶ CLICK

Second, / they're **multi-part**. / Two or three questions in one sentence, / and one search can't find the best chunks for all of them.


▶ CLICK

Third, / they're **follow-ups**. / "And for the other plan?" / only makes sense if you know the chat history. / On its own, / it's a terrible query.


▶ CLICK

And fourth, / they use **different words**. / Users say refund. / The documents say reimbursement. / Semantic search helps, / but it doesn't always close the gap.


▶ CLICK

So the fix is simple to say. / Don't search with the raw question. / **Improve the query first**. [long pause]

Transition: How? / Here are three techniques.

## 3. Three ways to improve the query

(About 1 min 30 seconds)

All three use a model **before** retrieval, / to turn the question into a better query. [pause]

▶ CLICK

First, / **rewrite**. / You give a model the chat history and the new question, / and it writes one **standalone** question. / "And for the other plan?" / becomes / "What does the premium plan cover for water damage?" / That's the one you search with. / For any chat app, / this is the first fix to make.


▶ CLICK

Second, / **expand**. / The model writes a few alternative versions of the query, / with synonyms and different phrasings. / You search with each one, / then merge the results / and remove the duplicates. / Now refund / **and** reimbursement / both find their chunks.


▶ CLICK

Third, / a **hypothetical answer**. / This one sounds strange at first. / The model drafts an answer to the question, / without any documents. / Then you embed that draft, / and search with it. / Why? / Because an answer looks much more like your documents / than a short question does. / This technique is often called **HyDE**. / The draft might be wrong, / but that's fine. / You only use it to search, / never to answer.


▶ CLICK

Now, / each of these adds one model call. / So use a **small, fast** model for it. / The extra call is cheap, / and the gain in retrieval is usually worth it. / But measure it on your own questions. [long pause]

Transition: And what about questions with several parts?

## 4. Split it, search each part, answer once

(About 1 min 30 seconds)

For those, / you use **query decomposition**. [pause]

▶ CLICK

Take this question. / "How do the EU and US return policies differ, / and did either one change this year?" / That's really three questions in one.


▶ CLICK

So a model **splits** it. / One, / what's the EU return policy? / Two, / what's the US return policy? / Three, / what changed this year?


▶ CLICK

Then you **retrieve for each** sub-question, / separately. / Each search is narrow, / so each one finds the right chunks.


▶ CLICK

And finally, / the model writes **one answer** / from all the chunks together. / It can compare the two policies, / because it actually has both of them.


▶ CLICK

And you don't have to build this yourself. / In Bedrock Knowledge Bases, / the RetrieveAndGenerate API has a **query decomposition** option. / You turn it on in the orchestration settings, / and the Knowledge Base splits the question for you. [pause] Use it for complex, / multi-part questions. / For simple ones, / it just adds latency. [long pause]

Transition: So far, / we've improved the query. / Now, / who actually calls retrieval?

## 5. Many apps, one way to retrieve

(About 1 min 15 seconds)

In a real company, / it's not one app. / It's many apps, / and more and more agents. [pause]

▶ CLICK

Without a plan, / **every app writes its own retrieval code**. / Different filters, / different numbers of results, / different settings. / And one day, / someone forgets the tenant filter, / and a customer sees another customer's documents.


▶ CLICK

The fix is **one retrieval function** / that every app and every agent calls. / And it gives you three things.


▶ CLICK

**Same rules**. / The tenant filter, / and who's allowed to see what, / are applied in **one** place. / Nobody can forget them.


▶ CLICK

**Same settings**. / The number of results, / hybrid search, / reranking. / You tune them once, / and everyone gets the improvement.


▶ CLICK

And **same logs**. / One place to see every query, / and what came back. / That's what you need when an answer is wrong / and you have to find out why. [long pause]

Transition: So, / how do you give that one function to a model?

## 6. Function calling with the Converse API

(About 1 min 45 seconds)

With **function calling**, / which Bedrock calls **tool use**. / Here it is with the Converse API. [pause]

▶ CLICK

Step one, / you **describe the tool**. / In toolConfig, / you give it a name, / search_docs, / a description, / and a JSON schema for its input. / Here, / just a query string. / The description matters, / because it's how the model decides **when** to search.


▶ CLICK

Step two, / the model **asks**. / When it needs information, / it doesn't answer. / It stops with the reason **tool_use**, / and gives you the tool name / and the query it wants to run. / Notice that the model doesn't run anything. / It only asks.


▶ CLICK

Step three, / **your code** runs it. / You call the Knowledge Base's **Retrieve** API with that query, / and with **your** filters. / Then you send the chunks back as a tool result, / and the model writes the answer.


▶ CLICK

And here's the most important point. / The model chooses the **query**. / Your code chooses the **filters**. / The tenant filter comes from the signed-in user, / never from the model. / So even a clever prompt injection / can't make it search someone else's data. [long pause]

Transition: That works for one app. / But what if many different clients need the same tool?

## 7. One MCP server, every client

(About 1 min 30 seconds)

That's where **MCP** comes in. / The **Model Context Protocol**. / It's an open standard / for connecting models to tools and data. [pause]

▶ CLICK

On the left, / your **clients**. / A chat app, / an agent built with a framework like Strands Agents, / or a developer's coding assistant. / They're all MCP clients, / so they can discover and call the same tools, / in the same way.


▶ CLICK

In the middle, / an **MCP server**. / It exposes one tool, / search_docs. / And this is where the filters, / the access rules / and the settings live. / In **one** place.


▶ CLICK

On the right, / the **Knowledge Base**. / The server calls Retrieve, / with the same settings for every client.


▶ CLICK

And you don't have to start from scratch. / AWS publishes an **open-source MCP server** for Bedrock Knowledge Bases. / Or, / you can put your own retrieval Lambda behind **Amazon Bedrock AgentCore Gateway**, / which serves it as an MCP tool. [pause] Either way, / you write the retrieval logic once, / and every client gets it. [long pause]

Transition: Let's wrap up.

## 8. Three things to remember

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / fix the query before you search. / Rewrite follow-ups into standalone questions, / expand with synonyms, / or search with a drafted answer.


▶ CLICK

Second, / split complex questions. / Decompose them into sub-questions, / retrieve for each one, / and answer once. / In Knowledge Bases, / that's one setting.


▶ CLICK

And third, / give everyone **one way to retrieve**. / One tool, / through function calling or MCP, / with the filters and access rules in one place. [pause]

So, / back to our one sentence. [pause] Fix the **query** before you search, / and put retrieval behind **one** tool that everyone calls. [long pause]

Transition: In the next lecture, / it's demo time. / We'll tune chunking on a real Knowledge Base, / and add a reranker.
