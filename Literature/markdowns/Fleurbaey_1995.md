---
title: "Three Solutions for the Compensation Problem"
authors: [Marc Fleurbaey]
year: 1995
outlet: "Journal of Economic Theory, 65, 505--521"
country_or_context: "Theoretical (no empirical application)"
population: "N/A (abstract fair division model)"
data_period: "N/A"
shelf: "fairness / compensation / egalitarian-equivalence / conditional equality / social choice"
tags: [fairness, compensation, equal-opportunity, egalitarian-equivalence, conditional-equality, no-envy, consistency, handicaps, talents, axiomatic, social-choice, Fleurbaey]
priority: "high"
read_status: "extracted"
---

# Full citation

Fleurbaey, M. (1995). Three Solutions for the Compensation Problem. *Journal of Economic Theory*, 65, 505--521.

# One-sentence contribution

Formalises the compensation problem -- how to allocate a divisible resource among agents who differ in non-transferable talents/handicaps and in preferences -- and characterises three solutions axiomatically: conditional equality, the egalitarian-equivalent solution (Pazner-Schmeidler), and average compensation, showing that the first two form a dual pair under the consistency axiom while EREH and EWEP are fundamentally incompatible.

# Why this paper matters

This is a foundational paper in the fairness literature that directly shapes the welfare metrics used in Bargain et al. (2013) and the broader Fleurbaey-Maniquet framework. It establishes the formal tension between two ethical principles: (1) compensating fully for handicaps (EWEP: equal welfare for equal preferences) and (2) not compensating for preference differences (EREH: equal resource for equal handicap). Proposition 1 shows these are incompatible on any reasonably large domain. The paper then derives two consistent solutions -- conditional equality and egalitarian-equivalence -- that each satisfy one principle fully and a weakened version of the other. These solutions become the basis for the equivalent income welfare metrics applied to labour supply in later work.

# Core research question

What are the axiomatic foundations for fair compensation when agents differ in both non-transferable characteristics (handicaps/talents) and preferences, and which allocation rules satisfy combinations of compensation principles and consistency?

# Economic setting and context

Pure exchange economy. A total resource $\omega \in \mathbb{R}_{++}$ must be divided among $n$ agents. Each agent $i$ is characterised by:
- $y_i \in Y$: a non-transferable personal parameter (handicap or talent)
- $R_i$: strict preferences over pairs $(x_i, y_i) \in \mathbb{R}_+ \times Y$ (resource received, own handicap)

Preferences are monotone in $x_i$ and continuous. An economy is $\mathscr{E} = (y; R; \omega)$. A solution $\varphi$ maps economies to feasible allocations: $\varphi(\mathscr{E}) \in \mathbb{R}_+^n$ with $\sum \varphi_i(\mathscr{E}) = \omega$.

# Model / theoretical framework

**Two compensation axioms (Section 3):**

*Equal Resource for Equal Handicap (EREH):* If $y_i = y_j$, then $\varphi_i(\mathscr{E}) = \varphi_j(\mathscr{E})$. Agents with the same handicap get the same resource, regardless of preferences. This embodies the principle of *not compensating for preference differences*.

*Equal Welfare for Equal Preference (EWEP):* If $R_i = R_j$, then either $\varphi_i = 0$ and $(0, y_i) R_i(\varphi_j, y_j)$, or $\varphi_j = 0$ and $(0, y_j) R_j(\varphi_i, y_i)$, or both are indifferent. Agents with the same preferences reach the same welfare level. This embodies *full compensation for handicap differences*.

**Proposition 1 (Incompatibility):** There is no solution on $\mathscr{D}$ satisfying both EREH and EWEP.

**Weakened versions:** EREH* (equal resource only when all handicaps or all preferences coincide) and EWEP* (equal welfare only when all handicaps or all preferences coincide). Many solutions satisfy both simultaneously.

**Other axioms:** Anonymity, continuity, consistency (restriction to subeconomies), expansion invariance, resource monotonicity, population monotonicity, sensitiveness.

**Three solutions characterised:**

1. **$\tilde{R}$-Conditional equality (Section 5, Proposition 7):** Fix benchmark preferences $\tilde{R}$. Choose $x$ such that for all $i$, $(x_i, y_i) \, \tilde{I}(\tilde{x}, \tilde{y})$ or $x_i = 0$ and $(0, y_i) \, \tilde{R}_i(\tilde{x}, \tilde{y})$. Allocates resources to equalise welfare according to the benchmark preferences $\tilde{R}$, ignoring individual preference differences. Satisfies EREH, $\tilde{R}$-EWEP*, anonymity, continuity, consistency, expansion invariance, population monotonicity, resource monotonicity.

2. **$\tilde{y}$-Egalitarian-equivalent (Section 5, Proposition 8):** Fix benchmark handicap $\tilde{y}$. Choose $x$ such that for all $i$, $(x_i, y_i) \, I_i(\tilde{x}, \tilde{y})$ or $x_i = 0$ and $(0, y_i) \, R_i(\tilde{x}, \tilde{y})$. Each agent is indifferent between their bundle and a common reference bundle at the benchmark handicap. Satisfies EWEP, $\tilde{y}$-EREH*, anonymity, continuity, consistency, expansion invariance, population monotonicity, resource monotonicity.

   Define $\gamma(y_i, R_i) = \inf\{x_i \in \mathbb{R}_+ \mid (x_i, y_i) \, R_i(0, \tilde{y})\}$: the minimum resource needed to compensate agent $i$ for having handicap $y_i$ instead of $\tilde{y}$.

3. **Average compensation (Section 6, Proposition 10):** Each agent $i$ proposes an allocation $x^i$ that leximins welfare according to her own preferences $R_i$. The final allocation is $x = \frac{1}{n} \sum_i x^i$. Satisfies EREH, EWEP*, anonymity, continuity, resource monotonicity, but NOT consistency, expansion invariance, or population monotonicity.

**Dual characterisation (Proposition 9):** $\tilde{R}$-Conditional equality is the only consistent solution over $\mathscr{U}'$ satisfying EREH* and $\tilde{R}$-EWEP*. The $\tilde{y}$-Egalitarian-equivalent is the only consistent solution over $\mathscr{U}''$ satisfying $\tilde{y}$-EREH* and EWEP*.

# Key objects

- **EREH / EWEP:** The two fundamental compensation principles (responsibility vs. compensation)
- **Consistency:** If the solution is applied to a subeconomy (subset of agents with their allocation as total resource), the same allocation obtains
- **$\gamma(y_i, R_i)$:** Compensation cost function -- minimum resource to bring agent $i$ with handicap $y_i$ to the welfare of having benchmark handicap $\tilde{y}$ with zero resource
- **Conditional equality allocation:** Resource that equalises welfare under benchmark preferences $\tilde{R}$
- **Egalitarian-equivalent allocation:** Resource that makes each agent indifferent to a common reference bundle $(\ \tilde{x}, \tilde{y})$

# Data

No data. Purely axiomatic/theoretical.

# Identification logic

Not applicable (axiomatic characterisation). The results are logical derivations from axioms.

# Estimation / empirical strategy

Not applicable.

# Treatment of preferences

Preferences are the central object. The key ethical distinction is between handicaps $y$ (which should be compensated) and preferences $R$ (which should not be compensated, or at least not fully). The paper assumes preferences are observable and ordinal -- no utility functions are needed. The EREH axiom ensures that preference differences do not generate resource differences; the EWEP axiom ensures that handicap differences do not generate welfare differences.

The conditional equality solution uses benchmark preferences $\tilde{R}$ to evaluate handicaps, ignoring individual preferences. The egalitarian-equivalent solution respects individual preferences but uses a benchmark handicap $\tilde{y}$.

# Treatment of opportunities / constraints

Opportunities are implicitly modelled through the handicap parameter $y$. A worse handicap means fewer opportunities (in the sense that more resource $x$ is needed to reach any given welfare level). However, the model does not explicitly model choice sets, job availability, or labour demand. The "opportunity" is entirely captured by the handicap parameter.

# Welfare / normative object

The paper characterises fair allocation rules, not social welfare functions per se. However, the egalitarian-equivalent solution can be interpreted as maximining equivalent income: agent $i$'s equivalent income is $\tilde{x}$ such that $(x_i, y_i) \, I_i(\tilde{x}, \tilde{y})$. The leximin of $\tilde{x}$ values yields the egalitarian-equivalent allocation. This is the foundation for the equivalent income welfare metric used in Bargain et al. (2013) and Fleurbaey-Maniquet.

# Main findings

1. **Incompatibility (Proposition 1):** EREH and EWEP cannot be jointly satisfied. Full compensation for handicaps and full neutrality toward preferences are logically incompatible when both handicaps and preferences vary.

2. **Consistency implies strong structure (Propositions 2--5):** Any anonymous, consistent solution is expansion invariant (Prop. 2), regular (Prop. 3--4), and resource/population monotonic (Prop. 5). Consistency is a very powerful axiom in this model.

3. **Dual characterisation (Proposition 9):** Conditional equality is the unique consistent solution satisfying EREH* and benchmark-EWEP*. Egalitarian-equivalence is the unique consistent solution satisfying EWEP and benchmark-EREH*. They form a dual pair: one fixes benchmark preferences, the other fixes benchmark handicap.

4. **Average compensation (Propositions 10--11):** A third solution that satisfies both EREH and EWEP* simultaneously, but sacrifices consistency. When there are $\geq 3$ different handicaps, it is the unique anonymous solution satisfying sensitiveness and EWEP*.

5. **Corollary 1:** No consistent solution on $\mathscr{D}$ satisfies both EREH* and EWEP*. One must choose between full compensation and full responsibility.

# Main limitations

- One-good model (single transferable resource) -- does not directly apply to multi-dimensional allocation
- Handicaps are assumed perfectly observable and classifiable
- No production, no labour supply, no dynamic considerations
- The choice of benchmark ($\tilde{R}$ or $\tilde{y}$) is not determined by the axioms -- it requires a normative judgement
- Does not address implementation (mechanism design) or incentive compatibility
- No empirical application

# Relevance for my JMP

## possible use for framing
This paper provides the axiomatic foundations for the welfare metrics in Bargain et al. (2013). The EREH-EWEP tension is the formal expression of the responsibility-compensation trade-off: should society compensate people for their preferences (laziness?) or only for their circumstances (handicaps, limited job availability)? In the $W(z, R, A; y)$ framework, the EREH principle says that $W$ should not vary with $R$ (holding $A$ and $y$ fixed), while EWEP says $W$ should not vary with $A$ or $y$ (holding $R$ fixed). The incompatibility result means the framework must choose which principle to prioritise.

## possible use for welfare metric design
The egalitarian-equivalent solution maps directly to the equivalent income metric: agent $i$'s welfare is $\tilde{x}$ such that $U_i(x_i, y_i) = U_i(\tilde{x}, \tilde{y})$. In the labour supply context, this becomes: what income at the reference opportunity set $\tilde{A}$ and reference tax schedule $\tilde{y}$ would make agent $i$ as well off as their actual bundle $(z_i, R_i, A_i, y_i)$? This is the "equivalent income" metric.

## possible use for the R-A decomposition
The dual characterisation (Proposition 9) shows that conditional equality uses benchmark preferences (ignoring individual $R$) while egalitarian-equivalence uses benchmark handicap (respecting individual $R$). For $W(z, R, A; y)$, this suggests: conditional equality evaluates the $A$-channel (opportunity differences) holding preferences fixed, while egalitarian-equivalence evaluates the $R$-channel (preference satisfaction) at a common reference opportunity set. The RURO framework's separation of $g(h,w)$ (opportunities) from $v(C, T-h)$ (preferences) enables both evaluations.

# Research questions this paper inspires

1. How does the incompatibility between EREH and EWEP manifest in the labour supply context? If two workers have identical opportunities ($A$) but different preferences ($R$), EREH says they should receive the same resources (same tax treatment), while EWEP says they should reach the same welfare level (different tax treatment compensating for preference differences). How does this tension interact with the RURO framework's decomposition?

2. Can the benchmark handicap $\tilde{y}$ be given an empirical interpretation in the labour supply context? In the RURO framework, $\tilde{y}$ could correspond to a "reference opportunity set" $\tilde{A}$ -- e.g., the median worker's opportunity density $g(h,w)$.

3. The average compensation solution (Section 6) aggregates each agent's proposed leximin allocation. Could this be operationalised in a microsimulation context, where each individual proposes an allocation based on their own preferences?

# Challenge to this paper

The paper assumes that the boundary between handicaps $y$ (to be compensated) and preferences $R$ (not to be compensated) is clearly defined and exogenous. In the labour supply context, this boundary is contested: is low labour supply due to preferences (laziness, high value of leisure) or handicaps (lack of job opportunities, health limitations, caring responsibilities)? The RURO framework partially addresses this by structurally separating preferences $v(C, T-h)$ from opportunities $g(h,w)$, but even there, preferences may be shaped by opportunities (adaptive preferences), and opportunities may depend on preferences (self-selection into sectors).

Moreover, the one-good setting obscures the multi-dimensional nature of compensation in labour markets. An agent's "handicap" includes not just skill level but also the structure of available jobs (hours, commuting, working conditions), which cannot be captured by a single parameter $y$.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper establishes two compensation principles: EREH (no compensation for preferences) and EWEP (full compensation for handicaps). In $W(z, R, A; y)$, EREH says that $W$ should be invariant to $R$ when $A$ and $y$ are held fixed (i.e., only $A$ and $y$ matter for the allocation). EWEP says that $W$ should be invariant to $A$ and $y$ when $R$ is held fixed (i.e., preferences should be fully respected and handicaps fully compensated).

[Reasonable inference for my project] The egalitarian-equivalent solution provides the theoretical foundation for the equivalent income welfare metric. In the RURO context, agent $i$'s equivalent income would be: the income level at a reference opportunity density $\tilde{g}(h,w)$ and reference tax schedule $\tilde{y}$ that would make $i$ as well off as under actual conditions. The RURO decomposition into $v(C, T-h)$ and $g(h,w)$ makes this computation tractable.

[Unclear from paper] How the consistency axiom translates to the labour supply context. Consistency requires that if one re-solves the allocation problem for a subset of agents, the solution should not change. In a tax-benefit system, this would require that the optimal tax for a subpopulation equals the restriction of the optimal tax for the full population -- a very strong requirement.

The paper is closest to: **the axiomatic foundations of fair compensation** and **the egalitarian-equivalent / conditional equality welfare metrics**.

# Relation to Bargain et al. (2013)

Bargain et al. (2013) directly implement the egalitarian-equivalent and conditional equality solutions from this paper in a labour supply context. Their three welfare metrics -- $W^{eq}$ (equivalent income with reference wage), $W^{ce}$ (conditional equality with reference preferences), and $W^{rent}$ (rent from working) -- correspond to: (1) the $\tilde{y}$-egalitarian-equivalent solution (fixing reference wage = benchmark handicap), (2) the $\tilde{R}$-conditional equality solution (fixing benchmark preferences), and (3) a special case of (1) with reference preferences set to disliking work. This paper provides the axiomatic justification for why these are the "right" welfare metrics.

# Relation to opportunities vs preferences

This is the foundational paper for the opportunities-preferences distinction in welfare analysis. The handicap $y$ maps to opportunities ($A$ in the JMP framework): non-transferable characteristics that affect what an agent can achieve. Preferences $R$ map to $R$ in the framework. The EREH principle says: do not compensate for $R$-differences. The EWEP principle says: fully compensate for $A$-differences. The incompatibility result (Proposition 1) means that no allocation rule can simultaneously achieve both goals, forcing a choice between the conditional equality approach (prioritise EREH, use benchmark $\tilde{R}$) and the egalitarian-equivalent approach (prioritise EWEP, use benchmark $\tilde{A}$).

# Useful quotations / formulas

**On the compensation problem (p. 506):**
"In this paper, I will not address the difficult question of how the factors should be sorted out and will examine only the methods by which the partial compensation can be performed."

**EREH (p. 509):**
"If the compensation is made only for handicaps of the agents, then two agents with identical handicaps should receive the same amount of resource."

**EWEP (p. 509):**
"If full compensation is performed, then two agents who differ only in their handicaps should obtain the same welfare, or at least, the allocation should maximin their welfare."

**Incompatibility (Proposition 1, p. 509):**
"There is no solution on $\mathscr{D}$ satisfying EREH and EWEP."

**Egalitarian-equivalent (p. 513):**
Define $\gamma(y_i, R_i) = \inf\{x_i \in \mathbb{R}_+ \mid (x_i, y_i) \, R_i(0, \tilde{y})\}$ -- the minimum resource to compensate for handicap $y_i$ relative to benchmark $\tilde{y}$.

**On the dual characterisation (p. 514):**
"These two solutions have a symmetric behavior as regards the compensation properties [...] and this is the main result of this paper, they can be dually characterized by this particular feature."

# Suggested tags

fairness, compensation, egalitarian-equivalence, conditional-equality, EREH, EWEP, handicaps, talents, preferences, responsibility, axiomatic, consistency, no-envy, Pazner-Schmeidler, benchmark-preferences, benchmark-handicap, equivalent-income, leximin, social-choice

# My quick takeaway

This paper is the axiomatic bedrock for the welfare metrics I need. The key result -- EREH and EWEP are incompatible -- means that no welfare metric can simultaneously be fully neutral to preferences and fully compensatory for handicaps. The two consistent solutions (conditional equality and egalitarian-equivalence) form a dual pair and correspond exactly to the welfare metrics in Bargain et al. (2013). For my JMP, the egalitarian-equivalent solution is the most natural fit: it respects individual preferences ($R$) and compensates for opportunity differences ($A$) by evaluating everyone at a benchmark opportunity set $\tilde{A}$. The RURO framework's structural separation of $v(C, T-h)$ from $g(h,w)$ provides the machinery to compute this metric. The paper's limitation -- single-good, no labour market -- is exactly what Bargain et al. and my JMP address by embedding these principles in a structural labour supply model.
