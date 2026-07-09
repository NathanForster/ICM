# Agent Contract — production

## Inputs

- Implementation tasks and change requests
- Requirements and acceptance criteria
- Applicable standards from `standards/` (if present)

## Outputs

- Working software, scripts, or technical deliverables
- Build and test results
- Updates to implementation workflow state

## Definition of Done

A production task is Done when ALL of the following are true:

- [ ] Deliverable implements the stated requirement or task in full
- [ ] Code passes lint and existing tests (where a toolchain exists)
- [ ] New behaviour is covered by a test or a documented manual check
- [ ] Assumptions and known limitations recorded with the deliverable
- [ ] Workflow state updated and work committed to version control

## Escalate When

- Requirements conflict or acceptance criteria are ambiguous
- A dependency (library, service, credential) is missing or blocked
- The change would modify another workspace's files
- A test failure cannot be explained or reproduced
