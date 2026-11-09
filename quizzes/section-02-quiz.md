# Section 2 quiz: GenAI on AWS refresher

10 questions. Aim for 8 or more. Answers and explanations are at the end.

**1.** A support bot built on Amazon Bedrock gives different answers to the same policy question each time it is asked. The team wants consistent, repeatable answers. What should they change first? *(skill 4.2.4)*

- A. Increase maxTokens
- B. Lower the temperature
- C. Switch to Provisioned Throughput
- D. Fine-tune the model on the policy documents

**2.** A developer wants to call several different chat models on Bedrock with the same request code, and switch models by changing only the model ID. Which API should they use? *(skill 1.3.3)*

- A. InvokeModel
- B. Converse
- C. CreateModelInvocationJob
- D. InvokeModelWithResponseStream

**3.** A company must summarize 4 million archived documents. Results are needed by next week, and cost is the top priority. Which Bedrock option fits best?

- A. On-demand inference with ConverseStream
- B. Provisioned Throughput
- C. Batch inference
- D. Cross-Region inference

**4.** An application has steady, high request volume around the clock and is being throttled on on-demand quotas. It needs guaranteed capacity. What should the team use?

- A. Batch inference
- B. Provisioned Throughput
- C. Prompt caching
- D. A larger maxTokens value

**5.** A team needs to deploy an open-weight model that isn't available in Amazon Bedrock, on a specific GPU instance type, with a custom inference container. Which service should they use?

- A. Amazon Bedrock on-demand
- B. Amazon SageMaker AI endpoint, with JumpStart if the model is in its catalog
- C. Amazon Bedrock Knowledge Bases
- D. AWS Lambda

**6.** An HR assistant must answer from policy documents that change weekly, and every answer must cite the source document. Which pattern fits best with the least effort?

- A. Fine-tune the model weekly
- B. Train a model from scratch
- C. Retrieval augmented generation
- D. Increase the context window

**7.** A marketing team wants every response to follow the company's brand voice and a fixed structure. Detailed prompts have not held the style reliably across thousands of outputs. Which approach should they try next?

- A. RAG over past marketing copy
- B. Fine-tuning on approved examples
- C. Raising the temperature
- D. Batch inference

**8.** Which TWO statements about tokens and context windows are true? (Select TWO.)

- A. The context window limits the prompt only; the response is unlimited.
- B. On-demand pricing is based on input and output tokens.
- C. Retrieved documents and conversation history count toward the context window.
- D. Every model on Bedrock uses the same tokenizer.
- E. Tokens are always whole words.

**9.** A team is building a custom agent in Python with its own tools, and wants a managed service to host it with session isolation and to give it long-term memory. Which combination fits?

- A. Strands Agents, deployed on Amazon Bedrock AgentCore Runtime with AgentCore Memory
- B. Amazon SageMaker JumpStart and Amazon S3
- C. Bedrock batch inference and Amazon DynamoDB
- D. An MCP server only

**10.** Several teams' agents need to share the same set of internal tools through one standard interface. What should the platform team build?

- A. A fine-tuned model per team
- B. A Model Context Protocol (MCP) server that exposes the tools
- C. A Bedrock batch inference job
- D. A Provisioned Throughput commitment

---

## Answers

1. **B.** Temperature controls randomness. Lower it for repeatable answers. A changes length, C changes capacity, and D is far more effort than the problem needs.
2. **B.** Converse gives one request shape across chat models. InvokeModel needs each model's native body.
3. **C.** Batch inference is discounted and suits large jobs that don't need real-time results.
4. **B.** Provisioned Throughput gives dedicated capacity for steady, high volume.
5. **B.** A model outside Bedrock plus control of hardware and container points to a SageMaker AI endpoint.
6. **C.** RAG handles changing data by re-indexing and can return sources. Fine-tuning would need retraining each week and gives no citations.
7. **B.** Tone and structure are a behavior problem, which fine-tuning addresses once prompting has been tried.
8. **B, C.** The window holds prompt, history, retrieved context and the response; tokenizers differ by model; tokens can be parts of words.
9. **A.** Strands builds the agent, AgentCore Runtime hosts it with session isolation, and AgentCore Memory keeps long-term context.
10. **B.** MCP is the open standard for exposing tools so any MCP-aware agent can use them.
