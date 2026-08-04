# Contributing

Contributions should improve QG-01 without turning it into a demand for numbers everywhere.

## Before opening a pull request

1. Read `SKILL.md` and `AGENTS.md`.
2. Keep the governing rule intact: relevant, decision-useful, and epistemically defensible.
3. Add or update behavioral tests in `EVALS.md` for any normative change.
4. Update `CHANGELOG.md` when behavior or packaging changes.
5. Run `python scripts/validate.py`.

## Contribution categories

Useful contributions include:

- sharper activation and suppression rules;
- domain-specific metric guidance;
- better uncertainty calibration;
- adversarial evaluation cases;
- integrations that preserve model-agnostic behavior;
- portability and machine-readability improvements.

## Design constraints

Do not introduce:

- fabricated or decorative numbers;
- mandatory Quantitative Frames for every answer;
- product-specific assumptions into the normative core;
- examples that conflict with `SKILL.md`;
- unnecessary dependencies for validation.

## Pull request format

Describe:

- the behavior being changed;
- why the change improves decision quality;
- failure modes considered;
- tests added or modified.
