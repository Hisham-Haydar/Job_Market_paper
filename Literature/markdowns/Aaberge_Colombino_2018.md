---
title: "Structural Labour Supply Models and Microsimulation"
authors: [Rolf Aaberge, Ugo Colombino]
year: 2018
outlet: "International Journal of Microsimulation, 11(1), 162--197"
country_or_context: "General (with examples from Italy, Norway, Sweden)"
population: "General survey of methods"
data_period: "N/A (survey paper)"
shelf: "structural labour supply / discrete choice / microsimulation / survey"
tags: [RURO, discrete-choice, van-Soest, microsimulation, optimal-taxation, common-welfare-function, King-1983, Fleurbaey, social-welfare, survey, labour-supply-elasticities, Norway, Italy]
priority: "high"
read_status: "extracted"
---

# Full citation

Aaberge, R., & Colombino, U. (2018). Structural Labour Supply Models and Microsimulation. *International Journal of Microsimulation*, 11(1), 162--197.

# One-sentence contribution

Provides a comprehensive survey of structural labour supply modelling approaches — the Discrete Choice (DC/van Soest) model and the Random Utility Random Opportunities (RURO) model — and their integration with microsimulation for policy evaluation, including the social evaluation of reforms via individual welfare functions (common utility and preference-respecting approaches) and optimal taxation.

# Why this paper matters

This is the most complete methodological survey of the DC and RURO approaches to labour supply modelling, written by two of the principal architects of the RURO framework. It synthesizes two decades of research into a single reference, covering: (i) the relationship between DC and RURO models, (ii) the representation of opportunity sets, (iii) simulation procedures, (iv) social evaluation of policy reforms (common welfare function vs. preference-respecting approaches), and (v) optimal taxation via microsimulation. It explicitly discusses the Fleurbaey-Maniquet alternative and acknowledges the limitation of the common welfare function approach.

# Core research question

How should structural labour supply models be specified, estimated, and used for policy simulation and welfare evaluation? What are the relative advantages of the DC and RURO approaches, and how should simulation results be translated into social welfare assessments?

# Economic setting and context

Survey paper drawing on applications from Italy (1987, 1993 SHIW), Norway (1979--2011 tax data), and Sweden (1981 HINK). The paper discusses the evolution of labour supply elasticities over time (1979--2011 for Norway) and the application of microsimulation to tax reforms including flat taxes, NIT, basic income, and in-work tax credits.

# Model / theoretical framework

The paper presents two modelling approaches:

**1. Discrete Choice (DC) model (van Soest 1995):**
$$P(h) = \frac{\exp\{v(f(wh, I), h)\}}{\sum_{y=0}^{T} \exp\{v(f(wy, I), y)\}}$$
with "dummies refinement" adding $\gamma_\ell \mathbf{1}(h \in S_\ell)$ terms to account for job availability and fixed costs.

**2. RURO model (Dagsvik 1994; Aaberge et al. 1995):**
$$\varphi(w, h) = \frac{\exp\{v(f(wh, I), h)\} \cdot p(w, h)}{\sum_{(x,y) \in B} \exp\{v(f(xy, I), y)\} \cdot p(x, y)}$$
where $p(w, h)$ is the opportunity density, factorized as $p(w, h) = p_1 g_1(h) g_2(w)$ for $h > 0$ and $1 - p_1$ for $h = 0$.

**Key relationship:** The DC model is a special case of RURO when $w$ is fixed (household-specific) and $p(x, y)$ is constant. The RURO "dummies" ($\gamma_0, \gamma_\ell$) have a structural interpretation: $\gamma_0 = \ln J + A_0$ and $\gamma_\ell = \ln(J_\ell / J) + A_\ell$, where $J$ is the number of market alternatives and $J_\ell$ the number in subset $S_\ell$.

**Framework:** Methodological survey covering both positive (estimation, simulation) and normative (welfare evaluation, optimal taxation) aspects.

# Key objects

- **Opportunity density** $p(w, h) = p_1 g_1(h) g_2(w)$: the core RURO object distinguishing it from DC. $p_1$ is the density of market alternatives, $g_1(h)$ has peaks at part-time and full-time, $g_2(w)$ is log-normal.
- **Common welfare function** $V(y, h) = \gamma_2(y^{\gamma_1}-1)/\gamma_1 + \gamma_4(L^{\gamma_3}-1)/\gamma_3$: used for interpersonal comparability in welfare evaluation. Same functional form as individual utility but with homogeneous parameters estimated to capture the "social planner's preferences."
- **King (1983) equivalent income** $V^*(w_R, \omega_i, Z_R) = V^*(w_i, I_i, Z_i)$: money-metric welfare index using reference characteristics $Z_R$ and reference budget $(w_R, I_R)$.
- **Rank-dependent SWF** $W_k^* = \int_0^1 p_k(t) F^{-1}(t) dt$: the family of social welfare functions used for evaluating distributions of individual welfare.
- **Optimal tax problem (eq. 16):** $\max_\vartheta W(U_1, \ldots, U_N)$ s.t. incentive compatibility and revenue constraint — solved computationally by iterative microsimulation.

# Data

No new data — the paper surveys results from multiple studies. Key datasets referenced: Italian SHIW (1987, 1993), Norwegian administrative tax data (1979, 1986, 1994, 2006, 2011), Swedish HINK (1981).

# Identification logic

The paper discusses identification at a general level:
- **DC models:** Preferences identified from tax-function non-linearities. The $\varepsilon$ term has dual interpretations: (i) unobserved job attributes (RUM/McFadden) or (ii) optimization error. These have different implications for simulation and welfare evaluation.
- **RURO models:** Additionally identifies opportunity density parameters from hours/wage distributions. The structural interpretation of the "dummies" coefficients enables equilibrium simulation.
- **Structural vs. reduced form:** The paper argues strongly for structural models for *ex-ante* policy evaluation, citing Marschak (1953) and Lucas (1976). It notes that "data, by themselves, whether experimental or quasi-experimental or non-experimental, are not sufficient to identify policy-invariant parameters" (p. 179).

# Estimation / empirical strategy

Survey of estimation methods:
- Maximum likelihood with McFadden (1978) procedure (random sampling from the opportunity set)
- Simultaneous vs. two-step wage estimation
- Ben-Akiva and Lerman (1985) importance sampling for RURO
- Mixed Logit / random parameters for relaxing IIA

# Treatment of preferences

The paper discusses two interpretations of the random component $\varepsilon$:
1. **RUM interpretation:** $\varepsilon$ captures unobserved utility from job attributes — the household truly maximizes $v(f(wh, I), h) + \varepsilon$. This is the natural RURO interpretation.
2. **Optimization error:** $\varepsilon$ is a mistake — the true utility is $v(f(wh, I), h)$ but the household is displaced. More common in DC models.

The interpretation matters for welfare evaluation: under (1), welfare includes $\varepsilon$; under (2), welfare is just $v(\cdot)$. The paper notes that the DC literature tends toward interpretation (2), focusing on flexible specification of $v(\cdot)$ and quasi-concavity.

Preference heterogeneity: through observed demographics (taste-shifters) and unobserved random parameters (Mixed Logit). The paper notes the trend toward random coefficients to relax IIA.

# Treatment of opportunities / constraints

**Central to the paper.** The survey devotes extensive attention to the representation of the opportunity set:
- **DC models:** Opportunity set is typically fixed and imputed to all households (e.g., 6 or 24 equally-spaced hours points). The "dummies refinement" is a reduced-form way to account for job availability.
- **RURO models:** Opportunity set is explicitly modeled through $p(w, h)$ with estimated density parameters. The set is unknown to the analyst and estimated from the data. Sampling from a pre-estimated density $q(w, h)$ with importance weights $p/q$.
- **Equilibrium simulation:** In RURO, since the opportunity density represents labour demand, a reform that changes labour supply also changes the density of available jobs. Colombino (2013) proposes an iterative equilibrium procedure exploiting the structural interpretation of the dummies.
- **DC vs. RURO on opportunities:** The paper argues that RURO's structural representation of opportunities is a key advantage for policy simulation, since the "dummies" in DC are reduced-form and may not be policy-invariant.

# Welfare / normative object

The paper surveys three approaches to welfare evaluation:

**1. Common utility function (Deaton & Muellbauer 1980; Hammond 1991; Aaberge & Colombino 2013):**
$$V(y, h) = \gamma_2 \frac{y^{\gamma_1} - 1}{\gamma_1} + \gamma_4 \frac{L^{\gamma_3} - 1}{\gamma_3}$$
Estimated with the same functional form as the individual utility but homogeneous parameters. Used as input to social welfare functions. "By definition contains interpersonal comparability of both welfare levels and welfare differences" (p. 189).

**2. Preference-respecting approaches (Fleurbaey 2008; Fleurbaey & Maniquet 2006; Piacquadio 2017):**
The paper explicitly acknowledges these as "alternative and promising approaches aiming at respecting individual (consumption/leisure) preferences" (p. 190). Cites applications by Bargain et al. (2013) and Decoster & Haan (2015). Notes the limitation flagged by Decoster & Haan (2015): "the choice of a specific preference respecting welfare metric might have a significant impact on the result of the welfare evaluation" and "depending on the chosen metric, a work averse or work loving individual will be favoured" (p. 190).

**3. King (1983) equivalent income:**
$$V^*(w_R, \omega_i, Z_R) = V^*(w_i, I_i, Z_i)$$
Uses reference characteristics $Z_R$ and reference budget. Empirical applications by King (1983), Aaberge et al. (2004), Islam & Colombino (2018).

**Social welfare functions:** Both primal (Atkinson 1970, eq. 20--23) and dual (rank-dependent Weymark 1981/Yaari 1988, eq. 24--25) approaches surveyed. Also Kolm (1976) absolute inequality index (eq. 26).

# Main findings

**As a survey, the main findings are methodological:**

1. **DC is a special case of RURO** when wages are fixed and opportunity densities are uniform. The RURO provides a structural interpretation of the "dummies" that are ad hoc in the DC framework.

2. **Choice-set specification matters dramatically** for out-of-sample prediction (Aaberge, Colombino & Wennemo 2009): models with job dummies + peaks dummies + 24 sampled alternatives perform best.

3. **Norwegian elasticities have declined over time** (1979--2011): total labour supply elasticity went from positive to near zero, driven by rising female participation (less room for extensive margin response), income growth, and increased leisure valuation.

4. **Computational optimal taxation** produces different results from analytical approaches: monotonically increasing MTRs (not U-shaped), negative bottom MTR (like EITC/in-work credits), unlike Mirrlees (1971)/Saez (2001) which predict positive lump-sum transfer with high phase-out rates. The difference is attributed to the restrictive assumptions (quasi-linear preferences, no income effects, fixed elasticities, individuals not couples) required for analytical solutions.

5. **Welfare evaluation requires careful treatment of interpersonal comparability.** The common utility function provides comparability but ignores preference heterogeneity. Preference-respecting approaches (Fleurbaey) respect heterogeneity but face the "work averse vs. work loving" problem. No clear winner — the paper treats this as an open question.

# Main limitations

- As a survey, the paper does not present new empirical results.
- The discussion of welfare evaluation acknowledges the unresolved tension between the common utility approach and preference-respecting approaches but does not resolve it.
- Dynamic models (stochastic dynamic programming) and collective/bargaining models are mentioned but not developed in detail.
- Labour demand side is discussed briefly; general equilibrium effects are acknowledged as important but understudied.

# Relevance for my JMP

## possible use for framing
The paper provides the authoritative survey of the DC and RURO modelling approaches that underlie my empirical framework. It explicitly positions the RURO as the more general and structurally interpretable approach, which motivates my choice of modelling framework.

## possible use for model design
The detailed exposition of the RURO model (eqs. 4--14), including the factorization of the opportunity density, the structural interpretation of the dummies, and the equilibrium simulation procedure, provides the technical foundation for my model specification.

## possible use for welfare measurement
The paper's discussion of the common welfare function vs. preference-respecting approaches (Section 5.5.1) is directly relevant. My $W(z, R, A; y)$ framework can be seen as a response to the tension identified here: it respects individual preferences (like Fleurbaey) while also accounting for opportunity heterogeneity (like the RURO model's $p(w,h)$), combining the strengths of both approaches.

## possible use for identification
The paper's discussion of structural vs. reduced-form identification (Section 4) and the case for structural models in *ex-ante* policy evaluation provides methodological justification for my approach.

## possible use for comparative application
The evolution of Norwegian elasticities (Section 5.2) provides time-series context for the cross-sectional analysis in my framework. The finding that elasticities have declined as participation has risen suggests that the opportunity set $A$ has expanded over time (more women have market opportunities), reducing the scope for extensive-margin responses.

# Research questions this paper inspires

1. Can the tension between the common utility approach and the Fleurbaey preference-respecting approach be resolved by a framework like $W(z, R, A; y)$ that conditions welfare on both preferences and opportunities?

2. The paper notes that "depending on the chosen metric, a work averse or work loving individual will be favoured" — does the $W(z, R, A; y)$ framework resolve this by making the treatment of preferences explicit through the responsibility axiom?

3. How would optimal tax results change if the RURO model's opportunity density were allowed to respond endogenously to tax changes (general equilibrium) in the welfare evaluation?

4. The declining elasticities over time in Norway — is this driven by changes in preferences ($R$) or opportunities ($A$) or the pay schedule ($y$)?

# Challenge to this paper

The paper presents the common utility function $V(y, h)$ as the preferred approach for welfare evaluation in the Aaberge-Colombino framework, but acknowledges that it "disregards the interpersonal comparability problem" by construction (p. 189) — it achieves comparability by assuming it. The alternative preference-respecting approaches (Fleurbaey, Piacquadio) are presented as "promising" but problematic due to sensitivity to the choice of metric. However, the paper does not consider a third option: a framework that conditions welfare on both the preference type $R$ and the opportunity set $A$, using $R$ for responsibility and $A$ for compensation. This is precisely what the $W(z, R, A; y)$ framework offers, and it resolves the "work averse vs. work loving" problem by making explicit which differences in preferences the social planner should respect and which should be compensated.

# Relation to my jobs_and_wellbeing framework

[Reasonable inference for my project] The paper's Section 5.5.1 directly addresses the question my framework answers: how to construct individual welfare measures for social evaluation when households have heterogeneous preferences and face heterogeneous opportunity sets. The common utility function $V(y, h)$ is analogous to using a fixed reference preference $\bar{R}$ in my framework. The King (1983) approach (eq. 19) is closest to my Measure 5 (Reference Ability LF), using reference characteristics and reference budget. The Fleurbaey approach is closest to my Measures 3--4, which respect individual preferences while compensating for opportunity differences.

[Explicit in paper] The paper explicitly discusses Fleurbaey (2008), Fleurbaey & Maniquet (2006), and Piacquadio (2017) as alternatives to the common utility approach (p. 190). It cites Bargain et al. (2013) and Decoster & Haan (2015) as empirical applications. It explicitly states that the common utility function "is supposed to capture the preferences of the social planner, whereas the individual/household-specific utility functions solely are assumed to capture the consumption/leisure preferences of individuals/households" (p. 190).

[Unclear from paper] How the common welfare function $V(y, h)$ relates to the axioms in my framework (Full Compensation, Full Responsibility, Independence of $A$, Independence of $\mathbf{y}$). Since $V$ does not condition on $A$ or $R$, it likely satisfies a form of "neutrality" (same welfare for same $(y, h)$) but violates Full Compensation (does not account for differences in feasible sets).

The paper is closest to: **methodological foundations** for the entire RURO-based welfare evaluation pipeline that my framework builds upon.

# Relation to Bargain et al. (2013)

The paper explicitly cites Bargain et al. (2013) as an application of the Fleurbaey-Maniquet preference-respecting approach to labour supply welfare evaluation (p. 190). It positions Bargain et al. as an alternative to the Aaberge-Colombino common utility approach: Bargain et al. use heterogeneous preferences for welfare evaluation, while Aaberge-Colombino use a common $V(y, h)$. The paper notes the Decoster & Haan (2015) critique that the choice of preference-respecting metric matters — a point relevant to both Bargain et al.'s implementation and my own framework.

# Relation to opportunities vs preferences

The paper provides the clearest articulation of the RURO approach's advantage in separating preferences from opportunities. In the DC model, the "dummies" $\gamma_\ell$ are reduced-form mixtures of preference and opportunity effects. In the RURO model, the opportunity density $p(w, h)$ is structurally identified and separately estimated from preferences $v(f(wh, I), h)$. This separation is maintained through to the welfare evaluation: the common welfare function $V(y, h)$ captures a "reference preference" while the structural model's $p(w, h)$ captures opportunities. However, the welfare evaluation itself does not exploit this separation — $V(y, h)$ does not condition on $p(w, h)$. This is the gap my framework fills.

# Useful quotations / formulas

**RURO choice probability (eq. 6):**
$$\varphi(w, h) = \frac{\exp\{v(f(wh, I), h)\} \cdot p(w, h)}{\sum_{(x,y) \in B} \exp\{v(f(xy, I), y)\} \cdot p(x, y)}$$

**Common welfare function (eq. 17):**
$$V(y, h) = \gamma_2 \left(\frac{y^{\gamma_1} - 1}{\gamma_1}\right) + \gamma_4 \left(\frac{L^{\gamma_3} - 1}{\gamma_3}\right)$$

**King (1983) equivalent income (eq. 19):**
$$V^*(w_R, \omega_i, Z_R) = V^*(w_i, I_i, Z_i)$$

**Optimal taxation problem (eq. 16):**
$$\max_\vartheta W(U_1(c_1, h_1, j_1), \ldots, U_N(c_N, h_N, j_N))$$
s.t. $(c_n, h_n, j_n) = \arg\max U_n$ s.t. $c = f(wh, I_n; \vartheta)$ and $\sum(w_n h_n + I_n - f(\cdot)) \geq R$.

**On the case for structural models (p. 179):**
"The answer to question (i) is negative: *ex-ante* evaluation requires a structural model, whether parametric or non-parametric, based on utility maximization or not, explicit or implicit, estimated on observational or (quasi-) experimental data, etc."

**On preference-respecting welfare (p. 190):**
"The choice of a specific preference respecting welfare metric might have a significant impact on the result of the welfare evaluation, and moreover shows to depend on the degree of emphasis the welfare metric places on willingness-to-work."

# Suggested tags

RURO, discrete-choice, van-Soest, microsimulation, survey, optimal-taxation, common-welfare-function, King-1983, Fleurbaey, preference-respecting, social-welfare, rank-dependent-SWF, Atkinson, labour-supply-elasticities, equilibrium-simulation, structural-estimation

# My quick takeaway

This is the definitive survey of the RURO/DC labour supply modelling literature and its applications to microsimulation, welfare evaluation, and optimal taxation. For my JMP, its main value is: (i) it establishes the RURO as the state-of-the-art approach for structural labour supply modelling, providing the positive model for my framework; (ii) it explicitly identifies the unresolved tension between the common utility function ($V(y, h)$, interpersonally comparable but ignoring preference heterogeneity) and the Fleurbaey preference-respecting approach (respecting preferences but sensitive to the choice of metric) — this is precisely the tension my $W(z, R, A; y)$ framework resolves; (iii) it provides the computational optimal taxation framework (eq. 16) that I can use to find optimal taxes under my welfare criterion. The paper's honest acknowledgment that "no clear winner" exists between the common utility and preference-respecting approaches motivates my contribution.
