# GLOBAL FRAMEWORK CONSTRAINTS (ICM.md)

This repository operates under the Interpretable Context Methodology (ICM). All code modifications, text processing, and data transformations must comply with the global mandates, development standards, and behavior constraints defined below.

> **Overlay merge rule.** The base template's root `ICM.md` remains the project's Layer 0.
> Append the sections below to it, verbatim and in order, as **"Part B — Pipeline
> execution constraints"** — do not fold them into the base file's own sections (Part A
> stays untouched, Part B is recognisably the overlay). Replace the illustrative stack
> line in §3 with the project's real stack. Do not replace the base file. Delete this
> block after merging.

---

## 1. CORE OPERATIONAL PRINCIPLES
*   **Context Isolation (stage runs):** When executing as a pipeline stage via `.icm-runner.py`, never read or infer files outside the stage folder and the context layers the runner supplies (root `ICM.md`/`CONTEXT.md`, any intermediate workspace `ICM.md`/`CONTEXT.md`, and the stage `CONTEXT.md`). Interactive sessions that write briefs, code, or docs are governed by the base template's normal routing rules, not by this restriction.
*   **Plain-Text State Preservation:** All intermediate states, pipeline data, and handoffs must be written to disk as clean Markdown (`.md`), Plain Text (`.txt`), or structural JSON data.
*   **Deterministic Output:** Adhere strictly to the layout schema defined in the active Stage Contract. Do not invent or skip fields.

## 2. OUTPUT GENERATION & WRITING STANDARDS
When generating text content, summaries, outlines, or reports, you must enforce the following formatting constraints:
*   **No Chit-Chat or Meta-Text:** Do not include introductory phrases (e.g., "Sure, here is...", "Based on my analysis...") or concluding remarks. Begin immediately with the requested content.
*   **Semantic Markdown:** Use appropriate header depth hierarchy (`#`, `##`, `###`). Bold critical key phrases exactly once per section to optimize human scannability.
*   **Verbatim Grounding:** When summarizing source texts or transcripts, any extracted quote must be surrounded by blockquotes (`> "example"`) and represent an exact, unmodified copy of the raw source data.

## 3. CODE STYLE & TECHNICAL STANDARDS
When writing code scripts or modifying backend architecture within this workspace, enforce these strict practices:
*   **Language & Stack Constraints:** *(Illustrative — replace with the project's actual stack as recorded in its Technical Stack answer.)* Python must utilize version 3.10+; JavaScript/TypeScript must adhere to ECMAScript 2022 standards. Rely on native libraries or lightweight, verified packages (e.g. `requests`, `pydantic` for Python; `fs-extra` for JS).
*   **File I/O Resilience:** Always wrap file operations in explicit exception blocks (`try/except` in Python, `try/catch` in JS). If a target file is missing, fail fast with a non-zero exit code.
*   **No Placeholders:** Write fully functional code. Do not use generic comment blocks like `# TODO: implement this` or `// insert logic here`.

## 4. SYSTEM BOUNDARIES & GUARDRAILS
*   **Hallucination Prevention:** If a Stage Contract asks you to extract information that is completely missing from your active input artifacts, output an explicit system-error tag instead of guessing: `[ERROR: DATA_NOT_FOUND_IN_ARTIFACT]`.
*   **Token Rationing:** Keep responses concise. Extract the highest density of actionable facts using bullet points rather than winding paragraphs.
*   **Model Agnosticism:** Write instructions, prompts, and documentation assuming they will be processed interchangeably by OpenAI, Anthropic, or local open-source LLMs. Do not use vendor-specific syntax wrappers.
