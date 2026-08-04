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

The GitHub Actions workflow runs the same validation on every push and pull request.

## Version

Canonical skill version: **1.0.2**

The original UTF-8 files were functionally valid. This release uses ASCII-safe punctuation to reduce mojibake risk in mobile and plain-text previews.

## Author

Created by **Andrew Fai** ([@andydrewie](https://github.com/andydrewie)) through iterative human-AI specification design.

## License

MIT. See [`LICENSE`](LICENSE).
