# DID: Software Requirements Specification (SRS)

**DID Number:** DI-IPSC-81433A  
**Title:** Software Requirements Specification (SRS)  
**Approval Date:** 1999-12-15  
**Supersedes:** DI-IPSC-81433  
**AMSC Number:** N7358  
**Office of Primary Responsibility:** NAVY/EC  
**Source PDF:** [SRS-DI-IPSC-81433A.pdf](SRS-DI-IPSC-81433A.pdf)

---

## Purpose

The SRS specifies the requirements for a Computer Software Configuration Item (CSCI) and the methods to be used to ensure each requirement has been met. Requirements pertaining to the CSCI's external interfaces may be presented in the SRS or in one or more Interface Requirements Specifications (IRSs) (DI-IPSC-81434A).

The SRS, possibly supplemented by IRSs, is used as the basis for design and qualification testing of a CSCI.

This DID is used when the developer is tasked to **define and record the software requirements to be met by a CSCI**.

---

## General Instructions

- **Automated techniques:** Use of automated techniques is encouraged. "Document" means a collection of data regardless of medium.
- **Alternate presentation styles:** Diagrams, tables, matrices, and other presentation styles are acceptable substitutes for text when they make data more readable.
- **Standard data descriptions:** If a data description required by this DID has been published in a standard data element dictionary specified in the contract, reference to that dictionary entry is preferred over including the description itself.
- **Substitute documents:** Commercial or other existing documents may be substituted if they contain the required data.
- **Tailoring:** If a paragraph is tailored out, the document shall state the paragraph number and title followed by "This paragraph has been tailored out."
- **Multiple paragraphs:** Any section, paragraph, or subparagraph may be written as multiple paragraphs or subparagraphs to enhance readability.

---

## Format Requirements

- Contractor format unless otherwise specified in the CDRL (DD 1423)
- May be delivered on paper or electronic media (ASCII, CALS, word processor, CASE tool, etc.)
- May reside in a CASE or other automated tool rather than a traditional document
- Must include:
  - **Title page:** document number, volume number, version/revision, security markings, date, title, name/abbreviation of system/subsystem/item, contract number, CDRL item number, organization, name/address of preparer, distribution statement
  - **Table of contents:** number, title, and page of each paragraph, figure, table, and appendix
  - **Page numbering:** unique page number displaying document number, version, and date on each page

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

### 3. Requirements

This section specifies the CSCI requirements — those characteristics that are conditions for its acceptance. Each requirement shall be assigned a project-unique identifier to support testing and traceability, and shall be stated in a way that an objective test can be defined for it. Each requirement shall be annotated with associated qualification method(s) (see Section 4) and traceability to system (or subsystem, if applicable) requirements (see Section 5).

The degree of detail is left to the developer. Include characteristics the acquirer is willing to leave to design.

#### 3.1 States and Modes
If the CSCI is required to operate in more than one state or mode (e.g., idle, ready, active, post-use analysis, training, degraded, emergency, backup, wartime, peacetime), identify and define each state and mode. Correlate all requirements in Section 3 to states and modes by table, annotation, or appendix reference.

If no states/modes are required, this paragraph shall so state.

#### 3.2 CSCI Capability Requirements
One subparagraph per CSCI capability, itemizing all requirements associated with that capability.

##### 3.2.x (CSCI Capability)
Identify a required CSCI capability. If a capability can be more clearly specified by dividing it into constituent capabilities, present those as subparagraphs. Requirements shall specify required behavior of the CSCI and include, as applicable:
- Timing constraints, sequencing, accuracy, capacities (how much/how many)
- Priorities, continuous operation requirements, allowable deviations based on operating conditions
- Required behavior under unexpected, unallowed, or "out of bounds" conditions
- Requirements for error handling
- Provisions to support continuity of operations in the event of emergencies

Paragraph 3.3.x of this DID provides a list of topics to consider when specifying inputs the CSCI must accept and outputs it must produce.

#### 3.3 CSCI External Interface Requirements
Divided into subparagraphs to specify the external interface requirements for the CSCI. This paragraph may reference one or more IRSs (DI-IPSC-81434A).

##### 3.3.1 Interface Identification and Diagrams
Identify the required external interfaces of the CSCI (that is, relationships with other entities involving sharing, providing, or exchanging data). Each interface shall include a project-unique identifier and designate the interfacing entities by name, number, version, and documentation references. State which interfaces are fixed and which are being developed or modified (having interface requirements imposed on them). Provide one or more interface diagrams.

##### 3.3.x (Project-Unique Identifier of an Interface)
One subparagraph per CSCI external interface (beginning with 3.3.2). Briefly identify the interfacing entities and state the CSCI's requirements for the interface. Requirements shall include, as applicable:

- **a. Priority** the CSCI must assign the interface
- **b. Requirements on type of interface** (e.g., real-time data transfer, storage-and-retrieval)
- **c. Required characteristics of individual data elements** the CSCI must provide/store/send/access/receive:
  1. Names/identifiers: (a) project-unique identifier, (b) non-technical name, (c) DoD standard data element name, (d) technical name (variable/field name in code or database), (e) abbreviation or synonymous names
  2. Data type (alphanumeric, integer, etc.)
  3. Size and format (length and punctuation of a character string)
  4. Units of measurement (meters, dollars, nanoseconds)
  5. Range or enumeration of possible values (such as 0–99)
  6. Accuracy (how correct) and precision (number of significant digits)
  7. Priority, timing, frequency, volume, sequencing, and other constraints; whether data element may be updated; whether business rules apply
  8. Security and privacy constraints
  9. Sources (setting/sending entities) and recipients (using/receiving entities)
- **d. Required characteristics of data element assemblies** (records, messages, files, arrays, displays, reports, etc.) the CSCI must provide/store/send/access/receive:
  1. Names/identifiers: (a) project-unique identifier, (b) non-technical name, (c) technical name (record or data structure name in code/database), (d) abbreviations or synonymous names
  2. Data elements in the assembly and their structure (number, order, grouping)
  3. Medium (such as disk) and structure of data elements/assemblies on the medium
  4. Visual and auditory characteristics of displays/outputs (colors, layouts, fonts, icons, display elements, beeps, lights)
  5. Relationships among assemblies (sorting/access characteristics)
  6. Priority, timing, frequency, volume, sequencing, and other constraints; whether assembly may be updated; whether business rules apply
  7. Security and privacy constraints
  8. Sources (setting/sending entities) and recipients (using/receiving entities)
- **e. Required characteristics of communication methods** the CSCI must use for the interface:
  1. Project-unique identifier(s)
  2. Communication links/bands/frequencies/media and their characteristics
  3. Message formatting
  4. Flow control (sequence numbering, buffer allocation)
  5. Data transfer rate (periodic/aperiodic), interval between transfers
  6. Routing, addressing, and naming conventions
  7. Transmission services, including priority and grade
  8. Safety/security/privacy considerations (encryption, user authentication, compartmentalization, auditing)
- **f. Required characteristics of protocols** the CSCI must use for the interface:
  1. Project-unique identifier(s)
  2. Priority/layer of the protocol
  3. Packeting, including fragmentation and reassembly, routing, and addressing
  4. Legality checks, error control, and recovery procedures
  5. Synchronization, including connection establishment, maintenance, termination
  6. Status, identification, and other reporting features
- **g. Other required characteristics** such as physical compatibility of interfacing entities (dimensions, tolerances, loads, plug compatibility, voltages, etc.)

#### 3.4 CSCI Internal Interface Requirements
Specify requirements, if any, imposed on interfaces internal to the CSCI. If all internal interfaces are left to the design, state that fact. If such requirements are imposed, paragraph 3.3 of this DID provides a list of topics to consider.

#### 3.5 CSCI Internal Data Requirements
Specify requirements, if any, on data internal to the CSCI — including requirements on databases and data files to be included. If all internal data decisions are left to design, state that fact. If imposed, paragraphs 3.3.x.c and 3.3.x.d provide a list of topics to consider.

#### 3.6 Adaptation Requirements
Specify requirements, if any, for installation-dependent data the CSCI must provide (e.g., site-dependent latitude/longitude or site-dependent state tax codes) and operational parameters that may vary according to operational needs (e.g., parameters indicating operation-dependent targeting constants or data recording).

#### 3.7 Safety Requirements
Specify the CSCI requirements, if any, concerned with preventing or minimizing unintended hazards to personnel, property, and the physical environment. Examples:
- Safeguards the CSCI must provide to prevent inadvertent actions (such as accidentally issuing an "auto pilot off" command)
- Non-actions (failure to issue an intended "auto pilot off" command)
- Requirements regarding nuclear components of the system, including prevention of inadvertent detonation and compliance with nuclear safety rules

#### 3.8 Security and Privacy Requirements
Specify requirements, if any, concerned with maintaining security and privacy. Include as applicable:
- The security/privacy environment in which the CSCI must operate
- Type and degree of security or privacy to be provided
- Security/privacy risks the CSCI must withstand
- Required safeguards to reduce those risks
- The security/privacy policy that must be met
- Security/privacy accountability the CSCI must provide
- Criteria that must be met for security/privacy certification/accreditation

#### 3.9 CSCI Environment Requirements
Specify requirements, if any, regarding the environment in which the CSCI must operate — including the computer hardware and operating system on which the CSCI must run. (Additional computer resource requirements are in Section 3.10.)

#### 3.10 Computer Resource Requirements
Divided into the following subparagraphs:

##### 3.10.1 Computer Hardware Requirements
Specify the CSCI's requirements, if any, on computer hardware. Include as applicable:
- Number of each type of equipment, type, size, capacity
- Characteristics of processors, memory, input/output devices, auxiliary storage, communications/network equipment, and other required equipment

##### 3.10.2 Computer Hardware Resource Utilization Requirements
Specify requirements, if any, on the CSCI's computer hardware resource utilization (e.g., maximum allowable use of processor capacity, memory capacity, input/output device capacity, auxiliary storage device capacity, communications/network equipment capacity). Requirements shall include the conditions under which resource utilization is to be measured.

##### 3.10.3 Computer Software Requirements
Specify requirements, if any, on computer software that must be used by or incorporated into the CSCI. Examples: operating systems, management systems, communications/network software, utility software, input and equipment simulators, test software, and manufacturing software. Include correct nomenclature, version, and documentation references.

##### 3.10.4 Computer Communications Requirements
Specify additional requirements, if any, on computer communications that must be used by the CSCI. Examples:
- Geographic locations to be linked, configuration and network topology
- Transmission techniques, data transfer rates, gateways
- Required system use times: type and volume of data to be transmitted/received, time boundaries for transmission/reception/response
- Peak volumes of data, diagnostic features

#### 3.11 Software Quality Factors
Specify the CSCI requirements, if any, for software quality factors identified in the contract or derived from a higher level specification. Examples:
- **Functionality** — ability to perform all required functions
- **Reliability** — ability to deliver all required functions with correct, consistent results
- **Maintainability** — ability to be easily corrected
- **Availability** — ability to be accessed and operated when needed
- **Flexibility** — ability to be easily adapted to changing requirements
- **Portability** — ability to be easily modified for a new environment
- **Reusability** — ability to be used in multiple applications
- **Testability** — ability to be easily and thoroughly tested
- **Usability** — ability to be easily learned and used
- Other attributes specified in the contract

#### 3.12 Design and Implementation Constraints
Specify requirements, if any, that constrain the design and implementation of the CSCI. May be specified by reference to commercial or military standards. Examples:
- a. Use of a particular CSCI architecture; required databases; use of standard, military, or existing components; use of Government/acquirer-furnished property (equipment, information, or software)
- b. Use of particular design or implementation standards; data standards; programming language
- c. Flexibility and expandability to support anticipated areas of growth or changes in technology, threat, or mission

#### 3.13 Personnel-Related Requirements
Specify CSCI requirements, if any, to accommodate number, skill levels, duty cycles, training needs, or other information about the personnel who will use or support the CSCI. Include:
- Requirements for number of simultaneous users and for built-up help or training features
- Human factors engineering requirements: capabilities and limitations of humans; foreseeable human errors under normal and extreme conditions; specific areas where effects of human error would be particularly serious
- Examples: requirements for color and duration of error messages, physical placement of critical indicators or keys, use of auditory signals

#### 3.14 Training-Related Requirements
Specify requirements, if any, pertaining to training — for example, training software to be included in the CSCI.

#### 3.15 Logistics-Related Requirements
Specify requirements, if any, concerned with logistics considerations:
- System maintenance, software support, system transportation modes
- Supply-system requirements, impact on existing facilities, impact on existing equipment

#### 3.16 Other Requirements
Specify additional CSCI requirements, if any, not covered in the previous paragraphs.

#### 3.17 Packaging Requirements
Specify requirements, if any, for packaging, labeling, and handling the CSCI for delivery (e.g., delivery on 8-track magnetic tape labeled and packaged in a specific way). Applicable military specifications and standards may be referenced.

#### 3.18 Precedence and Criticality of Requirements
Specify, if applicable, the order of precedence, criticality, or assigned weights indicating the relative importance of the requirements in this specification. Identify requirements deemed critical to safety, security, or privacy for special treatment.

If all requirements have equal weight, this paragraph shall so state.

---

### 4. Qualification Provisions

Define a set of qualification methods and specify for each requirement in Section 3 the method(s) to be used to ensure the requirement has been met. A table may be used, or each requirement in Section 3 may be annotated with the method(s). Qualification methods:

- **a. Demonstration** — Operation of the CSCI, or part of it, relying on observable functional operation, not requiring instrumentation, special test equipment, or subsequent analysis
- **b. Test** — Operation of the CSCI, or part of it, using instrumentation or other special test equipment to collect data for later analysis
- **c. Analysis** — Processing of accumulated data obtained from other qualification methods (e.g., reduction, interpretation, extrapolation of test results)
- **d. Inspection** — Visual examination of CSCI code, documentation, etc.
- **e. Special qualification methods** — Any special methods for the CSCI, such as special tools, techniques, procedures, facilities, and acceptance limits

---

### 5. Requirements Traceability

- **a. Requirements → System (upward):** Traceability from each CSCI requirement in this specification to the system (or subsystem, if applicable) requirements it addresses. (Alternatively, may be provided by annotating each requirement in Section 3.)
  - Note: Each level of system refinement may result in requirements not directly traceable to higher-level requirements (e.g., CSCI interface requirements from system architectural decisions). Such requirements may be traced to a general requirement such as "system implementation" or to the system design decisions that produced them.
- **b. System → Requirements (downward):** Traceability from each system (or subsystem, if applicable) requirement allocated to this CSCI to the CSCI requirements that address it. All system/subsystem requirements allocated to this CSCI shall be accounted for. Requirements that trace to CSCI requirements contained in IRSs shall reference those IRSs.

---

### 6. Notes
- Background information, glossary, rationale
- Alphabetical listing of all acronyms and abbreviations with meanings
- List of terms and definitions needed to understand this document

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
| SDD | Software Design Document |
| SRS | Software Requirements Specification |
| STP | Software Test Plan |
| STR | Software Test Report |

---

## ICM Usage Notes

This DID defines the required content of a contractually deliverable SRS. An AI agent working within an ICM project can use this file to:

- **Generate** a compliant SRS outline or draft by reading system requirements and project context from ICM.md and CONTEXT.md, then populating Sections 1–3 with CSCI-specific requirements. Begin with §3.1 (states/modes) to frame all subsequent requirements.
- **Validate** a draft SRS for completeness — every requirement in Section 3 must have a project-unique identifier, a qualification method (Section 4), and bidirectional traceability (Section 5); every external interface (§3.3.x) must address all applicable items from the a–g checklist.
- **Generate external interface specs:** §3.3.x items c–f provide a detailed data element and protocol checklist that can drive generation of interface control documents. If interfaces are complex, reference to IRSs (DI-IPSC-81434A) is explicitly supported.
- **Map to the SDP:** the SRS is the basis for design (SDD) and qualification testing (STP). SDP §3.8.e covers software requirements analysis; SDP §3.8.k references CSCI qualification testing driven by SRS requirements.
- **Map to the RTVM:** every requirement in Section 3 with a project-unique identifier is a candidate row in the RTVM (DI-MGMT-82133A). The SRS is the primary source document for Tier 1/Tier 2 requirement entries.
- **Track completeness of §3.18:** safety-critical, security-critical, and privacy-critical requirements identified in §3.18 require special treatment — flag these in ICM's requirements tracking workspace for heightened review and verification.

When generating an SRS, populate §3.2 (capability requirements) and §3.3 (external interfaces) first, as these drive all traceability. Use §3.9–3.10 for environment and resource constraints after the functional requirements are stable.
