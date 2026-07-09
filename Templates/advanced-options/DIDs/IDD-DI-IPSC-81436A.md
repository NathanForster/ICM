# DID: Interface Design Description (IDD)

**DID Number:** DI-IPSC-81436A  
**Title:** Interface Design Description (IDD)  
**Approval Date:** 1999-12-15  
**Supersedes:** DI-IPSC-81436  
**AMSC Number:** N7361  
**Preparing Activity:** NAVY/EC  
**Source PDF:** [IDD-DI-IPSC-81436A.pdf](IDD-DI-IPSC-81436A.pdf)

---

## Purpose

The IDD describes the interface characteristics of one or more systems, subsystems, Hardware Configuration Items (HWCIs), Computer Software Configuration Items (CSCIs), manual operations, or other system components. An IDD may describe any number of interfaces.

The IDD can be used to supplement the System/Subsystem Design Description (SSDD, DI-IPSC-81432A), Software Design Description (SDD — this library holds revision B, DI-IPSC-81435B; the IDD text cites revision A), and Database Design Description (DBDD, DI-IPSC-81437A). The IDD and its companion Interface Requirements Specification (IRS, DI-IPSC-81434A) serve to communicate and control interface design decisions.

**IRS vs. IDD:** the IRS specifies interface *requirements*; the IDD describes the interface *characteristics selected to meet* those requirements. The IDD may reference the IRS to avoid repeating information.

---

## Format Requirements

Contractor format unless otherwise specified in the CDRL (DD 1423). May be delivered on paper or electronic media; may reside in a CASE tool rather than a traditional document.

---

## Required Content Structure

### 1. Scope

#### 1.1 Identification
Full identification of the system and the software to which this document applies: identification number(s), title(s), abbreviation(s), version number(s), and release number(s).

#### 1.2 System Overview
Briefly state the purpose of the system and the software to which this document applies. Describe the general nature of the system and software; summarize the history of system development, operation, and maintenance; identify the project sponsor, acquirer, user, developer, and support agencies; identify current and planned operating sites; list other relevant documents.

#### 1.3 Document Overview
Summarize the purpose and contents of this document and describe any security or privacy considerations associated with its use.

---

### 2. Referenced Documents
List the number, title, revision, and date of all documents referenced in this document. Identify the source for all documents not available through normal Government stocking activities.

---

### 3. Interface Design

Divided into paragraphs to describe the interface characteristics of one or more systems, subsystems, configuration items, manual operations, or other system components. If part or all of the design depends upon system states or modes, this dependency shall be indicated. If design information falls into more than one paragraph, it may be presented once and referenced from the other paragraphs. If part or all of this information is documented elsewhere, it may be referenced. Design conventions needed to understand the design shall be presented or referenced.

#### 3.1 Interface Identification and Diagrams
For each interface identified in §1.1, state the project-unique identifier assigned to the interface and identify the interfacing entities (systems, configuration items, users, etc.) by name, number, version, and documentation references, as applicable. State which entities have fixed interface characteristics (and therefore impose interface requirements on interfacing entities) and which are being developed or modified (thus having interface requirements imposed on them). Provide one or more interface diagrams, as appropriate, to depict the interfaces.

#### 3.x (Project-Unique Identifier of Interface)
Beginning with 3.2, one paragraph per interface. Identify the interface by project-unique identifier, briefly identify the interfacing entities, and divide into subparagraphs as needed to describe the interface characteristics of one or both of the interfacing entities.

If a given interfacing entity is not covered by this IDD (for example, an external system) but its interface characteristics need to be mentioned to describe interfacing entities that are, those characteristics shall be stated as assumptions or as "When [the entity not covered] does this, [the entity that is covered] will…". This paragraph may reference other documents (data dictionaries, standards for protocols, standards for user interfaces) in place of stating the information here.

The design description shall include the following, as applicable, presented in any order suited to the information, and shall note any differences in these characteristics from the point of view of the interfacing entities (such as different expectations about the size, frequency, or other characteristics of data elements):

- **a.** Priority assigned to the interface by the interfacing entity(ies)
- **b.** Type of interface (real-time data transfer, storage-and-retrieval of data, etc.) to be implemented
- **c.** Characteristics of individual data elements that the interfacing entity(ies) will provide, store, send, access, receive, etc.:
  1. Names/identifiers: a) project-unique identifier; b) non-technical (natural-language) name; c) DOD standard data element name; d) technical name (variable or field name in code or database); e) abbreviation or synonymous names
  2. Data type (alphanumeric, integer, etc.)
  3. Size and format (length and punctuation of a character string)
  4. Units of measurement (meters, dollars, nanoseconds)
  5. Range or enumeration of possible values (such as 0–99)
  6. Accuracy (how correct) and precision (number of significant digits)
  7. Priority, timing, frequency, volume, sequencing, and other constraints; whether the data element may be updated; whether business rules apply
  8. Security and privacy constraints
  9. Sources (setting/sending entities) and recipients (using/receiving entities)
- **d.** Characteristics of data element assemblies (records, messages, files, arrays, displays, reports, etc.) that the interfacing entity(ies) will provide, store, send, access, receive, etc.:
  1. Names/identifiers: a) project-unique identifier; b) non-technical (natural language) name; c) technical name (record or data structure name in code or database); d) abbreviations or synonymous names
  2. Data elements in the assembly and their structure (number, order, grouping)
  3. Medium (such as disk) and structure of data elements/assemblies on the medium
  4. Visual and auditory characteristics of displays and other outputs (colors, layouts, fonts, icons, beeps, lights)
  5. Relationships among assemblies, such as sorting/access characteristics
  6. Priority, timing, frequency, volume, sequencing, and other constraints; whether the assembly may be updated; whether business rules apply
  7. Security and privacy constraints
  8. Sources (setting/sending entities) and recipients (using/receiving entities)
- **e.** Characteristics of communication methods that the interfacing entity(ies) will use for the interface:
  1. Project-unique identifier(s)
  2. Communication links/bands/frequencies/media and their characteristics
  3. Message formatting
  4. Flow control (sequence numbering and buffer allocation)
  5. Data transfer rate, whether periodic/aperiodic, and interval between transfers
  6. Routing, addressing, and naming conventions
  7. Transmission services, including priority and grade
  8. Safety/security/privacy considerations (encryption, user authentication, compartmentalization, auditing)
- **f.** Characteristics of protocols that the interfacing entity(ies) will use for the interface:
  1. Project-unique identifier(s)
  2. Priority/layer of the protocol
  3. Packeting, including fragmentation and reassembly, routing, and addressing
  4. Legality checks, error control, and recovery procedures
  5. Synchronization, including connection establishment, maintenance, termination
  6. Status, identification, and any other reporting features
- **g.** Other characteristics — physical compatibility of the interfacing entity(ies) (dimensions, tolerances, loads, voltages, plug compatibility, etc.)

---

### 4. Requirements Traceability

This paragraph shall contain:

- **a.** Traceability from each software unit identified in this IDD to the system or to the CSCI requirements addressed by the entity's interface design
- **b.** Traceability from each system or CSCI requirement that affects an interface covered in this IDD to the interfacing entities that address it

---

### 5. Notes
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
| HWCI | Hardware Configuration Item |
| IDD | Interface Design Description |
| IRS | Interface Requirements Specification |
| SDD | Software Design Description |
| SSDD | System/Subsystem Design Description |

---

## Relationship to IRS and SDD

The interface documents form a requirements→design pair, mirroring the SRS→SDD pair:

- **IRS (DI-IPSC-81434A)** — *what* the interface must do: requirements with project-unique identifiers, qualification methods, and traceability
- **IDD (this DID)** — *how* the interface is designed: the characteristics selected to meet those requirements

The §3.x a–g characteristics checklist is deliberately parallel to the IRS §3.x checklist and the SDD §4.3.2 checklist — the same interface vocabulary flows from requirement to design. The SDD §4.3 (Interface Design) may present this information directly or delegate it to one or more IDDs.

---

## ICM Usage Notes

This DID defines the required content of an Interface Design Description. An AI agent working within an ICM project can use this file to:

- **Generate** an IDD by iterating over the interfaces in the corresponding IRS: one §3.x per interface, describing the design characteristics (a–g) chosen to satisfy each IRS requirement, with an interface inventory and diagram in §3.1
- **Validate** a draft IDD for completeness — every interface must have a project-unique identifier matching the IRS; each entity must be marked fixed vs. under development; §4 traceability must be bidirectional (interface design ↔ system/CSCI requirements)
- **Decide SDD §4.3 vs. standalone IDD:** keep interface design inside the SDD when interfaces are few and internal; use a standalone IDD when interfaces cross CSCI/organization boundaries, need independent baselining, or an IRS already exists as its requirements counterpart
- **Map to the IRS:** every requirement in IRS §3.x should have a corresponding design characteristic in IDD §3.x. The IDD may reference the IRS rather than restating requirements — do not duplicate requirement text into the IDD
- **Map to the SPS:** SPS §5.1 ("as built" software design) references the IDD when interface design is delivered separately; if the IDD is delivered for the "as built" CSCI, the SPS references it rather than restating it

When generating an IDD, start from the IRS interface inventory so identifiers match one-for-one, then describe the design per interface — flagging any IRS requirement with no corresponding design characteristic as an open design gap.
