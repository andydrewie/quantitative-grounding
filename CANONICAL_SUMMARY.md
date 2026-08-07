# QG-01: Quantitative Grounding

## Precision pass

Formalize the Quantitative Grounding Protocol as a portable, model-agnostic skill with explicit activation rules, execution logic, evidence standards, output behavior, safeguards, and evaluation tests.

## Answer

Done. I have formalized it as:

# QG-01: Quantitative Grounding

## Core purpose

> Add the minimum sufficient quantitative structure needed to understand **scale, comparison, likelihood, economics, uncertainty, and decision relevance**, without introducing numerical theater or false precision.

This is now a genuine **skill specification**, rather than merely a paragraph of prompting. It defines:

- how the Codex skill is explicitly invoked and how persistent prompt deployment differs;
- when it should remain suppressed;
- which metrics to select by domain;
- how evidence, calculations, estimates, and scenarios differ;
- how probabilities should be calibrated;
- how rankings should be constructed;
- how currentness and data freshness should be handled;
- what the output should look like;
- what constitutes failure;
- how another agent can evaluate whether the skill performed correctly.

## The governing rule

A number should be included only when it is:

1. **Relevant:** It materially changes the interpretation.
2. **Decision-useful:** It improves comparison, prioritization, forecasting, or action.
3. **Epistemically defensible:** It comes from reliable evidence, transparent calculation, or clearly stated assumptions.

This prevents the skill from degenerating into:

> "Add numbers everywhere."

Instead, it becomes:

> "Identify where measurement reveals the structure of the problem, then quantify only to the level the evidence supports."

## Invocation policy

The installed Codex skill is explicit-use only. Invoke it with `$quantitative-grounding`; installation does not activate it from prompt similarity alone.

Once explicitly invoked, QG-01 applies most fully to substantive questions involving:

- rankings and comparisons;
- companies, markets, and industries;
- probability, risk, and forecasting;
- costs, resources, time, capacity, and productivity;
- macroeconomics and microeconomics;
- technical architecture and system performance;
- social prevalence and institutional behavior;
- strategic decisions and opportunity costs;
- claims such as *large, likely, rare, expensive, dominant, fast, growing,* or *successful*.

Even after invocation, it remains light or qualitative for:

- creative writing;
- stylistic rewriting;
- emotional support;
- casual conversation;
- purely philosophical exploration;
- early ideation where premature quantification could narrow the thinking.

## Evidence hierarchy

The skill prefers quantitative grounding in this order:

1. Current authoritative or primary-source data
2. High-quality reported data with a stated date and scope
3. Transparent calculations from known inputs
4. Informed estimates with explicit assumptions and ranges
5. Scenario models showing how assumptions change outcomes
6. Qualitative analysis when reliable quantification is unavailable

The sixth option is important. The skill explicitly permits the model to say:

> Reliable quantification is unavailable here. Assigning a number would create false precision.

That is considered a successful result, not a failure.

## Epistemic distinctions

QG-01 distinguishes among:

- **Verified fact**
- **Reported data**
- **Calculated result**
- **Informed estimate**
- **Scenario assumption**
- **Speculative judgment**

It also separates two concepts that AI models frequently blur:

> **Event probability:** How likely the event is to occur.  
> **Estimate confidence:** How much confidence we should place in that probability estimate.

For example:

> Estimated probability: **35 to 55%**.  
> Confidence in the estimate: **low to moderate**, because the base rate is unclear and two assumptions dominate the result.

## Output behavior

The model should answer the question first, then integrate approximately **one to five high-value quantitative anchors** where applicable.

For major analytical answers, it may conclude with a compact:

### Quantitative Frame

| Metric | Value or range | Baseline or meaning | Basis or confidence |
|---|---:|---|---|

This section is omitted when it would add no real value.

## Invocation and deployment commands

### Explicit Codex invocation

> **Use $quantitative-grounding to add relevant baselines and uncertainty to this analysis.**

### Separate persistent prompt deployment

An operator may copy `SYSTEM_PROMPT.txt` into an agent's system or developer instructions when persistent behavior is desired for that configured environment. This opt-in deployment is distinct from the Codex skill's explicit-only policy.

> **Activate QG-01 by default for substantive analytical questions. Quantify only when relevant, decision-useful, and epistemically defensible.**

### Depth modes

- **QG-01/Lite:** `Use $quantitative-grounding in QG-01/Lite mode ...` for one to three quantitative anchors with minimal added length.
- **QG-01/Standard:** `Use $quantitative-grounding in QG-01/Standard mode ...` for three to five anchors, comparisons, and uncertainty.
- **QG-01/Deep:** `Use $quantitative-grounding in QG-01/Deep mode ...` for scenarios, assumptions, sensitivity analysis, and a Quantitative Frame.

## Integration with your precision-first behavior

The cleanest sequence is:

1. **Precision pass:** Identify what you are truly asking and sharpen the terms.
2. **QG-01:** Determine what can and should be measured.
3. **Domain reasoning:** Apply the appropriate economic, technical, social, legal, medical, philosophical, or strategic lens.
4. **Quantitative Frame:** Crystallize the numbers that materially shape the conclusion.

This means your two standing skills now perform different but complementary functions:

> **Precision identifies the true question.**  
> **Quantitative grounding establishes the scale of the answer.**

## Quality threshold

The included evaluation rubric scores each response across:

- relevance;
- grounding;
- comparison;
- uncertainty;
- decision utility.

A response passes at **8/10 or higher**, provided it contains no critical failure such as fabricated data, false precision, unsupported current figures, misleading denominators, or incompatible comparisons.

## Canonical principle

> **Quantify when numbers reveal reality. Do not quantify when numbers merely imitate certainty.**

## Transferable skill package

The package contains the full skill specification, a compact system prompt, deployment instructions, and behavioral evaluation tests.
