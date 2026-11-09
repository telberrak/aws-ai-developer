# AWS AI Professional Certification: Udemy Course Blueprint

Exported from the course blueprint doc: https://claude.ai/code/artifact/8586db2d-eaa4-4889-b4d1-5d82ec6199df (Oct 15, 2026). The doc is the live version.

## Course overview

A 26-section, roughly 35-hour course that walks every one of the 20 task statements and 98 skills in the AIP-C01 exam guide, with study time split in proportion to each domain's weighting.

**Working title:** AWS Certified Generative AI Developer - Professional (AIP-C01): Complete Course + 4 Practice Exams

**Subtitle:** Build production RAG, agents, guardrails and evaluation pipelines on Amazon Bedrock, then pass AIP-C01 on your first attempt.

**Who it is for:** developers with about 2 years building on AWS and some hands-on GenAI work, which is the exam's stated target candidate. Data scientists who want to ship GenAI to production also fit.

**Prerequisites the course assumes, not teaches:** AWS compute, storage and networking basics; IAM fundamentals; one IaC tool (CDK or CloudFormation); Python. A refresher section covers the minimum for anyone rusty.

**Out of scope, so not taught:** model training from scratch, advanced ML techniques, data and feature engineering. The exam guide excludes all three.

**Format and assets:**

- About 35 hours of video: concept lectures (5 to 12 minutes), architecture whiteboards and console or code demos
- 23 hands-on labs (Lab 0 to Lab 22), all in Python with AWS CDK, published in this repo with a cost estimate and teardown script per lab
- One end-of-section quiz per section (10 to 15 questions), written in the exam's multiple-choice and multiple-response styles
- 4 full practice exams of 75 questions each, timed at 180 minutes, plus one 30-question diagnostic
- Downloadable cheat sheets: service picker, Bedrock API quick reference, "which service for which keyword" table
- A capstone project that ties all five domains together

**Learning outcomes (from the exam guide's task list):** design RAG and vector store solutions; integrate FMs into applications and workflows; apply prompt engineering and prompt governance; build agentic AI; optimize cost, latency and throughput; implement security, governance and responsible AI; monitor and troubleshoot GenAI apps; evaluate FMs for quality and responsibility.

## Exam at a glance

AIP-C01 has 65 scored plus 10 unscored questions, a pass mark of 750 on a 100 to 1,000 scale, and compensatory scoring, so you only need to pass overall, not each domain.

| Domain | Exam weight | Approx. scored questions | Course hours | Course sections |
| --- | --- | --- | --- | --- |
| 1. FM Integration, Data Management, and Compliance | 31% | 20 | 9.5 h | 3 to 8 |
| 2. Implementation and Integration | 26% | 17 | 8 h | 9 to 13 |
| 3. AI Safety, Security, and Governance | 20% | 13 | 5.5 h | 14 to 17 |
| 4. Operational Efficiency and Optimization | 12% | 8 | 3.5 h | 18 to 20 |
| 5. Testing, Validation, and Troubleshooting | 11% | 7 | 3 h | 21 to 22 |
| Foundations, capstone, review | – | – | 5.75 h | 1, 2, 23 to 26 |

**Question types:** multiple choice (1 correct of 4) and multiple response (2 or more correct of 5 or more, all must be selected). No penalty for guessing, so never leave a question blank.

**Exam technique taught in Section 1:** spot the constraint word ("least operational overhead", "most cost-effective", "lowest latency", "without code changes"), eliminate options that break any constraint, and prefer managed Bedrock features over custom builds unless the question rules them out.

**Service scope:** the course demos only in-scope services. Amazon Bedrock (including AgentCore, Knowledge Bases, Prompt Management, Prompt Flows, Guardrails), SageMaker AI, OpenSearch Service, Step Functions, Lambda, API Gateway, CloudWatch and IAM carry most of the content. Out-of-scope look-alikes (for example Amazon Redshift, AWS Budgets, Amazon DevOps Guru) appear only as "don't design with these" drills.

## Course curriculum

Each section maps to one exam task statement; skill IDs in brackets point to the exam guide so every skill is covered at least once. Every section ends with a quiz in exam format.

### Part 0: Getting ready

#### Section 1: Welcome and exam strategy (45 min)

Slides: [slides/section-01-welcome-and-exam-strategy.pptx](../slides/section-01-welcome-and-exam-strategy.pptx) · Script: [slides/section-01-script.md](../slides/section-01-script.md)

1. How this course maps to AIP-C01 and how to use it
2. Exam format, scoring, 750 pass mark and compensatory scoring
3. Reading professional-level scenarios: constraint words and distractors
4. In-scope versus out-of-scope services: the shortlist that matters
5. Setting up your AWS account, Bedrock model access, budgets and the course repo
6. Diagnostic test: 30 questions across all 5 domains (find your weak domain first)

#### Section 2: GenAI on AWS refresher (1.5 h)

1. FMs, tokens, context windows and inference parameters in plain terms
2. Amazon Bedrock tour: model catalog, Converse API, InvokeModel, on-demand versus provisioned
3. SageMaker AI and JumpStart: when you need them instead of Bedrock
4. The core architecture patterns: prompt-only, RAG, agents, fine-tuned models
5. Bedrock AgentCore, Strands Agents and MCP in one picture

- **Lab 0:** First Bedrock call with boto3 using the Converse API, then the same call through the AWS CLI
- **Quiz:** 10 questions

Slides: [slides/section-02-genai-on-aws-refresher.pptx](../slides/section-02-genai-on-aws-refresher.pptx) · Script: [slides/section-02-script.md](../slides/section-02-script.md) · Lab: [labs/lab-00-first-bedrock-call](../labs/lab-00-first-bedrock-call/README.md) · Quiz: [quizzes/section-02-quiz.md](../quizzes/section-02-quiz.md)

### Part 1: Domain 1, Foundation Model Integration, Data Management, and Compliance (31%)

#### Section 3: Analyze requirements and design GenAI solutions, Task 1.1 (1 h)

1. Turning business requirements into a GenAI architecture: choosing FM, integration pattern, deployment [1.1.1]
2. Building a proof of concept on Bedrock that proves feasibility, latency and business value [1.1.2]
3. The Well-Architected Generative AI Lens and the WA Tool for standard components [1.1.3]
4. Architecture case studies: chatbot, document Q&A, content generation, agentic workflow

- **Lab 1:** Run a Generative AI Lens review in the Well-Architected Tool against a sample design
- **Quiz:** 10 questions

Slides: [slides/section-03-designing-genai-solutions.pptx](../slides/section-03-designing-genai-solutions.pptx) · Script: [slides/section-03-script.md](../slides/section-03-script.md) · Lab: [labs/lab-01-genai-lens-review](../labs/lab-01-genai-lens-review/README.md) · Quiz: [quizzes/section-03-quiz.md](../quizzes/section-03-quiz.md)

#### Section 4: Select and configure FMs, Task 1.2 (2 h)

1. Evaluating FMs: benchmarks, capabilities, context length, modality, limits, price [1.2.1]
2. Provider-agnostic model abstraction with Lambda, API Gateway and AWS AppConfig for model switching without code changes [1.2.2]
3. Resilience: Step Functions circuit breakers, Bedrock cross-Region inference, graceful degradation [1.2.3]
4. Customizing FMs: fine-tuning versus continued pre-training versus LoRA and adapters [1.2.4]
5. SageMaker Model Registry, automated deployment pipelines, rollback and model retirement [1.2.4]

- **Lab 2:** Build a model router whose target model lives in AppConfig, then switch models live with zero redeploys
- **Lab 3:** Add a Step Functions circuit breaker that fails over to a cross-Region inference profile
- **Quiz:** 12 questions

Slides: [slides/section-04-selecting-and-configuring-fms.pptx](../slides/section-04-selecting-and-configuring-fms.pptx) · Script: [slides/section-04-script.md](../slides/section-04-script.md) · Labs: [lab-02-model-router](../labs/lab-02-model-router/README.md), [lab-03-circuit-breaker](../labs/lab-03-circuit-breaker/README.md) · Quiz: [quizzes/section-04-quiz.md](../quizzes/section-04-quiz.md)

#### Section 5: Data validation and processing pipelines, Task 1.3 (1.5 h)

1. Data quality for FM consumption: Glue Data Quality, Data Wrangler, Lambda checks, CloudWatch metrics [1.3.1]
2. Multimodal pipelines: text, image, audio (Transcribe), tabular, SageMaker Processing, Bedrock Data Automation [1.3.2]
3. Formatting inputs per model: Bedrock request JSON, SageMaker payloads, conversation turns [1.3.3]
4. Improving input quality: Bedrock reformatting, Comprehend entity extraction, Lambda normalization [1.3.4]

- **Lab 4:** Audio-to-insight pipeline: S3 upload, Transcribe, Comprehend entities, Bedrock summary
- **Quiz:** 10 questions

#### Section 6: Vector store solutions, Task 1.4 (1.5 h)

1. Vector store options compared: Bedrock Knowledge Bases, OpenSearch Service (Neural plugin), Aurora pgvector, RDS with S3, DynamoDB for metadata [1.4.1]
2. Metadata frameworks: S3 object metadata, custom attributes, tagging for domain classification and filtering [1.4.2]
3. Scaling vector search: OpenSearch sharding, multi-index design, hierarchical indexes [1.4.3]
4. Connecting sources: data source connectors for wikis, document management systems, S3, web crawlers [1.4.4]
5. Keeping vectors fresh: incremental sync, change detection with EventBridge, scheduled refresh [1.4.5]

- **Lab 5:** Create a Bedrock Knowledge Base on OpenSearch Serverless with metadata filtering and an EventBridge-triggered incremental sync
- **Quiz:** 12 questions

#### Section 7: Retrieval mechanisms for FM augmentation, Task 1.5 (2 h)

1. Chunking strategies: fixed-size, hierarchical, semantic, custom Lambda chunking [1.5.1]
2. Choosing embeddings: Titan versus other Bedrock embedding models, dimensions, batch embedding with Lambda [1.5.2]
3. Deploying vector search: OpenSearch k-NN, Aurora pgvector, managed Knowledge Base stores [1.5.3]
4. Better relevance: hybrid search, Bedrock reranker models [1.5.4]
5. Query handling: query expansion, decomposition with Lambda, transformation with Step Functions [1.5.5]
6. Consistent retrieval access: function calling, MCP clients for vector queries, standard retrieval APIs [1.5.6]

- **Lab 6:** Compare fixed, hierarchical and semantic chunking on the same corpus and measure retrieval hit rate
- **Lab 7:** Add hybrid search plus a reranker and see the before-and-after answers
- **Quiz:** 15 questions

#### Section 8: Prompt engineering and governance, Task 1.6 (1.5 h)

1. Instruction frameworks: system prompts, roles, Bedrock Prompt Management, response templates [1.6.1]
2. Conversational context: DynamoDB conversation history, Comprehend intent, Step Functions clarification loops [1.6.2]
3. Prompt governance: parameterized templates, versions and approvals, S3 template repos, CloudTrail and CloudWatch Logs [1.6.3]
4. Prompt QA: Lambda output checks, Step Functions edge-case tests, CloudWatch regression tracking [1.6.4]
5. Advanced techniques: structured inputs, output schemas, chain-of-thought, feedback loops [1.6.5]
6. Bedrock Prompt Flows: chains, conditional branches, reusable components, pre and post processing [1.6.6]

- **Lab 8:** Version a prompt in Prompt Management and wire it into a Prompt Flow with a conditional branch
- **Quiz:** 12 questions

**Domain 1 checkpoint:** 25-question mini exam, timed at 60 minutes.

### Part 2: Domain 2, Implementation and Integration (26%)

#### Section 9: Agentic AI and tool integrations, Task 2.1 (2.5 h)

1. What makes an agent: reasoning loop, memory, state, tools
2. Multi-agent systems with Strands Agents and AWS Agent Squad; Bedrock AgentCore runtime and memory [2.1.1]
3. ReAct and chain-of-thought orchestration with Step Functions [2.1.2]
4. Safeguarded agents: stopping conditions, Lambda timeouts, IAM resource boundaries, circuit breakers [2.1.3]
5. Model coordination: specialist FMs, ensembles with custom aggregation, model selection frameworks [2.1.4]
6. Human in the loop: Step Functions approval steps, API Gateway feedback, Amazon Augmented AI [2.1.5]
7. Tool design: Strands custom behaviors, standard function definitions, Lambda parameter validation and error handling [2.1.6]
8. MCP in practice: stateless MCP servers on Lambda, complex MCP servers on ECS, MCP client libraries [2.1.7]

- **Lab 9:** Build a Strands agent with two tools, then expose one tool as an MCP server on Lambda
- **Lab 10:** Multi-agent support desk with a supervisor agent and a Step Functions human approval step
- **Quiz:** 15 questions

#### Section 10: Model deployment strategies, Task 2.2 (1.25 h)

1. Picking the hosting model: Bedrock on-demand, provisioned throughput, SageMaker AI endpoints, hybrids [2.2.1]
2. Why LLM hosting differs: GPU memory, model loading, token throughput, LMI containers [2.2.2]
3. Right-sizing: smaller task-specific models and API-based model cascading [2.2.3]

- **Lab 11:** Deploy a JumpStart open-weight model to a SageMaker endpoint and cascade to Bedrock for hard queries
- **Quiz:** 10 questions

#### Section 11: Enterprise integration architectures, Task 2.3 (1.5 h)

1. Bringing FMs to legacy systems: API integrations, event-driven loose coupling, data sync patterns [2.3.1]
2. Microservice integration with API Gateway, Lambda webhooks and EventBridge [2.3.2]
3. Secure access: identity federation, IAM Identity Center, Cognito, RBAC, least-privilege Bedrock policies [2.3.3]
4. Data residency and hybrid: AWS Outposts, AWS Wavelength, secure cloud-to-on-premises routing [2.3.4]
5. CI/CD for GenAI with CodePipeline and CodeBuild, security scans, rollback; the GenAI gateway pattern [2.3.5]

- **Lab 12:** CodePipeline that deploys a prompt and Lambda change, runs automated prompt tests, and rolls back on failure
- **Quiz:** 12 questions

#### Section 12: FM API integrations, Task 2.4 (1.5 h)

1. Sync and async invocation: Bedrock APIs, SDKs, SQS-buffered processing, API Gateway request validation [2.4.1]
2. Real-time UX: ConverseStream, WebSockets, server-sent events, chunked transfer [2.4.2]
3. Resilience: SDK exponential backoff and jitter, throttling and rate limits, fallbacks, X-Ray tracing [2.4.3]
4. Model routing: static config, content-based routing with Step Functions, metric-driven routing, Bedrock intelligent prompt routing [2.4.4]

- **Lab 13:** Streaming chat over an API Gateway WebSocket API with retries and an SQS async path
- **Quiz:** 12 questions

#### Section 13: Application integration patterns and dev tools, Task 2.5 (1.25 h)

1. GenAI-specific API concerns: streaming, token limits, timeout retries [2.5.1]
2. Accessible interfaces: Amplify UI components, OpenAPI-first design, Prompt Flows as no-code builder [2.5.2]
3. Business enhancements: CRM with Lambda, document processing with Step Functions and Bedrock Data Automation [2.5.3]
4. Developer productivity with Amazon Q Developer and Kiro [2.5.4]
5. Advanced orchestration: Strands, Agent Squad, Step Functions agent patterns, prompt chaining [2.5.5]
6. Troubleshooting toolkit: CloudWatch Logs Insights for prompts, X-Ray for FM calls, Q Developer error analysis [2.5.6]

- **Lab 14:** Intelligent document processing with Bedrock Data Automation and Step Functions
- **Quiz:** 10 questions

**Domain 2 checkpoint:** 25-question mini exam, timed at 60 minutes.

### Part 3: Domain 3, AI Safety, Security, and Governance (20%)

#### Section 14: Input and output safety controls, Task 3.1 (2 h)

1. Bedrock Guardrails deep dive: content filters, denied topics, word filters, sensitive info filters, contextual grounding, automated reasoning checks [3.1.1, 3.1.2]
2. Custom moderation workflows with Step Functions and Lambda; real-time input validation [3.1.1]
3. Safe outputs: FM-based toxicity evaluation, text-to-SQL for deterministic answers [3.1.2]
4. Reducing hallucinations: Knowledge Base grounding, confidence scoring, similarity checks, JSON Schema structured outputs [3.1.3]
5. Defense in depth: Comprehend pre-filters, Guardrails, Lambda post-validation, API Gateway response filtering, AWS WAF [3.1.4]
6. Adversarial threats: prompt injection, jailbreaks, input sanitization, safety classifiers, automated red-teaming [3.1.5]

- **Lab 15:** Build a Guardrail with denied topics, PII masking and contextual grounding, then attack it with a prompt-injection test suite
- **Quiz:** 15 questions

#### Section 15: Data security and privacy controls, Task 3.2 (1.25 h)

1. Locking down FM workloads: VPC endpoints and PrivateLink for Bedrock, IAM data access patterns, Lake Formation, KMS encryption [3.2.1]
2. Monitoring data access with CloudWatch and CloudTrail [3.2.1]
3. Finding PII: Comprehend PII detection versus Amazon Macie for S3 [3.2.2, 3.2.3]
4. Bedrock data privacy guarantees, Guardrails output filtering, S3 Lifecycle retention [3.2.2]
5. Masking, anonymization and tokenization strategies that keep FM utility [3.2.3]

- **Lab 16:** Private RAG: Bedrock through a VPC interface endpoint, KMS-encrypted Knowledge Base, Comprehend PII redaction before indexing
- **Quiz:** 10 questions

#### Section 16: AI governance and compliance, Task 3.3 (1.25 h)

1. Compliance frameworks: SageMaker model cards, Glue lineage, decision logs in CloudWatch Logs [3.3.1]
2. Source traceability: Glue Data Catalog, metadata tags for attribution in generated content, CloudTrail audit [3.3.2]
3. Organizational governance: policies, approval boards, aligning with regulation and responsible AI principles [3.3.3]
4. Continuous governance: misuse and drift detection, bias drift, automated alerting and remediation, token-level redaction, response logging [3.3.4]

- **Lab 17:** Turn on Bedrock model invocation logging, build a CloudWatch alarm for policy violations, and auto-remediate with EventBridge and Lambda
- **Quiz:** 10 questions

#### Section 17: Responsible AI principles, Task 3.4 (1 h)

1. Transparency: reasoning displays, confidence metrics, source citations, Bedrock agent traces [3.4.1]
2. Fairness: fairness metrics, A/B tests with Prompt Management and Prompt Flows, LLM-as-a-judge evaluations, SageMaker Clarify [3.4.2]
3. Policy compliance: Guardrails from policy, model cards for limitations, Lambda compliance checks [3.4.3]

- **Quiz:** 8 questions

**Domain 3 checkpoint:** 20-question mini exam, timed at 45 minutes.

### Part 4: Domain 4, Operational Efficiency and Optimization (12%)

#### Section 18: Cost optimization and resource efficiency, Task 4.1 (1.25 h)

1. Token economics: estimation, tracking, context pruning, prompt compression, max-token limits [4.1.1]
2. Cost-aware model selection: tiered models by query complexity, price-to-performance measurement [4.1.2]
3. Throughput and utilization: batch inference, capacity planning, auto scaling, provisioned throughput sizing [4.1.3]
4. Caching: Bedrock prompt caching, semantic caching with ElastiCache or OpenSearch, request hashing, CloudFront edge caching [4.1.4]

- **Lab 18:** Add prompt caching and a semantic cache, then compare cost and latency in Cost Explorer and CloudWatch
- **Quiz:** 10 questions

#### Section 19: Application performance, Task 4.2 (1.25 h)

1. Latency versus cost: pre-computation, latency-optimized inference, parallel requests, streaming, benchmarking [4.2.1]
2. Faster, better retrieval: index tuning, query preprocessing, hybrid scoring [4.2.2, 4.2.6]
3. Throughput tuning: batch inference jobs, concurrency limits, token processing [4.2.3]
4. Inference parameters: temperature, top-k, top-p, stop sequences by use case; A/B testing changes [4.2.4]
5. Resource allocation for GenAI traffic: token-based capacity planning, auto scaling for bursty prompts [4.2.5]
6. Profiling prompt-completion patterns and efficient service communication [4.2.6]

- **Quiz:** 10 questions

#### Section 20: Monitoring GenAI applications, Task 4.3 (1 h)

1. Holistic observability: operational, trace, FM interaction and business metrics on one dashboard [4.3.1, 4.3.3]
2. GenAI KPIs in CloudWatch: token usage, prompt effectiveness, hallucination rate, anomaly detection, Cost Anomaly Detection, invocation logs [4.3.2]
3. Tool and agent observability: call patterns, multi-agent coordination tracking, baselines [4.3.4]
4. Vector store operations: performance monitoring, index optimization, data quality checks [4.3.5]
5. GenAI-specific failure modes: golden datasets, output diffing, reasoning path tracing [4.3.6]

- **Lab 19:** CloudWatch GenAI dashboard with token, latency and guardrail-intervention metrics plus an anomaly alarm, viewed also in Managed Grafana
- **Quiz:** 10 questions

### Part 5: Domain 5, Testing, Validation, and Troubleshooting (11%)

#### Section 21: Evaluation systems for GenAI, Task 5.1 (1.75 h)

1. Beyond accuracy: relevance, factual accuracy, consistency, fluency [5.1.1]
2. Bedrock Model Evaluations: automatic, human and LLM-as-a-judge jobs; A/B and canary testing; cost-performance analysis [5.1.2, 5.1.5]
3. User-centered evaluation: feedback widgets, ratings, Ground Truth and Augmented AI annotation [5.1.3]
4. Continuous QA: regression suites, automated quality gates in CI/CD [5.1.4]
5. RAG evaluation and retrieval testing: Knowledge Base evaluations, relevance scoring, context match, retrieval latency [5.1.5, 5.1.6]
6. Agent evaluation: task completion rate, tool-use effectiveness, reasoning quality [5.1.7]
7. Reporting to stakeholders with QuickSight dashboards and automated reports [5.1.8]
8. Deployment validation: synthetic user journeys with CloudWatch Synthetics, semantic drift checks [5.1.9]

- **Lab 20:** Run a Bedrock RAG evaluation job with LLM-as-a-judge and use its score as a CodePipeline quality gate
- **Quiz:** 12 questions

#### Section 22: Troubleshooting GenAI applications, Task 5.2 (1.25 h)

1. Content handling: context window overflow, truncation errors, dynamic chunking [5.2.1]
2. API integration errors: throttling, validation exceptions, model access, malformed responses [5.2.2]
3. Prompt problems: testing frameworks, version comparison, systematic refinement [5.2.3, 5.2.5]
4. Retrieval problems: irrelevant chunks, embedding drift, vectorization and chunking fixes [5.2.4]
5. Prompt observability with CloudWatch Logs and X-Ray; schema validation for format drift [5.2.5]

- **Lab 21:** Break-fix lab: diagnose five planted faults in a RAG app (overflow, throttling, bad chunking, prompt confusion, schema drift)
- **Quiz:** 10 questions

**Domains 4 and 5 checkpoint:** 20-question mini exam, timed at 45 minutes.

### Part 6: Bringing it together

#### Section 23: Capstone project (2 h)

Build an enterprise knowledge assistant end to end: Knowledge Base RAG with hybrid search and reranking, a Strands agent with an MCP tool, Guardrails, private networking, prompt caching, a CloudWatch dashboard and an evaluation quality gate in CodePipeline, all deployed with CDK.

- **Lab 22:** Capstone build in 5 guided milestones, one per domain, with teardown at the end

#### Section 24: Rapid service review (1 h)

1. Bedrock family cram: what each feature does and its exam keywords
2. "Which service?" drills: 40 one-line scenarios answered in under 30 seconds each
3. Out-of-scope services and common traps

## Practice exams and final review

Four full-length practice exams, each 75 questions in 180 minutes and weighted like the real exam, with a target of 80% before booking.

#### Section 25: Practice exams

| Exam | Purpose | D1 | D2 | D3 | D4 | D5 | Mode |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Practice Exam 1 | Baseline after finishing the course | 23 | 20 | 15 | 9 | 8 | Timed, explanations after |
| Practice Exam 2 | Targets common traps and multiple-response items | 23 | 20 | 15 | 9 | 8 | Timed, explanations after |
| Practice Exam 3 | Hardest set: long multi-service scenarios | 23 | 20 | 15 | 9 | 8 | Timed, explanations after |
| Practice Exam 4 | Final readiness check | 23 | 20 | 15 | 9 | 8 | Timed, explanations after |

**Question writing rules:**

- About 30% multiple response ("select TWO" or "select THREE"), the rest multiple choice
- Every question tagged to a skill ID, so the results page shows a per-task score, not only per domain
- Every explanation says why each wrong option is wrong, with a link to the lecture and the AWS doc page
- Distractors use real in-scope services in the wrong role

#### Section 26: Final review and exam day (30 min)

1. Reading your practice exam report: turning weak skill IDs into a 3-day revision list
2. The last-48-hours checklist: cheat sheets, rest, no new material
3. Exam-day logistics: online proctoring versus test center, ID, breaks, flagging questions
4. Time management: one pass, then review flagged items
5. After the exam: score report, digital badge, recertification

## Study schedule and production notes

The suggested learner path is 6 weeks at about 8 to 10 hours a week, front-loading Domains 1 and 2 because together they are 57% of the exam.

| Week | Sections | Focus | Milestone |
| --- | --- | --- | --- |
| 1 | 1 to 5 | Setup, refresher, design, FM selection, data pipelines | Diagnostic test done |
| 2 | 6 to 8 | Vector stores, retrieval, prompt engineering | Domain 1 checkpoint at 75% or more |
| 3 | 9 to 13 | Agents, deployment, integration, APIs | Domain 2 checkpoint at 75% or more |
| 4 | 14 to 17 | Safety, security, governance, responsible AI | Domain 3 checkpoint at 75% or more |
| 5 | 18 to 23 | Cost, performance, monitoring, evaluation, troubleshooting, capstone | Capstone deployed |
| 6 | 24 to 26 | Service review and all 4 practice exams | Two practice exams at 80% or more, then book the exam |

**Production notes for the instructor:**

- Record concept lectures first and demos last; Bedrock console screens change often, so keep demo videos short and easy to re-record
- Ship every lab as CDK code with a README, an estimated cost, and a teardown command; warn loudly about provisioned throughput and OpenSearch costs
- Keep a skill coverage matrix (skill ID to lecture, lab, quiz and practice questions) in the repo and check it before each update
- Promo video (2 minutes): the 5 domains, the capstone demo, and the practice exam score report
- Review the course against the AWS exam guide each quarter, since the in-scope service list can change
- The exam guide does not state exam duration or price; confirm both on the AWS Certification site before publishing (the 180-minute practice exam timing is an assumption)
