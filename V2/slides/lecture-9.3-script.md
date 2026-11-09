# Lecture 9.3: Front ends and business integrations — narration script

Section 9, FM APIs and application patterns. About 8 minutes. The same text is in the speaker notes of `lecture-9.3.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Front ends and business integrations

(About 40 seconds)

So far, / our model lives behind an API. / But people don't call APIs. / They use **apps**. / A website, / a CRM, / a contact center, / a pile of scanned forms. [pause] In this lecture, / I'll show you how to put a front end on your model, / how to describe your APIs once so every tool can use them, / and how to bring AI into the business systems people already work in. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Keep the model **behind your backend**, / describe your APIs **once**, / and bring the AI to **where people already work**. [long pause]

Transition: So, / how do you build a front end quickly?

## 2. A web front end with Amplify

(About 1 min 30 seconds)

With **AWS Amplify**. [pause]

▶ CLICK

It starts with a **web app**. / React, / or another framework, / and Amplify hosts it for you.


▶ CLICK

**Sign-in**. / Amplify sets up Amazon Cognito, / so users and sessions are handled from day one.


▶ CLICK

The **backend**. / In Amplify, / you define your API and your functions in code, / and it deploys them for you.


▶ CLICK

And **Bedrock** gets called from that backend. / **Never** from the browser. / If the browser could call the model directly, / anyone could grab the credentials and run up your bill.


▶ CLICK

Amplify also has an **AI kit**. / You declare a chat conversation, / or a one-shot generation, / in your backend code, / and you get ready-made chat components for the front end. / And the model credentials stay on the server, / where they belong. [long pause]

Transition: Now, / what about connecting AI to the APIs you already have?

## 3. One OpenAPI spec, many uses

(About 1 min 30 seconds)

Here's a habit that pays off again and again. / Describe each API **once**, / with an **OpenAPI** spec. [pause]

On the left, / a tiny spec. / A path, / an operation ID, / and a description. [pause]

▶ CLICK

**API Gateway** can import that spec / to create the API itself, / with its routes and request validation.


▶ CLICK

**Bedrock Agents** use it too. / An action group takes the spec, / so the agent knows which operations it can call, / and with which parameters.


▶ CLICK

And **AgentCore Gateway** can take it / and turn that API into tools / that any MCP client can use.


▶ CLICK

So here's the tip. [pause] Write **good descriptions**. / The model reads them to decide which operation to call. / A vague description means the wrong tool, / or no tool at all. [long pause]

Transition: Now, / let's go to where many users actually live. / The CRM.

## 4. Bring AI into the CRM

(About 1 min 30 seconds)

There are four ways to bring AI into your business systems. [pause]

▶ CLICK

First, / **the CRM calls you**. / A button, / or a workflow step in the CRM, / calls your GenAI API, / through API Gateway, / to draft a reply / or summarize a case.


▶ CLICK

Second, / **data flows to you**. / Amazon AppFlow copies records from SaaS apps, / like Salesforce, / into S3. / And from there, / they're ready for a knowledge base.


▶ CLICK

Third, / **events reach you**. / Some SaaS apps can send events to EventBridge, / so a new case or a new order can start an AI workflow on its own.


▶ CLICK

And fourth, / **the contact center**. / Amazon Connect brings AI into customer calls and chats, / with assistance for the human agents built in. [pause] So you don't have to drag people to a new app. / You bring the AI to them. [long pause]

Transition: And one integration shows up in almost every company. / Documents.

## 5. From a scanned form to clean data

(About 1 min 45 seconds)

Here's a document processing pipeline, / from a scanned form to clean data. [pause]

▶ CLICK

It starts with an **upload**. / A form or a PDF lands in S3.


▶ CLICK

The upload event goes to **EventBridge**, / and that **triggers** the workflow.


▶ CLICK

**Step Functions** orchestrates every step. / It retries what fails, / and catches what can't be fixed.


▶ CLICK

Then we **read and extract**. / Textract pulls out the text, / the forms / and the tables, / or Bedrock Data Automation does it in one call. / Then a model maps the result to clean JSON. / Name, / amount, / date, / policy number.


▶ CLICK

And we **store** the clean fields, / say in DynamoDB, / ready for other systems.


▶ CLICK

And here's the part people forget. [pause] When the confidence is **low**, / send that document to a person for review, / with Augmented AI, / before it goes anywhere. [long pause]

Transition: Let's wrap up.

## 6. Lecture recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / Amplify for the front end. / Hosting, / sign-in with Cognito, / and a backend that calls Bedrock for you.


▶ CLICK

Second, / describe your APIs **once**. / One OpenAPI spec feeds API Gateway, / agents / and MCP tools.


▶ CLICK

And third, / meet people where they work. / CRM calls, / AppFlow, / EventBridge, / Amazon Connect, / and document pipelines. [pause]

So, / back to our one sentence. [pause] Keep the model **behind your backend**, / describe your APIs **once**, / and bring the AI to **where people already work**. [long pause]

Transition: Next, / the tools that help you build all this faster, / and find out why it broke.
