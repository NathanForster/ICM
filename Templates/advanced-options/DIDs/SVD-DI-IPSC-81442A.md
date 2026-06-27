# DID: Software Version Description (SVD)

**DID Number:** DI-IPSC-81442A  
**Title:** Software Version Description (SVD)  
**Approval Date:** 2000-01-11  
**Supersedes:** DI-IPSC-81442  
**AMSC Number:** N7377  
**Preparing Activity:** N/SPAWAR  
**Source PDF:** [SVD-DI-IPSC-81442A.pdf](SVD-DI-IPSC-81442A.pdf)

---

## Purpose

The SVD identifies and describes a software version consisting of one or more Computer Software Configuration Items (CSCIs). It is used to release, track, and control software versions.

The term "version" may be applied to:
- The initial release of the software
- A subsequent release of that software
- One of multiple forms of the software released at approximately the same time (for example, to different sites)

This DID is used when the developer is tasked to identify and record the exact version of software to be delivered to a user, support, or other site.

---

## Format Requirements

Contractor format unless otherwise specified in the CDRL (DD 1423). May be delivered on paper or electronic media; may reside in a CASE tool rather than a traditional document.

---

## Required Content Structure

### 1. Scope

#### 1.1 Identification
Full identification of the system and the software to which this document applies: identification number(s), title(s), abbreviation(s), version number(s), and release number(s). Also identify the intended recipients of the SVD to the extent that this identification affects the contents of the software released (for example, source code may not be released to all recipients).

#### 1.2 System Overview
Briefly state the purpose of the system and the software to which this document applies. Describe the general nature of the system and software; summarize history of system development, operation, and maintenance; identify the project sponsor, acquirer, user, developer, and support agencies; identify current and planned operating sites; list other relevant documents.

#### 1.3 Document Overview
Summarize the purpose and contents of this document and describe any security or privacy considerations associated with its use.

---

### 2. Referenced Documents
List the number, title, revision, and date of all documents referenced in this document. Identify the source for all referenced documents not available through normal Government stocking activities.

---

### 3. Version Description

Divided into the following paragraphs.

#### 3.1 Inventory of Materials Released
List by identifying numbers, titles, abbreviations, dates, version numbers, and release numbers, as applicable:
- All **physical media** (listings, tapes, disks) and **associated documentation** that make up the software version being released
- Applicable security and privacy considerations for these items
- Safeguards for handling them (concerns for static and magnetic fields)
- Instructions and restrictions regarding duplication and license provisions

#### 3.2 Inventory of Software Contents
List by identifying numbers, titles, abbreviations, dates, version numbers, and release numbers, as applicable, **all computer files** that make up the software version being released. Include any applicable security and privacy considerations.

#### 3.3 Changes Installed
Contain a list of **all changes incorporated into the software version since the previous version**. If change classes have been used, such as the Class I/Class II changes in MIL-STD-973, the changes shall be separated into these classes.

For each change, identify as applicable:
- The problem reports, change proposals, and change notices associated with each change
- The effects, if any, of each change on system operation
- Effects on interfaces with other hardware and software

*This paragraph does not apply to the initial software version.*

#### 3.4 Adaptation Data
Identify or reference all **unique-to-site data** contained in the software version. For software versions after the first, this paragraph shall describe changes made to the adaptation data.

#### 3.5 Related Documents
List by identifying numbers, titles, abbreviations, dates, version numbers, and release numbers, as applicable, all **documents pertinent to the software version being released but not included in the release**.

#### 3.6 Installation Instructions
Provide or reference the following information, as applicable:

- **a.** Instructions for installing the software version
- **b.** Identification of other changes that have to be installed for this version to be used, including site-unique adaptation data not included in the software version
- **c.** Security, privacy, or safety precautions relevant to the installation
- **d.** Procedures for determining whether the version has been installed properly
- **e.** A point of contact to be consulted if there are problems or questions with the installation

#### 3.7 Possible Problems and Known Errors
Identify any possible problems or known errors with the software version at the time of release, including:
- Any steps being taken to resolve the problems or errors
- Instructions (either directly or by reference) for recognizing, avoiding, correcting, or otherwise handling each one

The information presented shall be appropriate to the intended recipient of the SVD. For example, a user agency may need advice on avoiding errors, while a support agency may need advice on correcting them.

---

### 4. Notes
General information that aids in understanding this document (background information, glossary, rationale). Include an alphabetical listing of all acronyms, abbreviations, and their meanings as used in this document, and a list of any terms and definitions needed to understand this document.

---

### A. Appendices
May be used to provide information published separately for convenience in document maintenance (e.g., charts, classified data). Each appendix shall be referenced in the main body where the data would normally have been provided. Appendices may be bound as separate documents. Lettered alphabetically (A, B, etc.).

---

## Key Acronyms

| Acronym | Meaning |
|---------|---------|
| CASE | Computer-Aided Software Engineering |
| CDRL | Contract Data Requirements List |
| CSCI | Computer Software Configuration Item |
| MIL-STD-973 | Military Standard — Configuration Management |
| SPS | Software Product Specification |
| SVD | Software Version Description |

---

## Relationship to SPS and CMP

The SVD works alongside the SPS and CMP in the configuration management lifecycle:

- **SPS (DI-IPSC-81441A)** establishes the product baseline — the definitive file manifests for the CSCI's executable software and source files. The SPS defines *what* is the correct CSCI.
- **SVD (this DID)** describes a specific released version — *what* was released, to *whom*, *when*, and *what changed* since the last version. The SVD enables tracking of which version is installed at each site.
- **CMP (DI-SESS-80858D)** defines the configuration management process — procedures for identifying, controlling, and accounting for configuration items. The CMP governs the process by which SVDs are generated and controlled; the SVD is an artifact of that process.

---

## ICM Usage Notes

This DID defines the required content of a Software Version Description. An AI agent working within an ICM project can use this file to:

- **Generate** an SVD for each software release by: (1) inventorying all physical media and associated documentation in §3.1; (2) listing all computer files in the version in §3.2; (3) documenting all changes since the previous version in §3.3 (linked to problem reports and change proposals); (4) identifying site-specific adaptation data in §3.4; (5) providing installation instructions in §3.6; (6) documenting known issues in §3.7
- **Validate** a draft SVD for completeness — §3.1 must cover all physical media; §3.2 must enumerate all computer files; §3.3 must reference all problem reports and change proposals incorporated (except for initial release); §3.6 must include all five installation information elements (instructions, dependencies, security precautions, verification procedures, and point of contact); §3.7 must be present even if it states "None"
- **Handle the initial release special case:** §3.3 (Changes Installed) does not apply to the initial software version. All other sections apply.
- **Handle recipient-differentiated releases:** §1.1 requires identifying intended recipients to the extent that this affects what is released (e.g., source code may not be released to all recipients). §3.2 software contents and §3.6 installation instructions may differ by recipient — generate recipient-specific SVDs if needed.
- **Map to the SPS:** §3.2 (inventory of software contents) is the version-specific complement to SPS §3.1 and §3.2 (product baseline file manifests). The SPS files define what is correct; the SVD files describe what was released in this specific version.
- **Map to the CMP and CM status accounting:** the SVD is a primary input to CM status accounting (one of the five CM areas in EIA/SAE-649C also required by the CMP, DI-SESS-80858D). SVD §3.3 change history feeds the CM change log; §3.1–3.2 inventory feeds the CM item inventory.
- **Map to the STR:** if a software version was released following testing, the STR (DI-IPSC-81440A) documents the test results for that version. Cross-reference the SVD version identifier with the STR to establish the tested baseline.

When generating an SVD, begin with §3.2 (the computer file inventory) as the authoritative list, then work backward to §3.1 (physical media packaging) and forward to §3.3 (changes) and §3.6 (installation). The file inventory is the core artifact — all other sections support its delivery and use.
