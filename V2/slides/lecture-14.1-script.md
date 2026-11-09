# Lecture 14.1: The "Which service?" drill — narration script

Section 14, Final review and exam day. About 12 minutes. The same text is in the speaker notes of `lecture-14.1.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. The "Which service?" drill

(About 40 seconds)

Welcome to the final section. / Final review, / and exam day. [pause] We start with a drill. / I describe a situation, / and you name the AWS service. / Fast. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Find the **constraint** in the question first, / and the service usually names itself. [long pause]

Transition: So, / how does the drill work?

## 2. Three moves for every scenario

(About 1 min)

Every scenario gets the same three moves. [pause]

▶ CLICK

One. / **Spot the constraint**. / Lowest cost, / least effort, / real time, / most secure. / One phrase usually decides the answer.


▶ CLICK

Two. / **Name the service**. / Say it out loud, / before you even look at the options.


▶ CLICK

And three. / **Say why**. / One reason it fits, / and one reason the closest rival doesn't. [pause] That last part is what turns a guess into an answer. / And here's how to use this lecture. / After each scenario, / pause the video, / answer it yourself, / and then carry on. [long pause]

Transition: Round one. / Safety and data.

## 3. Protect and ground the answers

(About 2 min)

Round one. / Protecting and grounding the answers. [pause]

▶ CLICK

You need to block a denied topic, / and mask personal data in prompts and answers, / for every model you use. [pause]

That's **Amazon Bedrock Guardrails**. / One policy, / applied on every call, / to the input and the output. / A system prompt can only ask. / A guardrail enforces.


▶ CLICK

Your assistant must answer from company documents in S3, / with citations, / and stay up to date. [pause]

**Bedrock Knowledge Bases**. / It chunks, / embeds and retrieves for you, / and returns citations. / And a sync keeps it fresh.


▶ CLICK

You need to find personal data that's already sitting in S3 buckets, / across the whole account. [pause]

**Amazon Macie**. / It scans data at rest in S3, / and reports where the sensitive data lives.


▶ CLICK

You need to detect and redact personal data in text, / inside your own application code. [pause]

**Amazon Comprehend**. / You call it from your code, / on the text in front of you. / Macie looks at buckets. / Comprehend looks at text. [long pause]

Transition: Round two. / Building.

## 4. Agents, prompts and configuration

(About 2 min)

Round two. / Agents, / prompts / and configuration. [pause]

▶ CLICK

You want to run an agent with tools, / memory and identity, / without managing any servers. [pause]

**Amazon Bedrock AgentCore**. / Runtime, / memory, / gateway for tools, / and identity, / all managed for you, / and it works with the agent framework you already use.


▶ CLICK

You want to version your prompts, / with variables, / so every app calls an approved version. [pause]

**Bedrock Prompt Management**. / Prompts become versioned resources, / not strings buried in your code.


▶ CLICK

You want to chain a prompt, / a Knowledge Base / and a Lambda function, / without writing glue code. [pause]

**Bedrock Flows**. / You connect the steps visually, / and call the whole flow as one.


▶ CLICK

You need to switch the model in production, / without a redeploy, / and roll back if it goes wrong. [pause]

**AWS AppConfig**. / The model ID lives in configuration, / it rolls out gradually, / and it rolls back automatically on an alarm. [long pause]

Transition: Round three. / Models and capacity.

## 5. Pay for the right capacity

(About 2 min)

Round three. / Paying for the right capacity. [pause]

▶ CLICK

Your traffic is steady and high, / and you need reserved capacity, / or you're serving a custom model. [pause]

**Provisioned Throughput**. / You buy model units, / and the capacity is yours. / It's also how you serve many custom models.


▶ CLICK

You need to summarize two million documents overnight, / at the lowest price. [pause]

**Batch inference**. / Nobody's waiting for the answer, / so you submit a job, / and you pay a lower price than on-demand.


▶ CLICK

Your traffic bursts past one Region's quota, / and you can't change the code. [pause]

**Cross-Region inference**. / You call an inference profile, / and Bedrock spreads the requests across Regions for you.


▶ CLICK

You want easy prompts to go to a smaller model, / and hard ones to a larger model. [pause]

**Intelligent Prompt Routing**. / One endpoint, / and Bedrock picks the model per request, / to save cost without losing quality. [long pause]

Transition: The last round. / Documents, / quality / and people.

## 6. Extract, evaluate and review

(About 2 min)

Round four. / Extract, / evaluate / and review. [pause]

▶ CLICK

You need to pull fields out of PDFs, / images, / audio and video, / into structured output. [pause]

**Bedrock Data Automation**. / You define what you want, / and it returns structured results, / from any of those formats.


▶ CLICK

You want to compare three models on your own prompts, / with scores. [pause]

**Bedrock model evaluation**. / Automatic metrics, / a model as a judge, / or human reviewers, / on your own dataset.


▶ CLICK

Low-confidence results must go to people for review. [pause]

**Amazon Augmented AI**, / or A2I. / It sends those results to a human review workflow.


▶ CLICK

You need to train or host your own model, / in your own container, / with full control. [pause]

**Amazon SageMaker AI**. / When Bedrock's managed options aren't enough, / and you need control of the training and the hosting. [long pause]

Transition: Now, / the traps. / Where the answers look alike.

## 7. Four traps between close answers

(About 1 min 45 seconds)

Most wrong answers aren't random. / They're the close rival. / Here are four pairs to keep apart. [pause]

▶ CLICK

**Macie or Comprehend?** / Macie scans data at rest in S3. / Comprehend reads text inside your application. / Buckets, / or text.


▶ CLICK

**A guardrail, or a system prompt?** / A guardrail is enforced on every call. / A system prompt only asks the model nicely. / When the question says must, / or always, / it's a guardrail.


▶ CLICK

**Provisioned Throughput, or cross-Region inference?** / Provisioned Throughput is reserved capacity you pay for. / Cross-Region inference uses spare capacity across Regions, / at on-demand prices. / Steady and guaranteed, / or bursty and flexible.


▶ CLICK

And **a Knowledge Base, or fine-tuning?** / Fresh facts come from retrieval. / Style and behavior come from tuning. / If the data changes every week, / it's a Knowledge Base. [long pause]

Transition: Let's wrap up.

## 8. Lecture recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / constraint first. / One phrase in the question usually decides the service.


▶ CLICK

Second, / know the Bedrock family. / Guardrails, / Knowledge Bases, / AgentCore, / Prompt Management, / Flows, / and the ways to pay for capacity.


▶ CLICK

And third, / separate the look-alikes. / Macie or Comprehend, / guardrail or prompt, / retrieval or tuning. [pause]

So, / back to our one sentence. [pause] Find the **constraint** in the question first, / and the service usually names itself. [long pause]

Transition: In the next lecture, / we plan your last forty-eight hours, / and walk through exam day itself.
