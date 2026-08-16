# Global Routing Context

This file is the **single source of truth** for what folders exist in this project and
when work is routed to each. Every folder in the routing tables must exist; every
workspace folder must have a row. Always load a workspace's local `CONTEXT.md` before
executing inside it.

> **Customise on instantiation.** The three workspaces below are the template's starting
> point, not a mandate — rename, remove, or add rows to match the project. Delete this
> block when the file is complete.

---

## Active workspaces

Work is routed here. Each has its own `ICM.md` (local constraints and standards),
`CONTEXT.md` (mission, scope, and — once the project defines them — its workflow stages),
and `AGENT.md` (persona).

| Workspace | Route When |
|-----------|-----------|
| `writing-room/` | Tutorials, documentation, blog posts, long-form content creation |
| `production/` | Implementation, software builds, engineering work, technical execution |
| `community/` | Outreach, marketing, customer communication, social content |

## Registry workspaces

Folders that hold project memory or generated output. They are **not** routed for
execution — an agent reads or writes them as directed by an active workspace's contract,
but never "works inside" them.

| Folder | Purpose | Owned by |
|--------|---------|----------|
| `state/` | Persistent operational memory. Read `state/HANDOFF.md` at the start of every session; update it at the end. Decisions worth remembering go in its **Decisions** section (this template has no separate decision log). | Whoever ends the session |

## Non-workspace folders and files

Not workspaces, not routed — but every top-level item is accounted for here so nothing
is unowned. *(Rows marked "when present" exist only if the project creates the item.)*

| Item | What it is | Owner |
|------|-----------|-------|
| `docs/` *(when present)* | Authored project deliverables — see **Deliverable library** below. `docs/status/` holds living trackers | `writing-room/` unless `docs/DELIVERABLES.md` says otherwise |
| `reference/` *(when present)* | Third-party material the project depends on but does not author — see **Deliverable library** below | `writing-room/` (manifest upkeep) |
| `templates/` *(when present)* | Reusable skeletons for this project's own documents | The workspace that uses them |
| Root `ICM.md`, `CONTEXT.md`, `README.md`, `.gitignore` | Project-level framework files | Edited only when the project's shape changes |

> Code, if the project has any, lives inside `production/` by default (that workspace's
> `CONTEXT.md` says so). Add a root `src/` row here only if the project chooses a root
> source tree instead.

---

## Deliverable library

Deliverables — manuals, UAT records, trackers, summaries, runbooks, and (when the
project needs them) DoD-format specifications — are generated from definitions in the
companion **SE-Deliverables** library, which lives beside this project under the parent
`.ai/` folder (`.ai/SE-Deliverables/`, https://github.com/NathanForster/SE-Deliverables).

- **Never copy library files into this project.** Generate documents from them into
  `docs/`, using the library's naming convention `docs/<ACRONYM>-<PROJECT>.md` for
  formal deliverables and `docs/status/` for living trackers.
- **`docs/DELIVERABLES.md`** is the project's map: which deliverables were selected,
  their file names, and which workspace owns each. It exists whenever `docs/` exists.
- **Ownership default:** `writing-room/` owns `docs/` unless `docs/DELIVERABLES.md`
  says otherwise. Split ownership (e.g. `production/` owns a runbook) is fine — record
  it in the map.
- **Adapting library templates.** The library's templates were written against a
  systems-engineering workflow (requirements IDs, source code, formal UAT). A generic
  project may adapt their structure — columns, fields, section names — to its own
  workflow, provided the file naming, `docs/` placement, and `DELIVERABLES.md`
  bookkeeping conventions are preserved. Record any structural adaptation in the map.
- **Static-site generators and `docs/`.** MkDocs, Jekyll, and similar default to
  `docs/` as their *source* folder. In an ICM project `docs/` holds deliverables, not
  site content — configure the generator's source directory explicitly (e.g. MkDocs
  `docs_dir:` pointing into the owning workspace) so trackers and the deliverables map
  are never published as pages.
- **`reference/`** is the sibling of `docs/` for material the project *uses* but does
  *not* author — vendor manuals, protocol specs, standards, reference datasets. It is
  tracked (large binaries may be linked instead), and its `README.md` is a provenance
  manifest (source, version, date obtained, status). `docs/` is authored; `reference/`
  is not.

---

## Version Control — Files That Must Be Gitignored

| Category | Examples |
|----------|---------|
| Credentials | `.env`, `*.key`, `*.pem`, `secrets.*` |
| Runtime config | `settings.json`, user data files modified at runtime |
| Build / generated output | `dist/`, `build/`, `__pycache__/`, `*.pyc`, `docs/output/` (generated PDFs), static-site output (`site/` MkDocs, `_site/` Jekyll, `public/` Hugo, `.next/`) |
| Committed on purpose | Pipeline `input_*.md` / `output_*.md` stage artifacts (advanced overlay) — they are the audit trail; `docs/output/README.md` (the only tracked file in `docs/output/`) |
| Virtual environments | `.venv/`, `node_modules/`, `.conda/` |
| IDE / local state | `*.local.json`, `.DS_Store`, `*.user`, `Thumbs.db` |
| Editor backups | `*.bak`, `*~`, `*.swp` |

The **only** committed credential file should be the example template (e.g. `.env.example`
with placeholder values). Never commit real keys, tokens, or passwords.

**Assemble and review `.gitignore` before the first commit.** The generated file is
built from this table; before `git add` on a fresh repository, check it against the
project's actual stack (venv location, build output, IDE files, static-site output) and
run `git status` to confirm nothing sensitive is staged. A file committed once remains in
the history after it is ignored — reviewing first is cheap; scrubbing history is not.
