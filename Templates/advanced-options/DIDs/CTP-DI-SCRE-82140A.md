# DID: Cybersecurity Test Plan (CTP)

**DID Number:** DI-SCRE-82140A  
**Title:** Cybersecurity Test Plan (CTP)  
**Approval Date:** 2022-10-19  
**Supersedes:** DI-MGMT-82140  
**AMSC Number:** N10361  
**Preparing Activity:** AS  
**Project Number:** SCRE-2022-031  
**Source PDF:** [CTP-DI-SCRE-82140A.pdf](CTP-DI-SCRE-82140A.pdf)

---

## Purpose

The CTP describes plans for security qualification testing of hardware and software supporting:
- Risk Management Framework Assessment & Authorization (A&A)
- CYBERSAFE certification
- Meeting the Cyber Survivability Key Performance Parameter (KPP)
- Compliance with specified system security requirements

The CTP describes the test environment, identifies tests to be performed, and provides schedules for test activities.

---

## Format Requirements

Contractor format is acceptable.

---

## Required Content Structure

### 3.1 Test Environment

Identify one or more test sites and describe the test environment at each. If all tests are at a single site, present once. If multiple sites share the same environment, discuss together. Duplicative information may be reduced by referencing earlier descriptions.

#### 3.1.1 Software Items
Identify by name, number, and version all software items needed for testing at the site(s):
- Operating systems, compilers, communications software, related applications software, databases, input files
- Code auditors, dynamic path analyzers, test drivers, preprocessors, test data generators, test control software, other special test software, postprocessors
- **Automated security analysis tools** (CTP-specific)
- Purpose of each item, media type (tape, disk, etc.)
- Items expected to be supplied by the site
- Classified processing or security/privacy issues

> **Note:** Authoritative information already provided via other collection methods (such as RMF steps) shall be re-used to avoid duplication. Unique software items not identified in other authoritative sources shall be included here.

#### 3.1.2 Hardware and Firmware Items
Identify by name, number, and version all hardware and firmware items:
- Computer hardware, interfacing equipment, communications equipment, test data reduction equipment
- Extra peripherals (tape drives, printers, plotters), test message generators, test timing devices, test event records
- Purpose of each item, period of usage, number needed
- Items expected to be supplied by the site
- Classified processing or security/privacy issues

> **Note:** Authoritative information already provided via other collection methods (such as RMF steps) shall be re-used. Unique items not identified elsewhere shall be included here.

#### 3.1.3 Other Materials
Identify and describe any other materials needed for testing at the site(s):
- Automated security analysis tools, manuals, software listings, media containing data to be used in tests, sample listings of outputs, other forms or instructions
- Type, layout, and quantity of materials
- Items to be delivered to the site vs. supplied by the site
- Classified processing or security/privacy issues

#### 3.1.4 Proprietary Nature, Acquirer's Rights, and Licensing
Identify the proprietary nature, acquirer's rights, and licensing issues associated with each element of the software test environment.

#### 3.1.5 Installation, Testing, and Control
Tester's plans for:
- **3.1.5.1** Acquiring or developing each element of the test environment
- **3.1.5.2** Installing and testing each item of the test environment prior to its use
- **3.1.5.3** Controlling and maintaining each item of the test environment

#### 3.1.6 Participating Organizations
Organizations participating in testing at the test site(s), and the roles and responsibilities of each. This paragraph shall also ensure:
- Allotted time and physical space for government witness of any tests
- Ability to review test results without interfering with the conduct of the test

#### 3.1.7 Personnel
Number, type, and skill level of personnel needed during the test period at each site:
- Dates and times they will be needed
- Special needs (multi-shift operation, retention of key skills for continuity in extensive test programs)

#### 3.1.8 Orientation Plan
Any orientation and training to be given before and during the testing, related to personnel needs:
- User instruction, operator instruction, maintenance and control group instruction, orientation briefings to staff personnel
- If extensive training is anticipated, a separate plan may be developed and referenced here

#### 3.1.9 Tests to Be Performed
Identify the tests to be performed at the test site(s) (by referencing Section 3.2/3.3).

#### 3.1.10 Government Furnished Information and Equipment
Identify any required Government Furnished Information (GFI) and/or Government Furnished Equipment (GFE) and associated lead times required.

---

### 3.2 Test Identification

Identify and describe each test to which this CTP applies.

#### 3.2.1 General Information

##### 3.2.1.1 Test Levels
Describe the levels at which testing will be performed (e.g., component level, WRA level, or system level).

##### 3.2.1.2 Test Classes
Describe the types or classes of tests that will be performed (e.g., hardware/software penetration, IAVM, SCAP, IA Controls tests).

##### 3.2.1.3 General Test Conditions
Conditions that apply to all tests or to a group of tests. Examples:
- "Each test will include nominal, maximum, and minimum values"
- "Each test of type x will use live data"
- "Each attempt at penetration will assume encryption is/is not enabled"
- Statement of the extent of testing to be performed and rationale for the extent selected

##### 3.2.1.4 Test Progression
For progressive or cumulative tests: planned sequence or progression of tests.

##### 3.2.1.5 Data Recording, Reduction, and Analysis
Data recording, reduction, and analysis procedures to be used during and after the tests:
- Manual, automatic, and semi-automatic techniques for recording test results
- Manipulating raw results into a form suitable for evaluation
- Retaining results of data reduction and analysis

##### 3.2.1.6 Classification Level
Describe the classification level at which the tests and test results will be conducted and captured.

##### 3.2.1.7 Risks and Hazards
Describe the risks and hazards to be encountered during the test. Examples:
- Data sources will be wiped out during the tests
- Hard drives will be encrypted without the ability to recover the data
- Data results will be overwritten if the test runs past certain control points

---

### 3.3 Planned Tests

Describe the total scope of planned testing.

#### 3.3.1 Item(s) to Be Tested
Identify a subsystem, system, or other entity by name and project-unique identifier. Divide into subparagraphs to describe the testing planned for the item(s).

> Note: The "tests" in this plan are collections of test cases. There is no intent to describe each individual test case here.

##### 3.3.1.1 Project-Unique Identifier of a Test
For each test, provide:

- **3.3.1.1.1 Test Objective**, including:
  - **3.3.1.1.1.1** Threat represented (external nation state, external criminal, insider with restricted access) — drop-down type answer, no specifics to drive a classified report
  - **3.3.1.1.1.2** Test scope: what elements are included/excluded from this test
  - **3.3.1.1.1.3** Test level
  - **3.3.1.1.1.4** Test type or class

- **3.3.1.1.2** Qualification method(s) as specified in the requirements specification

- **3.3.1.1.3** Identifier of the security requirements and, if applicable, system requirements addressed by this test (may alternatively be provided in Section 3.4.1.6)

- **3.3.1.1.4** Special requirements (e.g., 48 hours of continuous facility time, weapon simulation, extent of test, use of special input or database)

- **3.3.1.1.5** Type of data to be recorded

- **3.3.1.1.6** Type of data recording/reduction/analysis to be employed

- **3.3.1.1.7** Assumptions and constraints: anticipated limitations on the test due to system or test conditions (timing, interfaces, equipment, personnel, database, etc.)

- **3.3.1.1.8** Safety, security, and privacy considerations associated with the test

---

### 3.4 Test Schedules

Schedules for conducting the tests identified in this plan.

#### 3.4.1 Sites and Time Frames
A listing or chart depicting the sites at which testing will be scheduled and the time frames during which testing will be conducted.

##### 3.4.1.1 Per-Site Schedule
For each test site, a schedule depicting activities and events in chronological order with supporting narrative:
- **3.4.1.1.1** On-site test period and periods assigned to major portions of testing
- **3.4.1.1.2** Pretest on-site period for setting up the test environment, other equipment, system orientation, and familiarization
- **3.4.1.1.3** Collection of database/data file values, input values, and other operational data needed for testing
- **3.4.1.1.4** Conducting the tests, including planned retesting
- **3.4.1.1.5** Preparation, review, and approval of the Cybersecurity Test Report (CSTR)
- **3.4.1.1.6** Requirements traceability:
  - **3.4.1.1.6.1** Traceability from each test in this plan to security requirements and, if applicable, system requirements it addresses
  - **3.4.1.1.6.2** Traceability from each security requirement and, if applicable, each system requirement covered by this plan to the test(s) that address it

---

### 3.5 Appendices
Appendices may be used for separately published information (charts, classified data). Each appendix shall be referenced in the main body where data would normally have been provided. Appendices may be bound as separate documents. Lettered alphabetically (A, B, etc.).

---

## Key Acronyms

| Acronym | Meaning |
|---------|---------|
| A&A | Assessment & Authorization |
| CSTR | Cybersecurity Test Report |
| CTP | Cybersecurity Test Plan |
| GFE | Government Furnished Equipment |
| GFI | Government Furnished Information |
| IAVM | Information Assurance Vulnerability Management |
| KPP | Key Performance Parameter |
| RMF | Risk Management Framework |
| SCAP | Security Content Automation Protocol |
| SOW | Statement of Work |
| WRA | Weapon Replaceable Assembly |

---

## ICM Usage Notes

This DID defines the required content of a contractually deliverable Cybersecurity Test Plan. An AI agent working within an ICM project can use this file to:

- **Generate** a compliant CTP outline by reading project security requirements and RMF artifacts from the project's cybersecurity workspace, then populating §3.1 (test environment) and §3.3 (planned tests)
- **Validate** a draft CTP for completeness — each planned test (§3.3.1.1) must address all eight required fields (3.3.1.1.1–3.3.1.1.8), including the threat representation dropdown fields at §3.3.1.1.1.1
- **Avoid duplication with RMF:** §3.1.1 and §3.1.2 explicitly require re-use of authoritative information already provided via RMF steps — an agent should cross-reference existing RMF artifacts before populating these sections
- **Map to the CTP suite:** the CTP pairs with the Cybersecurity Test Procedures/Descriptions (CSTP/CSTD, DI-MGMT-82141A) and the Cybersecurity Test Report (CSTR, DI-MGMT-82142A). The CTP identifies and schedules tests; the CSTP/CSTD provides step-by-step procedures; the CSTR records results.
- **Note §3.2.1.6 (classification level):** test results may be classified; ensure the project's ICM workspace structure accommodates classified artifact handling before generating this section

When generating a CTP, begin with §3.2.1 (general information — levels, classes, conditions) to frame the scope, then expand each planned test in §3.3, then build the schedule in §3.4.
