# Lecture 4.3: Choosing a vector store — narration script

Section 4, Data pipelines and vector stores. About 10 minutes. The same text is in the speaker notes of `lecture-4.3.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Choosing a vector store

(About 40 seconds)

Every RAG system needs somewhere to keep its vectors. / And on AWS, / you've got more than one choice. [pause] In this lecture, / I'll show you what a vector store actually does, / how Amazon Bedrock Knowledge Bases fits on top, / the five stores you should know, / and how to pick one. / And we'll see where DynamoDB fits, / because it's not where most people expect. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Every vector store does the **same job**, / so you choose on **cost, / scale / and features**, / not on the name. [long pause]

Transition: So, / what is that job?

## 2. What a vector store does

(About 1 min 20 seconds)

A vector store does three things. [pause]

▶ CLICK

It **stores**. / For each chunk of a document, / it keeps the vector, / the original text, / and the metadata that describes it.


▶ CLICK

It **searches**. / You turn the user's question into a vector, / with the same embedding model, / and the store finds the vectors **nearest** to it. / Nearest in meaning, / not in spelling.


▶ CLICK

And it **filters**. / Before or during that search, / it can narrow the results on metadata. / Only this product, / only this year, / only this team's documents.


▶ CLICK

Here's the good news. / Every option we'll look at does those three things. [pause] What changes is the **cost**, / how far it **scales**, / how fast it answers, / which search features it has, / and what your team already knows how to run. [long pause]

Transition: But before we compare stores, / who does the work of filling them?

## 3. Managed RAG, with your choice of store

(About 1 min 20 seconds)

On AWS, / that's usually **Amazon Bedrock Knowledge Bases**. / It's managed RAG. / It runs the whole pipeline for you. [pause]

▶ CLICK

First, / it **connects** to your data sources / and reads the documents.


▶ CLICK

Second, / it **chunks** each document, / and calls the embedding model you chose / to turn every chunk into a vector.


▶ CLICK

Third, / it **writes** those vectors, / with their text and metadata, / into the vector store you picked.


▶ CLICK

And fourth, / it **retrieves**. / The Retrieve API gives you the matching chunks, / and RetrieveAndGenerate goes one step further, / and has a model write the answer with citations.


▶ CLICK

So remember this. / Knowledge Bases runs the pipeline, / but the **vector store** underneath / is still your decision. / Some stores it can create for you, / and others you bring yourself. [long pause]

Transition: So, / which stores are we choosing between?

## 4. Five vector stores to know

(About 2 min)

There are five you should know. / For each one, / think about what it's good at, / and what to watch out for. [pause]

▶ CLICK

**Amazon OpenSearch Serverless**. / It's fully managed, / it scales on its own, / and it supports **hybrid search**, / so keyword and semantic search together. / That's why it's the default for so many Knowledge Bases. / The catch? / There's a **minimum capacity cost**, / even when nobody's searching.


▶ CLICK

**An Amazon OpenSearch Service cluster**. / Same engine, / but you control the shards, / the nodes / and the tuning. / That's great for very high query rates. / The catch is that **you** run and size the cluster.


▶ CLICK

**Aurora PostgreSQL with pgvector**. / If your application already lives in PostgreSQL, / your vectors can sit right next to your business data, / and you can join them with plain SQL. / The catch is that your vector search now scales with the database.


▶ CLICK

**Amazon S3 Vectors**. / Vector storage built into S3. / It's made for **huge** numbers of vectors, / at the **lowest cost**. / The catch is that queries are slower than an in-memory engine, / and it has fewer search features.


▶ CLICK

And **Neptune Analytics**. / It's a graph. / Knowledge Bases can use it for **GraphRAG**, / where the answer depends on how people, / products / or events connect to each other. / Only reach for it when those links really matter. [pause] There are third-party options too, / like Pinecone or MongoDB Atlas, / but these five are the AWS ones to know. [long pause]

Transition: So, / how do you actually pick?

## 5. Match the store to the requirement

(About 1 min 30 seconds)

Start from the requirement, / and the store usually picks itself. [pause]

▶ CLICK

You want the **fastest path**, / fully managed, / with keyword and semantic search together. / That's **OpenSearch Serverless**.


▶ CLICK

Your app **already runs on PostgreSQL**, / and you want one database to manage. / That's **Aurora with pgvector**.


▶ CLICK

You've got **billions** of vectors, / cost comes first, / and an answer in under a second is fine. / That's **S3 Vectors**.


▶ CLICK

You need strict tuning, / or very high query rates, / and you've got the people to run a cluster. / That's an **OpenSearch cluster**.


▶ CLICK

And the answers depend on **how entities connect**. / That's **Neptune Analytics**. [pause] When you read a scenario, / listen for those clues. / Words like "lowest cost", / "existing PostgreSQL", / "hybrid search" / or "relationships" / point straight at one of these. [long pause]

Transition: And now, / where does DynamoDB fit?

## 6. DynamoDB holds the metadata, not the vectors

(About 1 min 20 seconds)

DynamoDB shows up in almost every GenAI architecture. / But it holds the **metadata**, / not the vectors. [pause]

▶ CLICK

First, / a **document registry**. / For every document, / its ID, / where it came from, / its version, / its owner, / and when it was last indexed. / That's how you know what's in your vector store, / and what's out of date.


▶ CLICK

Second, / **access rules**. / Which teams or tenants are allowed to see each document. / Your app reads them, / and turns them into metadata filters on the search.


▶ CLICK

Third, / **conversation state**. / The session history for a multi-turn chat, / so the next question has context.


▶ CLICK

What DynamoDB is great at / is fast lookups **by key**. / It doesn't do similarity search. / So the vectors themselves / live in one of the stores you just saw. [long pause]

Transition: Let's wrap up.

## 7. Lecture recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / every vector store does one job. / It stores, / searches / and filters vectors. / And Knowledge Bases manages the pipeline that fills it.


▶ CLICK

Second, / pick the store by the requirement. / OpenSearch Serverless for managed and hybrid search, / Aurora pgvector when you already run PostgreSQL, / S3 Vectors for the lowest cost at scale, / and an OpenSearch cluster when you need tuning.


▶ CLICK

And third, / DynamoDB holds the **metadata**. / The registry, / the access rules / and the conversation state. / Not the similarity search. [pause]

So, / back to our one sentence. [pause] Every vector store does the **same job**, / so you choose on **cost, / scale / and features**, / not on the name. [long pause]

Transition: In the next lecture, / we make retrieval precise with metadata, / and keep those vectors fresh.
