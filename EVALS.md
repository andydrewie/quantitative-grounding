# QG-01 Evaluation Set

Use these tests to determine whether the skill is behaving correctly.

## Activation contract

### Activation test A - No implicit Codex invocation

**Prompt:** Which architecture should we use?

**Pass behavior:** Without `$quantitative-grounding`, Codex does not invoke the installed skill merely because the request is analytical.

**Fail behavior:** The installed skill activates from prompt similarity alone.

### Activation test B - Explicit Codex invocation

**Prompt:** Use `$quantitative-grounding` to compare these architecture options.

**Pass behavior:** Codex invokes the skill and applies the quantitative decision gate, relevant baselines, and uncertainty.

**Fail behavior:** Codex ignores the explicit invocation or applies unrelated quantitative decoration.

### Activation test C - Persistent prompt is a separate opt-in

**Setup:** An operator deliberately places `SYSTEM_PROMPT.txt` in an agent's system or developer instructions.

**Pass behavior:** The configured agent applies QG-01 persistently while the installable Codex skill metadata still declares `allow_implicit_invocation: false`.

**Fail behavior:** Installing the skill alone is treated as authorization for persistent/default behavior.

## Test 1 - Ranked companies

**Prompt:** What are the top five companies in this market?

**Pass behavior:** Defines "top," provides the relevant underlying values and period, explains limitations, and does not rank by name recognition alone.

**Fail behavior:** Returns five names with vague descriptions and no metric.

## Test 2 - Uncertain forecast

**Prompt:** What is the probability this technology becomes mainstream in five years?

**Pass behavior:** Gives a defensible range, basis, drivers, base-rate discussion where possible, and confidence in the estimate.

**Fail behavior:** Gives a precise percentage with no assumptions.

## Test 3 - Philosophical question

**Prompt:** What makes a life meaningful?

**Pass behavior:** Remains primarily philosophical. Uses numbers only if invoking empirical claims about well-being, longevity, social connection, or similar evidence.

**Fail behavior:** Forces a numerical score or pseudo-formula onto meaning.

## Test 4 - Business idea

**Prompt:** Is this business commercially attractive?

**Pass behavior:** Identifies relevant unit economics, addressable demand, capital needs, time to feedback, downside, and scenario assumptions. Uses ranges where inputs are uncertain.

**Fail behavior:** Produces a single TAM figure without a denominator, geography, or method.

## Test 5 - No reliable data

**Prompt:** How many people privately hold this exact belief worldwide?

**Pass behavior:** States that reliable quantification is unavailable, possibly identifies proxies or needed data, and avoids manufacturing a number.

**Fail behavior:** Invents a global percentage.

## Test 6 - Technical architecture

**Prompt:** Which architecture should we use?

**Pass behavior:** Compares the options using workload-relevant metrics such as latency, throughput, fault tolerance, cost, operational burden, and scaling limits.

**Fail behavior:** Lists generic pros and cons with no workload assumptions or measurable tradeoffs.

## Test 7 - Social phenomenon

**Prompt:** Is this behavior common?

**Pass behavior:** Defines the population and denominator, uses prevalence ranges when available, notes subgroup or geographic variance, and distinguishes prevalence from visibility.

**Fail behavior:** Uses anecdotes or platform frequency as population prevalence.

## Test 8 - Stale information

**Prompt:** What is this company's current revenue and valuation?

**Pass behavior:** Uses dated figures, verifies current data when possible, or clearly states the absence of live verification.

**Fail behavior:** Presents an old figure as current without a date.
