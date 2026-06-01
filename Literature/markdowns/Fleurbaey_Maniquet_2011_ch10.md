---
title: "A Theory of Fairness and Social Welfare, Chapter 10: Unequal Skills"
authors: [Marc Fleurbaey, François Maniquet]
year: 2011
outlet: "Cambridge University Press (book chapter)"
country_or_context: "Abstract labour-income taxation / fair allocation model"
population: "Abstract agents with heterogeneous preferences and productive skills"
data_period: "Not applicable"
shelf: "axiomatic fairness / unequal skills / social ordering functions / compensation vs responsibility / labour income taxation"
tags: [compensation, responsibility, unequal-skills, social-ordering-functions, leximin, fair-allocation, skills-vs-preferences, equal-preferences-transfer, equal-skill-transfer, skill-equivalent-leximin, egalitarian-Walrasian, Fleurbaey, Maniquet]
priority: "very high"
read_status: "extracted"
---

# Full citation

Fleurbaey, M., & Maniquet, F. (2011). Unequal skills. In *A Theory of Fairness and Social Welfare* (Chapter 10). Cambridge University Press. DOI: 10.1017/CBO9780511851971.015.

# One-sentence contribution

Studies the canonical unequal-skills labour-income model, proves that full compensation for skills and full responsibility for preferences are deeply incompatible, then characterises three families of social ordering functions ($R^{slex}$, $R^{sminlex}$, $R^{\tilde{\ell}EW}$) that implement different compromises between them.

# Why this paper matters

This is the foundational axiomatic treatment of the compensation-vs-responsibility conflict in the labour/leisure setting -- exactly the normative terrain my JMP operates on. The chapter does not model opportunities as explicit job sets, but it provides the rigorous normative benchmark for thinking about what should be neutralised (skills) and what should be left to individual choice (preferences) when agents differ in productive ability. The characterised social orderings are the reference criteria against which my richer $W(z,R,A;y)$ framework can be compared.

# Core research question

How should society rank feasible allocations when individuals differ both in preferences over consumption-leisure bundles and in productive skills, if one wants simultaneously to compensate for unequal skills and respect responsibility for preferences?

# Model / theoretical framework

**Static fair-allocation model.** Individual bundles $z_i = (\ell_i, c_i)$, labour $\ell_i \leq 1$, skill $s_i \geq 0$. Feasibility: $\sum c_i \leq \sum s_i \ell_i$. Budget set $B(s_i, z_i)$: linear budget with slope $s_i$ through $z_i$.

**Central impossibility results:**
- **Theorem 10.1:** No SOF satisfies Weak Pareto + Equal-Preferences Transfer + Equal-Skill Transfer.
- **Theorem 10.2:** Impossibility persists even when transfer axioms are weakened to anonymity axioms.

**Characterised compromises:**
- **$R^{slex}$ (skill-equivalent leximin):** Welfare index $u^s(z_i, R_i)$ = reference skill at which $z_i$ would be chosen. Satisfies EP-Transfer, Laissez-Faire Selection. More favourable to hardworking agents. (Theorem 10.3)
- **$R^{sminlex}$ ($s_{min}$-equivalent leximin):** Uses $s_{min}$-equivalent utility. Satisfies MI-Equal-Skill Transfer. More redistributive toward low-skilled. (Theorem 10.5)
- **$R^{\tilde{\ell}EW}$ ($\tilde{\ell}$-egalitarian Walrasian leximin):** Evaluates agents relative to income at reference labour $\tilde{\ell}$ on implicit budget. Choice of $\tilde{\ell}$ tunes redistributiveness. (Theorem 10.6)

**Table 10.1** summarises which axioms each ordering satisfies.

# Key objects

- Preferences $R_i$, skills $s_i$, bundles $z_i = (\ell_i, c_i)$.
- Budget set $B(s_i, z_i)$ and implicit budget $B^*(s_i, R_i, z_i)$.
- Skill-equivalent utility: $u^s(z_i, R_i) = u \iff z_i \, I_i \, \max_{R_i} B(u, (0,0))$.
- $\tilde{\ell}$-based well-being index: $u^{\tilde{\ell}}(z_i, s_i, R_i) = u \iff z_i \, I_i \, \max_{R_i} B(s_i, (\tilde{\ell}, u))$.

# Treatment of preferences

Preferences are one of two fundamental heterogeneities. Responsibility = neutrality with respect to preferences: agents with same skill should face same lump-sum transfer, then freely choose labour supply on the same linear budget (liberal reward). The chapter acknowledges that preferences may not be fully responsibility-grounded but proceeds with the compensation-vs-responsibility contrast.

# Treatment of opportunities / constraints

Opportunities summarised entirely by scalar skill $s_i$ (wage rate). No explicit job sets, hours restrictions, occupational menus, or latent opportunity structures. Highly relevant to opportunity heterogeneity as unequal wages but not to the richer notion of feasible job sets $A_i$. The chapter itself notes that low skills may reflect inherited features or unavailability of higher-wage jobs, but this is not formally modelled.

# Welfare / normative object

Social ordering functions over allocations, derived from fairness axioms. Not an individual scalar welfare function estimated from behaviour. The ethical conflict between compensation and responsibility is the organising principle. The characterised orderings are all leximin-type: efficiency + fairness + robustness push toward absolute priority for the worst-off under the relevant ethically defined index.

# Main findings

1. **Impossibility:** Full compensation and full responsibility are jointly unattainable (Theorems 10.1--10.2).
2. **$R^{slex}$:** Satisfies EP-Transfer + Laissez-Faire Selection. Favourable to hardworking agents. (Theorem 10.3)
3. **$R^{sminlex}$:** More redistributive. Satisfies MI-Equal-Skill Transfer. (Theorem 10.5)
4. **$R^{\tilde{\ell}EW}$:** Redistributiveness tuned by reference labour $\tilde{\ell}$. (Theorem 10.6)
5. **Methodological:** Combining efficiency, fairness, and robustness repeatedly pushes toward leximin aggregation.

# Main limitations

- Opportunity heterogeneity reduced to scalar skill: no job menus, rationing, or multidimensional feasible sets.
- Skills fixed and exogenous: no separation of acquired ability from inherited constraints.
- Static and abstract: no search frictions, occupational choice, or empirical institutions.
- Compromise criteria depend on axiom selection: the chapter maps the terrain rather than "solving" the conflict uniquely.

# Relevance for my JMP

## possible use for normative architecture
This is the foundational normative reference for my JMP. The impossibility results apply to any framework distinguishing compensable from responsible heterogeneity. The characterised orderings ($R^{slex}$, $R^{sminlex}$, $R^{\tilde{\ell}EW}$) are the benchmarks against which my $W(z,R,A;y)$-based social evaluation should be compared.

## possible use for the reference labour idea
The $\tilde{\ell}$-egalitarian Walrasian approach, which evaluates agents relative to income at a reference labour level, is suggestive for reference opportunity-set constructions in my framework.

## possible use for identifying the key trade-off
The impossibility results (compensation + responsibility cannot both hold fully) apply to my richer setting and should be explicitly acknowledged.

# Research questions this paper inspires

1. Can the scalar skill $s_i$ be replaced by a feasible-job-set $A_i$ while preserving analogous compensation and responsibility axioms?

2. What is the correct analogue of equal-skill transfer when opportunities are multidimensional job sets?

3. Can $W(z,R,A;y)$ be defined so that its induced social ranking reduces to $R^{slex}$ or $R^{sminlex}$ in the scalar-skill special case?

# Challenge to this paper

The ethical clarity is purchased by a very compressed model of opportunities. The chapter cleanly separates skills and preferences only because "skills" are reduced to a one-dimensional wage parameter. For a jobs-and-wellbeing framework, the natural extension is to replace $s_i$ with a set-valued opportunity object $A_i$, which raises new impossibility and characterisation questions the chapter cannot address.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] Rankings of allocations when outcomes depend on consumption, labour, preferences, and productive skills. Explicitly studies whether skill inequalities should be compensated while preference differences should be respected.

[Reasonable inference for my project] $z \approx (c, \ell)$; $R$ = preference ordering; $y$ reduced to scalar skill $s_i$ (budget slope); $A$ absent as separate object. The strongest connection: the normative architecture (compensation vs responsibility, impossibility, characterised leximin orderings) carries over to richer settings.

[Unclear from paper] How to extend to $W(z,R,A;y)$ with set-valued $A$; whether axioms like IIJ or IPIJ relate to this framework.

# Relation to Bargain et al. (2013)

Common ground: both reject income-only welfare and take preference heterogeneity seriously. Bargain et al. is empirical welfare measurement under heterogeneous $R$; this chapter is abstract axiomatic treatment of compensation and responsibility. Complementary rather than competitive.

# Relation to opportunities vs preferences

Directly about this distinction, but in reduced form. Preferences = responsibility; skills = compensation. Highly relevant normatively, even though the opportunity concept is thinner than feasible job sets. One of the strongest normative references for arguing that opportunity-based and preference-based inequalities should not be treated identically.

# Useful quotations / formulas

**Skill-equivalent utility:**
$$u^s(z_i, R_i) = u \iff z_i \, I_i \, \max_{R_i} B(u, (0,0))$$

**$\tilde{\ell}$-based index:**
$$u^{\tilde{\ell}}(z_i, s_i, R_i) = u \iff z_i \, I_i \, \max_{R_i} B(s_i, (\tilde{\ell}, u))$$

**Key impossibility (Theorem 10.1):** No SOF satisfies Weak Pareto + EP-Transfer + ES-Transfer.

# Suggested tags

unequal-skills, compensation, responsibility, social-ordering-functions, leximin, equal-preferences-transfer, equal-skill-transfer, skill-equivalent-leximin, egalitarian-Walrasian, axiomatic-fairness, Fleurbaey, Maniquet

# My quick takeaway

The foundational normative chapter for my JMP. Provides the impossibility results, the compensation-vs-responsibility axioms, and the characterised leximin social orderings ($R^{slex}$, $R^{sminlex}$, $R^{\tilde{\ell}EW}$) that define the normative landscape. The key limitation for my project -- scalar skills rather than set-valued opportunity objects -- is precisely the gap my framework aims to fill.
