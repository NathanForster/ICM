# AI Instructions for Creating an ICM Project Instance

## Objective

Create a customized Interpretable Context Methodology (ICM) project instance based on the selected template.

The resulting project should:

- be interpretable
- support deterministic routing
- minimize context pollution
- support scalable workflows
- maintain explicit ownership boundaries
- support future AI-agent operation

---

# Required Workflow

## Step 1 — Load Core Context

Ask which template to use. Templates are folder names within the `Templates/` folder that end in `-ICM`:

- `generic-agent-oriented-ICM/` — general-purpose structure for content, software, business operations, and documentation work
- `systems-engineering-ICM/` — engineering-intensive structure for validation- and governance-heavy work (requirements, standards, risk management, compliance, V&V, decision logs)

Then ask the user if they would like the **advanced version** of the ICM. Explain what it adds before they answer:

- a stage-gated pipeline runner (`.icm-runner.py`, `run_data_pipeline.sh`, `run_source_dev.sh`) with human review pauses between stages
- a `CLAUDE.md` context proxy enforcing a mandatory implementation → validation sequence per requirement
- stricter global constraints (`ICM.md`) covering output formatting, code standards, and hallucination guardrails

If yes, merge the `advanced-options/` content with the user's selected template.

Separately from the advanced choice, the interview (Step 2, Documentation Requirements)
asks **which documents the project will produce**, offering the companion
**SE-Deliverables** library's contents as options. Do not gate this on the phrase "formal
deliverables" — a project may need a user's manual, a UAT log, or a backlog without
thinking of them as formal. If the user selects anything, confirm SE-Deliverables is
available at `.ai/SE-Deliverables/` (clone from
https://github.com/NathanForster/SE-Deliverables if not) — see the Deliverables section
below.

Read:
- `ICM.md`
- top-level `CONTEXT.md`
- local workspace `CONTEXT.md`
- local `AGENT.md`

---

## Step 2 — Interview the User

**Ask questions one at a time.** Do not present the full question list in a single message.
Wait for each answer before asking the next question, and use earlier answers to skip
questions that no longer apply or to sharpen later ones.

**Present options wherever appropriate.** When a question has a bounded set of common
answers (workflow stages, review process, compliance regime, etc.), offer 2–4 concrete
options plus a free-form alternative, rather than asking open-endedly. Use a structured
choice tool (e.g. AskUserQuestion) when one is available; otherwise list the options in
the message.

Gather information about:

### Project Identity
- project name
- project purpose
- project domain
- target users

### Technical Stack
- languages
- frameworks
- databases
- infrastructure
- hardware interfaces

### Workflow Requirements
- workflow stages
- review process
- validation requirements
- deployment requirements

### Organizational Structure
- desired workspaces
- ownership boundaries
- approval flows
- escalation paths

### Documentation Requirements

Ask this as a **multi-select checklist**: *"Which of these documents will this project
produce?"* — grouped as below, with an explicit **"None of these"** option. Every item maps
to a definition in the companion SE-Deliverables library; see the Deliverables section
for what to do with the answer.

- **DoD / contract deliverables** (DID-governed): OCD, SSS, SRS, IRS, SDD, IDD, DBDD, SDP,
  CMP, CI Documentation Recommendation, STP, STPr, STR, RTVM, CTP, CSTP/CSTD, CSTR, SPS, SVD
- **Manuals:** User's Manual, Programmer's Manual
- **Acceptance & live testing:** UAT findings log (+ tester-facing status table),
  live-testing checklist
- **Trackers:** backlog, enhancement-request intake, deviations register (for ports /
  migrations of a reference system)
- **Summaries:** management summary, executive summary
- **Operations:** runbooks (risk-tiered)
- **Consolidated PDF documentation set** (DOCSET.json-driven build; implies a gitignored
  `docs/output/` with its self-explaining README)
- release notes / other (free-form)

### Compliance and Governance
- regulatory requirements
- traceability needs
- security requirements
- audit requirements

Skip whole categories when the user's earlier answers make them irrelevant (e.g. skip
hardware interfaces for a pure content project). Prefer a short interview that captures
what matters over an exhaustive one.

---

# Project Generation Rules

## Preserve Interpretability

The generated structure should clearly communicate:
- ownership
- workflow
- routing
- responsibilities
- dependencies

---

## Preserve Context Isolation

Avoid unnecessary cross-workspace coupling.

---

## Prefer Explicit Structure

Prefer:
- named workflows
- explicit handoffs
- local context files
- clearly defined ownership

Avoid:
- ambiguous folders
- overloaded workspaces
- undocumented routing

---

## Generate Required Files

Workspaces come in two tiers:

**Active workspaces** (agent-operated workflows — e.g. source-development, documentation,
requirements, sales) each include:
- `ICM.md`
- `CONTEXT.md`
- `AGENT.md`
- `README.md`

**Registry workspaces** (records rather than workflows — e.g. decisions, standards,
metrics, state) include:
- `README.md` describing what is recorded there and any file conventions

The top-level `CONTEXT.md` routing table must list every workspace that exists —
and only workspaces that exist. Routing and folder structure must never disagree.

---

## Generate Supporting Systems

When applicable, generate:
- standards/
- templates/
- state/
- decisions/
- projects/
- docs/ (deliverables — see below)

---

## Deliverables (the SE-Deliverables companion library)

Deliverable *definitions* — DoD DID digests, manual/UAT/tracker/summary/runbook templates,
and the consolidated-PDF tooling — live in the companion **SE-Deliverables** library
(`.ai/SE-Deliverables/`, https://github.com/NathanForster/SE-Deliverables). ICM does not
depend on it; the Documentation Requirements checklist in Step 2 decides whether the
project uses it.

**Always, regardless of the checklist answer:**

- Write a standing pointer in the instance's top-level `CONTEXT.md`:

  ```
  ## Deliverable library
  Companion: `.ai/SE-Deliverables/` (https://github.com/NathanForster/SE-Deliverables)
  Selected for this project: <list, or "none at creation — add via SE-Deliverables/templates/README.md">
  ```

  so a later session on the project can find the library even if nothing was chosen now.

**When any document was selected:**

- **Do NOT copy DID digests or templates into the project instance.** They stay in
  SE-Deliverables and are loaded from there when generating or validating a deliverable.
- **Create the deliverable documents themselves in the instance's `docs/` folder**, one
  per selected item, named per the template/digest header (e.g. `docs/SRS-<P>.md`,
  `docs/USERS-MANUAL-<P>.md`; living trackers in `docs/status/`). Populate each from
  its digest/template with the project's identity filled in and remaining sections
  scaffolded — do not leave a bare filename.
- **Create `docs/DELIVERABLES.md`** from `SE-Deliverables/templates/DELIVERABLES-TEMPLATE.md`
  — one row per selected document: file → governing library item (path) → owner
  workspace → status. This is the authoritative map for future agents. Record library
  items considered but not selected, with the reason.
- For DoD deliverables, use `SE-Deliverables/DIDs/GUIDE.md` to check dependency order
  (e.g. OCD before SSS before SRS) and to catch missing companions (an SRS with external
  interfaces usually wants an IRS).
- If the consolidated PDF set was selected: copy `SE-Deliverables/tools/docset/DOCSET.example.json`
  to the instance root as `DOCSET.json` populated with the selected documents; create
  `docs/output/README.md` from `SE-Deliverables/templates/docs-output/README.md`; append
  the `.gitignore` snippet.
- Route deliverable work: in the sys-eng template, `documentation/` owns manuals,
  summaries, DID documents, and runbooks; `requirements/` owns the register and its RTVM
  counterpart; `verification-validation/` owns UAT and live-testing records. In the
  generic template, `writing-room/` owns them all unless the user says otherwise. Add the
  chosen documents to the owning workspace's `CONTEXT.md` so routing stays deterministic.

---

# Required Deliverable

The final deliverable is a fully generated folder structure with populated example
markdown files.

**Record the template version:** in the instance's top-level `CONTEXT.md`, note the
ICM templates repository commit (`git -C <templates-repo> rev-parse --short HEAD`)
and date the instance was generated from, so future agents can diff against the
templates that produced it.

The delivery method depends on the environment:

- **Local agent with filesystem access** (e.g. Claude Code): create the project
  directly as a sibling folder under `.ai/` (see the Recommended Folder Structure
  in `Templates/README.md`). Do not create a ZIP.
- **Chat environment without filesystem access:** package the structure as a ZIP
  archive downloadable by the user.

---

# Output Quality Rules

The generated ICM project should:
- be deterministic
- be maintainable
- scale cleanly
- minimize ambiguity
- support future automation
- support human readability
- support multi-agent orchestration

Never generate:
- contradictory workflows
- ambiguous ownership
- hidden routing rules
- undocumented standards
- routing tables that reference nonexistent folders
