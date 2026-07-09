# Project Status

Living status file for the ICM templates repository. Update when repo-level work
completes or new follow-up items emerge.

**Remote:** https://github.com/NathanForster/ICM.git
**Branch:** master

---

## What this repository is

A templates library for the Interpretable Context Methodology (ICM) — orchestrating
AI agent workflows using folders, markdown files, and structure instead of code-heavy
frameworks. Generated project instances live in their own repositories, sibling to
this one under `.ai/`. See [README.md](README.md).

---

## Current state

- **Two base templates:** `generic-agent-oriented-ICM/` and `systems-engineering-ICM/`,
  plus the `advanced-options/` overlay (stage-gated pipeline runner, CLAUDE.md context
  proxy, stricter global constraints).
- **DIDs library complete for the MIL-STD-498 set:** 18 DID pairs (PDF + digest)
  covering planning (SDP, CMP, CI Documentation Recommendation), requirements (SSS, SRS,
  IRS), design (SDD, IDD, DBDD), test (STP, STPr, STR, RTVM), cybersecurity (CTP,
  CSTP/CSTD, CSTR), and delivery (SPS, SVD) — with `DIDs/GUIDE.md` providing selection
  guidance and a dependency map.
- **Project-creation flow:** `Templates/AI_PROJECT_CREATION_INSTRUCTIONS.md` — interview
  is one-question-at-a-time with options; DID-based deliverables are generated into the
  instance's `docs/` folder (digests are never copied out of this repo).

---

## Open items

- None currently. Additional DIDs can be added as project needs arise (download the
  PDF from quicksearch.dla.mil and follow the pair convention in `DIDs/README.md`).
- Methodology pilot in progress; templates not yet validated at organizational scale.
