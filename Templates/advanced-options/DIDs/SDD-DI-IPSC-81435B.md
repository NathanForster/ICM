# DID: Software Design Description (SDD)

**DID Number:** DI-IPSC-81435B  
**Title:** Software Design Description (SDD)  
**Approval Date:** 2021-11-22  
**Supersedes:** DI-IPSC-81435A  
**AMSC Number:** N10191  
**Preparing Activity:** EC  
**Project Number:** IPSC-2020-002  
**Source PDF:** [SDD-DI-IPSC-81435B.pdf](SDD-DI-IPSC-81435B.pdf)

> **Revision note:** This is revision B (DI-IPSC-81435B), approved 2021-11-22. It supersedes revision A (DI-IPSC-81435A). Notable additions in revision B include §1.4 (Section 508 IT Accessibility), §3.1 (Cybersecurity and PII requirements), the MBSE subsection (§3.f), external dependencies (§3.g), and explicit cybersecurity considerations in interface design (§4.3.2.b).

---

## Purpose

The SDD describes the design of a Computer Software Configuration Item (CSCI). It describes:
- CSCI-wide design decisions (behavioral, architectural, and other decisions affecting the entire CSCI)
- CSCI architectural design (the software units that make up the CSCI and their relationships)
- Detailed design needed to implement the software

The SDD may be supplemented by Interface Design Descriptions (IDDs, DI-IPSC-81436) and Database Design Descriptions (DBDDs, DI-IPSC-81437). The SDD with its associated IDDs and DBDDs is used as the basis for implementing the software; it provides the acquirer visibility into the design and provides information needed for software support.

This DID is used when the developer is tasked to define and record the design of a CSCI. Designs pertaining to interfaces may be presented in the SDD or in IDDs. Designs pertaining to databases may be presented in the SDD or in DBDDs.

---

## Format Requirements

The SDD shall be in the format as directed in the contract. Use of automated techniques is encouraged. Diagrams, tables, matrices, and other presentation styles are acceptable substitutes for text. For data in a database or other alternative form, include security markings in accordance with DoD Manual (DoDM) 5200.01; distribution statement in accordance with DoD Instruction (DoDI) 5230.24.

---

## Required Content Structure

### 1. Scope

#### 1.1 System Identification
Full identification of the system and the software to which the SDD applies:
- a) Identification number(s)
- b) Title(s)
- c) Abbreviation(s)
- d) Version number(s)
- e) Release number(s)

#### 1.2 System Overview
Briefly state the purpose of the system and the software to which the SDD applies. Describe the general nature of the system and software; summarize the history of system development, operation, and maintenance; identify the project sponsor, acquirer, user, developer, and support agencies; identify current and planned operating sites; list other relevant documents.

#### 1.3 Document Overview
Summarize the purpose and contents of this document. Describe any security or privacy considerations associated with its use.

#### 1.4 Section 508, IT Accessibility
Usability will be in compliance with the Section 508 Amendment of the Rehabilitation Act of 1973.

---

### 2. Referenced Documents
List the number, title, revision, and date of all documents referenced in this document. Identify the source for all referenced documents not available through Government sources.

---

### 3. CSCI-Wide Design Decisions

Present as needed to describe CSCI-wide design decisions — decisions about the CSCI's behavioral design (how it will behave, from a user's point of view, ignoring internal implementation) and other decisions affecting the selection and design of the software units that make up the CSCI.

If all such decisions are explicit in the CSCI requirements or are deferred to the design of the CSCI's software units, so state. Design decisions that respond to requirements designated critical (safety, security, or privacy) shall be placed in separate subparagraphs. If a design decision depends upon software states, modes, or lists, explain the software states and modes. Design conventions needed to understand the design shall be presented or referenced.

Examples of CSCI-wide design decisions:

- **a. Input/Output (I/O).** Design decisions regarding inputs the CSCI will accept and outputs it will produce, including interfaces with other systems, HWCIs, CSCIs, and users. Define the target operating system(s). CSCI behavior for I/O conditions — actions the CSCI performs in response to each input or condition, including response times and other performance characteristics. If this information is in IDDs, it may be referenced.
- **b. Equations, algorithms, rules, and handling of un-allowed inputs or conditions.**
- **c. Databases and data files.** Design decisions on how databases and data files appear to the end user. If this information is in DBDDs, it may be referenced.
- **d. Selected approach to meeting safety, security, and privacy requirements.**
- **e. Other decisions.** Other CSCI-wide design decisions made in response to requirements, such as the selected approach to providing required flexibility, availability, and maintainability.
- **f. Model Based Systems Engineering (MBSE).** MBSE can be used to develop a set of related system models that help define, design, analyze, and document the system under development.
- **g. External dependencies.** List all external dependencies, for example:
  1. Software libraries
  2. Web services, etc.

#### 3.1 Cyber Security and Personally Identifiable Information (PII) Requirements
Specify the software requirements concerned with maintaining cyber security and any PII data. Include as applicable: the security/privacy environment in which the software must operate; the type and degree of security or privacy to be provided; the security/privacy risks the software must withstand; required safeguards to reduce those risks; the security/privacy policy that must be met; the security/privacy accountability the software must provide; and the criteria that must be met for security/privacy certification/accreditation.

---

### 4. CSCI Architectural Design

Divided into paragraphs to describe the CSCI architectural design. If part or all of the design depends upon software states or modes, this dependency shall be indicated. If design information falls into more than one paragraph, it may be presented once and referenced from other paragraphs. Design conventions needed to understand the design shall be presented or referenced.

#### 4.1 CSCI Components

This paragraph shall:

- **a.** Identify the individual software units that make up the CSCI. Each software unit shall be assigned a unique identifier.

  *Note: A software unit is defined as an element in the design of a CSCI — for example, a major subdivision of a CSCI, a component of that subdivision, a class, object, module, function, routine, or database. Software units may exist at different levels of a hierarchy and may consist of other software units. Software units in the design may or may not have a one-to-one relationship with the code and data entities (routines, procedures, databases, datafiles, etc.) that implement them, or with the computer files containing those entities. A database may be treated as a CSCI or as a software unit.*

- **b. Relationships.** Show the static (such as "consists of") relationship(s) of the software units. Multiple relationships shall be presented, depending on the selected software design methodology (e.g., in object-oriented or modular open systems design, present class and object structures as well as module and process architectures of the CSCI).
- **c. Requirements and Allocation.** State the purpose of each software unit, the CSCI requirements, and the CSCI-wide design decisions allocated to it.
- **d. Identifying Information.** Identify groups of software unit development status/type:
  - New development
  - Existing design or software to be reused as is
  - Existing design or software to be reengineered
  - Software to be developed for reuse
  - Software planned for Build N, etc.
  For existing design or software, include identifying information such as name, version, documentation references, library, etc.
- **e. Computer Hardware Resources.** Describe the CSCI's (and as applicable, each software unit's) planned utilization of computer hardware resources:
  1. The CSCI requirements or system-level resource allocations being satisfied
  2. The assumptions and conditions on which the utilization data are based (typical usage, worst-case usage, assumptions of certain events)
  3. Any special considerations affecting the utilization (virtual memory, overlays, multiprocessors, operating system overhead, library software, or other implementation overhead)
  4. The units of measure used (percentage of processor capacity, cycles per second, bytes of memory, bytes per second)
  5. The level(s) at which the estimates or measures are made (software unit, CSCI, or executable program)
- **f.** State the library, website, etc. where the software unit is to be placed.

#### 4.2 Concept of Execution
Describe the concept of execution among the software units — how they will interact during CSCI operation, including:
- Flow of execution control
- Data flow
- State transition diagrams
- Timing
- Priorities among units
- Handling of interrupts
- Timing/sequencing relationships
- Exception handling
- Concurrent execution
- Dynamic allocation/deallocation
- Dynamic creation or deletion of objects, processes, tasks, and other aspects of dynamic behavior

#### 4.3 Interface Design
Divided into subparagraphs to describe the interface characteristics of the software units. Include both interfaces among the software units and their interfaces with external entities such as systems, configuration items, Service Level Agreements for interfaces, and users. If this information is contained in IDDs or elsewhere, those sources may be referenced.

##### 4.3.1 Interface Identification and Diagrams
State the project-unique identifier assigned to each interface and identify the interfacing entities (software units, systems, configuration items, users, etc.) by name, number, version, and documentation references, as applicable. State which entities have fixed interface characteristics (and therefore impose interface requirements on interfacing entities) and which are being developed or modified (thus having interface requirements imposed on them). Provide one or more interface diagrams as appropriate.

##### 4.3.2 (Unique Identifier of Interface)
One subparagraph per interface, identified by unique identifier. Briefly identify the interfacing entities and divide into subparagraphs as needed to describe the interface characteristics of one or both of the interfacing entities. If a given interfacing entity is not covered by this SDD (e.g., an external system), its interface characteristics shall be stated as assumptions or as "When [the entity not covered] does this, [the entity that is covered] will…" The design description shall include the following as applicable:

- **a. Priority assigned to the interface** by the interfacing entity(ies) such as:
  1. Spanning tree
  2. Priority queue
  3. Tree
  4. Other data structures
- **b. Cybersecurity considerations** for interface requirements such as:
  1. Identifying vulnerabilities
  2. Evaluating vulnerabilities
  3. Reporting vulnerabilities
  4. Mitigating or resolving security vulnerabilities
- **c.** Type of interface (such as real-time data transfer, storage-and-retrieval of data, etc.) to be implemented
- **d.** Characteristics of individual data elements that the interfacing entity(ies) provide, store, send, access, receive, etc.:
  1. Names and identifiers: a) unique identifier; b) non-technical name; c) DoD standard data element name; d) technical name (variable or field name); e) abbreviation or synonymous name(s)
  2. Data type (alphanumeric, integer, etc.)
  3. Size and format (length and punctuation of a character string)
  4. Units of measurement (meters, dollars, nanoseconds)
  5. Range or enumeration of possible values (such as 0–99)
  6. Accuracy (how correct) and precision (number of significant digits)
  7. Priority, timing, frequency, volume, sequencing, and other constraints; whether data element may be updated; whether business rules apply
  8. Security and privacy constraints
  9. Sources (setting/sending entities) and recipients (using/receiving entities)
- **e.** Characteristics of data element assemblies (records, messages, files, arrays, displays, reports, etc.) that the interfacing entity(ies) provide, store, send, access, receive, etc.:
  1. Names and identifiers: a) unique identifier; b) non-technical name; c) technical name (record or data structure name); d) abbreviations or synonymous names
  2. Data elements in the assembly and their structure (number, order, grouping)
  3. Medium (such as disk) and structure of data elements/assemblies on the medium
  4. Visual and auditory characteristics of displays and outputs (colors, layouts, fonts, icons, beeps, lights)
  5. Relationships among assemblies, such as sorting/access characteristics
  6. Priority, timing, frequency, volume, sequencing, and other constraints; whether assembly may be updated; whether business rules apply
  7. Security and privacy constraints
  8. Sources (setting/sending entities) and recipients (using/receiving entities)
- **f.** Characteristics of communication methods the interfacing entity(ies) use for the interface:
  1. Unique identifier(s)
  2. Communication links, bands, frequencies, media and their characteristics
  3. Message formatting
  4. Flow control (sequence numbering and buffer allocation)
  5. Data transfer rate, whether periodic/aperiodic, and interval between transfers
  6. Routing, addressing, and naming conventions
  7. Transmission services, including priority and grade
  8. Safety, security, and privacy considerations (encryption, user authentication, compartmentalization, and auditing)
- **g.** Characteristics of protocols that the interfacing entity(ies) use for the interface:
  1. Unique identifier(s)
  2. Priority and layer of the protocol
  3. Packeting, including fragmentation and reassembly, routing, and addressing
  4. Legality checks, error control, and recovery procedures
  5. Synchronization, including: connection establishment, maintenance, termination; status, identification, and any other reporting features
- **h.** Other characteristics — physical compatibility of the interfacing entity(ies) (dimensions, tolerances, loads, voltages, plug compatibility, etc.)

---

### 5. Requirements Traceability

This section shall contain:

- **a.** Traceability from each software unit identified in this SDD to the CSCI requirements allocated to it (use of MBSE methods is acceptable)
- **b.** Traceability from each CSCI requirement to the software units to which it is allocated

---

### 6. Notes
General information that aids in understanding this document (background information, glossary, rationale). Include an alphabetical listing of all acronyms, abbreviations, and their meanings as used in this document, and a list of any terms and definitions needed to understand the SDD.

---

### Appendices
May be used to provide information published separately for convenience in document maintenance (e.g., charts, classified data). Each appendix shall be referenced in the main body where the data would normally have been provided. Appendices may be bound as separate documents. Lettered alphabetically (A, B, etc.).

---

## Key Acronyms

| Acronym | Meaning |
|---------|---------|
| CASE | Computer-Aided Software Engineering |
| CSCI | Computer Software Configuration Item |
| DBDD | Database Design Description |
| DID | Data Item Description |
| HWCI | Hardware Configuration Item |
| IDD | Interface Design Description |
| MBSE | Model Based Systems Engineering |
| PII | Personally Identifiable Information |
| SDD | Software Design Description |
| SLA | Service Level Agreement |

---

## ICM Usage Notes

This DID defines the required content of a Software Design Description. An AI agent working within an ICM project can use this file to:

- **Generate** an SDD by first documenting CSCI-wide design decisions in §3 (I/O, algorithms, databases, safety/security approach, external dependencies, and cybersecurity/PII requirements in §3.1), then decomposing the CSCI into software units in §4.1, then describing execution relationships in §4.2, then detailing each interface in §4.3.x using the a–h checklist
- **Validate** a draft SDD for completeness — every software unit in §4.1 must have: a unique identifier, purpose statement, CSCI requirements allocated to it, and identifying development status. The §4.3.2 interface descriptions must cover cybersecurity considerations (item b, new in revision B). Traceability in §5 must be bidirectional.
- **Decide SDD vs. IDD vs. DBDD:** interface design information may be placed in the SDD or in separate IDDs (DI-IPSC-81436); database design information may be placed in the SDD or in DBDDs (DI-IPSC-81437). For complex systems, separate IDDs and DBDDs keep the SDD focused on architecture while enabling independent CM of interface and database design.
- **Map to the SRS:** §5 traceability links SDD software units back to SRS CSCI requirements. Every SRS requirement that was allocated to this CSCI must appear in §5.b. Gaps indicate requirements not yet addressed in the design.
- **Map to the SPS:** §5.1 of the SPS (DI-IPSC-81441A) references the SDD as the "as built" software design. If the SDD (or IDD/DBDD) is delivered, the SPS §5.1 may reference it. If not, the SDD content must be included directly in the SPS.
- **Map to the RTVM:** the RTVM (DI-MGMT-82133A) §3.2.18 (Design Reference) field should reference the SDD paragraph(s) where a given requirement is addressed in the design.
- **Apply Section 508:** §1.4 requires compliance with the Section 508 Amendment of the Rehabilitation Act of 1973 for IT accessibility — ensure accessibility requirements are addressed in the I/O and user interface design decisions in §3.a.

When generating an SDD, structure §4.1 as a component breakdown diagram or table before writing prose — a visual decomposition makes it easier to verify that all software units have unique identifiers, relationships are shown, and requirements are fully allocated.
