# Design: "HelpBot" customer support assistant (v0.9, draft)

**Owner:** Customer Support Engineering · **Status:** ready for review

## Goal

Answer customer questions about orders, returns and warranties on the public website, 24/7, to reduce tickets to human agents.

## Architecture

1. The website chat widget calls a public Amazon API Gateway REST endpoint.
2. API Gateway invokes an AWS Lambda function.
3. The Lambda function builds a prompt and calls Amazon Bedrock with the Converse API. The model ID is hard-coded in the function.
4. To answer policy questions, the function loads the full returns and warranty policy documents (about 60 pages) from Amazon S3 and adds them to every prompt.
5. To answer order questions, the function queries the orders table in Amazon DynamoDB using the order number the customer types.
6. The last 20 messages of each conversation are kept in the Lambda function's memory between calls.
7. The answer is returned in one piece when generation finishes.

## Security

- The Lambda execution role has `bedrock:*`, `s3:*` and `dynamodb:*` on all resources.
- The API is open to the internet so anonymous visitors can use it.

## Operations

- Lambda logs go to Amazon CloudWatch Logs with default settings.
- Deployed in one Region from the console.

## Testing

- The team tried about 15 questions during development and the answers looked good.

## Cost

- Not estimated yet. Expected traffic: 50,000 conversations per day at launch.
