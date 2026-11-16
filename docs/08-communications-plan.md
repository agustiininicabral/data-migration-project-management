# Communications Plan

**Status:** Proposed plan for a simulated project environment. No meetings or stakeholder communications are claimed to have occurred.

| Audience | Information | Trigger / cadence | Channel / format | Owner | Expected outcome |
|---|---|---|---|---|---|
| Project owner | Work progress, blockers, risks, changes | At each work-package review | Status log | Project owner | Decisions and next actions recorded |
| Hypothetical data owner | Source mappings, rejected records, reconciliation exceptions | At requirements and acceptance gates | Mapping review and exception report | Data lead | Business rules validated |
| Hypothetical technical reviewer | Schema, constraints, test and CI evidence | At design and technical completion gates | Repository, SQL, CI report | Technical lead | Design and integrity review |
| Hypothetical security/privacy reviewer | Data classification, access, retention, audit controls | Before any real-data or production scope | Risk review | Project owner | Security/privacy gaps identified |
| Portfolio reviewer / recruiter | Purpose, contribution, evidence, limitations | On portfolio publication | README and linked artifacts | Project owner | Work can be evaluated quickly |

## Escalation model

1. Log the issue with impact, affected workstream, and owner.
2. Classify severity as low, medium, or high.
3. For high-impact data-integrity, privacy, or security issues, stop the affected release path until reviewed.
4. Record the decision, mitigation, and any scope/schedule impact.
5. Update the risk register and status report.

## Communication principles

- Prefer written, traceable decisions.
- Separate confirmed facts from assumptions.
- Never publish personal or confidential data.
- Do not represent hypothetical stakeholder engagement as actual consultation.
