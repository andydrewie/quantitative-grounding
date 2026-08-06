---
name: quantitative-grounding
description: "Add the minimum sufficient quantitative structure needed to understand scale, comparison, likelihood, economics, uncertainty, and decision relevance without numerical theater or false precision. Use by default for substantive analytical requests involving rankings, companies, markets, probability, forecasting, economics, technical performance, social prevalence, strategy, resources, capacity, or consequential empirical claims; also use when the user invokes QG-01, quantitative grounding, quantify this, or compared with what. Use lightly or suppress for creative writing, stylistic rewriting, emotional support, casual conversation, non-empirical philosophy, or early ideation unless the user explicitly asks for quantification."
---

# QG-01 - Quantitative Grounding

## 1. Purpose

Convert relevant qualitative claims into decision-useful quantitative structure.

The skill should help the user answer:

- How large is it?
- Compared with what?
- How likely is it?
- Over what period?
- What does it cost or produce?
- How widely is it distributed?
- Which assumptions drive the result?
- How reliable is the estimate?

The objective is not numerical density. The objective is the **minimum sufficient quantitative structure needed to understand the actual shape of reality**.

## 2. Governing Rule

Use quantitative grounding when it is:

1. **Relevant** - the number materially changes interpretation.
2. **Decision-useful** - the number improves comparison, prioritization, forecasting, or action.
3. **Epistemically defensible** - the number comes from reliable evidence, transparent calculation, or clearly stated assumptions.

Never manufacture numbers merely to make an answer appear rigorous.

## 3. Trigger Conditions

### Activate by default when the request involves

- rankings, comparisons, or superlative requests;
- companies, markets, industries, business models, or investment;
- probability, risk, forecasting, or scenario analysis;
- cost, time, resources, capacity, productivity, or performance;
- macroeconomics or microeconomics;
- technical systems, architecture, reliability, latency, throughput, or scaling;
- social prevalence, population effects, institutional behavior, or policy;
- strategic or personal decisions where expected benefit, downside, reversibility, or opportunity cost matters;
- claims using words such as large, small, likely, rare, expensive, fast, dominant, successful, efficient, growing, or important.

### Suppress or use lightly when the request is primarily

- creative writing;
- stylistic rewriting;
- emotional support;
- casual conversation;
- open-ended philosophical exploration with no empirical claim;
- early ideation where numbers would prematurely narrow the search space.

Quantify these only when the user asks or when an empirical claim materially affects the answer.

## 4. Quantification Decision Gate

Before including a number, test it against five questions:

1. **Materiality:** Would this number change how the user understands or acts on the answer?
2. **Metric fit:** Does the metric actually measure the claim being made?
3. **Grounding:** Is it supported by evidence, calculation, or explicit assumptions?
4. **Freshness:** Is the number current enough for the question?
5. **Calibration:** Should it be a range, distribution, or scenario rather than a point estimate?

If the number fails materiality or grounding, omit it.

## 5. Evidence Hierarchy

Prefer quantitative claims in this order:

1. Current authoritative or primary-source data.
2. High-quality reported data with a stated date and scope.
3. Transparent calculation from known inputs.
4. Informed estimate with explicit assumptions and a defensible range.
5. Scenario model showing how outputs change under different assumptions.
6. Qualitative treatment when reliable quantification is unavailable.

Do not descend the hierarchy silently. Label the epistemic status when ambiguity could mislead the user.

## 6. Epistemic Labels

Use labels selectively, especially for decision-critical claims:

- **Verified fact** - directly supported by reliable evidence.
- **Reported data** - attributed data that may depend on a source's methodology.
- **Calculated result** - derived transparently from stated inputs.
- **Informed estimate** - reasoned approximation with an uncertainty range.
- **Scenario assumption** - hypothetical input used to explore outcomes.
- **Speculative judgment** - plausible but weakly grounded interpretation.

Do not label every number mechanically. Use labels where provenance or uncertainty matters.

## 7. Metric Selection by Domain

Select only the metrics that explain the conclusion.

### Companies and markets

Possible metrics include revenue, growth rate, gross margin, operating margin, EBITDA, free cash flow, valuation, market share, headcount, revenue per employee, customer concentration, capital intensity, retention, unit economics, or geographic exposure.

Do not request or include EBITDA by reflex. Use it only when it is economically meaningful for the business model and comparison.

### Rankings

Provide:

- the ranking criterion;
- the underlying values;
- the applicable period;
- the coverage set or denominator;
- material limitations.

Do not present a ranked list of names without explaining what "top" means.

### Macroeconomics

Possible metrics include GDP share, productivity, employment, inflation, interest rates, trade flows, capital expenditure, fiscal burden, demographic change, or historical growth.

State geography, currency, nominal versus real treatment, and time period when relevant.

### Technical systems and architecture

Possible metrics include latency, throughput, uptime, error rate, failure probability, cost per request, compute or memory requirements, concurrency, recovery time, scaling curve, bottleneck capacity, or human-review burden.

### Social systems and sociology

Possible metrics include prevalence, incidence, population affected, effect size, demographic distribution, geographic variation, historical trend, sample size, response rate, or institutional concentration.

Avoid treating an average as the whole distribution when variance or subgroup differences matter.

### Personal and strategic decisions

Possible metrics include expected benefit, probability of success, downside magnitude, time commitment, opportunity cost, reversibility, switching cost, time to feedback, and expected value.

## 8. Probability Protocol

Distinguish:

- **Event probability:** the estimated chance that something will happen.
- **Estimate confidence:** how reliable that probability estimate is.

For model-generated probabilities:

- explain the basis;
- use base rates when available;
- identify the strongest positive and negative drivers;
- prefer defensible ranges over arbitrary point estimates;
- avoid decorative percentages;
- do not imply statistical measurement when the number is a judgment call.

Example:

> Estimated probability: 35-55%. Confidence in this estimate: low-to-moderate, because the base rate is unclear and two key assumptions dominate the outcome.

## 9. Estimation and Scenario Protocol

When exact data is unavailable but estimation would be useful:

1. State the target quantity.
2. Define the calculation or model.
3. List the material assumptions.
4. Use a range or multiple scenarios.
5. Identify the most sensitive assumption.
6. State confidence and limitations.

Do not provide a precise point estimate when the inputs support only an order of magnitude.

## 10. Freshness and Retrieval Rule

Time-sensitive figures must include a date, reporting period, or "as of" marker.

When current verification is unavailable:

- do not present unstable figures as current;
- state that live verification is required;
- use older figures only when clearly dated and still analytically useful;
- never fabricate a recent value to complete the answer.

## 11. Output Contract

### Default response behavior

- Answer the user's actual question first.
- Integrate one to five high-value quantitative anchors into the reasoning.
- Provide an explicit baseline or comparator where it changes interpretation.
- State uncertainty where material.
- Keep the answer proportionate; do not turn every response into a financial report.

### Quantitative Frame

For major analytical responses, end with a compact **Quantitative Frame** containing the three to five numbers, ranges, ratios, or measurable constraints that most materially shape the conclusion.

Suggested format:

| Metric | Value or range | Baseline / meaning | Basis / confidence |
|---|---:|---|---|

Omit the section when quantification would not meaningfully improve the answer.

## 12. Systems Lens

When useful, connect the numbers to:

- system structure;
- incentives;
- constraints and bottlenecks;
- feedback loops;
- resource flows;
- power or concentration;
- institutional behavior;
- human behavior;
- second-order effects.

Use the user's systems-architect, ontological, and sociological perspective as an analytical lens, not as a constraint that overrides the domain's own expertise.

## 13. Anti-Patterns

Never do the following:

- invent numbers to satisfy the skill;
- use an exact percentage without a defensible basis;
- provide a ranking without a criterion;
- compare figures from incompatible years, currencies, geographies, or accounting definitions without warning;
- cite revenue when profit, cash flow, adoption, or reliability is the true issue;
- use EBITDA where it obscures capital intensity or cash economics;
- present an average without noting a consequential distribution;
- use stale figures as though they were current;
- confuse correlation with effect size or causation;
- bury the conclusion beneath numerical clutter;
- use "fuzzy math" without assumptions, ranges, or sensitivity analysis.

## 14. Failure Behavior

When reliable quantification is unavailable, say so directly.

Preferred behavior:

> Reliable quantification is not available here. I can identify the relevant variables and what data would be needed, but assigning a number would create false precision.

Remaining qualitative is better than manufacturing certainty.

## 15. Activation Syntax

### Persistent activation

> Activate QG-01 by default for substantive analytical questions. Quantify only when relevant, decision-useful, and epistemically defensible.

### On-demand activation

> Run QG-01 on this question.

### Depth modes

- **QG-01/Lite:** one to three quantitative anchors; minimal added length.
- **QG-01/Standard:** three to five anchors, baselines, and uncertainty.
- **QG-01/Deep:** scenarios, sensitivity analysis, assumptions, and a Quantitative Frame.

## 16. Interoperability with a Precision-First Skill

Recommended order:

1. **Precision pass:** sharpen the user's question and identify the true decision or comparison.
2. **QG-01:** determine what should be measured and how defensibly it can be measured.
3. **Domain reasoning:** answer using the appropriate technical, economic, social, legal, medical, or philosophical lens.
4. **Quantitative Frame:** summarize only the numbers that materially shape the conclusion.

## 17. Quality Rubric

Score each dimension from 0 to 2:

1. **Relevance:** Are the numbers material to the question?
2. **Grounding:** Are they supported, calculated, or explicitly assumed?
3. **Comparison:** Is there a useful baseline, denominator, or reference class?
4. **Uncertainty:** Are ranges, limitations, and confidence handled honestly?
5. **Decision utility:** Do the numbers improve judgment or action?

Passing score: **8/10 or higher**, with no critical failure.

Critical failures include fabricated data, false precision, an unsupported current figure, a misleading denominator, or an unexplained incompatible comparison.

## 18. Canonical Principle

> Quantify when numbers reveal reality. Do not quantify when numbers merely imitate certainty.
