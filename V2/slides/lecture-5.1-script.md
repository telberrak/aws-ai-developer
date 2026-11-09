# Lecture 5.1: Chunking strategies and choosing embeddings — narration script

Section 5, Retrieval for RAG. About 10 minutes. The same text is in the speaker notes of `lecture-5.1.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Chunking strategies and choosing embeddings

(About 50 seconds)

Welcome to Section 5. / In Section 4, / we got clean data into a vector store. / Now we make **retrieval** good, / because in RAG, / the model can only answer from what you hand it. [pause] In this lecture, / we look at the two decisions you make before a single question is asked. / How you **split** your documents into chunks, / and which **embedding model** turns those chunks into vectors. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Split your documents into chunks that each hold **one idea**, / and embed them with a model you've **tested on your own data**, / because you'll live with it for the life of the index. [long pause]

Transition: So, / why does the size of a chunk matter so much?

## 2. Why chunk size matters

(About 1 min 20 seconds)

Think about what a chunk is for. / It's the piece of text that gets matched to a question, / and then handed to the model. [pause]

▶ CLICK

Make it **too big**, / and one chunk covers lots of topics. / Its vector becomes an average of all of them, / so the match gets diluted. / And every time it's retrieved, / you pay for all that extra context.


▶ CLICK

Make it **too small**, / and you get the opposite problem. / A sentence without its neighbours / often loses its meaning. / "It must be returned within 30 days." / What must? [pause]


▶ CLICK

What you want is **one idea per chunk**, / with enough context around it / that it still makes sense on its own.


▶ CLICK

And remember this. / Chunking happens at **ingestion**. / If you change the strategy later, / you re-ingest every document. / So it's worth getting right early. [long pause]

Transition: So, / what are your options?

## 3. Five ways to split a document

(About 2 min)

Amazon Bedrock Knowledge Bases gives you five ways to split a document. [pause]

▶ CLICK

**Fixed-size**. / You set a maximum number of tokens per chunk, / and a percentage of overlap. / The default option works the same way, / with chunks of about 300 tokens. / It's simple and predictable, / and it works well for short, / uniform documents, / like FAQs or support articles.


▶ CLICK

**Hierarchical**. / Each document is split into large **parent** chunks, / and each parent into smaller **child** chunks. / That's built for long, / structured manuals. / I'll show you how it works in a moment.


▶ CLICK

**Semantic**. / Instead of counting tokens, / it splits where the **meaning** changes. / That's great for documents that jump between topics.


▶ CLICK

**No chunking**. / Each file stays one chunk. / Use it when you've already split the content yourself, / say, / one product or one FAQ per file.


▶ CLICK

And **custom Lambda**. / After parsing, / Knowledge Bases calls your own Lambda function, / which does the splitting. / That's your answer for tables, / code, / or any special format, / and you can add your own metadata at the same time. [pause] When a scenario says the built-in strategies don't fit the document format, / think **Lambda**. [long pause]

Transition: Two of these need a closer look.

## 4. Hierarchical, semantic and overlap

(About 1 min 30 seconds)

Hierarchical and semantic chunking / are the two that people mix up. [pause]

▶ CLICK

With **hierarchical** chunking, / the search runs on the small **child** chunks. / Small chunks give you a precise match. / But what goes to the model / is the larger **parent** chunk the child belongs to. / So you get precision when you search, / and context when you answer. / Best of both.


▶ CLICK

With **semantic** chunking, / an embedding model compares neighbouring sentences, / and starts a new chunk where the topic changes. / The chunks are cleaner, / but there's a catch. / It calls a model during ingestion, / so ingestion costs **more**.


▶ CLICK

And one more idea, / for fixed-size chunks. / **Overlap**. / You repeat a small part of each chunk at the start of the next one, / usually 10 to 20 percent. / So if an idea gets cut in two at a boundary, / it still lands whole in one of the chunks. [long pause]

Transition: Now, / the second decision. / Which embedding model?

## 5. What to compare in an embedding model

(About 1 min 40 seconds)

Six things to compare when you pick an embedding model. [pause]

▶ CLICK

**Quality**. / How well it retrieves the right chunks / for **your** questions. / And the only way to know / is to test it on your own data.


▶ CLICK

**Dimensions**. / That's the length of each vector. / More dimensions can capture finer detail, / but they take more storage, / and the search is slower. / Often a smaller size loses very little.


▶ CLICK

**Max input**. / How many tokens the model accepts per input. / Your largest chunk has to fit, / or it gets cut off.


▶ CLICK

**Languages**. / Is your content English only, / or in many languages? / Some models are built for multilingual search.


▶ CLICK

**Modality**. / Text only, / or do you need images too, / like charts, / diagrams / or scanned pages?


▶ CLICK

And **cost**. / You pay per token to embed, / both your documents and every question. / And bigger vectors cost more to store. [long pause]

Transition: So, / which models will you actually meet in Bedrock?

## 6. Embedding models you'll meet

(About 1 min 30 seconds)

Here are the ones that come up most. [pause]

▶ CLICK

**Amazon Titan Text Embeddings V2**. / You choose 256, / 512 / or 1,024 dimensions, / and it accepts up to about 8,000 tokens per input. / It's a strong default for text RAG, / and it's the one we used in the Section 4 demo.


▶ CLICK

**Cohere Embed v3**. / It comes in an English and a multilingual version, / with 1,024 dimensions. / But each input is limited to 512 tokens, / so keep your chunks short.


▶ CLICK

**Cohere Embed v4**. / It handles text **and** images, / in many languages, / with much longer inputs. / That's a good fit for documents full of charts and scans.


▶ CLICK

And **Titan Multimodal Embeddings**. / It puts text and images in the **same** vector space, / so you can find an image / by describing it in words. [pause] Model versions change often, / so always check what's available in your Region. [long pause]

Transition: And whichever one you pick, / there's one rule you can't break.

## 7. One embedding model for the life of the index

(About 1 min 20 seconds)

You use **one** embedding model / for the whole life of the index. [pause]

▶ CLICK

First, / the **same model both ways**. / Your documents and your users' questions / must be embedded by the same model. / Vectors from two different models / live in different spaces, / so comparing them is meaningless.


▶ CLICK

Second, / the **dimensions are fixed**. / The index is created for one vector size, / and one distance metric.


▶ CLICK

So third, / **changing the model means re-embedding**. / You build a new index, / re-ingest everything, / test it, / and then switch the traffic over.


▶ CLICK

And in Knowledge Bases, / you can't change the embedding model after it's created. / So pick it with your test set, / **up front**. [long pause]

Transition: Let's wrap up.

## 8. Lecture recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / chunk to **one idea**. / Fixed-size with overlap, / hierarchical, / semantic, / no chunking, / or your own Lambda when the format is special.


▶ CLICK

Second, / choose your embedding model **on your data**. / Compare quality, / dimensions, / input length, / languages, / modality / and cost.


▶ CLICK

And third, / the model is **for life**. / Documents and questions share one model, / and changing it means re-embedding everything. [pause]

So, / back to our one sentence. [pause] Split your documents into chunks that each hold **one idea**, / and embed them with a model you've **tested on your own data**, / because you'll live with it for the life of the index. [long pause]

Transition: In the next lecture, / we look at how those vectors are searched, / and how to put the best chunks first.
