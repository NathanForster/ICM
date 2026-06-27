# DID: System/Subsystem Specification (SSS)

**DID Number:** DI-IPSC-81431A  
**Title:** System/Subsystem Specification (SSS)  
**Approval Date:** 2000-01-10  
**Supersedes:** DI-IPSC-81431  
**AMSC Number:** N7376  
**Preparing Activity:** N/SPAWAR  
**Source PDF:** [SSS-DI-IPSC-81431A.pdf](SSS-DI-IPSC-81431A.pdf)

---

## Purpose

The SSS specifies the requirements for a system or subsystem and the methods to ensure each requirement is met. Requirements pertaining to external interfaces may be placed in the SSS or in one or more Interface Requirements Specifications (IRSs, DI-IPSC-81434A) referenced from the SSS.

The SSS, possibly supplemented by IRSs, is used as the basis for design and qualification testing. Throughout the DID, "system" may be interpreted as "subsystem" — the resulting document should be titled System Specification or Subsystem Specification (SSS) as applicable.

---

## Format Requirements

Contractor format unless otherwise specified in the CDRL (DD 1423). May be delivered on paper or electronic media; may reside in a CASE tool rather than a traditional document.

---

## Required Content Structure

### 1. Scope

#### 1.1 Identification
Full identification of the system and software to which this document applies: identification number(s), title(s), abbreviation(s), version number(s), and release number(s).

#### 1.2 System Overview
State the purpose of the system and the software to which this document applies. Describe the general nature of the system and software; summarize development, operation, and maintenance history; identify the project sponsor, acquirer, user, developer, and support agencies; identify current and planned operating sites; list other relevant documents.

#### 1.3 Document Overview
Summarize the purpose and contents of this document. Describe any security or privacy considerations associated with its use.

---

### 2. Referenced Documents
List number, title, revision, and date of all documents referenced. Identify the source for all documents not available through normal Government stocking activities.

---

### 3. Requirements

This section specifies the system requirements — those characteristics that are conditions for acceptance — and shall state in objective terms those characteristics of the system that the acquirer is willing to leave up to the developer. Each requirement shall be assigned a project-unique identifier to support testing and traceability.

Each requirement shall be annotated with the qualification method(s) to be used (see §4) and, for subsystems, traceability to system requirements (see §5.a) if not provided in those sections.

#### 3.1 Required States and Modes
If the system operates in more than one state or mode, identify and distinguish them. Requirements shall be correlated to states and modes. A table or other method in this paragraph, or annotation of the requirements in appendices, may be used.

#### 3.2 System Capability Requirements
Divided into subparagraphs (3.2.x) to itemize the requirements associated with each capability. "Capability" may be replaced with "function," "subject," "object," or other useful presentation term. Each 3.2.x subparagraph shall identify a required system capability and shall specify required behavior, including timing constraints, sequencing, accuracy, capacities (how much/how many), priorities, continuous operation requirements, and allowable deviations based on operating conditions.

#### 3.3 System External Interface Requirements
Divided into subparagraphs specifying any external interface requirements. May reference one or more IRSs instead.

##### 3.3.1 Interface Identification and Diagrams
Identify the required external interfaces and the interfacing entities (systems, configuration items, users, etc.) by name, number, version, and documentation references. Designate which entities have fixed interface characteristics (and therefore impose requirements on interfacing entities) and which are being developed or modified. Provide one or more interface diagrams.

##### 3.3.x (Project-Unique Identifier of Interface)
Beginning with 3.3.2, one subparagraph per interface. Briefly identify the interfacing entities and divide into subparagraphs as needed to state the requirements imposed on one or both of the interfacing entities. Requirements include, as applicable:

- **a.** Priority the system must assign the interface
- **b.** Requirements on the type of interface (real-time data transfer, storage-and-retrieval, etc.) to be implemented
- **c.** Required characteristics of individual data elements the interfacing entity will provide, store, send, access, receive, etc.:
  1. Names/identifiers: a) project-unique identifier; b) non-technical name; c) DoD standard data element name; d) technical name (variable or field name); e) abbreviation or synonymous names
  2. Data type (alphanumeric, integer, etc.)
  3. Size and format (length and punctuation of a character string)
  4. Units of measurement (meters, dollars, nanoseconds)
  5. Range or enumeration of possible values (such as 0–99)
  6. Accuracy (how correct) and precision (significant digits)
  7. Priority, timing, frequency, volume, sequencing, and other constraints; whether data element may be updated; whether business rules apply
  8. Security and privacy constraints
  9. Sources (setting/sending entities) and recipients (using/receiving entities)
- **d.** Required characteristics of data element assemblies (records, messages, files, arrays, displays, reports, etc.):
  1. Names/identifiers: a) project-unique identifier; b) non-technical name; c) technical name (record or data structure name); d) abbreviations or synonymous names
  2. Data elements in the assembly and their structure (number, order, grouping)
  3. Medium (such as disk) and structure of data elements/assemblies on the medium
  4. Visual and auditory characteristics of displays and other outputs (colors, layouts, fonts, icons, beeps, lights)
  5. Relationships among assemblies, such as sorting/access characteristics
  6. Priority, timing, frequency, volume, sequencing, and other constraints; whether assembly may be updated; whether business rules apply
  7. Security and privacy constraints
  8. Sources (setting/sending entities) and recipients (using/receiving entities)
- **e.** Required characteristics of communication methods the system must use for the interface:
  1. Project-unique identifier(s)
  2. Communication links/bands/frequencies/media and their characteristics
  3. Message formatting
  4. Flow control (sequence numbering and buffer allocation)
  5. Data transfer rate, whether periodic/aperiodic, and interval between transfers
  6. Routing, addressing, and naming conventions
  7. Transmission services, including priority and grade
  8. Safety/security/privacy considerations (encryption, user authentication, compartmentalization, auditing)
- **f.** Required characteristics of protocols the system must use for the interface:
  1. Project-unique identifier(s)
  2. Priority/layer of the protocol
  3. Packeting, including fragmentation and reassembly, routing, and addressing
  4. Legality checks, error control, and recovery procedures
  5. Synchronization, including connection establishment, maintenance, termination
  6. Status, identification, and any other reporting features
- **g.** Other required characteristics — physical compatibility of the interfacing entities (dimensions, tolerances, loads, plug compatibility, voltages, etc.)

#### 3.4 System Internal Interface Requirements
Specify requirements, if any, imposed on interfaces internal to the system. If all internal interfaces are left to the design or to requirement specifications for system components, so state. If requirements are imposed, §3.3 provides a list of topics to consider.

#### 3.5 System Internal Data Requirements
Specify requirements, if any, imposed on data internal to the system. Includes requirements on databases and data files to be included in the system. If all decisions about internal data are left to the design or to requirements specifications for system components, so state. §§3.3.x.c and 3.3.x.d provide a list of topics to consider.

#### 3.6 Adaptation Requirements
Specify requirements, if any, concerning installation-dependent data the system is required to provide (site-dependent latitude and longitude, state tax codes) and operational parameters that may vary according to operational needs (operation-dependent targeting constants or data recording).

#### 3.7 Safety Requirements
Specify system requirements concerned with preventing or minimizing unintended hazards to personnel, property, and the physical environment. Examples: restricting use of dangerous materials; classifying explosives for shipping, handling, and storing; abort/escape provisions from enclosures; gas detection and warning devices; grounding of electrical systems; decontamination; explosion proofing. Include nuclear safety requirements if applicable.

#### 3.8 Security and Privacy Requirements
Specify system requirements concerned with maintaining security and privacy. Include: security/privacy environment in which the system must operate; type and degree of security or privacy; security/privacy risks the system must withstand; required safeguards; security/privacy policy that must be met; security/privacy accountability the system must provide; criteria for security/privacy certification/accreditation.

#### 3.9 System Environment Requirements
Specify requirements, if any, regarding the environment in which the system must operate. For software systems: the computer hardware and operating system on which the software must run. Additional computer resource requirements are given in §3.10. Environmental conditions the system must withstand during transportation, storage, and operation (wind, rain, temperature, geographic location, induced environment such as motion/shock/noise/electromagnetic radiation, environments due to enemy action).

#### 3.10 Computer Resource Requirements
Divided into subparagraphs. Coverage depends on whether computer resources constitute the system's environment (software system) or are components of the system (hardware-software system).

##### 3.10.1 Computer Hardware Requirements
Requirements for computer hardware that must be used by or incorporated into the system. Include as applicable: number of each type of equipment, type, size, capacity, and other required characteristics of processors, memory, input/output devices, auxiliary storage, communications/network equipment, and other required equipment.

##### 3.10.2 Computer Hardware Resource Utilization Requirements
Specify requirements, if any, on the system's computer hardware resource utilization — maximum allowable use of processor capacity, memory capacity, auxiliary storage device capacity, and communications/network equipment capacity. State the conditions under which each resource utilization is to be measured.

##### 3.10.3 Computer Software Requirements
Specify requirements regarding computer software that must be used by or incorporated into the system. Examples: operating systems, database management systems, communications/network software, utility software, input and output equipment simulators, test software, and manufacturing software. Provide correct nomenclature, version, and documentation references.

##### 3.10.4 Computer Communications Requirements
Additional requirements, if any, concerning computer communications that must be used by or incorporated into the system. Include: geographic locations to be linked; configuration and network topology; transmission techniques; data transfer rates; gateways; required system use times; type and volume of data to be transmitted/received; time boundaries for transmission/reception/response; peak volumes of data; diagnostic features.

#### 3.11 System Quality Factors
Specify requirements, if any, pertaining to system quality factors:
- Functionality (the ability to perform all required functions)
- Reliability (mean time between failure for equipment)
- Maintainability (ability to be easily serviced, repaired, or corrected)
- Availability (ability to be accessed and operated when needed)
- Flexibility (ability to be easily adapted to changing requirements)
- Portability (ability to be easily modified for a new environment)
- Reusability (ability to be used in multiple applications)
- Testability (ability to be easily and thoroughly tested)
- Usability (ability to be easily learned and used)
- Other attributes

#### 3.12 Design and Construction Constraints
Specify requirements, if any, that constrain the design and construction of the system. For hardware-software systems, include physical requirements imposed on the system. Requirements may be specified by reference to appropriate commercial or military standards and specifications. Examples:

- **a.** Use of a particular system architecture or requirements on the architecture; use of standard, military, or existing components; use of Government/acquirer-furnished property
- **b.** Use of particular design or construction standards; data standards; particular programming language; workmanship requirements and production techniques
- **c.** Physical characteristics (weight limits, dimensional limits, color, protective coatings); interchangeability of parts; ability to be transported; ability to be carried or set up by one person or a given number
- **d.** Materials that can and cannot be used; handling of toxic materials; limits on electromagnetic radiation the system may generate
- **e.** Use of nameplates, part marking, serial and lot number marking, and other identifying markings
- **f.** Flexibility and expandability to support anticipated areas of growth or changes in technology, threat, or mission

#### 3.13 Personnel-Related Requirements
Specify system requirements to accommodate the number, skill levels, duty cycles, training needs, or other information about the personnel who will use or support the system. Include human factors engineering requirements, as applicable — considerations for capabilities and limitations of humans, foreseeable human errors under normal and extreme conditions, and specific areas where effects of human error would be particularly serious. Examples: adjustable-height workstations, color and duration of error messages, physical placement of critical indicators or buttons, and use of auditory signals.

#### 3.14 Training-Related Requirements
Specify system requirements pertaining to training. Examples: training devices and training materials to be included in the system.

#### 3.15 Logistics-Related Requirements
Specify system requirements concerned with logistics considerations. Include: system maintenance, software support, system transportation modes, supply-system requirements, impact on existing facilities, and impact on existing equipment.

#### 3.16 Other Requirements
Specify additional system requirements, if any, not covered in the previous paragraphs. Examples include requirements for system documentation (specifications, drawings, technical manuals, test plans and procedures, installation instruction data) if not covered in other contractual documents.

#### 3.17 Packaging Requirements
Specify requirements, if any, for packaging, labeling, and handling the system and its components for delivery. Applicable military specifications and standards may be referenced.

#### 3.18 Precedence and Criticality of Requirements
Specify, if applicable, the order of precedence, criticality, or assigned weights indicating the relative importance of requirements. Examples: identifying requirements critical to safety, to security, or to privacy for special treatment. If all requirements have equal weight, state so.

---

### 4. Qualification Provisions

Define a set of qualification methods and specify for each requirement in §3 the method(s) to be used to ensure that the requirement has been met. A table may be used. Methods may include:

- **a. Demonstration:** Operation of the system (or a part) that relies on observable functional operation without use of instrumentation, special test equipment, or subsequent analysis
- **b. Test:** Operation of the system (or a part) using instrumentation or other special test equipment to collect data for later analysis
- **c. Analysis:** Processing of accumulated data obtained from other qualification methods — examples: reduction, interpolation, or extrapolation of test results
- **d. Inspection:** Visual examination of system components, documentation, etc.
- **e. Special qualification methods:** Special tools, techniques, procedures, facilities, acceptance limits, use of standard samples, preproduction or periodic production samples, pilot models, or pilot lots

---

### 5. Requirements Traceability

For system-level specifications, this paragraph does not apply.

For subsystem-level specifications, this paragraph shall contain:

- **a.** Traceability from each subsystem requirement in this specification to the system requirements it addresses (alternatively, this traceability may be provided by annotating each requirement in §3)
- **b.** Traceability from each system requirement that has been allocated to the subsystem covered by this specification to the subsystem requirements that address it. All system requirements allocated to the subsystem shall be accounted for. Those that trace to subsystem requirements contained in IRSs shall reference those IRSs.

*Note: Each level of system refinement may result in requirements not directly traceable to higher-level requirements. A system architectural design creating two subsystems may result in requirements about how the subsystems will interface, even though these interfaces are not covered in system requirements. Such requirements may be traced to a general requirement such as "system implementation" or to the system design decisions that resulted in their generation.*

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
| SSS | System/Subsystem Specification |

---

## ICM Usage Notes

This DID defines the required content of a System/Subsystem Specification. An AI agent working within an ICM project can use this file to:

- **Generate** an SSS by working through §§3.1–3.18 systematically: start with states/modes (3.1), then capabilities (3.2.x), then external interfaces (3.3.x using the a–g checklist), then internal interfaces (3.4), internal data (3.5), and continuing through all remaining requirement paragraphs
- **Validate** a draft SSS for completeness — ensure each requirement is assigned a project-unique identifier, has an annotated qualification method (§4), and is traceable. For subsystem-level SSS, verify bidirectional traceability in §5
- **Decide IRS vs. SSS for interface requirements:** requirements pertaining to external interfaces may be placed in the SSS or in a separate IRS (DI-IPSC-81434A). If interfaces are numerous or complex, an IRS reduces SSS bulk and enables independent CM of interface requirements
- **Map to the SRS:** the SRS (DI-IPSC-81433A) captures software-specific requirements for CSCIs derived from the SSS. Requirements allocated to CSCIs in the SSS must appear in or trace through the SRS
- **Map to qualification testing:** §4 qualification methods (Demonstration/Test/Analysis/Inspection) become the test basis for the Software Test Plan (STP, DI-IPSC-81438A) and the test results basis for the Software Test Report (STR, DI-IPSC-81440A) and RTVM (DI-MGMT-82133A)
- **Map to the CI Documentation Recommendation (DI-SESS-82007B):** the SSS is a type of configuration documentation for a system-level CI. The CI Documentation Recommendation drives which system elements receive SSS-level documentation

When generating an SSS, annotate each requirement in §3 with its qualification method(s) from §4 (e.g., "T" for Test, "D" for Demonstration) either inline or in a table — this eliminates the need for a separate qualification provisions matrix and keeps requirements and verification methods co-located.
