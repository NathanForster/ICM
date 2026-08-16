# Changelog

Notable changes to the ICM templates library. Generated project instances should
record the template version they were created from (see
`Templates/AI_PROJECT_CREATION_INSTRUCTIONS.md`).

## 2026-08

- **Runner context bug fixed** (`advanced-options/.icm-runner.py`) — Layer 0/1 were read
  from the *workspace_root* argument (`source-development/workflows`), which has no
  `ICM.md`/`CONTEXT.md`, so in every sys-eng advanced instance the global constraints and
  project blueprint never reached the LLM. The runner now walks up from the stage folder
  to the nearest ancestor holding `ICM.md`, loads root Layer 0/1 there, adds intermediate
  workspace `ICM.md`/`CONTEXT.md` as **Layer 1a: LOCAL CONTEXT**, then the stage
  `CONTEXT.md`. Verified against both the nested sys-eng layout and the flat pipeline layout.
  Exposed by a fresh-agent dry run of the advanced overlay.
- **Advanced overlay merge guidance** — overlay `ICM.md`/`CONTEXT.md` now carry explicit
  merge rules (base template authoritative; overlay ICM appended as *Part B*; overlay
  CONTEXT §1–4 merged as a *Pipeline blueprint*, §5–6 discarded); creation instructions
  and the overlay README spell out the same rules plus script edits (`run_data_pipeline.sh`
  per-stage blocks, `run_source_dev.sh` workspace argument, `check_requirements.py` paths).
  Fixed `run_pipeline.sh` → `run_data_pipeline.sh` in the gate policy; "Context Isolation"
  scoped to stage runs; illustrative stack line marked; `CLAUDE.md` commit-gate step
  corrected (5, not 4); `check_requirements.py` accepts `Captured`/blank status and forces
  UTF-8 stdout so it runs on a default Windows console.
- **Generic template gains the same `CONTEXT.md` shape as sys-eng** — Active / Registry /
  Non-workspace tables, a `## Deliverable library` heading (so the creation flow's merge
  rule applies to both bases), `state/` classed as registry, and the canonical Version
  Control table extended (`docs/output/`, static-site output, editor backups).
- **Creation instructions** — sys-eng-only supporting systems labelled (standards,
  decisions, governance, src; templates/ optional); explicit permission to adapt library
  templates' structure to a non-sys-eng workflow while keeping naming/placement/map
  conventions; generic-template ownership split for deliverables; git-init recommended
  not run; Step 1 read-list includes workspace `ICM.md` and the overlay files; root
  scripts/config get one Non-workspace row.
- **Dry-run methodology** — five fresh-agent creation dry runs this month (three sys-eng,
  one generic, one advanced+PDF-set) drove the above; the third sys-eng pass converged
  (18/18 prior findings did not recur).
- **`reference/` folder** — SE-Deliverables `templates/reference/` offered in the
  documentation checklist and scaffolded beside `docs/` when hardware, protocols, or a
  regulatory regime are named. `docs/` is authored; `reference/` is not.

## 2026-07

- **DIDs library moved to companion repo** — `Templates/advanced-options/DIDs/` (18 DID
  pairs + GUIDE) separated into [SE-Deliverables](https://github.com/NathanForster/SE-Deliverables)
  so ICM remains a pure orchestration methodology; all cross-references now point to
  `.ai/SE-Deliverables/`. Deliverable definitions were never required for ICM operation.
- **DIDs library completed** (before the move) — IDD (DI-IPSC-81436A) and DBDD
  (DI-IPSC-81437A) added, closing the SDD's delegated-design references; 18 DID pairs total
- **Worked example added** (`Examples/temp-logger/`) — one requirement through the
  full lifecycle with briefs, register, matrix, ADR, source, passing tests, and handoff
- **Stage scaffolds shipped** — `source-development/workflows/03-implementation/` and
  `04-validation/` with example stage contracts (the runner's Layer 2); workflow
  READMEs document the project-wide stage numbering
- **Base/advanced dependency made explicit** — stage runs and `check_requirements.py`
  marked "(advanced overlay)" in base sys-eng files
- **Workspace quality pass** — Definition of Done in all AGENT.md files;
  domain-specific missions in generic workspaces; generic template gains `state/`;
  registry workspaces gain starter artifacts (ADR template, risk register, KPI table,
  compliance matrix, CI register)
- **Tooling** — runner defaults refreshed (`claude-opus-4-8`), sampling params removed
  for current Anthropic models, `LLM_MAX_TOKENS`/`LLM_TEMPERATURE` env-configurable;
  `run_source_dev.sh` artifact matching covers all legacy name forms; data-transmission
  notice added
- **Deck** — separator-line strike-through fixed (baked-in background lines removed);
  slide content aligned with revised creation flow, advanced options, and `.ai/` structure

## 2026-06 and earlier

- DIDs library: 16 DoD Data Item Description pairs (PDF + AI-readable digest) with
  selection GUIDE, dependency map, and cross-reference matrix
- Consistency pass: single-source routing tables, two-tier workspace file convention,
  one-question-at-a-time interview, environment-dependent delivery, DID deliverables
  generated into instance `docs/`
- Root README, LICENSE (MIT), `.ai/` recommended folder structure, PPTX/PDF walkthrough
