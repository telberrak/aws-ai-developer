# Lab account setup

Do this once before Lab 0. It matches Lecture 1.5 of the course.

## 1. Use a dedicated account

Create a new AWS account, or ask for a sandbox account in your organization. Never run course labs in a production account.

## 2. Secure the root user and create an admin user

1. Sign in as root and turn on MFA for the root user.
2. Enable IAM Identity Center and create a user with administrator access.
3. Sign out of root and use that user from now on.

## 3. Set up cost protection

1. Create a CloudWatch billing alarm at a low monthly amount you're comfortable with.
2. Turn on AWS Cost Anomaly Detection with an email alert.

## 4. Pick one region

Use one region for every lab: `[region]`. Pick a region where Amazon Bedrock offers the models listed below; check the Bedrock console's model catalog for availability.

## 5. Enable Bedrock model access

In the Amazon Bedrock console, enable access to the models the labs use:

- `[text model]`
- `[embedding model, for example an Amazon Titan embeddings model]`
- `[reranker model]`

## 6. Install local tools

- AWS CLI v2, configured for your admin user (`aws configure sso`)
- Python 3
- Node.js and the AWS CDK (`npm install -g aws-cdk`), then `cdk bootstrap` in your region
- Clone this repo

## Check it works

```bash
aws sts get-caller-identity
```

This should print your account and user. A smoke-test script that calls a Bedrock model will be added with Lab 0.

## Cost rules for every lab

1. Run the lab's teardown command the same day.
2. Watch always-on resources: Bedrock provisioned throughput, OpenSearch clusters and SageMaker endpoints bill by the hour.
3. Check Cost Explorer weekly, grouped by service.
