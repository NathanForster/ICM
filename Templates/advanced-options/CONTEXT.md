# PROJECT BLUEPRINT & ROUTING MAP

This document establishes the macro-workflow, execution ordering, and data handoff
contracts for the active project workspace. All execution scripts and processing
layers look to this blueprint to navigate the repository.

> **This is an overlay, not a replacement.** The base template's `CONTEXT.md` (its
> routing tables, Deliverable library, and Version Control sections) is authoritative.
> When applying the overlay, **merge** sections 1–4 below into the base file as a
> "Pipeline blueprint" part (adapting stage names to the project's real pipeline) and
> **discard** sections 5–6 — the base file already has them and its rows are the real ones.
> Replace every `[PLACEHOLDER]` with project-specific content and delete this block
> when the merge is complete.

---

## 1. PROJECT OBJECTIVE

**Name:** `[PROJECT NAME]`

**Purpose:** `[One-paragraph description of what this project produces and why.]`

**Primary output:** `[Deliverable type — e.g. software application, data report, document, API]`

---

## 2. REPOSITORY PIPELINE TOPOLOGY

The workflow is strictly decoupled into linear, isolated execution stages.
Each stage folder contains its own local `CONTEXT.md` governing its internal
transformation behaviour.

```
  [Raw Input / Requirements]
          │
          ▼
  ┌───────────────────┐
  │  01-<stage-name>/ │  ──►  output_01-<stage-name>.md
  └────────┬──────────┘
           │  (promoted by run_data_pipeline.sh)
           ▼
  ┌───────────────────┐
  │  02-<stage-name>/ │  ──►  output_02-<stage-name>.md
  └────────┬──────────┘
           │  (promoted by run_data_pipeline.sh)
           ▼
  ┌───────────────────┐
  │  03-<stage-name>/ │  ──►  output_03-<stage-name>.md  (final deliverable)
  └───────────────────┘
```

Replace the stage names above with the actual stages for this project. Note that
`run_data_pipeline.sh` ships with the stage sequence `01-ingest → 02-transform →
03-validate → 04-load` hard-coded as per-stage blocks (`STAGE1=…`, `INPUT2=…`) — edit
those blocks to match whatever you draw here, or the runner and the blueprint will
disagree.

---

## 3. STAGE EXECUTION MATRIX

### STAGE 1: `01-[stage-name]/`

- **Purpose:** `[What this stage does to its inputs]`
- **Primary input:** `input_[name].[ext]`
- **Expected output:** `output_01-[stage-name].md`
- **Downstream consumer:** Stage 2

### STAGE 2: `02-[stage-name]/`

- **Purpose:** `[What this stage does to its inputs]`
- **Primary input:** `input_[name].md` (promoted from Stage 1 output)
- **Expected output:** `output_02-[stage-name].md`
- **Downstream consumer:** Stage 3

### STAGE 3: `03-[stage-name]/`

- **Purpose:** `[What this stage does to its inputs]`
- **Primary input:** `input_[name].md` (promoted from Stage 2 output)
- **Expected output:** `output_03-[stage-name].md`
- **Downstream consumer:** End consumer / release

---

## 4. HUMAN INTERVENTION GATE POLICY

This pipeline enforces a **strict gate pattern** between stages.

1. When a stage completes, the pipeline runner (`run_data_pipeline.sh` for a
   stage sequence, `run_source_dev.sh <REQ-ID>` for the source-development pair)
   pauses automatically.
2. A human operator inspects the output file in that stage's folder.
3. The operator may edit the output directly to correct errors or adjust scope.
4. On confirmation, the runner promotes the (possibly edited) output to become
   the immutable `input_*.md` for the next stage — preventing hallucinated drift
   across stage boundaries.

---

## 5. WORKSPACE ROUTING

> **Discard on merge.** The base template's `CONTEXT.md` already holds the project's
> routing tables; these rows are illustrative only and reference folders that may not
> exist in your project. Do not copy them across.

| Workspace | Route When |
|-----------|-----------|
| `source-development/` | Writing, modifying, or reviewing source code |
| `data-pipeline/` | Ingesting, transforming, validating, or loading data |
| `testing-validation/` | Writing or running tests |
| `documentation/` | Creating or updating any technical document |
| `requirements/` | Capturing, triaging, or tracing requirements |

---

## 6. VERSION CONTROL

> **Discard on merge — nothing to carry.** The base template's `CONTEXT.md` **Version
> Control** section is canonical and already states that pipeline `input_*.md` /
> `output_*.md` artifacts **are** committed (the audit trail) while any `.env` holding
> `ANTHROPIC_API_KEY` / `OPENAI_API_KEY` is not.
