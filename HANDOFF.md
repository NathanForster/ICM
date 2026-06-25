# Session Handoff

## Context

This is the ICM (Interpretable Context Methodology) repository — a templates library for
orchestrating AI agent workflows using folders, markdown files, and structure instead of
code-heavy frameworks.

**Remote:** https://github.com/NathanForster/ICM.git
**New local path:** `C:\.ai\ICM`
**Branch:** master (clean, fully pushed)

---

## What was done in the last session

1. **`Templates/README.md`** — significantly updated:
   - Added a "Recommended Folder Structure" section showing `.ai/` as the parent directory,
     with `ICM/`, `skills/`, `memory/`, `tools/`, and sibling project folders alongside it.
   - Simplified the workflow: Step 1 renamed to "Think about which Template to use"; Step 2
     reduced to a single line — "Point an AI agent at AI_PROJECT_CREATION_INSTRUCTIONS.md."
   - Added advice to create a completely empty remote repo (no README, no .gitignore) before
     first push, with the full git remote setup command sequence.

2. **`Interpretable_Context_Methodology_(ICM).pptx` / `.pdf`** — updated to match:
   - Slide 8 Step 02 and Slide 12 Step 2 now say "Point the AI agent at
     AI_PROJECT_CREATION_INSTRUCTIONS.md." (previously listed individual files to read).

3. **`README.md`** (root) — created from scratch with a full project description covering the
   problem, what ICM is, repo contents, getting started steps, provenance, and license.

4. **`LICENSE`** — MIT license added, copyright 2026 Nathan Forster.

---

## Current repo structure

```
C:\.ai\ICM\
├── README.md                                      ← root project description
├── LICENSE                                        ← MIT 2026
├── Interpretable_Context_Methodology_(ICM).pptx
├── Interpretable_Context_Methodology_(ICM).pdf
└── Templates/
    ├── README.md                                  ← templates library guide
    ├── AI_PROJECT_CREATION_INSTRUCTIONS.md        ← AI instructions for project creation
    ├── advanced-options/
    ├── generic-agent-oriented-ICM/
    └── systems-engineering-ICM/
```

---

## Key design decisions made this session

- **Projects live outside this repo.** This repo is a templates library only. Generated
  project instances go in their own repos, sibling to this one under `.ai/`.
- **`.ai/` parent directory** is the recommended convention for scoping AI access — user
  agreed this is the right framing.
- **`skills/`, `memory/`, `tools/`** folders were recommended alongside `ICM/` and project
  folders under `.ai/`. User confirmed all three are useful.
- **Step 2 is one line.** The full list of files for the AI to read was removed from both
  the README and the PPTX — `AI_PROJECT_CREATION_INSTRUCTIONS.md` covers it.

---

## Suggested next steps (not yet done)

- The `.ai/` folder structure and `skills/`, `memory/`, `tools/` recommendations exist in
  `Templates/README.md` but are **not yet reflected in the PPTX**. A new or updated slide
  could cover this.
- GitHub repo description and topics were set this session (done outside git):
  - **Description:** "File-based methodology for orchestrating AI agent workflows — using
    folders, markdown, and structure instead of code, so every routing decision and context
    boundary is visible, auditable, and governable."
  - **Topics:** `ai` `agents` `llm-orchestration` `prompt-engineering` `workflow-automation`
    `context-management` `markdown` `interpretability` `ai-governance` `systems-engineering`

---

## To resume on the new machine

```bash
git clone https://github.com/NathanForster/ICM.git C:\.ai\ICM
```

Then open a new Claude Code session with working directory `C:\.ai\ICM` and reference this
file for context.
