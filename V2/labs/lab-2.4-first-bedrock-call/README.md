# Lecture 2.4 demo: your first Bedrock call

This is the code for the demo in Lecture 2.4. You send the same Converse request two ways: from Python with boto3, then from the AWS CLI.

**Cost:** a few cents in on-demand tokens. **Teardown:** nothing to delete. This lab creates no resources.

## Before you start

- Your account is set up as in Lecture 1.3.
- Model access is on in the Bedrock console for the model you'll use, in your Region.
- Your role can call `bedrock:InvokeModel` (Converse uses the same permission).

Set two variables. Copy the model ID from the Bedrock console, or use an inference profile ID if the console says the model needs one.

```bash
export AWS_REGION=[region]
export MODEL_ID=[model-id-or-inference-profile-id]
```

## Part 1: Python

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python converse.py "What is RAG?"
```

Look at the stop reason (`end_turn`) and the usage line (input, output and total tokens).

Then try:

1. Run `python converse.py "Suggest a name for a GenAI study group" --temperature 0.9` three times. Then run it three times with `--temperature 0`. Which answers vary more?
2. Run with `--max-tokens 20`. The answer is cut off and the stop reason is now `max_tokens`.
3. Compare `outputTokens` in the usage line with the length of each answer.

## Part 2: AWS CLI

```bash
aws bedrock-runtime converse \
  --model-id "$MODEL_ID" \
  --messages '[{"role":"user","content":[{"text":"What is RAG?"}]}]' \
  --inference-config '{"temperature":0.2,"maxTokens":300}'
```

The response has the same shape as in Python: `output.message.content[0].text`, `stopReason` and `usage`.

## If it fails

| Error | Fix |
| --- | --- |
| `AccessDeniedException` | Turn on model access for this model in this Region, and check that your role can invoke it. |
| `ValidationException` mentioning on-demand throughput or an inference profile | Use the model's inference profile ID as `MODEL_ID`. |
| `ResourceNotFoundException` | The model isn't offered in your Region. Pick another model or Region. |
| `ThrottlingException` | Wait a few seconds and retry. On-demand quotas are per account and Region. |
