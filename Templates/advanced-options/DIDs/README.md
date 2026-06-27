# Data Item Descriptions (DIDs)

This folder contains US DoD Data Item Descriptions (DIDs) relevant to software and systems engineering projects operating under ICM.

Each DID specifies the required format and content for a contractually deliverable document. They are published by the Defense Standardization Program. The PDFs in this folder were obtained from the DoD Quick Search tool: [quicksearch.dla.mil](https://quicksearch.dla.mil/qsSearch.aspx)

For DID selection guidance, a document dependency map, and a cross-reference matrix, see **[GUIDE.md](GUIDE.md)**.

---

## Contents

| DID Number | Title | Companion .md |
|------------|-------|---------------|
| DI-SESS-82007B | Configuration Item (CI) Documentation Recommendation | [CI-DI-SESS-82007B.md](CI-DI-SESS-82007B.md) |
| DI-IPSC-81427B | Software Development Plan (SDP) | [SDP-DI-IPSC-81427B.md](SDP-DI-IPSC-81427B.md) |
| DI-SESS-80858D | Supplier's Configuration Management Plan (CMP) | [CMP-DI-SESS-80858D.md](CMP-DI-SESS-80858D.md) |
| DI-IPSC-81438A | Software Test Plan (STP) | [STP-DI-IPSC-81438A.md](STP-DI-IPSC-81438A.md) |
| DI-IPSC-81440A | Software Test Report (STR) | [STR-DI-IPSC-81440A.md](STR-DI-IPSC-81440A.md) |
| DI-MGMT-82133A | Requirements Traceability Verification Matrix (RTVM) | [RTVM-DI-MGMT-82133A.md](RTVM-DI-MGMT-82133A.md) |
| DI-IPSC-81433A | Software Requirements Specification (SRS) | [SRS-DI-IPSC-81433A.md](SRS-DI-IPSC-81433A.md) |
| DI-SCRE-82140A | Cybersecurity Test Plan (CTP) | [CTP-DI-SCRE-82140A.md](CTP-DI-SCRE-82140A.md) |
| DI-MGMT-82141A | Naval Aviation Cybersecurity Test Procedures/Descriptions (CSTP/CSTD) | [CTPr-DI-MGMT-82141A.md](CTPr-DI-MGMT-82141A.md) |
| DI-MGMT-82142A | Naval Aviation Cybersecurity Test Report (CSTR) | [CTR-DI-MGMT-82142A.md](CTR-DI-MGMT-82142A.md) |
| DI-IPSC-81439A + DI-NDTI-80603A | **Software Test Procedure (STPr)** — combined digest of STD and Test Procedure DIDs | [STPr-Combined.md](STPr-Combined.md) |
| DI-IPSC-81431A | System/Subsystem Specification (SSS) | [SSS-DI-IPSC-81431A.md](SSS-DI-IPSC-81431A.md) |
| DI-IPSC-81435B | Software Design Description (SDD) | [SDD-DI-IPSC-81435B.md](SDD-DI-IPSC-81435B.md) |
| DI-IPSC-81434A | Interface Requirements Specification (IRS) | [IRS-DI-IPSC-81434A.md](IRS-DI-IPSC-81434A.md) |
| DI-IPSC-81441A | Software Product Specification (SPS) | [SPS-DI-IPSC-81441A.md](SPS-DI-IPSC-81441A.md) |
| DI-IPSC-81442A | Software Version Description (SVD) | [SVD-DI-IPSC-81442A.md](SVD-DI-IPSC-81442A.md) |

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

- Others as applicable
