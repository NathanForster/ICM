# CLAUDE CONTEXT PROXY

## IMPORTANT: SYSTEM COMPLIANCE

This project standardizes architectural guardrails, constraints, and instructions
using the **Interpretable Context Methodology (ICM)**.

Do not define standalone guidelines inside this file. You must read, respect, and
strictly adopt the global parameters outlined in the companion configuration file.

## REQUIRED ACTION

Before executing any file modifications, code generations, or workflow routing steps,
you are explicitly ordered to read the following file:

- **`./ICM.md`** — Layer 0: Global Framework Constraints

Treat the rules inside `ICM.md` as hard operational boundaries for your active session.

---

## MANDATORY SOURCE-DEVELOPMENT PIPELINE

When implementing any **Baselined** requirement, you MUST follow this sequence.

> **Do not write code until step 2 is complete.**
> **Do not commit until step 4 is complete.**

1. **Write an implementation brief** in `source-development/workflows/03-implementation/`
   named `input_<REQ-ID>_implementation.md`.
   Include: design summary, files to be modified, key functions/classes, constraints.

2. **Run stage 03:**
   ```
   python .icm-runner.py source-development/workflows 03-implementation
   ```

3. **Write the code** in `src/`.
   Run lint and a smoke test before proceeding.

4. **Write a validation brief** in `source-development/workflows/04-validation/`
   named `input_<REQ-ID>_validation.md`.
   Include: lint result, logic review, edge cases tested, test results, overall PASS/FAIL.

5. **Run stage 04:**
   ```
   python .icm-runner.py source-development/workflows 04-validation
   ```

6. **Update the requirements register** — change Status from `Baselined` to `Implemented`.
   Update the Trace column with the source file(s).

7. **Commit** source code + ICM artifacts + register update together in a single commit.

**Shortcut:** Use `bash run_source_dev.sh <REQ-ID>` to be guided through steps 1–5
with automatic pauses for human review between each stage.

### Backfill policy

If a requirement was implemented without following this sequence, **backfill** the
input briefs retroactively, re-run stages 03 and 04, then update the register.
Do not skip directly to Verified — the register must pass through Implemented first.

### Artifact naming convention

```
input_<REQ-ID>_implementation.md    e.g.  input_REQ-42_implementation.md
input_<REQ-ID>_validation.md        e.g.  input_REQ-42_validation.md

Grouped REQs:  input_REQ-<N>-<M>_implementation.md
```

---

## WORKSPACE COMMANDS

If executing terminal commands or pipeline runs via the CLI, refer to these primary
entry points (all relative to the project root):

- **Data pipeline (ingest → transform → validate → load):** `bash run_data_pipeline.sh`
- **Source-development pipeline (per requirement):**        `bash run_source_dev.sh <REQ-ID>`
- **Isolated single stage:**                                `python .icm-runner.py <workspace/workflows> <stage>`
