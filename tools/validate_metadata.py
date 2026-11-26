#!/usr/bin/env python3
"""Validates YAML frontmatter in all knowledge documents against schemas/scenario.schema.json."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "schemas" / "scenario.schema.json"

ALLOWED_SCENARIO_TYPES = {"business_process", "enterprise_structure", "master_data", "configuration", "ai_use_case"}
ALLOWED_STATUS = {"draft", "in-review", "reviewed", "deprecated"}
ALLOWED_DIFFICULTY = {"beginner", "intermediate", "advanced"}
ALLOWED_DEPLOYMENTS = {"on-premise", "private-cloud", "public-cloud", "btp"}
ID_PATTERN = re.compile(r"^[A-Z]+-[A-Z0-9]+-[A-Z0-9]+-[0-9]{3}$")


def parse_simple_yaml(yaml_text: str) -> dict:
    """Zero-dependency YAML frontmatter parser supporting scalars, nulls, inline lists, and block lists."""
    data = {}
    current_key = None
    for raw_line in yaml_text.splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if re.match(r"^\s*-\s+", line) and current_key is not None:
            val = re.sub(r"^\s*-\s+", "", line).strip().strip('"').strip("'")
            if isinstance(data[current_key], list):
                data[current_key].append(val)
            continue
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip()
            current_key = key
            if val == "" or val == "[]":
                data[key] = []
            elif val.lower() == "null":
                data[key] = None
            elif val.startswith("[") and val.endswith("]"):
                inner = val[1:-1].strip()
                data[key] = [x.strip().strip('"').strip("'") for x in inner.split(",") if x.strip()] if inner else []
            else:
                data[key] = val.strip('"').strip("'")
    return data


def extract_frontmatter(md_path: Path):
    text = md_path.read_text(encoding="utf-8").replace("\r\n", "\n")
    if not text.startswith("---\n"):
        return None
    parts = text.split("\n---\n", 1)
    if len(parts) < 2:
        return None
    return parse_simple_yaml(parts[0][4:])


def validate_doc(md_path: Path, schema: dict) -> list:
    errors = []
    meta = extract_frontmatter(md_path)
    if meta is None:
        return []

    for req in schema.get("required", []):
        if req not in meta or meta[req] in (None, "", []):
            errors.append(f"{md_path.relative_to(ROOT)}: Missing required field '{req}'")

    doc_id = meta.get("id", "")
    if doc_id and not ID_PATTERN.match(str(doc_id)):
        errors.append(f"{md_path.relative_to(ROOT)}: Invalid id format '{doc_id}'")

    if meta.get("scenario_type") not in ALLOWED_SCENARIO_TYPES:
        errors.append(f"{md_path.relative_to(ROOT)}: Invalid scenario_type '{meta.get('scenario_type')}'")

    if meta.get("status") not in ALLOWED_STATUS:
        errors.append(f"{md_path.relative_to(ROOT)}: Invalid status '{meta.get('status')}'")

    if meta.get("difficulty") not in ALLOWED_DIFFICULTY:
        errors.append(f"{md_path.relative_to(ROOT)}: Invalid difficulty '{meta.get('difficulty')}'")

    for dep in meta.get("deployment", []):
        if dep not in ALLOWED_DEPLOYMENTS:
            errors.append(f"{md_path.relative_to(ROOT)}: Invalid deployment '{dep}'")

    if meta.get("status") == "reviewed" and not meta.get("last_verified"):
        errors.append(f"{md_path.relative_to(ROOT)}: 'reviewed' document must set 'last_verified'")

    return errors


def main() -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    all_errors = []
    validated_count = 0

    for md_path in sorted(ROOT.rglob("*.md")):
        if any(part in {".git", "templates", "tests"} for part in md_path.parts):
            continue
        meta = extract_frontmatter(md_path)
        if meta is not None:
            validated_count += 1
            all_errors.extend(validate_doc(md_path, schema))

    if all_errors:
        print("METADATA VALIDATION FAILED:")
        for err in all_errors:
            print(f"  - {err}")
        return 1

    print(f"Metadata validation passed ({validated_count} structured documents verified).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
