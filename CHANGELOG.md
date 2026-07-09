# Changelog

Notable changes to the ICM templates library. Generated project instances should
record the template version they were created from (see
`Templates/AI_PROJECT_CREATION_INSTRUCTIONS.md`).

## 2026-07

- **DIDs library completed** — IDD (DI-IPSC-81436A) and DBDD (DI-IPSC-81437A) added,
  closing the SDD's delegated-design references; 18 DID pairs total
- **Worked example added** (`Examples/temp-logger/`) — one requirement through the
  full lifecycle with briefs, register, matrix, ADR, source, passing tests, and handoff
- **Stage scaffolds shipped** — `source-development/workflows/03-implementation/` and
  `04-validation/` with example stage contracts (the runner's Layer 2); workflow
  READMEs document the project-wide stage numbering
- **Base/advanced dependency made explicit** — stage runs and `check_requirements.py`
  marked "(advanced overlay)" in base sys-eng files
- **Workspace quality pass** — Definition of Done in all AGENT.md files;
  domain-specific missions in generic workspaces; generic template gains `state/`;
  registry workspaces gain starter artifacts (ADR template, risk register, KPI table,
  compliance matrix, CI register)
- **Tooling** — runner defaults refreshed (`claude-opus-4-8`), sampling params removed
  for current Anthropic models, `LLM_MAX_TOKENS`/`LLM_TEMPERATURE` env-configurable;
  `run_source_dev.sh` artifact matching covers all legacy name forms; data-transmission
  notice added
- **Deck** — separator-line strike-through fixed (baked-in background lines removed);
  slide content aligned with revised creation flow, advanced options, and `.ai/` structure

## 2026-06 and earlier

- DIDs library: 16 DoD Data Item Description pairs (PDF + AI-readable digest) with
  selection GUIDE, dependency map, and cross-reference matrix
- Consistency pass: single-source routing tables, two-tier workspace file convention,
  one-question-at-a-time interview, environment-dependent delivery, DID deliverables
  generated into instance `docs/`
- Root README, LICENSE (MIT), `.ai/` recommended folder structure, PPTX/PDF walkthrough
