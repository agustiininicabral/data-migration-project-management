# Performance Measures and KPI Definitions

This document distinguishes technical quality indicators from project-management performance indicators. Only the former currently have recorded evidence in the linked repositories.

## 1. Technical indicators with available sample evidence

| Indicator | Current sample value | Interpretation | Source |
|---|---:|---|---|
| Users accepted rows | 26 / 32 (81.25%) | Rows passing the documented user validation rules | Users migration README / quality report |
| Users rejected rows | 6 / 32 (18.75%) | Rows rejected by the documented rules | Users migration README / quality report |
| Roles & permissions accepted rows | 52 / 58 (89.66%) | Records accepted across the documented workbook processing | Roles & permissions README / quality report |
| Roles & permissions rejected rows | 6 / 58 (10.34%) | Records rejected by validation | Roles & permissions README / quality report |
| Activity history accepted rows | 26 / 33 (78.79%) | Events accepted by the documented validation rules | Activity history README / quality report |
| Activity history rejected rows | 7 / 33 (21.21%) | Events rejected by validation | Activity history README / quality report |
| MySQL integration CI | Successful latest known runs at assembly | Confirms tested integration path, not production readiness | Each repository's GitHub Actions |

Percentages are calculated from the sample counts and rounded to two decimal places. They should not be compared as if the datasets had equivalent business rules or complexity.

## 2. Project-management indicators to collect in a future live exercise

| KPI | Definition | Required data | Why it matters |
|---|---|---|---|
| Milestone adherence | Milestones achieved on or before baseline date / milestones due | Approved baseline and actual dates | Schedule control |
| Schedule variance | Actual duration minus baseline duration | Baseline and actual start/finish | Identify delay |
| Scope change rate | Approved scope changes / baseline scope items | Change log and scope baseline | Detect scope instability |
| Defect escape rate | Defects found after acceptance / total defects | Defect log and test results | Quality effectiveness |
| Risk response completion | Mitigations completed by due date / mitigations due | Risk register with dates | Risk control |
| Effort variance | Actual effort minus estimated effort | Time records and estimates | Estimation improvement |
| Stakeholder acceptance | Accepted deliverables / deliverables submitted | Recorded acceptance decisions | Delivery alignment |

## 3. Metrics deliberately not reported

No CPI, SPI, earned value, actual labor utilization, actual cost variance, or Scrum velocity is calculated. Those measures require reliable baselines and actual time/cost/progress data that this case study does not possess. Fabricating them would make the portfolio less credible.

## 4. Dashboard recommendation

For a real project, maintain a weekly dashboard with:
- Overall status (scope, schedule, cost, quality, risk).
- Milestones planned versus actual.
- Work items by workflow state.
- Open high-severity risks and overdue mitigations.
- Defects by severity and age.
- Accepted/rejected row counts and reconciliation totals.
- Change requests and their impacts.
