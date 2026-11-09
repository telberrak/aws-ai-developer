# Lecture 5.4: Demo: tuning chunking and adding a reranker — narration script

Section 5, Retrieval for RAG. About 15 minutes. The same text is in the speaker notes of `lecture-5.4.pptx`. The lab is in `labs/lab-5.4-chunking-and-reranking`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next. [ON SCREEN: …] = what to show during the live demo.

## 1. Tuning chunking and adding a reranker

(About 45 seconds)

In the last three lectures, / we talked about chunking, / embeddings, / search / and reranking. / Now / we **test** them. [pause] We'll build two Knowledge Bases over the same documents, / change **one** thing between them, / ask both the same questions, / and then put a reranker on top / to see how it changes the order. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Don't guess your retrieval settings. / **Test** them on your own documents, / one change at a time. [long pause]

Transition: So, / what are we building?

## 2. Two Knowledge Bases, one difference

(About 1 min 30 seconds)

Here's the setup. / One bucket, / two Knowledge Bases, / and a reranker on the side. [pause]

▶ CLICK

First, / **one S3 bucket** with two documents. / Both Knowledge Bases read the same files, / and both use the same embedding model, / Titan Text Embeddings V2.


▶ CLICK

The first Knowledge Base uses **fixed-size** chunks. / A hundred tokens each, / with almost no overlap. / That's small on purpose, / so we can see what goes wrong.


▶ CLICK

The second uses **semantic** chunking. / Up to three hundred tokens, / and it splits where the meaning of the text changes, / not at a fixed count. [pause] That's the only difference between the two. / So whatever changes in the results, / we know chunking caused it.


▶ CLICK

And at query time, / we add a **reranker**. / It's a model you call through the same Retrieve API, / so there's nothing extra to deploy. [long pause]

Transition: But the documents matter just as much as the settings. / Let's see what's in them.

## 3. Rules with exceptions, and a distractor

(About 1 min 15 seconds)

A test is only useful if it can **fail**. / So these two documents are built to find the weak spots. [pause]

▶ CLICK

The first is a **travel policy**, / with eight sections. / And many of its rules come with an exception a sentence or two later. / The hotel limit is a hundred and eighty dollars a night. / But in London, / New York, / Tokyo / and Zurich, / it's two hundred and sixty. / Cut those two sentences apart, / and you get a wrong answer.


▶ CLICK

The second is a short **FAQ**. / It uses the same words as the policy, / hotel, / budget, / claim, / but it often answers a **different** question. / "Is there a hotel budget for team offsites?" / sounds a lot like a question about hotel limits, / but it isn't one.


▶ CLICK

So here's the idea. [pause] Split rules test the **chunking**. / Look-alike text tests the **ranking**. / And when you build a test set for your own project, / do the same thing. / Pick the questions where you expect it to break. [long pause]

Transition: Now, / let's look at the code.

## 4. Three choices in the lab

(About 1 min 15 seconds)

The lab is one CDK app and two small scripts. / There are three choices worth seeing. [pause]

▶ CLICK

First, / each Knowledge Base gets its **own index** in the vector bucket. / That way, / their vectors never mix, / and we're comparing two clean results.


▶ CLICK

Second, / the **only** difference. / The fixed one says FIXED SIZE, / a hundred tokens. / The semantic one says SEMANTIC, / up to three hundred tokens, / with a buffer of one sentence / and a breakpoint threshold of ninety. / That threshold decides how big a change in meaning it takes to start a new chunk. [pause] And remember, / chunking is set when the data source is created. / To change it, / you create a new data source / and sync again.


▶ CLICK

Third, / the reranker. / In the Retrieve call, / we ask vector search for **ten** results, / and then the reranking configuration keeps the best **three**. / Retrieve wide, / rerank narrow. [long pause]

Transition: Let's run it.

## 5. Same question, two chunkings

(About 2 min 30 seconds)

[ON SCREEN: terminal in the lab folder, virtual environment active, Region set to one with a reranker model, such as us-west-2] [pause]

▶ CLICK

First, / I deploy. [ON SCREEN: run cdk deploy] [pause] CDK creates the bucket, / the vector bucket with two indexes, / and the two Knowledge Bases with their data sources.


▶ CLICK

Then I upload the documents / and sync **both** Knowledge Bases. [ON SCREEN: run python sync.py docs and wait for both jobs] [pause] Both jobs should end with COMPLETE. / The semantic one takes a little longer, / because it embeds sentences to decide where to split.


▶ CLICK

Now the real test. / Same question to both. [ON SCREEN: run compare.py with the London hotel question and point at each column] [pause] "What is the hotel limit in London?" / The script prints the top three chunks from each Knowledge Base, / side by side, / with the score / and the file each one came from.


▶ CLICK

And here's the kind of thing to look for. [pause] On the left, / the fixed chunks. / You might get a chunk that says the limit is a hundred and eighty dollars, / and stops. / The London rule can land in the **next** chunk. / A model reading only that chunk / would give the wrong answer, / with total confidence. [pause] On the right, / the semantic chunk usually holds the **whole** hotel section. / The rule, / the city exception / and the manager exception, / together. [pause] But notice the cost. / Each semantic chunk carries more words into the prompt. / Better context, / more tokens. / That's the trade-off you're always tuning. [long pause]

Transition: Now, / let's fix the order with a reranker.

## 6. Add a reranker

(About 2 min 15 seconds)

Here's what the reranker adds. / Three steps. [pause]

▶ CLICK

First, / **vector search** returns the ten chunks whose vectors are closest to the question. / That's fast, / but it's ranking by similarity, / not by whether a chunk actually **answers** the question.


▶ CLICK

Second, / the **reranker**. / It reads the question together with each of those ten chunks, / and gives each pair a relevance score. / It's slower than vector search, / which is why we only give it ten.


▶ CLICK

Third, / we keep the **top three**, / in the new order.


▶ CLICK

Let's try it. [ON SCREEN: run compare.py with the hotel booking question and the rerank flag, then point at the first result in each column] [pause] "Can I claim a hotel I booked myself?" / On the left, / plain vector search. / Watch for the FAQ answer about team offsites. / It shares words with the question, / so it can rank near the top. / On the right, / after reranking, / the chunks about booking through the travel portal / should move up, / because they actually answer the question. [pause] And don't compare the numbers across the two columns. / The left shows similarity scores, / the right shows the reranker's own relevance scores.


▶ CLICK

So what does it cost? [pause] One extra model call per query. / A little more **latency**, / and a little more **cost**. / For most RAG apps, / that's a good deal, / because the model now sees the right chunk first. [long pause]

Transition: And if something doesn't work for you, / here's what to check.

## 7. Three checks, then tear it down

(About 1 min)

Three problems cover most of what you'll hit. [pause]

▶ CLICK

If the reranker call fails, / check your **Region**. / Reranker models aren't offered everywhere. / Check the model catalog in the Bedrock console, / or use US West, / Oregon.


▶ CLICK

If you get an access denied error, / check that your account can use **both** models. / Titan Embeddings V2 for the sync, / and the reranker for the query.


▶ CLICK

And if both sides look the same, / first check that both ingestion jobs ended with COMPLETE. / Then ask about a rule that has an **exception**. / That's where chunking shows.


▶ CLICK

And when you're done, / **tear it down**. / Run cdk destroy. / The lab costs a few cents, / but don't leave anything running. [long pause]

Transition: Let's wrap up.

## 8. Three things to remember

(About 1 min 15 seconds)

So, / let's bring it together. [pause]

▶ CLICK

First, / change **one thing at a time**. / Two Knowledge Bases, / the same data, / the same embeddings, / and different chunking. / That's how you know what caused the difference.


▶ CLICK

Second, / chunk size is a **trade-off**. / Small chunks can cut a rule away from its exception. / Bigger chunks keep the context together, / but they cost more tokens in every prompt.


▶ CLICK

And third, / **retrieve wide, / rerank narrow**. / Ten candidates from vector search, / and the reranker keeps the best three. [pause]

So, / back to our one sentence. [pause] Don't guess your retrieval settings. / **Test** them on your own documents, / one change at a time. [pause] And that's the end of Section 5. / You can now chunk documents, / choose embeddings, / combine vector and keyword search, / rerank the results, / and give your apps one consistent way to retrieve. [long pause]

Transition: In the next section, / we turn to the other half of every request. / The **prompt**. / How to structure it, / version it, / and govern it.
