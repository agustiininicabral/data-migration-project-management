# Confluence Workspace Guide

**Live space:** [Data Migration PM Case Study (DMPC)](https://agustinkbral2013.atlassian.net/wiki/spaces/DMPC)  
**Home page:** [Data Migration Program — Project Hub](https://agustinkbral2013.atlassian.net/wiki/spaces/DMPC/pages/229377)  
**State reviewed:** 2026-11-16

## 1. Verified space and page tree

The Confluence space exists and is connected from the Jira setup flow. The page tree contains:

- Project Hub.
- 01 — Project Charter and Scope.
- 02 — Work Breakdown and Schedule.
- 03 — Backlog and Agile Delivery.
- 04 — Risks, Issues, Assumptions and Dependencies.
- 05 — Decisions and Change Log.
- 06 — Status Reports and KPIs.
- 07 — Technical Workstream Evidence.
  - Users Migration.
  - Roles and Permissions Migration.
  - Activity History Migration.
- 08 — Closure and Lessons Learned.

A separate page titled **Data Migration PM Case Study Home** is also present in the space. Its origin has not been established; do not treat it as part of the authored page tree or modify it without review.

## 2. Current content responsibilities

| Page | Purpose |
|---|---|
| Project Hub | Case overview, links to repositories, Jira and governance documentation |
| 01 — Charter and Scope | Objectives, scope, exclusions, assumptions and constraints |
| 02 — Work Breakdown and Schedule | WBS, dependencies and relative estimates |
| 03 — Backlog and Agile Delivery | Live Jira hierarchy, workflow limitations, DoR/DoD and sprint rules |
| 04 — Risks and Dependencies | Risks, assumptions, mitigation and production gaps |
| 05 — Decisions and Change Log | Actual decisions and prospective change-control records |
| 06 — Status Reports and KPIs | Dated snapshots and metric definitions |
| 07 — Technical Workstream Evidence | Summary of the three implementation repositories |
| Child evidence pages | Workstream rules, sample outcomes, CI verification and limitations |
| 08 — Closure and Lessons Learned | Educational-scope outcome and production-adaptation checklist |

## 3. Jira integration

The live Jira project is [DMMP](https://agustinkbral2013.atlassian.net/jira/software/projects/DMMP/boards). Its backlog contains three epics and nine open child tasks. No sprint has been started.

The Jira board currently has three columns: Por hacer, En curso and Listo. Review and Blocked are planning targets only; the available connector does not expose supported board/workflow write operations. Quick filters are not yet configured.

## 4. Evidence page standard

Each technical child page should contain:
- Purpose and scope.
- Synthetic source-data description.
- Validation rules and sample counts.
- Schema and transformation overview.
- Repository and GitHub Actions links.
- What the evidence demonstrates and does not demonstrate.
- Review date and related Jira issue.
- Known limitations and production gaps.

## 5. Prospective records

Create a dated status note after a meaningful review. Record only work that actually occurred. For decisions, capture the actual date, context, options, rationale, impact and related Jira issue. For retrospectives, record observations after a real working cycle and define one measurable improvement action.

## 6. Publication and integrity rules

- Do not store access tokens, passwords, personal source data or secrets.
- Do not present hypothetical stakeholders as real participants.
- Do not represent the reconstructed PM baseline as contemporaneous records.
- Do not invent approvals, meetings, budgets, actual effort or sprint velocity.
- Link to repository evidence rather than duplicating large technical files.
