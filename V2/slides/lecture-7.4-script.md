# Lecture 7.4: Tool design and MCP servers — narration script

Section 7, Agents and tools. About 10 minutes. The same text is in the speaker notes of `lecture-7.4.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Tool design and MCP servers

(About 30 seconds)

An agent is only as good as the tools you give it. [pause] In this lecture, / we look at how to design a tool a model can actually use well, / and then how to serve your tools through **MCP**, / so every agent calls them the same way. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Design each tool as a **clear contract**, / then serve it **once** through MCP, / on the AWS service that fits how it runs. [long pause]

Transition: So, / what does a model actually see when it looks at a tool?

## 2. A tool is a contract the model reads

(About 1 min 15 seconds)

Here's a tool definition. / To the model, / this is a **contract**. / It's all it knows about the tool. [pause]

▶ CLICK

First, / the **name**. / Use a verb and a noun, / like get order status. / Models pick tools by name first, / so a vague name like helper / leads to wrong calls.


▶ CLICK

Second, / the **description**. / This is the model's only manual. / Say what the tool does, / and **when** to use it. / Here, / when a customer asks where their order is.


▶ CLICK

And third, / the **input schema**. / Types, / patterns, / and required fields. / The order ID must look like O R D, / dash, / six digits. / So a bad call fails early, / with a clear reason, / before it ever reaches your system. [long pause]

Transition: From that, / we get five rules for good tools.

## 3. Five rules for tools a model can use

(About 1 min 30 seconds)

Five rules. / Get these right, / and most agent problems with tools disappear. [pause]

▶ CLICK

One. / A **clear name and description**. / Say what it does, / when to use it, / and what it returns.


▶ CLICK

Two. / A **tight input schema**. / Use enums, / patterns / and required fields, / instead of one big free-text field the model has to guess at.


▶ CLICK

Three. / **One job per tool**. / A small, / focused tool beats one giant tool with ten modes and a mode parameter. / The model chooses better, / and you can secure each one separately.


▶ CLICK

Four. / **Safe to retry**. / Make tools idempotent where you can. / Models retry, / and so do networks. / Creating the same refund twice is a bug you don't want.


▶ CLICK

And five. / **Errors the model can act on**. / Order ID must look like O R D, / dash, / six digits, / tells the model exactly how to fix the call. / Error five hundred / tells it nothing. [long pause]

Transition: Now, / how do you share those tools with every agent you build?

## 4. MCP: write a tool once, use it from any agent

(About 1 min 15 seconds)

That's what the **Model Context Protocol**, / MCP, / is for. / It's an open standard for connecting agents to tools. [pause]

▶ CLICK

It starts with the **host**. / That's the agent, / the IDE / or the chat app the user works in.


▶ CLICK

Inside the host, / there's an **MCP client**. / It keeps one connection to each server.


▶ CLICK

The **MCP server** is where your tools live. / It tells the client which tools, / resources / and prompts it offers, / and it runs the calls.


▶ CLICK

And behind the server, / **your systems**. / Databases, / APIs / and files, / reached on the agent's behalf. [pause] Here's why that matters. / Without MCP, / every agent wraps every API in its own way. / With MCP, / you write the server **once**, / and every agent can use it. [long pause]

Transition: So, / how does a client actually talk to a server?

## 5. Two ways to connect

(About 1 min)

There are two transports. [pause]

▶ CLICK

The first is **stdio**. / The host starts the server as a local process, / and they talk over standard input and output. / No network at all. / It's perfect for local tools on a developer's machine.


▶ CLICK

The second is **streamable HTTP**. / The server runs as a web service, / clients connect over HTTP, / and responses can stream back. / That's what you use for shared, / remote servers, / and it needs **authentication**.


▶ CLICK

And on AWS, / your servers are remote. / So in practice, / you'll use **streamable HTTP**, / behind authentication. [long pause]

Transition: Which brings us to the question. / Where do you run that server?

## 6. Where to run an MCP server on AWS

(About 1 min 30 seconds)

You've got three good options. [pause]

▶ CLICK

First, / **AWS Lambda**. / It fits **stateless** servers. / A request comes in, / a response goes out, / and nothing is kept in memory between calls. / It scales to zero, / so you pay per call. / But remember, / each call is limited to fifteen minutes.


▶ CLICK

Second, / **Amazon ECS on Fargate**. / This fits **long-running** servers. / Sessions with state in memory, / long streams, / and steady traffic. / The trade-off is that it's always on, / so you pay for uptime.


▶ CLICK

And third, / **Bedrock AgentCore**. / Its **Gateway** turns Lambda functions and existing APIs into MCP tools for you. / Its **Runtime** can host your own MCP server. / And inbound authentication is built in.


▶ CLICK

So here's a useful rule. / If you **already have APIs**, / don't write a new server from scratch. / Put AgentCore Gateway in front of them. [long pause]

Transition: And wherever you host it, / you have to secure it.

## 7. Every tool call is a request to your systems

(About 1 min 15 seconds)

Remember, / every tool call is a real request to your systems. / So treat it like one. [pause]

▶ CLICK

First, / **authenticate the caller**. / Use OAuth tokens, / for example from Cognito, / or IAM signatures, / before any tool runs.


▶ CLICK

Second, / **least privilege per tool**. / Each tool's role can touch only what that tool needs. / The order status tool can read orders. / It can't issue refunds.


▶ CLICK

Third, / **keep credentials out of prompts**. / The server fetches API keys from Secrets Manager. / The model never sees them, / so it can never leak them.


▶ CLICK

And fourth, / **log every call**. / Who called which tool, / with what input, / and what came back. / CloudTrail and CloudWatch give you that trail. [long pause]

Transition: Let's wrap up.

## 8. Lecture recap

(About 45 seconds)

So, / let's bring it together. [pause]

▶ CLICK

First, / design the contract. / A clear name, / a real description, / a tight schema, / one job per tool, / and errors the model can act on.


▶ CLICK

Second, / MCP lets you serve tools **once**. / Host, / client, / server. / stdio for local tools, / and streamable HTTP on AWS.


▶ CLICK

And third, / pick the right home. / Lambda for stateless servers, / ECS on Fargate for long-running ones, / and AgentCore Gateway when you already have APIs. [pause]

So, / back to our one sentence. [pause] Design each tool as a **clear contract**, / then serve it **once** through MCP, / on the AWS service that fits how it runs. [long pause]

Transition: In the next lecture, / we put it all together. / A Strands agent, / calling an MCP tool, / live.
