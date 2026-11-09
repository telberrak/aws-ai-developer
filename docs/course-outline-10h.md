# AIP-C01 course: 10-hour outline (proposal)

Proposal for review, 9 November 2026. Every task in the AIP-C01 exam guide is still covered. The original 35-hour plan is in `course-blueprint.md` and is unchanged until this proposal is approved.

## The budget

- **Video total:** 9 h 50 min, leaving 10 minutes of headroom under the 10-hour cap.
- **Time per domain:** follows the exam weight. Domains 1 and 2 are 57% of the exam and get about 5 h 40 min of the content time.
- **How the cut is made:**
  - Lectures last 6 to 10 minutes and each one covers a whole task, not a single skill.
  - The 23 hands-on labs become **8 short demo lectures** (in the times below). The other labs stay in the repo as optional written guides, with no video.
  - The capstone build and the rapid service review become downloadable guides. The final section keeps a 20-minute cram.
- **Not counted as video:** the 4 practice exams, the 5 checkpoint quizzes and the diagnostic test all stay.

| Domain | Exam weight | Old plan | New plan | New sections |
|---|---|---|---|---|
| Getting ready | | 2 h 15 min | 50 min | 1, 2 |
| 1. FM integration, data and compliance | 31% | 9 h 30 min | 3 h 10 min | 3 to 6 |
| 2. Implementation and integration | 26% | 8 h | 2 h 30 min | 7 to 9 |
| 3. AI safety, security and governance | 20% | 5 h 30 min | 1 h 40 min | 10, 11 |
| 4. Operational efficiency | 12% | 3 h 30 min | 55 min | 12 |
| 5. Testing, validation, troubleshooting | 11% | 3 h | 45 min | 13 |
| Wrap-up | | 3 h 30 min | 20 min | 14 |
| **Total** | | **35 h** | **9 h 50 min** | **14 sections** |

## Curriculum

### Part 0: Getting ready (50 min)

**Section 1: Welcome and exam strategy (20 min)**
1. How the course and the exam fit together, and the 6-week plan (5 min)
2. Exam format, scoring and how to read scenario questions (10 min)
3. Account setup, budgets and Bedrock model access (5 min)

Then the diagnostic test (30 questions, no video).

**Section 2: GenAI on AWS essentials (30 min)**
1. FMs, tokens, context windows and inference parameters (8 min)
2. Bedrock, its APIs and pricing options, and when SageMaker AI fits instead (10 min)
3. The four architecture patterns: prompt only, RAG, agents, fine-tuning (6 min)
4. Demo: first Bedrock call with the Converse API (6 min)

### Part 1: Domain 1, FM integration, data management and compliance (3 h 10 min)

**Section 3: Designing solutions and choosing models (55 min)** covers Tasks 1.1 and 1.2
1. Requirements to architecture, proof of concept, and the Well-Architected Generative AI Lens (12 min)
2. Evaluating and choosing FMs (8 min)
3. Switching models without code changes with AppConfig (7 min)
4. Resilience: circuit breakers, cross-Region inference and graceful degradation (8 min)
5. Customizing models and managing their lifecycle (10 min)
6. Demo: model router with AppConfig (10 min)

**Section 4: Data pipelines and vector stores (50 min)** covers Tasks 1.3 and 1.4
1. Data quality and multimodal pipelines: Glue Data Quality, Transcribe, Bedrock Data Automation (10 min)
2. Formatting and improving inputs: request formats, Comprehend, Lambda normalization (7 min)
3. Vector store options compared: Knowledge Bases, OpenSearch, Aurora pgvector, DynamoDB metadata (10 min)
4. Metadata, scaling, source connectors and keeping vectors fresh (10 min)
5. Demo: Knowledge Base with an S3 source and incremental sync (13 min)

**Section 5: Retrieval for RAG (45 min)** covers Task 1.5
1. Chunking strategies and choosing embeddings (10 min)
2. Vector search, hybrid search and reranking (10 min)
3. Query expansion, decomposition and consistent retrieval access with function calling and MCP (10 min)
4. Demo: tuning chunking and adding a reranker (15 min)

**Section 6: Prompt engineering and governance (40 min)** covers Task 1.6
1. Instruction frameworks, Prompt Management and conversation context (10 min)
2. Prompt governance and QA: versions, approvals, logging, regression tests (10 min)
3. Advanced techniques and Prompt Flows (10 min)
4. Demo: versioned prompt with a Prompt Flow (10 min)

Then the Domain 1 checkpoint (25 questions, no video).

### Part 2: Domain 2, implementation and integration (2 h 30 min)

**Section 7: Agents and tools (55 min)** covers Task 2.1
1. What makes an agent, and multi-agent systems with Strands, Agent Squad and AgentCore (12 min)
2. Orchestration and safeguards: ReAct with Step Functions, stopping conditions, IAM boundaries (10 min)
3. Model coordination and human in the loop with Augmented AI (8 min)
4. Tool design and MCP servers on Lambda and ECS (10 min)
5. Demo: a Strands agent with an MCP tool (15 min)

**Section 8: Deployment and enterprise integration (45 min)** covers Tasks 2.2 and 2.3
1. Hosting choices, why LLM hosting differs, and right-sizing (12 min)
2. Integrating with legacy systems and microservices: events, API Gateway, EventBridge (10 min)
3. Secure access, data residency and hybrid: Identity Center, Cognito, Outposts, Wavelength (12 min)
4. CI/CD for GenAI and the GenAI gateway pattern (11 min)

**Section 9: FM APIs and application patterns (50 min)** covers Tasks 2.4 and 2.5
1. Sync and async invocation, and streaming with ConverseStream and WebSockets (10 min)
2. Resilience and model routing: backoff, throttling, intelligent prompt routing (10 min)
3. Front ends and business integrations: Amplify, OpenAPI, CRM, document processing (8 min)
4. Developer tools and troubleshooting: Q Developer, Kiro, Logs Insights, X-Ray (10 min)
5. Demo: streaming chat with retries (12 min)

Then the Domain 2 checkpoint (25 questions, no video).

### Part 3: Domain 3, AI safety, security and governance (1 h 40 min)

**Section 10: Safety controls (45 min)** covers Task 3.1
1. Bedrock Guardrails in depth, including contextual grounding and automated reasoning checks (12 min)
2. Reducing hallucinations and structured outputs (8 min)
3. Defense in depth and adversarial threats: prompt injection, jailbreaks, red-teaming (12 min)
4. Demo: a guardrail that blocks injection and masks PII (13 min)

**Section 11: Security, privacy, governance and responsible AI (55 min)** covers Tasks 3.2, 3.3 and 3.4
1. Locking down FM workloads: PrivateLink, IAM, Lake Formation, KMS, CloudTrail (12 min)
2. PII: Comprehend versus Macie, masking and tokenization, retention (10 min)
3. Governance and compliance: model cards, lineage, traceability, continuous monitoring (15 min)
4. Responsible AI: transparency, fairness with Clarify and LLM-as-a-judge, policy compliance (12 min)
5. Recap of how the controls fit together (6 min)

Then the Domain 3 checkpoint (20 questions, no video).

### Part 4: Domain 4, operational efficiency and optimization (55 min)

**Section 12: Cost, performance and monitoring (55 min)** covers Tasks 4.1, 4.2 and 4.3
1. Token economics, tiered models and caching, including prompt caching and semantic caching (12 min)
2. Latency, throughput and inference parameter tuning (12 min)
3. Observability: GenAI KPIs in CloudWatch, invocation logs, agent and vector store monitoring (13 min)
4. Demo: a CloudWatch dashboard for token use, latency and cost (18 min)

### Part 5: Domain 5, testing, validation and troubleshooting (45 min)

**Section 13: Evaluation and troubleshooting (45 min)** covers Tasks 5.1 and 5.2
1. Evaluation metrics and Bedrock Model Evaluations, including LLM-as-a-judge (12 min)
2. RAG and agent evaluation, quality gates and deployment validation (12 min)
3. Troubleshooting: context overflow, API errors, prompt and retrieval problems (13 min)
4. Reporting quality to stakeholders (8 min)

Then the Domains 4 and 5 checkpoint (20 questions, no video).

### Part 6: Final review (20 min)

**Section 14: Final review and exam day (20 min)**
1. "Which service?" drill on the most-tested Bedrock features (12 min)
2. The last-48-hours plan and exam-day tactics (8 min)

Then the 4 practice exams (75 questions each, no video). The capstone and full service review ship as downloadable guides.

## What happens to the work already done

The four sections already built hold about 2 h 20 min of narration. In the new plan they fit into 1 h 45 min (Sections 1 to 3).

- **Old Section 1:** becomes new Section 1. Cut from 24 slides to about 12.
- **Old Section 2:** becomes new Section 2. Cut from 22 slides to about 14. Lab 0 becomes the demo.
- **Old Sections 3 and 4:** merge into new Section 3. Cut from 48 slides to about 30. Lab 2 becomes the demo. Lab 1 (lens review) and Lab 3 (circuit breaker) stay as written guides.

All four quizzes stay as they are.

## Exam guide coverage check

| Task | New section |
|---|---|
| 1.1 Analyze requirements and design solutions | 3 |
| 1.2 Select and configure FMs | 3 |
| 1.3 Data validation and processing pipelines | 4 |
| 1.4 Vector store solutions | 4 |
| 1.5 Retrieval mechanisms | 5 |
| 1.6 Prompt engineering and governance | 6 |
| 2.1 Agentic AI and tool integrations | 7 |
| 2.2 Model deployment strategies | 8 |
| 2.3 Enterprise integration architectures | 8 |
| 2.4 FM API integrations | 9 |
| 2.5 Application integration patterns and dev tools | 9 |
| 3.1 Input and output safety controls | 10 |
| 3.2 Data security and privacy | 11 |
| 3.3 AI governance and compliance | 11 |
| 3.4 Responsible AI principles | 11 |
| 4.1 Cost optimization | 12 |
| 4.2 Application performance | 12 |
| 4.3 Monitoring | 12 |
| 5.1 Evaluation systems | 13 |
| 5.2 Troubleshooting | 13 |

All 20 tasks in the exam guide are covered.
