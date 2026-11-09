# Lecture 5.4 demo: tuning chunking and adding a reranker

This is the code for the demo in Lecture 5.4. You deploy two Amazon Bedrock Knowledge Bases over the same documents. They're identical except for one thing: how they split the documents into chunks. Then you ask both the same questions, compare what comes back, and finally add a reranker to see how it changes the order of the results.

**Cost:** a few cents. Two small documents, a few embedding calls and a handful of rerank requests cost very little, and S3 Vectors charges only for what you store and query. **Teardown:** `cdk destroy`.

## What gets deployed

- **Source bucket**: one S3 bucket with the documents, read by both Knowledge Bases
- **Vector store**: one S3 vector bucket with two indexes, `kb-fixed` and `kb-semantic` (1024 dimensions, cosine distance)
- **Knowledge Base `lab-5-4-fixed`**: fixed-size chunks of 100 tokens with almost no overlap (1 percent, the minimum)
- **Knowledge Base `lab-5-4-semantic`**: semantic chunks of up to 300 tokens, split where the meaning of the text changes
- **IAM role**: lets both Knowledge Bases read the bucket, call Titan Text Embeddings V2 and write to their own index

Both use Amazon Titan Text Embeddings V2. The chunking is the only difference, so any difference in the results comes from chunking.

The reranker isn't deployed. It's a model you call at query time, through the `rerankingConfiguration` of the Retrieve API.

## The documents

- `docs/travel-policy.md`: a travel and expense policy with eight sections. Several rules come with an exception a sentence or two later, such as the hotel limit and the higher limit for expensive cities.
- `docs/expenses-faq.md`: a short FAQ that uses the same words as the policy (hotel, budget, claim, late) but often answers a different question. It's there to distract the vector search.

## Before you start

- Your account is set up as in Lecture 1.3, including the AWS CDK. Bootstrap the account and Region once with `cdk bootstrap`.
- **Pick a Region with S3 Vectors, Knowledge Bases and a reranker model.** Reranker models aren't offered in every Region, so check the Bedrock console's model catalog first. `us-west-2` (US West, Oregon) has all three at the time of writing.
- Your account can use **Amazon Titan Text Embeddings V2** and a reranker model: **Amazon Rerank 1.0** (`amazon.rerank-v1:0`) or **Cohere Rerank 3.5** (`cohere.rerank-v3-5:0`).
- Your own IAM user or role needs `bedrock:Retrieve`, plus `bedrock:Rerank` and `bedrock:InvokeModel` for the reranker. The administrator access from Lecture 1.3 covers this.

## Steps

1. Install and deploy:

   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   cdk deploy
   ```

2. Upload the documents and sync both Knowledge Bases:

   ```bash
   python sync.py docs
   ```

   Both jobs should end with `COMPLETE` and 2 documents indexed. The semantic one takes a little longer, because it embeds sentences to decide where to split.

3. Compare the chunking. Each command shows the top 3 chunks from both Knowledge Bases side by side:

   ```bash
   python compare.py "What is the hotel limit in London?"
   python compare.py "When can I fly business class?"
   python compare.py "What if I lose a receipt?"
   ```

4. Add the reranker. This retrieves 10 candidates from one Knowledge Base, then lets the reranker pick the best 3:

   ```bash
   python compare.py "What is the hotel limit in London?" --rerank
   python compare.py "Can I claim a hotel I booked myself?" --rerank
   python compare.py "Can I claim a hotel I booked myself?" --rerank --kb semantic
   ```

   To use Cohere instead, add `--reranker cohere.rerank-v3-5:0`.

## What to look for

Exact scores and orders depend on the embedding and reranker versions, so look for these patterns rather than specific numbers.

- **Fixed-size chunks cut rules in half.** With 100-token chunks, a rule and its exception often land in different chunks. For the London question, a fixed chunk may hold the 180-dollar limit without the 260-dollar city limit, or the city list without the number.
- **Semantic chunks keep a section together.** The semantic Knowledge Base tends to return the whole hotel section in one chunk, so the model would see the rule, the city exception and the manager exception at once.
- **Bigger chunks cost context.** Each semantic chunk carries more words into the prompt. That's the trade-off: more complete context, more tokens.
- **The reranker fixes the order.** Vector search ranks by how similar the words are, so an FAQ answer that shares words with the question can rank high even when it doesn't answer it. The reranker reads each candidate together with the question and usually moves the chunk that actually answers it to the top.
- **Scores on the two sides aren't comparable.** Vector search returns similarity scores; the reranker returns its own relevance scores.

## If it fails

| Problem | Fix |
| --- | --- |
| CDK says the bootstrap stack is missing | Run `cdk bootstrap` once for this account and Region, then deploy again. |
| The deploy fails on the vector bucket or a Knowledge Base | Check that the Region supports both S3 Vectors and Knowledge Bases. |
| An ingestion job fails with an access error | Check that your account can use Titan Text Embeddings V2 in this Region. |
| `--rerank` fails with a validation error or `AccessDeniedException` | Check that a reranker model is available in this Region and that your account can use it. Try the other reranker with `--reranker`. |
| Both sides look the same | Check that both ingestion jobs ended with `COMPLETE`. Try a question whose answer has an exception, like the hotel or flight rules. |

## Changing the chunking

Chunking is set when a data source is created and can't be changed afterwards. To try other settings, change `CHUNKING` in `app.py` and deploy again; CloudFormation replaces the data source, and you run `sync.py` again. You can also add a third entry, for example hierarchical chunking, by following the same pattern.

## Clean up

```bash
cdk destroy
```

This deletes both Knowledge Bases, the vector bucket and its indexes, and empties and deletes the source bucket.
