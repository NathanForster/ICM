# DID: Software Development Plan (SDP)

**DID Number:** DI-IPSC-81427B  
**Approval Date:** 2017-03-13  
**Supersedes:** DI-IPSC-81427A  
**Preparing Activity:** EC  
**Project Number:** IPSC-2017-001  
**Source PDF:** [SDP-DI-IPSC-81427B.pdf](SDP-DI-IPSC-81427B.pdf)

---

## Purpose

The SDP gives the acquirer insight into — and a monitoring tool for — the processes, methods, schedules, organization, and resources to be used for software development. It applies to new development, modification, reuse, reengineering, maintenance, and other activities producing software products.

---

## Required Content Structure

Each section below maps directly to a required paragraph in the DID. Sections not applicable to the project may be satisfied with "Not applicable." Each paragraph must also identify applicable risks/uncertainties and plans for addressing them.

---

### 1. Referenced Documents
List all documents referenced in the plan: number, title, revision, date, and source (address/website) for any not available through normal Government stocking activities.

---

### 3.1 Identification
Full identification of the system and software: identification number(s), title(s), abbreviations, version number(s), release number(s).

---

### 3.2 System Overview
- Purpose of the system and software
- General nature of the system
- History of development, operation, and maintenance
- Project sponsor, acquirer, user, developer, and support agencies
- Current and planned operating sites
- Other relevant documents

---

### 3.3 Document Overview
- Summary of this document's purpose and contents
- Security or privacy considerations associated with its use

---

### 3.4 Relationship to Other Plans
Describe the relationship of this SDP to other project management plans.

---

### 3.5 Overview of Required Work
Establish context for the planning in later sections. Cover as applicable:
- a. Requirements and constraints on the system and software to be developed
- b. Requirements and constraints on project documentation
- c. Position of the project in the system life cycle
- d. Selected program/acquisition strategy and any constraints on it
- e. Requirements and constraints on project schedules and resources
- f. Other requirements and constraints (security, privacy, methods, standards, hardware/software interdependencies, etc.)

---

### 3.6 Plans for General Software Development Activities

#### 3.6.a Software Development Process
- Describe the process to be used (e.g., waterfall, iterative, Agile)
- Identify planned builds, their objectives, and activities per build
- Explain why the approach was chosen
- Describe previous experience with software of similar nature

#### 3.6.b Agile-Specific Requirements (if applicable)
If an Agile process is used, the following must be addressed:
1. Agile technique(s) employed (Scrum, pair programming, XP, etc.) and approach for each
2. Release planning approach
3. Sprint length (for Scrum) and rationale
4. How the backlog is initially established and re-prioritized
5. Typical sprint activities and what happens each iteration
6. Product Owner identification and roles/responsibilities
7. Acquirer role in sprints if acquirer is not the Product Owner
8. Mechanism for getting acquirer/end-user feedback per sprint
9. How the working product will be demonstrated after each sprint
10. Handling of incomplete, unsatisfactory, and buggy user stories and how they re-enter the backlog
11. Configuration Management process for tracking user story status (pass/rework/fail)
12. Artifact delivery approach (SRS, SDD, Software Test Plan, System Integration Plan delivery timing)
13. Refactoring approach
14. Software metrics to be used
15. Technical debt payoff approach
16. How story points for velocity will be determined
17. Integrated Requirements Toolset (IRT) tracing user stories to mission threads and KPPs
18. Coordination with Integration and Test (I&T) team and assurance that I&T can keep up with releases
19. Sprint-to-sprint dependency resolution (product and resource dependencies)
20. Strategy for keeping multiple sprint teams in sync
21. Maintaining baseline integrity for the next sprint
22. Regression testing approach for each sprint release covering all previously released functions
23. Automated testing techniques for sprint and regression testing
24. Synchronization and coordination with systems engineering activities and reviews

---

### 3.7 General Plans for Software Development

#### 3.7.a Software Development Methods
- Manual and automated tools and procedures supporting the methods
- Must cover all contractual clauses on this topic

#### 3.7.b Standards for Software Products
Standards for: requirements, design, code, test cases, test procedures, test results. For each programming language, code standards must include at minimum:
1. Format standards (indentation, spacing, capitalization, information order)
2. Header comment standards (name/ID, version, modification history, purpose, requirements/design decisions, processing notes, data notes)
3. Other comment standards (required number and content)
4. Naming conventions (variables, parameters, packages, procedures, files)
5. Restrictions on programming language constructs or features
6. Restrictions on code aggregate complexity

#### 3.7.c Reusable Software Products
1. **Incorporating reusable software:** Approach for identifying, evaluating, and incorporating reusable products; scope of search; evaluation criteria; known candidates with benefits, drawbacks, and restrictions
2. **Developing reusable software:** Approach for identifying, evaluating, and reporting reuse opportunities

#### 3.7.d Handling of Critical Requirements
For each of the following critical requirement categories, describe approach across all lifecycle phases (Software Requirements → System Software Architecture & Preliminary Design → Detailed Design → Coding & Unit Test → CSC Integration & Test → CSCI FQT → Subsystem Integration & Test → System Qualification Test):

1. **Safety Assurance** — address each lifecycle phase listed above
2. **Cyber-Security / Software Assurance** — address each lifecycle phase listed above; include mechanism to address constantly emerging cyber-security requirements
3. **Assurance of other critical requirements**

#### 3.7.e Computer Hardware Resource Utilization
- Approach for allocating computer hardware resources
- Approach for monitoring utilization

#### 3.7.f Recording Rationale
- Approach for recording rationale for key decisions
- Definition of "key decisions" for this project
- Where rationales will be recorded

#### 3.7.g Access for Acquirer Review
Approach for providing acquirer (or authorized representative) access to developer and subcontractor facilities for software product and activity review.

---

### 3.8 Plans for Detailed Software Development Activities

For each activity below, describe: (1) approach/methods/procedures/tools; (2) how results are recorded; (3) how deliverables are prepared; (4) applicable risks and mitigation plans.

#### 3.8.a Project Planning and Oversight
1. Software development planning (including plan update process)
2. CSCI test planning
3. System test planning
4. Software installation planning
5. Software transition planning
6. Following and updating plans; intervals for management review

#### 3.8.b Establishing a Software Development Environment
1. Software engineering environment
2. Software test environment
3. Software development library
4. Software development files
5. Non-deliverable software
6. Software assurance considerations, including tool selection

#### 3.8.c System Requirements Analysis
1. Analysis of user input
2. Operational concept
3. System requirements

#### 3.8.d System Design
1. System-wide design decisions
2. System architectural design

#### 3.8.e Software Requirements Analysis
Approach for software requirements analysis.

#### 3.8.f Software Design
1. CSCI-wide design decisions
2. CSCI architectural design
3. CSCI detailed design

#### 3.8.g Peer Review
Describe the peer review process covering: system requirements, system design, software requirements, software design, software implementation, and software testing.

#### 3.8.h Coding Standards
Uniform rules and guidelines for software development, including standards for creating and sustaining secure systems.

#### 3.8.i Software Implementation and Unit Testing
1. Software implementation
2. Preparing for unit testing
3. Performing unit testing
4. Revision and retesting
5. Analyzing and recording unit test results

#### 3.8.j Unit Integration and Testing
1. Preparing for unit integration and testing
2. Performing unit integration and testing
3. Revision and retesting
4. Analyzing and recording unit integration and test results

#### 3.8.k CSCI Qualification Testing
1. Independence in CSCI qualification testing
2. Testing on the target computer system
3. Preparing for CSCI qualification testing
4. Dry run of CSCI qualification testing
5. Performing CSCI qualification testing
6. Revision and retesting
7. Analyzing and recording CSCI qualification test results

#### 3.8.l CSCI/HWCI Integration and Testing
1. Preparing for CSCI/HWCI integration and testing
2. Performing CSCI/HWCI integration and testing
3. Revision and retesting
4. Analyzing and recording CSCI/HWCI integration and test results

#### 3.8.m System Qualification Testing
1. Independence in system qualification testing
2. Testing on the target computer system
3. Preparing for system qualification testing
4. Dry run of system qualification testing
5. Performing system qualification testing
6. Revision and retesting
7. Analyzing and recording system qualification test results
8. Process for government real-time access to code evaluation results; use of automated code analyzers and documented peer review

#### 3.8.n Preparing for Software Use
1. Preparing the executable software
2. Preparing version descriptions for user sites
3. Preparing user manuals
4. Installation at user sites

#### 3.8.o Preparing for Software Transition
1. Preparing the executable software
2. Preparing source files
3. Preparing version descriptions for the support site
4. Preparing the "as built" CSCI design and other software support information
5. Updating the system design description
6. Preparing support manuals
7. Transition to the designated support site
8. Evaluation of code quality and defect removal before handoff to system integrators (coding standards conformance; dead code, memory leaks, unreachable code)

#### 3.8.p Software Configuration Management
1. Configuration identification
2. Configuration control
3. Configuration status accounting
4. Configuration audits
5. Packaging, storage, handling, and delivery

#### 3.8.q Software Product Evaluation
1. In-process and final software product evaluations
2. Software product evaluation records (items to be recorded)
3. Independence in software product evaluation

#### 3.8.r Software Quality Assurance
1. Software quality assurance evaluations
2. Software quality assurance records (items to be recorded)
3. Independence in software quality assurance

#### 3.8.s Corrective Action
1. Problem/change reports — items to record: project name, originator, problem number, problem name, affected software element or document, origination date, category and priority, description, assigned analyst, assignment date, completion date, analysis time, recommended solution, impacts, problem status, solution approval, follow-up actions, corrector, correction date, version corrected, correction time, description of solution implemented
2. Corrective action system

#### 3.8.t Joint Technical and Management Reviews
1. Joint technical reviews (including proposed review set)
2. Joint management reviews (including proposed review set)

#### 3.8.u Other Software Development Activities
1. Risk management — known risks and corresponding strategies
2. Software management indicators — indicators to be used
3. Security and privacy
4. Subcontractor management
5. Interface with software independent verification and validation (IV&V) agents
6. Coordination with associate developers
7. Improvement of project processes
8. Other activities not covered elsewhere

#### 3.8.v Schedules and Activity Network
1. Schedule(s) identifying activities in each build: initiation, draft/final deliverables, milestones, and completion
2. Activity network showing sequential relationships, dependencies, and critical-path activities

---

### 3.9 Project Organization and Resources

#### 3.9.a Project Organization
- Organizational structure: organizations involved, relationships, authority, and responsibility
- Definition of Systems Engineering, Software Engineering, and Integrated Product and Process Development processes for responsible divisions and principal subcontractors

#### 3.9.b Project Resources
Include description of continuity from previous efforts using these processes. Cover:
1. **Personnel resources:**
   - a. Estimated staff-loading (number of personnel over time)
   - b. Staff-loading breakdown by responsibility (management, software engineering, software testing, CM, product evaluation, QA)
   - c. Skill levels, geographic locations, and security clearances per responsibility
2. Overview of developer facilities (geographic locations, facilities, secure areas)
3. Acquirer-furnished equipment, software, services, documentation, data, and facilities — with schedule for when each is needed
4. Other required resources — plan for obtaining, dates needed, availability

---

### 3.10 Notes
- Background information, glossary, rationale
- Alphabetical listing of all acronyms and abbreviations with meanings
- List of terms and definitions needed to understand the document

---

### 3.11 Appendixes
- May be used for separately published information (charts, classified data)
- Each appendix referenced in the main body where data would normally appear
- May be bound as separate documents
- Lettered alphabetically (A, B, etc.)

---

## Key Acronyms

| Acronym | Meaning |
|---------|---------|
| CSCI | Computer Software Configuration Item |
| CSC | Computer Software Component |
| DID | Data Item Description |
| FQT | Formal Qualification Test |
| HWCI | Hardware Configuration Item |
| I&T | Integration and Test |
| IRT | Integrated Requirements Toolset |
| IV&V | Independent Verification and Validation |
| KPP | Key Performance Parameter |
| SDD | Software Design Document |
| SDP | Software Development Plan |
| SRS | Software Requirements Specification |

---

## ICM Usage Notes

This DID defines the **complete required content** of a contractually deliverable SDP. An AI agent working within an ICM project can use this file to:

- **Generate** a compliant SDP outline or template pre-populated with project context from ICM.md and CONTEXT.md
- **Validate** a draft SDP for completeness against every required paragraph
- **Map** DID sections to ICM workspaces (e.g., 3.8.p Configuration Management → CM workspace; 3.8.r Quality Assurance → QA workspace)
- **Identify gaps** when onboarding an existing project's documentation into an ICM structure

When generating an SDP, read the project's top-level ICM.md and CONTEXT.md first to populate identification, system overview, and organizational sections before expanding the technical planning sections.
