# DID: Software Product Specification (SPS)

**DID Number:** DI-IPSC-81441A  
**Title:** Software Product Specification (SPS)  
**Approval Date:** 1999-12-15  
**Supersedes:** DI-IPSC-81441  
**AMSC Number:** N7366  
**Preparing Activity:** N/SPAWAR  
**Source PDF:** [SPS-DI-IPSC-81441A.pdf](SPS-DI-IPSC-81441A.pdf)

---

## Purpose

The SPS contains or references the executable software, source files, and software support information — including "as built" design information and compilation, build, and modification procedures — for a Computer Software Configuration Item (CSCI).

The SPS can be used to order the executable software and/or source files for a CSCI and is the primary software support document for the CSCI. Note: Different organizations have different policies for ordering delivery of software — these policies should be determined before applying this DID.

This DID is used when the developer is tasked to prepare executable software, source files, "as built" CSCI design, and/or related support information for delivery.

---

## Key Concept: Software as Product Baseline

> **Note from §3:** The software itself — not a design description — is the criterion for a "valid copy" of the CSCI. Previous versions of this DID required presenting the "as built" software design (modeled on hardware development where the product specification presents the final design). For software, this approach does not apply because software consists of electronic components. The software itself establishes the product baseline, not a design description. If any portion of this specification is placed under acquirer configuration control, it should be limited to §3, as the software itself is what establishes the product baseline.

---

## Format Requirements

Contractor format unless otherwise specified in the CDRL (DD 1423). Title page shall include signature blocks for: the developer representative authorized to release the document; the acquirer representative authorized to approve the document; and the dates of release/approval.

---

## Required Content Structure

### 1. Scope

#### 1.1 Identification
Full identification of the system and the software to which this document applies: identification number(s), title(s), abbreviation(s), version number(s), and release number(s).

#### 1.2 System Overview
Briefly state the purpose of the system and the software to which this document applies. Describe the general nature of the system and software; summarize history of system development, operation, and maintenance; identify the project sponsor, acquirer, user, developer, and support agencies; identify current and planned operating sites; list other relevant documents.

#### 1.3 Document Overview
Summarize the purpose and contents of this document and describe any security or privacy considerations associated with its use.

---

### 2. Referenced Documents
List the number, title, revision, and date of all documents referenced. Identify the source for all referenced documents not available through normal Government stocking activities.

---

### 3. Requirements

Divided into the following paragraphs to establish the requirements that a body of software must meet to be considered a valid copy of the CSCI.

#### 3.1 Executable Software
Provide by reference to enclosed or otherwise provided electronic media the executable software for the CSCI, including any batch files, command files, data files, or other software files needed to install and operate the software on its target computer(s). In order for a body of software to be considered a valid copy of the CSCI's executable software, it must be shown to match these files exactly.

#### 3.2 Source Files
Provide by reference to enclosed or otherwise provided electronic media the source files for the CSCI, including any batch files, command files, data files, or other files needed to regenerate the executable software for the CSCI. In order for a body of software to be considered a valid copy of the CSCI's source files, it must be shown to match these files exactly.

#### 3.3 Packaging Requirements
State the requirements, if any, for packaging and marking copies of the CSCI.

---

### 4. Qualification Provisions

State the method(s) to be used to demonstrate that a given body of software is a valid copy of the CSCI. For example:
- For executable files: establish that each executable file referenced in §3.1 has an identically-named counterpart in the software in question, and that each such counterpart can be shown, via bit-for-bit comparison, check sum, or other method, to be identical to the corresponding executable file
- For source files: comparable method using the source files referenced in §3.2

---

### 5. Software Support Information

Divided into the following paragraphs to provide information needed to support the CSCI.

#### 5.1 "As Built" Software Design
Contains, or references an appendix or other deliverable document that contains, information describing the design of the "as built" CSCI. The information shall be the same as that required in a Software Design Description (SDD, DI-IPSC-81435B), Interface Design Description (IDD, DI-IPSC-81436), and Database Design Description (DBDD, DI-IPSC-81437), as applicable.

- If these documents or their equivalents are to be delivered for the "as built" CSCI, this paragraph shall reference them.
- If not, the information shall be provided in this document.
- Information provided in headers, comments, and code of the source code listings may be referenced and need not be repeated in this section.
- If the SDD, IDD, or DBDD is included in an appendix, the paragraph numbers and page numbers need not be changed.

#### 5.2 Compilation/Build Procedures
Describe, or reference an appendix that describes, the compilation/build process to be used to create the executable files from the source files and to prepare the executable files to be loaded into firmware or other distribution media. Specify:
- The compiler(s)/assembler(s) to be used, including version numbers
- Other hardware and software needed, including version numbers
- Any settings, options, or conventions to be used
- Procedures for compiling/assembling, linking, and building the CSCI and the software system/subsystem containing the CSCI, including variations for different sites, configurations, versions, etc.

Build procedures above the CSCI level may be presented in one SPS and referenced from the others.

#### 5.3 Modification Procedures
Describe the procedures that must be followed to modify the CSCI. Include or reference information on the following, as applicable:
- **a.** Support facilities, equipment, and software, and procedures for their use
- **b.** Database/data files used by the CSCI and procedures for using and modifying them
- **c.** Design, coding, and other conventions to be followed
- **d.** Compilation/build procedures if different from those in §5.2
- **e.** Integration and testing procedures to be followed

#### 5.4 Computer Hardware Resource Utilization
Describe the "as built" CSCI's measured utilization of computer hardware resources:
- Processor capacity
- Memory capacity
- Input/output device capacity
- Auxiliary storage capacity
- Communications/network equipment capacity

Shall cover all computer hardware resources included in utilization requirements for the CSCI, in system-level resource allocations affecting the CSCI, and in resource utilization measurement planning in the Software Development Plan.

For each computer hardware resource, include:
- **a.** The CSCI requirements or system-level resource allocations being satisfied (alternatively, the traceability to CSCI requirements may be provided in §6.c)
- **b.** The assumptions and conditions on which the utilization data are based (typical usage, worst-case usage, assumption of certain events)
- **c.** Any special considerations affecting the utilization (virtual memory, overlays, multiprocessors, operating system overhead, library software, or other implementation overhead)
- **d.** The units of measure used (percentage of processor capacity, cycles per second, bytes of memory, kilobytes per second)
- **e.** The level(s) at which the estimates or measures are made (software unit, CSCI, or executable program)

If all utilization data for a given computer hardware resource is presented in a single SPS, that SPS and paragraph shall be referenced from others.

---

### 6. Requirements Traceability

This section shall provide:

- **a.** Traceability from each CSCI source file to the software unit(s) that it implements
- **b.** Traceability from each software unit to the source files that implement it
- **c.** Traceability from each computer hardware resource utilization measurement given in §5.4 to the CSCI requirements it addresses (alternatively, this traceability may be provided in §5.4)
- **d.** Traceability from each CSCI requirement regarding computer hardware resource utilization to the utilization measurements given in §5.4

---

### 7. Notes
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
| DBDD | Database Design Description |
| IDD | Interface Design Description |
| SDD | Software Design Description |
| SPS | Software Product Specification |

---

## ICM Usage Notes

This DID defines the required content of a Software Product Specification. An AI agent working within an ICM project can use this file to:

- **Generate** an SPS by: (1) enumerating all executable files and source files for the CSCI in §3.1 and §3.2 as a manifest; (2) specifying the exact-match qualification criterion in §4; (3) populating §5 with "as built" design reference (or content if SDD/IDD/DBDD are not separately delivered), build procedures, modification procedures, and measured hardware resource utilization
- **Validate** a draft SPS for completeness — §3.1 and §3.2 must enumerate or reference all files; §4 must specify the comparison method (bit-for-bit, checksum, etc.); §5.2 must include compiler versions and all build settings; §5.4 must cover all hardware resources named in CSCI utilization requirements; §6 traceability must be four-directional (source file ↔ software unit, utilization measurement ↔ CSCI requirement)
- **Understand the product baseline distinction:** the SPS is the product baseline document — it establishes what the "official" software is through the exact file manifests in §3. Unlike hardware product specifications, the SPS does not describe the design as the criterion; it points to the actual files. The "as built" design documentation in §5.1 is support information, not the baseline artifact.
- **Map to the SDD:** if the SDD (DI-IPSC-81435B) is delivered, §5.1 of the SPS references it. If not, §5.1 must contain the equivalent SDD content. Do not duplicate information already in a delivered SDD — reference it.
- **Map to the SVD:** the SVD (DI-IPSC-81442A) describes what is in a software version release (inventory of materials and files). The SVD §3.2 (inventory of software contents) complements the SPS §3 (file manifests) — the SPS establishes the product baseline definition while the SVD describes a specific released version.
- **Map to the RTVM:** §6.c–d traceability from utilization measurements to CSCI requirements provides data for the RTVM (DI-MGMT-82133A) §3.2.21 (Verification Results) for computer resource utilization requirements.

When generating an SPS, establish the §3.1 and §3.2 file manifests first (these are the core product baseline artifacts), then work through §5 support information. The file manifests in §3 are what make the SPS a binding product baseline document — they must be complete and precise.
