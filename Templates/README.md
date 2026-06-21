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
│       └── systems-engineering-ICM/
│
├── skills/                       ← shared prompts and instructions
├── memory/                       ← shared context across projects
├── tools/                        ← shared scripts and utilities
│
├── my-first-project/             ← generated project instances live here
└── my-second-project/
```

---

# Recommended Workflow

## Step 1 — Select a Template

Choose the template that most closely matches the intended project domain.

---

## Step 2 — Provide the Template to an AI

Point an AI agent at [AI_PROJECT_CREATION_INSTRUCTIONS.md](AI_PROJECT_CREATION_INSTRUCTIONS.md).

---

# Recommended AI Workflow

The AI should gather information such as:

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
- documentation needs

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
- standards
- templates
- workflow scaffolds
- state tracking files
- README files
- placeholder project artifacts

The AI should then create:

- downloadable ZIP archive

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

Example:

```bash
git init
git add .
git commit -m "Initial ICM project instance"
```
