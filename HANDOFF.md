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
  explicit merge rules. Validated by nine fresh-agent dry runs (2026-08): all three
  paths (sys-eng, generic, advanced+PDF-set) converged on their third pass — every prior
  finding resolved, remaining items polish-level and applied. The advanced pass 3 caught
  broken shell continuations that pass 2's fix had introduced; the script is now proven
  end-to-end with a stub runner.
- **Runner:** `.icm-runner.py` assembles context by ancestor walk to the *topmost*
  `ICM.md` (root Layer 0/1 → workspace Layer 1a → stage Layer 2) and takes
  `--input`/`--artifact` for per-requirement runs. A pre-2026-08 instance that copied
  the runner should re-copy it (and `run_source_dev.sh`, `check_requirements.py`,
  `CLAUDE.md`) — the old version silently dropped Layers 0/1 in nested layouts.

---

## Open items

- Methodology pilot in progress; templates not yet validated at organizational scale.
- Dry-run passes are done for all three paths. A future pass is warranted only after a
  substantive change to the instructions, a template, or the overlay scripts.
- `Examples/temp-logger/` was generated before the 2026-08 instruction changes; it is
  still valid but does not exercise the generic template, the overlay merge, or the
  `reference/` folder.
