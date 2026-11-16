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
| CR-004 | Extend the case with Jira and Confluence implementation | Approved and initiated 2026-11-16 | Establish a live operational workspace and prospective tracking after the technical workstreams were documented |

## Prospective operational decisions — 2026-11-16

| Decision ID | Decision | Rationale | Impact / related work |
|---|---|---|---|
| DEC-2026-001 | Retain the three existing Jira statuses and board columns until additional workflow configuration can be performed and verified in native Jira settings. | The connected integration exposes board/status reads but no supported writes for workflow statuses or column mapping. | Review/Blocked remain unconfigured; DMMP-4 and DMMP-5 document the limitation. |
| DEC-2026-002 | Close work items only when acceptance criteria are supported by reviewed evidence; leave quick-filter configuration open. | The backlog hierarchy, evidence pages, issue transition test, status review, decisions and retrospective were verified. Quick filters could not be created through the available integration. | Eight child tasks closed; DMMP-5 remains open. |
| DEC-2026-003 | Use Confluence evidence pages and repository Actions pages as durable evidence entry points without asserting unverified run-specific outcomes. | Run-specific GitHub Actions status was not independently retrievable during this review. | Preserves traceability without overstating CI evidence; applies to DMMP-7 through DMMP-9. |

These are operational decisions for an individual portfolio tooling phase, not client approvals or retroactive records. This log is not a claim of formal organizational change governance.
