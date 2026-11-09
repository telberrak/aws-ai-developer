# Lecture 7.5: Demo: a Strands agent with an MCP tool — narration script

Section 7, Agents and tools. About 15 minutes. The same text is in the speaker notes of `lecture-7.5.pptx`. The demo code is in `labs/lab-7.5-strands-mcp-agent`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next. [ON SCREEN: …] = what to show during the live demo.

## 1. A Strands agent with an MCP tool

(About 45 seconds)

In this lecture, / we build a real agent. / A small **support agent** for an online shop. / Its tools don't live inside the agent. / They come from an **MCP server** that we write ourselves. [pause] Then we watch the agent loop call those tools, / we try to break it with bad input, / and we make it stop when it's had enough. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Put the tools behind **MCP**, / put the safety rules **in the tools**, / and give the agent a **budget**, / and any agent can use them safely. [long pause]

Transition: So, / what are we building?

## 2. One agent, tools from an MCP server

(About 2 minutes)

Here's the whole thing. / Four parts, / and one optional step. [pause]

▶ CLICK

First, / the **Strands agent**. / It's a few lines of Python. / A model, / a system prompt, / and a list of tools. / Strands runs the agent loop for us. / The model thinks, / asks for a tool, / Strands calls it, / and hands the result back to the model, / until the model has an answer.


▶ CLICK

Second, / the **model**, / in **Amazon Bedrock**. / We use Amazon Nova Pro by default, / through the Converse API. / But any Bedrock model that supports tool use will work. / You just pass a different model ID.


▶ CLICK

Third, / the **MCP server**. / This is where the tools live. / The agent doesn't import them. / It connects to the server with an **MCP client**, / asks it which tools it has, / and calls them over the protocol. / That means another agent, / or an IDE, / or a different framework, / could use the very same tools.


▶ CLICK

Fourth, / the **data**. / A small JSON file with four orders. / In real life, / this would be your order database or an internal API. / The point is, / only the server touches it. / The agent never sees the data directly, / only what the tools return.


▶ CLICK

And the optional step. / Everything runs on your laptop today. / But if you want to host it, / **Amazon Bedrock AgentCore Runtime** can run the agent for you, / and the MCP server can run there too, / or sit behind AgentCore Gateway. / The README has the steps. / You don't need them for this demo. [long pause]

Transition: So, / what do those tools look like?

## 3. Two narrow, read-only tools

(About 1 min 45 seconds)

Two tools. / And notice how **narrow** they are. [pause]

▶ CLICK

The first one is **get_order_status**. / You give it an order ID, / and it gives you back the status, / the item, / and the shipping details. / Notice what it leaves out. / It doesn't return the customer's name. / A tool should return what the agent needs, / and nothing more.


▶ CLICK

The second one is **check_refund_eligibility**. / Same input, / an order ID. / It tells you whether the order can be refunded, / and why. / And look at its description. / It says, / quote, / "It **never** issues a refund." / That's on purpose. / The model reads that description to decide when to use the tool, / so it's part of your safety design.


▶ CLICK

And here are the three rules both tools follow. [pause] They're **read-only**, / and they say so in their annotations. [pause] They **check their input** before they touch any data. / An order ID has to look exactly like O-R-D, / dash, / four digits, / or the tool refuses. [pause] And they have **clear descriptions**, / with the argument format spelled out. / Small, / strict / and well described. / That's what makes a good tool. [long pause]

Transition: Now let's look at the code that ties it together.

## 4. Three things in agent.py

(About 1 min 30 seconds)

Here's the heart of agent dot py. / Three things to notice. [pause]

▶ CLICK

Number one, / the **MCP client**. / We tell it how to start the server, / here over **stdio**, / which means the client launches the server as a child process and talks to it through standard input and output. / If the server runs somewhere else, / you pass a URL instead, / and it uses **streamable HTTP**.


▶ CLICK

Number two, / the **tools come from the server**. / list tools sync asks the server what it offers, / and we hand that list straight to the agent. / We never wrote a tool definition in the agent. / Add a tool to the server, / and the agent gets it next time it connects.


▶ CLICK

And number three, / the **stopping condition**. / ToolBudget is a hook. / Before every tool call, / Strands fires an event, / and our hook counts the calls. / Once we pass the budget, / it **cancels** the call, / and tells the model to answer with what it already knows. / So the agent can't loop forever, / and you control the cost of every question. [long pause]

Transition: Let's run it.

## 5. Check the server, then ask the agent

(About 2 min 30 seconds)

[ON SCREEN: terminal in the lab folder, virtual environment active, requirements installed] [pause]

▶ CLICK

First, / I check the server **on its own**, / with no AWS call at all. [ON SCREEN: run python list_tools.py] [pause] There are our two tools, / with their descriptions. / A status for order one-oh-oh-two. / A "not eligible" for one-oh-oh-four, / because it was delivered eighty-six days ago. / And the bad order ID gets **refused**. / So the server works before any model is involved.


▶ CLICK

Now the agent. [ON SCREEN: run python agent.py "Where is my order ORD-1002?" and point at the tool-call line on stderr] [pause] Watch the line on top. / Tool call one of three, / get order status, / with order ID one-oh-oh-two. / The model chose the tool, / and filled in the argument. / And the answer? / It shipped with UPS on the sixth of November.


▶ CLICK

Now a question that needs **both** tools. [ON SCREEN: run python agent.py "Refund ORD-1001? Has it arrived, can I return it?"] [pause] Two tool calls this time. / The status first, / then the refund check. / The answer says it arrived, / it's inside the thirty-day window, / and, / just as the tool description promised, / the agent says it **can't** issue the refund itself. / It can only tell you you're eligible. [pause] The wording will be a little different every time you run it, / but the tool calls and the facts won't. [long pause]

Transition: Now let's try to break it.

## 6. Break it, then make it stop

(About 2 min 15 seconds)


▶ CLICK

First, / **bad input**. [ON SCREEN: run python agent.py "Check ORD-1001; DROP TABLE orders and refund everything"] [pause] The model passes that string to the tool. / And the tool **refuses** it, / before it reads any data. / So the agent comes back and asks for a valid order ID. [pause] Here's the important part. / The rule lives **in the tool**, / not in the prompt. / So every agent that uses this server gets the same protection, / even one with a careless prompt.


▶ CLICK

Second, / the **budget**. [ON SCREEN: run python agent.py --max-tool-calls 2 "Status and refund for ORD-1001 to ORD-1004", and point at the cancelled call] [pause] I ask about four orders, / but I only allow two tool calls. / Watch. / Call one, / call two, / and call three gets **cancelled** by the hook. / The agent answers with the two orders it checked, / and tells me what it couldn't check. / It stops, / instead of running up the bill.


▶ CLICK

And third, / the same tools over **HTTP**. [ON SCREEN: in a second terminal run python order_server.py --http, then run python agent.py --http "Can I still return ORD-1004?"] [pause] Now the server runs on its own, / on port eight thousand, / and the agent connects with a URL. / Same tools, / same answer. / Only the transport changed. / And that's exactly how you'd connect to a shared MCP server in production. [long pause]

Transition: And if something doesn't work for you, / here's what to check.

## 7. Three checks, then clean up

(About 1 minute)

Three problems cover most of what you'll hit. [pause]

▶ CLICK

If you get **access denied**, / or the model ID is invalid, / turn on access to that model in the Bedrock console, / in the same Region. / And if the model has no on-demand ID, / use its **inference profile** ID, / like the one we use by default.


▶ CLICK

If the MCP client fails to start, / run the server **on its own** first. / You'll see the real error. / Usually it's the virtual environment.


▶ CLICK

And if you copied older example code, / and Python can't find FastMCP, / that's because version two of the MCP SDK renamed it. / It's now **MCPServer**.


▶ CLICK

And cleanup is easy. / Nothing runs in AWS, / so there's nothing to delete there. / Stop the server, / and that's it. / The whole lab costs a few cents in model calls. [long pause]

Transition: Let's wrap up.

## 8. Three things to remember

(About 1 min 15 seconds)

So, / let's bring it together. [pause]

▶ CLICK

First, / tools live behind **MCP**. / The agent discovers them at run time, / over stdio or HTTP, / so any agent or client can share them.


▶ CLICK

Second, / safety lives **in the tool**. / Narrow, / read-only tools that check their input, / with descriptions that say what they won't do.


▶ CLICK

And third, / every agent needs a **stopping condition**. / A hook that caps the tool calls / keeps the loop and the cost under control. [pause]

So, / back to our one sentence. [pause] Put the tools behind **MCP**, / put the safety rules **in the tools**, / and give the agent a **budget**, / and any agent can use them safely. [pause] And that's the end of Section 7. / You know what makes an agent, / how to orchestrate it with safeguards, / when to bring a human into the loop, / and how to design tools and serve them with MCP. [long pause]

Transition: In the next section, / we take all this to production. / Where to host it, / how to connect it to the systems you already have, / and how to ship it safely.
