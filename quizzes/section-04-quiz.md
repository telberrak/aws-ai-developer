# Section 4 quiz: Selecting and configuring FMs

12 questions. Aim for 10 or more. Answers and explanations are at the end.

**1.** A company must choose between three Bedrock models for summarizing support tickets. Public benchmark scores favor model A. What is the BEST way to decide?

- A. Choose model A because it has the best benchmark score
- B. Choose the newest model
- C. Run a representative set of real tickets through each model and compare quality, latency and cost per summary
- D. Choose the model with the largest context window

**2.** A team needs to classify 3 million short support emails into 8 categories each day at the lowest cost. Quality tests show every candidate scores above the target. Which model should they pick?

- A. The largest available model
- B. The smallest, fastest model that meets the quality target
- C. An embedding model
- D. A fine-tuned large model

**3.** Several applications call Bedrock directly with hard-coded model IDs. The company wants to change models for all applications without modifying application code. Which solution meets this requirement?

- A. Store the model ID in each Lambda function's environment variables
- B. A shared API Gateway and Lambda router that reads the model ID from AWS AppConfig
- C. Ask each team to update its code when the model changes
- D. Use Provisioned Throughput for every model

**4.** Why is AWS AppConfig a better place than a Lambda environment variable for the active model ID? (Select TWO.)

- A. AppConfig validates configuration against a schema before deployment
- B. AppConfig makes model calls cheaper
- C. AppConfig can roll back automatically when a CloudWatch alarm fires during deployment
- D. AppConfig encrypts model responses
- E. AppConfig removes the need for IAM permissions

**5.** A chat application is throttled during peak hours. The model it uses has limited capacity in the company's Region. The company wants more throughput with no infrastructure to manage. What should it do?

- A. Move the application to a SageMaker AI endpoint
- B. Call the model through a Bedrock cross-Region inference profile
- C. Increase maxTokens
- D. Disable retries

**6.** A healthcare company must keep all data processing in the EU. It wants to use cross-Region inference. What must it check?

- A. That the model supports streaming
- B. That the inference profile only routes to Regions inside the EU
- C. That it uses batch inference
- D. That the model is open-weight

**7.** A team wants requests to stop going to a primary model that keeps failing, use a fallback instead, and try the primary again after a cool-down. Which pattern and services fit?

- A. A circuit breaker built with AWS Step Functions and Amazon DynamoDB
- B. An Amazon SQS dead-letter queue only
- C. A larger Lambda timeout
- D. An AWS Budgets alert

**8.** A legal firm has 400 GB of unlabeled contracts. It wants a model that understands legal language better before it builds any specific tasks. Which customization method fits?

- A. Fine-tuning on prompt and answer pairs
- B. Continued pre-training on the unlabeled contracts
- C. Prompt engineering only
- D. RAG with no customization

**9.** A software company needs 40 customized variants of one base model, one per enterprise customer, and wants to keep hosting costs low. What approach fits BEST?

- A. Fully fine-tune 40 separate models and host each on its own endpoint
- B. Train a LoRA adapter per customer and serve the adapters on shared SageMaker AI endpoints with inference components
- C. Use 40 different foundation models
- D. Put each customer's data in the system prompt

**10.** Which service gives a team versioning, approval status and lineage for customized models, and can trigger deployment when a version is approved?

- A. Amazon ECR
- B. SageMaker Model Registry
- C. AWS CodeCommit
- D. Amazon S3 versioning only

**11.** A new fine-tuned model version is being deployed to a SageMaker AI endpoint. The company wants to limit the impact if the new version performs badly. What should it use?

- A. Deploy to all traffic at once and monitor manually
- B. Deployment guardrails with canary traffic shifting and automatic rollback on CloudWatch alarms
- C. Delete the old version before deploying
- D. Increase the instance count

**12.** A Bedrock model that an application depends on has moved to Legacy status. What is the BEST response?

- A. Ignore it until the model stops responding
- B. Evaluate replacement models on the existing test set, then switch through configuration and roll out gradually
- C. Rewrite the application for a new provider
- D. Buy Provisioned Throughput for the legacy model

---

## Answers

1. **C.** Benchmarks shortlist, but your own representative data decides.
2. **B.** For a narrow, high-volume task that every model handles, the smallest model that meets the target minimizes cost.
3. **B.** A router reading AppConfig switches models for every app without code changes.
4. **A, C.** Validation and alarm-based rollback, along with gradual rollout and no redeploy.
5. **B.** Cross-Region inference adds capacity and resilience with no infrastructure to manage.
6. **B.** Requests can be processed in any Region in the profile, so it must stay within the EU.
7. **A.** Step Functions runs the flow and DynamoDB stores the circuit state.
8. **B.** Large amounts of unlabeled domain text point to continued pre-training.
9. **B.** LoRA adapters are small and can share endpoints, which keeps hosting cheap.
10. **B.** Model Registry versions models and tracks approval, and approval can trigger deployment.
11. **B.** Gradual traffic shifting with automatic rollback limits the impact of a bad release.
12. **B.** A test set plus config-driven routing makes migration routine.
