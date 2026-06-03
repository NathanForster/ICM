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

The document uses placeholder values (`[PROJECT NAME]`, `[DATE]`, etc.) — replace all
placeholders when creating a new project instance from this template.
