# Lecture 6.4: Demo: a versioned prompt in a Prompt Flow — narration script

Section 6, Prompt engineering and governance. About 10 minutes. The same text is in the speaker notes of `lecture-6.4.pptx`. The demo code is in `labs/lab-6.4-prompt-flow`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next. [ON SCREEN: …] = what to show during the live demo.

## 1. A versioned prompt in a Prompt Flow

(About 40 seconds)

In this lecture, / we put everything about prompts into practice. / We store a prompt in **Prompt Management**, / freeze it as a version, / and run it inside a **Prompt Flow** that apps call through an alias. / Then we release a new prompt, / and roll it back, / without touching a line of app code. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] **Version** every prompt, / call it through an **alias**, / and a release becomes one pointer change you can undo. [long pause]

Transition: So, / what are we building?

## 2. From prompt to alias

(About 1 min 30 seconds)

Here's the whole stack. / Four parts in a line, / and one app calling it. [pause]

▶ CLICK

First, / the **prompt**. / It lives in Prompt Management, / not in your code. / It holds the template, / one variable called ticket, / the model, / and its settings. / Our prompt triages support tickets.


▶ CLICK

Second, / **version one** of the prompt. / A frozen copy of that prompt. / Once it's created, / nobody can change it, / not even by accident.


▶ CLICK

Third, / the **flow**. / It's as simple as a flow gets. / An input, / a prompt node that uses prompt version one, / and an output.


▶ CLICK

Fourth, / an **alias** called live. / It points at version one of the flow.


▶ CLICK

And here's the important part. / Your app calls the **alias**. / It never names a prompt, / or a version. / So when you release a new prompt, / the app doesn't change at all. [pause] And again, / it's all one CDK app. [long pause]

Transition: But what exactly is the difference between a version and an alias?

## 3. Draft, version, alias

(About 1 min 15 seconds)

Prompts and flows both work the same way, / with three ideas. [pause]

▶ CLICK

The **draft**. / That's your working copy. / You edit it as often as you like, / and apps never call it.


▶ CLICK

A **version**. / It's a numbered snapshot of the draft. / One, / two, / three. / And it **can't** be edited. / If you want a change, / you change the draft / and create a new version.


▶ CLICK

And an **alias**. / It's just a name that points at one version. / Live points at version one. / Apps call the alias.


▶ CLICK

So a **release** is simple. / You move the alias to the new version. / And a **rollback**? / You move it back. / Nothing is rebuilt, / nothing is redeployed. [long pause]

Transition: So, / what does the code look like?

## 4. Three choices in the CDK app

(About 1 min 15 seconds)

Most of the CDK app is plumbing. / Three choices matter. [pause]

▶ CLICK

First, / we **version the prompt**. / CfnPromptVersion takes a frozen copy of the prompt. / A version can't change under you.


▶ CLICK

Second, / we **pin the prompt node** to that version. / The flow's prompt node points at prompt version one, / exactly. / Not the draft. / So editing the draft can't break production.


▶ CLICK

And third, / we create the **alias**. / Live, / pointing at flow version one. / That's the only thing an app ever calls. [long pause]

Transition: Let's run it.

## 5. Deploy and call the alias

(About 1 min 30 seconds)

Over to the terminal. [ON SCREEN: terminal in the lab folder, virtual environment active, in a Region with Bedrock Prompt Management and Flows] [pause]

▶ CLICK

First, / I deploy the stack. [ON SCREEN: run cdk deploy and show the outputs: PromptId, FlowId, FlowAliasId] [pause] CDK creates the prompt, / prompt version one, / the flow, / flow version one, / and the alias. / The scripts read these outputs themselves, / so there's nothing to copy.


▶ CLICK

Now I call the flow, / the way an app would. [ON SCREEN: run python invoke.py with the broken order ticket, point at the alias line] [pause] The script calls InvokeFlow with the **alias**, / and first it tells us where the alias points. / Version one.


▶ CLICK

And here's the answer. [ON SCREEN: point at the three lines of output] [pause] Three lines. / A summary, / the sentiment, / and the next action. / That's what version one of our prompt asks for. [long pause]

Transition: Now, / let's release a better prompt.

## 6. Release a new prompt, then roll back

(About 2 min)

Our support team wants one more thing. / An **urgency** label, / and shorter answers. / So I've written a new prompt in prompt-v2.txt. [pause]

▶ CLICK

I run the release script. [ON SCREEN: run python release.py prompt-v2.txt and point at each of the four lines it prints] [pause] Watch the order. / One, / it creates **prompt version two**. / Two, / it points the flow's draft at that version, / and prepares the flow. / Three, / it creates **flow version two**. / And only then, / four, / it **moves the alias** from one to two. / Until that last step, / every caller was still on version one.


▶ CLICK

Now the same ticket again. [ON SCREEN: run python invoke.py with the same ticket, point at the alias line and the Urgency line] [pause] The alias points at version **two**, / and the answer has four lines now, / with urgency, / and it's shorter. / Same app, / same call, / new prompt. / And by the way, / the wording will change a little from run to run. / The shape of the answer is what tells you which version ran.


▶ CLICK

And now, / let's say the support team doesn't like it. / We **roll back**. [ON SCREEN: run python rollback.py 1, then invoke.py again] [pause] One command. / The alias points at version one again, / and we're back to three lines. / Nothing was rebuilt. / Version two still exists, / so we can move forward again whenever we want. [long pause]

Transition: And if something doesn't work for you, / here's what to check.

## 7. Three checks, then tear it down

(About 1 min)

Three problems cover most of what you'll hit. [pause]

▶ CLICK

If the deploy fails on the flow, / check the **model ID** is right for your Region, / and that the prompt's variable, / ticket, / matches the prompt node's input.


▶ CLICK

If you get an access denied error, / check that your account can use the **model**. / Some models must be called through an inference profile ID.


▶ CLICK

And if the release script says the flow failed to prepare, / you probably changed the prompt's **variables**. / The node's inputs have to match them. / So keep the ticket variable.


▶ CLICK

And when you're done, / **tear it down**. / Run the cleanup script first, / because it removes the versions that release.py created. / Then run cdk destroy. / The lab only costs a few cents in model calls. [long pause]

Transition: Let's wrap up.

## 8. Three things to remember

(About 1 min 15 seconds)

So, / let's bring it together. [pause]

▶ CLICK

First, / **version everything**. / Prompt versions and flow versions are frozen. / Only drafts change.


▶ CLICK

Second, / apps call an **alias**. / The alias picks the version, / so a release needs no code change.


▶ CLICK

And third, / you release and roll back by **moving the alias**. / New versions first, / then one pointer change. / And you back out the same way. [pause]

So, / back to our one sentence. [pause] **Version** every prompt, / call it through an **alias**, / and a release becomes one pointer change you can undo. [pause] And that's the end of Section 6, / and of Domain 1. / You can design a solution, / choose and run a model, / prepare your data, / build retrieval, / and manage your prompts. [pause] Next comes the Domain 1 checkpoint. / Twenty-five questions to see what's stuck, / and what's worth another look. [long pause]

Transition: Then, / in Section 7, / we move into Domain 2, / starting with agents and the tools they use.
