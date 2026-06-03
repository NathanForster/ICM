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

Ask which template to use. Templates are folder names within the ICM_Examples folder that end in "-ICM".

Ask the user if they would like an advanced version of the ICM. If yes, then merge the "advanced-options" content with content from the user's selected template.

Read:
- `ICM.md`
- top-level `CONTEXT.md`
- local workspace `CONTEXT.md`
- local `AGENT.md`

---

## Step 2 — Interview the User

Ask questions necessary to customize the project instance.

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

### Compliance and Governance
- regulatory requirements
- traceability needs
- security requirements
- audit requirements

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

Each workspace should include:
- `ICM.md`
- `CONTEXT.md`
- `AGENT.md`
- README.md

---

## Generate Supporting Systems

When applicable, generate:
- standards/
- templates/
- state/
- decisions/
- inbox/
- projects/

---

# Required Deliverable

The final deliverable should be:

1. fully generated folder structure
2. populated example markdown files
3. packaged ZIP archive
4. downloadable by the user

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
