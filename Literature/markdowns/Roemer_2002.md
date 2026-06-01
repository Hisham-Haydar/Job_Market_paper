---
title: "Equality of opportunity: A progress report"
authors: [John E. Roemer]
year: 2002
outlet: "Social Choice and Welfare, 19(2), 455--471"
country_or_context: "General normative framework; empirical illustrations for US and 10--11 OECD countries"
population: "Abstract populations partitioned into types; empirical: young men (US), national populations (OECD fiscal)"
data_period: "US: late 1960s (age 16) to ~1980s (age 30); OECD fiscal: various years"
shelf: "equality of opportunity / responsibility / circumstances / effort / non-welfarist / optimal policy"
tags: [equality-of-opportunity, circumstances-effort, responsibility, non-welfarist, educational-finance, tax-transfer, types, quantile-effort, Roemer, compensation, EOp]
priority: "high"
read_status: "extracted"
---

# Full citation

Roemer, J. E. (2002). Equality of opportunity: A progress report. *Social Choice and Welfare*, 19(2), 455--471.

# One-sentence contribution

Formalises equality of opportunity as equalisation of outcomes across circumstance-defined types at fixed effort ranks, develops a non-welfarist policy objective based on that idea, and illustrates it with applications to US educational finance (optimal compensatory spending ratios of 5:1) and cross-country fiscal systems (Nordic countries "overtax" relative to the EOp optimum).

# Why this paper matters

This is one of the clearest statements of Roemer's responsibility-sensitive equality-of-opportunity programme in a form directly usable for policy analysis. For my JMP, it provides the ethical template for distinguishing compensable disadvantage (circumstances) from responsible variation (effort), even though it does not model opportunities as explicit feasible job sets.

# Core research question

How should equality of opportunity be formalised when society wants to compensate for circumstances and hold individuals responsible for effort, and what policy recommendations follow?

# Model / theoretical framework

**Normative policy framework:** Outcomes $u(C, e, \varphi)$ where $C$ = circumstances, $e$ = effort, $\varphi$ = policy. Population partitioned into types (homogeneous in $C$). Morally relevant effort measured by rank $\pi$ in type-specific effort distribution $F^t$ (not absolute effort levels).

**Equal-opportunity objective (eq. 2.2):**
$$\varphi^{EOp} = \arg\max_\varphi \int_0^1 \min_t v^t(\pi, \varphi) \, d\pi$$

Maximise the integral of the lower envelope of type-specific outcome profiles across effort quantiles. Egalitarian across types at fixed effort rank; permissive across differential effort.

**Computational shortcut (Section 3):** Under three assumptions (effort = rank, effort = residual, more effort → higher outcomes), the EOp policy can be computed from outcome distributions by type without observing effort directly.

# Key objects

- **Types:** Groups defined by observed circumstances (parental education, race, IQ).
- **Effort quantile $\pi$:** Rank within the type-specific effort distribution. Two individuals at the same $\pi$ in different types are treated as having exerted the same morally relevant effort.
- **$v^t(\pi, \varphi)$:** Outcome of type-$t$ individual at effort quantile $\pi$ under policy $\varphi$.
- **US education result (Table 1):** Optimal EOp allocation: ~$5,360/pupil for most disadvantaged type vs $1,110 for most advantaged (5:1 ratio), yielding 2.6% higher average wages than equal spending.
- **OECD fiscal result (Table 3):** Denmark, Norway, Sweden, Netherlands, Germany "overtax" relative to EOp optimum; Italy, US, Britain "undertax."

# Data

US: National Longitudinal Study of Young Men (age 16 in late 1960s, wages at 30). OECD fiscal: panel data for 11 countries using prefisc/postfisc income by parental-education types.

# Treatment of preferences

Preferences enter through the ethical distinction between responsibility and circumstance. Roemer argues that beliefs and preferences within a type are partly shaped by circumstances, which is why absolute effort is rejected and rank-based effort adopted. Not a structural treatment of heterogeneous preferences.

# Treatment of opportunities / constraints

Opportunities represented through circumstance-defined types and type-specific outcome distributions, NOT through explicit feasible job sets, latent offers, or demand-side constraints. No $A_i$ object. Useful for normative decomposition (circumstances vs effort) but not for structural separation of preferences from opportunity sets.

# Welfare / normative object

Explicitly non-welfarist. The EOp objective depends on the distribution of outcomes by type and effort rank, not only on outcome levels. This distinguishes it from utilitarianism (which is outcome-level-only) and standard Rawlsianism. The "equalisandum" $u$ can be income, wages, life expectancy -- not necessarily utility.

# Main findings

1. **Effort should be measured by rank:** Absolute effort is partly a characteristic of type; morally relevant effort = quantile within type-specific distribution.

2. **US education:** EOp policy assigns 5:1 spending ratio to most vs least disadvantaged type; SES-only EOp does little for racial inequality (blacks: 38.1% → 35.3% of bottom wage quintile). Adding race to type definition produces much stronger compensation.

3. **OECD fiscal:** Nordic countries more than compensate for parental-education disadvantage; Italy, US, Britain undertax relative to EOp.

4. **Adding IQ as circumstance:** Netherlands no longer overtaxes; Denmark and Sweden still do.

5. **Conservative bias:** Effort-as-residual necessarily misattributes some unmodelled circumstances to effort.

# Main limitations

- Effort defined as residual: misattributes unobserved circumstances to effort.
- Coarse circumstance partitions (parental education, race, IQ in few categories).
- Opportunities not modelled as actual feasible sets; no job menus, wage-offer distributions, or opportunity correspondences.
- Fiscal applications restricted to affine tax systems; richer policy space might change conclusions.

# Relevance for my JMP

## possible use for normative framing
Extremely useful. Provides the clearest formulation of the responsibility-sensitive intuition: decompose outcome inequality into compensable (circumstances) and responsible (effort) components before evaluating welfare. Directly positions my JMP's normative motivation.

## possible use for the effort-rank concept
The insight that effort should be compared by rank within type -- because the distribution of effort is itself partly circumstance-determined -- is directly relevant if my framework needs to separate responsible from non-responsible variation.

## possible use for identifying limitations of circumstance-based approaches
Roemer's own acknowledgement that effort-as-residual is "conservative" motivates my structural approach: by modelling opportunity sets $A_i$ explicitly (via RURO), I can capture demand-side constraints that circumstance partitions miss.

# Research questions this paper inspires

1. How should Roemer's circumstance-effort decomposition be reformulated when individuals face heterogeneous feasible job sets $A_i$?

2. How much of measured "effort" disappears once one models unobserved opportunity constraints explicitly rather than treating them as residuals?

# Challenge to this paper

The framework operationalises responsibility by rank within type-specific residual outcome distributions, but it does not model whether observed low outcomes arise from effort, taste, luck, or lack of feasible opportunities. In the RURO framework, a worker with "high effort" (high rank within type) may still have poor outcomes because her opportunity set $A_i$ contains only low-quality jobs. Roemer's approach would attribute this to "effort" (since it is within-type variation), missing the demand-side constraint entirely.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] Distinguishes outcomes, circumstances, effort, and policy. Central ethical claim: equalise outcomes across types at fixed effort ranks.

[Reasonable inference for my project] Provides the ethical template for distinguishing compensable from responsible heterogeneity. In my notation, most naturally related to the distinction between $R$-like and $A$-like sources of inequality, though Roemer does not formulate it that way.

[Unclear from paper] How the effort-rank method should be modified when the relevant disadvantage is person-specific feasible-job-set restriction, not only circumstance.

# Relation to Bargain et al. (2013)

Indirect. Roemer provides a non-welfarist, responsibility-sensitive normative criterion; Bargain et al. provide structural welfare analysis using equivalent income. Roemer is the normative benchmark; Bargain et al. the structural implementation. My JMP aims to bridge both.

# Relation to opportunities vs preferences

Stronger on circumstances vs effort than on opportunities vs preferences. Does not structurally model preferences and opportunities as separate objects. Best read as a normative precursor: provides the ethical template but not the positive labour-market structure needed to distinguish preferences from actual opportunity sets.

# Useful quotations / formulas

**Equal-opportunity objective (eq. 2.2, p. 459):**
$$\varphi^{EOp} = \arg\max_\varphi \int_0^1 \min_t v^t(\pi, \varphi) \, d\pi$$

**On effort comparability (pp. 458--459):**
Morally relevant effort = quantile rank $\pi$ within the type-specific distribution $F^t$, not absolute effort.

**On conservative bias (pp. 462--463):**
Effort-as-residual is "conservative" because it attributes to effort much that may belong to unmodelled circumstances.

# Suggested tags

equality-of-opportunity, Roemer-EOp, circumstances-effort, responsibility, non-welfarist, rank-based-effort, educational-finance, fiscal-equality-of-opportunity, type-based-compensation, parental-background

# My quick takeaway

A core normative paper providing the ethical template for responsibility-sensitive welfare evaluation: compensate for circumstances, respect effort, compare effort by rank within type. For my JMP, it supplies the normative motivation while highlighting the limitation that my RURO framework addresses: Roemer's approach lacks an explicit opportunity-set object $A_i$, so it cannot distinguish low outcomes due to lack of effort from low outcomes due to constrained opportunity sets.
