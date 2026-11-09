# Lecture 4.5: Demo: a Knowledge Base with an S3 source and incremental sync — narration script

Section 4, Data pipelines and vector stores. About 13 minutes. The same text is in the speaker notes of `lecture-4.5.pptx`. The demo code is in `labs/lab-4.5-knowledge-base`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next. [ON SCREEN: …] = what to show during the live demo.

## 1. A Knowledge Base with an S3 source and incremental sync

(About 40 seconds)

In this lecture, / we build a **Knowledge Base** from scratch. / We point it at an S3 bucket full of documents, / ask it questions, / then change the documents / and watch it pick up **only** what changed. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] A Knowledge Base is only as fresh as its **last sync**, / so make syncing cheap, / incremental / and automatic. [long pause]

Transition: So, / what are we building?

## 2. From documents to vectors

(About 1 min 45 seconds)

Here's the whole pipeline. / Four parts in a line, / and one way to ask questions. [pause]

▶ CLICK

First, / an **S3 bucket**. / Your documents go in as plain files. / Markdown, / PDFs, / Word files, / whatever you've got.


▶ CLICK

Second, / the **data source**. / It reads the bucket, / and splits every document into chunks of about three hundred tokens, / with a little overlap so no idea gets cut in half.


▶ CLICK

Third, / the **embedding model**. / We use Amazon Titan Text Embeddings V2. / It turns each chunk into a vector, / a list of numbers that captures what the chunk means.


▶ CLICK

Fourth, / **S3 Vectors**. / That's where the vectors live, / in one index. / Why S3 Vectors? / Because for a lab, / it's the cheapest option. / You pay for what you store and query, / and nothing runs while you're asleep.


▶ CLICK

And your app asks questions through two APIs. / **Retrieve** gives you back the best chunks. / **RetrieveAndGenerate** goes one step further, / and has a model write the answer, / with **citations** to the files it used. [pause] And again, / it's all one CDK app. [long pause]

Transition: But what happens when the documents change?

## 3. Only the changes get processed

(About 1 min 45 seconds)

This is the part people often get wrong. / When you sync again, / the Knowledge Base doesn't start from zero. / It compares the bucket with the last sync, / and each file falls into one of four groups. [pause]

▶ CLICK

A **new** file / gets chunked, / embedded / and added.


▶ CLICK

A **changed** file / gets its old vectors replaced with new ones.


▶ CLICK

A **deleted** file / has its vectors removed. / So the Knowledge Base stops answering from a document that no longer exists.


▶ CLICK

And an **unchanged** file / is simply skipped. / No new embeddings, / no extra cost. / That's what makes syncing a big library cheap.


▶ CLICK

But here's the catch. [pause] **Nothing syncs on its own**. / The work is done by an **ingestion job**, / and something has to start it. / In a real system, / you start it on a schedule with EventBridge, / or whenever a new file lands in the bucket. / Forget that, / and your answers quietly go stale. [long pause]

Transition: So, / what does the code look like?

## 4. Three choices in the CDK app

(About 1 min 45 seconds)

The CDK app is short, / but it makes three choices you should know about. [pause]

▶ CLICK

First, / the **vector index**. / It has to match the embedding model. / Titan V2 gives us 1024 dimensions, / so the index has 1024, / and we compare vectors with cosine distance. / And we mark the chunk text, / and Bedrock's own metadata, / as **non-filterable**. / Why? / Because filterable metadata in S3 Vectors is small, / and the chunk text wouldn't fit.


▶ CLICK

Second, / the **embedding model**. / Pick it carefully, / because it's fixed for the life of the index. / If you change it later, / every vector has to be rebuilt.


▶ CLICK

And third, / **chunking**. / Fixed-size chunks of three hundred tokens, / with twenty percent overlap. / It's a sensible default, / and in Section 5 / we'll see when to choose something smarter. [long pause]

Transition: Enough reading. / Let's deploy it.

## 5. Live demo, part 1: deploy, sync, ask

(About 3 minutes)

Over to the terminal. [ON SCREEN: terminal in the lab folder, virtual environment active, in a Region with S3 Vectors and Knowledge Bases] [pause]

▶ CLICK

First, / I deploy the stack. [ON SCREEN: run cdk deploy and show the outputs: SourceBucket, KnowledgeBaseId, DataSourceId] [pause] CDK creates the bucket, / the vector index, / the Knowledge Base / and its data source. / The scripts read these outputs themselves, / so there's nothing to copy.


▶ CLICK

Now the first sync. [ON SCREEN: run python sync.py docs/v1 and point at the statistics] [pause] The script uploads three documents, / a returns policy, / a shipping page / and a warranty, / then starts the ingestion job and waits. / And look at the statistics. / **New, three**. / Everything else is zero.


▶ CLICK

Let's ask a question, / but first, / let's only **retrieve**. [ON SCREEN: run ask.py with --retrieve-only, point at the scores and the file names] [pause] These are the chunks it found, / with a score, / and the file each one came from. / This is the step to check first / when an answer looks wrong.


▶ CLICK

Now the full answer. [ON SCREEN: run ask.py with --model and your text model ID, point at "30 days" and the source] [pause] The model writes the answer from those chunks. / **Thirty days**, / and it cites returns-policy.md. / That citation is what lets a user trust the answer. [long pause]

Transition: Now, / let's change the documents.

## 6. Live demo, part 2: change the documents, sync again

(About 2 min 30 seconds)

This is the part that matters in real life. [pause]

▶ CLICK

The v2 folder is the same library, / with three changes. [ON SCREEN: open docs/v2 next to docs/v1] [pause] The return window goes from **thirty** days to **forty-five**. / There's a **new** loyalty program page. / The warranty page is **gone**. / And the shipping page / hasn't changed at all.


▶ CLICK

Remember our first sync. / Three new, / nothing else.


▶ CLICK

Now I sync v2. [ON SCREEN: run python sync.py docs/v2 and point at each count] [pause] The script makes the bucket match the folder. / And look at the statistics. / One **new**, / one **modified**, / one **deleted**, / and one **unchanged**. / The shipping page wasn't embedded again. / That's incremental sync, / working.


▶ CLICK

And now we ask again. [ON SCREEN: run ask.py for the return window, then for the warranty] [pause] The answer now says **forty-five** days. / And when I ask about the warranty, / it can't find anything, / because deleting the file / deleted its vectors too. [long pause]

Transition: And if something doesn't work for you, / here's what to check.

## 7. If it fails: three checks, then tear it down

(About 1 min 15 seconds)

Three problems cover most of what you'll hit. [pause]

▶ CLICK

If the deploy fails on the vector bucket or the Knowledge Base, / check your **Region**. / You need one with both S3 Vectors and Knowledge Bases, / like us-east-1.


▶ CLICK

If you get an access denied error, / check that your account can use **both** models. / Titan Embeddings for the sync, / and your text model for the answers. / And some models need an **inference profile** ID, / not the plain model ID.


▶ CLICK

And if an answer still shows old content, / check that the last ingestion job ended with **COMPLETE**. / Changes only reach the vectors after a sync.


▶ CLICK

And when you're done, / **tear it down**. / Run cdk destroy. / The lab costs a few cents, / but don't leave anything running. [long pause]

Transition: Let's wrap up.

## 8. Lecture recap: three things to remember

(About 1 min 15 seconds)

So, / let's bring it together. [pause]

▶ CLICK

First, / bucket in, / vectors out. / A data source chunks your files, / Titan embeds them, / and S3 Vectors stores them.


▶ CLICK

Second, / sync is **incremental**. / New and changed files get embedded, / deleted ones get removed, / and unchanged ones are skipped.


▶ CLICK

And third, / **nothing syncs on its own**. / Run the ingestion job on a schedule, / or when a new file arrives, / or your answers go stale. [pause]

So, / back to our one sentence. [pause] A Knowledge Base is only as fresh as its **last sync**, / so make syncing cheap, / incremental / and automatic. [pause] And that's the end of Section 4. / You can check and prepare your data, / format it for the model, / choose a vector store, / and keep it fresh. [long pause]

Transition: In the next section, / we make retrieval itself better. / Chunking, / embeddings, / hybrid search / and reranking.
