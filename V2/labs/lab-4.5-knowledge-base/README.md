# Lecture 4.5 demo: a Knowledge Base with an S3 source and incremental sync

This is the code for the demo in Lecture 4.5. You deploy an Amazon Bedrock Knowledge Base that reads documents from an S3 bucket and stores its vectors in Amazon S3 Vectors. Then you sync, ask questions, change the documents, and sync again to see that only the changes are processed.

**Cost:** a few cents. Embedding a handful of small documents and a few questions costs very little, and S3 Vectors charges only for what you store and query, with no cluster running in the background. **Teardown:** `cdk destroy`.

## What gets deployed

- **Source bucket**: an S3 bucket that holds the documents
- **Vector store**: an S3 vector bucket with one index (`kb-index`, 1024 dimensions, cosine distance)
- **Knowledge Base** `lab-4-5-kb`: embeds with Amazon Titan Text Embeddings V2
- **Data source** `s3-docs`: points at the source bucket and splits documents into chunks of 300 tokens with 20 percent overlap
- **IAM role**: lets the Knowledge Base read the bucket, call the embedding model and write to the vector index, and nothing else

## Why S3 Vectors

It's the cheapest vector store for a lab: you pay for storage and queries, and nothing runs while you're not using it. OpenSearch Serverless gives lower latency and hybrid search, but it bills for capacity units every hour, even when it's idle, so it's easy to forget and expensive to leave running. Lecture 4.3 compares the options.

## Before you start

- Your account is set up as in Lecture 1.3, including the AWS CDK. Bootstrap the account and Region once with `cdk bootstrap`.
- Use a Region where Bedrock Knowledge Bases and Amazon S3 Vectors are both available, such as `us-east-1`.
- Your account can use **Amazon Titan Text Embeddings V2** and one text model to write answers. Note that model's ID, or its inference profile ID if the console says the model needs one.

## Steps

1. Install and deploy:

   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   cdk deploy
   ```

   The scripts read the stack outputs themselves, so you don't need to copy anything.

2. First sync. This uploads the three documents in `docs/v1` and runs an ingestion job:

   ```bash
   python sync.py docs/v1
   ```

   Expect `new 3`, and `modified`, `deleted` and `unchanged` at 0.

3. Ask a question. First see what retrieval finds, then let a model answer from it:

   ```bash
   python ask.py "How long do I have to return an item?" --retrieve-only
   python ask.py "How long do I have to return an item?" --model [text-model-id]
   ```

   The answer says 30 days and cites `returns-policy.md`.

4. Change the documents. `docs/v2` is the same set with three changes: the return window goes from 30 to 45 days, `loyalty-program.md` is new, and `warranty.md` is gone. `shipping.md` is identical.

   ```bash
   python sync.py docs/v2
   ```

   Expect `new 1`, `modified 1`, `deleted 1`, `unchanged 1`. The unchanged file isn't embedded again.

5. Ask again:

   ```bash
   python ask.py "How long do I have to return an item?" --model [text-model-id]
   python ask.py "What does the warranty cover?" --model [text-model-id]
   ```

   The first answer now says 45 days. The second can't find the warranty any more, because deleting the file removed its vectors.

## Things to notice

- Each sync is **incremental**. The Knowledge Base compares the bucket with the last sync, then embeds new and changed files and removes the vectors of deleted ones.
- Nothing syncs on its own. In a real system you'd start the ingestion job on a schedule with EventBridge, or from an S3 event when a file lands.
- The index marks `AMAZON_BEDROCK_TEXT` and `AMAZON_BEDROCK_METADATA` as non-filterable, because the chunk text is too large for filterable metadata in S3 Vectors.
- `sync.py` works out "unchanged" as scanned minus new, modified and failed. The ingestion job reports the other counts directly.

## If it fails

| Problem | Fix |
| --- | --- |
| CDK says the bootstrap stack is missing | Run `cdk bootstrap` once for this account and Region, then deploy again. |
| The deploy fails on the vector bucket or the Knowledge Base | Check that the Region supports both S3 Vectors and Knowledge Bases, or deploy to `us-east-1`. |
| The ingestion job fails with an access error | Check that your account can use Titan Text Embeddings V2 in this Region. |
| `ask.py` returns an `AccessDeniedException` or a validation error | Check that your account can use the text model. If the console says it needs an inference profile, pass the profile ID, for example `us.[model-id]`. |
| An answer still shows old content | Check that the last ingestion job ended with `COMPLETE`. Changes only reach the vectors after a sync. |

## Teardown

```bash
cdk destroy
```
