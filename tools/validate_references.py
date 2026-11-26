#!/usr/bin/env python3
"""Validates that all cross-referenced scenario IDs in YAML frontmatter exist in the repository."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_metadata import ROOT, extract_frontmatter


def main() -> int:
    known_ids = {}
    doc_metas = []

    for md_path in sorted(ROOT.rglob("*.md")):
        if any(part in {".git", "templates", "tests"} for part in md_path.parts):
            continue
        meta = extract_frontmatter(md_path)
        if meta and meta.get("id"):
            doc_id = meta["id"]
            if doc_id in known_ids:
                print(f"REFERENCE VALIDATION FAILED: Duplicate ID '{doc_id}'")
                return 1
            known_ids[doc_id] = md_path
            doc_metas.append((md_path, meta))

    errors = []
    for md_path, meta in doc_metas:
        for ref_field in ("dependencies", "related_scenarios"):
            for ref_id in meta.get(ref_field, []):
                if ref_id not in known_ids:
                    errors.append(f"{md_path.relative_to(ROOT)}: Unresolved {ref_field} ID '{ref_id}'")

    if errors:
        print("REFERENCE VALIDATION FAILED:")
        for err in errors:
            print(f"  - {err}")
        return 1

    print(f"Reference validation passed ({len(known_ids)} unique IDs indexed, zero broken references).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
