# Section 2: GenAI on AWS refresher — narration script

One block per slide, in deck order. The same text is in the speaker notes of `section-02-genai-on-aws-refresher.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. Lines starting "Transition:" are the spoken bridge into the next slide.

## Lecture 2.1: foundation models, tokens, context windows and inference parameters

### Slide 1: GenAI on AWS refresher

(About 80 seconds)

Welcome to Section 2. / This is a refresher, / about an hour and a half, / and its job is to make sure we share the **same** vocabulary / before we go deep in Domain 1.

If you use Bedrock every day, / watch this at a faster speed. [pause] But don't skip the lab at the end. Lab 0 is where you make your **first** Bedrock call from Python, / and every later lab builds on that setup.

We'll cover five things. Foundation models, / tokens, / context windows / and inference parameters. A tour of Amazon Bedrock: / its catalog, / APIs / and pricing options. When SageMaker AI is the better fit. The four core patterns: / prompt-only, / RAG, / agents / and fine-tuning. And how Bedrock AgentCore, / Strands Agents / and the Model Context Protocol / fit together. [long pause]

This first lecture goes from the model, / to tokens, / to the settings. If I had to sum up this lecture in one sentence, / it would be this. [pause] You don't build the model, / you **steer** it, / and tokens and a few settings decide what it can hold, / what it costs / and how it answers. [long pause]

Transition: So, / let's start with the foundation model itself.

### Slide 2: One pre-trained model, many jobs

(About 85 seconds)

A foundation model / is one big model that can do **many** jobs. A provider has pre-trained it **once**, / on a very broad dataset, / so it can handle lots of different tasks / without being trained for each one. We call it a foundation model, / or **FM**.

Three ideas matter for this exam. [pause] First, / it's **pre-trained**. Someone else did the expensive training, / not you. Remember from Section 1: / model training is out of scope for AIP-C01.

Second, / you **adapt** it. You steer a foundation model with prompts. With context you retrieve and add to the prompt. With tools it can call. And, / when you really need to, / with fine-tuning. [pause] Choosing between those methods / is one of the most tested things on this exam, / and we'll come back to it in Lecture 2.4.

Third, / many models are **multimodal**. Depending on the model, / it can take or produce text, / images / and documents. And some models produce **embeddings**. Those are the numeric vectors / behind semantic search and RAG. [pause]

So keep this framing for the whole course. The exam is about **using** and **adapting** foundation models in production, / never about building them. [long pause]

Transition: Now, / models don't read words the way we do, / so let's look at what they actually read: / tokens.

### Slide 3: Tokens set your limits and your bill

(About 85 seconds)

Here's the point of this slide. [pause] Tokens set your limits, / and tokens set your **bill**.

A token is a word, / or a piece of a word. Models don't see characters. They read and write in tokens, / and every limit and every bill / is counted in them.

The **context window** is the most tokens / one single request can hold. And that budget is **shared**. [pause] Your system prompt, / the conversation history, / any documents you retrieve for RAG, / and the model's answer / all have to fit. So when an exam question mentions truncated answers, / or errors on long documents, / think context window **first**. [pause]

Pricing for on-demand use is **per token**, / with input and output tokens priced separately for each model. That's why so many cost answers / are really about tokens. Shorter prompts. Pruning context. Caching repeated prompts. Limiting response length. Or using a smaller model. We'll go deep on that in Domain 4.

Exact token limits and prices vary by model, / and they change over time. So I won't ask you to memorize numbers. [pause] The exam tests the **concepts**, / and the Bedrock console shows the current values. [long pause]

Transition: So tokens are the unit. Next, / let's see the five settings that shape how the model uses them.

### Slide 4: Five settings shape every response

(About 90 seconds)

Five settings shape **every** response. We call them inference parameters, / and the exam expects you to know all five.

**Temperature** controls randomness. A low temperature makes the model pick the most likely tokens, / so answers are focused and repeatable. A higher temperature gives you more varied, / creative output. [pause]

**Top P** limits sampling to the smallest set of tokens / whose probabilities add up to P. **Top K** limits sampling to the K most likely tokens. Both narrow the choice of the next token. [pause] But top K isn't supported by every model. So in Bedrock's Converse API, / it goes in the model-specific fields, / additionalModelRequestFields, / not in the standard inferenceConfig.

**Max tokens** caps the length of the response. That matters for cost and latency. And honestly, / it's a common cause of answers that stop mid-sentence. If an exam scenario describes cut-off answers, / check max tokens / and the context window. [pause]

**Stop sequences** are pieces of text / that end generation as soon as the model writes them. That's handy for structured output.

A practical tip. [pause] Change temperature or top P, / but usually **not** both at once. That way, / you can tell which change made the difference. [long pause]

Transition: So now you know the five settings. [pause] Let's see how to pick them for a real job.

### Slide 5: Match the settings to the job

(About 85 seconds)

So how do you choose the settings? [pause] You **match** them to the job.

On the left, / tasks with **one** right answer. Extracting fields, / classifying a ticket, / generating SQL, / producing JSON that code will parse, / or RAG answers. Use a **low** temperature. You want the same input / to give the same output.

In the middle, / assistants and support bots. A **moderate** temperature keeps answers natural, / without wandering off topic.

On the right, / brainstorming, / marketing copy / or story variations, / where variety is the point. A **higher** temperature helps there. [pause]

Now, / watch for this pattern on the exam. A scenario says users get **inconsistent** answers to the same question. The free fix, / with no architecture change, / is to **lower** the temperature. [pause] If answers are too repetitive or bland, / it goes the other way.

And these are starting points. In production, / you A/B test settings against real prompts / rather than guessing. [pause]

So, / back to our one sentence. You don't build the model, / you **steer** it, / and tokens and a few settings decide what it can hold, / what it costs / and how it answers. [long pause]

Transition: Next lecture, / we'll tour the service that serves those models on AWS: / Amazon Bedrock.

## Lecture 2.2: a tour of Amazon Bedrock, its APIs and its pricing options

### Slide 6: A tour of Amazon Bedrock

(About 40 seconds)

Lecture 2.2. [pause] Here's the service that serves foundation models for you: / **Amazon Bedrock**, / the key service on this exam. It's in almost every domain: / Knowledge Bases, / Guardrails, / Prompt Management, / Prompt Flows, / AgentCore, / evaluations / and the model APIs.

We'll cover the catalog, / the APIs, / and the ways to pay, / a favorite in cost questions.

If I had to sum up this lecture in one sentence, / it would be this. [pause] Bedrock gives you **many** models behind **one** API, / and you choose how to pay / by the **shape** of your traffic. [long pause]

Transition: So, / let's start with the catalog.

### Slide 7: Many providers behind one service

(About 90 seconds)

Here's the point. [pause] One service, / and behind it, / models from **many** providers. Amazon Bedrock is fully managed, / and providers include Amazon, / with the Nova and Titan families, / plus Anthropic, / Meta, / Mistral AI, / Cohere / and others. [pause] The catalog changes often, / so the exam focuses on choosing the right **type** of model for a job, / not on memorizing names.

On the left are the model types you'll use in this course. Text and chat models, / for generation. Multimodal models, / that accept images as well as text. Embedding models, / which turn text into vectors for semantic search, / like Amazon Titan embeddings. Image generation models. And reranker models, / which reorder search results by relevance. You'll use rerankers in Section 7.

On the right is your checklist / before you can call a model. [pause] It has to be offered in your **Region**. You have to enable **access** to it in the Bedrock console. Your IAM role needs **permission** to invoke it. And you need its model ID, / or, / for cross-Region inference, / an inference profile ID.

Here's a classic troubleshooting question. [pause] The code is fine, / but the call fails with an **access denied** error. The answer is usually model access, / or IAM. [long pause]

Transition: So you've picked a model, / and you're allowed to call it. Next, / let's see **how** you call it.

### Slide 8: Converse is the default way in

(About 90 seconds)

You call Bedrock models through a handful of runtime APIs, / and **Converse** is the default way in.

Converse is the one to reach for first. It gives you one consistent request and response shape / across chat models, / so switching models / is mostly a change of model ID. [pause] It also supports **tool use**, / which is how agents call functions, / plus system prompts and inference settings / in a standard format.

ConverseStream is the same thing, / but the answer comes back token by token. That's what you use for a chat UI, / where users should see text appear **immediately**. Streaming comes up often in latency questions.

InvokeModel takes the model's own **native** JSON body. Every provider's format is a bit different, / which is why you need to format input data / according to each model's requirements. You'll typically use InvokeModel for embedding models. And there's a streaming version too, / InvokeModelWithResponseStream.

For large offline workloads, / a **batch inference job** reads thousands of prompts from S3 / and writes the results back to S3, / asynchronously. [pause]

One detail that trips people up. The runtime calls are on the **bedrock-runtime** client. But control-plane actions, / like creating a batch job or managing models, / are on the **bedrock** client. [long pause]

Transition: Now, / let's see what a Converse call actually looks like in code.

### Slide 9: A Converse call in Python

(About 90 seconds)

This is a Converse call in Python, / with boto3. And it's the **exact** pattern you'll use in Lab 0.

First, / you create a client for **bedrock-runtime**. Then you call converse, / with four things. [pause] The model ID, / which you set from the model you enabled in your account. An optional system prompt, / here telling the model to act as a concise AWS tutor. The messages, / which are a list of turns. Each turn has a role, / user or assistant, / and a list of content blocks. And the inference config, / with temperature and max tokens, / the parameters we covered in the last lecture.

The response gives you the model's message, / and you read the text from the first content block. It also gives you a **usage** section, / with input and output token counts. [pause] Get in the habit of logging that. It's the raw material for cost tracking, / and we'll build it into a CloudWatch dashboard in Domain 4.

Now, / notice what's **not** here. [pause] Nothing about the model's native request format. That's the whole point of Converse. To try a different model, / you change the model ID, / and the rest stays the same. [long pause]

Transition: So now you know how to call a model. [pause] The next question is how you **pay** for those calls.

### Slide 10: Pick the option by traffic shape

(About 105 seconds)

The right way to pay for inference / depends on the **shape** of your traffic. Honestly, / this table is exam gold.

**On-demand** is pay per token, / with no commitment. It's the default, / and the right answer for variable or unpredictable traffic.

**Batch** inference is also priced per token, / but at a **discount**, / because it runs asynchronously. If a scenario says "process millions of documents overnight", / or "results aren't needed in real time", / think batch. [pause]

**Provisioned Throughput** means you buy model units, / billed per hour, / for dedicated, / guaranteed capacity. It fits steady, / high-volume workloads, / and it's also used to serve some customized models. If a question mentions throttling at consistently high volume, / or needing guaranteed throughput, / provisioned is the likely answer. [pause] If traffic is spiky or low, / it's the **expensive** wrong answer.

**Cross-Region inference** uses inference profiles / to route on-demand requests across Regions. That gives you burst capacity and resilience, / especially for models with limited Regional availability.

Finally, / **prompt caching**. On supported models, / caching a long, / repeated prompt prefix, / like a big system prompt, / cuts cost and latency. We'll use it in Lab 18. Check the pricing page for current rates. [pause]

So, / back to our one sentence. Bedrock gives you many models behind one API, / and you choose how to pay / by the shape of your traffic. [long pause]

Transition: But Bedrock isn't the only way to run a model on AWS. In the next lecture, / we'll see when SageMaker AI is the better fit.

## Lecture 2.3: when SageMaker AI and JumpStart fit instead of Bedrock

### Slide 11: SageMaker AI and JumpStart

(About 40 seconds)

Lecture 2.3. [pause] Bedrock is the default, / but sometimes you want to host a model yourself, / on endpoints **you** control. That's **Amazon SageMaker AI**. And **SageMaker JumpStart** gives you a catalog of open-weight models / you can deploy in a few clicks.

We'll compare them side by side, / then I'll give you a simple rule for choosing.

If I had to sum up this lecture in one sentence, / it would be this. [pause] Default to **Bedrock**, / and move to SageMaker AI / only when the scenario gives you a **reason**. [long pause]

Transition: So, / let's put them side by side.

### Slide 12: Managed API versus your own endpoint

(About 85 seconds)

Bedrock is a managed API. [pause] SageMaker AI gives you **your own** endpoint. Let's compare them row by row.

**Infrastructure.** Bedrock is serverless. There are no instances to choose or scale. With a SageMaker AI endpoint, / you pick the instance type, / often GPUs for large models, / and you configure scaling.

**Models.** Bedrock gives you a curated catalog from its providers. SageMaker gives you JumpStart, / a catalog of open-weight models you can deploy. And you can also bring any model you like, / in your own container.

**Customization.** Bedrock offers managed fine-tuning and related options, / for the models that support them. SageMaker gives you **full** control. That includes parameter-efficient techniques like LoRA adapters, / and the SageMaker Model Registry / for versioning and deploying customized models.

**Pricing.** Bedrock is per token, / or provisioned units. A SageMaker endpoint is billed per instance-hour while it's running, / whether or not anyone calls it. [pause] That last point matters for cost questions, / and for your lab budget.

**Operational effort.** Bedrock is the lowest. With SageMaker, / you own the endpoint. [pause]

So when a question says **"least operational overhead"**, / Bedrock is almost always the starting point. [long pause]

Transition: Which brings me / to the simple rule I promised.

### Slide 13: Default to Bedrock, unless…

(About 95 seconds)

Here's the rule to carry into the exam. [pause] Default to Bedrock, / **unless** the scenario gives you a reason not to. There are four common reasons.

One. The model you need isn't available in Bedrock. For example, / a specific open-weight model, / or a domain model your team already has.

Two. You need control over the hardware or the serving stack. A particular GPU instance, / a custom inference container, / or special model-loading behavior. [pause] Container-based deployment, / tuned for memory, / GPU use and token throughput, / is SageMaker territory.

Three. You run your own fine-tuning pipeline, / with versioning, / approval and rollback, / using SageMaker Model Registry and automated pipelines.

Four. A small, / task-specific model would be **cheaper** than a large general one, / for a narrow, / high-volume task.

When one of those is true, / SageMaker AI is the answer. Often with JumpStart to get the model, / Model Registry to version it, / and a pipeline to deploy it. [pause]

A side note. Bedrock also has **Custom Model Import**, / for bringing certain supported model architectures into Bedrock. Check the docs for current support, / but know it exists as a middle ground. [pause]

So, / back to our one sentence. Default to Bedrock, / and move to SageMaker AI / only when the scenario gives you a reason. [long pause]

Transition: Now you know **where** to run a model. The next lecture is about **how** you make it useful: / the four core architecture patterns.

## Lecture 2.4: the four core GenAI architecture patterns

### Slide 14: Four core architecture patterns

(About 35 seconds)

Lecture 2.4. [pause] Almost every exam scenario / uses one of four patterns, / or a mix: / prompting, / RAG, / fine-tuning / and agents. Name the pattern quickly, / and you've eliminated **half** the options.

We'll meet the patterns, / put them on a ladder, / then compare RAG and fine-tuning.

If I had to sum up this lecture in one sentence, / it would be this. [pause] Climb only as **high** as you need: / a knowledge problem means RAG, / a behavior problem means fine-tuning. [long pause]

Transition: So, / let's meet the four patterns.

### Slide 15: Four ways to make a model useful

(About 95 seconds)

There are four ways to make a model useful, / and they run through Domain 1 and Domain 2 of the exam.

One: / **prompt engineering**. You change only what you send to the model. Clear instructions, / a few examples, / a defined output format, / maybe a system prompt with a role. No new data sources, / and no training. [pause] It's **always** where you start.

Two: / retrieval augmented generation, / or **RAG**. At query time, / you search your own documents, / pull back the most relevant chunks, / and put them in the prompt, / so the model answers from them. [pause] This is how you give a model knowledge it was never trained on, / and knowledge that changes often.

Three: / **fine-tuning**. You train the model further / on your own labeled examples. That changes how it **behaves**: / its tone, / its format, / its handling of a specialized task. It's more effort and cost, / and the knowledge is frozen at training time.

Four: / **agents**. The model doesn't just answer. It plans, / decides which tools to call, / such as APIs, / databases or other models, / looks at the results, / and keeps going until the task is done. [pause]

Real systems combine them. An agent might use RAG as one of its tools, / with a carefully engineered prompt on top. [long pause]

Transition: So those are the four. [pause] Now let's put them in order of cost and effort.

### Slide 16: Climb only as high as you need

(About 80 seconds)

Climb only as high as you need. [pause] That's the rule here. Think of the patterns as a ladder / of cost, / effort / and time.

The bottom rung is **prompt engineering**. It takes minutes, / and costs almost nothing beyond the tokens.

Next is **RAG**. You need a pipeline to ingest and chunk documents, / an embedding model, / and a vector store. But no training.

Then **fine-tuning**. You need curated, / labeled training data, / training jobs, / evaluation, / and often provisioned capacity or an endpoint / to serve the customized model.

At the top is training a model **from scratch**. For this exam, / that's almost never the right answer. [pause] It's the classic distractor.

So the exam rule is: / climb only as high as the problem requires. If a better prompt fixes it, / that's the answer with the least effort. If the model lacks your company's facts, / go to RAG. Only reach for fine-tuning / when you need to change behavior that prompting can't fix. [pause]

Agents aren't a rung. They sit **beside** the ladder, / and orchestrate whichever rungs you use. [long pause]

Transition: Now, / the two middle rungs get mixed up more than any others. So let's put RAG and fine-tuning head to head.

### Slide 17: RAG or fine-tuning?

(About 85 seconds)

This is the comparison the exam loves most, / so let's make it a **reflex**.

If the scenario says the data **changes often**, / like product catalogs, / policies or tickets, / choose RAG. You just re-index the documents. A fine-tuned model would need retraining every time.

If answers must **cite their sources**, / choose RAG. You can return the chunks you retrieved / alongside the answer. A fine-tuned model has no built-in way / to tell you where something came from. [pause]

If the problem is **tone, format or style**, / like always answering in the company voice, / or always producing a structure that prompting can't hold, / fine-tuning is the stronger tool.

For a specialized task or heavy domain jargon, / fine-tuning helps the model learn the pattern, / while RAG helps with the facts.

And if the scenario asks for the **least effort** to get started, / RAG wins, / because it needs no labeled training data. [pause]

So, / back to our one sentence. Climb only as high as you need. A **knowledge** problem means RAG. A **behavior** problem means fine-tuning. [pause] And if a better prompt solves it, / that comes first. [long pause]

Transition: One pattern still needs a closer look, / and that's agents. In the next lecture, / we'll see the AWS pieces that build, / run / and connect them.

## Lecture 2.5: AgentCore, Strands Agents and MCP, then Lab 0

### Slide 18: AgentCore, Strands and MCP

(About 35 seconds)

Lecture 2.5, / the last one here. Agents matter a lot, / especially in Domain 2, / and three names keep coming up: / Amazon Bedrock AgentCore, / Strands Agents, / and the Model Context Protocol, / or **MCP**.

They're easy to mix up. So we'll put them in **one** picture, / practice spotting them, / then do Lab 0, / your first Bedrock call.

If I had to sum up this lecture in one sentence, / it would be this. [pause] **Strands** builds, / **AgentCore** runs, / **MCP** connects. [long pause]

Transition: So, / let's look at that picture.

### Slide 19: Each piece has one job

(About 2 min)

Each piece of the agent stack has **one** job. [pause] Read the picture from the top down.

First, / you need somewhere to **write** the agent: / its system prompt, / the model it uses, / and the tools it can call, / as plain Python functions. That's **Strands Agents**, / an open-source SDK from AWS. It handles the loop for you: / reason, / call a tool, / read the result, / and keep going. [pause]

Next, / you need a safe place to **run** that agent. That's **Amazon Bedrock AgentCore**, / a managed platform made of several services. A runtime that hosts the agent securely and scales it. Memory, / for short- and long-term context. A gateway that turns your APIs and Lambda functions / into tools the agent can call. Identity, / for handling who the agent acts as. And observability, / for tracing what it did. [pause] AgentCore works with Strands, / and with other frameworks too.

Then you need a standard way to **connect** agents to tools and data. That's **MCP**, / the Model Context Protocol, / an open standard. An MCP server exposes tools in a standard way, / and any MCP-aware agent can discover and use them. You should know how to expose tools through MCP, / for example with Lambda or ECS.

At the bottom is the foundation model, / the reasoning engine, / typically called through Bedrock. [pause]

You'll also see **Bedrock Agents**, / the earlier, / fully managed agent feature you configure in the console. We'll compare all of these properly in Section 9. For now, / remember the jobs. [pause] Strands builds. AgentCore runs. MCP connects. [long pause]

Transition: Now let's practice using that picture / on the kind of wording the exam uses.

### Slide 20: Which piece does the scenario want?

(About 70 seconds)

Let's practice spotting the **clue words**. [pause] Each scenario points to one piece.

"Build a custom agent in Python with our own tools." [pause] That's about **writing** the agent, / so think Strands Agents.

"Host and scale agents securely, / with each user session isolated." That's about **running** the agent in production, / so AgentCore Runtime.

"Remember user preferences across sessions." That's state that lasts **beyond** one conversation, / so AgentCore Memory.

"Expose our existing APIs or Lambda functions / as tools the agent can use." That's AgentCore **Gateway**.

"A standard interface, / so many different agents can share the same tools." [pause] That's the job of **MCP**. Build an MCP server once, / and any MCP-aware client can use it.

Don't worry about the details yet. In Section 9, / we'll build an agent with Strands, / deploy it to AgentCore, / and connect it to an MCP server. For now, / you just need the map. [long pause]

Transition: Enough theory for this section. Let's make your first real call, / in Lab 0.

### Slide 21: Same call, two ways

(About 90 seconds)

Time for Lab 0. [pause] You'll make the **same** Bedrock call / in two ways.

First, / with Python and boto3. Open the lab folder in the course repo, / labs, / lab-00-first-bedrock-call. Set your Region, / and the model ID of the model you enabled in Section 1, / and run converse.py. Then change the temperature from **0.2** to **0.9**, / and run it a few times. Notice how the answers vary more. [pause] Look at the usage numbers too, / and see how the output token count / tracks the length of the answer.

Second, / with the AWS CLI. The command is **aws bedrock-runtime converse**, / with the model ID / and the same messages structure, / as JSON. It's the same API, / so the response has the same shape. That's useful for quick tests, / and for scripts.

If something fails, / here's where to look. [pause] An **access denied** error? Check that model access is enabled in the Bedrock console for your Region, / and that your profile has permission for bedrock:InvokeModel. A **validation** error about the model ID? Some models need an inference profile ID, / not the base model ID. The lab README covers both.

The whole lab costs a few cents. [pause] So pause the video, / do the lab, / and come back for the wrap-up. [long pause]

Transition: Welcome back. Let's wrap up the section, / and see what comes next.

### Slide 22: Take the quiz, then start designing solutions

(About 85 seconds)

That's the end of Section 2. [pause] Let's recap.

Foundation models work in **tokens**, / with a context window that limits input plus output, / and you control them with temperature, / top P / and max tokens. Amazon Bedrock is the default way to use them on AWS, / through the **Converse** API, / and you pick on-demand, / batch / or provisioned throughput / based on the shape of your traffic. [pause] SageMaker AI fits when you need a model, / or a level of control, / that Bedrock doesn't give you. The four patterns are prompt engineering, / RAG, / fine-tuning and agents, / and you climb the ladder only as high as you need. A knowledge problem means RAG. A behavior problem means fine-tuning.

And for agents, / back to our one sentence for this lecture. [pause] **Strands** builds, / **AgentCore** runs, / **MCP** connects. [long pause]

Your next step is the **ten-question** quiz for this section. If you score under eight, / rewatch the lecture on the patterns before you move on, / because everything after this builds on it. [pause]

Transition: Then join me in Section 3, / where Domain 1 starts. We'll turn business requirements into a GenAI architecture, / build a proof of concept, / and review it with the Well-Architected Generative AI Lens. [pause] See you there.
