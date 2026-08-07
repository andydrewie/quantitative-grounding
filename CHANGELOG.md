# Changelog

## 2.0.0 - Explicit Codex invocation

- Changed the installed Codex skill from implicit/default activation to explicit `$quantitative-grounding` invocation.
- Added `policy.allow_implicit_invocation: false` to the root and plugin-package Codex metadata.
- Preserved `SYSTEM_PROMPT.txt` as a separate operator-controlled deployment path for agents intentionally configured with persistent QG-01 behavior.
- Updated the normative skill, agent contract, README, canonical summary, examples, and evaluations to distinguish the two deployment modes.
- Updated machine-readable activation metadata and validation so packaging cannot silently restore implicit invocation.
- Bumped the major version because changing when an installed skill runs is an incompatible user-facing activation-contract change.

## 1.0.3 - Agent Plugins packaging

- Added the Agent Plugins 1.0 root manifest and fixed `skills/quantitative-grounding/` discovery layout.
- Added a generated Codex legacy manifest for Codex 0.145 compatibility.
- Preserved the root standalone-skill installation contract for one compatibility release.
- Kept QG-01 behavior unchanged and added validation for generated-mirror parity.
- Normalized `SKILL.md` frontmatter to the current Codex `name` and `description` schema.
- Preserved the QG-01 identifier, version, aliases, and activation behavior in the manifest and skill instructions.
- Added Codex UI metadata in `agents/openai.yaml`.
- Updated repository validation to enforce the compatible frontmatter shape.

## 1.0.2 - Canonical release

- Declared this package the single source of truth.
- Preserved the original QG-01 behavior and structure.
- Fixed `decision relevance-without` to `decision relevance without`.
- Replaced the shorthand `best/top questions` with `superlative requests`.
- Retained ASCII-safe punctuation to reduce mojibake in mobile and plain-text previews.
- Added `CANONICAL_SUMMARY.md` to preserve the original human-readable formalization.

## 1.0.1 - Portability revision

- Replaced smart punctuation with ASCII punctuation.
- Expanded `best/top questions` into a longer superlative example phrase.
- Added package-validation material.

## 1.0.0 - Initial release

- First complete QG-01 skill specification.
- Included the system prompt, deployment guide, and evaluation set.

## Mojibake clarification

The original v1.0.0 file was valid UTF-8. The strange characters shown in one iPhone preview were a decoding or rendering error, not a broken skill. Version 1.0.2 uses ASCII-safe punctuation so the same display issue is less likely across interfaces.
