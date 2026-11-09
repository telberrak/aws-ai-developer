# Section 3: Designing GenAI Solutions — narration script

One block per slide, in deck order. The same text is in the speaker notes of `section-03-designing-genai-solutions.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. Lines starting "Transition:" are the spoken bridge into the next slide.

## Lecture 3.1: turning business requirements into a GenAI architecture

### Slide 1: Designing GenAI solutions

(About 85 seconds)

Welcome to Section 3. / This is where Domain 1 starts, / and Domain 1 is the **biggest** part of the exam, / at thirty-one percent. [pause]

This section is about the first job on any GenAI project: / work out what the business needs, / and turn it into an architecture you can **defend**. Most exam scenarios work the same way. / They describe the business first, / and expect you to design from it. [pause]

We'll cover four things. / Turning requirements into three decisions: / the model, / the integration pattern / and the deployment approach. A proof of concept on Amazon Bedrock, / to prove the idea before anyone spends real money. Reviewing a design with the AWS Well-Architected Framework / and its Generative AI Lens. And four common architectures you'll see again and again. Then in Lab 1, / you'll run a real lens review / in the Well-Architected Tool. [pause]

This lecture goes through requirements, / the three decisions, / clues that point to designs, / and a shared backbone. If I had to sum up this lecture in one sentence, / it would be this. [pause] Find the **how well** requirements, / then pick the **simplest** managed design that meets every one. [long pause]

Transition: So, / let's start where every design starts: / with the requirements.

### Slide 2: Requirements come in two kinds

(About 90 seconds)

Here's the point of this slide. / Every design starts with requirements, / and they come in **two** kinds. [pause]

The first kind is what the system must **do**. / Answer employee questions about HR policies. Summarize customer calls. Draft replies to support tickets. Update a record in another system. [pause] These are the functional requirements, / and they usually point you at a pattern. Answering from documents points at **RAG**. / Taking actions points at an **agent**.

The second kind is **how well** it must do it. / How fast does an answer need to come back? How accurate does it need to be, / and what happens when it's wrong? What can each request cost? How many users at peak? [pause] Can data leave a Region, / or leave the company at all? And does every answer need to be traceable / for an auditor?

Now, / on the exam, / these quality requirements are usually what separates two answers that **both** work. And they tend to sit at the end of the scenario, / in phrases like "with the lowest latency" / or "while keeping data within the VPC". [pause] So when you read a question, / find the functional need first, / then hunt for the quality constraints. They **decide** the answer. [long pause]

Transition: Once you know the requirements, / you can make the three big decisions.

### Slide 3: Every design answers three questions

(About 80 seconds)

Once you know the requirements, / a GenAI architecture comes down to **three** decisions. [pause]

First, / which foundation model. You weigh its capability, / whether it handles the right modality, / like text, images or documents, / how much context it can take, / how fast it is, / and what it costs. We go deep on choosing models in Section 4.

Second, / which integration pattern. These are the four patterns from Section 2: / prompt engineering, / RAG, / fine-tuning / and agents, / or a mix of them. [pause] Remember the ladder. / Climb only as high as you **need**.

Third, / how it's deployed. On Bedrock, / that means on-demand, / batch, / or provisioned throughput. Or, / when you need a model or a level of control that Bedrock doesn't give you, / a SageMaker AI endpoint.

Around those three decisions / sit the usual building blocks: / an API layer, / orchestration, / storage, / security / and monitoring.

And here's the tie-breaker the exam uses all the time. [pause] When several designs meet every requirement, / the best answer is usually the **simplest managed** option. Less to build, / less to run, / less to go wrong. [long pause]

Transition: So, / how do you get from a requirement to a choice? / Let's look at the clues.

### Slide 4: Requirements point to design choices

(About 80 seconds)

This slide is a cheat sheet. / It links typical requirements to design choices. [pause] Honestly, / use it as a starting point, / not a rule.

If the system must answer from company documents, / design toward **RAG**. On AWS, / the managed way to do that / is Bedrock Knowledge Bases.

If it must take actions, / like creating a ticket or checking an order, / that's an **agent** with tools.

If the output must always sound like the brand / or follow a fixed format, / start with a good prompt template. [pause] Only move to fine-tuning / if prompting can't hold it.

If chat needs to feel fast, / think streaming responses, / a smaller or faster model, / and caching.

If you need to process millions of documents / and nobody is waiting, / use **batch** inference.

And if data must stay private, / think VPC endpoints, / so traffic stays off the internet, / KMS for encryption, / and Guardrails to filter sensitive information.

You'll notice / each of these is a **managed** feature. That's deliberate. [pause] On this exam, / the managed option that meets all the requirements / usually beats the custom build. [long pause]

Transition: And most of these choices / plug into the same basic shape. / Let's draw it.

### Slide 5: Most designs share one backbone

(About 80 seconds)

Most GenAI designs on AWS / share the same **backbone**. [pause]

On the left, / the client. / A web app, / a mobile app, / or a chat tool like Slack.

Then an API layer. / It gives you throttling, / authorization / and a stable endpoint. That's usually Amazon API Gateway, / with authentication, / for example through Amazon Cognito.

Then orchestration. / For a simple request and response, / a Lambda function is enough. For multi-step workflows with retries and branches, / Step Functions.

Then the model and its data: / Bedrock for the model, / Knowledge Bases if you need RAG, / and Guardrails to filter inputs and outputs.

And across every layer: / IAM for least-privilege access, / KMS for encryption, / CloudWatch for metrics and logs, / and CloudTrail for auditing who did what. [pause]

When an exam option leaves out something the requirements **clearly** need, / like authentication for a public app / or logging for an audited one, / that's a quick way to eliminate it. [pause]

So, / back to our one sentence. / Find the **how well** requirements, / then pick the **simplest** managed design that meets every one. [long pause]

Transition: But a design on paper isn't proof. / Next lecture, / we prove it with a PoC on Bedrock.

## Lecture 3.2: building a proof of concept on Amazon Bedrock

### Slide 6: Proof of concept on Amazon Bedrock

(About 45 seconds)

Lecture 3.2. / Before a company commits to a full GenAI build, / it should **prove** the idea works. That's the job of a proof of concept, / or PoC. [pause]

A good PoC is small, / fast / and measured. It answers questions with **numbers**, / not opinions. Bedrock is ideal, / because you can try several models / with no infrastructure to manage.

We'll cover what it proves, / how to run it, / what to measure, / and the mistakes that mislead. [pause] If I had to sum up this lecture in one sentence, / it would be this: / a PoC proves the idea with **real** data, / against numbers agreed **before** you start. [long pause]

Transition: So, / what is a PoC actually for?

### Slide 7: A PoC answers three questions

(About 70 seconds)

A proof of concept exists to answer **three** questions. [pause]

One: / is it **feasible**? Can a foundation model really do this task well enough, / with our real data? Not a demo with three hand-picked examples, / but a representative sample.

Two: / is it **fast** enough? Do the latency and throughput meet what users need? [pause] A model that gives brilliant answers in forty seconds / won't work for a live chat.

Three: / is it **worth** it? Does the business value beat the cost? That means estimating cost per request, / multiplying by real volume, / and comparing it to the value, / like hours saved or tickets deflected.

Now, / here's the key point. [pause] Each question needs a **number**, / agreed before you start. For example: / at least eighty-five percent of answers rated correct, / under three seconds to first token, / and under two cents per request. [pause] Without targets, / every PoC looks like a success. [long pause]

Transition: So, / how do you actually run one? / Here's a simple five-step method.

### Slide 8: Five steps to a useful PoC

(About 90 seconds)

Here's a simple method for running a PoC, / in **five** steps. [pause]

Step one, / define success. Agree the quality, / latency / and cost targets with the business / **before** you write any code.

Step two, / build a test set. Collect real examples, / somewhere around fifty to two hundred, / with the answer you'd expect for each. [pause] This set is **gold**. You'll reuse it to compare models now, / and as a regression test later.

Step three, / try models in Bedrock. Start in the console playground / to get a feel for a few candidates and your prompt. Then move to Converse API calls in code, / so you can run the whole test set automatically, / and swap models just by changing the model ID.

Step four, / measure. Score the quality of each answer, / record latency, / and record the input and output tokens / so you can work out cost. Bedrock's model evaluation feature can help score quality, / including using a model as a judge. We'll cover that properly in Domain 5.

Step five, / decide. Go ahead, / change the design, / for example by adding RAG or trying a smaller model, / or stop. [pause] Stopping early is a perfectly **good** result for a PoC. / It saved the company a full build. [long pause]

Transition: Step four said "measure", / so let's be specific about what that means.

### Slide 9: Measure what the business will judge

(About 80 seconds)

Here's the point. / Measure what the business will **judge** you on. [pause]

Answer quality. / Score every answer in the test set. You can use human reviewers, / simple rules like "does the JSON parse" / or "does it mention the right policy", / or a stronger model acting as a judge.

Latency. / Measure time to first token, / which is what users feel in a streaming chat, / and total time to complete. And measure it from the **client's** side, / so you include the network and your own code, / not just the model.

Cost per request. / The Converse API returns input and output token counts / with every response. Multiply them by the model's prices, / and you have cost per request.

Cost at scale. / Multiply that by the expected daily volume. [pause] This is where many PoCs get a surprise. Two cents a request sounds tiny, / until it's **two million** requests a day. [pause]

And business value, / in the business's own terms: / minutes saved per ticket, / percentage of tickets deflected, / and so on. That's what a decision maker compares the cost **against**. [long pause]

Transition: Even with good measures, / a PoC can still fool you. / Let's look at how.

### Slide 10: Four ways a PoC misleads you

(About 80 seconds)

Four mistakes / make PoCs look **better** than reality. [pause]

First, / cherry-picked data. If the test set only has clean, typical examples, / you'll miss the messy real cases. Scanned PDFs, / typos, / ambiguous questions, / other languages.

Second, / no baseline. If you don't know how the current process performs, / how long a human takes / and how accurate they are, / then you can't say the GenAI version is **better**.

Third, / ignoring scale. A design that works for ten testers / can hit cost limits and service quotas / at ten thousand users. Check the quotas for your model and Region, / and estimate cost at real volume.

Fourth, / skipping security / because "it's just a PoC". [pause] Real customer data needs proper IAM, / encryption / and guardrails. Production needs them anyway, / so plan them early and avoid a redesign.

On the exam, / PoC questions often hinge on one of these. If an option validates with **representative** data, / measures against clear targets / and keeps security in place, / it's usually the right one. [pause] Our one sentence again: / **real** data, / numbers agreed **before** you start. [long pause]

Transition: Next lecture, / we check the design itself / with Well-Architected and the Generative AI Lens.

## Lecture 3.3: the Well-Architected Framework and the Generative AI Lens

### Slide 11: Well-Architected and the Generative AI Lens

(About 45 seconds)

Lecture 3.3. / How do you know a design is **good**? [pause] AWS gives you a structured check: / the Well-Architected Framework, / and, / for GenAI, / the Generative AI Lens.

The exam expects you to know what they are, / how to use them in the Well-Architected Tool, / and how they help teams build **standard**, reusable components / instead of inventing their own.

We'll cover the pillars, / the lens, / the tool, / and standard components. [pause] If I had to sum up this lecture in one sentence, / it would be this: / a design is good when it **passes** a structured review, / not just when it works. [long pause]

Transition: So, / let's start with the pillars.

### Slide 12: Six pillars, applied to GenAI

(About 70 seconds)

The Well-Architected Framework has **six** pillars. You may know them already, / so let's focus on what each one means / for a GenAI application. [pause]

Operational excellence: / versioning your prompts, / monitoring model behavior, / and running evaluations automatically / when anything changes.

Security: / least-privilege IAM, / guardrails on inputs and outputs, / protecting personal data, / and keeping traffic private with VPC endpoints.

Reliability: / handling throttling with retries and backoff, / using cross-Region inference for capacity, / and having a fallback when a model call fails.

Performance efficiency: / the right model size for the task, / streaming responses, / and caching repeated results.

Cost optimization: / controlling tokens, / batch for offline work, / smaller models where they're good enough, / and prompt caching.

And sustainability: / not running a huge model when a small one does the job, / and not wasting inference on calls you didn't need. [pause]

When an exam question asks you to improve a design, / it's often asking / which pillar is **weak**. [long pause]

Transition: Now, / what does the Generative AI Lens add?

### Slide 13: A lens adds GenAI-specific questions

(About 75 seconds)

The framework is general. / A **lens** extends it with questions for one type of workload, / and the Generative AI Lens is the one for GenAI. [pause]

It follows the life of a GenAI workload. **Scoping**: / is generative AI even the right tool here, / and what does success look like? **Model selection**: / which model, / and on what evidence? **Customization**: / is prompting enough, / or do you need RAG or fine-tuning? Development and integration: / building the app and connecting it to data and other systems. Deployment: / running it securely and reliably. And continuous improvement: / evaluating, / monitoring / and improving over time.

At each stage, / the lens asks questions organized by the six pillars, / with best practices for each. For example, / do you protect against prompt injection? / Do you track cost per request? / Do you evaluate model output before release? [pause]

Honestly, / you don't need to memorize the questions. You need to know the lens **exists**, / what it covers, / and that you apply it in the Well-Architected Tool. [long pause]

Transition: So, / let's see how a review in that tool actually works.

### Slide 14: How a lens review works

(About 80 seconds)

The AWS Well-Architected Tool, / or WA Tool, / is a service in the console / that runs these reviews for you, / in **five** steps. [pause]

Step one: / define your workload. Give it a name, / the Regions, / the environment, / like production or pre-production, / and the owners.

Step two: / apply lenses. The Well-Architected Framework lens is always there, / and you add the Generative AI Lens / from the lens catalog.

Step three: / answer the questions. For each one, / tick the best practices you already follow, / and add notes. [pause] Be **honest**. The value is in finding gaps, / not in a perfect score.

Step four: / read the risks. The tool flags each question as high risk, / medium risk, / or no risk, / and links every risk to guidance on how to fix it.

Step five: / plan and track. The improvement plan lists what to fix first. When you've made changes, / save a **milestone**, / so you can show progress over time.

The tool itself has no extra charge, / which makes it easy to use. And you'll do exactly this in Lab 1. [long pause]

Transition: A review checks one design. / Now, / how do we keep **every** team consistent?

### Slide 15: Build it once, reuse it everywhere

(About 70 seconds)

With several GenAI apps, / consistency becomes a real problem. Each team picks its own models, / prompts / and security. [pause] The fix is **standard**, reusable components.

Infrastructure as code. / A shared CDK construct or CloudFormation template / that creates a Bedrock app the approved way, / with logging, encryption and IAM already right. Teams deploy it / instead of starting from scratch.

Approved prompts. / Versioned prompt templates in Bedrock Prompt Management. So teams reuse tested prompts, / and you can see exactly which version is in production.

Shared guardrails. / One Guardrails configuration that holds the company's content and privacy rules, / reused by every application.

And a review baseline. / The Generative AI Lens becomes the checklist / every new design must pass before launch. [pause]

On the exam, / when a scenario mentions many teams, / inconsistent implementations, / or governance across deployments, / look for answers built on **shared**, standardized components. [pause] Our one sentence: / a design is good when it **passes** a structured review. [long pause]

Transition: Next lecture, / we put it all together / in four case studies.

## Lecture 3.4: architecture case studies

### Slide 16: Architecture case studies

(About 30 seconds)

Lecture 3.4. / Four common GenAI architectures: / a support chatbot, / document question answering, / content generation, / and an agentic workflow. [pause]

Notice how the **requirements** drive each design. Then a closer look at document Q&A, / a worked exam-style question, / and Lab 1. [pause] If I had to sum up this lecture in one sentence, / it would be this: / same backbone every time, / and the requirements decide where the **weight** sits. [long pause]

Transition: Here they are, / side by side.

### Slide 17: Requirements drive the shape

(About 80 seconds)

Here are the four designs. / The requirement **shapes** each one. [pause]

A customer support chatbot needs fast, safe answers / that stay on topic. So: / streaming with ConverseStream for a responsive feel, / Guardrails to block off-topic or harmful content / and filter personal data, / and conversation history stored in DynamoDB, / so the bot remembers the session.

Document question answering needs answers grounded in the company's documents, / **with** sources. That's RAG. / A Bedrock knowledge base over documents in S3, / a vector store such as OpenSearch Serverless, / and citations returned with every answer.

Content generation, / like product descriptions or marketing emails, / needs a consistent brand voice / at **volume**. So: / well-tested prompt templates, / batch inference for large runs, / and a human review step before anything is published, / for example with Amazon Augmented AI.

An agentic workflow needs multi-step actions in other systems, / like processing a refund. That's an agent with tools, / run on AgentCore, / often with Step Functions coordinating the steps / and handling approvals. [pause]

Same backbone each time, / different centre of gravity. [long pause]

Transition: One of these shows up most on the exam, / so let's zoom in on document Q&A.

### Slide 18: Document Q&A, end to end

(About 75 seconds)

Let's look closer at document Q&A, / because it appears **constantly** on the exam. [pause]

The documents, / like policies and manuals, / live in an S3 bucket.

A Bedrock knowledge base ingests them. During a **sync**, / it splits each document into chunks, / turns each chunk into a vector with an embedding model, / and stores those vectors.

The vectors go into a vector store. OpenSearch Serverless is a common choice, / and Aurora with pgvector and others are options too. We'll compare vector stores in Section 6.

At query time, / the knowledge base retrieves the most relevant chunks for the user's question, / passes them to the model along with the question, / and returns the answer / with **citations** to the source documents. [pause]

Two requirements show up again and again. If documents change often, / you re-run the sync when they change, / for example triggered by an S3 event. And if the data is private, / you lock it down with IAM, / encrypt with KMS, / and keep traffic inside your network / with VPC endpoints. [long pause]

Transition: Now, / let's use exactly this design / to answer an exam-style question.

### Slide 19: Pick the design that meets every need

(About 85 seconds)

Let's finish with a worked example. / I wrote this one for the course. / It's not from the exam. [pause]

A manufacturer wants field engineers / to ask questions about equipment manuals. The manuals are updated **every week**. Every answer must show which manual it came from. And the team wants the **least** operational overhead.

Option A: / fine-tune a model on the manuals every month. Monthly is too slow for weekly updates, / and a fine-tuned model can't cite its sources. Out.

Option B: / a Bedrock knowledge base on the manuals in S3, / with citations, / and a sync whenever the manuals change. It stays fresh, / it cites sources, / and it's fully managed. [pause] That's the **answer**.

Option C: / a self-managed vector database on EC2 with custom chunking code. It would work, / but it's the most overhead of all, / and the question asked for the least. Out.

Option D: / put every manual into every prompt. That hits context limits quickly / and costs a fortune in tokens. Out. [pause]

Notice the method. / Find the constraints, / weekly freshness, / citations / and least overhead, / then strike every option that breaks **one**. [long pause]

Transition: Now it's your turn to review a real design, / in Lab 1.

### Slide 20: Review a design in the WA Tool

(About 75 seconds)

Time for Lab 1. / You'll review a GenAI design / the way a real architecture review would. [pause]

In the lab folder in the course repo, / there's a sample design for a customer support chatbot. Read it first. It works, / but it has gaps, / **on purpose**.

Then open the Well-Architected Tool in the console, / create a workload for this chatbot, / and apply the Generative AI Lens.

Answer the lens questions / based **only** on what the design document says. If the document doesn't mention something, / don't tick it. [pause] That's exactly how a reviewer would treat it.

When you finish, / look at the risks the tool reports. Pick the top high-risk items, / and write down how you'd change the design to fix each one. The lab README lists the gaps I planted, / so you can check your answers.

The WA Tool has no charge, / and nothing in this lab creates billable resources. When you're done, / you can delete the workload, / or keep it as a reference. [long pause]

Transition: Once you've done the lab, / let's wrap up the section.

### Slide 21: Take the quiz, then choose your models

(About 70 seconds)

That's the end of Section 3. / Let's recap. [pause]

Requirements come in two kinds: / what the system must do, / and how well it must do it. And the quality requirements usually **decide** the answer. Every design comes down to three decisions: / model, / pattern / and deployment. The simplest managed option that meets every requirement / usually wins.

A proof of concept answers three questions, / feasibility, / performance / and value, / with numbers agreed up front / and a representative test set. The Well-Architected Framework and its Generative AI Lens / give you a structured review in the WA Tool, / and standard components keep many teams consistent.

And the four designs, / chatbot, / document Q&A, / content generation / and agentic workflow, / share one backbone. [pause] Our one sentence: / the requirements decide where the **weight** sits. [long pause]

Your next step / is the **ten-question** quiz for this section.

Transition: Then join me in Section 4, / where we evaluate and choose foundation models, / switch models without code changes, / and make it all resilient. [pause] See you there.
