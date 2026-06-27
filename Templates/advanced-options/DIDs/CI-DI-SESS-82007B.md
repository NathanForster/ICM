# DID: Configuration Item (CI) Documentation Recommendation

**DID Number:** DI-SESS-82007B  
**Title:** Configuration Item (CI) Documentation Recommendation  
**Approval Date:** 2022-12-01  
**Supersedes:** DI-SESS-82007A, DI-SESS-81879  
**AMSC Number:** N10371  
**Preparing Activity:** AS  
**Project Number:** SESS-2023-005  
**Governing Standards:** EIA-649-1A (implementation); SAE/EIA-649C (principles)  
**Standards Source:** SAE International — [www.sae.org](https://www.sae.org); DoD guidance at [quicksearch.dla.mil](https://quicksearch.dla.mil)  
**Source PDF:** [CI-DI-SESS-82007B.pdf](CI-DI-SESS-82007B.pdf)

---

## Purpose

The CI Documentation Recommendation details the contractor's recommendations for:
1. **Designation of items as CIs** in the contract work breakdown structure (WBS) and its extensions
2. **Types of configuration documentation** to be used to identify the configurations of those CIs

The purpose is to facilitate program management by further decomposing the system architecture into logical components that enhance:
- Systems engineering
- Integrated logistics support
- Configuration management efforts

The data also provides the Government with technical rationale for selecting the most appropriate type(s) of configuration documentation to describe the performance and physical requirements of CIs.

---

## Format Requirements

Contractor format.

---

## Required Content

### 3.1 CI Designation Recommendations

Recommendations, supported by rationale, for:

- **Designating elements of the contract WBS and its extensions as CIs** — identify which WBS elements should be designated as Configuration Items and explain why
- **Identifying the most appropriate type(s) of configuration documentation** to be used to identify the configuration of each CI

The rationale shall reflect the decomposition of the system architecture into logical components and explain how each recommended CI designation enhances systems engineering, integrated logistics support, and configuration management.

---

## Key Concepts for AI Agents

**Configuration Item (CI):** A system element designated for configuration management. CIs are identified at a level of the system hierarchy appropriate for configuration tracking, baseline management, and independent delivery or support. A CI may be hardware, software, firmware, or a combination.

**WBS (Work Breakdown Structure):** The hierarchical decomposition of the total scope of work into manageable elements. CI designations map to WBS elements and their extensions.

**Types of configuration documentation** (per EIA-649/SAE-649C principles) typically include:
- **System/Subsystem Specifications (SSS/SSSpec)** — functional and performance requirements at system level
- **Software Requirements Specifications (SRS)** — CSCI-level requirements
- **Interface Requirements Specifications (IRS)** — interface requirements between CIs
- **Software Design Documents (SDD)** — design-level descriptions
- **Product Specifications** — performance/physical requirements for hardware CIs
- **Product Baselines** — "as-built" configuration documentation

**Governing standards:**
- **EIA-649-1A** — Configuration Management implementation requirements
- **SAE/EIA-649C** — Configuration Management principles (CM planning, CI identification, change management, status accounting, verification and audits) — same five areas required by the CMP (DI-SESS-80858D)

---

## ICM Usage Notes

This DID defines the required content of a CI Documentation Recommendation. An AI agent working within an ICM project can use this file to:

- **Generate** a CI Documentation Recommendation by iterating over the project's WBS (from contract or project planning workspace) and, for each element, evaluating whether it warrants CI designation using criteria such as: independent deliverability, need for configuration control across multiple builds, logistics support requirements, interface criticality, or contractual baseline requirements
- **Validate** a draft CI Documentation Recommendation for completeness — every recommended CI designation must include rationale explaining the systems engineering or logistics benefit; every CI must be paired with a recommended type of configuration documentation
- **Map to the CMP:** the CMP (DI-SESS-80858D) describes configuration identification procedures across the product lifecycle — the CI Documentation Recommendation is the upstream input that establishes *which* items will be subject to those procedures
- **Map to the SDP:** SDP §3.8.p (configuration management) references configuration identification as the first CM activity — the CI Documentation Recommendation is the artifact that drives that identification
- **Map to the RTVM:** CI designations define the allocation boundaries for requirements. Requirements allocated to a CSCI (§3.2.17 of RTVM, DI-MGMT-82133A) should align with the CI boundaries established in the CI Documentation Recommendation
- **Apply EIA-649C vocabulary:** CI, baseline, functional baseline, allocated baseline, product baseline, configuration control board (CCB), engineering change — use these terms consistently, as also required by the CMP

When generating a CI Documentation Recommendation, organize by WBS element and for each provide: (1) recommendation (CI or not CI), (2) CI type if applicable (CSCI, HWCI, etc.), (3) recommended documentation type(s), (4) rationale in terms of systems engineering / logistics / CM benefit.
