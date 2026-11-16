# Change Control

## Purpose

Prevent uncontrolled scope growth and preserve traceability between requested changes, project objectives, acceptance criteria, risks, and delivery estimates.

## Change request template

| Field | Required information |
|---|---|
| Change ID | Unique identifier (CR-###) |
| Requester | Role or stakeholder requesting the change |
| Date | Date submitted |
| Description | What should change and why |
| Business value | Problem solved or benefit expected |
| Affected workstream | Users, roles/permissions, activity history, or project governance |
| Impact | Scope, schedule, cost, quality, security, and dependencies |
| Options | Approve, reject, defer, or request clarification |
| Decision owner | Authorized decision-maker |
| Decision and rationale | Recorded outcome |
| Follow-up | Updated backlog, WBS, schedule, risks, and documentation |

## Decision workflow

1. Log the request before implementation.
2. Clarify the problem and measurable acceptance criteria.
3. Assess technical dependencies and project impacts.
4. Check whether the request violates an explicit exclusion.
5. Decide approve, reject, defer, or request more information.
6. Update the relevant baseline and communicate the decision.
7. Verify the change against acceptance criteria.

## Portfolio case change log

| Change ID | Change | Decision | Rationale |
|---|---|---|---|
| CR-001 | Create a dedicated project-management repository for the three technical workstreams | Approved for this case study | Keeps governance artifacts separate from implementation repositories |
| CR-002 | Use relative schedule estimates instead of invented historical dates | Approved | No contemporaneous schedule records were available |
| CR-003 | Exclude production deployment and real personal data | Approved / retained | No client authorization, source access, or production controls |
| CR-004 | Treat Jira and Confluence implementation as a future extension | Deferred | First establish a coherent, reviewable project-management baseline |

This log records decisions made while preparing the portfolio case. It is not a claim of formal organizational change governance.
