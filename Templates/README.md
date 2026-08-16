# Creating an ICM Project Instance

## Purpose

This repository contains reusable Interpretable Context Methodology (ICM) templates.

These templates are intended to help humans and AI agents create structured, deterministic, interpretable project workspaces.

The templates are designed around:

- context isolation
- explicit routing
- modular workflows
- agent-operable folder structures
- persistent organizational memory
- deterministic execution boundaries

---

# Available Templates

## generic-agent-oriented-ICM/

A generalized multi-agent project structure.

Recommended for:
- content workflows
- software projects
- business operations
- documentation systems
- general-purpose orchestration

---

## systems-engineering-ICM/

A systems-engineering-focused project structure.

Recommended for:
- software engineering
- automation systems
- DAQ systems
- validation-heavy projects
- hardware/software integration
- engineering governance

---

# Recommended Folder Structure

This repository is a templates library. Generated project instances should live separately, outside this repository.

A `.ai/` parent directory is recommended for all of these folders. The name signals to both the user and the AI that this is where AI-assisted work lives, and makes it practical to limit AI access scope to just this directory tree.

```
.ai/                              ← recommended parent; scope AI access here
├── ICM/                          ← this repo, templates only
│   └── Templates/
│       ├── README.md
│       ├── AI_PROJECT_CREATION_INSTRUCTIONS.md
│       ├── generic-agent-oriented-ICM/
│       ├── systems-engineering-ICM/
│       └── advanced-options/
│
├── SE-Deliverables/              ← optional companion: deliverable definitions
│                                    (DoD DIDs, manual templates, UAT artifacts)
├── skills/                       ← shared prompts and instructions
├── memory/                       ← shared context across projects
├── tools/                        ← shared scripts and utilities
│
├── my-first-project/             ← generated project instances live here
└── my-second-project/
```

---

## Companion: SE-Deliverables

Formal deliverable definitions — US DoD Data Item Description (DID) digests, manual
templates, UAT artifacts, and documentation-set tooling — live in a separate companion
repository: [SE-Deliverables](https://github.com/NathanForster/SE-Deliverables). Clone
it beside ICM under `.ai/` when a project has DoD, contractual, or formal documentation
requirements. ICM does not depend on it; it is optional for projects without such
requirements.

---

# Recommended Workflow

## Step 1 — Think about which Template to use

Choose the template that most closely matches the intended project domain.

---

## Step 2 — Direct the AI to setup your new project.

Point an AI agent at [AI_PROJECT_CREATION_INSTRUCTIONS.md](AI_PROJECT_CREATION_INSTRUCTIONS.md).

For a picture of what a finished instance looks like in use, see the worked
examples in [`../Examples/`](../Examples/README.md).

---

# Recommended AI Workflow

The AI should interview the user **one question at a time**, presenting concrete
options where appropriate rather than open-ended prompts, and skipping categories
that earlier answers make irrelevant.

It should gather information such as:

## General Information
- project name
- project type
- project goals
- primary technologies
- expected outputs
- stakeholders

## Workflow Information
- desired workspaces
- workflow stages
- review requirements
- validation requirements
- documentation needs — asked as a checklist drawn from the companion SE-Deliverables
  library (DoD DIDs, manuals, UAT/live-testing records, trackers, summaries, runbooks,
  consolidated PDF set), with "none" as an option

## Operational Information
- coding standards
- naming conventions
- security requirements
- traceability requirements
- compliance constraints

## Agent Coordination Information
- routing rules
- escalation conditions
- handoff requirements
- ownership boundaries

---

# Expected AI Output

The AI should generate:

- customized folder structure
- ICM.md files
- CONTEXT.md files
- AGENT.md files
- state tracking files (`state/HANDOFF.md`)
- README files (root and per workspace)
- `.gitignore`
- and, when the template or interview calls for them: standards, templates, workflow
  scaffolds, `docs/` deliverables and their map — see
  `AI_PROJECT_CREATION_INSTRUCTIONS.md` for which apply to which template
- placeholder project artifacts

Delivery depends on the environment:

- **Local agent with filesystem access** (e.g. Claude Code) — create the project directly as a sibling folder under `.ai/`
- **Chat environment without filesystem access** — create a downloadable ZIP archive

---

# Important Design Principles

## 1. Local Context Authority

The nearest context file is authoritative.

---

## 2. Explicit Ownership

Each workspace should own:
- workflows
- outputs
- temporary state
- standards
- deliverables

---

## 3. Deterministic Routing

The AI should avoid ambiguous workspace selection.

---

## 4. Minimal Prompt Pollution

Agents should load only necessary context.

---

## 5. Interpretability

The repository structure itself should explain:
- ownership
- workflow
- routing
- operational boundaries
- execution flow

---

# Long-Term Recommendation

Treat ICM repositories as:

- operational systems
- engineering assets
- organizational memory systems
- workflow engines
- AI-operable execution environments

Version control is strongly recommended.

When creating a remote repository, create it completely empty — no README, no .gitignore. This avoids merge conflicts on the first push.

Example:

```bash
git init
git add .
git commit -m "Initial ICM project instance"
git remote add origin https://github.com/your-org/your-project.git
git push -u origin master
```
