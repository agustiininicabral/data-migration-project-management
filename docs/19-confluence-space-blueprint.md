# Confluence Workspace Blueprint

**Purpose:** Create a concise, navigable project knowledge base linked to the Jira project.  
**State:** Page structure and draft content prepared; no Confluence space or pages have been created yet.

## 1. Space setup

Suggested space name: **Data Migration PM Case Study**  
Suggested space key: **DMPC** (if available).  
Home page title: **Data Migration Program — Project Hub**

Use a private space initially. The Free plan has limited permission customization; review the current access model before adding collaborators. Never publish real personal data, credentials, or private project records.

## 2. Page tree

Create the following page hierarchy:

```text
Data Migration Program — Project Hub
├── 01 — Project Charter and Scope
├── 02 — Work Breakdown and Schedule
├── 03 — Backlog and Agile Delivery
├── 04 — Risks, Issues, Assumptions and Dependencies
├── 05 — Decisions and Change Log
├── 06 — Status Reports and KPIs
├── 07 — Technical Workstream Evidence
│   ├── Users Migration
│   ├── Roles and Permissions Migration
│   └── Activity History Migration
└── 08 — Closure and Lessons Learned
```

## 3. Home page draft

### Purpose

This space documents an individual educational project-management case study coordinating three synthetic Excel-to-MySQL migration workstreams.

### Project status

- Technical workstreams: implemented in separate public repositories.
- Technical verification: each repository documents automated tests and MySQL 8.0 CI integration.
- Project-management artifacts: reconstructed as a learning case after technical implementation.
- Jira tracking: to be configured; no sprint history is claimed yet.
- Production deployment: not performed.

### Quick links

- [Project repository](https://github.com/agustiininicabral/data-migration-project-management)
- [Users migration](https://github.com/agustiininicabral/excel-to-sql-users-migration)
- [Roles and permissions](https://github.com/agustiininicabral/excel-to-sql-roles-permissions)
- [Activity history](https://github.com/agustiininicabral/excel-to-sql-activity-history)

Add the Jira project link after the project is created. Do not invent a Jira URL.

### Current focus

Configure Jira, import the initial backlog, create this Confluence page tree, and begin prospective tracking of tasks, decisions, blockers, and reviews.

## 4. Page content guidance

### 01 — Project Charter and Scope
Summarize the business need, objectives, scope, exclusions, assumptions, constraints, and success criteria. Link to `docs/01-project-charter.md` and `docs/02-scope-management-plan.md`.

### 02 — Work Breakdown and Schedule
Embed or link the WBS and relative schedule. Explicitly label durations as estimates, not historical actuals. Link to `docs/03-work-breakdown-structure.csv` and `docs/04-schedule-and-milestones.csv`.

### 03 — Backlog and Agile Delivery
Link the Jira backlog and board. Document the workflow, sprint goal, Definition of Ready, Definition of Done, and retrospective actions. Link to `docs/09-product-backlog.csv` and `docs/10-agile-delivery-plan.md`.

### 04 — Risks, Issues, Assumptions and Dependencies
Review top risks, mitigations, current blockers, assumptions, and cross-workstream dependencies. Link to `docs/07-risk-register.csv` and `docs/15-assumptions-and-limitations.md`.

### 05 — Decisions and Change Log
Record decisions prospectively using this format:

| Field | Description |
|---|---|
| Decision ID | DEC-YYYY-NNN |
| Date | Date actually made |
| Context | Problem or trigger |
| Options considered | Real alternatives |
| Decision | Chosen option |
| Rationale | Why it was selected |
| Impact | Scope, schedule, quality, risk |
| Owner role | Responsible role |
| Related Jira issue | Actual issue link |

Do not backfill invented decisions or dates.

### 06 — Status Reports and KPIs
Create a dated status entry after each meaningful review. Report scope, schedule, quality, risk, blockers, decisions, and next steps. Use only collected data. Do not invent CPI, SPI, actual effort, or velocity.

### 07 — Technical Workstream Evidence
Create one child page per technical repository. Each page should include:
- Purpose and scope.
- Source-data description (synthetic).
- Data-quality rules and sample counts.
- Schema and transformation overview.
- Tests and CI run link.
- Known limitations.
- Evidence review date.

### 08 — Closure and Lessons Learned
Use the existing closure report as the starting point. Update only after the Jira and Confluence exercise has been performed. Distinguish the original technical case from the new tooling implementation phase.

## 5. Templates for prospective records

### Weekly status note
- Reporting date:
- Overall status:
- Completed since last review:
- Planned next:
- Blockers:
- Risks / changes:
- Decisions:
- Evidence links:

### Retrospective
- What worked:
- What did not:
- What was learned:
- One improvement to test next sprint:
- Owner role:
- Review date:

### Evidence record
- Evidence ID:
- Date captured:
- Related issue:
- Artifact or URL:
- What it demonstrates:
- What it does not demonstrate:
- Privacy / sensitivity check:

## 6. Publication and integrity rules

- Keep the space private unless intentional public sharing is approved.
- Never store access tokens, passwords, personal source data, or secrets.
- Do not present hypothetical stakeholders as real participants.
- Do not represent the reconstructed PM baseline as contemporaneous records.
- Link to repository evidence rather than duplicating large technical files.
