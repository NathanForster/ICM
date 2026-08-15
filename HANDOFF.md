# Project Status

Living status file for the ICM templates repository. Update when repo-level work
completes or new follow-up items emerge.

**Remote:** https://github.com/NathanForster/ICM.git
**Branch:** master

---

## What this repository is

A templates library for the Interpretable Context Methodology (ICM) — orchestrating
AI agent workflows using folders, markdown files, and structure instead of code-heavy
frameworks. Generated project instances live in their own repositories, sibling to
this one under `.ai/`. See [README.md](README.md).

---

## Current state

- **Two base templates:** `generic-agent-oriented-ICM/` and `systems-engineering-ICM/`,
  plus the `advanced-options/` overlay (stage-gated pipeline runner, CLAUDE.md context
  proxy, stricter global constraints).
- **Companion repository:** the DoD DIDs library (18 pairs) was separated into
  [SE-Deliverables](https://github.com/NathanForster/SE-Deliverables) (`.ai/SE-Deliverables/`)
  in 2026-07 so ICM stays a pure orchestration methodology. ICM references it from the
  sys-eng template's documentation/requirements/compliance/V&V workspaces but does not
  depend on it. SE-Deliverables will grow to hold manual templates, UAT artifacts,
  backlog templates, and documentation-set PDF tooling.
- **Project-creation flow:** `Templates/AI_PROJECT_CREATION_INSTRUCTIONS.md` — interview
  is one-question-at-a-time with options; formal deliverables are generated into the
  instance's `docs/` folder from SE-Deliverables definitions (never copied in).

---

## Open items

- Methodology pilot in progress; templates not yet validated at organizational scale.
