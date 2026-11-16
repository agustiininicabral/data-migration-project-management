# Jira Implementation and Operating Guide

**Live project:** [DMMP — Data Migration Project Management](https://agustinkbral2013.atlassian.net/jira/software/projects/DMMP/boards)  
**Board:** DMMP board, Scrum, board ID 2  
**State reviewed:** 2026-11-16

## 1. Verified project setup

The company-managed Jira Software Scrum project exists with key **DMMP**. The project is intended for an individual educational portfolio case study coordinating three synthetic Excel-to-MySQL migration workstreams. It is not a client implementation or production migration.

## 2. Live issue hierarchy

| Parent epic | Child issues |
|---|---|
| DMMP-1 — Configure Jira project and Scrum board | DMMP-4, DMMP-5, DMMP-6 |
| DMMP-2 — Document technical workstream evidence | DMMP-7, DMMP-8, DMMP-9 |
| DMMP-3 — Establish prospective project controls | DMMP-10, DMMP-11, DMMP-12 |

The live hierarchy was checked in Jira. The CSV export at [jira-import-backlog.csv](../jira/jira-import-backlog.csv) preserves the three epics and nine child tasks using Jira's Work item ID and Parent mapping.

## 3. Workflow and board

The project currently exposes these three statuses for its work types:

- **Por hacer** — not started.
- **En curso** — work in progress.
- **Listo** — completed.

The board maps each status to a matching column. The board uses the existing Story Points field for estimation and Jira's configured Rank field for ordering.

The target workflow in the planning model includes Review and Blocked handling, but those are **not configured**. The available Atlassian connector provides read access to board configuration and issue transitions, but no supported write operation for board columns, workflow statuses or quick filters. Do not imply that Review or Blocked columns exist. If a blocker occurs, record its description, dependency, resolution role and next review trigger in the issue until native configuration is available.

## 4. Labels and filters

The nine tasks were created with labels aligned to tooling, evidence, governance, quality and workstream categories. Use labels consistently and avoid adding synonyms without a reason.

Useful quick filters to create through Jira's native board settings, if available:
- Blocked work (once a reliable flag or label convention is in use).
- `labels = tooling`
- `labels = evidence`
- `labels = governance`

Quick filters have not been configured or verified through the current integration.

## 5. Sprint operating rules

No sprint has been started. Start the first real sprint only when there is:
1. One specific sprint goal.
2. A realistic selection of open tasks.
3. Confirmed acceptance criteria and dependencies.
4. A real start and end period that can be reviewed.
5. A plan to capture blockers and decisions as they happen.

Do not create artificial velocity or backdate ceremonies. For this individual portfolio exercise, estimate in hours or small/medium/large effort bands. Story points are optional and are not a performance metric without repeated real sprint data.

## 6. Definition of Ready

- Outcome and reason are clear.
- Acceptance criteria are testable.
- Dependencies and assumptions are identified.
- Work is small enough to review.
- Required source material and access are available.

## 7. Definition of Done

- All acceptance criteria are satisfied.
- Repository, CI and Confluence evidence links are attached.
- Evidence is reproducible or the limitation is disclosed.
- Documentation is updated.
- Remaining risks are recorded.
- No unsupported historical or production claims are introduced.

## 8. Reporting discipline

At the end of each actual work session, update issue status, blockers, decisions, risks, evidence links and next actions. Do not report schedule variance, cost variance, CPI, SPI or velocity unless reliable baseline and actual data have been collected prospectively.

## 9. Related workspace

The [Confluence space DMPC](https://agustinkbral2013.atlassian.net/wiki/spaces/DMPC) contains the project hub, governance pages and technical evidence pages. The live project backlog is not evidence of completed sprints or multi-person delivery.
