# State

Persistent operational memory — survives LLM session boundaries.

## Contents

| File | Purpose |
|------|---------|
| `HANDOFF.md` | Session handoff document — critical paths, commands, ICM state, recent commits |

## HANDOFF.md

`HANDOFF.md` is the primary mechanism for preserving context across LLM context-window
boundaries.  It should be:

- **Committed to the repository** so it travels with the code.
- **Updated at the end of every working session** (header line, §7 pipeline state, §9 current state).
- **Read at the start of every new session** before any other action.

<!-- Instantiation: rewrite this README for the instance — describe what THIS project
keeps in state/ (HANDOFF.md plus anything else, e.g. a session log), and delete the
paragraph below, which is advice to the instantiating agent, not project record. -->

The document uses placeholder values (`[PROJECT NAME]`, `[DATE]`, etc.) — replace all
placeholders when creating a new project instance from this template.
