# Configuration Item Register
# Project: [PROJECT NAME] | Updated: [DATE]

## Configuration Items

| CI ID | Name | Type | Current Baseline | Documentation | Change Authority |
|-------|------|------|------------------|---------------|------------------|
| CI-01 | [item name] | CSCI / HWCI / Document | [version/tag] | [governing spec or doc] | [who approves changes] |
| CI-02 | [item] | [type] | [baseline] | [doc] | [authority] |

## Baseline Log

| Date | CI ID | Baseline | Change summary | Approved by |
|------|-------|----------|----------------|-------------|
| [DATE] | CI-01 | v1.0 | Initial baseline | [name] |

## Rules

- Every CI has exactly one current baseline and a named change authority
- Baseline changes append to the log — never rewrite history
- CI designation rationale belongs in `decisions/` (ADR) or, for DoD contracts,
  in a CI Documentation Recommendation (DI-SESS-82007B — digest in the ICM
  templates repository under `Templates/advanced-options/DIDs/`)
