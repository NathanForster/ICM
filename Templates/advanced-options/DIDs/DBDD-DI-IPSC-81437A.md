# DID: Database Design Description (DBDD)

**DID Number:** DI-IPSC-81437A  
**Title:** Database Design Description (DBDD)  
**Approval Date:** 1999-12-15  
**Supersedes:** DI-IPSC-81437  
**AMSC Number:** N7362  
**Preparing Activity:** NAVY/EC  
**Source PDF:** [DBDD-DI-IPSC-81437A.pdf](DBDD-DI-IPSC-81437A.pdf)

---

## Purpose

The DBDD describes the design of a database — a collection of related data stored in one or more computerized files in a manner that can be accessed by users or computer programs via a database management system (DBMS). It can also describe the software units used to access or manipulate the data.

The DBDD is used as the basis for implementing the database and related software units. It provides the acquirer visibility into the design and provides information needed for software support.

Software units that access or manipulate the database may be described here or in Software Design Descriptions (SDDs — this library holds revision B, DI-IPSC-81435B; the DBDD text cites revision A). Interfaces may be described here or in Interface Design Descriptions (IDDs, DI-IPSC-81436A).

---

## Format Requirements

Contractor format unless otherwise specified in the CDRL (DD 1423). May be delivered on paper or electronic media; may reside in a CASE tool rather than a traditional document.

---

## Required Content Structure

### 1. Scope

#### 1.1 Identification
Full identification of the system and the software to which this document applies: identification number(s), title(s), abbreviation(s), version number(s), and release number(s).

#### 1.2 Database Overview
Briefly state the purpose of the database to which this document applies. Describe the general nature of the database; summarize the history of its development, use, and maintenance; identify the project sponsor, acquirer, user, developer, and support agencies; identify current and planned operating sites; list other relevant documents.

#### 1.3 Document Overview
Summarize the purpose and contents of this document and describe any security or privacy considerations associated with its use.

---

### 2. Referenced Documents
List the number, title, revision, and date of all documents referenced. Identify the source for all documents not available through normal Government stocking activities.

---

### 3. Database-Wide Design Decisions

Divided into paragraphs as needed to present database-wide design decisions — decisions about the database's behavioral design (how it will behave, from a user's point of view, in meeting its requirements, ignoring internal implementation) and other decisions affecting further design of the database.

If all such decisions are explicit in the system or CSCI requirements, this section shall so state. Design decisions that respond to requirements designated critical (safety, security, or privacy) shall be placed in separate subparagraphs. If a design decision depends upon system states or modes, this dependency shall be indicated. If some or all of the design decisions are described in the documentation of a custom or commercial DBMS, they may be referenced from this section. Design conventions needed to understand the design shall be presented or referenced. Examples:

- **a.** Design decisions regarding queries or other inputs the database will accept and outputs (displays, reports, messages, responses, etc.) it will produce, including interfaces with other systems, HWCIs, CSCIs, and users (§5.x.d of this DID identifies topics to be considered). If part or all of this information is given in IDDs, they may be referenced.
- **b.** Design decisions on database behavior in response to each input or query, including actions, response times and other performance characteristics, selected equations/algorithms/rules, disposition, and handling of unallowed inputs
- **c.** Design decisions on how databases/data files will appear to the user (§4.x of this DID identifies topics to be considered)
- **d.** Design decisions on the database management system to be used (including name, version/release) and the type of flexibility to be built into the database for adapting to changing requirements
- **e.** Design decisions on the levels and types of availability, security, privacy, and continuity of operations to be offered by the database
- **f.** Design decisions on database distribution (such as client/server), master database file updates and maintenance, including maintaining consistency, establishing/reestablishing and maintaining synchronization, enforcing integrity and business rules
- **g.** Design decisions on backup and restoration, including data and process distribution strategies, permissible actions during backup and restoration, and special considerations for new or non-standard technologies such as video and sound
- **h.** Design decisions on repacking, sorting, indexing, synchronization, and consistency, including automated disk management and space reclamation considerations, optimizing strategies and considerations, storage and size considerations, and population of the database and capture of legacy data

---

### 4. Detailed Design of the Database

Divided into paragraphs as needed to describe the detailed design of the database. The number of levels of design and the names of those levels shall be based on the design methodology used. Examples of database design levels include conceptual, internal, logical, and physical. If part or all of the design depends upon system states or modes, this dependency shall be indicated. Design conventions needed to understand the design shall be presented or referenced.

> **Terminology note (from the DID):** "data element assembly" means any entity, relation, schema, field, table, array, etc. that *has* structure (number/order/grouping of data elements) at a given design level; "data element" means any relation, attribute, field, cell, etc. that does *not* have structure at that level.

#### 4.x (Name of Database Design Level)
One paragraph per design level. Identify the database design level and describe the data elements and data element assemblies of the database in the terminology of the selected design method. Include the following, as applicable, presented in any order suited to the information:

- **a.** Characteristics of individual data elements in the database design:
  1. Names/identifiers: a) project-unique identifier; b) non-technical (natural-language) name; c) DoD standard data element name; d) technical name (e.g., field name in the database); e) abbreviation or synonymous names
  2. Data type (alphanumeric, integer, etc.)
  3. Size and format (length and punctuation of a character string)
  4. Units of measurement (meters, dollars, nanoseconds)
  5. Range or enumeration of possible values (such as 0–99)
  6. Accuracy (how correct) and precision (number of significant digits)
  7. Priority, timing, frequency, volume, sequencing, and other constraints; whether the data element may be updated; whether business rules apply
  8. Security and privacy constraints
  9. Sources (setting/sending entities) and recipients (using/receiving entities)
- **b.** Characteristics of data element assemblies (records, messages, files, arrays, displays, reports, etc.) in the database design:
  1. Names/identifiers: a) project-unique identifier; b) non-technical (natural language) name; c) technical name (record or data structure name in code or database); d) abbreviations or synonymous names
  2. Data elements in the assembly and their structure (number, order, grouping)
  3. Medium (such as disk) and structure of data elements/assemblies on the medium
  4. Visual and auditory characteristics of displays and other outputs (colors, layouts, fonts, icons, beeps, lights)
  5. Relationships among assemblies, such as sorting/access characteristics
  6. Priority, timing, frequency, volume, sequencing, and other constraints; whether the assembly may be updated and whether business rules apply
  7. Security and privacy constraints
  8. Sources (setting/sending entities) and recipients (using/receiving entities)

---

### 5. Detailed Design of Software Units Used for Database Access or Manipulation

Divided into paragraphs to describe each software unit used for database access or manipulation. If part or all of this information is provided elsewhere — such as in an SDD, the SDD for a customized DBMS, or the user manual of a commercial DBMS — that information may be referenced rather than repeated here. If part or all of the design depends upon system states or modes, this dependency shall be indicated. Design conventions needed to understand the design shall be presented or referenced.

#### 5.x (Project-Unique Identifier of a Software Unit, or Designator for a Group of Software Units)
Identify a software unit by project-unique identifier and describe the unit (or designate a group of software units and describe them in subparagraphs). Software units that contain other software units may reference the descriptions of those units rather than repeating information. Include, as applicable:

- **a.** Unit design decisions, if any, such as algorithms to be used, if not previously selected
- **b.** Any constraints, limitations, or unusual features in the design of the software unit
- **c.** The programming language to be used and rationale for its use if other than the specified CSCI language
- **d.** If the software unit consists of or contains procedural commands (such as menu selections in a DBMS for defining forms and reports, on-line DBMS queries for database access and manipulation, input to a graphical user interface (GUI) builder for automated code generation, commands to the operating system, or shell scripts): a list of the procedural commands and a reference to user manuals or other documents that explain them
- **e.** If the software unit contains, receives, or outputs data: a description of its inputs, outputs, and other data elements and data element assemblies, as applicable. Data local to the software unit shall be described separately from data input to or output from it. Interface characteristics may be provided here or by referencing Interface Design Description(s). If a given interfacing entity is not covered by this DBDD, state its characteristics as assumptions or as "When [the entity not covered] does this, [the software unit] will…". Include as applicable, noting differences from the point of view of the interfacing entities:
  1. Project-unique identifier for the interface
  2. Identification of the interfacing entities (software units, configuration items, users, etc.) by name, number, version, and documentation references
  3. Priority assigned to the interface by the interfacing entity(ies)
  4. Type of interface (real-time data transfer, storage-and-retrieval of data, etc.) to be implemented
  5. Characteristics of individual data elements (topics per §4.x.a of this DID)
  6. Characteristics of data element assemblies (topics per §4.x.b of this DID)
  7. Characteristics of communication methods: a) project-unique identifier(s); b) communication links/bands/frequencies/media; c) message formatting; d) flow control; e) data transfer rate, periodic/aperiodic, interval; f) routing, addressing, naming conventions; g) transmission services incl. priority and grade; h) safety/security/privacy considerations (encryption, user authentication, compartmentalization, auditing)
  8. Characteristics of protocols: a) project-unique identifier(s); b) priority/layer; c) packeting incl. fragmentation/reassembly, routing, addressing; d) legality checks, error control, recovery; e) synchronization incl. connection establishment, maintenance, termination; f) status, identification, and other reporting features
  9. Other characteristics — physical compatibility of the interfacing entity(ies) (dimensions, tolerances, loads, voltages, plug compatibility, etc.)
- **f.** If the software unit contains logic: the logic to be used by the software unit, including as applicable:
  1. Conditions in effect within the software unit when its execution is initiated
  2. Conditions under which control is passed to other software units
  3. Response and response time to each input, including data conversion, renaming, and data transfer operations
  4. Sequence of operations and dynamically controlled sequencing during the software unit's operation, including: a) the method for sequence control; b) the logic and input conditions of that method (timing variations, priority assignments); c) data transfer in and out of memory; d) the sensing of discrete input signals and timing relationships between interrupt operations within the software unit
  5. Exception and error handling

---

### 6. Requirements Traceability

This section shall contain:

- **a.** Traceability from each database or other software unit covered by this DBDD to the system or CSCI requirements it addresses
- **b.** Traceability from each system or CSCI requirement that has been allocated to a database or other software unit covered in this DBDD to the database or other software units that address it

---

### 7. Notes
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
| DBMS | Database Management System |
| GUI | Graphical User Interface |
| HWCI | Hardware Configuration Item |
| IDD | Interface Design Description |
| SDD | Software Design Description |

---

## ICM Usage Notes

This DID defines the required content of a Database Design Description. An AI agent working within an ICM project can use this file to:

- **Generate** a DBDD by: (1) recording database-wide design decisions in §3 (DBMS selection, availability/security levels, distribution, backup, indexing/optimization); (2) describing each design level in §4.x (e.g. conceptual → logical → physical), with data elements (a) and assemblies (b) in the terminology of the chosen method; (3) describing access/manipulation software units in §5.x, referencing the SDD or DBMS documentation instead of duplicating it
- **Validate** a draft DBDD for completeness — §3 must either state design decisions or explicitly state that all decisions are explicit in requirements; each §4.x design level must name its methodology level; §6 traceability must be bidirectional (database/software unit ↔ system/CSCI requirements)
- **Decide SDD vs. DBDD content split:** software units that access or manipulate the database may be described in the SDD (DI-IPSC-81435B) or here — pick one home per unit and reference from the other; never duplicate. For a commercial DBMS, reference its user manual for procedural commands (§5.x.d) rather than restating them.
- **Map to the IDD:** database interface characteristics (§5.x.e) may be delegated to IDDs (DI-IPSC-81436A) — reference the IDD's project-unique interface identifiers rather than restating the a–h communication/protocol detail
- **Map to the SPS:** SPS §5.1 ("as built" software design) references the DBDD when database design is delivered separately; if not delivered, the equivalent content must be included in the SPS directly
- **Map to the SDD §3.c:** the SDD's CSCI-wide design decision on "how databases and data files appear to the end user" may be presented in the SDD or referenced to this DBDD (§3.c here)

When generating a DBDD, settle §3 (database-wide decisions) first — DBMS choice and distribution strategy constrain everything in §4 and §5. Then work top-down through design levels in §4, and describe only project-developed access software in §5, referencing DBMS documentation for the rest.
