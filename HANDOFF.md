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
  in 2026-07 so ICM stays a pure orchestration methodology. ICM references it from both
  base templates' `## Deliverable library` sections but does not depend on it.
  SE-Deliverables now holds 19 DID pairs, 15 templates (manuals, UAT, trackers,
  summaries, runbook, docs-output, reference/), and the vendored docset PDF engine.
- **Project-creation flow:** `Templates/AI_PROJECT_CREATION_INSTRUCTIONS.md` — interview
  is one-question-at-a-time with options; deliverables are generated into the instance's
  `docs/` folder from SE-Deliverables definitions (never copied in); advanced overlay has
  explicit merge rules. Validated by seven fresh-agent dry runs (2026-08): sys-eng
  converged on pass 3; generic pass 2 resolved 12/12 prior findings; advanced pass 2
  resolved 12/13 and caught that the runner fix was incomplete (now corrected). Both
  second passes surfaced smaller second-order items, all applied.
- **Runner:** `.icm-runner.py` assembles context by ancestor walk to the *topmost*
  `ICM.md` (root Layer 0/1 → workspace Layer 1a → stage Layer 2) and takes
  `--input`/`--artifact` for per-requirement runs. A pre-2026-08 instance that copied
  the runner should re-copy it (and `run_source_dev.sh`, `check_requirements.py`,
  `CLAUDE.md`) — the old version silently dropped Layers 0/1 in nested layouts.

---

## Open items

- Methodology pilot in progress; templates not yet validated at organizational scale.
- A third generic/advanced dry-run pass would confirm the second-pass fixes converged
  the way sys-eng did; not yet run.
- `Examples/temp-logger/` was generated before the 2026-08 instruction changes; it is
  still valid but does not exercise the generic template, the overlay merge, or the
  `reference/` folder.
