# Lecture 11.2: Protecting PII — narration script

Section 11, Security, privacy, governance and responsible AI. About 10 minutes. The same text is in the speaker notes of `lecture-11.2.pptx`.

> Delivery marks: **bold** = stress · / = brief pause · [pause] = 1 second · [long pause] = 2 to 3 seconds. ▶ CLICK = advance to the next build. "Transition:" is the spoken bridge into what comes next.

## 1. Protecting PII

(About 40 seconds)

In the last lecture, / we locked down the workload. / Now we zoom in on one kind of data that needs extra care. / **Personal information**, / or PII. / Names, / emails, / phone numbers, / card numbers. [pause]

Here's the one sentence for this lecture. [pause] **Find** the personal data, / **mask** it or **tokenize** it, / and **don't keep it** longer than you need. [long pause]

Transition: So, / where does PII actually show up in a GenAI app?

## 2. Four places personal data turns up

(About 1 min 30 seconds)

More places than people expect. / There are four. [pause]

▶ CLICK

First, / your **source documents**. / The support tickets, / contracts / and emails you load into a Knowledge Base. / They're full of names and phone numbers.


▶ CLICK

Second, / **prompts**. / You can't control what users type. / Someone will paste their email address, / or their card number, / straight into the chat box.


▶ CLICK

Third, / **answers**. / The model repeats what it read in the documents, / or what the user just told it.


▶ CLICK

And fourth, / **logs**. / If you turned on invocation logging, / every full prompt and every full answer is stored. / That's a lot of personal data in one place.


▶ CLICK

So you need to protect **all four**. / Cleaning your source data is great, / but it doesn't help if a user types their card number into the prompt, / and your log keeps it for years. [long pause]

Transition: First, / how do you find it?

## 3. Comprehend cleans text, Macie scans buckets

(About 1 min 45 seconds)

Two services detect PII, / and the exam loves to mix them up. / The difference is **where** the data is. [pause]

▶ CLICK

**Amazon Comprehend** works on **text in flight**. / You give it a piece of text, / and it tells you every PII entity, / its type, / and exactly where it sits in the text. / It can also redact it for you, / either masking it with a character, / or replacing it with the entity type, / like the word NAME. / You can call it in real time, / or run a batch job over documents in S3.


▶ CLICK

**Amazon Macie** works on **data at rest** in S3. / It scans your buckets and discovers where sensitive data lives. / It uses managed data identifiers, / and you can add your own. / It also flags buckets that are public or unencrypted. / And its findings go to Security Hub and EventBridge, / so you can alert or fix things automatically.


▶ CLICK

So here's the easy way to remember it. / **Macie finds the bucket. / Comprehend cleans the text.** / Use Macie to find out where PII lives, / and Comprehend to strip it out before it reaches the model, / for example while you prepare documents for a Knowledge Base. [long pause]

Transition: But what about PII in live prompts and answers?

## 4. Guardrails sensitive information filters

(About 1 min 30 seconds)

That's where Guardrails come in. / We met Guardrails in the last section. / Here we use one specific policy, / the **sensitive information filter**. [pause]

▶ CLICK

It comes with **built-in PII types**. / Names, / emails, / phone numbers, / addresses, / card numbers, / account numbers / and many more. / You pick the ones you care about.


▶ CLICK

For each type, / you choose an action. / **Block** the whole message, / or **mask** the value. / Masking swaps the value for a tag, / like EMAIL in curly braces, / and lets the rest of the answer through.


▶ CLICK

You set that action for the **prompt**, / the **answer**, / or both. / So you might mask an email in the user's prompt, / and block any answer that contains a card number.


▶ CLICK

And you can add **your own patterns**, / with regular expressions. / That's for IDs only your business uses, / like a policy number or an internal customer ID. [pause] Because the filter runs on every call, / it protects prompts and answers, / not just your stored data. [long pause]

Transition: Now, / masking is just one way to hide a value.

## 5. Redact, mask or tokenize

(About 1 min 45 seconds)

There are three, / and choosing the right one is a common exam question. [pause]

▶ CLICK

**Redact** means remove it for good. / The value is gone, / and you can't get it back. / Use it when nobody needs the value later. / Summaries, / analytics, / and training data.


▶ CLICK

**Mask** means hide all or part of it. / A card number showing only the last four digits. / The person on screen can confirm it's the right card, / without seeing the whole number.


▶ CLICK

**Tokenize** means swap the value for a token / that you can turn back into the real value later. / The real value is stored somewhere safe, / and only a trusted service can look it up.


▶ CLICK

So here's the rule. / **Tokenize when a later step needs the real value.** / Say an agent processes a refund. / The model only ever sees the token. / Then a separate, / locked-down service swaps it back / and sends the refund to the real account. / The model never touched the real number. [long pause]

Transition: And the last piece of privacy, / is how long you keep things.

## 6. Don't keep it longer than you need

(About 1 min 45 seconds)

The safest personal data is the data you no longer have. [pause]

▶ CLICK

In S3, / use **lifecycle rules**. / Move old source data and invocation logs to colder storage, / and then expire them after a set time.


▶ CLICK

In CloudWatch Logs, / set a **retention period** on every log group. / Here's the catch. / The default is to keep logs **forever**. / So if you never set it, / those prompts stay there for good.


▶ CLICK

For chat history and session memory in DynamoDB, / use **TTL**, / time to live. / Each item gets an expiry time, / and DynamoDB deletes it for you.


▶ CLICK

And when someone asks you to delete their data, / don't stop at the source file. / Delete it, / and then **sync the Knowledge Base**, / so the vectors built from it go too. / Otherwise the model can still find it.


▶ CLICK

So remember. / **Data you deleted can't leak.** / Retention isn't just about the storage bill. / It's a privacy control. [long pause]

Transition: Let's wrap up.

## 7. Lecture recap

(About 1 min)

So, / let's bring it together. [pause]

▶ CLICK

First, / PII hides in **four places**. / Source documents, / prompts, / answers / and logs. / Protect all four.


▶ CLICK

Second, / **find it, / then clean it**. / Macie scans your buckets. / Comprehend and Guardrails clean the text.


▶ CLICK

And third, / **keep only what you need**. / Tokenize when you need the value back, / and let the rest expire. [pause]

So, / back to our one sentence. [pause] **Find** the personal data, / **mask** it or **tokenize** it, / and **don't keep it** longer than you need. [long pause]

Transition: Next, / we step back from single controls, / and look at governance. / How do you prove your AI system is under control?
