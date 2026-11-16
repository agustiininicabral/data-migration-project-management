# Project Charter — Excel-to-MySQL Migration Program

**Document status:** Portfolio case study / reconstructed planning baseline  
**Version:** 1.0  
**Project owner in this case study:** Individual project author  
**Delivery model:** Hybrid (predictive governance + iterative technical delivery)

## 1. Business need

Small organizations often receive operational data in spreadsheets that must be cleaned, validated, and transferred into a relational database. Poorly controlled migrations can introduce duplicate records, invalid relationships, inconsistent timestamps, missing audit context, and weak traceability.

This case study models a coordinated migration initiative across three related data domains: users, authorization roles and permissions, and activity history. It demonstrates how project controls can be applied to a technical delivery with explicit quality gates.

## 2. Project purpose

Plan and document three reproducible educational migrations from synthetic Excel workbooks to MySQL 8.0, while demonstrating project initiation, scope definition, work decomposition, scheduling, stakeholder analysis, risk management, iterative delivery, monitoring, and closure.

## 3. Measurable objectives and success criteria

| Objective | Success criterion | Evidence |
|---|---|---|
| Deliver three independent migration workstreams | Each workstream has a public repository, documented setup, source workbook generation, SQL schema, tests, and usage instructions | Three linked GitHub repositories |
| Validate database behavior | CI executes against MySQL 8.0 and verifies persisted data and integrity constraints | Successful workflow runs and uploaded reports |
| Make data-quality decisions explicit | Each workstream documents acceptance/rejection rules and limitations | README, quality report, validation queries |
| Establish project-management traceability | Scope, WBS, schedule, RACI, stakeholder, risk, backlog, status, and closure artifacts are available | This repository's `docs/` directory |
| Avoid unsupported claims | Synthetic data, individual authorship, reconstructed planning assumptions, and missing real-world approvals are disclosed | README and limitations register |

## 4. High-level scope

**In scope**
- Three synthetic Excel-to-MySQL migration workstreams.
- User data cleaning, validation, deduplication, and relational loading.
- Roles/permissions normalization and referential integrity.
- Activity-history parsing, timestamp normalization, and audit-oriented loading.
- SQL schemas and validation/audit queries.
- Automated tests and MySQL 8.0 CI integration.
- Documentation, quality summaries, and project-management artifacts.

**Out of scope**
- Production deployment or migration of real customer/employee data.
- Integration with a real organization's identity provider or business applications.
- Security certification, penetration testing, legal/privacy review, or formal compliance attestation.
- High availability, disaster recovery, production backup operations, and service-level commitments.
- Runtime authorization product implementation.
- Claims of a real sponsor, client, multi-person team, or approved organizational budget.

## 5. Major deliverables

1. Users migration repository.
2. Roles and permissions migration repository.
3. Activity history migration repository.
4. Project charter, scope baseline, WBS, and schedule.
5. RACI and stakeholder register.
6. Risk register and communications plan.
7. Product backlog and iterative delivery plan.
8. Status report, performance-measure definitions, and change-control process.
9. Closure report, lessons learned, and limitations.

## 6. Assumptions

- All datasets are synthetic and created for demonstration.
- MySQL 8.0 is the target database for the technical validation.
- Each workstream is independently reproducible from its repository instructions.
- A single individual performs the portfolio work; role assignments in RACI represent responsibilities, not separate people.
- The schedule is a planning estimate expressed in relative weeks, not a recovered historical timeline.

## 7. Constraints

- No real source-system access, customer data, production credentials, or external sponsor.
- No confirmed budget or labor-cost records.
- Portfolio evidence is limited to repository contents, commits, documentation, and CI artifacts that remain accessible.
- GitHub Actions and artifact retention are subject to platform availability and retention policies.

## 8. High-level risks

- Requirements are incomplete because there is no real business sponsor.
- Synthetic datasets do not represent full production complexity.
- Data-quality rules may not match an actual organization's policies.
- CI success may be mistaken for production readiness.
- Relative estimates may be interpreted as actual historical performance unless clearly labeled.

See the [risk register](07-risk-register.csv) for probability, impact, response, and owner role.

## 9. Milestone model

| Milestone | Target |
|---|---|
| M1 — Charter and scope baseline | End of relative week 1 |
| M2 — Users migration workstream | End of relative week 3 |
| M3 — Roles & permissions workstream | End of relative week 5 |
| M4 — Activity history workstream | End of relative week 7 |
| M5 — Integrated review and closure | End of relative week 8 |

These are planning targets for the case study and are not represented as original actual completion dates.

## 10. Authority and approval

This is a self-directed portfolio exercise. The author may define and revise the educational scope and documentation. There is no external sponsor authorization, customer acceptance, or organizational authority to allocate resources. In a real project, this charter would require sponsor review and approval before the project baseline is treated as formally authorized.

## 11. Definition of success

The case is successful when the three technical repositories remain reproducible and their evidence is accurately represented, all project-management artifacts are internally consistent, risks and assumptions are transparent, and a reviewer can trace objectives through planned work to verifiable outputs.
