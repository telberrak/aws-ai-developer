# Section 3 quiz: Designing GenAI solutions

10 questions. Aim for 8 or more. Answers and explanations are at the end.

**1.** A company wants an assistant that answers employee questions from 5,000 internal policy documents. Answers must include the source document. The team wants the least operational overhead. Which design should they choose?

- A. Fine-tune a model on the policy documents
- B. A Bedrock knowledge base over the documents in Amazon S3, returning citations
- C. A self-managed vector database on Amazon EC2 with custom retrieval code
- D. Add all policy documents to the system prompt

**2.** In a scenario, which phrase most often decides between two designs that both work?

- A. The name of the company
- B. The functional requirement, such as "answer questions"
- C. A quality constraint, such as "with the least operational overhead" or "keep data in the VPC"
- D. The number of developers on the team

**3.** A team is planning a proof of concept for a GenAI document summarizer. What should they do FIRST?

- A. Buy Provisioned Throughput
- B. Agree measurable targets for quality, latency and cost
- C. Fine-tune a model
- D. Deploy to production in one Region

**4.** A PoC was tested on 12 clean, hand-picked documents and every summary looked good. What is the biggest weakness of this PoC?

- A. It used Amazon Bedrock
- B. The test data isn't representative, and there were no agreed targets
- C. It didn't use a SageMaker AI endpoint
- D. It used the Converse API

**5.** A PoC costs $0.02 per request. Production traffic will be 2 million requests per day. Roughly what is the daily model cost?

- A. $400
- B. $4,000
- C. $40,000
- D. $400,000

**6.** Which TWO measurements belong in a GenAI PoC? (Select TWO.)

- A. Time to first token measured from the client
- B. The number of AWS Regions in the world
- C. Answer quality scored against a test set with expected answers
- D. The size of the development team
- E. The number of lines of code

**7.** A company wants to check a new GenAI workload against AWS best practices, find high-risk issues and track improvements over time. What should they use?

- A. AWS Trusted Advisor
- B. The AWS Well-Architected Tool with the Generative AI Lens applied
- C. Amazon Inspector
- D. AWS Config rules

**8.** Twelve teams are building GenAI apps. Each team writes its own IAM policies, prompts and content filters, and security reviews keep finding the same gaps. What is the BEST long-term fix?

- A. Ask each team to read the AWS documentation
- B. Provide standardized components: shared IaC constructs, versioned prompts in Bedrock Prompt Management, and a shared Guardrails configuration
- C. Move every team to SageMaker AI
- D. Use one large model for all teams

**9.** A public chatbot design has a Lambda function with `bedrock:*` on all resources. Which Well-Architected pillar does this weaken MOST?

- A. Sustainability
- B. Performance efficiency
- C. Security
- D. Cost optimization

**10.** A retailer needs to generate 2 million product descriptions in its brand voice over the next week. A person must approve the descriptions before they are published. Which design fits best?

- A. A streaming chatbot with ConverseStream
- B. Prompt templates, Bedrock batch inference, and a human review step
- C. An agent with tools on AgentCore Runtime
- D. Provisioned Throughput with real-time calls from the website

---

## Answers

1. **B.** Managed RAG with citations meets every requirement with the least overhead. A gives no sources and is stale between training runs, C works but has the most overhead, and D exceeds context limits.
2. **C.** Quality constraints usually separate working answers.
3. **B.** Without agreed targets, a PoC can't prove anything.
4. **B.** Hand-picked data and no targets make the result unreliable.
5. **C.** $0.02 × 2,000,000 = $40,000 per day. This is why you estimate cost at scale.
6. **A, C.** Latency from the client and quality against a test set are core PoC measures.
7. **B.** The WA Tool runs lens reviews, reports high and medium risks, and tracks milestones.
8. **B.** Shared, standardized components make every implementation consistent.
9. **C.** Wildcard permissions break least privilege.
10. **B.** Large offline volume points to batch inference, a consistent voice to templates, and approval to human review.
