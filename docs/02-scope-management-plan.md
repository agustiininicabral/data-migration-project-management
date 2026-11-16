# Scope Management Plan

**Status:** Proposed baseline for a portfolio case study

## 1. Scope statement

The initiative coordinates three educational data-migration workstreams from synthetic Excel inputs into MySQL 8.0. It includes technical delivery evidence and the project controls needed to plan, track, and close the initiative.

## 2. Product scope by workstream

### A. Users migration
- Read a synthetic user workbook.
- Normalize and validate user fields.
- Apply a documented duplicate-email policy.
- Load accepted records into a MySQL schema.
- Verify persisted counts and data-quality constraints.

Repository: https://github.com/agustiininicabral/excel-to-sql-users-migration

### B. Roles and permissions migration
- Read a synthetic multi-sheet authorization workbook.
- Normalize users, roles, permissions, and assignment relationships.
- Enforce primary-key and foreign-key integrity.
- Load entities in dependency order.
- Verify referential integrity and audit queries.

Repository: https://github.com/agustiininicabral/excel-to-sql-roles-permissions

### C. Activity history migration
- Read synthetic activity events.
- Normalize event fields and timestamps.
- Validate actor references, event types, IP addresses, and JSON payloads.
- Preserve append-oriented event behavior.
- Verify stored history and audit integrity.

Repository: https://github.com/agustiininicabral/excel-to-sql-activity-history

## 3. Acceptance criteria

A workstream is accepted for this educational case when:
1. The README explains purpose, limitations, setup, and execution.
2. Synthetic input data can be generated or reproduced.
3. Validation rules and rejection behavior are documented.
4. Automated tests pass.
5. CI runs the migration against MySQL 8.0.
6. Persisted records and key integrity constraints are checked.
7. SQL schema and validation/audit queries are included.
8. Architecture and quality documentation are available.
9. No secrets or real personal data are committed.

Passing these criteria does **not** mean the migration is production-ready.

## 4. Scope verification

Verification is evidence-based:
- Inspect repository files and instructions.
- Run tests and dry-run validation.
- Execute the database integration workflow.
- Review workflow logs and generated artifacts.
- Check README claims against actual schema, code, and reports.
- Record gaps instead of silently treating them as complete.

## 5. Change control

Any proposed addition must state:
- The requirement and business reason.
- Which workstream is affected.
- Expected benefit and acceptance criteria.
- Impact on effort, schedule, quality, and risk.
- Whether it is mandatory for the current case or deferred.

The project owner records the decision in the change log. Out-of-scope production controls remain recommendations unless the case is explicitly expanded.

## 6. Exclusions and scope guardrails

No real data, customer deployment, live identity integration, formal security certification, or production SLA is included. Requests for these items require a new scope decision, specialist review, and appropriate authorization.
