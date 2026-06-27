# DID: Naval Aviation Cybersecurity Test Report (CSTR)

**DID Number:** DI-MGMT-82142A  
**Title:** Naval Aviation Cybersecurity Test Report  
**Approval Date:** 2022-06-02  
**Supersedes:** DI-MGMT-82142  
**AMSC Number:** N10323  
**Preparing Activity:** AS  
**Project Number:** MGMT-2022-016  
**Deliverable Acronym:** CSTR (Cybersecurity Test Report)  
**Source PDF:** [CTR-DI-MGMT-82142A.pdf](CTR-DI-MGMT-82142A.pdf)

> **File naming note:** This DID is named with the "CTR" prefix (for Cybersecurity Test Report) to distinguish it from similarly named DIDs. The deliverable produced from this DID is called the CSTR.

---

## Purpose

The CSTR documents the results from cybersecurity (CS) testing. It is the paired output deliverable to the Cybersecurity Test Plan (CTP, DI-SCRE-82140A) and Cybersecurity Test Procedures/Descriptions (CSTP/CSTD, DI-MGMT-82141A).

---

## Format Requirements

Contractor format is acceptable.

---

## Required Content Structure

### 3.1 Identification
Full identification of the system to which this document applies:
- Identification number(s), title(s), abbreviation(s)
- Software version number(s), hardware components, release number(s)

### 3.2 System Overview
State the purpose of the system and the hardware/software to which this document applies:
- General nature of the system
- Summary of system development, operation, and maintenance history
- Project sponsor, acquirer, user, developer, and support agencies
- Current and planned operating sites
- Other relevant documents

### 3.3 Document Overview
Summarize the purpose and contents of this document. Describe any security or privacy considerations associated with its use.

### 3.4 Referenced Documents
List the number, title, revision, and date of all documents referenced. Identify the source for all documents not available through normal Government stocking activities.

---

### 3.5 Overview of Test Results

#### 3.5.1 Overall Assessment of Hardware/Software Tested

##### 3.5.1.1
Provide an overall assessment of the system as demonstrated by the test results in this report.

##### 3.5.1.2
Identify any remaining deficiencies, limitations, or constraints detected by the testing performed. Problem/change reports may be used to provide deficiency information.

##### 3.5.1.3
For each important finding, limitation, or constraint, describe:
- **3.5.1.3.1** Its impact on hardware/software and system security posture, including identification of security requirements not met
- **3.5.1.3.2** The impact on hardware/software and system design to correct it
- **3.5.1.3.3** A recommended solution/approach for correcting it

#### 3.5.2 Impact of Test Environment
Assess the manner in which the test environment may be different from the operational environment and the effect of this difference on the test results.

#### 3.5.3 Recommended Improvements
Provide any recommended improvements in the design, operation, or testing of the hardware/software tested. Include a discussion of each recommendation and its impact on the system security posture. If no recommended improvements are provided, this paragraph shall state "None."

---

### 3.6 Detailed Test Results

One subparagraph per test. Note: the word "test" means a related collection of test cases.

#### 3.6.1 (Project-Unique Identifier of a Test)
Identify a test by project-unique identifier. Divide into the following subparagraphs.

##### 3.6.1.1 Summary of Test Results
Summarize the results of the test. Include, possibly in a table, the completion status of each test case associated with the test:
- "All results as expected"
- "Problems encountered"
- "Deviations required"

When the completion status is not "as expected," reference the following paragraphs for details.

##### 3.6.1.2 Problems Encountered
Divided into subparagraphs identifying each test case in which one or more problems occurred.

#### 3.6.2 (Project-Unique Identifier of a Test Case with Problems)
For each test case in which one or more problems occurred, provide:
- **3.6.2.1** A brief description of the result(s) that occurred
- **3.6.2.2** Identification of the test procedure step(s) in which they occurred
- **3.6.2.3** Reference(s) to the associated problem/change report(s) and backup data, as applicable
- **3.6.2.4** The number of times the procedure or step was repeated in attempting to correct the problem(s) and the outcome of each attempt
- **3.6.2.5** Back-up points or test steps where tests were resumed for retesting

#### 3.6.3 Deviations from Test Cases/Procedures
Divided into subparagraphs identifying each test case in which deviations from test case/test procedures occurred.

#### 3.6.4 (Project-Unique Identifier of a Test Case with Deviations)
For each test case in which one or more deviations occurred, provide:
- **3.6.4.1** A description of the result(s) (e.g., test case run in which the deviation occurred, nature of the deviation such as substitution of required equipment, procedural steps not followed, schedule deviations). Red-lined test procedures may be used to show the deviations.
- **3.6.4.2** The rationale for the deviation(s) if required
- **3.6.4.3** An assessment of the deviations' impact on the validity of the test case

---

### 3.7 Test Log
A chronological record of the test events covered by this report, presented possibly in a figure or appendix. The test log shall include:
- **3.7.1** The date(s), time(s), and location(s) of the tests performed
- **3.7.2** The hardware and software configurations used for each test, including as applicable: part/model/serial number, manufacturer, revision level, calibration date of all hardware; version number and name for software components used
- **3.7.3** The date and time of each test-related activity, the identity of the individual(s) who performed the activity, and the identities of witnesses, as applicable

---

### 3.8 Red Lines, Notes, and Unplanned Tests
Present the tester(s)' handwritten materials, if applicable, including:
- Comments and redlines
- Unplanned test runs and their results

Provided as a scanned document.

---

### 3.9 Notes
General information that aids in understanding this document:
- Alphabetical listing of all acronyms, abbreviations, and their meanings
- List of terms and definitions needed to understand this document

---

### 3.10 Appendices
Appendices may be used for separately published information (charts, classified data). Each appendix shall be referenced in the main body where the data would normally have been provided. Appendices may be bound as separate documents. Lettered alphabetically (A, B, etc.).

---

## Key Acronyms

| Acronym | Meaning |
|---------|---------|
| CSTR | Cybersecurity Test Report |
| CSTD | Cybersecurity Test Description |
| CSTP | Cybersecurity Test Procedures |
| CTP | Cybersecurity Test Plan |
| SOW | Statement of Work |

---

## ICM Usage Notes

This DID defines the required content of a contractually deliverable Cybersecurity Test Report. An AI agent working within an ICM project can use this file to:

- **Generate** a CSTR by reading test execution records from the project's cybersecurity testing workspace and mapping each test to a §3.6.1 section, with problems in §3.6.2 and deviations in §3.6.4
- **Validate** a draft CSTR for completeness — §3.5.1.3 requires that every finding/deficiency include all three sub-fields (security posture impact, design correction impact, and recommended solution); §3.6.2 requires all five fields per problem case; §3.6.4 requires all three fields per deviation case
- **Map to the CTP and CSTP/CSTD:** test identifiers in §3.6.1 must match those in CTP §3.3; test case identifiers in §3.6.2/3.6.4 must match CSTP/CSTD §3.2.1; step references in §3.6.2.2 must match CSTP/CSTD §3.4.1 step numbers
- **Populate §3.8 (Red Lines):** this section is unique to the CSTR — it requires scanned handwritten tester materials as a document artifact, not structured data. Flag this requirement when generating the CSTR so the project can collect physical or scanned materials from testers.
- **Map to the RTVM:** security requirement identifiers referenced in §3.5.1.3.1 (requirements not met) are the same identifiers tracked in the RTVM (DI-MGMT-82133A) — link findings to RTVM rows with "Non-Compliant" or "Partial Compliant" status and non-conforming entries pointing to problem/change reports

When generating a CSTR, begin with §3.5 (overall assessment) as the executive summary, then expand each test in §3.6 from lowest-level execution records, then compile the §3.7 test log from chronological activity data.
