# Changelog

Notable changes to the ICM templates library. Generated project instances should
record the template version they were created from (see
`Templates/AI_PROJECT_CREATION_INSTRUCTIONS.md`).

## 2026-08

- **Runner context bug fixed** (`advanced-options/.icm-runner.py`) — Layer 0/1 were read
  from the *workspace_root* argument (`source-development/workflows`), which has no
  `ICM.md`/`CONTEXT.md`, so in every sys-eng advanced instance the global constraints and
  project blueprint never reached the LLM. The runner now walks up from the stage folder
  to the **topmost** ancestor holding `ICM.md` (bounded by the repository's `.git`) — not
  the nearest, because sys-eng workspaces carry their own `ICM.md` and a first fix that
  stopped at the nearest one was caught by the second dry-run pass — loads root Layer 0/1
  there, adds intermediate workspace `ICM.md`/`CONTEXT.md` as **Layer 1a: LOCAL
  CONTEXT**, then the stage `CONTEXT.md`. Verified against a realistic nested sys-eng
  tree (workspace `ICM.md` present, `.git` at root) and the flat pipeline layout.
- **Runner input selection** — new `--input <brief>` (load only that brief as Layer 4,
  instead of every `input_*` file in the folder — earlier requirements' briefs no longer
  pollute later runs) and `--artifact <path>` (load e.g. the stage-03 output for the
  stage-04 run, which its contract asks it to check against). `run_source_dev.sh`,
  `CLAUDE.md`, and the sys-eng HANDOFF §4/§7 use them. Default behaviour without flags is
  unchanged (flat pipelines).
- **`check_requirements.py`** — `Captured`/blank rows are open, not "artifacts missing";
  stage `output_*.md` files are no longer reported as orphans; UTF-8 stdout forced.
- **Third-pass fixes (generic + advanced re-runs)** — `run_source_dev.sh`, `CLAUDE.md`
  and the sys-eng HANDOFF §4 shipped with **broken line continuations** from the
  previous pass's edit (literal `\n` / lost backslashes — the script would have passed a
  stray `n` argument and aborted); fixed and the script now proven end-to-end with a
  stub runner. Runner: root detection no longer depends on `.git` (contiguous-`ICM.md`
  rule — a not-yet-initialised project cannot be hijacked by a stray ancestor `ICM.md`);
  a brief named by `--input` is always Layer 4 even if its name contains `config` /
  `reference` / `style`; an empty `--input` file is an error. `run_source_dev.sh`
  `find_brief` requires `_` after the ID (`REQ-1` no longer matches `REQ-10`) and warns on
  multiple matches. Docs: generic workspace files lose their software slant ("product
  claims", DoD "code passes lint") and gain a *Standards* section stub in each `ICM.md`;
  stage-03 contract no longer asks the LLM to read `standards/` (the runner does not
  load it — the brief carries the rules); overlay §4 gate wording covers both the
  promotion and the `--artifact` mechanism; instructions: interview qualifiers for
  `standards/`/`reference/`/review process, `templates/` is registry in sys-eng,
  Version Control table pruned per instance, DID *presentation* may adapt (content may
  not), `reference/standards/` holds contract documentation requirements, static-site
  rule in both content- and build-owning workspaces, `git init` before the first stage
  run, REQ-ID form must match the register.
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
- **Second-pass fixes (generic + advanced re-runs)** — sys-eng `CONTEXT.md` gains the
  Non-workspace table it was described as having; generic `CONTEXT.md` moves `docs/` /
  `reference/` to Non-workspace (matching sys-eng and the instructions), notes that code
  lives in `production/`, warns about static-site generators defaulting to `docs/`, adds
  `site/` and a "committed on purpose" row; generic HANDOFF gains a §5 *Decisions* table;
  instructions: always create a root `README.md`, where approvals/standards/decisions
  land in a generic instance, dangling-reference removal as a general rule, no-data-
  pipeline case (delete `run_data_pipeline.sh`, do not repoint), sys-eng `templates/` is
  a shipped registry row, RTVM ownership exception, `docs/output/` owner, "template
  defaults" means writing-room owns all, intake-tool-unknown case, harness `CLAUDE.md`
  auto-load trap; overlay `ICM.md` no longer offers "fold into matching sections".
- **`.gitignore` before the first commit** — the instructions, both templates' Version
  Control sections, the Templates README quick-start, and the top-level README now
  strongly recommend the sequence `git init` → review the generated `.gitignore` against
  the actual stack → `git status` → first commit, and the generated root README carries
  it as a "First commit" block. A file committed once stays in history after it is
  ignored.
- **Dry-run methodology** — nine fresh-agent creation dry runs this month (three each
  of sys-eng, generic, advanced+PDF-set) drove the above. All three paths have now
  converged: sys-eng pass 3 (18/18 prior findings resolved), generic pass 3 (21/21 pass-2
  findings resolved), advanced pass 3 (14/14 pass-2 findings resolved — and it caught the
  broken continuations that pass 2's own fix had introduced, which is exactly what a
  third pass is for).
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
