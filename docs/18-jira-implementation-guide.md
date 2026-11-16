# Jira Implementation Guide

**Purpose:** Turn the portfolio backlog into an actively managed Jira project.  
**State:** Configuration blueprint; no Jira project or board has been created yet.  
**Tooling target:** Jira Cloud Free.

## 1. Project setup

Create a company-managed or team-managed **Scrum** project if Jira Free offers it in the current workspace. Prefer a Scrum template because the case study already contains epics, a product backlog, and an iterative delivery model.

Suggested project name: **Data Migration Project Management**  
Suggested project key: **DMMP** (use another available key if Jira reports a conflict).  
Project description:

> Individual educational project-management case study coordinating three synthetic Excel-to-MySQL migration workstreams. Tracks planning, evidence review, quality gates, risks, documentation, and closure. Not a client implementation or production migration.

Do not add fictitious team members, stakeholders, approvals, or historical dates. Keep the project private to the account unless there is a deliberate reason to share it.

## 2. Issue hierarchy and initial backlog

Use:
- **Epic:** a major delivery or governance outcome.
- **Task:** a concrete piece of work with verifiable acceptance criteria.
- **Bug:** a defect discovered during review or execution.

The import file at [jira-import-backlog.csv](../jira/jira-import-backlog.csv) contains the proposed initial work items. Import it only after the project exists, map the columns carefully, and inspect the preview before confirming. If Jira's importer does not resolve Epic Link references in one pass, import epics first and then child tasks using the generated epic keys.

The backlog is prospective. Existing technical work is recorded as completed evidence in the case study; new Jira tasks cover the current tooling and evidence-management phase. Do not backdate tasks or manufacture completed sprint work.

## 3. Workflow

Recommended workflow:

`To Do → In Progress → Review → Done`

Add **Blocked** as a status or flag if available. A blocked item must include:
- What is blocked.
- The dependency or decision required.
- Who can resolve it (role, not an invented person).
- The next review trigger.

**Done** requires the acceptance criteria to be met and evidence linked in the issue. A code commit alone is not enough.

## 4. Board configuration

- Board type: Scrum.
- Columns: To Do, In Progress, Review, Done.
- Map Blocked to its own column if the template supports it; otherwise use a flag and a clear label.
- Group backlog items by Epic.
- Use labels consistently: `governance`, `tooling`, `documentation`, `quality`, `risk`, `evidence`.
- Useful quick filters: `Blocked`, `label = tooling`, `label = evidence`, `priority = Highest`.

## 5. Sprint operating rules

Do not create artificial velocity or claim historical Scrum ceremonies. Start the first real sprint only after the project and board are configured.

For each sprint:
1. Set one sprint goal.
2. Select only work that can realistically be completed by one contributor.
3. Confirm dependencies and acceptance criteria before starting.
4. Record blockers and scope changes as they happen.
5. Review completed items against evidence.
6. Write a short retrospective with one improvement action.

For this individual portfolio exercise, estimate work in hours or small/medium/large effort bands. Story points and velocity are optional learning exercises, not performance metrics.

## 6. Definition of Ready

An issue is ready when:
- The outcome and reason are clear.
- Acceptance criteria are testable.
- Dependencies are identified.
- The work is small enough to review.
- Required source material or access is available.

## 7. Definition of Done

An issue is done when:
- All acceptance criteria are satisfied.
- Relevant repository or Confluence links are attached.
- Evidence is reproducible or the limitation is disclosed.
- Documentation is updated.
- Remaining risks are recorded.
- No unsupported historical or production claims are introduced.

## 8. Reporting

At the end of each real work session, update:
- Issue status and remaining work.
- Blockers and decisions.
- Risks changed or newly identified.
- Evidence links.
- Next action.

Do not report schedule variance, cost variance, CPI, SPI, or velocity unless an approved baseline and actual data have been collected prospectively.

## 9. First working session

The first session is complete only when:
- Jira project and Scrum board exist.
- Epics and initial tasks are imported.
- Workflow and columns are checked.
- The first sprint goal is selected.
- The Confluence home page links to the Jira project.
- A screenshot or URL evidence record is stored in the repository (do not commit credentials or private data).

## 10. Reference

See [Confluence workspace blueprint](19-confluence-space-blueprint.md) for the documentation structure and page templates.
