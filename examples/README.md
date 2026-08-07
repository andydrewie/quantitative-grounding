# Examples

## Explicit invocation

```text
Use $quantitative-grounding to answer this question: Which database architecture should we use for a latency-sensitive agent system?
```

Expected behavior:

- define the workload and comparison criteria;
- compare latency, throughput, consistency, failure recovery, operational burden, and cost where relevant;
- state assumptions and uncertainty;
- avoid generic pros-and-cons lists without measurable tradeoffs.

## Lite mode

```text
Use $quantitative-grounding in QG-01/Lite mode: Is this market large enough to matter?
```

Expected behavior: one to three high-value anchors, a relevant baseline, and minimal added length.

## Standard mode

```text
Use $quantitative-grounding in QG-01/Standard mode: Rank the leading companies in this category.
```

Expected behavior: define "leading," provide the underlying values and period, and explain material limitations.

## Deep mode

```text
Use $quantitative-grounding in QG-01/Deep mode: What is the probability this technology becomes mainstream within five years?
```

Expected behavior: base rates where available, a probability range, positive and negative drivers, scenario assumptions, sensitivity analysis, and confidence in the estimate.

## Correct abstention

```text
Use $quantitative-grounding to answer: How many people worldwide privately hold this exact belief?
```

Expected behavior: state that reliable quantification is unavailable, identify possible proxies or required data, and avoid inventing a percentage.
