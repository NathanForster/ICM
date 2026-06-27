# DoD DID Selection and Dependency Guide

This guide helps engineers and AI agents select the right Data Item Descriptions (DIDs) for a DoD software/systems project and understand how the documents relate to each other.

All DID PDFs and AI-readable `.md` digests are in this folder. Source: [quicksearch.dla.mil](https://quicksearch.dla.mil/qsSearch.aspx)

---

## Document Dependency Map

The arrows below show the primary feed relationships: the document at the tail is an input to, or the basis for, the document at the head.

```
                    CI Documentation Recommendation
                        (DI-SESS-82007B)
                              │
                              ▼
               ┌──────────────────────────────┐
               │                              │
               ▼                              ▼
    System/Subsystem Spec            Config Management Plan
         (SSS)                             (CMP)
    DI-IPSC-81431A                    DI-SESS-80858D
               │
       ┌───────┴────────┐
       ▼                ▼
  Software             Interface
  Requirements         Requirements Spec
  Spec (SRS)           (IRS)
  DI-IPSC-81433A       DI-IPSC-81434A
       │                    │
       └───────┬────────────┘
               ▼
    Software Design Desc
           (SDD)
      DI-IPSC-81435B
               │
       ┌───────┴───────────────────────────────┐
       ▼                                       ▼
  Software Dev Plan              Software Test Plan (STP)
      (SDP)                         DI-IPSC-81438A
  DI-IPSC-81427B                         │
                                  ┌──────┴──────┐
                                  ▼             ▼
                          Software Test    Cybersecurity
                          Procedure (STPr) Test Plan (CTP)
                          DI-IPSC-81439A   DI-SCRE-82140A
                          + DI-NDTI-80603A      │
                                  │             ▼
                                  │    CS Test Procedures
                                  │    (CSTP/CSTD)
                                  │    DI-MGMT-82141A
                                  │             │
                            ┌─────┴─────────────┘
                            ▼
                     Requirements
                     Traceability
                     Verification
                     Matrix (RTVM)
                     DI-MGMT-82133A
                            │
                    ┌───────┴────────┐
                    ▼                ▼
            Software Test    CS Test Report
            Report (STR)         (CSTR)
            DI-IPSC-81440A   DI-MGMT-82142A
                    │
                    ▼
           Software Product Spec
                  (SPS)
            DI-IPSC-81441A
                    │
                    ▼
           Software Version Desc
                  (SVD)
            DI-IPSC-81442A
```

---

## Cross-Reference Matrix

Each row is a document; each column is a document that feeds into it or that it feeds into. Read left-to-right as "this document → is used by →".

| Document | Feeds Into | Receives From |
|----------|-----------|---------------|
| **CI Documentation Recommendation** (DI-SESS-82007B) | SSS, SRS, IRS, SDD — drives which items receive which documentation | WBS / contract |
| **CMP** (DI-SESS-80858D) | Governs all other deliverables (CM process); SVD change log | CI Documentation Recommendation, EIA-649 standards |
| **SSS** (DI-IPSC-81431A) | SRS (allocated CSCI requirements), IRS (interface requirements), SDD (design basis), STP (test basis) | CI Documentation Recommendation, contract/SOW |
| **SRS** (DI-IPSC-81433A) | SDD (design basis), STP (test cases), RTVM (requirements), STPr (traceability) | SSS (allocated requirements), IRS |
| **IRS** (DI-IPSC-81434A) | SDD §4.3 / IDD (interface design), STP (interface test cases), RTVM | SSS §3.3 (or standalone), SRS §3.3 |
| **SDP** (DI-IPSC-81427B) | Governs development process; SDD (CM of design artifacts) | SRS, SSS, contract/SOW |
| **SDD** (DI-IPSC-81435B) | SPS §5.1 (as-built design), RTVM (design reference), implementation | SRS (requirements allocated to CSCI), IRS |
| **STP** (DI-IPSC-81438A) | STPr (procedure detail), STR (results), RTVM (verification methods) | SRS, IRS, SSS, SDD |
| **CTP** (DI-SCRE-82140A) | CSTP/CSTD (procedure detail), CSTR (results), RTVM | SRS (security requirements), SDD |
| **STPr** (DI-IPSC-81439A + DI-NDTI-80603A) | STR (references step numbers) | STP (test cases), SRS/IRS/SSS (traceability) |
| **CSTP/CSTD** (DI-MGMT-82141A) | CSTR (references step numbers) | CTP (cybersecurity test cases) |
| **RTVM** (DI-MGMT-82133A) | STR / CSTR (verification status), program management | SRS, IRS, SSS, STP, CTP, SDD |
| **STR** (DI-IPSC-81440A) | SPS (confirms tested baseline), RTVM (verification results) | STPr (step references), STP (test plan), RTVM |
| **CSTR** (DI-MGMT-82142A) | RTVM (security verification results) | CSTP/CSTD (step references), CTP, RTVM |
| **SPS** (DI-IPSC-81441A) | SVD (product baseline definition), deployment | SDD (as-built design), STR (tested baseline confirmation) |
| **SVD** (DI-IPSC-81442A) | Sites / users / support agencies | SPS (product baseline), CMP (CM status accounting), STR |

---

## DID Selection by Project Phase

### Phase 1 — Program Planning

| Document | When to Use |
|----------|-------------|
| **CI Documentation Recommendation** (DI-SESS-82007B) | Early — establishes which WBS elements become CIs and what documentation type each receives. Drives everything downstream. |
| **CMP** (DI-SESS-80858D) | Early — establishes the CM process for the entire program. Required before any baselining activity begins. |
| **SDP** (DI-IPSC-81427B) | Early — establishes the software development process, tools, standards, and schedule. |

---

### Phase 2 — Requirements

| Document | When to Use |
|----------|-------------|
| **SSS** (DI-IPSC-81431A) | Required when developer is tasked to define system or subsystem requirements. Use for the top-level system and for each major subsystem. |
| **SRS** (DI-IPSC-81433A) | Required for each CSCI — captures software requirements derived from/allocated out of the SSS. |
| **IRS** (DI-IPSC-81434A) | Use when interface requirements are complex enough to warrant a separate document from the SSS/SRS, or when interfaces cross organizational/contract boundaries. Optional if §3.3 of the SSS or SRS is sufficient. |

---

### Phase 3 — Design

| Document | When to Use |
|----------|-------------|
| **SDD** (DI-IPSC-81435B) | Required for each CSCI — captures the architectural and detailed design. May be supplemented by IDDs (DI-IPSC-81436) for interface design and DBDDs (DI-IPSC-81437) for database design if those are complex enough to warrant standalone documents. |

---

### Phase 4 — Test Planning and Execution

| Document | When to Use |
|----------|-------------|
| **STP** (DI-IPSC-81438A) | Required when developer is tasked to plan software qualification testing. Covers all non-cybersecurity test types. |
| **CTP** (DI-SCRE-82140A) | Required when cybersecurity testing is contractually required (typically for systems subject to DoD RMF). Paired with CSTP/CSTD and CSTR. |
| **STPr** (DI-IPSC-81439A + DI-NDTI-80603A) | Required when developer is tasked to produce step-by-step test procedures. Use the combined STPr digest which merges the STD (software) and TPr (hardware/calibration) DIDs. |
| **CSTP/CSTD** (DI-MGMT-82141A) | Required alongside the CTP — provides step-by-step cybersecurity test procedures. Includes the sanitize-and-restore step (§3.4.1.1.1.16) that has no analog in standard STPr. |
| **RTVM** (DI-MGMT-82133A) | Use throughout test execution to track verification status of each requirement. Maintained as a living database; populated from SRS/IRS/SSS requirements and updated with test results from STR/CSTR. |

---

### Phase 5 — Test Reporting

| Document | When to Use |
|----------|-------------|
| **STR** (DI-IPSC-81440A) | Required upon completion of software qualification testing — documents results for each test. |
| **CSTR** (DI-MGMT-82142A) | Required upon completion of cybersecurity testing. Includes scanned handwritten tester materials (§3.8 Red Lines) — a unique requirement not present in the STR. |

---

### Phase 6 — Delivery and Sustainment

| Document | When to Use |
|----------|-------------|
| **SPS** (DI-IPSC-81441A) | Required when developer is tasked to deliver the executable software, source files, and "as built" support information. Establishes the product baseline through exact file manifests. |
| **SVD** (DI-IPSC-81442A) | Required for each software release — identifies and describes what is in each version (file inventory, changes since prior version, installation instructions, known errors). |

---

## Minimum Viable DID Set by Contract Type

### Small Software-Only Contract (CSCI delivery, no cybersecurity testing)
SDP → SRS → SDD → STP → STPr → STR → RTVM → SPS → SVD

### System-Level Contract (system + subsystems + software)
CI Documentation Recommendation → CMP → SSS → SRS + IRS → SDP → SDD → STP → STPr → RTVM → STR → SPS → SVD

### Cybersecurity-Augmented Contract (adds RMF testing)
Above set, plus: CTP → CSTP/CSTD → CSTR (with RTVM capturing cybersecurity verification results alongside functional results)

---

## AI Agent Usage Notes

When an ICM project is configured for DoD contract deliverables, an AI agent should:

1. **Read the CI Documentation Recommendation digest first** — it establishes which CIs exist and which documentation types apply. This scopes which other DID digests need to be loaded.
2. **Load only the digests relevant to the current task** — loading all 16 digests at once is wasteful. For a design review task, load SDD; for a test report task, load STR and RTVM; for a delivery task, load SPS and SVD.
3. **Follow the dependency order** when generating a suite of documents — do not start SDD before SRS is complete; do not start STR before STPr is complete.
4. **Use the RTVM as the spine** — all requirement UIDs originate in the SRS/IRS/SSS and flow through the RTVM. When generating any document that references requirements by identifier, verify that those identifiers match the RTVM.
5. **Check traceability at handoff points** — §5 (Requirements Traceability) appears in SSS, SRS, IRS, SDD, SPS, and IRS. At each phase transition, verify that the traceability matrix closes (no unallocated requirements, no orphaned design elements).
