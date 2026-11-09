# AIP-C01 course, version 2 (under 10 hours of video)

This folder holds the shorter course that follows `docs/course-outline-10h.md`.

- `slides/` has one animated PowerPoint per lecture (`lecture-X.Y.pptx`) and its narration script (`lecture-X.Y-script.md`). Content builds on each click, and every `▶ CLICK` in the script matches one build step.
- `labs/` has the demo code and the optional written labs.

Each lecture ends with a short recap, not a knowledge check. Quizzes and practice exams are separate.

## Status

| Section | Lecture | Status |
|---|---|---|
| 1. Welcome and exam strategy | 1.1 How this course and the exam fit together | Draft for review |
| | 1.2 The exam: format, scoring and reading the questions | Draft for review |
| | 1.3 Setting up your AWS account safely | Draft for review |
| 2. GenAI on AWS essentials | 2.1 Models, tokens and inference parameters | Draft for review |
| | 2.2 Amazon Bedrock, its APIs and pricing | Draft for review |
| | 2.3 The four architecture patterns | Draft for review |
| | 2.4 Demo: your first Bedrock call (lab: `labs/lab-2.4-first-bedrock-call`) | Draft for review |
| 3. Designing solutions and choosing models | 3.1 From requirements to a reviewed architecture | Draft for review |
| | 3.2 Evaluating and choosing foundation models | Draft for review |
| | 3.3 Switching models without code changes | Draft for review |
| | 3.4 Designing for resilience | Draft for review |
| | 3.5 Customizing models and managing their lifecycle | Draft for review |
| | 3.6 Demo: a model router with AppConfig (lab: `labs/lab-3.6-model-router`) | Draft for review |
| 4. Data pipelines and vector stores | 4.1 Data quality and multimodal pipelines | Draft for review |
| | 4.2 Formatting and improving inputs | Draft for review |
| | 4.3 Choosing a vector store | Draft for review |
| | 4.4 Metadata, scaling and keeping vectors fresh | Draft for review |
| | 4.5 Demo: a Knowledge Base with an S3 source and incremental sync (lab: `labs/lab-4.5-knowledge-base`) | Draft for review |
| 5. Retrieval for RAG | 5.1 Chunking strategies and choosing embeddings | Draft for review |
| | 5.2 Vector search, hybrid search and reranking | Draft for review |
| | 5.3 Query expansion, decomposition and consistent retrieval | Draft for review |
| | 5.4 Demo: tuning chunking and adding a reranker (lab: `labs/lab-5.4-chunking-and-reranking`) | Draft for review |
| 6. Prompt engineering and governance | 6.1 Instruction frameworks, Prompt Management and conversation context | Draft for review |
| | 6.2 Prompt governance and QA | Draft for review |
| | 6.3 Advanced techniques and Prompt Flows | Draft for review |
| | 6.4 Demo: a versioned prompt in a Prompt Flow (lab: `labs/lab-6.4-prompt-flow`) | Draft for review |
| 7. Agents and tools | 7.1 What makes an agent, and multi-agent systems | Draft for review |
| | 7.2 Orchestration and safeguards | Draft for review |
| | 7.3 Model coordination and human in the loop | Draft for review |
| | 7.4 Tool design and MCP servers | Draft for review |
| | 7.5 Demo: a Strands agent with an MCP tool (lab: `labs/lab-7.5-strands-mcp-agent`) | Draft for review |
| 8. Deployment and enterprise integration | 8.1 Hosting choices and right-sizing | Draft for review |
| | 8.2 Integrating with legacy systems and microservices | Draft for review |
| | 8.3 Secure access, data residency and hybrid | Draft for review |
| | 8.4 CI/CD for GenAI and the GenAI gateway | Draft for review |
| 9. FM APIs and application patterns | 9.1 Sync, async and streaming invocation | Draft for review |
| | 9.2 Resilience and model routing | Draft for review |
| | 9.3 Front ends and business integrations | Draft for review |
| | 9.4 Developer tools and troubleshooting | Draft for review |
| | 9.5 Demo: streaming chat with retries (lab: `labs/lab-9.5-streaming-chat`) | Draft for review |
| 10. Safety controls | 10.1 Bedrock Guardrails in depth | Draft for review |
| | 10.2 Reducing hallucinations and structured outputs | Draft for review |
| | 10.3 Defense in depth and adversarial threats | Draft for review |
| | 10.4 Demo: a guardrail that blocks injection and masks PII (lab: `labs/lab-10.4-guardrail`) | Draft for review |
| 11. Security, privacy, governance and responsible AI | 11.1 Locking down FM workloads | Draft for review |
| | 11.2 Protecting PII | Draft for review |
| | 11.3 Governance and compliance | Draft for review |
| | 11.4 Responsible AI | Draft for review |
| | 11.5 How the controls fit together | Draft for review |
| 12. Cost, performance and monitoring | 12.1 Token economics and caching | Draft for review |
| | 12.2 Latency, throughput and parameter tuning | Draft for review |
| | 12.3 Observability for GenAI | Draft for review |
| | 12.4 Demo: a CloudWatch dashboard for tokens, latency and cost (lab: `labs/lab-12.4-genai-dashboard`) | Draft for review |
| 13. Evaluation and troubleshooting | 13.1 Evaluation metrics and Bedrock evaluations | Draft for review |
| | 13.2 Evaluating RAG and agents, and quality gates | Draft for review |
| | 13.3 Troubleshooting GenAI applications | Draft for review |
| | 13.4 Reporting quality to stakeholders | Draft for review |
| 14. Final review and exam day | 14.1 The "Which service?" drill | Draft for review |
| | 14.2 The last 48 hours and exam day | Draft for review |
