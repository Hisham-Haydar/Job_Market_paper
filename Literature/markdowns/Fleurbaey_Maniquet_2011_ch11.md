---
title: "A Theory of Fairness and Social Welfare, Chapter 11: Income Taxation"
authors: [Marc Fleurbaey, François Maniquet]
year: 2011
outlet: "Cambridge University Press (book chapter)"
country_or_context: "Abstract optimal income taxation model with private information"
population: "Abstract agents with heterogeneous skills and preferences"
data_period: "Not applicable"
shelf: "axiomatic income taxation / second-best / incentive compatibility / compensation vs responsibility"
tags: [income-taxation, second-best, incentive-compatibility, leximin, compensation-vs-responsibility, zero-marginal-tax, observable-labour, unobservable-labour, egalitarian-Walrasian, axiomatic-public-finance, Fleurbaey, Maniquet]
priority: "very high"
read_status: "extracted"
---

# Full citation

Fleurbaey, M., & Maniquet, F. (2011). Income taxation. In *A Theory of Fairness and Social Welfare* (Chapter 11). Cambridge University Press. DOI: 10.1017/CBO9780511851971.016.

# One-sentence contribution

Shows how the social ordering functions characterised in Chapter 10 generate concrete second-best tax criteria under private information on skills and preferences, deriving that all highlighted orderings imply zero or nonpositive marginal taxation at low incomes.

# Why this paper matters

This is the policy-implementation chapter for the Fleurbaey-Maniquet axiomatic framework. It bridges abstract fairness axioms and actual tax design under informational constraints, showing that responsibility-sensitive fairness criteria have sharp policy implications that differ from standard welfarist optimal taxation. For my JMP, this chapter demonstrates how a normative welfare framework translates into concrete tax properties -- the kind of bridge my framework would need to cross from $W(z,R,A;y)$ to policy recommendations.

# Core research question

Given the social ordering functions from Chapter 10 ($R^{slex}$, $R^{sminlex}$, $R^{\tilde{\ell}EW}$), what optimal income tax properties follow when skills and preferences are private information and the policymaker is restricted to incentive-compatible allocations?

# Model / theoretical framework

**Unequal-skills model from Chapter 10** with two informational structures:
1. **Observable labour:** Labour time and earnings observed; skill hidden. IC: agent with skill $s_i \geq w_j$ must prefer own bundle to bundle of agent earning $w_j$.
2. **Unobservable labour:** Only earnings observed. IC: agent with $s_i$ can imitate gross earnings of agent with $s_j$ by adjusting labour: $(\ell_i, c_i) \, R_i \, (s_j \ell_j / s_i, c_j)$.

**Key representation results:** IC allocations representable as tax schedules -- menus of skill-contingent tax functions when labour is observable (Lemma 11.1); a single earnings tax function $\tau(y)$ when labour is unobservable (Lemma 11.2).

# Key objects

- IC allocations represented as tax functions.
- Reform-evaluation criteria for each SOF under each informational structure (Table 11.1).
- Zero or nonpositive marginal tax results for low-skilled agents.

# Main findings

1. **SOF approach accommodates IC naturally:** Because SOFs are leximin-type with informationally simple indices, the policymaker can evaluate tax systems without full type-distribution knowledge.

2. **EP-Transfer SOFs are more redistributive** than ES-Transfer SOFs.

3. **Zero marginal tax at low incomes (Theorem 11.1):** Under observable labour, $R^{sminlex}$ and $R^{\tilde{\ell}EW}$ optima can be implemented with zero marginal taxation for the low-skilled; $R^{slex}$ implies nonpositive average marginal taxation.

4. **Reform priorities differ (Table 11.1):** $R^{slex}$ and $R^{sminlex}$ focus reform attention on low-skilled; $R^{\tilde{\ell}EW}$ may prioritise higher-skilled agents.

5. **Unobservable labour (Theorem 11.3):** Under Assumption 11.1, $R^{sminlex}$ and $R^{\tilde{\ell}EW}$ optima have tax constant on $[0, s_{min}]$.

6. **$R^{sminlex}$ optimal tax (Theorem 11.4):** Minimise $\tau(s_{min})$ subject to $\tau(y) = \tau(s_{min})$ for $y \leq s_{min}$ and $\tau(y) \geq \tau(s_{min})$ for $y > s_{min}$.

7. **$R^{\tilde{\ell}EW}$ with small $\tilde{\ell}$:** At $\tilde{\ell} = 0$, laissez-faire is optimal. "Leximin-like" does not automatically mean "high redistribution."

# Treatment of preferences

Preferences are private information and cannot be conditioned upon by the tax authority. But the relevant welfare indices can be inferred from observed choices and tax schedules, keeping the framework implementable.

# Treatment of opportunities / constraints

Opportunities remain scalar skills, as in Chapter 10. The new ingredient is informational: the policymaker cannot observe true skills or (in one case) labour time. IC constraints are the mechanism through which opportunity heterogeneity enters tax design. No explicit job sets, $A$-type objects, or demand-side constraints.

# Welfare / normative object

Policy objective: maximise chosen SOF under IC. The chapter preserves the compensation-vs-responsibility distinction and studies how it constrains tax design under asymmetric information. Directly relevant to tax design under opportunity-sensitive fairness.

# Main limitations

- Skills remain the only opportunity heterogeneity; no job sets, search, rationing.
- Exact optimal-tax formulas largely unavailable; many results are partial characterisations or conditional ("if second-best efficient, then optimal").
- Assumptions 11.1--11.2 restrict type distributions.
- Policymaker knows type distribution (hidden identities, not hidden aggregates).

# Relevance for my JMP

## possible use for policy bridge
Shows how to translate fairness axioms into second-best tax properties. If my framework defines $W(z,R,A;y)$, this chapter provides the template for deriving tax implications under IC.

## possible use for the zero marginal tax result
The finding that fairness-based criteria imply zero or nonpositive marginal tax at low incomes is a strong normative benchmark for evaluating actual tax-transfer systems through my framework.

## possible use for IC formulation
Clarifies which private information matters: hidden skills, hidden preferences, hidden labour. For my richer setting, hidden opportunity sets would be an additional dimension.

# Research questions this paper inspires

1. What is the analogue of the zero low-income marginal tax result when the ethical object is $W(z,R,A;y)$ with set-valued opportunities?

2. How should IC be formulated when agents can hide not only skill but also the composition of their feasible opportunity sets?

3. Can the $\tilde{\ell}$-type tax idea be generalised into a reference-opportunity tax principle?

# Challenge to this paper

The chapter translates scalar unequal-skills ethics into tax design very successfully, but precisely because the opportunity side is a scalar, the implementation problem is cleaner than the one my project addresses. Hidden skills and hidden effort are central; hidden opportunity sets are not. This makes the chapter a strong normative-public-finance benchmark rather than a final model of labour-market justice.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] Second-best policy design when social welfare depends on preferences and skills under private information. $z = (\ell, c)$; $R$ = private preferences; $y$ enters as pretax earnings and tax-induced consumption mapping; $A$ absent (skill $s_i$ proxies opportunity).

[Reasonable inference for my project] The tax-design logic could extend: if $W(z,R,A;y)$ is defined and a social ordering derived, IC constraints would restrict implementable policies analogously.

[Unclear from paper] No $W(z,R,A;y)$; no IIJ/IPIJ axioms; no actual vs reference opportunity sets.

# Relation to Bargain et al. (2013)

Not directly related. Bargain et al. is empirical; this chapter is theoretical. Both take preference heterogeneity seriously.

# Relation to opportunities vs preferences

Highly relevant in the same narrow sense as Chapter 10. Skills = compensable opportunity; preferences = responsibility. The whole chapter studies how this ethical distinction survives the move to second-best taxation. But opportunities remain scalar, not set-valued.

# Useful quotations / formulas

**IC (observable labour):**
$$s_i \geq w_j \Rightarrow (\ell_i, c_i) \, R_i \, (\ell_j, c_j)$$

**IC (unobservable labour):**
$$s_i \geq s_j \ell_j \Rightarrow (\ell_i, c_i) \, R_i \, \left(\frac{s_j}{s_i}\ell_j, c_j\right)$$

**Theorem 11.1:** $R^{sminlex}$ and $R^{\tilde{\ell}EW}$ $\Rightarrow$ zero marginal tax for low-skilled (observable labour).

**Theorem 11.3:** $R^{sminlex}$ and $R^{\tilde{\ell}EW}$ $\Rightarrow$ $\tau$ constant on $[0, s_{min}]$ (unobservable labour).

# Suggested tags

income-taxation, second-best, incentive-compatibility, zero-marginal-tax, leximin, compensation-vs-responsibility, observable-labour, unobservable-labour, egalitarian-Walrasian, axiomatic-public-finance, Fleurbaey, Maniquet

# My quick takeaway

The policy-implementation companion to Chapter 10. Its main value for my JMP is as a template for translating fairness axioms into second-best tax properties under IC. The headline result -- zero or nonpositive marginal taxation at low incomes under all highlighted SOFs -- is a powerful normative benchmark. The extension to richer opportunity structures (set-valued $A_i$ rather than scalar $s_i$) is the natural next step.
