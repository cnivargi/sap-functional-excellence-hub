#!/usr/bin/env python3
"""Validates that all relative Markdown links resolve to existing files in the repository."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def main() -> int:
    broken = []
    checked = 0

    for md_path in sorted(ROOT.rglob("*.md")):
        if any(part in {".git", "tests"} for part in md_path.parts):
            continue
        text = md_path.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            target = match.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target_clean = target.split("#", 1)[0]
            if not target_clean:
                continue
            checked += 1
            resolved = (md_path.parent / target_clean).resolve()
            if not resolved.exists():
                broken.append(f"{md_path.relative_to(ROOT)} -> broken link '{target}'")

    if broken:
        print("LINK VALIDATION FAILED:")
        for b in broken:
            print(f"  - {b}")
        return 1

    print(f"Link validation passed ({checked} relative links verified).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
