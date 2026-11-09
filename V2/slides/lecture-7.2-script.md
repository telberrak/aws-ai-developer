# Lecture 7.2: Orchestration and safeguards — narration script

Section 7, Agents and tools. About 10 minutes. The same text is in the speaker notes of `lecture-7.2.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Orchestration and safeguards

(About 40 seconds)

In the last lecture, / we saw that an agent decides its own next step. / In this one, / we make sure it does that **safely**. [pause] I'll show you the loop at the heart of every agent, / how to run that loop with Step Functions, / how to make sure it always stops, / and how to fence in what it can do. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] The model only **asks** for actions, / your code decides whether they **happen**. [long pause]

Transition: So, / what does that loop look like?

## 2. Reason, act, observe, repeat

(About 1 min 30 seconds)

Most agents run a pattern called **ReAct**. / Reason, / then act. / Here's how it goes. [pause]

▶ CLICK

First, / **reason**. / The model looks at the goal / and everything it knows so far, / and works out what it needs next.


▶ CLICK

Second, / **act**. / It asks for **one** tool call, / with the arguments. / Look up order one two three, / for example.


▶ CLICK

Third, / **observe**. / Your code runs the tool, / and hands the result back to the model.


▶ CLICK

And when it has enough, / it stops asking for tools, / and **answers**.


▶ CLICK

Steps one to three repeat, / as many times as it needs. [pause] And here's the important part. / The model **never** runs a tool itself. / It only asks. / Your code runs it. [pause] And that's exactly where you keep control. / Every safeguard in this lecture sits at that point. [long pause]

Transition: So, / who runs that loop? / You can write it yourself, / or let a framework do it. / But there's another option.

## 3. Run the loop as a Step Functions workflow

(About 2 minutes)

You can run the loop as a **Step Functions** workflow. [pause]

▶ CLICK

First state, / **call the model**. / Step Functions has an optimized integration with Bedrock, / so there's no Lambda in between.


▶ CLICK

Then a **Choice** state. / It reads the stop reason in the response. / Did the model ask for a tool, / or did it finish?


▶ CLICK

If it asked for a tool, / **run the tool**. / One Lambda function per tool, / and then loop back to the model with the result.


▶ CLICK

And when the model stops asking for tools, / **return the answer**.


▶ CLICK

So, / why go to the trouble? [pause] Because you get three things for free. / **Retries and timeouts** on every state. / A **full history** of every step, / which is gold for an audit. / And a **human approval step**. / Step Functions can pause and wait for a task token, / until a person approves, / and then carry on. [pause] So when a question mentions auditability, / or a human approval in the middle of an agent, / think Step Functions. [long pause]

Transition: But whoever runs the loop, / it needs a way to stop.

## 4. Every loop needs a way out

(About 1 min 30 seconds)

An agent that never stops / is an agent that burns money. / So every loop needs a way out. / Here are four. [pause]

▶ CLICK

**Maximum iterations**. / Stop after a fixed number of tool calls. / Ten is a common starting point.


▶ CLICK

**Timeouts**. / On each tool call, / so one slow API doesn't hang everything, / and on the whole run.


▶ CLICK

**Budgets**. / A ceiling on tokens, / or on cost, / for a single request.


▶ CLICK

And **no progress**. / If the model calls the same tool, / with the same arguments, / twice in a row, / it's stuck. / Stop it.


▶ CLICK

And when a limit hits, / fail **gracefully**. / Return what you have, / say what's missing, / or hand it over to a person. / Never just time out with an error. [long pause]

Transition: Stopping is one guardrail. / Limiting what the agent can touch is another.

## 5. An agent can only do what its role allows

(About 1 min 30 seconds)

Here's the principle. / An agent can only do what its **role** allows. / So you design the roles carefully. [pause]

▶ CLICK

**One role per tool**. / Each Lambda tool gets its own IAM role, / with only the actions and resources that tool needs. / The order-lookup tool can read orders. / It can't touch payments.


▶ CLICK

**Permission boundaries**. / A ceiling that no tool role can go above, / even if someone edits the role later.


▶ CLICK

**Act as the user**. / The agent should work with the user's identity and permissions, / never with broader access of its own. / AgentCore Identity is built for exactly this.


▶ CLICK

And **confirm risky actions**. / Refunds, / deletes, / emails to customers. / Those wait for a person to approve them. [pause] The model can be tricked by what it reads. / Your IAM policy can't. [long pause]

Transition: Last piece. / Checking what goes in, / and what comes out.

## 6. Check what goes in, what comes out, and what it did

(About 1 min 30 seconds)

Four checks, / around the whole loop. [pause]

▶ CLICK

**Bedrock Guardrails**. / Content filters, / denied topics, / PII masking, / and prompt-attack detection. / And you apply them to the input **and** the output.


▶ CLICK

**Validate tool inputs**. / Before any tool runs, / check every argument the model sent. / Is that order ID real? / Is that amount within limits?


▶ CLICK

**Trace every step**. / Model calls, / tool calls and tokens, / in CloudWatch. / So you can see why the agent did what it did.


▶ CLICK

And **audit every action**. / CloudTrail records the AWS API calls your tools made, / and who made them. [long pause]

Transition: Let's wrap up.

## 7. Lecture recap

(About 1 minute)

So, / let's bring it together. [pause]

▶ CLICK

First, / the model asks, / and your code acts. / ReAct repeats reason, / act, / observe. / And Step Functions can run that loop, / with retries, / history / and human approval built in.


▶ CLICK

Second, / every loop needs a way out. / Maximum iterations, / timeouts, / budgets, / and a no-progress check. / Then fail gracefully.


▶ CLICK

And third, / fence the agent in. / Least-privilege roles, / Bedrock Guardrails, / validated tool inputs, / and a full audit trail. [pause]

So, / back to our one sentence. [pause] The model only **asks** for actions, / your code decides whether they **happen**. [long pause]

Transition: In the next lecture, / we look at agents working with **people**, / and with other models. / Model coordination and human in the loop.
