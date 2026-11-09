# Lecture 11.1: Locking down FM workloads — narration script

Section 11, Security, privacy, governance and responsible AI. About 12 minutes. The same text is in the speaker notes of `lecture-11.1.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Locking down FM workloads

(About 50 seconds)

Welcome to Section 11. / In the last section, / we stopped bad **content**. / Prompt injection, / jailbreaks, / harmful answers. [pause] Now we protect the **workload** itself. / Security, / privacy, / governance / and responsible AI. [pause] And in this first lecture, / we lock down a foundation model workload, / layer by layer. [pause]

If I had to sum it up in one sentence, / it would be this. [pause] There's no single switch that secures a GenAI app. / You stack **layers**, / so that when one fails, / the next one still holds. [long pause]

Transition: So, / what are those layers?

## 2. Six layers between an attacker and your model

(About 1 min 45 seconds)

There are six, / and you'll see all of them in exam scenarios. [pause]

▶ CLICK

First, / the **network**. / VPC endpoints, / powered by PrivateLink, / keep model traffic on the AWS network. / We covered them in Section 8, / so here they're just the first layer.


▶ CLICK

Second, / **identity**. / IAM roles that allow only the calls an app actually needs.


▶ CLICK

Third, / the **organization**. / Service control policies set the outer limit, / for every account at once.


▶ CLICK

Fourth, / **data access**. / Lake Formation decides which data is allowed to feed the model in the first place.


▶ CLICK

Fifth, / **encryption**. / KMS keys that **you** own, / protecting everything at rest.


▶ CLICK

And sixth, / **audit**. / CloudTrail records who did what, / and when. [pause] Keep this picture in mind. / When a question asks for the **most** secure design, / the right answer usually touches more than one of these layers. [long pause]

Transition: Let's go through them, / starting with identity.

## 3. Least privilege for model calls

(About 2 min)

Here's what least privilege looks like for a model call. / It's a normal IAM policy, / and it does three things well. [pause]

▶ CLICK

First, / it **names the actions**. / InvokeModel, / and the streaming version. / That's it. / This role can call a model, / but it can't create a custom model, / start a fine-tuning job / or delete anything.


▶ CLICK

Second, / it **names the models**. / The resource is one specific model ARN. / Not a wildcard on every model in the account. / So if someone changes the app to call a bigger, / more expensive model, / the call simply fails.


▶ CLICK

Third, / it **adds conditions**. / Here, / the call has to come through our own VPC endpoint. / You can also limit the Regions, / with the requested Region condition key. [pause] So even if these credentials leak, / they're useless from outside our network.


▶ CLICK

Two details catch people out. / The Converse API uses the **same** InvokeModel permission, / so there's no separate Converse action to allow. / And if the app calls through an **inference profile**, / the policy has to allow the profile **and** the models it routes to. / Miss the second part, / and you'll get access denied in some Regions but not others. [long pause]

Transition: That's one role in one account. / But what about the whole company?

## 4. Service control policies set the outer limit

(About 1 min 30 seconds)

In a company with hundreds of accounts, / you can't check every IAM policy by hand. / That's what **service control policies** are for. / They live in AWS Organizations, / and they apply to every account below them. [pause]

▶ CLICK

First, / **deny unapproved Regions**. / If your data must stay in Europe, / an SCP blocks every other Region, / whoever the account admin is.


▶ CLICK

Second, / **deny unapproved models**. / Your review board clears a short list of models, / and an SCP denies InvokeModel on everything else.


▶ CLICK

Third, / **deny turning off the audit trail**. / Nobody, / not even an account admin, / can stop CloudTrail or delete the logging setup.


▶ CLICK

And remember the one rule. / An SCP **never grants** anything. / It only sets the maximum. / A role still needs its own IAM policy, / and when the two disagree, / the SCP wins. [long pause]

Transition: Now, / let's talk about the data that feeds the model.

## 5. Control what data reaches the model

(About 1 min 45 seconds)

Here's a risk people miss. / A model can only leak what it was given. / So the question is, / what data reaches it? [pause]

▶ CLICK

It starts with your **data lake in S3**. / Customer records, / support tickets, / documents.


▶ CLICK

On top of it sits **AWS Lake Formation**. / It grants access by database, / table, / column, / and even by row. / So you can say, / this role sees the tickets table, / but not the email column, / and only rows for its own region.


▶ CLICK

Those permissions are attached to tables in the **Glue Data Catalog**, / the one place that describes every table.


▶ CLICK

And then come the **pipelines that read** the data. / Athena queries, / and the jobs that build your RAG documents or your fine-tuning set. / Every one of them goes through Lake Formation.


▶ CLICK

So here's why it matters for GenAI. / **A model can't leak a column it never saw.** / Give the job that builds your Knowledge Base, / or your training set, / a role that sees only the approved tables, / columns / and rows. / Then a clever prompt can't pull out data that was never there. [long pause]

Transition: Next, / encryption.

## 6. Encrypt with keys you control

(About 1 min 45 seconds)

Everything in Bedrock is encrypted at rest by default, / with keys AWS manages. / But many companies need keys **they** control. / That's a **customer managed key** in KMS. / So where do you use one? [pause]

▶ CLICK

**Customized models**. / When you fine-tune a model, / or run continued pre-training, / you can encrypt the resulting model with your own key.


▶ CLICK

**Knowledge Bases and agents**. / The data during ingestion, / the vector store, / and agent session data can all use your key.


▶ CLICK

**Logs**. / Your invocation logs hold full prompts and answers. / So encrypt the CloudWatch log group, / and the S3 bucket, / with your key.


▶ CLICK

And your **source data** in S3. / Training data / and the documents behind your Knowledge Base.


▶ CLICK

Here's the reason it matters. / A customer managed key is a **second lock**. / Even someone who can reach the data / can't read it unless the **key policy** lets them decrypt. / And you can disable the key, / or see every use of it in CloudTrail. [long pause]

Transition: Which brings us to the last layer. / Audit.

## 7. Record every call with CloudTrail

(About 1 min 45 seconds)

If something goes wrong, / you need to answer one question fast. / Who did this? [pause]

▶ CLICK

**CloudTrail** records every Bedrock API call. / Which role, / which action, / when, / and from where, / including which VPC endpoint.


▶ CLICK

For some runtime calls, / like agent and Knowledge Base calls, / CloudTrail treats them as **data events**. / Those aren't recorded until you turn them on. / So if your audit needs them, / enable them on purpose.


▶ CLICK

Now, / a common exam trap. / CloudTrail does **not** hold the prompts and answers. / For the actual text, / you need **model invocation logging**, / which we set up back in Section 6. / CloudTrail says who called the model. / Invocation logging says what was said.


▶ CLICK

And finally, / keep it **tamper-proof**. / Send your trails to a separate log archive account, / and turn on S3 Object Lock. / Then not even an attacker with admin rights in the workload account / can quietly delete the evidence. [long pause]

Transition: Let's wrap up.

## 8. Lecture recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / security is **six layers**, / not one. / Network, / identity, / organization, / data access, / encryption / and audit.


▶ CLICK

Second, / start with **least privilege**, / then set a limit. / Name the actions, / the models / and the conditions. / And let SCPs cap every account.


▶ CLICK

And third, / **own the keys, / keep the trail**. / KMS keys you control, / and CloudTrail in a locked archive account. [pause]

So, / back to our one sentence. [pause] There's no single switch that secures a GenAI app. / You stack **layers**, / so that when one fails, / the next one still holds. [long pause]

Transition: Next, / we zoom in on one kind of data that needs extra care. / Personal information.
