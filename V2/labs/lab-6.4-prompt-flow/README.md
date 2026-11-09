# Lecture 6.4 demo: a versioned prompt in a Prompt Flow

This is the code for the demo in Lecture 6.4. You deploy a prompt in Amazon Bedrock Prompt Management, freeze it as version 1, and use that version in an Amazon Bedrock Flow that apps call through an alias named `live`. Then you release a new prompt by creating new versions and moving the alias, and you roll back by moving the alias back.

**Cost:** a few cents. Prompts, flows, versions and aliases cost nothing to keep; you pay only for the model tokens each call uses. **Teardown:** `python cleanup.py`, then `cdk destroy`.

## What gets deployed

- **Prompt** `lab-6-4-ticket-triage`: a text template with one variable, `{{ticket}}`, plus the model and its settings (temperature 0.2, up to 300 tokens)
- **Prompt version 1**: a frozen snapshot of that prompt
- **Flow** `lab-6-4-ticket-flow`: input, then a prompt node that uses prompt version 1, then output
- **Flow version 1** and the alias **`live`**, which points at it. Apps call the alias, never a version number.
- **IAM role**: lets the flow read the prompt and call the one model, and nothing else

## Before you start

- Your account is set up as in Lecture 1.3, including the AWS CDK. Bootstrap the account and Region once with `cdk bootstrap`.
- Use a Region with Bedrock Prompt Management and Flows, such as `us-east-1`.
- Your account can use the text model in `cdk.json`, Amazon Nova Micro by default. To use another model, pass `-c model_id=<id>`. If the console says the model needs an inference profile, pass the profile ID, such as `us.amazon.nova-micro-v1:0`.

## Steps

1. Install and deploy:

   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   cdk deploy
   ```

   The scripts read the stack outputs themselves, so you don't need to copy anything.

2. Call the flow the way an app would:

   ```bash
   python invoke.py "My order arrived broken and nobody answers my emails."
   ```

   It says the alias points at flow version 1, then prints three lines: Summary, Sentiment and Next action.

3. Release a new prompt. `prompt-v2.txt` adds an **Urgency** line and a 50-word limit:

   ```bash
   python release.py prompt-v2.txt
   ```

   The script edits the prompt's draft, creates prompt version 2, points the flow's draft at it, prepares the flow, creates flow version 2, and only then moves `live` from version 1 to version 2.

4. Call it again with the same ticket:

   ```bash
   python invoke.py "My order arrived broken and nobody answers my emails."
   ```

   The alias now points at version 2, and the answer has four lines, including Urgency.

5. Roll back:

   ```bash
   python rollback.py 1
   python invoke.py "My order arrived broken and nobody answers my emails."
   ```

   The answer goes back to three lines. Nothing was rebuilt: the alias just points at version 1 again.

Model answers vary from call to call, so expect the wording to change. The shape of the answer, three lines or four, is what shows which version ran.

## Good to know

- Steps 3 to 5 change the prompt, the flow and the alias outside CloudFormation, so CloudFormation sees them as drift. That's fine for a lab. In a real project you'd release through your pipeline instead.
- Prompt and flow versions can't be edited. To change anything, you change the draft and create a new version.

## If something fails

- **`cdk deploy` fails on the flow or the alias.** Check that the model ID is right for your Region, and that the prompt's variable name (`ticket`) matches the prompt node's input.
- **`AccessDeniedException` or `ValidationException` when you call the flow.** Check that your account can use the model. Some models must be called through an inference profile ID.
- **`release.py` says the flow failed to prepare.** If you changed the prompt's variables, the prompt node's inputs no longer match. Keep the variable `{{ticket}}`.
- **The answer didn't change after a release.** Run `invoke.py` again and check which version it says the alias points at.

## Teardown

```bash
python cleanup.py
cdk destroy
```

`cleanup.py` moves the alias back to version 1 and deletes the versions `release.py` created, because CloudFormation only knows about the ones it made.
