# DID: Software Test Plan (STP)

**DID Number:** DI-IPSC-81438A  
**Title:** Software Test Plan (STP)  
**Approval Date:** 1999-12-15  
**Supersedes:** DI-IPSC-81438  
**AMSC Number:** N7363  
**Office of Primary Responsibility:** NAVY/EC  
**Source PDF:** [STP-DI-IPSC-81438A.pdf](STP-DI-IPSC-81438A.pdf)

---

## Purpose

The STP describes plans for **qualification testing** of Computer Software Configuration Items (CSCIs) and software systems. It describes the software test environment, identifies the tests to be performed, and provides schedules for test activities.

There is typically a single STP per project. It enables the acquirer to assess the adequacy of planning for CSCI and, if applicable, software system qualification testing.

This DID is used when the developer is tasked to **develop and record plans for conducting qualification testing and/or system qualification testing** of a software system.

---

## General Instructions

- **Automated techniques:** Use of automated techniques is encouraged. "Document" means a collection of data regardless of medium.
- **Alternate presentation styles:** Diagrams, tables, matrices, and other presentation styles are acceptable substitutes for text when they make data more readable.
- **Substitute documents:** Commercial or other existing documents may be substituted if they contain the required data.
- **Tailoring:** If a paragraph is tailored out, the resulting document shall state the paragraph number and title followed by "This paragraph has been tailored out."

---

## Format Requirements

- Contractor format unless otherwise specified in the CDRL (DD 1423)
- May be delivered on paper or electronic media (ASCII, CALS, word processor, CASE tool, etc.)
- Must include: title page, table of contents, unique page numbers with document number/version/date

---

## Required Content Structure

### 1. Scope
#### 1.1 Identification
Full identification of the system and software: identification number(s), title(s), abbreviation(s), version number(s), release number(s).

#### 1.2 System Overview
- Purpose of the system and software
- General nature of system and software
- History of development, operation, and maintenance
- Project sponsor, acquirer, user, developer, and support agencies
- Current and planned operating sites
- Other relevant documents

#### 1.3 Document Overview
Summary of this document's purpose and contents; any security or privacy considerations associated with its use.

#### 1.4 Relationship to Other Plans
Relationship of the STP to related project management plans (e.g., the SDP).

---

### 2. Referenced Documents
List all referenced documents: number, title, revision, date. Identify source for documents not available through normal Government stocking activities.

---

### 3. Software Test Environment

Describe the software test environment at each intended test site. Reference may be made to the SDP for resources already described there.

#### 3.x (Name of Test Site)
One subparagraph per test site. If all tests are at a single site, present once. If multiple sites share the same environment, they may be discussed together.

##### 3.x.1 Software Items
Identify by name, number, and version all software items needed for testing at this site:
- Operating systems, compilers, communications software, related applications, databases, input files
- Code auditors, dynamic path analyzers, test drivers, preprocessors, test data generators, test control software, post-processors, and other special test software
- Purpose of each item, media type (tape, disk, etc.)
- Items expected to be supplied by the site
- Classified processing or security/privacy issues

##### 3.x.2 Hardware and Firmware Items
Identify by name, number, and version all hardware and firmware items:
- Computer hardware, interfacing equipment, communications equipment, test data reduction equipment
- Extra peripherals (tape drives, printers, plotters), test message generators, test timing devices, test event records
- Purpose of each item, period of usage, number of each item needed
- Items expected to be supplied by the site
- Classified processing or security/privacy issues

##### 3.x.3 Other Materials
Identify any other materials needed for testing:
- Manuals, software listings, media containing software to be tested, media containing data, sample listings of outputs, other forms or instructions
- Type, layout, and quantity of materials
- Items to be delivered to site vs. supplied by site
- Classified processing or security/privacy issues

##### 3.x.4 Proprietary Nature, Acquirer's Rights, and Licensing
Identify proprietary nature, acquirer's rights, and licensing issues for each element of the software test environment.

##### 3.x.5 Installation, Testing, and Control
Developer's plans for:
- a. Acquiring or developing each element of the software test environment
- b. Installing and testing each item prior to use
- c. Controlling and maintaining each item

##### 3.x.6 Participating Organizations
Organizations participating in testing at this site and the roles and responsibilities of each.

##### 3.x.7 Personnel
Number, type, and skill level of personnel needed during the test period:
- Dates and times they will be needed
- Special needs (multishift operation, key skill retention for continuity in extensive test programs)

##### 3.x.8 Orientation Plan
Orientation and training to be given before and during testing:
- User instruction, operator instruction, maintenance and control group instructions, orientation briefings to staff
- If extensive training is anticipated, a separate plan may be developed and referenced

##### 3.x.9 Tests to Be Performed
Identify (by referencing Section 4) the tests to be performed at this test site.

---

### 4. Test Identification

Identify and describe each test to which this STP applies.

#### 4.1 General Information

##### 4.1.1 Test Levels
Describe the levels at which testing will be performed (e.g., CSCI level, system level).

##### 4.1.2 Test Classes
Describe the types or classes of tests to be performed (e.g., timing tests, erroneous input tests, maximum capacity tests).

##### 4.1.3 General Test Conditions
Conditions that apply to all tests or to a group of tests:
- Each test shall include nominal, maximum, and minimum values
- "Each test of type x shall use live data"
- "Execution size and time shall be measured for each CSCI"
- Statement of the extent of testing to be performed and rationale for the extent selected
- Extent of testing expressed as a percentage of some well-defined total quantity (samples of discrete operating conditions, values, or other sampling approach)
- Approach to be followed for retesting/regressing testing

##### 4.1.4 Test Progression
For progressive or cumulative tests: planned sequence or progression of tests.

##### 4.1.5 Data Recording, Reduction, and Analysis
Identify and describe the data recording, reduction, and analysis procedures to be used during and after tests:
- Manual, automatic, and semi-automatic techniques for recording test results
- Manipulating raw results into a form suitable for evaluation
- Retaining results of data reduction and analysis

#### 4.2 Planned Tests

One subparagraph per CSCI, subsystem, system, or other entity being tested.

##### 4.2.x (Item(s) to Be Tested)
Identify the CSCI, subsystem, system, or other entity by name and project-unique identifier. Divide into subparagraphs per test. Note: tests in this plan are collections of test cases — individual test cases are not described here.

##### 4.2.x.y (Project-Unique Identifier of a Test)
For each test, provide:
- a. Test objective
- b. Test level
- c. Test type or class
- d. Qualification method(s) as specified in the requirements specification
- e. Identifier of CSCI requirements addressed (and software system requirements if applicable) — may alternatively be provided in Section 6
- f. Special requirements (e.g., 48 hours of continuous facility time, weapon simulation, extent of test, use of special input or database)
- g. Type of data to be recorded
- h. Type of data recording/reduction/analysis to be employed
- i. Assumptions and constraints (anticipated limitations due to system or test conditions: timing, interfaces, equipment, personnel, database, etc.)
- j. Safety, security, and privacy considerations associated with the test

---

### 5. Test Schedules

Schedules for conducting the tests identified in this plan:

- a. Listing or chart of test sites and time frames during which testing will be scheduled
- b. Schedule for each test site (chronological order with supporting narrative):
  1. On-site test period and periods assigned to major test portions
  2. Pretest on-site period for setting up the software test environment, system debugging, orientation, and familiarization
  3. Collection of database/data file values, input values, and other operational data
  4. Conducting the tests, including planned retesting
  5. Preparation, review, and approval of the Software Test Report (STR)

---

### 6. Requirements Traceability

- a. **Test → Requirements:** Traceability from each test in this plan to the CSCI requirements (and software system requirements, if applicable) it addresses. May alternatively be provided in 4.2.x.y (item e) and referenced here.
- b. **Requirements → Tests:** Traceability from each CSCI requirement (and software system requirement, if applicable) to the test(s) that cover it. Shall cover CSCI requirements in all applicable Software Requirements Specifications (SRSs), associated Interface Requirements Specifications (IRSs), and — for software systems — system requirements in all applicable System/Subsystem Specifications (SSSs) and associated system-level IRSs.

---

### 7. Notes
- Background information, glossary, rationale
- Alphabetical listing of all acronyms and abbreviations with meanings
- List of terms and definitions needed to understand the document

---

### A. Appendices
- May be used for separately published information (charts, classified data)
- Each appendix referenced in the main body where data would normally appear
- May be bound as separate documents
- Lettered alphabetically (A, B, etc.)

---

## Key Acronyms

| Acronym | Meaning |
|---------|---------|
| CASE | Computer-Aided Software Engineering |
| CDRL | Contract Data Requirements List |
| CSCI | Computer Software Configuration Item |
| DID | Data Item Description |
| IRS | Interface Requirements Specification |
| SDP | Software Development Plan |
| SRS | Software Requirements Specification |
| SSS | System/Subsystem Specification |
| STR | Software Test Report |
| STP | Software Test Plan |

---

## ICM Usage Notes

This DID defines the required content of a contractually deliverable STP. An AI agent working within an ICM project can use this file to:

- **Generate** a compliant STP outline or draft using project context from ICM.md and CONTEXT.md, with test site details from the engineering environment workspace
- **Validate** a draft STP for completeness — every section (1–6) and every 4.2.x.y test entry must include all required fields (a–j)
- **Map** to the SDP (DI-IPSC-81427B): the STP expands on the test planning described in SDP §3.8.a (CSCI test planning), §3.8.k (CSCI qualification testing), and §3.8.m (system qualification testing)
- **Generate traceability matrices** (Section 6) by cross-referencing test identifiers against SRS/IRS/SSS requirement identifiers — a natural fit for ICM's state-tracking and traceability workspace patterns
- **Note the relationship to the STR:** Section 5 schedules include STR preparation; the STP and STR are paired deliverables

When generating an STP, begin with Section 3 (test environment) by reading the project's engineering environment descriptions, then populate Section 4 (test identification) from the requirements workspace.
