# AGENTS.md

This repository defines **QG-01: Quantitative Grounding**, a model-agnostic behavioral skill.

## Source-of-truth precedence

1. `SKILL.md` is normative.
   `skills/quantitative-grounding/SKILL.md` is its generated plugin-package mirror and must remain byte-identical.
2. `SYSTEM_PROMPT.txt` is the compact deployment form.
3. `skill.json` is the machine-readable manifest.
4. `EVALS.md` defines behavioral validation.
5. Examples are illustrative and must not override `SKILL.md`.

## Agent objective

Add the minimum sufficient quantitative structure needed to understand:

- scale;
- comparison;
- likelihood;
- economics;
- uncertainty;
- decision relevance.

Do not maximize numerical density.

## Activation

**Codex skill installation is explicit-use only.** Do not invoke the installed skill from prompt similarity alone. The user must call `$quantitative-grounding`, for example:

```text
Use $quantitative-grounding to compare these options with relevant baselines and uncertainty.
```

After explicit invocation, apply the full protocol to substantive analytical requests involving rankings, companies, markets, probability, forecasting, economics, technical performance, social prevalence, strategy, resources, capacity, or consequential empirical claims. Use lightly or remain qualitative for creative writing, stylistic rewriting, emotional support, casual conversation, non-empirical philosophy, and early ideation when quantification would not help.

The persistent prompt is a separate, operator-controlled deployment mode. Copying `SYSTEM_PROMPT.txt` into an agent's system or developer instructions intentionally makes QG-01 persistent for that configured agent; it does not authorize implicit invocation of the installed Codex skill.

## Decision gate

Include a number only when it is:

1. relevant;
2. decision-useful;
3. epistemically defensible.

Omit the number when materiality or grounding fails.

## Required behavior

- Answer the user's actual question first.
- Select domain-appropriate metrics.
- Include a comparator, denominator, period, or reference class when material.
- Date time-sensitive figures.
- Use ranges or scenarios when uncertainty is material.
- State assumptions for calculations and estimates.
- Distinguish event probability from confidence in the estimate.
- Remain qualitative when reliable quantification is unavailable.

## Forbidden behavior

- Fabricated data.
- Decorative percentages.
- False precision.
- Rankings without criteria.
- Stale values presented as current.
- Incompatible comparisons without warning.
- Numerical clutter that obscures the conclusion.

## Optional structured output

For tool pipelines that require machine-readable output, use `schemas/quantitative-frame.schema.json` for the final Quantitative Frame. This schema is optional and does not require every answer to contain a frame.

## Validation

Before publishing changes, run:

```bash
python scripts/validate.py
```

Behavioral changes require corresponding updates to `EVALS.md` and `CHANGELOG.md`.
