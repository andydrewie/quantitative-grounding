# Quantitative Grounding

**QG-01** is a portable, model-agnostic behavioral skill that adds the minimum sufficient quantitative structure needed to understand scale, comparison, likelihood, economics, uncertainty, and decision relevance without numerical theater or false precision.

> Quantify when numbers reveal reality. Do not quantify when numbers merely imitate certainty.

## Why this exists

AI answers can be qualitatively correct yet quantitatively ungrounded. They may describe something as large, likely, expensive, dominant, fast-growing, or important without establishing magnitude, baseline, time horizon, uncertainty, or economic significance.

QG-01 turns the recurring question **"compared with what?"** into an explicit reasoning protocol.

## Quick start

### System or developer prompt

Copy the contents of [`SYSTEM_PROMPT.txt`](SYSTEM_PROMPT.txt) into the persistent instruction layer of your model or agent.

### Agent skill

Provide [`SKILL.md`](SKILL.md) to the agent as a behavioral skill and activate it with:

```text
Activate QG-01 by default for substantive analytical questions.
```

For a single request:

```text
Run QG-01 on this question.
```

Depth modes:

```text
QG-01/Lite
QG-01/Standard
QG-01/Deep
```

### Codex plugin

Install the Codex Skills marketplace, then install this immutable, validated package:

```bash
codex plugin marketplace add https://github.com/andydrewie/codex-skills
codex plugin add quantitative-grounding@andydrewie-codex-skills
```

The root `plugin.json` follows Agent Plugins 1.0. The generated `.codex-plugin/plugin.json` keeps Codex 0.145 compatible while the root manifest is used by Codex 0.146 and newer.

## Governing rule

A number should be included only when it is:

1. **Relevant**: it materially changes interpretation.
2. **Decision-useful**: it improves comparison, prioritization, forecasting, or action.
3. **Epistemically defensible**: it comes from reliable evidence, transparent calculation, or clearly stated assumptions.

When reliable quantification is unavailable, remaining qualitative is the correct behavior.

## Repository map

| File | Purpose |
|---|---|
| [`SKILL.md`](SKILL.md) | Normative behavioral specification and source of truth |
| [`agents/openai.yaml`](agents/openai.yaml) | Codex UI metadata and default invocation prompt |
| [`plugin.json`](plugin.json) | Portable Agent Plugins 1.0 manifest |
| [`.codex-plugin/plugin.json`](.codex-plugin/plugin.json) | Generated Codex 0.145 compatibility manifest |
| [`skills/quantitative-grounding/`](skills/quantitative-grounding/) | Generated fixed-location plugin skill mirror |
| [`SYSTEM_PROMPT.txt`](SYSTEM_PROMPT.txt) | Compact deployment prompt |
| [`AGENTS.md`](AGENTS.md) | Agent-facing integration and precedence rules |
| [`skill.json`](skill.json) | Machine-readable manifest |
| [`EVALS.md`](EVALS.md) | Behavioral tests and pass/fail criteria |
| [`schemas/quantitative-frame.schema.json`](schemas/quantitative-frame.schema.json) | Optional structured-output schema |
| [`examples/`](examples/) | Human and machine-readable usage examples |
| [`scripts/validate.py`](scripts/validate.py) | Dependency-free repository validator |
| [`CANONICAL_SUMMARY.md`](CANONICAL_SUMMARY.md) | Human-readable formalization |
| [`CHANGELOG.md`](CHANGELOG.md) | Version history |

If files conflict, [`SKILL.md`](SKILL.md) controls.

## Agent integration contract

An agent implementing QG-01 should:

- answer the actual question first;
- add one to five high-value quantitative anchors when applicable;
- state the baseline, denominator, period, or reference class when material;
- distinguish fact, reported data, calculation, estimate, scenario, and speculation when provenance matters;
- distinguish event probability from confidence in the estimate;
- prefer ranges and scenarios when inputs do not justify a point estimate;
- omit quantitative framing when it would create false precision.

See [`AGENTS.md`](AGENTS.md) for the complete agent-facing contract.

## Validation

Run locally:

```bash
python scripts/validate.py
```

Check Codex skill-structure compatibility with the installed official validator:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/quantitative-grounding
```

The GitHub Actions workflow runs the same validation on every push and pull request.

## Version

Canonical skill version: **1.0.3**

This packaging-only release adds portable Agent Plugins discovery and the transitional Codex compatibility bridge without changing QG-01 behavior.

## Author

Created by **Andrew Fai** ([@andydrewie](https://github.com/andydrewie)) through iterative human-AI specification design.

## License

MIT. See [`LICENSE`](LICENSE).
