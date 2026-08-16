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

**Placeholders used in these instructions:** `<P>` (also written `<PROJECT>`) is the
project name exactly as the user gives it, used verbatim in file names — e.g. project
`bench-thermal-logger` → `docs/SRS-bench-thermal-logger.md`. Do not abbreviate it in
file names (an abbreviation may be coined *inside* documents for prose).

Ask which template to use. Templates are folder names within the `Templates/` folder that end in `-ICM`:

- `generic-agent-oriented-ICM/` — general-purpose structure for content, software, business operations, and documentation work
- `systems-engineering-ICM/` — engineering-intensive structure for validation- and governance-heavy work (requirements, standards, risk management, compliance, V&V, decision logs)

Then ask the user if they would like the **advanced version** of the ICM. Explain what it adds before they answer:

- a stage-gated pipeline runner (`.icm-runner.py`, `run_data_pipeline.sh`, `run_source_dev.sh`) with human review pauses between stages
- a `CLAUDE.md` context proxy enforcing a mandatory implementation → validation sequence per requirement
- stricter global constraints (`ICM.md`) covering output formatting, code standards, and hallucination guardrails

If yes, **merge** the `advanced-options/` content with the user's selected template. The
overlay is additive; the base template stays authoritative for structure. Concretely:

- **Root `ICM.md`:** keep the base file; append the overlay's four sections as
  **"Part B — Pipeline execution constraints"** (the overlay's own header block says
  this). Replace the overlay's illustrative stack line with the project's real stack.
- **Root `CONTEXT.md`:** keep the base file's routing tables, Deliverable library, and
  Version Control sections — the overlay's §5 (routing) and §6 (version control) are
  **discarded**, since their rows are examples that may name folders the project does
  not have. Merge the overlay's §1–4 (objective, pipeline topology, stage matrix, gate
  policy) in as a "Pipeline blueprint" part, with stage names replaced by the project's
  real stages.
- **Scripts and config at the instance root:** `.icm-runner.py`, `run_data_pipeline.sh`,
  `run_source_dev.sh`, `check_requirements.py`, `CLAUDE.md`, plus `DOCSET.json` if the
  PDF set is selected. Copy them verbatim, then: edit `run_data_pipeline.sh`'s per-stage
  blocks (`STAGE1=`/`INPUT2=`… — it ships with `01-ingest…04-load`) to the project's
  real stage folders, and
  point `check_requirements.py`'s default paths at the project's register and brief
  folders if they differ from the sys-eng layout. Root scripts and config get **one
  combined row** in the Non-workspace table ("pipeline runner + config — not routed;
  invoked by workspaces"), not a row each.
- **`state/README.md`:** the base template's version speaks about the template; tailor
  it to say what this *instance* keeps in `state/`.
- **Pipeline stage folders** the overlay's blueprint refers to (`01-…/`, `02-…/`) must
  actually exist with a `CONTEXT.md` each — under the workspace that owns them (e.g.
  `data-pipeline/workflows/`), never loose at the root.

The overlay is designed around the sys-eng template but works with the generic one:
the source-development pair (`03-implementation`/`04-validation`) simply lives under
whichever workspace does implementation work (`production/` in the generic template),
and `run_source_dev.sh`'s workspace argument is edited to match.

Separately from the advanced choice, the interview (Step 2, Documentation Requirements)
asks **which documents the project will produce**, offering the companion
**SE-Deliverables** library's contents as options. Do not gate this on the phrase "formal
deliverables" — a project may need a user's manual, a UAT log, or a backlog without
thinking of them as formal. If the user selects anything, confirm SE-Deliverables is
available at `.ai/SE-Deliverables/` (clone from
https://github.com/NathanForster/SE-Deliverables if not) — see the Deliverables section
below.

Read, from the **selected template** (no instance exists yet):
- `ICM.md`
- top-level `CONTEXT.md`
- every active workspace's `ICM.md`, `CONTEXT.md` and `AGENT.md` (and its `README.md`)
- every registry workspace's `README.md` and any starter artifact beside it
- the advanced overlay's `README.md` (to describe it accurately when asking); if the
  user chooses it, also its `ICM.md`, `CONTEXT.md`, and `CLAUDE.md` before merging

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
- hardware interfaces (name vendor and model — this seeds the `reference/` manifest)
- coding standards, naming conventions, lint/test tooling (this seeds `standards/`)

### Workflow Requirements
- workflow stages
- review process
- validation requirements
- deployment requirements

### Organizational Structure
- desired workspaces — offer the template's defaults; for any default workspace with no
  work in this project (e.g. `sales/` for an internal tool), keep it but mark it
  **Dormant** in the routing table rather than deleting it
- ownership boundaries
- approval flows
- escalation paths

### Documentation Requirements

Ask this as a **multi-select checklist**: *"Which of these documents will this project
produce?"* — grouped as below, with an explicit **"None of these"** option. Every item maps
to a definition in the companion SE-Deliverables library; see the Deliverables section
for what to do with the answer.

- **DoD / contract deliverables** (DID-governed): OCD, SSS, SRS, IRS, SDD, IDD, DBDD, SDP,
  CMP, CI Documentation Recommendation, STP, STPr, STR, RTVM, CTP, CSTP/CSTD, CSTR, SPS, SVD
- **Manuals:** User's Manual, Programmer's Manual
- **Acceptance & live testing:** UAT findings log (+ tester-facing status table),
  live-testing checklist
- **Trackers:** backlog, enhancement-request intake, deviations register (for ports /
  migrations of a reference system)
- **Summaries:** management summary, executive summary
- **Operations:** runbooks (risk-tiered)
- **Consolidated PDF documentation set** (DOCSET.json-driven build; implies a gitignored
  `docs/output/` with its self-explaining README)
- **Third-party reference folder** (`reference/`, sibling of `docs/`) — for vendor
  equipment manuals, protocol specs, standards the system implements, and reference
  datasets. Offer this whenever the Technical Stack answers named hardware interfaces,
  external protocols, or a regulatory regime, even if the user did not think to ask.
- **Release notes / other (free-form)** — the one item with no library definition; it
  is listed so the user can name project documents the library does not cover.

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
Both base templates ship the same three-part shape — **Active workspaces** table,
**Registry workspaces** table, **Non-workspace folders and files** table — keep it.
Folders that are *not* workspaces (`src/`, `docs/`, `docs/output/`, `reference/`,
`templates/`, and any root scripts/config) go in the Non-workspace table, each with its
owning workspace — so every top-level item is accounted for without pretending it is
routable.

**Version control.** Do not run `git init` or make commits on the user's behalf unless
asked; do recommend initialising the repository as the first thing after generation, and
generate `.gitignore` regardless (see Required Deliverable).

**Base vs. advanced instances (sys-eng template).** The sys-eng template's files mention the advanced
overlay's scripts (`.icm-runner.py`, `check_requirements.py`, `run_*.sh`) in two forms:
(a) **one deletable block** in `state/HANDOFF.md` §4, fenced with `ADVANCED OVERLAY ONLY`
comments; (b) **inline "(advanced) / (base)" alternative pairs** everywhere else
(`source-development/CONTEXT.md` and `AGENT.md`, `workflows/README.md`,
`requirements/CONTEXT.md` and `README.md`, the register, the traceability matrix,
HANDOFF §7). When generating a **base** instance: delete the HANDOFF block, and in every
inline pair keep only the base alternative — rewrite the sentence so it no longer
mentions the script, or states plainly "there is no `<script>` in this project". Then
grep the instance for `icm-runner|check_requirements|run_source_dev` and confirm every
surviving hit is a *negation*, not an instruction. When generating an **advanced**
instance, keep the advanced alternative in each pair (drop the "(base)" clause) and keep
the HANDOFF §4 block with its fence comments removed. The generic template has no such
pairs — its files do not mention the overlay's scripts at all, so an advanced generic
instance must have the pipeline commands *added* to `state/HANDOFF.md` §4 and to the
implementing workspace's `CONTEXT.md`.

---

## Generate Supporting Systems

When applicable, generate:
- state/ — **both templates**; always present (HANDOFF.md lives here)
- docs/ (authored deliverables — see below) — both templates, when any deliverable
  is selected
- reference/ (third-party material the project depends on — see below; a sibling of
  docs/, never inside it) — both templates, when selected
- templates/ — **optional**, either template; only when the project will have its
  own reusable document skeletons (a content project's post template, a sys-eng
  project's brief template). Do not create it empty.
- standards/  (with at least one concrete standard file if the interview supplied
  coding/naming/review rules — the README says "one standard per file") — **sys-eng
  template**; for a generic project, put coding/style rules in the owning workspace's
  `ICM.md` instead unless the user wants a registry
- decisions/ — **sys-eng template** (it is one of its registry workspaces); a generic
  project records decisions in `state/HANDOFF.md` unless it asks for a log
- governance/  (with an approval-matrix file if the interview supplied approval or
  escalation paths) — **sys-eng template**
- src/ and src/tests/ (placeholder READMEs, since workspace files reference them) —
  **sys-eng template**, or a generic project whose `production/` workspace writes code

"Sys-eng template" items are not forbidden in a generic instance — add them if the
interview calls for them — but do not create them by reflex; the generic template's
`CONTEXT.md` does not reference them and the instance's routing table must not either.

---

## Deliverables (the SE-Deliverables companion library)

Deliverable *definitions* — DoD DID digests, manual/UAT/tracker/summary/runbook templates,
and the consolidated-PDF tooling — live in the companion **SE-Deliverables** library
(https://github.com/NathanForster/SE-Deliverables). It is a **sibling of the project
instance under `.ai/`** — i.e. `.ai/SE-Deliverables/` beside `.ai/ICM/` and
`.ai/<project>/`, *not* inside the project. If it is absent, clone it there. ICM does not
depend on it; the Documentation Requirements checklist in Step 2 decides whether the
project uses it.

**Always, regardless of the checklist answer:**

- The template's top-level `CONTEXT.md` already contains a `## Deliverable library`
  section. **Keep it and add these lines to it** (merge — do not replace, do not
  duplicate the heading):

  ```
  Selected for this project: <list with paths, or "none at creation — add via SE-Deliverables/templates/README.md">
  Map and status: `docs/DELIVERABLES.md`
  Library version at creation: SE-Deliverables commit <sha> (<date>)
  ```

  so a later session on the project can find the library even if nothing was chosen now.

**When any document was selected:**

- **Do NOT copy DID digests or templates into the project instance.** They stay in
  SE-Deliverables and are loaded from there when generating or validating a deliverable.
- **Create the deliverable documents themselves in the instance's `docs/` folder**, one
  per selected item. **Names come from `SE-Deliverables/templates/README.md`'s index**
  (its "Instantiate as" column) — templates repeat the name in their header comment; DID
  digests do not, so for a DID use `docs/<ACRONYM>-<P>.md` (e.g. `docs/SRS-<P>.md`).
  Living trackers go in `docs/status/`.
  **"Scaffolded" means:** the document's title block / identification is filled in with
  the project's identity; every top-level section required by the digest or template is
  present as a heading; sections that clearly do not apply say so in one line (DIDs
  require the statement); the `<!-- -->` instantiation guidance is **removed** (keep at
  most a short note pointing at the governing definition). Do not attempt to write final
  content at creation — do not leave a bare filename either.
- **Create `docs/DELIVERABLES.md`** from `SE-Deliverables/templates/DELIVERABLES-TEMPLATE.md`
  — one row per selected document: file → governing library item (path) → owner
  workspace → status. This is the authoritative map for future agents. Record library
  items considered but not selected, with the reason.
- **Whenever any DID is selected** (whether or not the project is DoD/contract), use
  `SE-Deliverables/DIDs/GUIDE.md` to check dependency order (e.g. OCD before SSS before
  SRS) and to catch missing companions (an SRS with external interfaces usually wants an
  IRS). Its "read the CI Documentation Recommendation first" note applies to multi-DID
  selections; for one or two DIDs, just check their rows. **If the GUIDE recommends a
  document the user did not select, honour the user's selection** — do not silently add
  it — and record the recommendation in `docs/DELIVERABLES.md`'s "Not selected" table as
  a flagged candidate.
- Templates that reference other library items (the live-testing checklist assumes a
  generated summary and the consolidated PDF set; the backlog references a deviations
  register; the User's Manual names a Programmer's Manual companion; HANDOFF's path table
  names credential files) carry those references as conditional. When instantiating,
  **remove references to items the user did not select or the project does not have**
  rather than leaving dangling pointers — the rule is general, not limited to these
  examples.
- If the consolidated PDF set was selected: copy `SE-Deliverables/tools/docset/DOCSET.example.json`
  to the instance root as `DOCSET.json` populated with the selected documents; create
  `docs/output/README.md` from `SE-Deliverables/templates/docs-output/README.md`; append
  the `.gitignore` snippet.
- If the third-party reference folder was selected: create `reference/README.md` at the
  **instance root, beside `docs/`** (not inside it) from
  `SE-Deliverables/templates/reference/README.md`, with only the sub-folders the project
  needs (`vendor/`, `standards/`, `data/`), each holding a `.gitkeep` so the empty
  folder survives git; seed the manifest with any hardware, protocol, or standard the
  interview named — status **"Pending placement"** if the user has the file, **"Not yet
  obtained"** if not — with bracketed filename/revision cells for the user to fill.
  `reference/` is tracked — do not add it to `.gitignore`. Add it to the Non-workspace
  folders table, owned by `documentation/` (sys-eng) or `writing-room/` (generic).
- **Adapting library templates to the project.** The library's templates were written
  against a systems-engineering workflow — the backlog assumes REQ IDs, code, and live
  testing; the enhancement intake assumes a UAT track; the runbook assumes an operations
  team. A project (especially a generic-template one) **may change their structure** —
  drop or rename columns, replace REQ-ID fields with the project's own identifiers,
  collapse sections it has no use for — as long as it keeps the library's conventions:
  the file name from the index, placement in `docs/` or `docs/status/`, the title block,
  and a row in `docs/DELIVERABLES.md`. Record the adaptation in that row's notes so the
  next agent knows the document deliberately differs from its governing template. Do not
  hunt for the sys-eng workflow's concepts in a project that lacks them.
- Route deliverable work. In the **sys-eng** template: `documentation/` owns manuals,
  summaries, DID documents, runbooks, and the enhancement-request intake;
  `requirements/` owns the register, its RTVM counterpart, and the **backlog**;
  `verification-validation/` owns UAT findings, the status table, and live-testing
  records; `decisions/` owns the deviations register (it is a decision log). In the
  **generic** template, `writing-room/` owns them all by default; a natural split when
  the project wants one is `production/` for the backlog and any runbook, `community/`
  for release notes and enhancement intake (they face users), `writing-room/` for
  everything else. Add the chosen documents to the owning workspace's `CONTEXT.md` — or
  its `README.md` for registry workspaces, which have no CONTEXT.md — so routing stays
  deterministic. A folder whose files have different owners (`docs/status/` — backlog to
  `requirements/`, live-testing to `verification-validation/`) gets one
  Non-workspace-folders row per owner, or one row naming both; either is fine as long as
  every file is accounted for.

---

# Required Deliverable

The final deliverable is a fully generated folder structure with populated example
markdown files.

**Always create `.gitignore`** from the Version Control table in the selected template's
top-level `CONTEXT.md` (both templates carry the same table — it is the canonical list
for both), even when no deliverable snippet applies — the template's own rules and the
"`reference/` is tracked" statement presuppose one exists. Add stack-specific lines the
interview implies (static-site output for a content project, `target/` for Rust, etc.).

**Record the template versions:** add a `## Template provenance` section at the end of
the instance's top-level `CONTEXT.md` with the ICM templates repository commit
(`git -C <templates-repo> rev-parse --short HEAD`) and date the instance was generated
from, and — if any deliverable was selected — the SE-Deliverables commit likewise (that
one is also written into the Deliverable-library section and `docs/DELIVERABLES.md`), so
future agents can diff against the definitions that produced it.

The delivery method depends on the environment:

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
