#!/usr/bin/env python3
"""Dependency-free validation for the QG-01 repository."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "1.0.3"
PORTABLE_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
PORTABLE_MANIFEST_FIELDS = {
    "$schema",
    "name",
    "version",
    "description",
    "author",
    "homepage",
    "repository",
    "license",
    "keywords",
    "extensions",
}
REQUIRED_FILES = [
    "SHA256SUMS.txt",
    "README.md",
    "SKILL.md",
    "agents/openai.yaml",
    "skills/quantitative-grounding/SKILL.md",
    "skills/quantitative-grounding/agents/openai.yaml",
    "plugin.json",
    ".codex-plugin/plugin.json",
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


def validate_package_tree() -> None:
    package_root = ROOT.resolve(strict=True)
    for path in ROOT.rglob("*"):
        if ".git" in path.parts:
            continue
        relative = path.relative_to(ROOT)
        if path.is_symlink():
            fail(f"plugin packages must not contain symlinks: {relative}")
        try:
            path.resolve(strict=True).relative_to(package_root)
        except (OSError, ValueError):
            fail(f"package path must resolve within the plugin root: {relative}")


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


def validate_identity_consistency() -> None:
    skill = read_utf8(ROOT / "SKILL.md")
    manifest = json.loads(read_utf8(ROOT / "skill.json"))
    if manifest.get("version") != VERSION:
        fail("skill.json version does not match validator version")
    if manifest.get("id") != "QG-01":
        fail("skill.json must declare id QG-01")

    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", skill, flags=re.DOTALL)
    if not match:
        fail("SKILL.md must begin with YAML frontmatter")
    frontmatter = match.group(1)
    if not re.search(r"^name:\s*quantitative-grounding\s*$", frontmatter, flags=re.MULTILINE):
        fail("SKILL.md frontmatter must declare name: quantitative-grounding")
    if not re.search(r"^description:\s*.+$", frontmatter, flags=re.MULTILINE):
        fail("SKILL.md frontmatter must declare a description")
    for unsupported in ("id", "version", "activation", "aliases"):
        if re.search(rf"^{unsupported}:\s*", frontmatter, flags=re.MULTILINE):
            fail(f"SKILL.md frontmatter must not declare unsupported key: {unsupported}")
    if not re.search(r"^# QG-01 - Quantitative Grounding\s*$", skill, flags=re.MULTILINE):
        fail("SKILL.md must retain the canonical QG-01 heading")

    plugin_skill = ROOT / "skills/quantitative-grounding/SKILL.md"
    if plugin_skill.read_bytes() != (ROOT / "SKILL.md").read_bytes():
        fail("plugin SKILL.md mirror must be byte-identical to root SKILL.md")
    plugin_agents = ROOT / "skills/quantitative-grounding/agents/openai.yaml"
    if plugin_agents.read_bytes() != (ROOT / "agents/openai.yaml").read_bytes():
        fail("plugin openai.yaml mirror must be byte-identical to root agents/openai.yaml")


def validate_plugin_manifests() -> None:
    portable = json.loads(read_utf8(ROOT / "plugin.json"))
    unknown = sorted(set(portable) - PORTABLE_MANIFEST_FIELDS)
    if unknown:
        fail("plugin.json contains unsupported fields: " + ", ".join(unknown))
    if portable.get("$schema") != PORTABLE_SCHEMA:
        fail("plugin.json must target Agent Plugins 1.0.0")
    if portable.get("name") != "quantitative-grounding":
        fail("plugin.json name must be quantitative-grounding")
    if portable.get("version") != VERSION:
        fail("plugin.json version does not match validator version")
    if not isinstance(portable.get("description"), str) or not portable["description"].strip():
        fail("plugin.json must provide a non-empty description")
    if portable.get("license") != "MIT":
        fail("plugin.json must declare the bundled MIT license")
    if not re.fullmatch(r"0|[1-9]\d*\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?", VERSION):
        fail("plugin version must use strict semantic versioning")

    extensions = portable.get("extensions")
    if not isinstance(extensions, dict) or set(extensions) != {"com.openai"}:
        fail("plugin.json must contain only the com.openai extension")
    codex = extensions["com.openai"]
    if not isinstance(codex, dict) or set(codex) != {"interface"}:
        fail("com.openai extension must contain only interface metadata")
    interface = codex["interface"]
    if not isinstance(interface, dict):
        fail("com.openai.interface must be an object")
    for field in (
        "displayName",
        "shortDescription",
        "longDescription",
        "developerName",
        "category",
        "capabilities",
        "defaultPrompt",
    ):
        if field not in interface:
            fail(f"com.openai.interface must contain {field}")

    expected_legacy = {
        key: value
        for key, value in portable.items()
        if key not in {"$schema", "extensions"}
    }
    expected_legacy["skills"] = "./skills/"
    expected_legacy["interface"] = interface
    legacy = json.loads(read_utf8(ROOT / ".codex-plugin/plugin.json"))
    if legacy != expected_legacy:
        fail(".codex-plugin/plugin.json is stale; regenerate it from plugin.json")
    if (ROOT / "mcp.json").exists() or (ROOT / ".mcp.json").exists():
        fail("QG-01 is skills-only and must not ship an empty MCP manifest")


def validate_json() -> None:
    schema = json.loads(read_utf8(ROOT / "schemas/quantitative-frame.schema.json"))
    example = json.loads(read_utf8(ROOT / "examples/quantitative-frame.example.json"))
    if schema.get("type") != "object":
        fail("quantitative frame schema must define an object")
    items = example.get("items")
    if not isinstance(items, list) or not 1 <= len(items) <= 5:
        fail("example Quantitative Frame must contain 1-5 items")


def validate_checksums() -> None:
    checksum_path = ROOT / "SHA256SUMS.txt"
    recorded: dict[str, str] = {}
    for line in read_utf8(checksum_path).splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if not match:
            fail(f"invalid SHA256SUMS.txt line: {line!r}")
        digest, relative = match.groups()
        if relative in recorded:
            fail(f"duplicate checksum entry: {relative}")
        recorded[relative] = digest

    expected_paths = {
        str(path.relative_to(ROOT))
        for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and "releases" not in path.parts
        and path.name != "SHA256SUMS.txt"
    }
    if set(recorded) != expected_paths:
        missing = sorted(expected_paths - set(recorded))
        extra = sorted(set(recorded) - expected_paths)
        fail(f"checksum path mismatch; missing={missing}, extra={extra}")
    for relative, expected_digest in recorded.items():
        actual = hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()
        if actual != expected_digest:
            fail(f"checksum mismatch: {relative}")


def print_manifest() -> None:
    print("QG-01 repository validation passed")
    for name in REQUIRED_FILES:
        path = ROOT / name
        digest = hashlib.sha256(path.read_bytes()).hexdigest()[:12]
        print(f"  {digest}  {name}")


def main() -> None:
    validate_required_files()
    validate_package_tree()
    validate_text_files()
    validate_identity_consistency()
    validate_plugin_manifests()
    validate_json()
    validate_checksums()
    print_manifest()


if __name__ == "__main__":
    main()
