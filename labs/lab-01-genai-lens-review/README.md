# Lab 1: Generative AI Lens review

Section 3, Lecture 3.3.

You review a draft GenAI design with the AWS Well-Architected Tool and the Generative AI Lens, then improve the design.

**Estimated cost:** none. The Well-Architected Tool has no charge, and this lab creates no billable resources. **Teardown:** delete the workload in the WA Tool when you finish (optional).

## Steps

1. Read [`sample-design.md`](sample-design.md), a draft design for a customer support assistant. Write down anything that worries you before you start.
2. Open the **AWS Well-Architected Tool** in the console in your lab Region and choose **Define workload**.
   - Name: `helpbot-lab1`
   - Environment: pre-production
   - Regions: your lab Region
3. On the **Apply lenses** step, keep the **AWS Well-Architected Framework** lens and add the **Generative AI Lens** from the lens catalog.
4. Start reviewing the **Generative AI Lens**. Answer each question **only from what the design document says**. If the document doesn't mention a practice, don't select it.
5. When you finish, open the **Improvement plan**. Note the high-risk items, then the medium-risk ones.
6. Write an improved version of the design (copy `sample-design.md` to `my-design.md`) that fixes the top five risks.
7. Optional: save a **milestone** named `before-fixes`, update your answers to match `my-design.md`, and compare the risk counts.

### Optional: the AWS CLI

```bash
aws wellarchitected list-lenses --query "LensSummaries[].[LensName,LensAlias]" --output table
```

Find the Generative AI Lens alias in the output. You can then use it with `aws wellarchitected create-workload --lenses wellarchitected <alias> ...`.

## Check your answers

Read this after you've done the review. These are the gaps planted in the design.

| Gap in the design | Better approach |
| --- | --- |
| No guardrails on a public chatbot | Amazon Bedrock Guardrails for harmful content, prompt attacks, denied topics and PII |
| Full 60-page policies in every prompt | RAG with a Bedrock knowledge base, which cuts tokens, cost and latency |
| Anyone can query any order number | Authenticate customers (for example Amazon Cognito) and only return their own orders |
| Wildcard IAM permissions | Least privilege: invoke only the chosen model, read only the needed bucket and table |
| Public API with no throttling | API Gateway usage plans and throttling, plus AWS WAF |
| Chat history in Lambda memory | Store session history in DynamoDB, because Lambda instances don't keep state |
| Hard-coded model ID | Configuration (for example AWS AppConfig) so the model can change without a deploy |
| No streaming | ConverseStream so customers see the answer as it's written |
| 15 informal test questions | A representative evaluation set with quality targets, run before each release |
| No cost estimate at 50,000 conversations per day | Estimate cost per conversation and set budgets and alarms |
| Console deployment, one Region, default logging | Infrastructure as code, a resilience plan (for example cross-Region inference) and model invocation logging |

## Cleanup

In the WA Tool, choose the `helpbot-lab1` workload, then **Delete**.
