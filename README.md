# critical-thinking-addy-osmani

> **Based on [Addy Osmani’s article on X](https://x.com/addyosmani/status/2117512471930167377).** This is an independent implementation of the ideas in that article, not an official Addy Osmani project or an endorsement.

An agent skill for practicing developer judgment before, during, and after implementation, inspired by Addy Osmani's writing on critical thinking in agentic workflows.

The core loop is **your view → the agent's evidence or challenge → your revised view**.

## Workflow

- **Before:** establish intent, form a hypothesis, and clarify the request and acceptance bar.
- **During:** examine consequential decisions, assumptions, and alternatives.
- **After:** inspect evidence, identify verification gaps, and complete a visual ownership quiz about the actual changes.

When active, the skill instructs the agent to prepare the quiz when work is considered done or the user asks to commit, merge, ship, or wrap up. These are agent instructions, not an installed Git hook. Explicit skips are respected.

The quiz preserves initial answers, reveals evidence, and invites revised reasoning. Use **Respond** to copy or download the response and return it to the agent for assessment. The HTML page does not automatically grade answers or send them anywhere.

## Install in Codex

Clone this private repository into your Codex skills directory:

```sh
git clone git@github.com:adnankarimdev/critical-thinking-addy-osmani.git ~/.codex/skills/critical-thinking-addy-osmani
```

If that directory already exists, update the existing installation instead of cloning over it.

Invoke with `$critical-thinking-addy-osmani` and your development task.

## Files

- `SKILL.md`: the eight principles, three stages, and completion triggers.
- `references/ownership-quiz.md`: question construction, response handling, and assessment guidance.
- `assets/ownership-quiz.html`: portable interactive quiz template.
- `scripts/build_quiz.py`: creates a standalone page from task-specific JSON using Python's standard library.
- `scripts/test_build_quiz.py`: generator validation tests.
- `agents/openai.yaml`: Codex skill metadata.

Generate a quiz using the input format in the reference:

```sh
python3 scripts/build_quiz.py /path/to/quiz.json --output /path/to/ownership-quiz.html
python3 scripts/test_build_quiz.py
```

Draft answers stay in the browser's local storage when available. Generated quizzes can contain source excerpts; keep them in an appropriate local artifact location. Assessment rubrics stay in the input JSON and are excluded from the generated page.

## Visual inspiration

The quiz uses an original implementation inspired by [Anthropic's html-plan plugin](https://github.com/anthropics/claude-plugins-community/tree/main/html-plan): restrained borders, serif headings, numbered expandable sections, and a fixed response control.
