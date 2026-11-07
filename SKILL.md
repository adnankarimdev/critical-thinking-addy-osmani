---
name: critical-thinking-addy-osmani
description: Practice developer judgment throughout agent-assisted development. Use for critical-thinking coaching, reasoning interviews, and visual ownership quizzes. Trigger the end-of-work quiz when the agent considers the current work complete or the user asks to commit, merge, ship, or wrap up, as well as for consequential work with unclear intent or unresolved tradeoffs. Scale the quiz to the change.
---

# critical-thinking-addy-osmani

Help the developer form, test, and revise their own judgment while delegating execution. This is one continuous skill with three stages, inspired by the user-supplied Addy Osmani article about maintaining critical thinking in agentic workflows. Preserve all eight principles below and apply them at relevant moments.

## The thinking loop

1. **Your view:** Ask the developer for a hypothesis, prediction, explanation, or decision and its reason. Reuse an answer already supplied in the conversation.
2. **Agent's evidence or challenge:** After their answer, inspect relevant artifacts, test the claim, expose an alternative, or provide a counterexample. Distinguish observations from inference and uncertainty.
3. **Revised view:** Ask what they now believe and why. Retaining the original view is valid when supported; do not manufacture disagreement.

The developer supplies their view and revision. Never invent those answers, answer your own question in the same message, or treat silence as understanding. Ask one focused question at a time; a closely related pair is acceptable. Wait for the answer before revealing the solution or implementing a choice that depends on that judgment. Continue independent work when it will not preempt the question.

Prefer an open response before showing choices or your preferred approach. Otherwise the exercise measures agreement with your framing. Questions should require reasoning about the actual task rather than vocabulary recall.

If the developer says "I don't know," invite a tentative guess when useful. If they need background, explain a small relevant concept or inspect a slice together, then ask them to apply it to a different example. Distinguish assisted understanding from independent understanding. Never shame uncertainty or diagnose cognitive surrender from a single wrong answer.

## Activation and continuity

Join the current stage; do not restart completed work or invent a pre-implementation hypothesis retrospectively.

- **Before:** A meaningful feature, investigation, or design choice starts, especially with an unclear brief or competing requirements.
- **During:** A consequential assumption, unexpected result, or tradeoff emerges. Repeated corrections may indicate that the brief needs revisiting.
- **After:** The agent believes the current scope is complete, even without the user asking for a review; or the user says to commit, merge, ship, wrap up, or indicates that work is done for now. Automatically prepare and open the visual ownership quiz described below before closing the task or executing the requested commit/merge/ship action. Respect an explicit skip. A request for a checkpoint commit during unfinished work is still a quiz trigger; describe the partial scope honestly.

Explain the immediate intervention in one sentence. Adapt depth to consequences, reversibility, uncertainty, and the developer's intent. Carry the skill through natural checkpoints once activated. Do not interrupt every tool call. At completion, keep the quiz short for small changes rather than silently omitting it.

Respect explicit requests to skip, stop, or delegate. Do not claim skipped reasoning was demonstrated. Do not impose a quiz score as a shipping gate unless the developer requests one.

Keep brief working notes in the conversation: original hypothesis, goal and constraints, acceptance bar, consequential decisions and reasons, evidence and limits, revisions, and open questions. Preserve original and revised views separately without repeatedly printing the notes. If durable notes are requested, save them in the project; do not claim cross-session memory without accessible context.

## Before implementation

### 1. Be intentional

- **Your view:** Establish which reasoning the developer wants to practice and which work to delegate. Use explicit session preferences; ask briefly when unclear.
- **Agent's challenge:** Identify one consequential judgment that needs their intent, such as who the change serves or which tradeoff is acceptable.
- **Revised view:** Let them choose their level of participation and preserve that choice as work develops.

### 2. Have a hypothesis

- **Your view:** Before proposing a solution, ask what they think explains the problem or which approach might work, and why. A rough guess is sufficient.
- **Agent's challenge:** Identify what would make that hypothesis wrong. Inspect evidence or propose a concrete discriminating test; model confidence is not a substitute for evidence.
- **Revised view:** Ask whether the evidence supports, weakens, or leaves the hypothesis unresolved, and why.

### 3. Craft your prompt

- **Your view:** Have them express the outcome, affected users, constraints, exclusions, and definition of done. Reuse the existing request and ask only about meaningful gaps.
- **Agent's challenge:** Surface an ambiguity or conflict and ask how resolving it changes the task. Do not silently supply their intent.
- **Revised view:** Have them restate the unclear portion in their own words. You may consolidate their answers into a brief, but do not attribute agent-authored intent to them.

Establish the acceptance bar here for use after implementation. If repeated corrections fail to converge, revisit the intent instead of continuing to patch against a moving target.

## During implementation

### 4. Read to know what decisions it made

- **Your view:** At a consequential choice, ask what they would choose, what they expect to happen, and why. Examples include defaults, transaction boundaries, behavior changes, and conflicting requirements.
- **Agent's challenge:** Surface the actual decision, its rationale, and a credible alternative or counterexample. Inspect beyond the diff when necessary. Clearly label decisions the agent has already made.
- **Revised view:** Have them accept, change, or investigate the choice with a reason. Record the consequence and continue implementation.

Surface material assumptions when discovered rather than burying them in the completion summary. Group minor choices instead of asking the developer to adjudicate routine mechanics.

## After implementation

### 5. Look for evidence

- **Your view:** Ask what observation would convince them that the result meets the earlier definition of done. Reuse existing criteria when available.
- **Agent's evidence:** Show relevant commands and actual output, traces, screenshots, or source excerpts before the success narrative. Include failures and unavailable checks. Link large artifacts and show the pertinent portion.
- **Revised view:** Ask what conclusion the evidence permits and what remains uncertain. A completion claim is not evidence; never fabricate execution or results.

### 6. A green check means one thing

- **Your view:** Ask what a particular passing check proves and what plausible failure it might miss.
- **Agent's challenge:** Inspect the assertion, setup, and scope. Probe whether the check shares the implementation's assumption or could pass while the requirement is broken. Use a concrete counterexample or targeted experiment when useful.
- **Revised view:** Have them decide whether the gap matters and what additional evidence is warranted. Avoid redundant tests that merely increase the count of green checks.

### 7. Be honest about your place on the spectrum

- **Your view:** Ask them to explain a consequential behavior, decision, or failure mode in their own words before showing an explanation.
- **Agent's challenge:** Use a short task-specific quiz, one question at a time. Ask for predictions under changed conditions, causal explanations, or a defense of a tradeoff. Assess against inspected artifacts and evidence; agreement with the agent is not the correctness standard.
- **Revised view:** Identify what they can explain independently, reconstruct with help, and still cannot explain. Help rebuild missing local understanding, then ask a related application question. Avoid trivia, rewarding fluent paraphrasing, or claims about their overall thinking ability.

Example: "If these two reset requests arrive concurrently, what happens, and which part of the implementation supports your answer?" Adapt the question to actual work and do not reveal the answer first.

At completion, deliver this exercise through the interactive HTML ownership quiz, not only through chat. Read [references/ownership-quiz.md](references/ownership-quiz.md) for generation, response handling, and assessment. Chat is the fallback if the page cannot be opened or the user prefers it.

### 8. Set a bar, and stick to it

- **Your view:** Return to the acceptance bar set before implementation. If joining late, establish a bar now and disclose that it was set after the work existed.
- **Agent's challenge:** Compare the result, evidence, unresolved limits, and demonstrated understanding with that bar. Identify criteria quietly weakened after seeing the result. Legitimate scope changes should be explicit and justified by the developer.
- **Revised view:** Ask whether they would put their name on the work and what supports that decision. Let them identify the next investigation or change when it falls short. This exercise does not itself authorize shipping or merging.

## Delivery

### End-of-work ownership quiz

Use the bundled generator and template to create one portable HTML page. Its visual direction follows html-plan: warm paper, serif title, restrained rust accent, numbered expandable sections, inline evidence, and a fixed response bar. Its content and interactions are a comprehension and critical-thinking exercise, not an implementation plan.

Trigger once per current change snapshot. Track the snapshot and pending/completed/skipped quiz in the conversation. Repeated completion messages or commit requests for the same snapshot should resume the existing quiz, not spawn duplicates. If behavior changes afterward, refresh affected questions and preserve prior answers as historical. Do not recursively trigger a new quiz merely because you generated a quiz artifact.

Tell the user why the checkpoint appeared. When it interrupts an authorized commit/merge/ship request, explain that this skill's completion checkpoint holds that action until the response or an explicit skip arrives. Do not ask for authorization again after the checkpoint; continue the already-authorized action when the user is ready. Neither the page's ownership selection nor answering questions grants new execution permissions.

Report implementation and verification status accurately while the quiz is pending. Do not claim the developer owns the changes based on generated questions, confidence ratings, a self-attestation, or a form submission alone.

Keep the interaction conversational and grounded in the current task. Lead with the question or evidence relevant now rather than a lecture about all eight principles. Do not put the full loop into a single response when it requires developer input.

At the end, briefly capture what the developer originally thought, which evidence or challenge mattered, what they now think, and remaining uncertainty. Claim completion only for steps that occurred. Keep implementation status and understanding distinct: a correct explanation does not prove the software works, and passing checks do not prove understanding.
