#!/usr/bin/env python3
"""Dependency-free validation for the QG-01 repository."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "1.0.2"
REQUIRED_FILES = [
    "README.md",
    "SKILL.md",
    "SYSTEM_PROMPT.txt",
    "AGENTS.md",
    "skill.json",
    "EVALS.md",
    "CANONICAL_SUMMARY.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "schemas/quantitative-frame.schema.json",
    "examples/README.md",
    "examples/quantitative-frame.example.json",
]
TEXT_SUFFIXES = {".md", ".txt", ".json", ".py", ".yml", ".yaml", ""}
MOJIBAKE_MARKERS = ("\u00e2\u20ac\u0153", "\u00e2\u20ac", "\u00c3", "\u00c2")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_utf8(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        fail(f"{path.relative_to(ROOT)} is not valid UTF-8: {exc}")


def validate_required_files() -> None:
    missing = [name for name in REQUIRED_FILES if not (ROOT / name).is_file()]
    if missing:
        fail("missing required files: " + ", ".join(missing))


def validate_text_files() -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = read_utf8(path)
        marker = next((m for m in MOJIBAKE_MARKERS if m in text), None)
        if marker:
            fail(f"mojibake marker {marker!r} found in {path.relative_to(ROOT)}")


def validate_version_consistency() -> None:
    skill = read_utf8(ROOT / "SKILL.md")
    manifest = json.loads(read_utf8(ROOT / "skill.json"))
    if manifest.get("version") != VERSION:
        fail("skill.json version does not match validator version")
    if not re.search(rf"^version:\s*{re.escape(VERSION)}\s*$", skill, flags=re.MULTILINE):
        fail("SKILL.md frontmatter version does not match validator version")
    if not re.search(r"^id:\s*QG-01\s*$", skill, flags=re.MULTILINE):
        fail("SKILL.md must declare id: QG-01")


def validate_json() -> None:
    schema = json.loads(read_utf8(ROOT / "schemas/quantitative-frame.schema.json"))
    example = json.loads(read_utf8(ROOT / "examples/quantitative-frame.example.json"))
    if schema.get("type") != "object":
        fail("quantitative frame schema must define an object")
    items = example.get("items")
    if not isinstance(items, list) or not 1 <= len(items) <= 5:
        fail("example Quantitative Frame must contain 1-5 items")


def print_manifest() -> None:
    print("QG-01 repository validation passed")
    for name in REQUIRED_FILES:
        path = ROOT / name
        digest = hashlib.sha256(path.read_bytes()).hexdigest()[:12]
        print(f"  {digest}  {name}")


def main() -> None:
    validate_required_files()
    validate_text_files()
    validate_version_consistency()
    validate_json()
    print_manifest()


if __name__ == "__main__":
    main()
