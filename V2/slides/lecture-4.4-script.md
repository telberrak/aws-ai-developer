# Lecture 4.4: Metadata, scaling and keeping vectors fresh — narration script

Section 4, Data pipelines and vector stores. About 10 minutes. The same text is in the speaker notes of `lecture-4.4.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Metadata, scaling and keeping vectors fresh

(About 40 seconds)

You've picked a vector store. / Now you have to keep it **useful**. [pause] In this lecture, / we'll use metadata to make retrieval precise, / see how each store grows, / look at where Knowledge Bases can read your data from, / and keep the vectors in step with the source. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Good RAG isn't just good search. / It's **precise filters**, / and vectors that stay **in sync** with the source. [long pause]

Transition: So, / first, / how does metadata make retrieval precise?

## 2. Metadata makes retrieval precise

(About 1 min 30 seconds)

Metadata is the information **about** a document. / And it's your sharpest retrieval tool. [pause]

▶ CLICK

First, / you **attach** it. / With an S3 data source, / you put a small JSON file next to each document, / with the same name plus **.metadata.json**. / So report.pdf / gets report.pdf.metadata.json. / Knowledge Bases reads it at ingestion, / and stores those fields with every chunk.


▶ CLICK

Then you **filter** on it. / At query time, / you pass a filter with the request. / Equals, / in a list, / greater than, / and you can combine them with and / or or.


▶ CLICK

And you **use** it for the things that matter to your business. / Department, / date, / product, / language, / or **tenant**.


▶ CLICK

Here's the point. / Filter first, / then search. / The model gets fewer, / better candidates, / so the answers are more relevant. / And with a tenant filter, / one customer **never** sees another customer's documents. [long pause]

Transition: Next, / what happens when the data grows?

## 3. How each store grows

(About 1 min 30 seconds)

Each store grows in its own way, / and you need to know who does the work. [pause]

▶ CLICK

**OpenSearch Serverless** scales itself. / It adds compute units for indexing and for search, / separately, / as the load changes. / You set a maximum to control cost.


▶ CLICK

An **OpenSearch cluster** is sized by **you**. / More shards to spread the data, / more replicas to handle more queries, / and more data nodes when it fills up.


▶ CLICK

**Aurora with pgvector** scales like a database. / Read replicas take the query load, / and an **HNSW index** keeps similarity search fast / as the table grows.


▶ CLICK

And **S3 Vectors** keeps vector indexes inside a vector bucket. / It's built for **billions** of vectors, / with nothing to provision.


▶ CLICK

And here's one lever that works everywhere. / Smaller vectors. / Many embedding models let you choose fewer dimensions. / Fewer dimensions means less storage / and faster search, / usually for a small loss in accuracy. / So test it on your own data. [long pause]

Transition: Now, / where does all this data come from?

## 4. Where Knowledge Bases can read from

(About 1 min 30 seconds)

Knowledge Bases has built-in **connectors**, / so you don't write the crawling code yourself. [pause]

▶ CLICK

**Amazon S3**. / Files in a bucket. / It's the most common source, / and the one we'll use in the demo.


▶ CLICK

The **Web Crawler**. / It reads web pages, / starting from the URLs you give it, / and staying inside the scope and limits you set.


▶ CLICK

**Confluence**. / Spaces and pages from your team's wiki.


▶ CLICK

**SharePoint**. / Sites and document libraries.


▶ CLICK

**Salesforce**. / Knowledge articles and records from your CRM.


▶ CLICK

And when none of those fit, / a **custom** data source. / Your own code pushes documents straight into the Knowledge Base through the API. / That's how you bring in anything else, / like a database, / or a system with no connector. [pause] Not every connector supports every feature, / so check the documentation for the one you choose. [long pause]

Transition: And once the data is in, / how do you keep it fresh?

## 5. A sync is an ingestion job

(About 1 min 40 seconds)

Here's the key idea. / A sync is an **ingestion job**. / And you decide when it runs. [pause]

▶ CLICK

First, / it's **incremental** by design. / Each sync only processes what was added, / changed / or deleted since the last one. / So you're not re-embedding your whole library every night, / and you're not paying for it either.


▶ CLICK

Second, / you can run it **on a schedule**. / EventBridge Scheduler starts the ingestion job every hour, / or every night. / Simple, / and good enough for most documents.


▶ CLICK

Third, / **on an event**. / A new file lands in S3, / that event triggers a Lambda function, / and the function starts the ingestion job. / Now your answers update within minutes.


▶ CLICK

And fourth, / **direct ingestion**. / For a handful of documents that must show up right away, / you push them straight in through the API, / with no full sync.


▶ CLICK

One thing to watch. / Only **one** ingestion job runs at a time / for a data source. / So if a thousand files arrive, / don't start a thousand jobs. / Batch the events together, / and start one. [long pause]

Transition: And finally, / how do you know it's actually working?

## 6. Watch the sync, not just the search

(About 1 min 20 seconds)

Most teams watch the search. / Watch the **sync** too. [pause]

▶ CLICK

First, / read the **job statistics**. / Every ingestion job tells you how many documents it scanned, / indexed, / modified, / deleted / and how many **failed**.


▶ CLICK

Second, / **alarm on failures**. / A failed or stuck job doesn't break your app. / It just quietly serves answers from **old** data. / And that's worse.


▶ CLICK

Third, / let **deletions** flow. / When a document is removed from the source, / the next sync removes its vectors too. / So delete at the source, / not by hand in the store.


▶ CLICK

And fourth, / keep connector credentials in **AWS Secrets Manager**. / Confluence, / SharePoint / and Salesforce all need them, / and Knowledge Bases reads them from there. / Never put them in code. [long pause]

Transition: Let's wrap up.

## 7. Lecture recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / metadata narrows the search. / Sidecar files in S3, / filters at query time, / and tenant isolation for free.


▶ CLICK

Second, / know how each store scales. / Serverless options scale themselves. / Clusters and databases are sized by you. / And smaller vectors help everywhere.


▶ CLICK

And third, / a sync keeps the vectors fresh. / Incremental ingestion jobs, / on a schedule, / on an event, / or with direct ingestion. / And watch the job statistics. [pause]

So, / back to our one sentence. [pause] Good RAG isn't just good search. / It's **precise filters**, / and vectors that stay **in sync** with the source. [long pause]

Transition: In the next lecture, / we build it. / A Knowledge Base with an S3 source, / and incremental sync.
