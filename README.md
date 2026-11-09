# AWS AI Developer: AIP-C01 course repo

Course materials for a Udemy course that prepares learners for the **AWS Certified Generative AI Developer - Professional (AIP-C01)** exam.

## What's here

| Path | What it is |
| --- | --- |
| `docs/course-blueprint.md` | Full course structure: 26 sections mapped to every exam task and skill, labs, quizzes, practice exams, study plan |
| `docs/AIP-C01-exam-guide.pdf` | The official AWS exam guide the course is built from |
| `slides/section-01-welcome-and-exam-strategy.pptx` | Section 1 slides (24 slides), narration in the speaker notes |
| `slides/section-01-script.md` | Section 1 narration script, one block per slide |
| `slides/section-02-genai-on-aws-refresher.pptx` | Section 2 slides (22 slides), narration in the speaker notes |
| `slides/section-02-script.md` | Section 2 narration script, one block per slide |
| `labs/lab-00-first-bedrock-call/` | Lab 0: first Bedrock Converse call from Python and the AWS CLI |
| `quizzes/section-02-quiz.md` | Section 2 quiz, 10 questions with explanations |
| `slides/section-03-designing-genai-solutions.pptx` | Section 3 slides (21 slides), narration in the speaker notes |
| `slides/section-03-script.md` | Section 3 narration script, one block per slide |
| `labs/lab-01-genai-lens-review/` | Lab 1: Generative AI Lens review of a sample design in the Well-Architected Tool |
| `quizzes/section-03-quiz.md` | Section 3 quiz, 10 questions with explanations |
| `slides/section-04-selecting-and-configuring-fms.pptx` | Section 4 slides (27 slides), narration in the speaker notes |
| `slides/section-04-script.md` | Section 4 narration script, one block per slide |
| `labs/lab-02-model-router/` | Lab 2: model router with AWS AppConfig (CDK, Python) |
| `labs/lab-03-circuit-breaker/` | Lab 3: Step Functions circuit breaker with cross-Region failover (CDK, Python) |
| `quizzes/section-04-quiz.md` | Section 4 quiz, 12 questions with explanations |
| `setup/README.md` | Lab account setup guide (Lecture 1.5) |

## Status

| Section | Slides | Script | Labs | Quiz |
| --- | --- | --- | --- | --- |
| 1. Welcome and exam strategy | Done | Done | n/a | Diagnostic test to write |
| 2. GenAI on AWS refresher | Done | Done | Lab 0 done | Done |
| 3. Designing GenAI solutions | Done | Done | Lab 1 done | Done |
| 4. Selecting and configuring FMs | Done | Done | Labs 2 and 3 done | Done |
| 5 to 26 | To do | To do | To do | To do |

## Conventions

- Slides go in `slides/`, named `section-NN-<short-title>.pptx`, with a matching `section-NN-script.md`.
- Quizzes go in `quizzes/`, named `section-NN-quiz.md`.
- Labs go in `labs/lab-NN-<short-title>/`, each with a README, estimated cost and a teardown command.
- Every lecture, lab and question is tagged with its exam skill ID (for example `1.5.4`).
