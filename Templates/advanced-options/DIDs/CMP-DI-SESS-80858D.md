# DID: Supplier's Configuration Management Plan (CMP)

**DID Number:** DI-SESS-80858D  
**Title:** Supplier's Configuration Management Plan  
**Approval Date:** 2020-02-11  
**Supersedes:** DI-SESS-80858C  
**AMSC Number:** N10144  
**Preparing Activity:** NM  
**Project Number:** SESS-2020-007  
**Governing Standards:** EIA-649-1, EIA-649 (available at www.sae.org)  
**Distribution:** Approved for public release. Distribution is unlimited.  
**Source PDF:** [CMP-DI-SESS-80858D.pdf](CMP-DI-SESS-80858D.pdf)

---

## Purpose

The Supplier's Configuration Management (CM) Plan describes the organization, procedures, and controls of the Supplier's CM program. Its primary use is to provide the Government a basis for review, evaluation, and monitoring of the CM program and associated proposed components.

---

## Format

The Supplier's CM Plan shall be prepared in **Supplier format** (contractor's own format is acceptable).

---

## Required Content

The Supplier's CM Plan shall identify the Supplier's processes and procedures for each of the following five areas:

### a. Configuration Management and Planning
Processes and procedures for CM planning over the **lifecycle of a product**.

### b. Configuration Identification
Processes and procedures for configuration identification **throughout the product lifecycle**.

### c. Configuration Change Management
Processes and procedures for controlling and documenting the product and its product configuration information **through the product's end of life**.

### d. Configuration Status Accounting
Processes and procedures for **recording and reporting** information needed to trace and manage configuration of a product.

### e. Verification and Audits
Processes and procedures to ensure **consistency of product information** is established and maintained across the total configuration — including hardware, software, and firmware.

---

## Key Points for AI Agents

- **Format is flexible:** the CMP uses Supplier format, not a prescribed government outline. The five required areas (a–e) must be addressed, but structure is up to the contractor.
- **Scope is total configuration:** hardware, software, and firmware are all in scope.
- **Lifecycle span:** CM planning covers from initial development through product end of life.
- **Standards basis:** EIA-649-1 (implementation) and EIA-649 (principles) are the governing standards. An AI generating a CMP should understand these standards' vocabulary (CI, baseline, CCB, SCR, etc.).

---

## ICM Usage Notes

This DID defines the five required content areas for a contractually deliverable CMP. An AI agent working within an ICM project can use this file to:

- **Generate** a CMP outline or draft by addressing each of the five required areas using project context from ICM.md and CONTEXT.md
- **Validate** a draft CMP for completeness — every area (a–e) must be covered
- **Map** CM activities to ICM structure: configuration identification and status accounting map naturally to ICM's `state/` folders and version-controlled file structure; change management maps to ICM's corrective action and review workflows
- **Cross-reference** with the SDP (DI-IPSC-81427B §3.8.p), which requires the SDP to describe the CM approach — the CMP expands that into a standalone deliverable

When generating a CMP, note that EIA-649 terminology (configuration item, baseline, configuration control board, engineering change, etc.) should be used consistently throughout.
