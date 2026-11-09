# Lecture 6.1: Instruction frameworks, Prompt Management and conversation context — narration script

Section 6, Prompt engineering and governance. About 10 minutes. The same text is in the speaker notes of `lecture-6.1.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Instruction frameworks, Prompt Management and context

(About 50 seconds)

Welcome to Section 6, / the last section on data and models. / We've chosen a model, / and we've built the retrieval that feeds it. / Now we look at the thing you send it every single time. / The **prompt**. [pause] In this lecture, / you'll see how to structure a prompt, / where to keep it so it isn't buried in your code, / and how to carry a conversation across many turns. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Give every prompt a **clear structure**, / keep it in **Prompt Management** instead of your code, / and remember that **you** carry the conversation, / not the model. [long pause]

Transition: So, / what does a well-built prompt actually contain?

## 2. A good prompt has six parts

(About 1 min 40 seconds)

Most good prompts have the same six parts. [pause]

▶ CLICK

First, / the **role**. / Who the model is. / "You are a claims assistant for an insurance company." / It sets the tone and the expertise.


▶ CLICK

Second, / the **task**. / One clear job. / "Summarize this claim." / If you ask for three things at once, / you'll usually get two of them done well.


▶ CLICK

Third, / the **context**. / The facts it needs to do the job. / The retrieved documents, / the customer's data, / today's date.


▶ CLICK

Fourth, / the **constraints**. / What it must do, / and what it must never do. / "Answer only from the documents. / If you don't know, / say so."


▶ CLICK

Fifth, / the **output format**. / The exact shape you want back. / JSON with these fields, / or three bullet points, / or under a hundred words. / If code reads the answer, / this part matters most.


▶ CLICK

And sixth, / **examples**. / One or two worked answers. / A model copies an example far more reliably / than it follows a description. [long pause]

Transition: So, / where does each of those parts go?

## 3. System prompt, user message, examples

(About 1 min 20 seconds)

You've got three places to put them. [pause]

▶ CLICK

The **system prompt**. / This is where the role, / the constraints / and the output format go. / It's the same on every call, / so you set it once.


▶ CLICK

The **user message**. / This carries the task and the context for **this** request. / It changes every time.


▶ CLICK

And the **few-shot examples**. / Pairs of input and ideal output. / You can put them in the prompt itself, / or as earlier turns in the conversation, / so the model sees them as answers it already gave. / They **show** the model what you want, / instead of telling it.


▶ CLICK

One more tip. / Make the parts **easy to find**. / Label each section, / or wrap it in tags like context and rules. / The model handles a clearly marked prompt much better / than one long paragraph where the instructions are hidden in the middle. [long pause]

Transition: Now, / where should all this prompt text live?

## 4. Keep prompts out of your code

(About 1 min 40 seconds)

Not in your code. / That's what **Amazon Bedrock Prompt Management** is for. [pause] A prompt there holds four things. [pause]

▶ CLICK

First, / the **template**. / The prompt text, / with variables in double curly braces, / like claim text. / Your app fills them in at run time.


▶ CLICK

Second, / the **model and its settings**. / The model ID, / the temperature, / the maximum tokens. / They're stored **with** the prompt, / because a prompt that works on one model / doesn't always work on another.


▶ CLICK

Third, / **variants**. / Different wordings, / or different models, / that you can run side by side in the console / and compare before you pick one.


▶ CLICK

And fourth, / **versions**. / When you're happy, / you create a version. / It's a numbered snapshot, / and it can't be changed.


▶ CLICK

So how does your app use it? / It calls the **Converse API**, / and instead of a model ID, / it passes the prompt version's **ARN**, / plus the values for the variables. / Bedrock fills in the template, / applies the settings, / and calls the model. [pause] There's no prompt text in your code at all. / So changing the prompt / doesn't mean changing the app. [long pause]

Transition: That covers one request. / But what about a whole conversation?

## 5. The model remembers nothing between calls

(About 1 min 40 seconds)

Here's the thing people forget. / The model **remembers nothing** between calls. [pause]

▶ CLICK

The Converse API is **stateless**. / To hold a conversation, / every call has to carry the earlier turns / in the messages list. / The model only "remembers" what you send it again.


▶ CLICK

But you can't send everything forever. / So you **keep a window**. / Only the last few turns, / so you stay inside the context limit.


▶ CLICK

And for the older turns, / you **summarize**. / Ask a model to write a short summary of what's been said, / and send that instead. / The details fade, / but the important facts stay.


▶ CLICK

And you **store** it. / Your app needs somewhere to keep the turns between requests. / A common choice is **DynamoDB**, / keyed by session ID, / so any instance of your app can pick up the conversation.


▶ CLICK

And remember the cost. / Every turn you resend is **input tokens** you pay for again. / A long history makes every call slower / and more expensive. / So trim it **on purpose**, / don't just let it grow. [long pause]

Transition: Let's wrap up.

## 6. Lecture recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / six parts, / three places. / Role, / task, / context, / constraints, / format / and examples, / split across the system prompt, / the user message / and a few examples.


▶ CLICK

Second, / prompts live in **Prompt Management**. / Templates with variables, / the model settings, / variants / and versions, / and your app calls them by ARN.


▶ CLICK

And third, / **you** carry the conversation. / Resend the history, / keep a window, / summarize the old turns, / and store them per session. [pause]

So, / back to our one sentence. [pause] Give every prompt a **clear structure**, / keep it in **Prompt Management** instead of your code, / and remember that **you** carry the conversation, / not the model. [long pause]

Transition: Next, / we make sure nobody can break a prompt by accident. / Prompt governance, / and how to test every change.
