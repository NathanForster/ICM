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
- the DoD **DIDs library** (`advanced-options/DIDs/`) — Data Item Description digests for generating contractually compliant deliverables (see its `GUIDE.md`)

If yes, merge the `advanced-options/` content with the user's selected template.

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
- user manuals
- specifications
- validation reports
- release notes
- formal deliverables (see DID-Based Deliverables below)

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
- inbox/
- projects/
- docs/ (formal deliverables — see below)

---

## DID-Based Deliverables

If the project has DoD or formal contractual deliverables (SRS, SDD, STP, RTVM, etc.):

- **Do NOT copy the DID digest `.md` files into the project instance.** The digests
  stay in the ICM templates repository (`Templates/advanced-options/DIDs/`) and are
  loaded from there when generating or validating a deliverable.
- **Create the deliverable documents themselves in a `docs/` folder** in the project
  instance, one document per required deliverable, structured per the relevant DID
  digest (e.g. `docs/SRS.md`, `docs/SDD.md`, `docs/RTVM.md`).
- Use `Templates/advanced-options/DIDs/GUIDE.md` to select which deliverables the
  project needs based on contract type and project phase.
- Record in the project's top-level `CONTEXT.md` which DIDs govern which `docs/`
  files, so future agents know where the authoritative format definitions live.

---

# Required Deliverable

The final deliverable is a fully generated folder structure with populated example
markdown files. The delivery method depends on the environment:

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
