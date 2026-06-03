# GLOBAL FRAMEWORK CONSTRAINTS (ICM.md)

This repository operates under the Interpretable Context Methodology (ICM). All code modifications, text processing, and data transformations must comply with the global mandates, development standards, and behavior constraints defined below.

---

## 1. CORE OPERATIONAL PRINCIPLES
*   **Context Isolation:** Never read or infer files outside the specific folder assigned to your active execution stage.
*   **Plain-Text State Preservation:** All intermediate states, pipeline data, and handoffs must be written to disk as clean Markdown (`.md`), Plain Text (`.txt`), or structural JSON data.
*   **Deterministic Output:** Adhere strictly to the layout schema defined in the active Stage Contract. Do not invent or skip fields.

## 2. OUTPUT GENERATION & WRITING STANDARDS
When generating text content, summaries, outlines, or reports, you must enforce the following formatting constraints:
*   **No Chit-Chat or Meta-Text:** Do not include introductory phrases (e.g., "Sure, here is...", "Based on my analysis...") or concluding remarks. Begin immediately with the requested content.
*   **Semantic Markdown:** Use appropriate header depth hierarchy (`#`, `##`, `###`). Bold critical key phrases exactly once per section to optimize human scannability.
*   **Verbatim Grounding:** When summarizing source texts or transcripts, any extracted quote must be surrounded by blockquotes (`> "example"`) and represent an exact, unmodified copy of the raw source data.

## 3. CODE STYLE & TECHNICAL STANDARDS
When writing code scripts or modifying backend architecture within this workspace, enforce these strict practices:
*   **Language & Stack Constraints:** Python must utilize version 3.10+; JavaScript/TypeScript must adhere to ECMAScript 2022 standards. Rely on native libraries or lightweight, verified packages (`fs-extra`, `openai`).
*   **File I/O Resilience:** Always wrap file operations in explicit exception blocks (`try/except` in Python, `try/catch` in JS). If a target file is missing, fail fast with a non-zero exit code.
*   **No Placeholders:** Write fully functional code. Do not use generic comment blocks like `# TODO: implement this` or `// insert logic here`.

## 4. SYSTEM BOUNDARIES & GUARDRAILS
*   **Hallucination Prevention:** If a Stage Contract asks you to extract information that is completely missing from your active input artifacts, output an explicit system-error tag instead of guessing: `[ERROR: DATA_NOT_FOUND_IN_ARTIFACT]`.
*   **Token Rationing:** Keep responses concise. Extract the highest density of actionable facts using bullet points rather than winding paragraphs.
*   **Model Agnosticism:** Write instructions, prompts, and documentation assuming they will be processed interchangeably by OpenAI, Anthropic, or local open-source LLMs. Do not use vendor-specific syntax wrappers.
