# Decisions

Architecture Decision Records (ADRs) — the traceable decision log.

## Conventions

- One decision per file: `ADR-001-short-title.md`, numbered sequentially
- Start from [ADR-template.md](ADR-template.md)
- Never delete or rewrite an accepted ADR — supersede it with a new one and
  update the old ADR's Status line
- Reference REQ IDs from the requirements register where a decision affects requirements

An AI agent should consult this folder before proposing changes that reverse
or conflict with a recorded decision, and should escalate rather than silently
contradict an accepted ADR.
