# Agile Delivery Plan

**Approach:** Hybrid. Predictive planning artifacts establish boundaries and quality gates; iterative work packages allow each migration to be built and verified independently.

## Backlog structure

- **Epic 1 — Project governance:** charter, scope, WBS, schedule, stakeholder and risk controls.
- **Epic 2 — Users migration:** ingest, clean, validate, load, verify, document.
- **Epic 3 — Roles and permissions:** model entities, enforce relationships, load, verify, document.
- **Epic 4 — Activity history:** parse events, normalize timestamps, load, verify, document.
- **Epic 5 — Integrated closure:** consolidate evidence, limitations, lessons, and follow-up work.

## Proposed sprint model

| Sprint | Goal | Planned output | Review gate |
|---|---|---|---|
| Sprint 0 (setup) | Establish project boundaries and delivery controls | Charter, scope, WBS, schedule, risks, stakeholder map | Planning baseline review |
| Sprint 1 | Deliver the user migration | Reproducible user workbook, validation, MySQL load, CI evidence | User acceptance criteria |
| Sprint 2 | Deliver the roles and permissions migration | Multi-sheet processing, normalized schema, FK checks, CI evidence | Referential-integrity review |
| Sprint 3 | Deliver the activity history migration | Timestamp/event validation, MySQL load, audit checks, CI evidence | Audit-integrity review |
| Sprint 4 (close) | Consolidate outcomes and close the case | Integrated status, lessons learned, closure report | Evidence and limitations review |

This is a proposed iteration model for explaining the delivery approach. It is not a claim that formal Scrum ceremonies, sprint commitments, or historical sprint durations were recorded during the original technical work.

## Definition of Ready

A work item is ready when:
- The expected outcome is clear.
- The affected workstream and dependencies are identified.
- Acceptance criteria are testable.
- Data assumptions and edge cases are documented.
- The work can be reviewed independently.

## Definition of Done

A work item is done when:
- Implementation and documentation are complete.
- Automated tests pass.
- Relevant MySQL 8.0 integration checks pass.
- Validation output is reviewed.
- Known limitations are documented.
- Evidence is linked from the repository.

## Suggested Jira workflow

`Backlog → Ready → In Progress → Code Review → Validation → Done`

Use `Blocked` as an explicit state with a reason and owner. Avoid moving work to Done based only on code completion; the acceptance criteria and evidence must also be satisfied.

## Retrospective prompts

1. Which validation rules prevented the most consequential data defects?
2. Which source assumptions were weakest?
3. Did workstream sequencing reduce rework?
4. Were integration checks sufficient to detect schema and loading errors?
5. What must change before any real-data migration?
