# Advanced Options

An optional overlay merged with a base template (`generic-agent-oriented-ICM/` or
`systems-engineering-ICM/`) when the user requests the advanced version of an ICM
project instance.

## What it adds

| Item | Purpose |
|------|---------|
| `ICM.md` | Stricter global constraints — output formatting, code standards, hallucination guardrails |
| `CONTEXT.md` | Project blueprint template with a stage-gated pipeline topology and human intervention gates |
| `CLAUDE.md` | Context proxy for Claude Code — enforces the mandatory implementation → validation sequence per requirement |
| `.icm-runner.py` | Runs a single isolated pipeline stage. Assembles the LLM context by walking up from the stage folder to the **topmost** ancestor holding `ICM.md` (the project root — bounded by the repo's `.git`), loading root `ICM.md`/`CONTEXT.md` (Layers 0/1), any intermediate workspace `ICM.md`/`CONTEXT.md` (Layer 1a), and the stage `CONTEXT.md` (Layer 2). `--input <brief>` restricts Layer 4 to one brief; `--artifact <path>` adds e.g. the previous stage's output |
| `run_data_pipeline.sh` | Full data pipeline (ingest → transform → validate → load) with review pauses between stages |
| `run_source_dev.sh` | Per-requirement source-development pipeline (implementation brief → code → validation brief) |
| `check_requirements.py` | Consistency check — flags register rows missing ICM artifacts and orphan artifacts |

## How it merges with a base template

The overlay is additive; the base template stays authoritative for structure.

| Overlay file | Merge rule |
|--------------|-----------|
| `ICM.md` | Append to the base root `ICM.md` as *Part B — Pipeline execution constraints*; replace the illustrative stack line with the project's real stack |
| `CONTEXT.md` | Merge §1–4 (objective, topology, stage matrix, gate policy) into the base root `CONTEXT.md` as a *Pipeline blueprint* part with real stage names; **discard** §5–6 — the base file already has routing and version-control sections and its rows are the real ones |
| `CLAUDE.md` | Copy to the instance root as-is |
| Scripts | Copy to the instance root; edit `run_data_pipeline.sh`'s per-stage blocks to the project's real stage folders — or **delete it** if the project has no multi-stage data pipeline (the source-development pair is driven by `run_source_dev.sh`); edit `run_source_dev.sh`'s workspace/dir variables if they differ; adjust `check_requirements.py` default paths if the register/brief folders differ from the sys-eng layout |
| Stage folders | Live under the owning workspace (`<workspace>/workflows/0N-<stage>/CONTEXT.md`), never loose at the root |

Full instructions: `Templates/AI_PROJECT_CREATION_INSTRUCTIONS.md`, Step 1.

## When to choose the advanced version

Choose advanced when the project needs:
- enforced human review gates between workflow stages
- per-requirement implementation/validation artifacts with an auditable trail

For lighter projects, the base templates alone are simpler to operate.

## Formal deliverables

Deliverable definitions — DoD Data Item Description digests, manual templates, UAT
artifacts — live in the companion **SE-Deliverables** repository
(`.ai/SE-Deliverables/`, https://github.com/NathanForster/SE-Deliverables). It is
optional and independent of the advanced overlay: any ICM project (base or advanced)
with formal deliverable requirements can reference it. Project instances generate their
deliverables in their own `docs/` folder; the library is never copied into a project.

## Data transmission notice

The pipeline runner (`.icm-runner.py`) sends stage content — ICM.md, CONTEXT.md,
stage contracts, reference files, and input briefs — to the configured cloud LLM
provider (Anthropic or OpenAI) for processing. Do not place credentials, export-
controlled data, or information barred from third-party processing in stage
folders. For such projects, run stages manually per the stage contracts instead
of using the runner, or use an approved provider endpoint.
