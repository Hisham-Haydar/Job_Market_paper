---
title: "A Practitioner's Note on the Shapley-Owen-Shorrocks Decomposition"
authors: [Richard Audoly, Rory McGee, Sergio Ocampo, Gonzalo Paz-Pardo]
year: 2025
outlet: "Federal Reserve Bank of New York Staff Reports, No. 1163"
country_or_context: "General methodological note"
population: "Not applicable"
data_period: "Not applicable"
shelf: "decomposition methods / Shapley value / structural models / methodology"
tags: [Shapley-decomposition, Owen-value, Shorrocks-decomposition, methodology, structural-models, nonlinear-decomposition, R-squared-decomposition, welfare-decomposition, grouped-factors]
priority: "medium"
read_status: "extracted"
---

# Full citation

Audoly, R., McGee, R., Ocampo, S., & Paz-Pardo, G. (2025). A practitioner's note on the Shapley-Owen-Shorrocks decomposition. *Federal Reserve Bank of New York Staff Reports* No. 1163, August 2025.

# One-sentence contribution

Provides a compact, practitioner-oriented exposition of the Shapley-Owen-Shorrocks decomposition for nonlinear outcomes, showing through worked examples how it yields an additive, order-invariant decomposition of arbitrary functions into contributions of individual inputs or groups of inputs.

# Why this paper matters

Structural economic models -- including the RURO labour supply models and equivalent income computations in my literature -- produce nonlinear outcomes that depend on many interacting inputs (preferences, opportunity sets, tax-benefit rules, wages). Decomposing aggregate welfare or inequality statistics into contributions of these components is a standard exercise, but standard decompositions are order-dependent when interactions are nonlinear. This paper provides the methodological tool for performing such decompositions cleanly.

# Core research question

How can one decompose a nonlinear aggregate outcome into contributions of inputs (or groups of inputs) in a way that is additive, symmetric, and interpretable?

# Economic setting and context

Purely methodological. No substantive country or population. Motivated by the prevalence of nonlinear aggregation in structural economic models and the underuse of the Shapley-Owen-Shorrocks decomposition despite its practical value.

# Model / theoretical framework

**General decomposition framework:** For an arbitrary function $Y = f(X_1, X_2, \ldots, X_n)$, the Shapley-Owen-Shorrocks decomposition assigns contribution $C_j$ to each input $X_j$.

**Four defining properties:**
1. **Exact decomposition:** $\sum_{j=1}^n C_j = f(X_1, \ldots, X_n) - f(\emptyset)$ (contributions sum to total minus null).
2. **Symmetry:** The order in which inputs are removed does not affect $C_j$.
3. **Null-effect normalization:** If $X_j$ never changes $f$, then $C_j = 0$.
4. **Linearity:** The attribution operator is linear in $f$.

**Contribution formula (eq. 2):**
$$C_j = \sum_{k=0}^{n-1} \frac{(n-k-1)!k!}{n!} \sum_{s \subseteq S_k \setminus \{X_j\}: |s|=k} [f(s \cup \{X_j\}) - f(s)]$$

This averages the marginal contribution of $X_j$ over all possible orderings in which other inputs are removed.

**Grouped factors (Owen extension):** When inputs naturally move together (e.g., all prices, all policy parameters), the Owen value extension decomposes across groups, then within groups, preserving the same properties.

# Key objects

- **Contribution $C_j$:** The proportion of $f(\cdot)$ attributable to input $X_j$, computed as the average marginal contribution across all elimination orderings.
- **Null/reference model $f(\emptyset)$:** The value of the function when all inputs are at their reference/null values. The decomposition is additive relative to this baseline.
- **Sub-models:** All $2^n$ evaluations of $f$ with different subsets of inputs at their actual vs null values.

# Data

No original data. Illustrated with toy examples (linear, nonlinear with interaction, $R^2$ decomposition).

# Identification logic

Deterministic once the analyst specifies: (1) the outcome function $f$, (2) the inputs/grouping, and (3) the null values. Substantive interpretation depends entirely on model design upstream of the decomposition.

# Estimation / empirical strategy

Expository. Worked examples: linear case (decomposition = standard additive), nonlinear interaction ($Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \beta_3 X_3 X_2$: interaction term split symmetrically, $C_2 = \beta_2 X_2 + \frac{1}{2}\beta_3 X_2 X_3$, $C_3 = \frac{1}{2}\beta_3 X_2 X_3$), and $R^2$ decomposition (differs from partial $R^2$ because it preserves exact additivity).

# Treatment of preferences

Not modelled. Preferences can enter only if the analyst chooses $f$ to depend on preference parameters.

# Treatment of opportunities / constraints

Not modelled. Relevant only as a downstream tool once a model has represented opportunities through feasible sets $A$, opportunity densities, or similar objects.

# Welfare / normative object

None. The paper is a decomposition tool, not a welfare criterion. But the authors explicitly mention welfare decompositions from counterfactual exercises as a promising application.

# Main findings

1. **Uniqueness:** The Shapley-Owen-Shorrocks decomposition is the unique decomposition satisfying exact additivity, symmetry, null-effect normalisation, and linearity.

2. **Linear case:** Reduces to standard additive decomposition (marginal effects are order-invariant).

3. **Nonlinear interaction case:** Interaction terms are split symmetrically across interacting variables. Clear illustration of why order-averaging matters.

4. **$R^2$ decomposition:** Differs from partial $R^2$ because it preserves exact additivity and symmetry.

5. **Computational cost:** $2^n$ sub-model evaluations required, but grouped factors (Owen extension) can reduce this substantially.

# Main limitations

- Purely methodological: does not tell the analyst how to define economically meaningful factors, how to choose null values, or how to interpret decomposed components ethically.
- Computational cost grows exponentially ($2^n$) with the number of inputs.
- The decomposition is as convincing as the substantive model underneath it -- it guarantees formal properties but not economic meaningfulness.

# Relevance for my JMP

## possible use for welfare decomposition
If my RURO framework generates an aggregate welfare or inequality statistic (e.g., inequality in equivalent incomes), the Shapley-Owen-Shorrocks decomposition can attribute it to contributions of preferences $R$, opportunity sets $A$, pay schedules $y$, and tax-benefit rules without arbitrary ordering. This is its strongest use for my project.

## possible use for grouped counterfactual accounting
The Owen extension for grouped factors is directly relevant if I want to group model components (e.g., all demand-side parameters as "opportunities", all preference parameters as "preferences") and decompose across groups first, then within groups.

## possible use for cross-country or cross-policy comparisons
If my project compares welfare across countries or policy regimes, the decomposition can attribute cross-context differences to specific model components.

# Research questions this paper inspires

1. Can inequality in equivalent incomes $W(z, R, A; y)$ be decomposed additively into contributions of $R$, $A$, $y$, and demographic characteristics using this method? What are the appropriate null values for "removing" opportunity sets (universal access? no access? reference access?)?

2. How sensitive are welfare decompositions in structural labour supply models to the choice of null values and factor groupings?

# Challenge to this paper

The method is formally elegant but substantively agnostic. The hard question in welfare decomposition is not the mechanics of order-invariant attribution but the economic meaning of "removing" an input. For the RURO framework, what does it mean to evaluate welfare with the opportunity density $g(h,w)$ set to its "null" value? Setting $g = 0$ (no jobs) is extreme; setting $g$ = uniform (equal access) imposes a normative reference. The Shapley-Owen-Shorrocks decomposition answers "how much" each factor contributes, but the "how much" depends entirely on the analyst's choice of null model, which encodes normative judgements the method itself does not adjudicate.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper provides a general decomposition for arbitrary nonlinear functions, explicitly mentioning welfare decompositions and structural counterfactuals as key applications. The Owen grouped-factor extension allows natural groupings of model components.

[Reasonable inference for my project] Directly relevant for decomposing aggregate outcomes from $W(z, R, A; y)$ across preferences, opportunities, pay schedules, and grouped parameter blocks. The method ensures additive and symmetric attribution without arbitrary ordering.

[Unclear from paper] How $z$, $R$, $A$, $y$ should be operationalised as "players", how the null model should be chosen, and how the decomposed contributions should be interpreted ethically. These are substantive modelling decisions the method does not address.

# Relation to Bargain et al. (2013)

Not directly related. Could be applied downstream to decompose cross-country differences in equivalent income inequality (as computed by Bargain et al.) into contributions of preferences, tax-benefit rules, and wage distributions.

# Relation to opportunities vs preferences

The paper is not about opportunities versus preferences. It is a tool for quantifying their relative contribution once a model has successfully distinguished them. Its correct role in my corpus is downstream and methodological.

# Useful quotations / formulas

**Contribution formula (eq. 2, p. 3):**
$$C_j = \sum_{k=0}^{n-1} \frac{(n-k-1)!k!}{n!} \sum_{s \subseteq S_k \setminus \{X_j\}: |s|=k} [f(s \cup \{X_j\}) - f(s)]$$

**On nonlinear interactions (p. 5-6):**
For $Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \beta_3 X_3 X_2$: $C_2 = \beta_2 X_2 + \frac{1}{2}\beta_3 X_2 X_3$, $C_3 = \frac{1}{2}\beta_3 X_2 X_3$.

**On applicability (p. 1):**
"We believe this is exceptionally well-suited to decompositions in rich-structural models of economic phenomena which are typically non-linear."

# Suggested tags

Shapley-Owen-Shorrocks, nonlinear-decomposition, grouped-decomposition, structural-model-accounting, welfare-decomposition, R-squared-decomposition, methodology, Audoly, McGee, Ocampo, Paz-Pardo

# My quick takeaway

A clean methodological note providing the tools for order-invariant, additive decomposition of nonlinear outcomes. For my JMP, this is a downstream tool: once the structural model produces welfare statistics, the Shapley-Owen-Shorrocks decomposition can attribute them to preferences, opportunities, and pay schedules without arbitrary ordering. The key limitation is that the method does not tell you what "removing" an input means economically -- that requires substantive modelling judgements about null/reference values.
