# Data Migration Project Management

[![Docs validation](https://github.com/agustiininicabral/data-migration-project-management/actions/workflows/docs-validation.yml/badge.svg)](https://github.com/agustiininicabral/data-migration-project-management/actions/workflows/docs-validation.yml)
[![Users migration CI](https://github.com/agustiininicabral/excel-to-sql-users-migration/actions/workflows/ci.yml/badge.svg)](https://github.com/agustiininicabral/excel-to-sql-users-migration/actions/workflows/ci.yml)
[![Roles & permissions CI](https://github.com/agustiininicabral/excel-to-sql-roles-permissions/actions/workflows/ci.yml/badge.svg)](https://github.com/agustiininicabral/excel-to-sql-roles-permissions/actions/workflows/ci.yml)
[![Activity history CI](https://github.com/agustiininicabral/excel-to-sql-activity-history/actions/workflows/ci.yml/badge.svg)](https://github.com/agustiininicabral/excel-to-sql-activity-history/actions/workflows/ci.yml)

An individual project-management portfolio case study coordinating three related Excel-to-MySQL migration workstreams: user data, roles and permissions, and activity history. The case demonstrates planning, governance artifacts, evidence traceability, risk controls and a live Jira/Confluence workspace.

> **Transparency:** This is an individual educational portfolio case study, not paid client work or evidence of employment as a Project Manager. The technical repositories and their automated integration checks are real. Planning artifacts not captured during implementation are reconstructed planning models, not historical facts. No production deployment, client approval, real-data processing, actual budget or multi-person team is claimed.

## Executive summary

| Workstream | Purpose | Technical evidence |
|---|---|---|
| [Users migration](https://github.com/agustiininicabral/excel-to-sql-users-migration) | Clean, validate, deduplicate and load synthetic user records | MySQL 8.0 CI integration; 32 sample records, 26 accepted, 6 rejected |
| [Roles & permissions](https://github.com/agustiininicabral/excel-to-sql-roles-permissions) | Normalize a multi-sheet authorization workbook and enforce relational integrity | MySQL 8.0 CI and FK checks; 58 sample records, 52 accepted, 6 rejected |
| [Activity history](https://github.com/agustiininicabral/excel-to-sql-activity-history) | Normalize historical events and load auditable activity records | MySQL 8.0 CI integration; 33 sample records, 26 accepted, 7 rejected |

The technical repositories document reproducible pipelines, synthetic workbooks, SQL schemas and validation queries, automated tests, architecture diagrams, quality summaries and GitHub Actions workflows. The PM case uses these repositories as delivery evidence; it does not imply deployment for a real organization.

## Project lifecycle and artifacts

| Phase | Artifacts |
|---|---|
| Initiation | [Project charter](docs/01-project-charter.md), [stakeholder register](docs/06-stakeholder-register.csv), assumptions and constraints |
| Planning | [Scope baseline](docs/02-scope-management-plan.md), [WBS](docs/03-work-breakdown-structure.csv), [schedule](docs/04-schedule-and-milestones.csv), [RACI](docs/05-raci-matrix.csv), [risk register](docs/07-risk-register.csv), [communications plan](docs/08-communications-plan.md) |
| Delivery model | [Product backlog](docs/09-product-backlog.csv), [Agile delivery plan](docs/10-agile-delivery-plan.md) |
| Monitoring & control | [Status report](docs/11-project-status-report.md), [KPI definitions](docs/12-performance-measures.md), [change control](docs/13-change-control.md) |
| Closure | [Closure report](docs/14-project-closure-report.md), lessons learned and follow-up recommendations |
| Live operations | [Jira implementation guide](docs/18-jira-implementation-guide.md), [Confluence workspace guide](docs/19-confluence-space-blueprint.md), [live tooling review](docs/20-live-tooling-review.md) |

See the [delivery map](docs/17-delivery-map.md) for the workstream dependency diagram, quality gates and control loop.

## Live project workspace

- Jira Software project [DMMP](https://agustinkbral2013.atlassian.net/jira/software/projects/DMMP/boards) is a company-managed Scrum project.
- The live backlog contains **3 epics and 9 child tasks**, with hierarchy verified in Jira. Five tasks are complete with documented acceptance evidence; four remain open.
- Confluence space [DMPC](https://agustinkbral2013.atlassian.net/wiki/spaces/DMPC) contains the project hub, eight governance pages and three technical evidence pages.
- The current Jira board has three columns: **Por hacer**, **En curso** and **Listo**. The project currently exposes only those three statuses. Review/Blocked statuses and quick filters are desired controls, not configured functionality; the available integration does not expose supported write operations for those settings.
- No sprint has been started. No issue has been marked complete merely to imply historical execution.

The [Jira backlog CSV](jira/jira-import-backlog.csv) is aligned with the live three-epic/nine-task hierarchy.

## Delivery approach

A **hybrid, lightweight approach** is modeled:
- Predictive controls for scope, deliverables, dependencies, milestones, risks, acceptance criteria and closure.
- Iterative work packages for independent technical delivery and review.
- Quality gates before a workstream is considered complete: automated tests, a real MySQL 8.0 integration run in CI, data-integrity checks, documentation and a reproducible execution path.

The schedule is expressed as estimated relative weeks, not fabricated calendar dates. No historical sprint velocity, labor cost, budget, stakeholder approval or meeting attendance is claimed.

## Current evidence and known gaps

**Technical evidence:** all three repositories are public and document implementation plus GitHub Actions validation workflows configured with MySQL 8.0. Review the repository Actions tabs for the latest run and artifacts.

**Project tooling:** Jira DMMP and Confluence DMPC are live. The backlog hierarchy and board configuration were inspected directly. The current state and limitations are recorded in [the live tooling review](docs/20-live-tooling-review.md).

**Not evidenced as historical project records:** approved business case, sponsor authorization, real end-user sign-off, actual expenditure, original estimates versus actuals, formal meeting minutes or multi-person team performance. These remain assumptions, proposed controls or future prospective records.

## How to review this portfolio case

1. Read the [charter](docs/01-project-charter.md) for the problem, objectives, scope and constraints.
2. Follow the [WBS](docs/03-work-breakdown-structure.csv) and [relative schedule](docs/04-schedule-and-milestones.csv) to see deliverable decomposition and sequencing.
3. Review the [RACI](docs/05-raci-matrix.csv), [stakeholders](docs/06-stakeholder-register.csv) and [risk register](docs/07-risk-register.csv).
4. Inspect the [live Jira backlog](https://agustinkbral2013.atlassian.net/jira/software/projects/DMMP/boards) and the [Confluence project hub](https://agustinkbral2013.atlassian.net/wiki/spaces/DMPC/pages/229377).
5. Compare the status and closure reports with the technical repositories to distinguish proven evidence from estimates and limitations.

## Repository structure

```text
docs/
  01-project-charter.md
  02-scope-management-plan.md
  03-work-breakdown-structure.csv
  04-schedule-and-milestones.csv
  05-raci-matrix.csv
  06-stakeholder-register.csv
  07-risk-register.csv
  08-communications-plan.md
  09-product-backlog.csv
  10-agile-delivery-plan.md
  11-project-status-report.md
  12-performance-measures.md
  13-change-control.md
  14-project-closure-report.md
  15-assumptions-and-limitations.md
  16-references.md
  17-delivery-map.md
  18-jira-implementation-guide.md
  19-confluence-space-blueprint.md
  20-live-tooling-review.md
jira/
  jira-import-backlog.csv
scripts/
  validate_project_docs.py
.github/workflows/
  docs-validation.yml
```

## Professional framing

Suggested CV/LinkedIn wording after you have reviewed and can explain the artifacts:

> Developed an individual project-management case study coordinating three Excel-to-MySQL migration workstreams; produced scope, WBS, schedule, RACI, risk, stakeholder, backlog, quality, status and closure artifacts, and linked project controls to automated MySQL integration evidence using Jira and Confluence.

Do not describe this as professional Project Manager employment, a client implementation, a production deployment or team leadership. Its value is demonstrating structured project-management thinking supported by tangible technical deliverables and a live tracking workspace.
