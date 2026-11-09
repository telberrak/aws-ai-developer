# Lecture 2.6 demo: model router with AppConfig

This is the code for the demo in Lecture 2.6. You deploy an API whose target model lives in AWS AppConfig, then switch models live without changing or redeploying any code.

**Cost:** a few cents in model calls. API Gateway, Lambda and AppConfig usage in this lab fit in typical free tiers. **Teardown:** `cdk destroy`.

## What gets deployed

- **API Gateway** `POST /chat`, throttled to 5 requests per second
- **Lambda router** ([`lambda/router.py`](lambda/router.py)): reads the route from AppConfig (cached for 15 seconds), then calls the Bedrock Converse API
- **AppConfig** application `model-router-demo`, environment `lab`, and the hosted JSON profile `model-routing`, with a JSON schema validator

## Before you start

- Your account is set up as in Lecture 0.3, including the AWS CDK. Bootstrap the account and Region once with `cdk bootstrap`.
- Model access is on in Bedrock for two models, so you have something to switch between. Note their model IDs, or inference profile IDs if the console says the model needs one.

## Steps

1. Install and deploy:

   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   cdk deploy -c modelId=[first-model-id]
   ```

   Copy the `ChatUrl` output into a variable: `export CHAT_URL=[ChatUrl]`.

2. Call the API and look at `modelId` in the response:

   ```bash
   curl -s -X POST "$CHAT_URL" -d '{"prompt":"Explain RAG in one sentence."}' | python -m json.tool
   ```

3. Switch the model. The code and the stack don't change:

   ```bash
   ./switch_model.sh [second-model-id]
   ```

4. Call the API again every few seconds. Within about 15 seconds (the router's cache), `modelId` shows the new model.
5. Try a bad change: edit `switch_model.sh` to set `"maxTokens": 99999`, then run it. The JSON schema validator rejects the new version, and production keeps working. Undo the edit afterwards.
6. Roll back by running `./switch_model.sh [first-model-id]`.

## Things to notice

- The router uses one Converse request shape for every model. That's why a model ID is all it takes to switch.
- In a real system you'd use a gradual deployment strategy (not `AppConfig.AllAtOnce`) and attach a CloudWatch alarm to the environment so AppConfig rolls back automatically.
- The IAM policy allows any foundation model or inference profile to keep the lab simple. In production, list only the models you allow.

## If it fails

| Problem | Fix |
| --- | --- |
| CDK says the bootstrap stack is missing | Run `cdk bootstrap` once for this account and Region, then deploy again. |
| The API returns an `AccessDeniedException` from Bedrock | Turn on model access for that model in your Region. |
| `modelId` doesn't change after a switch | Wait for the AppConfig deployment to finish, plus the router's 15-second cache. |

## Teardown

```bash
cdk destroy
```
