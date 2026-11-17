# Portfolio Presentation Guide

This guide is a short, evidence-led walkthrough for presenting the case study in an interview or portfolio review.

## 1. Suggested five-minute walkthrough

| Time | Show | Explain |
|---|---|---|
| 0:00–0:45 | [Project overview](assets/project-overview.svg) | Three related Excel-to-MySQL migration workstreams and the project-management problem being modeled. |
| 0:45–1:45 | The three technical repositories | Python processing, SQL validation, automated tests and MySQL 8.0 CI. |
| 1:45–2:30 | [Evidence chain](assets/evidence-chain.svg) | How source workbooks become validated database records and reviewable CI evidence. |
| 2:30–3:30 | Project artifacts | Charter, scope, WBS, schedule, RACI, stakeholder register, risk register, backlog, status and closure. |
| 3:30–4:30 | [Jira DMMP](https://agustinkbral2013.atlassian.net/jira/software/projects/DMMP/boards) and [Confluence DMPC](https://agustinkbral2013.atlassian.net/wiki/spaces/DMPC) | Live issue hierarchy, evidence traceability, governance pages and current configuration limits. |
| 4:30–5:00 | [Live tooling review](20-live-tooling-review.md) | What is complete, what remains open, and why the case does not claim a completed sprint or production delivery. |

## 2. Recommended explanation

> I built an individual project-management case study around three Excel-to-MySQL migration workstreams. I used predictive controls for scope, deliverables, dependencies and risks, then linked the work packages to technical evidence: Python validation, SQL integrity checks, automated tests and MySQL 8.0 integration in GitHub Actions. I documented the project in Jira and Confluence and kept the distinction between implemented evidence, planning assumptions and work that remains open.

## 3. Evidence worth showing

- Users migration: 32 synthetic records; 26 accepted and 6 rejected.
- Roles and permissions: 58 synthetic records; 52 accepted and 6 rejected.
- Activity history: 33 synthetic records; 26 accepted and 7 rejected.
- GitHub Actions: [latest project documentation validation](https://github.com/agustiininicabral/data-migration-project-management/actions).
- Jira: three epics and nine child tasks; eight child tasks are complete with evidence.
- Confluence: project hub, governance pages and three technical evidence pages.

## 4. Be precise about limitations

Do not claim paid client delivery, production deployment, real personal data, a multi-person team, sponsor approval, actual budget or historical Scrum velocity. The current Jira board has three statuses only. Quick filters remain open under DMMP-5; the saved board filter is not a quick filter. DMMP Sprint 1 is in Future state and has not been started.

## 5. Interview questions to prepare for

1. How did you define acceptance criteria for each migration workstream?
2. How did you handle rejected records and preserve data integrity?
3. Why use MySQL integration tests rather than mocks alone?
4. How did you decide what belonged in the WBS versus the product backlog?
5. How would you handle rollback, reconciliation and data ownership in a real migration?
6. What would you do next to make the Jira workflow operational?

The strongest presentation is a live, concise demonstration of the evidence and your decision-making—not a claim that every planned control has already been exercised in a real organization.
