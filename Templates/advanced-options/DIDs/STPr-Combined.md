# Combined DID Digest: Software Test Procedure (STPr)

**Compiled from two source DIDs:**

| DID Number | Title | Approval Date | Supersedes | Office |
|---|---|---|---|---|
| DI-IPSC-81439A | Software Test Description (STD) | 1999-12-15 | DI-IPSC-81439 | NAVY/EC (N/SPAWAR) |
| DI-NDTI-80603A | Test Procedure | 2006-11-14 | DI-NDTI-80603 | NS/DA023 |

**Source PDFs:** [STD-DI-IPSC-81439A.pdf](STD-DI-IPSC-81439A.pdf) · [TPr-DI-NDTI-80603A.pdf](TPr-DI-NDTI-80603A.pdf)

---

## Why These Two DIDs Are Combined

**DI-IPSC-81439A (STD)** governs software qualification testing under MIL-STD-498. It provides the test case–level structure: preparations, descriptions, inputs, criteria, procedures, and requirements traceability. It is the authoritative source for CSCI and software system qualification test documentation.

**DI-NDTI-80603A (TPr)** governs hardware/equipment test procedures for developmental, qualification, environmental, and acceptance testing. It adds rigor around physical setup: formal cover page metadata, record of changes, calibration requirements for test equipment, physical wiring/connection diagrams, ordered tables of tests, data sheets with technician signatures, and support equipment requirements.

Together they define a complete Software Test Procedure (STPr) applicable to modern defense software programs that include both software CSCI testing and hardware-in-the-loop or bench-level testing.

**When to use which source for a given section:**
- Software requirements, CSCI test cases, traceability to SRS/IRS/SSS → follow STD structure
- Physical hardware setup, calibration records, data sheets, support equipment → follow TPr structure
- Both apply to: step-by-step procedures, expected results, pass/fail criteria, assumptions/constraints

---

## Format Requirements

- Contractor format acceptable (both DIDs)
- TPr adds: 8½ × 11 inch paper, bound so pages may be removed or inserted without damage
- May be delivered on paper or electronic media; may reside in a CASE tool
- Safety precautions shall be marked by WARNING or CAUTION; security and privacy considerations included as applicable

---

## Required Content Structure

---

### PART 1 — FRONT MATTER
*(Source: DI-NDTI-80603A §3.1)*

#### 1.1 Cover and Title Page
The cover and title page shall include:
- a. Date of issue
- b. Revision date (if applicable)
- c. Procedure document identification number
- d. Contract number
- e. Contractor's name and address
- f. Type of procedure (e.g., first article test, developmental evaluation, qualification, environmental, acceptance, or other — specify)
- g. Identification of the system, subsystem, software, or equipment to be tested
- h. Security classification (if applicable)

#### 1.2 Record of Changes
A record of change pages shall be included to provide for tracking of changes to the test procedures.

#### 1.3 Table of Contents
Required when more than one test procedure is included in the document. Shall identify the page location of each procedure number, procedure title, and related equipment nomenclature.

---

### PART 2 — SCOPE
*(Source: DI-IPSC-81439A §1)*

#### 2.1 Identification
Full identification of the system and software to which this document applies: identification number(s), title(s), abbreviation(s), version number(s), release number(s).

#### 2.2 System Overview
- Purpose of the system and software
- General nature of the system and software
- History of system development, operation, and maintenance
- Project sponsor, acquirer, user, developer, and support agencies
- Current and planned operating sites
- Other relevant documents

#### 2.3 Document Overview
Summary of this document's purpose and contents. Any security or privacy considerations associated with its use.

---

### PART 3 — REFERENCED DOCUMENTS
*(Source: DI-IPSC-81439A §2; DI-NDTI-80603A §3.2.3.4)*

List the number, title, revision, and date of all documents referenced in this document. Identify the source for all documents not available through normal Government stocking activities. Include:
- Applicable specifications, standards, plans, or contract work statements (cite specific paragraphs containing prescribing contract requirements)
- Software requirements specifications (SRS), interface requirements specifications (IRS), system/subsystem specifications (SSS) — as applicable
- Published operating manuals and software manuals referenced in procedure steps

---

### PART 4 — TEST PREPARATIONS
*(Primary source: DI-IPSC-81439A §3; augmented by DI-NDTI-80603A §3.2.4, §3.2.6.a, §3.2.8)*

One subparagraph (4.x) per test, identified by project-unique identifier with a brief description. When information required duplicates information previously specified for another test, that information may be referenced rather than repeated.

#### 4.x (Project-Unique Identifier of a Test)

##### 4.x.1 Hardware Preparation
*(STD §3.x.1 + TPr §3.1.1, §3.2.4, §3.2.6.a)*

Describe procedures to prepare the hardware for the test. Reference may be made to published operating manuals. Provide as applicable:

- a. The specific hardware to be used, identified by name and, if applicable, number
- b. Any switch settings and cabling necessary to connect the hardware
- c. One or more diagrams to show hardware, interconnecting control, and data paths (including test equipment connections and instrumentation points)
- d. Step-by-step instructions for placing the hardware in a state of readiness

**Required test equipment** — for each piece of test equipment needed to perform the procedure:
- Nomenclature
- Use of test equipment
- Model number (if applicable)
- Manufacturer (if mandatory)
- Accuracy and calibration requirements
- Range or spectrum of measurements required

**Support requirements** — any special support needs:
- Use of special facilities or test ranges
- Personnel requirements (numbers, types, qualifications)
- Unusual electrical, hydraulic, pneumatic, or other requirements
- Support equipment requirements

##### 4.x.2 Software Preparation
*(STD §3.x.2)*

Describe procedures to prepare the item(s) under test and any related software, including data, for the test. Reference may be made to published software manuals. Provide as applicable:

- a. The specific software to be used in the test
- b. The storage medium of the item(s) under test (e.g., magnetic tape, diskette)
- c. The storage medium of any related software (e.g., simulators, test drivers, databases)
- d. Instructions for loading the software, including required sequence
- e. Instructions for software initialization common to more than one test case

##### 4.x.3 Other Pre-Test Preparations
*(STD §3.x.3)*

Any other pre-test personnel actions, preparations, or procedures necessary to perform the test.

---

### PART 5 — TEST DESCRIPTIONS
*(Primary source: DI-IPSC-81439A §4; augmented by DI-NDTI-80603A §3.2.1–§3.2.7)*

#### 5.x (Project-Unique Identifier of a Test)
Identify the test by project-unique identifier. Divide into subparagraphs per test case. When required information duplicates previously provided information, reference rather than repeat.

**Table of tests** *(TPr §3.2.5):* Include a table listing each test to be performed under this procedure, in the sequence to be performed, identified to the procedure paragraph and the related specification/contract requirement.

##### 5.x.y (Project-Unique Identifier of a Test Case)
Identify the test case by project-unique identifier, state its purpose, and provide a brief description. The following subparagraphs provide a detailed description.

###### 5.x.y.1 Requirements Addressed
*(STD §4.x.y.1)*

Identify the CSCI or system requirements addressed by this test case. (Alternatively, this information may be provided in Section 6 — Requirements Traceability.)

Cite the prescribing requirement paragraph in the applicable specification, standard, plan, or contract work statement. *(TPr §3.2.3.3)*

###### 5.x.y.2 Prerequisite Conditions
*(STD §4.x.y.2)*

Identify any prerequisite conditions that must be established prior to performing the test case. Discuss as applicable:

- a. Hardware and software configuration
- b. Flags, initial breakpoints, pointers, control parameters, or initial data to be set/reset prior to test commencement
- c. Preset hardware conditions or electrical states necessary to run the test case
- d. Initial conditions to be used in making timing measurements
- e. Conditioning of the simulated environment
- f. Other special conditions peculiar to the test case

###### 5.x.y.3 Test Inputs
*(STD §4.x.y.3)*

Describe the test inputs necessary for the test case. Provide as applicable:

- a. Name, purpose, and description (e.g., range of values, accuracy) of each test input
- b. Source of the test input and the method to be used for selecting it
- c. Whether the test input is real or simulated
- d. Time or event sequence of test input
- e. The manner in which the input data will be controlled to:
  1. Test the item(s) with a minimum/reasonable number of data types and values
  2. Exercise the item(s) with a range of valid data types and values that test for overload, saturation, and other "worst case" effects
  3. Exercise the item(s) with invalid data types and values to test for appropriate handling of irregular inputs
  4. Permit retesting, if necessary

###### 5.x.y.4 Expected Test Results
*(STD §4.x.y.4)*

Identify all expected test results for the test case. Both intermediate and final test results shall be provided, as applicable.

###### 5.x.y.5 Criteria for Evaluating Results
*(STD §4.x.y.5)*

Identify the criteria to be used for evaluating intermediate and final results of the test case. Provide as applicable:

- a. The range or accuracy over which an output can vary and still be acceptable
- b. Minimum number of combinations or alternatives of input and output conditions that constitute an acceptable test result
- c. Maximum/minimum allowable test duration, in terms of time or number of events
- d. Maximum number of interrupts, halts, or other system breaks that may occur
- e. Allowable severity of processing errors
- f. Conditions under which the result is inconclusive and re-testing is to be performed
- g. Conditions under which the outputs are to be interpreted as indicating irregularities in input test data, in the test database/data files, or in test procedures
- h. Allowable indications of the control, status, and results of the test and the readiness for the next test case (may be output of auxiliary test software)
- i. Additional criteria not mentioned above

###### 5.x.y.6 Test Procedure
*(STD §4.x.y.6 + TPr §3.2.6)*

Define the test procedure as a series of individually numbered steps listed sequentially in the order to be performed. Test procedures may be included as an appendix and referenced here. The appropriate level of detail depends on the type of software being tested — for some software, each keystroke may be a separate step; for most software, each step may include a logically related series of keystrokes or other actions. The appropriate level of detail is the level at which it is useful to specify expected results and compare them to actual results.

For each step, provide as applicable:

- a. Test operator actions and equipment operation, including commands:
  1. Initiate the test case and apply test inputs
  2. Inspect test conditions
  3. Perform interim evaluations of test results
  4. Record data
  5. Halt or interrupt the test case
  6. Request data dumps or other aids, if needed
  7. Modify the database/data files
  8. Repeat the test case if unsuccessful
  9. Apply alternate modes as required by the test case
  10. Terminate the test case

  *Additionally (TPr §3.2.6):*
  - Test set-up diagrams, including test equipment connections
  - Input and output instrumentation points
  - Test item operating limits and test conditions to be imposed
  - Performance parameters to be measured
  - Caution and safety warnings as appropriate

- b. Expected result and evaluation criteria for each step

- c. If the test case addresses multiple requirements: identification of which test procedure step(s) address which requirements (alternatively, provide in Section 6)

- d. Actions to follow in the event of a program stop or indicated error:
  1. Recording of critical data from indicators for reference purposes
  2. Halting or pausing time-sensitive test-support software and test apparatus
  3. Collection of system and operator records of test results

- e. Procedures to reduce and analyze test results to accomplish the following:
  1. Detect whether an output has been produced
  2. Identify media and location of data produced by the test case
  3. Evaluate output as a basis for continuation of test sequence
  4. Evaluate test output against required output

###### 5.x.y.7 Assumptions and Constraints
*(STD §4.x.y.7)*

Identify any assumptions made and constraints or limitations imposed on the description of the test case due to system or test conditions (timing, interfaces, equipment, personnel, database/data files). If waivers or exceptions to specified limits and parameters are approved, identify them and address their effects and impacts upon the test case.

---

### PART 6 — DATA SHEETS
*(Source: DI-NDTI-80603A §3.2.7)*

Data sheets shall be included with the procedure, or separately attached at the end of all procedures. They shall provide for:

- a. Identification of item tested, including model and serial numbers
- b. Recording of test measurements
- c. Identification of required or objective performance values, with tolerances
- d. Identification of applicable procedure paragraphs
- e. Date of test
- f. Signature of technician or inspector performing the tests

---

### PART 7 — REQUIREMENTS TRACEABILITY
*(Source: DI-IPSC-81439A §5)*

- **a. Test case → requirements (upward):** Traceability from each test case in this STPr to the system or CSCI requirements it addresses. If a test case addresses multiple requirements, traceability from each set of test procedure steps to the requirement(s) addressed. (Alternatively, provided in §5.x.y.1.)

- **b. Requirements → test cases (downward):** Traceability from each system or CSCI requirement covered by this STPr to the test case(s) that address it.
  - For CSCI testing: traceability from each CSCI requirement in the CSCI's SRS and associated IRSs
  - For system testing: traceability from each system requirement in the SSS and associated IRSs
  - If a test case addresses multiple requirements: the traceability shall indicate the particular test procedure steps that address each requirement

---

### PART 8 — NOTES
*(Source: DI-IPSC-81439A §6)*

General information that aids in understanding this document:
- Background information, glossary, rationale
- Alphabetical listing of all acronyms, abbreviations, and their meanings
- List of terms and definitions needed to understand this document

---

### PART A — APPENDICES
*(Both DIDs)*

Appendices may be used for separately published information (charts, classified data). Each appendix shall be referenced in the main body where the data would normally have been provided. Appendices may be bound as separate documents. Lettered alphabetically (A, B, etc.).

Common appendix content:
- Complete test procedures (when referenced from §5.x.y.6 body)
- Detailed data sheets
- Classified test data

---

## Source DID Comparison

| Requirement Area | STD (DI-IPSC-81439A) | TPr (DI-NDTI-80603A) | Combined STPr |
|---|---|---|---|
| Front matter / cover metadata | Minimal (title page) | Detailed (type of test, 8 fields) | Part 1 — from TPr |
| Scope sections | Full (1.1–1.3) | None | Part 2 — from STD |
| Referenced documents | §2 | §3.2.3.4 (within intro) | Part 3 — merged |
| Hardware preparation | §3.x.1 (4 items) | §3.2.4 (calibration) + §3.2.6.a (diagrams) + §3.2.8 (support) | Part 4.x.1 — merged |
| Software preparation | §3.x.2 (5 items) | N/A | Part 4.x.2 — from STD |
| Test equipment calibration | Not specified | §3.2.4 (6 fields per item) | Part 4.x.1 — from TPr |
| Table of tests | Not specified | §3.2.5 | Part 5.x preamble — from TPr |
| Test case prerequisites | §4.x.y.2 (6 items a–f) | Implicit | Part 5.x.y.2 — from STD |
| Test inputs | §4.x.y.3 (5 items a–e) | Implicit | Part 5.x.y.3 — from STD |
| Criteria for evaluating results | §4.x.y.5 (8 items a–i) | Implicit pass/fail | Part 5.x.y.5 — from STD |
| Step-by-step procedure | §4.x.y.6 (10 operator actions + analysis) | §3.2.6 (setup diagrams + parameters + cautions) | Part 5.x.y.6 — merged |
| Data sheets | Not specified | §3.2.7 (6 fields, signed) | Part 6 — from TPr |
| Requirements traceability | §5 (bidirectional, SRS/IRS/SSS) | Not specified | Part 7 — from STD |
| Notes / acronyms | §6 | Implicit | Part 8 — from STD |

---

## Key Acronyms

| Acronym | Meaning |
|---------|---------|
| CASE | Computer-Aided Software Engineering |
| CDRL | Contract Data Requirements List |
| CSCI | Computer Software Configuration Item |
| DID | Data Item Description |
| GFE | Government Furnished Equipment |
| IRS | Interface Requirements Specification |
| SRS | Software Requirements Specification |
| SSS | System/Subsystem Specification |
| STD | Software Test Description |
| STPr | Software Test Procedure |
| STP | Software Test Plan |
| STR | Software Test Report |
| TPr | Test Procedure |

---

## ICM Usage Notes

This combined digest defines the required content of a Software Test Procedure (STPr), synthesizing two complementary DIDs. An AI agent working within an ICM project can use this file to:

- **Generate** a complete STPr by populating Part 1 (front matter) from contract metadata, Part 2 (scope) from project ICM.md/CONTEXT.md, then iterating over tests from the STP (DI-IPSC-81438A) to generate Parts 4–5 for each
- **Validate** a draft STPr for completeness — each test case (§5.x.y) must have all seven subsections; §5.x.y.5 criteria must address all eight items a–i; data sheets (Part 6) must include technician signature fields; requirements traceability (Part 7) must be bidirectional
- **Apply DID-appropriate depth by test type:**
  - Pure software CSCI test cases → STD structure is authoritative; TPr additions are supplemental
  - Hardware-in-the-loop, bench tests, or acceptance tests → TPr additions (calibration, setup diagrams, data sheets, support equipment) become mandatory
  - Mixed test cases → use the combined structure fully
- **Map to related DIDs:**
  - STP (DI-IPSC-81438A): the STP identifies and schedules tests; the STPr expands each test into step-level procedures. Test identifiers in §5.x must match those in the STP §4.2.
  - STR (DI-IPSC-81440A): the STPr step numbers are referenced in STR §4.x.2.y fields when recording which procedure steps encountered problems
  - RTVM (DI-MGMT-82133A): requirements addressed in §5.x.y.1 and traced in Part 7 are the same requirement UIDs tracked in the RTVM verification columns
- **Generate data sheets** (Part 6) as a separate structured table or form artifact for each test case — these require physical technician signatures and are not generated as pure markdown

When generating an STPr, establish the hardware preparation (Part 4.x.1) and software preparation (Part 4.x.2) sections first as they are prerequisites for all test cases under a given test. Then generate each test case (5.x.y) in the sequence specified by the table of tests.
