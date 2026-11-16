# Agile Delivery Plan

**Approach:** Hybrid. Predictive planning artifacts establish scope, dependencies and quality gates; iterative work packages support independent technical delivery and review.

## Live Jira backlog

The live Jira Software project is [DMMP — Data Migration Project Management](https://agustinkbral2013.atlassian.net/jira/software/projects/DMMP/boards). Its current hierarchy is:

| Epic | Purpose | Child issues |
|---|---|---|
| [DMMP-1](https://agustinkbral2013.atlassian.net/browse/DMMP-1) — Configure Jira project and Scrum board | Operational Jira setup | DMMP-4, DMMP-5, DMMP-6 |
| [DMMP-2](https://agustinkbral2013.atlassian.net/browse/DMMP-2) — Document technical workstream evidence | Link verified technical evidence | DMMP-7, DMMP-8, DMMP-9 |
| [DMMP-3](https://agustinkbral2013.atlassian.net/browse/DMMP-3) — Establish prospective project controls | Record future project activity honestly | DMMP-10, DMMP-11, DMMP-12 |

The board contains nine child tasks, initially created in **Por hacer**. After acceptance reviews on 2026-11-16, eight tasks are in **Listo** (DMMP-4, DMMP-6, DMMP-7, DMMP-8, DMMP-9, DMMP-10, DMMP-11 and DMMP-12) and one remains in **Por hacer** (DMMP-5, quick-filter configuration). Parent relationships were verified through Jira. The three epics above are the live operational backlog; the technical workstreams are evidence already implemented in separate repositories, not additional Jira epics.

## Proposed delivery sequence

| Work package | Goal | Review gate |
|---|---|---|
| Tooling setup | Verify board, issue hierarchy, labels and available workflow | Board configuration and acceptance criteria checked |
| Technical evidence | Link each repository, its CI workflow and sample quality outcome | Evidence is reproducible and limitations are explicit |
| Prospective controls | Record dated status, decisions, blockers and retrospective outcomes as work occurs | Records are contemporaneous and supported |

This is a proposed sequence, not evidence of historical Scrum ceremonies or sprint execution. No sprint has been started.

## Workflow actually available

The DMMP project currently exposes three global statuses for its work types:

`Por hacer → En curso → Listo`

The Scrum board maps these to three columns with the same names. The current Atlassian integration exposes board configuration as read-only; it does not expose a supported operation to add workflow statuses, remap columns or create board quick filters. Therefore **Review** and **Blocked** remain desired controls, not configured statuses. Do not represent them as live functionality.

Until the board can be configured through Jira's native UI or a supported administrative operation:
- Keep the three existing statuses.
- Record blockers in the issue description or a comment, including dependency, resolution role and next review trigger.
- Use the existing labels for workstream and control categorization.
- Do not move an issue to **Listo** until its acceptance criteria and evidence are satisfied.

## Definition of Ready

A work item is ready when:
- The expected outcome and affected workstream are clear.
- Dependencies and data assumptions are identified.
- Acceptance criteria are testable.
- Edge cases are documented.
- Required source material and access are available.

## Definition of Done

A work item is done when:
- All acceptance criteria are satisfied.
- Relevant repository, CI and Confluence links are attached.
- Evidence is reproducible or the limitation is disclosed.
- Documentation is updated.
- Remaining risks are recorded.
- No unsupported historical or production claims are introduced.

## Sprint and retrospective rules

Do not create artificial velocity or claim historical ceremonies. Start a real sprint only when there is a specific goal, a realistic set of tasks, and a genuine work period to track. For this individual case, use small effort bands or hours if useful; story points and velocity are optional learning exercises, not performance metrics.

Retrospective prompts:
1. Which validation rules prevented the most consequential data defects?
2. Which source assumptions were weakest?
3. Did workstream sequencing reduce rework?
4. Were integration checks sufficient to detect schema and loading errors?
5. What must change before any real-data migration?
