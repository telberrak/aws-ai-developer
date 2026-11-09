# Lab 0: your first Bedrock call

Section 2, Lecture 2.5. Exam skills 1.3.3 and 2.4.1.

You make the same Converse request two ways: from Python with boto3, then from the AWS CLI.

**Estimated cost:** a few cents (on-demand tokens only). **Teardown:** nothing to delete; this lab creates no resources.

## Before you start

- Your lab account is set up as in [`setup/README.md`](../../setup/README.md).
- Model access is enabled in the Bedrock console for the model you'll use, in your Region.
- Your profile can call `bedrock:InvokeModel` (Converse uses the same permission).

Set two variables. Use the model ID from the Bedrock console, or an inference profile ID if the console says the model needs one.

```bash
export AWS_REGION=[region]
export MODEL_ID=[model-id]
```

## Part 1: Python

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python converse.py "What is RAG?"
```

Then try:

1. Run `python converse.py "Suggest a name for a GenAI study group" --temperature 0.9` three times. Then run it three times with `--temperature 0`. Which answers vary more?
2. Run with `--max-tokens 20`. Check that the stop reason is now `max_tokens` and the answer is cut off.
3. Compare `outputTokens` in the usage line with the length of each answer.

## Part 2: AWS CLI

```bash
aws bedrock-runtime converse \
  --model-id "$MODEL_ID" \
  --messages '[{"role":"user","content":[{"text":"What is RAG?"}]}]' \
  --inference-config '{"temperature":0.2,"maxTokens":300}'
```

The response has the same shape as in Python: `output.message.content[0].text`, `stopReason` and `usage`.

## Troubleshooting

| Error | Fix |
| --- | --- |
| `AccessDeniedException` | Enable model access for this model in this Region, and check your IAM permissions. |
| `ValidationException` mentioning on-demand throughput or an inference profile | Use the model's inference profile ID (for example one starting with a geography prefix) as `MODEL_ID`. |
| `ResourceNotFoundException` | The model isn't offered in your Region. Pick another model or Region. |
| `ThrottlingException` | Wait a few seconds and retry. On-demand quotas are per account and Region. |
