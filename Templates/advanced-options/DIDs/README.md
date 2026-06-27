# Data Item Descriptions (DIDs)

This folder contains US DoD Data Item Descriptions (DIDs) relevant to software and systems engineering projects operating under ICM.

Each DID specifies the required format and content for a contractually deliverable document. They are published by the Defense Standardization Program and downloaded from [assist.dla.mil](https://assist.dla.mil).

---

## Contents

| DID Number | Title | Companion .md |
|------------|-------|---------------|
| DI-IPSC-81427B | Software Development Plan (SDP) | [SDP-DI-IPSC-81427B.md](SDP-DI-IPSC-81427B.md) |
| DI-SESS-80858D | Supplier's Configuration Management Plan (CMP) | [CMP-DI-SESS-80858D.md](CMP-DI-SESS-80858D.md) |
| DI-IPSC-81438A | Software Test Plan (STP) | [STP-DI-IPSC-81438A.md](STP-DI-IPSC-81438A.md) |
| DI-IPSC-81440A | Software Test Report (STR) | [STR-DI-IPSC-81440A.md](STR-DI-IPSC-81440A.md) |
| DI-MGMT-82133A | Requirements Traceability Verification Matrix (RTVM) | [RTVM-DI-MGMT-82133A.md](RTVM-DI-MGMT-82133A.md) |
| DI-IPSC-81433A | Software Requirements Specification (SRS) | [SRS-DI-IPSC-81433A.md](SRS-DI-IPSC-81433A.md) |

---

## File Convention

Each DID is stored as a pair of files sharing the same base name:

```
<DID-NUMBER>.pdf    ← original DID document (authoritative)
<DID-NUMBER>.md     ← AI-readable digest (structured summary of all required content)
```

The `.md` digest is not a substitute for the authoritative PDF. It is structured for AI agent consumption: clean headers, every required section and subsection listed, key terms defined, and ICM usage notes at the bottom explaining how an agent should use the file.

---

## How an AI Agent Should Use These Files

1. **Load the relevant `.md` file** for the document type being generated or validated.
2. **Read the project's ICM.md and CONTEXT.md** for project-specific context.
3. **Generate, validate, or map** per the ICM Usage Notes at the bottom of each digest.

When in doubt, refer back to the `.pdf` for authoritative wording.

---

## Planned Additions

Additional DIDs to be added as PDFs are provided:

- Software Design Document (SDD)
- Others as applicable
