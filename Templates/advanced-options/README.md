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
| `.icm-runner.py` | Runs a single isolated pipeline stage |
| `run_data_pipeline.sh` | Full data pipeline (ingest → transform → validate → load) with review pauses between stages |
| `run_source_dev.sh` | Per-requirement source-development pipeline (implementation brief → code → validation brief) |
| `check_requirements.py` | Consistency check — flags register rows missing ICM artifacts and orphan artifacts |
| `DIDs/` | US DoD Data Item Description library (PDF + AI-readable digest pairs) — see [DIDs/GUIDE.md](DIDs/GUIDE.md) |

## When to choose the advanced version

Choose advanced when the project needs:
- enforced human review gates between workflow stages
- per-requirement implementation/validation artifacts with an auditable trail
- formal (DoD/contractual) deliverables generated from the DIDs library

For lighter projects, the base templates alone are simpler to operate.

## Data transmission notice

The pipeline runner (`.icm-runner.py`) sends stage content — ICM.md, CONTEXT.md,
stage contracts, reference files, and input briefs — to the configured cloud LLM
provider (Anthropic or OpenAI) for processing. Do not place credentials, export-
controlled data, or information barred from third-party processing in stage
folders. For such projects, run stages manually per the stage contracts instead
of using the runner, or use an approved provider endpoint.

## DID usage rule

DID digests and PDFs stay in this repository. Project instances generate their
deliverable documents in their own `docs/` folder (e.g. `docs/SRS.md`), structured
per the governing DID — see [DIDs/GUIDE.md](DIDs/GUIDE.md).
