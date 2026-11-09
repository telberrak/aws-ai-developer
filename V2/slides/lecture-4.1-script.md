# Lecture 4.1: Data quality and multimodal pipelines — narration script

Section 4, Data pipelines and vector stores. About 10 minutes. The same text is in the speaker notes of `lecture-4.1.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Data quality and multimodal pipelines

(About 40 seconds)

Welcome to Section 4. / In the last section, / we chose the model. / Now we turn to the **data**. / Because in most real projects, / the model answers from your documents, / and those documents have to get into a vector store first. [pause] In this lecture, / you'll see how to check that data before you use it, / and how to turn calls, / scans / and videos into text you can search. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] **Check** your data before you embed it, / and turn every format into **clean text** first. [long pause]

Transition: So, / why does the data matter so much?

## 2. RAG is only as good as its data

(About 1 min 30 seconds)

Here's the path your data takes / before a single question gets answered. [pause]

▶ CLICK

It starts with your **sources**. / Documents, / database tables, / recorded calls, / images.


▶ CLICK

Then you **validate** it. / Is it complete? / Are there duplicates? / Is it up to date?


▶ CLICK

Then you **extract** it. / Every format, / whether it's audio, / a scanned form / or a video, / becomes text.


▶ CLICK

Then you **chunk** that text, / and turn each chunk into a vector with an embedding model. / We'll go deep on that in Section 5.


▶ CLICK

And finally, / the vectors land in a **vector store**, / ready for retrieval.


▶ CLICK

Here's why it matters. / A model doesn't know your data is wrong. / If you feed it an outdated policy, / it'll quote that outdated policy, / and it'll sound **completely sure**. [pause] Bad data in, / confident wrong answers out. / So in this lecture, / we focus on the two highlighted steps. / Validate, / and extract. [long pause]

Transition: First, / how do you check the data?

## 3. AWS Glue Data Quality checks the data

(About 2 minutes)

On AWS, / the tool for this is **AWS Glue Data Quality**. / You write rules / in a small language called DQDL, / the Data Quality Definition Language, / and Glue checks your data against them. [pause]

▶ CLICK

**IsComplete**. / Every row has a policy ID. / No missing values.


▶ CLICK

**IsUnique**. / No policy shows up twice. / Duplicates in a knowledge base mean the same chunk comes back over and over.


▶ CLICK

**DataFreshness**. / Nothing older than a day. / This is the one people forget, / and it's the one that causes outdated answers.


▶ CLICK

And **RowCount**. / If you normally get a hundred thousand rows / and today you got twelve, / the extract probably broke halfway.


▶ CLICK

So, / what happens when a rule fails? / You decide. / You can **stop** the job, / or send the bad rows to a quarantine location. / The scores go to **CloudWatch**, / so you can graph them, / and the results go to **EventBridge**, / so you can trigger an alert or a workflow.


▶ CLICK

And here's the good news. / You don't have to write every rule from scratch. / Glue can **profile** your data / and recommend a starting set of rules. / You review them, / keep what makes sense, / and add your own. [long pause]

Transition: Clean tables are one thing. / But what about audio, / scans / and video?

## 4. Turn every format into text you can use

(About 2 minutes)

A lot of company knowledge isn't text yet. / So for each format, / there's a service that turns it into text. [pause]

▶ CLICK

Calls and meetings / go to **Amazon Transcribe**. / You get a transcript, / speaker labels so you know who said what, / and it can **redact** personal data like card numbers before anything gets stored. / And if your business uses its own terms, / a custom vocabulary helps it get them right.


▶ CLICK

Scanned forms and PDFs / go to **Amazon Textract**. / It reads the text, / and it understands **forms** and **tables**, / so a table stays a table / instead of turning into a jumble of words.


▶ CLICK

And when you've got a **mix** / of documents, / images, / audio / and video, / there's **Bedrock Data Automation**. / One API for all of them. / We'll look at it more closely in a moment.


▶ CLICK

Finally, / sometimes you don't want text at all. / If people need to search **images**, / a multimodal embedding model / puts images and text into the same vector space, / so a text question can find a picture. [pause] Each of these is a managed service, / so there's no model for you to host. [long pause]

Transition: So, / what makes Bedrock Data Automation different?

## 5. One service for unstructured content

(About 1 min 30 seconds)

Bedrock Data Automation / takes unstructured content / and gives you structured results back. / Three things to know. [pause]

▶ CLICK

First, / **standard output**. / For each type of content, / you get ready-made results. / Document text and layout, / descriptions of images, / transcripts and summaries of audio and video. / No setup.


▶ CLICK

Second, / **custom output**. / Here you use **blueprints**. / You name the fields you want, / like an invoice number / or a claim amount, / and it returns them as JSON. / That's extraction, / without writing parsing code.


▶ CLICK

Third, / it plugs into your **RAG pipeline**. / You can run it on files in S3, / or you can pick it as the **parser** / when a Knowledge Base ingests your documents. / That's handy for PDFs full of charts and tables.


▶ CLICK

So here's the clue to listen for. / **Many formats**, / **structured fields** out, / and the **least custom code**. / When you see that combination, / think Bedrock Data Automation. [long pause]

Transition: Now, / let's put all of this into one pipeline.

## 6. A data pipeline you can trust

(About 1 min 30 seconds)

Here's a data pipeline you can actually trust, / in five steps. [pause]

▶ CLICK

One. / **Land**. / New files arrive in an S3 bucket.


▶ CLICK

Two. / **Check**. / Glue Data Quality runs its rules on anything structured.


▶ CLICK

Three. / **Convert**. / Transcribe, / Textract / or Data Automation, / depending on the format.


▶ CLICK

Four. / **Store**. / The clean text goes back to S3, / together with its **metadata**. / The source, / the date, / the department. / You'll need that metadata later to filter results.


▶ CLICK

Five. / **Sync**. / The Knowledge Base picks up the changes / and embeds only what's new.


▶ CLICK

Something has to run these steps in order. / That's **Step Functions**, / or **EventBridge** rules for simpler flows. / And any file that fails / goes to a **quarantine** prefix, / so a person can look at it / instead of it quietly going into your vector store.


▶ CLICK

And the reason to do it in this order? / Fixing data is cheap. / Re-embedding millions of chunks / because a bad batch got in / isn't. / So **check before you embed**. [long pause]

Transition: Let's wrap up.

## 7. Recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / validate first. / Glue Data Quality rules catch data that's missing, / duplicated / or stale, / before it reaches the model.


▶ CLICK

Second, / every format becomes text. / Transcribe for speech, / Textract for scans, / and Bedrock Data Automation when you've got a mix and want structured fields.


▶ CLICK

And third, / automate the pipeline. / Land, / check, / convert, / store, / sync. / And quarantine whatever fails. [pause]

So, / back to our one sentence. [pause] **Check** your data before you embed it, / and turn every format into **clean text** first. [long pause]

Transition: In the next lecture, / we look at the other side. / The inputs that go **to** the model, / and how to format and improve them.
