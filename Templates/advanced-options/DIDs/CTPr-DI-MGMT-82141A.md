# DID: Naval Aviation Cybersecurity Test Procedures/Descriptions (CSTP/CSTD)

**DID Number:** DI-MGMT-82141A  
**Title:** Naval Aviation Cybersecurity Test Procedures/Descriptions  
**Approval Date:** 2022-06-02  
**Supersedes:** DI-MGMT-82141  
**AMSC Number:** N10322  
**Preparing Activity:** AS  
**Project Number:** MGMT-2022-015  
**Deliverable Acronym:** CSTP/CSTD (Cybersecurity Test Procedures/Descriptions)  
**Source PDF:** [CTPr-DI-MGMT-82141A.pdf](CTPr-DI-MGMT-82141A.pdf)

> **File naming note:** This DID is named with the "CTPr" prefix (for Test Procedures) to distinguish it from the CTP (Cybersecurity Test Plan, DI-SCRE-82140A). The deliverable produced from this DID is called the CSTP/CSTD.

---

## Purpose

This DID contains the format and content for the Cybersecurity Test Procedures/Descriptions (CSTP/CSTD). The CSTP/CSTD provides step-by-step test procedures and descriptions for individual cybersecurity test cases identified in the Cybersecurity Test Plan (CTP, DI-SCRE-82140A).

---

## Format Requirements

Contractor format is acceptable. Safety precautions marked by WARNING or CAUTION, and security and privacy considerations will be included as applicable throughout.

---

## Required Content Structure

### 3.1 Test Preparations

Identify a test by project-unique identifier, provide a brief description, and divide into the following subparagraphs. When information required duplicates information previously specified for another test, that information may be referenced rather than repeated.

#### 3.1.1 Hardware Preparation
Describe procedures necessary to prepare the hardware for the test. Reference may be made to published operating manuals. Provide as applicable:
- **3.1.1.1** The specific hardware to be used, identified by name and, if applicable, number
- **3.1.1.2** Any switch settings and cabling necessary to connect the hardware
- **3.1.1.3** One or more diagrams to show hardware, interconnecting control, and data paths
- **3.1.1.4** Step-by-step instructions for placing the hardware in a state of readiness

#### 3.1.2 Software Preparation
Describe procedures necessary to prepare the item(s) under test and any related software, including data, for the test. Reference may be made to published software manuals. Provide as applicable:
- **3.1.2.1** The specific software to be used in the test
- **3.1.2.2** The storage medium of the item(s) under test (e.g., magnetic tape, CD)
  - **3.1.2.2.1** The storage medium of any related software (e.g., simulators, test drivers, databases)
  - **3.1.2.2.2** Instructions for loading the software, including required sequence
  - **3.1.2.2.3** Instructions for software initialization common to more than one test case
  - **3.1.2.2.4** Other pre-test preparations: any other pre-test personnel actions, preparations, or procedures necessary to perform the test

---

### 3.2 Test Descriptions

One subparagraph per test case. Safety precautions (WARNING/CAUTION) and security and privacy considerations included as applicable.

#### 3.2.1 (Project-Unique Identifier of a Test Case)
Identify the test case by project-unique identifier, state its purpose, and provide a brief description. Subparagraphs provide a detailed description.

##### 3.2.1.1 Requirements Addressed
Identify the CSCI or system requirements addressed by this test case.

##### 3.2.1.1.1 Prerequisite Conditions
Identify any prerequisite conditions that must be established prior to performing the test case. Discuss as applicable:
- **3.2.1.1.1.1** Hardware and software configuration
- **3.2.1.1.1.2** Flags, initial breakpoints, pointers, control parameters, or initial data to be set/reset prior to test commencement
- **3.2.1.1.1.3** Preset hardware conditions or electrical states necessary to run the test case
- **3.2.1.1.1.4** Initial conditions to be used in making measurements
- **3.2.1.1.1.5** Conditioning of the simulated environment
- **3.2.1.1.1.6** Other special conditions peculiar to the test case

---

### 3.3 Test Inputs

Describe the test inputs necessary for the test case. Provide as applicable:

#### 3.3.1 Input Identification
- **Name, purpose, and description** (e.g., range of values, accuracy) of each test input
- **3.3.1.1** Source of the test input and the method to be used for selecting it
  - **3.3.1.1.1** Whether the test input is real or simulated
  - **3.3.1.1.2** Time or event sequence of test input
  - **3.3.1.1.3** The manner in which the input data will be controlled to:
    - **3.3.1.1.4** Test the item(s) with a minimum/reasonable number of data types and values
    - **3.3.1.1.5** Exercise the item(s) with a range of valid data types and values that test for overload, saturation, and other "worst case" effects
    - **3.3.1.1.6** Exercise the item(s) with invalid data types and values to test for appropriate handling of irregular inputs
    - **3.3.1.1.7** Permit retesting, if necessary
  - **3.3.1.2** Identify required Government Furnished Information (GFI) and Government Furnished Equipment (GFE) required to conduct and complete the test

#### 3.3.1.3 Expected Test Results
Identify all expected test results for the test case. Both intermediate and final results will be provided, as applicable.

#### 3.3.1.4 Criteria for Evaluating Results
Identify the criteria to be used for evaluating intermediate and final results of the test case. Provide as applicable:
- **3.3.1.4.1** Minimum number of combinations or alternatives of input and output conditions that constitute an acceptable test result
- **3.3.1.4.2** Maximum/minimum allowable test duration, in terms of time or number of events
- **3.3.1.4.3** Maximum number of deviations or failures that may occur
- **3.3.1.4.4** Allowable tolerances of errors
- **3.3.1.4.5** Conditions under which the result is inconclusive and re-testing is to be performed
- **3.3.1.4.6** Conditions under which the outputs are to be interpreted as indicating irregularities in input test data, in the test database/data files, or in test procedures
- **3.3.1.4.7** Allowable indications of the control, status, and results of the test and the readiness for the next test case
- **3.3.1.4.8** Additional criteria not mentioned above

---

### 3.4 Test Procedure

Define the test procedure for the test case as a series of individually numbered steps listed sequentially in the order to be performed. Test procedures may be included as an appendix and referenced. The appropriate level of detail depends on the type of cybersecurity testing and hardware/software configuration — the level at which it is useful to specify expected results and compare them to actual results.

#### 3.4.1 Test Operator Actions and Equipment Operation
For each step, including commands as applicable:
- **3.4.1.1.1** Initiate the test case and apply test inputs
  - **3.4.1.1.1.1** Inspect test conditions
  - **3.4.1.1.1.2** Perform interim evaluations of test results
  - **3.4.1.1.1.3** Record data
  - **3.4.1.1.1.4** Halt or interrupt the test case
  - **3.4.1.1.1.5** Request data dumps or other aids, if needed
  - **3.4.1.1.1.6** Modify the database/data files
  - **3.4.1.1.1.7** Number of repetitions required
  - **3.4.1.1.1.8** Apply alternate modes as required by the test case
  - **3.4.1.1.1.9** Terminate the test case
  - **3.4.1.1.1.10** Expected result and evaluation criteria for each step
  - **3.4.1.1.1.11** If the test case addresses multiple requirements: identification of which test procedure step(s) address which requirements
  - **3.4.1.1.1.12** Actions to follow in the event of a failure or deviation, such as:
    - **3.4.1.1.1.13** Recording of critical data from indicators for reference purposes
    - **3.4.1.1.1.14** Halting or pausing time-sensitive test-support software and test apparatus
    - **3.4.1.1.1.15** Collection of system and operator records of test results
    - **3.4.1.1.1.16** Procedures to sanitize and restore the system following the test

#### 3.4.2 Result Reduction and Analysis Procedures
Procedures to reduce and analyze test results to accomplish the following:
- **3.4.2.1** Detect whether a security failure has occurred
- **3.4.2.2** Identify media and location of data produced by the test case
- **3.4.2.3** Evaluate output as a basis for continuation of test sequence
- **3.4.2.4** Evaluate test output against required output

#### 3.4.3 Assumptions and Constraints
Any assumptions made and constraints or limitations imposed on the description of the test case due to system or test conditions (timing, interfaces, equipment, personnel, database/data files). If waivers or exceptions to specified limits and parameters are approved, identify them and address their effects and impacts on the test case.

#### 3.4.4 Requirements Traceability
- **3.4.4.1** Traceability from each test case in this CSTD to the system security requirements it addresses. If a test case addresses multiple requirements: traceability from each set of test procedure steps to the requirement(s) addressed.
- **3.4.4.2** Traceability from each system requirement or security requirement covered by this CSTD to the test case(s) that address it.
- **3.4.4.3** If a test case addresses multiple requirements: traceability will indicate the particular test procedure steps that address each requirement.

---

### 4. Appendices
Appendices may be used for separately published information (charts, classified data). Each appendix shall be referenced in the main body where the data would normally have been provided. Appendices may be bound as separate documents.

---

## Key Acronyms

| Acronym | Meaning |
|---------|---------|
| CSCI | Computer Software Configuration Item |
| CSTD | Cybersecurity Test Description |
| CSTR | Cybersecurity Test Report |
| CSTP | Cybersecurity Test Procedures |
| CTP | Cybersecurity Test Plan |
| GFE | Government Furnished Equipment |
| GFI | Government Furnished Information |
| SOW | Statement of Work |

---

## ICM Usage Notes

This DID defines the required content of a contractually deliverable CSTP/CSTD. An AI agent working within an ICM project can use this file to:

- **Generate** a CSTP/CSTD by iterating over each test case identified in the CTP (DI-SCRE-82140A) and expanding it into the full §3.1–§3.4 structure: preparations → description → inputs → procedure
- **Validate** a draft CSTP/CSTD for completeness — each test case must have all prerequisite conditions (§3.2.1.1.1.1–6), all input controls (§3.3.1.1.3–7), all evaluation criteria (§3.3.1.4.1–8), and all step-level actions (§3.4.1.1.1.1–16)
- **Map to the CTP:** test case identifiers in the CSTP/CSTD (§3.2.1) must match the project-unique test identifiers in CTP §3.3. Traceability in §3.4.4 closes the loop to security requirements.
- **Map to the CSTR:** the CSTP/CSTD procedures are the source for the CSTR (DI-MGMT-82142A) test log entries and detailed results. Step numbers in §3.4.1 correspond to test procedure steps referenced in CSTR §3.6.2.2.
- **Flag sanitization procedures:** §3.4.1.1.1.16 (sanitize and restore system following test) is a cybersecurity-specific requirement with no analog in the standard STP (DI-IPSC-81438A). Ensure this step is explicitly present for any penetration or IAVM test case.

When generating a CSTP/CSTD, complete §3.1 (hardware/software preparation) once per test group, then generate §3.2–§3.4 for each individual test case, referencing common preparation steps rather than repeating them.
