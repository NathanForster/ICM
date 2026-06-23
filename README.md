# ICM — Interpretable Context Methodology

**A file-based methodology for orchestrating AI agent workflows with folders, files, and
structure instead of code-heavy frameworks — so every routing decision, context boundary,
and workflow step is visible, auditable, and governable.**

---

## The problem

Most AI workflow frameworks rely on code-heavy orchestration that is hard to inspect, debug,
and maintain:

- Custom code, APIs, and runtime state management add significant engineering overhead.
- When an agent misbehaves, it is difficult to see *what context it was operating in* or
  *why* it made a decision.
- **Context pollution** — agents fed too much irrelevant information — produces inconsistent
  results.
- There is usually no persistent **organizational memory**: each session starts from scratch,
  with no record of prior decisions or workflow state.

These problems are worst exactly where rigor matters most: regulated, validation-heavy, and
governance-sensitive work.

## What ICM is

ICM uses folder structures, markdown files, and a small amount of local scripting to
orchestrate AI agents — making the project structure *itself* the workflow engine. An agent
operates by **reading files**, not by running an opaque framework.

Five ideas hold it together:

- **Interpretability** — every routing decision, context boundary, and workflow stage is a
  readable file. No hidden runtime state.
- **Context isolation** — each workspace loads only the context it needs, preventing prompt
  pollution.
- **Deterministic routing** — the same task always routes to the same workspace; the agent
  never guesses.
- **Explicit ownership** — each workspace owns its workflows, outputs, state, and standards.
- **Persistent memory** — decisions, standards, and state are stored as files that survive
  across sessions, creating an auditable trail.

Every workspace is described by three core files: `ICM.md` (purpose, what to load, when to
escalate), `CONTEXT.md` (routing map, allowed/forbidden actions), and `AGENT.md`
(inputs, outputs, definition of done).

## What's in this repo

This is a **templates library** — the methodology plus reusable starting structures. Generated
project instances are meant to live in their *own* repositories, not here.

- **`Templates/`** — the reusable ICM templates and AI project-creation instructions.
  - `generic-agent-oriented-ICM/` — general-purpose structure for content, software, business
    operations, and documentation work.
  - `systems-engineering-ICM/` — a structure for engineering-intensive work: automation, DAQ,
    hardware/software integration, and **validation- and governance-heavy projects**
    (requirements, standards, risk-management, compliance, verification-validation, decision
    logs).
- **`Interpretable_Context_Methodology_(ICM).pdf` / `.pptx`** — a full walkthrough of the
  methodology, its design principles, file anatomy, and execution flow.

## Getting started

1. **Choose a template** — `generic-agent-oriented-ICM` for general projects;
   `systems-engineering-ICM` for engineering, validation, or governance-heavy work.
2. **Point an AI agent at** `Templates/AI_PROJECT_CREATION_INSTRUCTIONS.md`.
3. **Answer the agent's questions** — project name, purpose, domain, technical stack, workflow
   stages, documentation and compliance needs.
4. **Review the generated instance** — confirm routing is unambiguous and ownership is explicit.
5. **Initialize version control** in the new project repo to begin accumulating organizational
   memory.

## Provenance and status

ICM builds on an **emerging practice** in AI-assisted work — using files and folder structure,
rather than code, to direct agents (a pattern also seen in conventions like `AGENTS.md` and
`CLAUDE.md`). What this project contributes is a **refined, reusable implementation** of that
pattern, with particular emphasis on **interpretability, determinism, and engineering
governance** — bringing traceability, V&V, and compliance structure to agent workflows.

**This is early-stage.** The templates are usable today, but the methodology has not yet been
deployed at organizational scale; an initial pilot is in progress. Feedback, issues, and
real-world results are welcome.

## License

MIT — see [LICENSE](LICENSE).
