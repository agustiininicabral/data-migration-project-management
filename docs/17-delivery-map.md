# Delivery Map and Dependencies

This diagram shows the proposed governance-to-delivery relationship. It is a model of the case study, not a timestamped historical execution log.

![Technical evidence chain](assets/evidence-chain.svg)

![Project and workstream overview](assets/project-overview.svg)

```mermaid
flowchart TD
    A[Initiation: problem, objectives, assumptions] --> B[Planning baseline: scope, WBS, schedule]
    B --> C[Governance: stakeholders, RACI, risks, communications]
    C --> D[Users migration]
    C --> E[Roles and permissions migration]
    C --> F[Activity history migration]
    D --> G[Integrated quality review]
    E --> G
    F --> G
    G --> H[Status, performance measures, change review]
    H --> I[Closure, lessons learned, follow-up]
```

## Workstream quality gates

| Gate | Required evidence | Decision |
|---|---|---|
| G1 — Requirements | Source assumptions, mappings, scope, acceptance rules | Proceed only when rules are explicit |
| G2 — Build | Transformations, schema, tests, reproducible input | Ready for integration validation |
| G3 — Integration | MySQL 8.0 CI run, persisted counts, integrity checks | Accept for educational scope or return for correction |
| G4 — Documentation | README, limitations, SQL, architecture, quality report | Ready for portfolio review |
| G5 — Closure | Outcomes, unresolved risks, lessons, next steps | Close educational workstream |

## Dependency notes

- The users workstream establishes a baseline for user identity and data validation.
- The roles/permissions workstream depends conceptually on user identity and demonstrates relational assignment integrity.
- The activity-history workstream depends conceptually on actor identity and demonstrates audit-event traceability.
- These are logical dependencies in the modeled program. The technical repositories remain independently executable; the diagram does not imply a required serial execution order.

## Control loop

```mermaid
flowchart LR
    P[Plan] --> W[Execute work package]
    W --> E[Collect test and CI evidence]
    E --> R{Acceptance criteria met?}
    R -- Yes --> U[Update status and risks]
    R -- No --> C[Corrective action]
    C --> W
    U --> P
```

A real project would add dated decisions, approved baseline changes, named accountable stakeholders, and actual progress data to this control loop.
