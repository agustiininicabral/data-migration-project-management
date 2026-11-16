#!/usr/bin/env python3
"""Validate the structure and cross-references of the PM portfolio artifacts."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "docs/01-project-charter.md",
    "docs/02-scope-management-plan.md",
    "docs/03-work-breakdown-structure.csv",
    "docs/04-schedule-and-milestones.csv",
    "docs/05-raci-matrix.csv",
    "docs/06-stakeholder-register.csv",
    "docs/07-risk-register.csv",
    "docs/08-communications-plan.md",
    "docs/09-product-backlog.csv",
    "docs/10-agile-delivery-plan.md",
    "docs/11-project-status-report.md",
    "docs/12-performance-measures.md",
    "docs/13-change-control.md",
    "docs/14-project-closure-report.md",
    "docs/15-assumptions-and-limitations.md",
    "docs/16-references.md",
    "docs/17-delivery-map.md",
    "docs/18-jira-implementation-guide.md",
    "docs/19-confluence-space-blueprint.md",
    "jira/jira-import-backlog.csv",
]

CSV_SCHEMAS = {
    "docs/03-work-breakdown-structure.csv": [
        "WBS ID", "Work package", "Activities", "Deliverable", "Acceptance evidence"
    ],
    "docs/04-schedule-and-milestones.csv": [
        "ID", "Phase", "Work package", "Duration estimate", "Predecessors",
        "Planned relative window", "Milestone", "Notes"
    ],
    "docs/05-raci-matrix.csv": [
        "Deliverable / activity", "Project owner", "Technical implementation",
        "Quality assurance", "Stakeholder / reviewer", "Notes"
    ],
    "docs/06-stakeholder-register.csv": [
        "Stakeholder ID", "Stakeholder archetype", "Interest", "Influence",
        "Information needs", "Engagement approach", "Status / transparency"
    ],
    "docs/07-risk-register.csv": [
        "Risk ID", "Risk description", "Category", "Probability", "Impact",
        "Exposure", "Response strategy", "Mitigation / contingency", "Owner role", "Status"
    ],
    "docs/09-product-backlog.csv": [
        "ID", "Epic", "User story / work item", "Priority", "Acceptance criteria",
        "Status / evidence"
    ],
    "jira/jira-import-backlog.csv": [
        "Work type", "Summary", "Description", "Priority", "Labels", "Work item ID", "Parent"
    ],
}

def fail(message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(1)

def read_csv(relative: str) -> tuple[list[str], list[dict[str, str]]]:
    path = ROOT / relative
    try:
        with path.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames is None:
                fail(f"{relative}: missing header")
            rows = list(reader)
    except (OSError, csv.Error) as exc:
        fail(f"{relative}: cannot parse CSV ({exc})")
    expected = CSV_SCHEMAS[relative]
    if reader.fieldnames != expected:
        fail(f"{relative}: header mismatch; expected {expected}, got {reader.fieldnames}")
    for line_number, row in enumerate(rows, start=2):
        if None in row or any(value is None for value in row.values()):
            fail(f"{relative}:{line_number}: inconsistent column count")
        optional_fields = {"Milestone"} if relative == "docs/04-schedule-and-milestones.csv" else set()
        if relative == "jira/jira-import-backlog.csv":
            optional_fields = {"Parent"} if row.get("Work type") == "Epic" else set()
        for field, value in row.items():
            if field not in optional_fields and not value.strip():
                fail(f"{relative}:{line_number}: blank required field '{field}'")
    return list(reader.fieldnames), rows

def check_unique(rows: list[dict[str, str]], field: str, relative: str) -> set[str]:
    values = [row[field] for row in rows]
    if len(values) != len(set(values)):
        fail(f"{relative}: duplicate values in {field}")
    return set(values)

def validate_markdown_links() -> int:
    checked = 0
    pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for markdown in ROOT.rglob("*.md"):
        content = markdown.read_text(encoding="utf-8")
        for raw_target in pattern.findall(content):
            target = raw_target.strip().split()[0].strip("<>")
            parsed = urlparse(target)
            if parsed.scheme or target.startswith(("#", "mailto:")):
                continue
            path_part = target.split("#", 1)[0]
            if not path_part:
                continue
            local_path = (markdown.parent / path_part).resolve()
            if not local_path.exists():
                fail(f"{markdown.relative_to(ROOT)}: broken local link {target}")
            checked += 1
    return checked

def main() -> None:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            fail(f"required file missing: {relative}")

    loaded = {path: read_csv(path)[1] for path in CSV_SCHEMAS}
    wbs_ids = check_unique(loaded["docs/03-work-breakdown-structure.csv"], "WBS ID",
                           "docs/03-work-breakdown-structure.csv")
    schedule_ids = check_unique(loaded["docs/04-schedule-and-milestones.csv"], "ID",
                                "docs/04-schedule-and-milestones.csv")
    check_unique(loaded["docs/07-risk-register.csv"], "Risk ID",
                 "docs/07-risk-register.csv")
    check_unique(loaded["docs/09-product-backlog.csv"], "ID",
                 "docs/09-product-backlog.csv")

    for row in loaded["docs/04-schedule-and-milestones.csv"]:
        for dependency in row["Predecessors"].split(";"):
            dependency = dependency.strip()
            if dependency and dependency != "None" and dependency not in schedule_ids:
                fail(f"schedule {row['ID']}: unknown predecessor {dependency}")

    jira_rows = loaded["jira/jira-import-backlog.csv"]
    jira_ids = [row["Work item ID"] for row in jira_rows]
    if len(jira_ids) != len(set(jira_ids)):
        fail("Jira import CSV: duplicate Work item ID")
    jira_by_id = {row["Work item ID"]: row for row in jira_rows}
    for row in jira_rows:
        parent = row["Parent"].strip()
        if row["Work type"] == "Epic" and parent:
            fail("Jira import CSV: Epic rows cannot have a parent")
        if row["Work type"] != "Epic":
            if parent not in jira_by_id:
                fail("Jira import CSV: unknown parent")
            if jira_by_id[parent]["Work type"] != "Epic":
                fail("Jira import CSV: parent must be an Epic")

    for row in loaded["docs/05-raci-matrix.csv"]:
        accountable = sum(value.strip() == "A" for key, value in row.items()
                          if key != "Deliverable / activity" and key != "Notes")
        if accountable != 1:
            fail(f"RACI row '{row['Deliverable / activity']}': expected exactly one A")

    link_count = validate_markdown_links()
    print(f"Validated {len(REQUIRED_FILES)} required artifacts.")
    print(f"Validated {sum(len(rows) for rows in loaded.values())} CSV records.")
    print(f"Validated {link_count} local Markdown links.")
    print(f"Validated {len(wbs_ids)} WBS IDs and {len(schedule_ids)} schedule IDs.")
    print("Project documentation quality checks passed.")

if __name__ == "__main__":
    main()
