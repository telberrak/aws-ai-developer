# Lecture 8.3: Secure access, data residency and hybrid — narration script

Section 8, Deployment and enterprise integration. About 12 minutes. The same text is in the speaker notes of `lecture-8.3.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Secure access, data residency and hybrid

(About 40 seconds)

In the last lecture, / we connected generative AI to the systems you already run. / Now we lock it down. [pause] Three questions. / **Who** gets in? / **Where** does the data stay? / And what do you do when the model has to run **outside** an AWS Region? [pause]

If I had to sum it up in one sentence, / it would be this. [pause] Give every user a proper **identity**, / keep the traffic **private**, / and decide **where** the data lives before you build. [long pause]

Transition: So, / who are your users?

## 2. Two kinds of users, two front doors

(About 1 min 30 seconds)

There are two kinds of users, / and each one gets its own front door. [pause]

▶ CLICK

First, / your **workforce**. / Your employees and contractors. / For them, / you use **AWS IAM Identity Center**. / They sign in once with your corporate directory, / permission sets map their groups to roles, / and they get short-lived credentials. / No IAM users, / and no access keys sitting on laptops.


▶ CLICK

Second, / your **customers**. / People signing up in your web or mobile app. / For them, / you use **Amazon Cognito**. / User pools handle sign-up and sign-in. / Your API checks the token, / for example with a Cognito authorizer in API Gateway. / And if the app really needs to call AWS directly, / identity pools can swap that token for temporary AWS credentials.


▶ CLICK

And here's the part that ties it together. / Either way, / an **IAM role** is what actually calls Bedrock. / Users never hold long-lived keys, / and the role allows only the models that app needs. / So if you see a question where an app stores access keys in its code, / that's the wrong answer. [long pause]

Transition: Next, / how does the request reach the model?

## 3. Keep model traffic off the internet

(About 1 min 30 seconds)

By default, / your app calls Bedrock on its public endpoint. / Encrypted, / yes, / but over the internet. / Many companies don't allow that. [pause]

▶ CLICK

So, / first, / your app runs in a **VPC**, / in private subnets. / It doesn't even need an internet gateway.


▶ CLICK

Second, / you create a **VPC endpoint** for Bedrock. / It's an interface endpoint, / powered by **AWS PrivateLink**, / and you create one for each Bedrock API you use. / The runtime API for model calls, / and the agent runtime API for Knowledge Bases and agents.


▶ CLICK

Third, / **Amazon Bedrock** receives the request, / and the traffic never leaves the AWS network.


▶ CLICK

Then you lock it down in three layers. [pause] An **endpoint policy** says which principals and models can use this endpoint. / An **IAM policy** says which actions and model ARNs each role can call. / And **condition keys** let you deny any call that doesn't come through your endpoint. / That last one is what turns "we have a private path" into "the private path is the only path". [long pause]

Transition: Now, / where does the data actually go?

## 4. Decide where the data is processed and stored

(About 2 min)

Data residency comes up in almost every regulated project. / Here are the four decisions. [pause]

▶ CLICK

First, / **pick the Region**. / Bedrock processes the request in the Region you call. / And it doesn't store your prompts or answers, / or use them to train the models.


▶ CLICK

Second, / if you need more capacity, / use a **geographic inference profile**. / A US, / EU / or APAC profile spreads the load across several Regions, / but it stays inside that geography. [pause] Be careful with a **global** profile, / though. / It can route the request anywhere in the world. / So if residency matters, / don't use it.


▶ CLICK

Third, / keep **your own data** local. / Your invocation logs, / your Knowledge Base sources / and your vector store all live in buckets and stores that **you** place. / So put them in the same Region.


▶ CLICK

Fourth, / **enforce** it. / With AWS Organizations, / a service control policy can deny the Regions you don't use. / One catch. / If you use a geographic profile, / allow the Regions it routes to, / or your calls will fail.


▶ CLICK

So, / when a question says "data must stay in the EU", / the answer has three parts. / An **EU Region**, / an **EU inference profile**, / and an **SCP** that blocks the rest. [long pause]

Transition: But what if the data can't go to a Region at all?

## 5. When it has to run outside the Region

(About 2 min)

Sometimes the model has to run **outside** a Region. / AWS gives you three ways to get there. [pause]

▶ CLICK

First, / **AWS Outposts**. / AWS racks or servers in **your own** data center. / You use it when the data can't leave the site, / like a factory, / a hospital, / or a bank's own data center.


▶ CLICK

Second, / **AWS Local Zones**. / AWS infrastructure close to a large city, / for very low latency to the users there.


▶ CLICK

Third, / **AWS Wavelength**. / AWS compute inside a 5G carrier network, / so you get the lowest latency to mobile devices.


▶ CLICK

Now here's the catch. [pause] **Bedrock runs only in AWS Regions.** / It doesn't run on Outposts, / in Local Zones / or in Wavelength. / So you have two options. [pause] Option one, / **self-host an open-weight model** on GPU instances at the edge, / where those instances are offered. / You manage the model yourself. [pause] Option two, / keep the **data** on site, / and call Bedrock **privately**. / Direct Connect or a VPN into your VPC, / and then the VPC endpoint we just saw. [pause] If the data can leave the building but not the network, / that's option two. / If nothing can leave, / that's option one. [long pause]

Transition: Let's practice reading these constraints.

## 6. Read the constraint, pick the service

(About 2 min)

Exam questions give you a constraint, / and you match it to a service. / Here are six you'll see. [pause]

▶ CLICK

Employees sign in with the corporate directory? / **IAM Identity Center**.


▶ CLICK

Customers sign up in a mobile app? / **Amazon Cognito**.


▶ CLICK

No model traffic over the public internet? / An **interface VPC endpoint** for Bedrock.


▶ CLICK

Data must stay in one geography? / The **Region**, / a **geographic** inference profile, / and an **SCP**.


▶ CLICK

Data can't leave the factory? / A **self-hosted model on Outposts**.


▶ CLICK

And the lowest latency for 5G devices? / **Wavelength**. [pause] Notice that the constraint word does all the work. / "Corporate directory", / "public internet", / "can't leave". / Find that word, / and the answer follows. [long pause]

Transition: Let's wrap up.

## 7. Lecture recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / two front doors. / IAM Identity Center for your people, / Cognito for your customers, / and IAM roles behind both.


▶ CLICK

Second, / private and in place. / VPC endpoints keep the traffic private. / The Region, / geographic profiles / and SCPs keep the data where it belongs.


▶ CLICK

And third, / the edge means self-hosting. / Outposts, / Local Zones / and Wavelength run **your own** model, / or connect privately back to Bedrock. [pause]

So, / back to our one sentence. [pause] Give every user a proper **identity**, / keep the traffic **private**, / and decide **where** the data lives before you build. [long pause]

Transition: Next, / we look at how you ship changes safely, / and how one gateway can sit in front of every model.
