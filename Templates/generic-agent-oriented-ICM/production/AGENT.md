# Agent Contract — production

## Inputs

- Implementation tasks and change requests
- Requirements and acceptance criteria
- Applicable standards from this workspace's `ICM.md` Standards section (or `standards/` if the project has one)

## Outputs

- Working software, scripts, or technical deliverables
- Build and test results
- Updates to implementation workflow state

## Definition of Done

A production task is Done when ALL of the following are true:

- [ ] Deliverable implements the stated requirement or task in full
- [ ] Output passes the project's checks — lint and tests for code; link checker, build, and validator for a site or document build (where a toolchain exists)
- [ ] New behaviour is covered by a test or a documented manual check (adapt to the kind of production work this project does)
- [ ] Assumptions and known limitations recorded with the deliverable
- [ ] Workflow state updated and work committed to version control

## Escalate When

- Requirements conflict or acceptance criteria are ambiguous
- A dependency (library, service, credential) is missing or blocked
- The change would modify another workspace's files
- A test failure cannot be explained or reproduced
