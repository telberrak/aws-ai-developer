# Lecture 3.6: Demo: a model router with AppConfig — narration script

Section 3, Designing solutions and choosing models. About 10 minutes. The same text is in the speaker notes of `lecture-3.6.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next. [ON SCREEN: …] = what to show during the live demo.

## 1. A model router with AppConfig

(About 40 seconds)

In this lecture, / we build something you'll reuse in every project. / A **model router**. / One API in front of Bedrock, / where the model choice lives in configuration, / not in code. [pause] Then we'll switch models live, / try a bad change, / and roll back. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Keep the model choice in **configuration**, / and switching models becomes a deployment, / not a code change. [long pause]

Transition: So, / what are we building?

## 2. One API, model choice in configuration

(About 1 min 30 seconds)

Here's the whole stack. / Four parts in a line, / and one on the side. [pause]

▶ CLICK

First, / your **apps**. / Every app calls one internal endpoint. / They don't know, / or care, / which model answers.


▶ CLICK

Second, / **API Gateway**. / It handles authentication and throttling, / and it gives every app one stable contract.


▶ CLICK

Third, / the **Lambda router**. / It reads the configuration, / picks the model for the use case, / and makes the call.


▶ CLICK

Fourth, / **Bedrock**, / through the Converse API. / And because Converse has the same request shape for every model, / a model ID is all it takes to switch.


▶ CLICK

And on the side, / **AWS AppConfig**. / It holds the model ID and its settings, / and the router reads them at run time. [pause] The whole thing is one CDK app, / so you deploy it with one command. [long pause]

Transition: But why AppConfig? / Why not just an environment variable?

## 3. Not just an environment variable

(About 1 min 30 seconds)

Good question. / An environment variable would work. / But AppConfig gives you four things it can't. [pause]

▶ CLICK

It's **validated**. / A JSON schema, / or a Lambda validator, / rejects a bad configuration before it ever reaches production.


▶ CLICK

It's **rolled out gradually**. / A deployment strategy can release a new configuration to a share of traffic, / over time.


▶ CLICK

It's **rolled back automatically**. / Attach a CloudWatch alarm to the environment, / and if errors go up during a deployment, / AppConfig rolls it back for you.


▶ CLICK

And there's **no redeploy**. / Changing a Lambda environment variable updates the function itself. / Changing AppConfig doesn't touch the function at all. [pause] So when you see "switch models without code changes", / this is the pattern to think of. [long pause]

Transition: Now, / let's read the code.

## 4. Read the config, then call

(About 1 min 30 seconds)

There are two pieces. / The configuration, / and the router that reads it. [pause]

▶ CLICK

First, / the **configuration profile**. / It's plain JSON. / A default route with a model ID, / a temperature / and max tokens. / And you can add a route per use case, / like summarize, / which could use a smaller, / cheaper model.


▶ CLICK

Then, / the router reads it with **get config**. / And notice it's cached. / The router only asks AppConfig for news every fifteen seconds, / so it's fast and cheap.


▶ CLICK

Next, / it **picks the route**. / The use case from the request, / or the default if there isn't one.


▶ CLICK

And finally, / **one Converse call**, / with whatever model and settings the route says. / That's the line that never changes, / no matter which model you switch to. [long pause]

Transition: OK, / let's deploy it and switch some models.

## 5. Deploy, call, switch, roll back

(About 3 min)

[ON SCREEN: terminal in the lab folder, virtual environment active, with two model IDs ready that your account can use] [pause]

▶ CLICK

First, / I deploy the stack with my first model ID. [ON SCREEN: run cdk deploy with the first model ID, then copy the ChatUrl output] [pause] CDK creates the API, / the Lambda function / and the AppConfig profile. / And at the end, / it prints the URL of the chat API.


▶ CLICK

Now I call it. [ON SCREEN: run the curl command and point at modelId in the response] [pause] Look at the response. / There's the answer, / the token usage, / and the **model ID** that answered. / That's our first model.


▶ CLICK

Now the interesting part. / I switch to my second model. [ON SCREEN: run switch_model.sh with the second model ID, then call the API every few seconds] [pause] The script creates a new configuration version, / and deploys it through AppConfig. / I haven't touched the code, / and I haven't redeployed the stack. [pause] And within about fifteen seconds, / which is the router's cache, / the model ID in the response changes. / Same code, / new model.


▶ CLICK

And now, / let's break it on purpose. [ON SCREEN: set maxTokens to 99999 in switch_model.sh and run it, show the validation error, then run switch_model.sh with the first model ID] [pause] The schema validator **rejects** that version, / and production keeps working with the last good one. / Then I roll back to my first model, / with the same one command. [long pause]

Transition: And if something doesn't work for you, / here's what to check.

## 6. Three checks, then tear it down

(About 1 min)

Three problems cover most of what you'll hit. [pause]

▶ CLICK

If CDK complains about a missing bootstrap stack, / your account and Region were never **bootstrapped**. / Run cdk bootstrap once, / then deploy again.


▶ CLICK

If the API returns an access denied error from Bedrock, / check that **model access** is on for that model in your Region.


▶ CLICK

And if the model ID doesn't change after a switch, / give it a moment. / The router caches the configuration for fifteen seconds, / and the AppConfig deployment has to finish first.


▶ CLICK

And when you're done, / **tear it down**. / Run cdk destroy. / The lab only costs a few cents in model calls, / but don't leave anything running. [long pause]

Transition: Let's wrap up.

## 7. Recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / one router API in front of Bedrock. / Every app calls the same endpoint, / and the Converse API makes every model look the same.


▶ CLICK

Second, / the model choice lives in AWS AppConfig. / It's validated, / rolled out gradually, / and rolled back automatically, / with no redeploy.


▶ CLICK

And third, / switching models is now a **deployment**. / A new config version, / a quick test, / and a rollback if you need it. [pause]

So, / back to our one sentence. [pause] Keep the model choice in **configuration**, / and switching models becomes a deployment, / not a code change. [pause] And that's the end of Section 3. / You can turn requirements into a design, / choose a model with evidence, / keep it running when things fail, / and customize it safely. [long pause]

Transition: In the next section, / we move to the data. / Data pipelines, / and the vector stores that power RAG.
