# DID: Software Test Report (STR)

**DID Number:** DI-IPSC-81440A  
**Title:** Software Test Report (STR)  
**Approval Date:** 1999-12-15  
**Supersedes:** DI-IPSC-81440  
**AMSC Number:** N7365  
**Office of Primary Responsibility:** NAVY/EC  
**Source PDF:** [STR-DI-IPSC-81440A.pdf](STR-DI-IPSC-81440A.pdf)

---

## Purpose

The STR documents the results of qualification testing performed on Computer Software Configuration Items (CSCIs) or software systems. It provides the acquirer a complete record of test outcomes, problems encountered, deviations from the test plan, and recommended improvements.

This DID is used when the developer is tasked to **plan, perform, and record results of qualification testing** of CSCIs and/or a software system.

---

## General Instructions

- **Automated techniques:** Use of automated techniques is encouraged. "Document" means a collection of data regardless of medium.
- **Alternate presentation styles:** Diagrams, tables, matrices, and other styles are acceptable substitutes for text when they make data more readable.
- **Substitute documents:** Commercial or other existing documents may be substituted if they contain the required data.
- **Tailoring:** If a paragraph is tailored out, the document shall state the paragraph number and title followed by "This paragraph has been tailored out."

---

## Format Requirements

- Contractor format unless otherwise specified in the CDRL (DD 1423)
- May be delivered on paper or electronic media (ASCII, CALS, word processor, CASE tool, etc.)
- Must include: title page, table of contents, unique page numbers with document number/version/date

---

## Required Content Structure

### 1. Scope
#### 1.1 Identification
Full identification of the system and software to which this document applies: identification number(s), title(s), abbreviation(s), version number(s), release number(s).

#### 1.2 System Overview
- Purpose of the system and software
- General nature of system and software
- History of development, operation, and maintenance
- Project sponsor, acquirer, user, developer, and support agencies
- Current and planned operating sites
- Other relevant documents

#### 1.3 Document Overview
Summary of this document's purpose and contents; any security or privacy considerations associated with its use.

---

### 2. Referenced Documents
List all referenced documents: number, title, revision, date. Identify source for documents not available through normal Government stocking activities.

---

### 3. Overview of Test Results

#### 3.1 Overall Assessment
Overall assessment of the software tested, including the following for each deficiency identified:
- a. Software tested (identification number(s), version(s), etc.)
- b. Testing conducted
- c. Testing limitations
- d. Number of deficiencies found (by problem/change report number and title)
- e. Impact of each deficiency on system and software operation
- f. Impact of each deficiency on testing
- g. Plans for correcting each deficiency

#### 3.2 Impact of Test Environment
Description of how the test environment differed from the operational environment, and the impact of those differences on test results.

#### 3.3 Recommended Improvements
Description of any recommended improvements to the software, development process, tests, or test environment.

---

### 4. Detailed Test Results

One subparagraph (4.x) per test identified in the Software Test Plan (STP).

#### 4.x (Project-Unique Identifier and Title of a Test)

##### 4.x.1 Summary of Test Results
Summary of the test results for this test, including:
- Pass/fail status for each test case
- Summary of deficiencies

##### 4.x.2 Problems
One subparagraph (4.x.2.y) per problem found during the test, each containing:
- a. Problem/change report number and title
- b. Test(s) during which problem occurred
- c. Date problem was found
- d. Description of the problem
- e. Impact of the problem on test results

##### 4.x.3 Deviations from the STP
One subparagraph (4.x.3.y) per deviation from the Software Test Plan, each containing:
- a. Description of the deviation
- b. Rationale for the deviation
- c. Impact of the deviation on validity of the test

---

### 5. Test Log

Chronological record of the test period for each test site, including:
- a. Dates, times, and locations of testing
- b. Hardware, software, and firmware configuration(s) used during testing
- c. Activity log in chronological order:
  - Activities performed (including which test cases were run)
  - Results of each activity
  - Identity of individuals performing each activity
  - Identity of witnesses where required

---

### 6. Notes
- Background information, glossary, rationale
- Alphabetical listing of all acronyms and abbreviations with meanings
- List of terms and definitions needed to understand the document

---

### A. Appendices
- May be used for separately published information (test logs, charts, classified data)
- Each appendix referenced in the main body where data would normally appear
- May be bound as separate documents
- Lettered alphabetically (A, B, etc.)

---

## Key Acronyms

| Acronym | Meaning |
|---------|---------|
| CDRL | Contract Data Requirements List |
| CSCI | Computer Software Configuration Item |
| DID | Data Item Description |
| SDP | Software Development Plan |
| STP | Software Test Plan |
| STR | Software Test Report |

---

## ICM Usage Notes

This DID defines the required content of a contractually deliverable STR. An AI agent working within an ICM project can use this file to:

- **Generate** a compliant STR draft by reading test execution records from the project's state/testing workspace and mapping each test to a 4.x section with the required 4.x.1/4.x.2/4.x.3 substructure
- **Validate** a draft STR for completeness — each test must have a summary (4.x.1), each problem must have all five fields (a–e in 4.x.2.y), and each STP deviation must have all three fields (a–c in 4.x.3.y)
- **Map to the STP:** the STR is the paired deliverable to the STP (DI-IPSC-81438A). Test identifiers in Section 4 must match those in STP Section 4.2; Section 5 test log corresponds to the STP Section 5 schedule
- **Track deficiencies:** Section 3.1 overall assessment requires a problem/change report (PCR) number and corrective action plan for each deficiency — link to the project's corrective action tracking workspace
- **Generate Section 5 test log** from chronological execution records, ensuring activity log entries include results and witness identities where required

When generating an STR, begin with Section 3 (overall assessment) using test summary data, then expand each test into Section 4 subsections, then generate the Section 5 log from raw execution records.
