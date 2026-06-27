# DID: Interface Requirements Specification (IRS)

**DID Number:** DI-IPSC-81434A  
**Title:** Interface Requirements Specification (IRS)  
**Approval Date:** 1999-12-15  
**Supersedes:** DI-IPSC-81434  
**AMSC Number:** N7359  
**Preparing Activity:** NAVY/EC  
**Source PDF:** [IRS-DI-IPSC-81434A.pdf](IRS-DI-IPSC-81434A.pdf)

---

## Purpose

The IRS specifies the requirements imposed on one or more systems, subsystems, Hardware Configuration Items (HWCIs), Computer Software Configuration Items (CSCIs), manual operations, or other system components to achieve one or more interfaces among these entities. An IRS can cover any number of interfaces.

The IRS can be used to supplement the System/Subsystem Specification (SSS, DI-IPSC-81431A) and Software Requirements Specification (SRS, DI-IPSC-81433A) as the basis for design and qualification testing of systems and CSCIs.

This DID is used when the developer is tasked to define and record the interface requirements for one or more systems, subsystems, HWCIs, CSCIs, manual operations, or other system components.

---

## Format Requirements

Contractor format unless otherwise specified in the CDRL (DD 1423). May be delivered on paper or electronic media; may reside in a CASE tool rather than a traditional document.

---

## Required Content Structure

### 1. Scope

#### 1.1 Identification
Full identification of the system and the software to which this document applies: identification number(s), title(s), abbreviation(s), version number(s), and release number(s).

#### 1.2 System Overview
Briefly state the purpose of the system and the software to which this document applies. Describe the general nature of the system and software; summarize history of system development, operation, and maintenance; identify the project sponsor, acquirer, user, developer, and support agencies; identify current and planned operating sites; list other relevant documents.

#### 1.3 Document Overview
Summarize the purpose and contents of this document and describe any security or privacy considerations associated with its use.

---

### 2. Referenced Documents
List the number, title, revision, and date of all documents referenced in this document. Identify the source for all referenced documents not available through normal Government stocking activities.

---

### 3. Requirements

This section specifies the requirements imposed on one or more systems, subsystems, configuration items, manual operations, or other system components to achieve one or more interfaces among these entities. Each requirement shall be assigned a project-unique identifier to support testing and traceability and shall be stated in such a way that an objective test can be defined for it.

Each requirement shall be annotated with associated qualification method(s) (see §4) and traceability to system (or subsystem, if applicable) requirements (see §5.a) if not provided in those sections. The degree of detail shall be guided by: include those characteristics of the interfacing entities that are conditions for acceptance; defer to design descriptions those characteristics that the acquirer is willing to leave up to the developer.

If interfacing entities operate in states and/or modes having different interface requirements, each requirement or group of requirements shall be correlated to the states and modes. A table or other method in this paragraph, or annotation of the requirements in an appendix, may be used.

#### 3.1 Interface Identification and Diagrams
For each interface identified in §1.1, this paragraph shall include a project-unique identifier and shall designate the interfacing entities (systems, configuration items, users, etc.) by name, number, version, and documentation references. The identification shall state which entities have fixed interface characteristics (and therefore impose interface requirements on interfacing entities) and which are being developed or modified (thus having interface requirements imposed on them). One or more interface diagrams shall be provided to depict the interfaces.

#### 3.x (Project-Unique Identifier of Interface)
Beginning with 3.2, one paragraph per interface. Briefly identify the interfacing entities; divide into subparagraphs as needed to state the requirements imposed on one or both of the interfacing entities to achieve the interface.

If the interface characteristics of an entity are not covered by this IRS but need to be mentioned to specify requirements for entities that are, those characteristics shall be stated as assumptions or as "When [the entity not covered] does this, [the entity being specified] shall…" rather than as requirements on entities not covered by this IRS.

This paragraph may reference other documents (data dictionaries, standards for communication protocols, standards for user interfaces) in place of stating the information here. Requirements include the following, as applicable, presented in any order suited to the requirements:

- **a.** Priority that the interfacing entity(ies) must assign the interface
- **b.** Requirements on the type of interface (real-time data transfer, storage-and-retrieval of data, etc.) to be implemented
- **c.** Required characteristics of individual data elements that the interfacing entity(ies) must provide, store, send, access, receive, etc.:
  1. Names/identifiers: a) project-unique identifier; b) non-technical (natural-language) name; c) DOD standard data element name; d) technical name (e.g., variable or field name in code or database); e) abbreviation or synonymous names
  2. Data type (alphanumeric, integer, etc.)
  3. Size and format (length and punctuation of a character string)
  4. Units of measurement (meters, dollars, nanoseconds)
  5. Range or enumeration of possible values (such as 0–99)
  6. Accuracy (how correct) and precision (number of significant digits)
  7. Priority, timing, frequency, volume, sequencing, and other constraints; whether data element may be updated; whether business rules apply
  8. Security and privacy constraints
  9. Sources (setting/sending entities) and recipients (using/receiving entities)
- **d.** Required characteristics of data element assemblies (records, messages, files, arrays, displays, reports, etc.) that the interfacing entity(ies) must provide, store, send, access, receive, etc.:
  1. Names/identifiers: a) project-unique identifier; b) non-technical (natural language) name; c) technical name (record or data structure name in code or database); d) abbreviations or synonymous names
  2. Data elements in the assembly and their structure (number, order, grouping)
  3. Medium (such as disk) and structure of data elements/assemblies on the medium
  4. Visual and auditory characteristics of displays and other outputs (colors, layouts, fonts, icons, beeps, lights)
  5. Relationships among assemblies, such as sorting/access characteristics
  6. Priority, timing, frequency, volume, sequencing, and other constraints; whether assembly may be updated; whether business rules apply
  7. Security and privacy constraints
  8. Sources (setting/sending entities) and recipients (using/receiving entities)
- **e.** Required characteristics of communication methods that the interfacing entity(ies) must use for the interface:
  1. Project-unique identifier(s)
  2. Communication links/bands/frequencies/media and their characteristics
  3. Message formatting
  4. Flow control (sequence numbering and buffer allocation)
  5. Data transfer rate, whether periodic/aperiodic, and interval between transfers
  6. Routing, addressing, and naming conventions
  7. Transmission services, including priority and grade
  8. Safety/security/privacy considerations (encryption, user authentication, compartmentalization, and auditing)
- **f.** Required characteristics of protocols the interfacing entity(ies) must use for the interface:
  1. Project-unique identifier(s)
  2. Priority/layer of the protocol
  3. Packeting, including fragmentation and reassembly, routing, and addressing
  4. Legality checks, error control, and recovery procedures
  5. Synchronization, including connection establishment, maintenance, termination
  6. Status, identification, and any other reporting features
- **g.** Other required characteristics — physical compatibility of the interfacing entities (dimensions, tolerances, loads, plug compatibility, voltages, etc.)

#### 3.y Precedence and Criticality of Requirements
The last paragraph of §3 shall specify, if applicable, the order of precedence, criticality, or assigned weights indicating the relative importance of requirements in this specification. Examples include identifying requirements critical to safety, to security, or to privacy for singling them out for special treatment. If all requirements have equal weight, state so.

---

### 4. Qualification Provisions

Define a set of qualification methods and specify for each requirement in §3 the qualification method(s) to be used to ensure the requirement has been met. A table may be used, or each requirement in §3 may be annotated with the method(s). Methods may include:

- **a. Demonstration:** The operation of interfacing entities that relies on observable functional operation not requiring the use of instrumentation, special test equipment, or subsequent analysis
- **b. Test:** The operation of interfacing entities using instrumentation or special test equipment to collect data for later analysis
- **c. Analysis:** The processing of accumulated data obtained from other qualification methods — reduction, interpretation, or extrapolation of test results
- **d. Inspection:** The visual examination of interfacing entities, documentation, etc.
- **e. Special qualification methods:** Any special qualification methods for the interfacing entities, such as special tools, techniques, procedures, facilities, and acceptance limits

---

### 5. Requirements Traceability

For system-level interfacing entities, this paragraph does not apply.

For each subsystem or lower-level interfacing entity covered by this IRS, this paragraph shall contain:

- **a.** Traceability from each requirement imposed on the entity in this specification to the system (or subsystem, if applicable) requirements it addresses. (Alternatively, this traceability may be provided by annotating each requirement in §3.)
- **b.** Traceability from each system (or subsystem, if applicable) requirement that has been allocated to the interfacing entity and that affects an interface covered in this specification to the requirements in this specification that address it.

*Note: Each level of system refinement may result in requirements not directly traceable to higher-level requirements. A system architectural design creating multiple CSCIs may result in requirements about how the CSCIs will interface, even though these interfaces are not covered in system requirements. Such requirements may be traced to a general requirement such as "system implementation" or to the system design decisions that resulted in their generation.*

---

### 6. Notes
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
| HWCI | Hardware Configuration Item |
| IRS | Interface Requirements Specification |
| SRS | Software Requirements Specification |
| SSS | System/Subsystem Specification |

---

## Relationship to SSS and SRS

The IRS sits between the SSS and the SRS in the requirements hierarchy:

- **SSS (DI-IPSC-81431A)** specifies system-level requirements. External interface requirements may be placed in the SSS (§3.3) or delegated to one or more IRSs.
- **IRS (this DID)** specifies interface requirements independently of the SSS and SRS, enabling separate CM and separate contracting of interface definition. An IRS may supplement both the SSS and the SRS.
- **SRS (DI-IPSC-81433A)** specifies CSCI-level requirements. CSCI external interface requirements may be placed in the SRS (§3.3) or delegated to an IRS.

The §3.3.x content checklist in the SSS and SRS (items a–g: priority, interface type, data elements, data element assemblies, communication methods, protocols, physical compatibility) is identical to the §3.x checklist in the IRS — these three DIDs share a common interface specification vocabulary.

---

## ICM Usage Notes

This DID defines the required content of an Interface Requirements Specification. An AI agent working within an ICM project can use this file to:

- **Generate** an IRS by first identifying all interfaces in §3.1 (with a diagram), then creating one §3.x subparagraph per interface using the a–g requirement checklist. For each interfacing entity, distinguish between entities with fixed characteristics (which impose requirements) and entities being developed (which receive requirements).
- **Validate** a draft IRS for completeness — each interface in §3.x must have a project-unique identifier, each requirement must be annotated with its qualification method (§4), and bidirectional traceability (§5) must be present for all subsystem or lower-level entities.
- **Decide IRS vs. SSS §3.3 vs. SRS §3.3:** use a separate IRS when: (1) interfaces involve entities owned by different organizations or contractors; (2) interface requirements need to be baselined and CM-managed independently; (3) interface complexity warrants a separate document. Reference the IRS from the SSS/SRS §3.3 rather than duplicating content.
- **Map to the SDD/IDD:** the IRS establishes what the interface must do (requirements); the SDD §4.3 or IDD (DI-IPSC-81436) establishes how it is designed (design). Every IRS requirement in §3.x must be addressable in the corresponding SDD/IDD interface design section.
- **Map to the STP and RTVM:** IRS requirements must be addressed in the Software Test Plan (DI-IPSC-81438A) — qualification methods in §4 of the IRS drive the test cases. RTVM (DI-MGMT-82133A) §3.2.17 (Requirement Allocation) should reference which IRS paragraph(s) capture requirements allocated to each interfacing CSCI.

When generating an IRS, create §3.1 first (interface inventory with diagram), then draft §3.x sections for each interface before filling in the a–g detail. This top-down approach prevents missed interfaces and keeps the document organized by interface boundary rather than by requirement type.
