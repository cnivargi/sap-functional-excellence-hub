#!/usr/bin/env python3
"""Generates a machine-readable JSON catalog of all structured SAP scenarios."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_metadata import ROOT, extract_frontmatter


def main() -> int:
    catalog = []
    for md_path in sorted(ROOT.rglob("*.md")):
        if any(part in {".git", "templates", "tests"} for part in md_path.parts):
            continue
        meta = extract_frontmatter(md_path)
        if meta and meta.get("id"):
            entry = dict(meta)
            entry["path"] = str(md_path.relative_to(ROOT)).replace("\\", "/")
            catalog.append(entry)

    out_path = ROOT / "11-REFERENCE-LIBRARY" / "catalog.json"
    out_path.write_text(json.dumps({"generated_count": len(catalog), "items": catalog}, indent=2) + "\n", encoding="utf-8")
    print(f"Generated catalog with {len(catalog)} entries -> {out_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
