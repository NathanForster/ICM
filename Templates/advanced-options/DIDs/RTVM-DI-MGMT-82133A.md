# DID: Requirements Traceability Verification Matrix (RTVM)

**DID Number:** DI-MGMT-82133A  
**Title:** Requirements Traceability Verification Matrix (RTVM)  
**Approval Date:** 2025-07-29  
**AMSC Number:** N10593  
**Preparing Activity:** AS  
**Project Number:** MGMT-2025-019  
**DTIC Applicable:** No  
**GIDEP Applicable:** No  
**Source PDF:** [RTVM-DI-MGMT-82133A.pdf](RTVM-DI-MGMT-82133A.pdf)

---

## Purpose

The RTVM provides **bidirectional traceability** from high-level system performance requirements down to the lowest-level requirements. It shows the traceability and allocation of requirements contained in the specification tree (performance specification, detailed specification, subsystem specification, software requirements specification, interface specification, and design documentation). The RTVM is also used to verify how each requirement is verified.

---

## Format Requirements

The RTVM shall be in an **electronic relational database format** that can be manipulated to show bidirectional requirements traceability and track the verification of each requirement.

---

## Required Content Structure

### Cover Page and Documentation

The RTVM software database files shall contain the following:

#### Cover Page
Enter: Title, Date of Issue, Revision Date, Contract Number, Contractor's name and address, Distribution Statement (as delineated in the contract), Export Control Warning Label (as applicable), and Security classification.

#### Record of Change Page
Enter a record of all changes made to the RTVM.

#### Database Architecture Description Pages
Enter a detailed description of the database, show relationships, and define all the terms/acronyms used in the database fields.

---

### Data Description

This section describes the data to be contained in the RTVM relational database. Each field is required unless marked optional.

#### 1 Tier 0 Unique Identification Number (UID)
Enter the UID for every requirement in the system configuration baseline (functional and physical).  
Example: `REQ-T0-PROJECTNAME-001`

#### 2 Source Document
For each specification and source document, enter the document number and title for the source of each requirement statement.

#### 3 Specification or Source Document Paragraph Number
Enter the specification or source document paragraph number for each requirement.

#### 4 Requirement Text (Tier 0)
Enter the specification or source document requirement text. Tier 0 requirements are broad statements of intent — they describe *what* the system needs to accomplish without specifying *how* it should be done.

#### 5 Tier 1 UID
Enter the UID for every requirement in the system configuration baseline (functional and physical).  
Example: `REQ-T1-PROJECTNAME-001`

#### 6 Tier 1 Requirement Text
Tier 1 requirements represent the highest level of abstraction in the project's requirements hierarchy. They articulate the fundamental needs, goals, and objectives that the project aims to satisfy.

#### 7 Tier 2 UID (if required)
Enter the UID for every requirement in the system configuration baseline (functional and physical).  
Example: `REQ-T2-PROJECTNAME-001`

#### 8 Tier 2 Requirement Text (if required)
Tier 2 requirements are derived directly from Tier 1 requirements. They translate high-level needs and objectives into more specific system-level or feature-level requirements. They define *what* the system or features within the system must *do* to satisfy the Tier 1 objectives.

#### 9 Tier 3 UID (if required)
Enter the UID for every requirement in the system configuration baseline (functional and physical).  
Example: `REQ-T3-PROJECTNAME-001`

#### 10 Tier 3 Requirement Text (if required)
Tier 3 requirements are derived directly from Tier 2 requirements. They represent the most detailed level of requirements specification, providing the granular instructions needed for developers to implement the system. They define how the system will achieve the functionality outlined in Tier 2.

#### 11 Requirement Type
The RTVM database shall identify if the requirement is "Derived" or "Decomposed".

#### 12 Requirement Attribute
For each requirement, define whether the requirement is a measure of performance, design parameter, software functional requirement, interface requirement, physical parameter, environmental or cybersecurity requirement. (This data field can encompass other data attributes if needed.)

#### 13 OEM Compliance of Requirement
The RTVM database shall identify if the OEM's compliance of the requirement is "Compliant", "Non-Compliant", or "Partial Compliant".

#### 14 Requirement Status
Identify the Requirement status for each requirement as "Approved", "Under Review", "Needs Revision", or "Rejected". The status should identify the latest revision number.

#### 15 Non-Conforming Requirements
For non-conforming requirements, enter the System Trouble Report (STR) and Deficiency Report (DR) number and title.

##### 15.1 Hyperlink
Provide hyper-link to the STR and DR databases.

#### 16 Design Reference
Enter the specific piece of design information (e.g., design document section, drawing, etc.) associated with each requirement.

#### 17 Requirement Allocation
Enter the specific system, subsystem, hardware item, component, Computer Software Configuration Item, Computer Software Component, and Computer Software Unit that each requirement has been allocated. System level requirements shall be allocated to all Configuration Items defined for the system.

#### 18 Form of End Product
Enter the form and maturity level of the end product used for verification. For example, the form can be the system, subsystem, unit level, software configuration item, and the maturity level can be the first article, production representative, prototype, or final configuration item.

#### 19 Verification Method
For each requirement, enter the verification method:

- **19.1 "Analysis"** — An element of verification that uses established technical or mathematical models or simulations, algorithms, charts, graphs, circuit diagrams, or other scientific principles and procedures to provide evidence that stated requirements were met. [Source: MIL-STD-961E with Change 2]
- **19.2 "Demonstration"** — An element of verification that involves the actual operation of an item to provide evidence that the required functions were accomplished under specific scenarios. The items may be instrumented and performance monitored. [Source: MIL-STD-961E with Change 2]
- **19.3 "Inspection"** — An element of verification that is generally nondestructive and typically includes the use of sight, hearing, smell, touch, and taste; simple physical manipulation; and mechanical and electrical gauging and measurement. [Source: MIL-STD-961E with Change 2]
- **19.4 "Test"** — An element of verification in which scientific principles and procedures are applied to determine the properties or functional capabilities of items. [Source: MIL-STD-961E with Change 2]

#### 20 Verification Document
Enter the document number, title, and date of the verification document that contains the verification method.

#### 21 Verification Document Paragraph
Enter the verification document paragraph number that provides the verification method.

#### 22 Verification Procedure
Enter the verification procedure section, and verification procedure step(s) that provide the verification method for each requirement.

#### 23 Other Tests
Enter the names of other tests conducted prior to verification of the requirement.

#### 24 Verification Results
Enter the results of the verification for each requirement. Did the system under test conform to the requirement? (Yes, No).

#### 25 Corrective Actions
Enter all corrective actions taken and the results of the corrective actions.

#### 26 Comments
Enter explanatory notes as required.

---

## Key Acronyms

| Acronym | Meaning |
|---------|---------|
| CI | Configuration Item |
| CSCI | Computer Software Configuration Item |
| DID | Data Item Description |
| DR | Deficiency Report |
| GIDEP | Government-Industry Data Exchange Program |
| KPP | Key Performance Parameter |
| OEM | Original Equipment Manufacturer |
| RTVM | Requirements Traceability Verification Matrix |
| SOW | Statement of Work |
| STR | System Trouble Report (or Software Test Report) |
| UID | Unique Identification Number |

---

## ICM Usage Notes

This DID defines the required content and structure of a contractually deliverable RTVM. An AI agent working within an ICM project can use this file to:

- **Generate** an RTVM database schema or spreadsheet by mapping each field in the Data Description section to a column; UIDs from fields 1/5/7/9 establish the tier hierarchy
- **Validate** RTVM completeness — every requirement must have all required fields populated; Tier 2 and Tier 3 fields are conditional on project scope
- **Map to the SDP and STP:** requirement allocation (field 17) maps to configuration items defined in the SDP (DI-IPSC-81427B); verification method and verification document fields (fields 19–22) link directly to the STP (DI-IPSC-81438A)
- **Track non-conformances:** field 15 links each non-conforming requirement to STR and DR tracking databases — a natural fit for ICM's corrective action workspace
- **Populate verification results** (fields 24–25) from test execution records after STR completion, closing the bidirectional traceability loop from requirements through tests to results

Note that this DID specifies a **relational database format** (not a document). An ICM agent generating an RTVM should produce a structured spreadsheet or database file with one row per requirement and the Data Description fields as columns. The Cover Page and Database Architecture Description should be separate tabs or companion documents.
