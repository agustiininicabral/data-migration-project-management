# Data Migration Project Management

[![Docs validation](https://github.com/agustiininicabral/data-migration-project-management/actions/workflows/docs-validation.yml/badge.svg)](https://github.com/agustiininicabral/data-migration-project-management/actions/workflows/docs-validation.yml)
[![Users migration CI](https://github.com/agustiininicabral/excel-to-sql-users-migration/actions/workflows/ci.yml/badge.svg)](https://github.com/agustiininicabral/excel-to-sql-users-migration/actions/workflows/ci.yml)
[![Roles & permissions CI](https://github.com/agustiininicabral/excel-to-sql-roles-permissions/actions/workflows/ci.yml/badge.svg)](https://github.com/agustiininicabral/excel-to-sql-roles-permissions/actions/workflows/ci.yml)
[![Activity history CI](https://github.com/agustiininicabral/excel-to-sql-activity-history/actions/workflows/ci.yml/badge.svg)](https://github.com/agustiininicabral/excel-to-sql-activity-history/actions/workflows/ci.yml)

A portfolio case study showing how a small, self-directed technology initiative can be framed, planned, monitored, and closed using practical project-management artifacts. The case coordinates three related Excel-to-MySQL migration workstreams: user data, roles and permissions, and activity history.

> **Transparency:** This is an individual educational portfolio case study, not paid client work or evidence of employment as a Project Manager. The technical repositories and their automated integration checks are real. Planning artifacts that were not captured during implementation (for example, original meeting records, approved budgets, actual sprint velocity, or stakeholder sign-offs) are explicitly presented as reconstructed planning models or simulations—not historical facts.

## Executive summary

| Workstream | Purpose | Technical evidence |
|---|---|---|
| [Users migration](https://github.com/agustiininicabral/excel-to-sql-users-migration) | Clean, validate, deduplicate and load synthetic user records | CI workflow with MySQL 8.0 integration; README reports 32 source records, 26 accepted and 6 rejected |
| [Roles & permissions](https://github.com/agustiininicabral/excel-to-sql-roles-permissions) | Normalize a multi-sheet authorization workbook and enforce relational integrity | CI workflow with MySQL 8.0 integration and foreign-key checks; README reports 58 records, 52 accepted and 6 rejected |
| [Activity history](https://github.com/agustiininicabral/excel-to-sql-activity-history) | Normalize historical events and load auditable activity records | CI workflow with MySQL 8.0 integration; README reports 33 records, 26 accepted and 7 rejected |

The three README files document reproducible pipelines, synthetic source workbooks, SQL schemas and validation queries, automated tests, architecture diagrams, quality summaries, and CI workflows. The project-management case uses those repositories as delivery evidence; it does not imply that the three pipelines were deployed for a real organization.

## Project lifecycle and deliverables

| Phase | Key artifacts |
|---|---|
| Initiation | [Project charter](docs/01-project-charter.md), [stakeholder register](docs/06-stakeholder-register.csv), assumptions and constraints |
| Planning | [Scope baseline](docs/02-scope-management-plan.md), [WBS](docs/03-work-breakdown-structure.csv), [schedule](docs/04-schedule-and-milestones.csv), [RACI](docs/05-raci-matrix.csv), [risk register](docs/07-risk-register.csv), [communications plan](docs/08-communications-plan.md) |
| Execution model | [Product backlog](docs/09-product-backlog.csv), [sprint plan](docs/10-agile-delivery-plan.md), technical workstream links |
| Monitoring & control | [Status report](docs/11-project-status-report.md), [KPI definitions](docs/12-performance-measures.md), [change control](docs/13-change-control.md) |
| Closure | [Closure report](docs/14-project-closure-report.md), lessons learned and follow-up recommendations |

See the [delivery map](docs/17-delivery-map.md) for the workstream dependency diagram, quality gates, and control loop.\n\nThe next operational phase is prepared in the [Jira implementation guide](docs/18-jira-implementation-guide.md), [Confluence workspace blueprint](docs/19-confluence-space-blueprint.md), and [Jira CSV import file](jira/jira-import-backlog.csv). These are setup assets, not evidence that an Atlassian workspace has already been created.

## Delivery approach

A **hybrid, lightweight approach** is modeled:

- Predictive controls for scope, deliverables, dependencies, milestones, risks, acceptance criteria, and closure.
- Iterative delivery for the three technical workstreams, with backlog-based prioritization and review points.
- Quality gates before a workstream is considered complete: automated tests, a real MySQL 8.0 integration run in CI, data-integrity checks, documentation, and a reproducible execution path.

The schedule is expressed as estimated relative weeks, not fabricated calendar dates. No historical sprint velocity, labor cost, budget, stakeholder approval, or meeting attendance is claimed.

## Current evidence and known gaps

**Verified technical evidence:** the three repositories are public; each has a documented implementation and GitHub Actions validation workflow. The latest recorded runs at the time this case study was assembled completed successfully, including MySQL 8.0 integration checks. See each repository's Actions tab for current status.

**Not evidenced as historical project records:** approved business case, sponsor authorization, real end-user sign-off, actual expenditure, original estimates versus actuals, formal meeting minutes, or multi-person team performance. These remain assumptions, proposed controls, or simulation exercises in this case study.

## How to review this portfolio case

1. Read the [charter](docs/01-project-charter.md) to understand the problem, objectives, scope, and constraints.
2. Follow the [WBS](docs/03-work-breakdown-structure.csv) and [relative schedule](docs/04-schedule-and-milestones.csv) to see how deliverables are decomposed and sequenced.
3. Review the [RACI](docs/05-raci-matrix.csv), [stakeholders](docs/06-stakeholder-register.csv), and [risk register](docs/07-risk-register.csv) for governance and control.
4. Inspect the backlog and delivery plan, then compare the planned controls with the technical evidence in the three linked repositories.
5. Finish with the status and closure reports to see what is proven, what is estimated, and what would be required before a real production rollout.

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
scripts/
  validate_project_docs.py
.github/workflows/
  docs-validation.yml
```

## Professional framing

Suggested CV/LinkedIn wording after you have reviewed and can explain the artifacts:

> Developed an individual project-management case study coordinating three Excel-to-MySQL migration workstreams; produced scope, WBS, schedule, RACI, risk, stakeholder, backlog, quality, status, and closure artifacts, linking project controls to automated MySQL integration evidence.

Do not describe this as professional Project Manager employment, a client implementation, a production deployment, or team leadership. The value is demonstrating structured project-management thinking supported by tangible technical deliverables.
