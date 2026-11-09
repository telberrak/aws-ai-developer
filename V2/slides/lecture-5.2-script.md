# Lecture 5.2: Vector search, hybrid search and reranking — narration script

Section 5, Retrieval for RAG. About 10 minutes. The same text is in the speaker notes of `lecture-5.2.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Vector search, hybrid search and reranking

(About 40 seconds)

In the last lecture, / we split our documents and turned them into vectors. / Now a question comes in. / How do we find the right chunks, / and how do we make sure the **best** ones come first? [pause] In this lecture, / I'll show you how vector search works, / how to measure "close", / the settings that shape the results, / hybrid search, / and reranking. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Vector search finds chunks that are **close in meaning**, / hybrid search adds **exact words**, / and a reranker puts the **best** ones first. [long pause]

Transition: So, / what actually happens when a question comes in?

## 2. How vector search finds the right chunks

(About 1 min 30 seconds)

Four steps, / every time. [pause]

▶ CLICK

First, / the **question**. / The user asks in plain words. / "How long do I have to return a jacket?"


▶ CLICK

Second, / we **embed** it. / And it has to be with the **same** model we used for the documents, / so the question and the chunks live in the same space.


▶ CLICK

Third, / we **search**. / The vector store finds the vectors nearest to the question's vector. / That's called **k-nearest neighbours**, / or k-NN, / where k is how many you want back.


▶ CLICK

And fourth, / it **returns** the top chunks, / each with a score, / so you can see how close each one was.


▶ CLICK

Now, / one detail that matters at scale. / **Exact** k-NN compares the question with every single vector. / With millions of vectors, / that's slow. / So vector stores use **approximate** search, / like HNSW, / which only checks a smart subset. / It's much faster, / and nearly as accurate. / That's what you're using almost every time. [long pause]

Transition: But what does "nearest" actually mean?

## 3. Three ways to measure "close"

(About 1 min 10 seconds)

There are three common ways to measure how close two vectors are. [pause]

▶ CLICK

**Cosine** similarity. / It looks at the **angle** between two vectors, / not their length. / It's the usual choice for text.


▶ CLICK

**Dot product**. / It takes the angle **and** the length into account. / And when the vectors are normalized, / which many embedding models do for you, / it ranks results exactly like cosine.


▶ CLICK

**Euclidean** distance. / The straight-line distance between two points. / Here, / smaller means closer.


▶ CLICK

So which one do you pick? / The one the embedding model was **built for**. / The model's documentation tells you. / And you set it when you create the index, / so it's another decision you make up front. [long pause]

Transition: Now, / the settings you can change on every search.

## 4. Three settings that shape the results

(About 1 min 20 seconds)

Three settings shape what comes back. [pause]

▶ CLICK

**Number of results**. / How many chunks the search returns. / In Knowledge Bases, / the default is five, / and you can go up to 100.


▶ CLICK

**Metadata filters**. / Equals, / in, / greater than, / and you can combine them with and / and or. / They narrow the search to the right documents. / Only this product, / only this year, / only what this tenant is allowed to see.


▶ CLICK

And the **search type**. / Semantic, / or **hybrid**, / when your vector store supports it. / More on that in a moment.


▶ CLICK

Here's the balance with the number of results. / Too few, / and you can miss the chunk that holds the answer. / Too many, / and you fill the prompt with noise, / which costs more and can confuse the model. [long pause]

Transition: So, / what's hybrid search, / and why would you want it?

## 5. Meaning plus keywords

(About 1 min 30 seconds)

Semantic search and keyword search / are good at different things. [pause]

▶ CLICK

**Semantic** search catches **meaning**. / "Can I get my money back?" / finds the refund policy, / even though the word "refund" never appeared in the question.


▶ CLICK

**Keyword** search catches **exact terms**. / Product codes, / error IDs, / people's names, / acronyms. / Semantic search can miss those, / because "error 4012" and "error 4013" look almost the same to an embedding model.


▶ CLICK

**Hybrid** search runs both, / and merges the scores. / So you get the paraphrases **and** the exact matches.


▶ CLICK

In Knowledge Bases, / hybrid search works with the **OpenSearch** and **Aurora PostgreSQL** vector stores. / With S3 Vectors, / search is semantic only. [pause] So when a scenario says users search by part number or error code, / and results are poor, / think **hybrid search**. [long pause]

Transition: But even with good search, / the best chunk isn't always at the top.

## 6. Retrieve many, keep the best

(About 1 min 30 seconds)

That's where **reranking** comes in. / The pattern is simple. / Retrieve many, / keep the best. [pause]

▶ CLICK

First, / **retrieve wide**. / Vector search is fast, / so ask it for more candidates than you need. / Say, / 30 to 50.


▶ CLICK

Second, / **rerank**. / A reranker model reads the question and each chunk **together**, / and gives each pair a relevance score. / That's slower than vector search, / but much more precise, / and on 50 chunks, / it's quick enough.


▶ CLICK

Third, / **keep the best**. / Only the top few chunks go to the model. / Better answers, / and a smaller prompt.


▶ CLICK

In Bedrock, / you've got **Amazon Rerank** and **Cohere Rerank 3.5**. / With Knowledge Bases, / you add one in the reranking configuration of the Retrieve call. / Or, / if your vectors live somewhere else, / you call the Rerank API directly. [long pause]

Transition: So, / how do you know which of these to reach for?

## 7. Match the fix to the symptom

(About 1 min 20 seconds)

Start from the symptom. / Each one points to a fix. [pause]

▶ CLICK

The right chunk comes back, / but it's **ranked low**. / Add a **reranker**.


▶ CLICK

**Exact** codes, / names / or IDs are missed. / Turn on **hybrid search**.


▶ CLICK

Results come from the **wrong** product, / or the wrong tenant. / Add **metadata filters**.


▶ CLICK

The answer is only **partly** there. / Return more results, / or go back and **rechunk**, / because the idea may be split across chunks.


▶ CLICK

And retrieval is too **slow** or too **costly**. / Return fewer results, / or use smaller vectors. [pause] Scenario questions often describe exactly one of these symptoms, / so match the symptom, / and you've found the answer. [long pause]

Transition: Let's wrap up.

## 8. Lecture recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / vector search finds chunks that are **nearest in meaning**. / Embed the question with the same model, / and approximate search finds the top chunks fast.


▶ CLICK

Second, / **tune** what comes back. / The number of results, / metadata filters, / and hybrid search when exact terms matter.


▶ CLICK

And third, / **retrieve many, / keep the best**. / A reranker scores the candidates, / and only the top few reach the model. [pause]

So, / back to our one sentence. [pause] Vector search finds chunks that are **close in meaning**, / hybrid search adds **exact words**, / and a reranker puts the **best** ones first. [long pause]

Transition: In the next lecture, / we work on the question itself. / Rewriting it, / breaking it down, / and giving every app the same way to retrieve.
