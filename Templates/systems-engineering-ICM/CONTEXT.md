# Global Systems Engineering Context

This file is the **single source of truth for workspace routing**. If a task does not
match a row in this table, escalate to the human operator rather than guessing.

---

## Workspace Routing Table

### Active workspaces (full context set: ICM.md, CONTEXT.md, AGENT.md, README.md)

| Workspace | Route When |
|-----------|-----------|
| `source-development/` | Writing, modifying, or reviewing source code; automation systems; DAQ systems; instrumentation integration |
| `documentation/` | Creating or updating any technical document — user manuals, development plans, validation documentation, release notes |
| `requirements/` | Capturing, triaging, baselining, or tracing requirements |
| `sales/` | Creating customer-facing materials — proposals, technical collateral, presentations, capability summaries |

### Registry workspaces (README.md only — records, not agent-operated workflows)

| Workspace | Route When |
|-----------|-----------|
| `compliance/` | Recording regulatory or contractual compliance evidence |
| `configuration-management/` | Recording configuration items, baselines, and change control |
| `decisions/` | Recording engineering or architectural decisions |
| `governance/` | Recording approval flows, ownership boundaries, and policies |
| `metrics/` | Defining, collecting, or reporting on KPIs |
| `risk-management/` | Identifying, assessing, or mitigating project risks |
| `standards/` | Recording coding, documentation, or process standards |
| `state/` | Session handoff and persistent operational state |
| `templates/` | Reusable document and artifact templates |
| `verification-validation/` | Recording validation workflows and evidence |

### Non-workspace folders and files (owned, not routed)

Every top-level item that is not a workspace is listed here with its owner, so nothing
is unaccounted for. Rows marked *(when present)* exist only if the project creates them.

| Item | What it is | Owner |
|------|-----------|-------|
| `src/` (and `src/tests/`) | Source code and tests | `source-development/` |
| `docs/` *(when present)* | Authored deliverables — see **Deliverable library**; `docs/status/` holds living trackers, `docs/output/` generated artifacts (gitignored except its README) | Per file, per `docs/DELIVERABLES.md` (default `documentation/`) |
| `reference/` *(when present)* | Third-party material the project depends on but does not author — see **Deliverable library** | `documentation/` (manifest upkeep) |
| Root `ICM.md`, `CONTEXT.md`, `README.md`, `.gitignore` | Project-level framework files | Edited only when the project's shape changes |
| Root scripts / config *(advanced overlay)* — `.icm-runner.py`, `run_*.sh`, `check_requirements.py`, `CLAUDE.md`, `DOCSET.json` | Pipeline runner and build config — invoked by workspaces, not routed | `source-development/` (runner, stage scripts), `requirements/` (`check_requirements.py`), `documentation/` (`DOCSET.json`) |

Always load local CONTEXT.md files (where present) before execution.

---

## Deliverable library

Deliverable definitions — DoD DID digests (OCD, SSS, SRS, SDD, STP, RTVM, …), manual /
UAT / tracker / summary / runbook templates, and the consolidated-PDF tooling — live in
the companion **SE-Deliverables** library (`.ai/SE-Deliverables/`,
https://github.com/NathanForster/SE-Deliverables). Generated deliverables go in this
project's `docs/` (living trackers in `docs/status/`); the map of which library item
governs which file is `docs/DELIVERABLES.md`. Never copy library files into this project.

Third-party material the project depends on but does not author — vendor manuals,
protocol specs, standards, reference datasets — goes in `reference/` (a sibling of
`docs/`, tracked, with a provenance manifest in its README). `docs/` is authored;
`reference/` is not.

Ownership: `documentation/` — manuals, summaries, DID documents, runbooks,
enhancement-request intake · `requirements/` — register, RTVM, backlog ·
`verification-validation/` — UAT findings, status table, live-testing records ·
`decisions/` — deviations register.

---

## Version Control — Files That Must Be Gitignored

This is the canonical gitignore guidance for the project; other context files reference
this section rather than repeating it.

| Category | Examples |
|----------|---------|
| Credentials | `.env`, `*.key`, `*.pem`, `secrets.*` |
| Runtime config | `settings.json`, user data files modified at runtime |
| Build / generated output | `dist/`, `build/`, `__pycache__/`, `*.pyc`, `docs/output/` (generated PDFs — its README is the one tracked file) |
| Virtual environments | `.venv/`, `node_modules/`, `.conda/` |
| IDE / local state | `*.local.json`, `.DS_Store`, `*.user`, `Thumbs.db` |
| Editor backups | `*.bak`, `*~`, `*.swp` |
| Committed on purpose | Pipeline `input_*.md` / `output_*.md` stage artifacts (advanced overlay) — they are the audit trail; `reference/` (third-party material, tracked) |

The **only** committed credential file should be the example template (e.g. `.env.example`
with placeholder values). Never commit real keys, tokens, or passwords.
