# Lecture 7.1: What makes an agent, and multi-agent systems — narration script

Section 7, Agents and tools. About 12 minutes. The same text is in the speaker notes of `lecture-7.1.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. What makes an agent, and multi-agent systems

(About 50 seconds)

Welcome to Section 7. / This is where Domain 2 starts, / and Domain 2 is all about **building** the application around the model. [pause] And we open with the topic everyone wants to talk about. / **Agents**. [pause]

In this lecture, / I'll show you the four parts that make an agent, / when you shouldn't use one, / the four ways to build one on AWS, / and what changes when you put several agents together. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] An agent is a model that **decides its own next step**, / so only use one when your code can't decide it for you. [long pause]

Transition: So, / what actually makes something an agent?

## 2. Four parts make an agent

(About 1 min 45 seconds)

Strip away the hype, / and an agent has four parts. [pause]

▶ CLICK

First, / the **model**. / On AWS, / that's usually a model on Bedrock. / It reads the goal, / looks at what it knows so far, / and decides what to do next.


▶ CLICK

Second, / **tools**. / Functions and APIs the agent is allowed to call. / Look up an order, / search a Knowledge Base, / send an email. / Without tools, / the model can only talk.


▶ CLICK

Third, / the **loop**. / Think, / act, / look at the result, / and go round again, / until the job is done.


▶ CLICK

And fourth, / **memory**. / What's happened in this session so far, / and, / if you need it, / what it learned in earlier sessions.


▶ CLICK

Now, / here's the part that matters. [pause] In a normal chain, / **your code** decides the order of the steps. / In an agent, / the **model** decides, / at run time. [pause] That's where the power comes from. / And it's also where the risk comes from. [long pause]

Transition: Which raises a fair question. / When should you **not** use an agent?

## 3. Not every problem needs an agent

(About 1 min 30 seconds)

Here's how I think about it. / Three options, / from simplest to most flexible. [pause]

▶ CLICK

If it's **one question with one answer**, / like summarizing a document, / use a single prompt. / It's the cheapest, / the fastest, / and the easiest to test.


▶ CLICK

If the steps are **known in advance**, / use a workflow. / Step Functions is a great fit. / Extract, / validate, / call the model, / store the result. / It's predictable, / you can audit every step, / and retries are built in.


▶ CLICK

And only when the steps **depend on what it finds along the way**, / use an agent. / A support case where the next lookup depends on the last answer, / for example. / You get flexibility, / but you pay for it in latency, / tokens, / and testing effort.


▶ CLICK

So here's my rule of thumb. [pause] If you can **draw the flowchart**, / build the workflow. / Use an agent when you can't. [pause] And in a scenario question, / if the steps are fixed and auditability matters, / the agent is usually the **wrong** answer. [long pause]

Transition: Now, / when you do need an agent, / how do you build one on AWS?

## 4. Four ways to build one

(About 2 minutes)

There are four ways you'll see. [pause]

▶ CLICK

First, / **Strands Agents**. / It's an open-source SDK from AWS. / You give it a model, / a system prompt and a list of tools, / and it runs the loop for you. / A working agent is a few lines of Python, / and it works with Bedrock models out of the box.


▶ CLICK

Second, / **Agent Squad**. / Also open source from AWS. / Its job is routing. / A classifier looks at each request / and sends it to the specialist agent that fits, / while keeping the conversation context.


▶ CLICK

Third, / **Bedrock Agents**. / This one's fully managed. / You write instructions, / attach action groups, / which are your APIs or Lambda functions, / and attach Knowledge Bases. / Bedrock runs the orchestration. / Less code, / less control.


▶ CLICK

And fourth, / **Bedrock AgentCore**. / This is the newer piece, / and it's about running agents in **production**. / You build the agent in whatever framework you like, / Strands, / LangGraph, / CrewAI, / and AgentCore runs it, / with the hard parts managed. [pause] So, / the simple way to remember it. / Strands and Agent Squad help you **build**. / Bedrock Agents and AgentCore help you **run**. [long pause]

Transition: So, / what are those hard parts that AgentCore takes off your hands?

## 5. What AgentCore runs for you

(About 2 minutes)

AgentCore is a set of services. / You can use them together, / or one at a time. / Here are the five you need to know. [pause]

▶ CLICK

**Runtime**. / Serverless hosting for your agent. / Each user session runs isolated from the others, / and it supports long-running work, / not just quick request and response.


▶ CLICK

**Gateway**. / It takes your existing APIs and Lambda functions / and turns them into **MCP tools** the agent can find and call. / So you don't rewrite your services to make them agent-ready.


▶ CLICK

**Memory**. / Short-term memory for the current session, / and long-term memory across sessions, / like a user's preferences. / You don't have to build that store yourself.


▶ CLICK

**Identity**. / Who the agent is acting for, / and the credentials it uses to reach other services, / including third-party ones through OAuth. / This is how you stop an agent from using **more** access than the user it's working for.


▶ CLICK

And **Observability**. / Traces of every step, / every tool call / and every token, / sent to CloudWatch. / When an agent does something strange, / this is where you find out why. [pause] There are also built-in tools, / like a code interpreter and a browser, / but these five are the core. [long pause]

Transition: So far, / we've talked about one agent. / What happens when you need several?

## 6. When one agent isn't enough

(About 2 minutes)

There are four common patterns. [pause]

▶ CLICK

**Supervisor**. / One agent plans the work, / and hands parts of it to specialist agents. / A travel agent hands flights to one specialist, / and hotels to another, / then puts the answers together.


▶ CLICK

**Agents as tools**. / This one's simpler than it sounds. / A specialist agent is just wrapped up as a tool, / and the main agent calls it like any other tool.


▶ CLICK

**Router**. / A classifier looks at each request / and sends it to the **one** agent that fits. / That's exactly what Agent Squad does.


▶ CLICK

And **graph**. / Agents connected in a fixed flow, / each one doing its part and passing the work on. / Notice that this one is close to a workflow, / just with agents in the boxes.


▶ CLICK

But here's my advice. [pause] **Start with one agent**. / Every extra agent adds latency, / cost, / and another place for things to go wrong. / Split it only when the prompt, / the tool list, / or the permissions get too big for one. [long pause]

Transition: Let's wrap up.

## 7. Lecture recap

(About 1 minute)

So, / let's bring it together. [pause]

▶ CLICK

First, / an agent has four parts. / A model, / tools, / a loop / and memory. / And the model picks the next step, / not your code.


▶ CLICK

Second, / pick the simplest thing that works. / A single prompt, / then a workflow, / then an agent, / and only then several agents.


▶ CLICK

And third, / build and run. / Strands or Agent Squad to build, / Bedrock Agents or AgentCore to run in production. [pause]

So, / back to our one sentence. [pause] An agent is a model that **decides its own next step**, / so only use one when your code can't decide it for you. [long pause]

Transition: But if the model decides the steps, / what stops it from going round forever, / or doing something it shouldn't? / That's the next lecture. / Orchestration and safeguards.
