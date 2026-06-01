---
title: "Equality of Opportunity: Theory and Measurement"
authors: [John E. Roemer, Alain Trannoy]
year: 2016
outlet: "Journal of Economic Literature"
country_or_context: "Survey / cross-country (Europe, US, Latin America, Africa)"
population: "General population (income earners, children for health/education outcomes)"
data_period: "Survey article; references data from EU-SILC 2005, PSID 1968-2001, Swedish registers 1955-1967 cohorts, and others"
shelf: "equality_of_opportunity_theory"
tags: [equality of opportunity, fairness, responsibility, circumstances, effort, types, compensation principle, reward principle, conditional equality, egalitarian equivalence, Roemer algorithm, Fleurbaey-Maniquet, decomposition, inequality measurement, cross-country, opportunity sets, philosophy]
priority: "very high"
read_status: "extracted"
---

# Full citation

Roemer, J. E. and A. Trannoy (2016). "Equality of Opportunity: Theory and Measurement." *Journal of Economic Literature* 54(4), 1288--1332.

# One-sentence contribution

This article provides a comprehensive survey of the theory and measurement of equality of opportunity (EOp), reviewing the philosophical foundations (Rawls, Dworkin, Sen, Roemer, Fleurbaey-Maniquet), the main economic models and algorithms for opportunity-equalizing policy, and the empirical literature measuring inequality of opportunity across countries and outcomes.

# Why this paper matters

This is the foundational survey for anyone working on equality of opportunity in economics. It consolidates 40 years of philosophical and economic thought into a unified framework, distinguishing between "circumstances" (factors beyond individual control) and "effort" (factors within individual control). It articulates the two main theoretical approaches --- Roemer's "compensating outcomes" program and the Fleurbaey-Maniquet "equalizing opportunity sets" approach --- and discusses their empirical implementations. For a JMP on well-being measurement with feasible job sets, this paper provides the normative conceptual foundations for thinking about what role the opportunity set $A$ should play in welfare evaluation and when differences in outcomes should be compensated versus respected.

# Core research question

What is the content of equality of opportunity as an ethical and economic concept? How have economists modeled it, and what does the empirical evidence say about the extent of inequality of opportunity across countries and outcomes?

# Economic setting and context

The paper does not present a single economic setting but surveys the field. The philosophical context begins with Rawls (1958, 1971), who introduced primary goods and the difference principle but did not distinguish between circumstances and effort. Dworkin (1981a, 1981b) introduced the idea that equality of welfare is flawed because society should not compensate for expensive tastes --- individuals should be held responsible for their preferences. Arneson (1989) and Cohen (1989) refined the notion further. On the economic side, Roemer (1993, 1998) proposed a formal algorithm for equalizing opportunities, and Fleurbaey and Maniquet developed an axiomatic approach based on fair allocation theory (beginning in the 1990s).

# Model / theoretical framework

The paper surveys multiple model classes:

**Roemer's Baseline Model (Section 3.1):** A population is partitioned into *types* $T = \{1, 2, ..., T\}$ defined by circumstances (beyond individual control). Within each type, individuals exert *effort* $e$. The outcome is $u^t(e, \varphi)$ where $\varphi$ is the social policy. Roemer measures effort by the rank $\pi$ of an individual in the within-type effort distribution: $v^t(\pi, \varphi) = u^t(e^t(\pi), \varphi)$, where $e^t(\pi)$ is the $\pi$th quantile of effort in type $t$. The *opportunity-equalizing policy* solves:

$$\max_{\varphi \in \Phi} \int_0^1 \min_{t \in T} v^t(\pi, \varphi) \, d\pi$$

This is a maximin over the lower envelope of type-specific quantile functions.

**Van de gaer's alternative (Program 2):** $\max_{\varphi \in \Phi} \min_{t \in T} \int_0^1 v^t(\pi, \varphi) \, d\pi$, which maximizes the average outcome for the worst-off type (mean-of-mins).

**Fleurbaey-Maniquet Approach (Section 4):** This approach is rooted in fair allocation theory (envy-freeness, compensation). It proposes ordinal allocation rules. The two key principles are:
- *Principle of compensation:* Individuals with identical effort should have the same outcome regardless of circumstances.
- *Principle of natural (liberal) reward:* Individuals with identical circumstances should receive the same resource transfer regardless of effort.

These two principles are generally incompatible (Fleurbaey 2008; Fleurbaey and Peragine 2013). Two compromise solutions are:
- *Conditional equality:* Fix a reference effort $e^*$; equalize outcomes across types at $e^*$; respect natural reward everywhere. The egalitarian-equivalent approach standardizes circumstances by assigning everyone the worst-off type.
- *Egalitarian equivalence:* Fix a reference type $t^*$ (worst-off); equalize outcomes to what each individual would get at type $t^*$ with their actual effort; respect compensation everywhere.

The framework is explicitly normative. It is useful for thinking about $W(z, R, A; y)$-type objects in the following sense: circumstances map to $A$ (the feasible set) and effort maps partly to $R$ (preferences governing choices). The outcome $u^t(e, \varphi)$ can be seen as a function of the realized bundle $z$, which depends on both circumstances and effort. The policy $\varphi$ shapes the pay schedule $y$ (e.g., the tax system).

# Key objects

**Types ($T$):** Groups defined by circumstances (e.g., parental education, race, gender, social background). Circumstances are beyond individual control.

**Effort ($e$):** Actions within individual control. Measured by the rank $\pi$ in the within-type effort distribution (Roemer identification axiom: $G^t_\varphi(e^t(\pi)) := \pi$).

**Accountable effort ($e_r$):** Relative effort measured by within-type rank, which sterilizes the influence of circumstances on the level of effort.

**Quantile functions $v^t(\pi, \varphi)$:** Type-specific outcome at effort rank $\pi$ under policy $\varphi$.

**Lower envelope $\theta(\pi, \varphi) = \min_t v^t(\pi, \varphi)$:** The worst-off type's outcome at each effort level.

**Direct Unfairness (DU):** $MLD(\Phi) = \log \frac{\mu}{(\mu^1)^{f^1}(\mu^2)^{f^2}}$, measuring inequality due to unequal type-means.

**Fairness Gap (FG):** $MLD(F) - MLD(\Phi)$, measuring the gap between actual inequality and inequality in the counterfactual where all types face their type-mean.

**Human Opportunity Index ($O$):** $O = \bar{p}(1-D)$, combining the level of opportunity ($\bar{p}$) and its inequality across circumstances ($D$).

**Compensation principle:** At a given effort level, outcome differences across types should be eliminated.

**Natural reward / liberal reward principle:** Within a type, resource allocation should be independent of effort (i.e., transfers equal across individuals in same type).

# Data

This is a survey article. It references empirical work using:
- EU-SILC 2005 data for European countries
- Swedish administrative data (1955--1967 cohorts, 1,152 types)
- Norwegian register data (1967--2006)
- US Panel Study of Income Dynamics (PSID, 1968--2001)
- German GSOEP
- Italian data (Checchi and Peragine 2010)
- Latin American data (Ferreira and Gignoux 2011)
- African surveys (Cogneau and Mesple-Soms 2008)
- SHARELIFE retrospective survey for European health

# Identification logic

The paper discusses identification extensively (Section 6.2). The key challenge is distinguishing circumstances from effort. Two approaches:

**Control view:** Effort is what individuals can control; circumstances are factors outside control. Under this view, the set of actions a person can access matters.

**Preference view:** Individuals are responsible for choices flowing from their preferences. Under this view, well-informed preferences should be respected.

**Roemer Identification Axiom (RIA):** Two individuals of different types who occupy the same quantile of their type-conditional distribution are deemed to have exerted the same degree of effort. This sterilizes the influence of circumstances on raw effort levels.

Identification challenges include: omitted circumstance variables (which bias estimates downward), endogeneity of effort (especially education), the treatment of residual variance (effort or luck?), and the problem of unobservable circumstances.

# Estimation / empirical strategy

The paper surveys multiple strategies:

**Rich data (structural model):** Estimate a system of simultaneous equations --- a return equation $y_i = \mu_{y1} + \alpha_c C_i + \alpha_d D_i + \alpha_e E_i + \varepsilon_i$ and reaction equations $e_{ij} = \mu_{ej} + \beta_c C_i + \beta_d D_i + \beta_m M_i + \gamma_{cd} C_i D_i + \gamma_{md} M_i D_i + r_{ij}$. The $\alpha$ coefficients capture the direct effect of circumstances; the $\beta$ and $\gamma$ coefficients capture how circumstances and demographics mediate effort.

**Poor data (reduced form):** Estimate $y_i = \mu_{y2} + \delta_c C_i + \delta_d D_i + v_i$, where $\delta_c$ gives a lower bound of the impact of circumstances on outcomes.

**Nonparametric methods:** Kernel density estimation of type-conditional income distributions (O'Neill, Sweetman, and Van de gaer 2000), hazard-function approaches (Pistolesi 2009).

**Decomposition:** Use the general entropy family $GE^\theta(F) = \sum_t f^t (\mu^t/\mu)^\theta GE^\theta(F^t) + GE^\theta(\Phi)$, decomposing total inequality into within-type and between-type components. The ratio $GE^0(\Phi)/GE^0(F)$ gives the share of inequality due to circumstances.

# Treatment of preferences

Preferences play a dual role in the EOp framework. Under the **preference view** of responsibility (Dworkin, Fleurbaey), individuals are held responsible for choices that flow from their preferences. Preferences are therefore on the "responsibility" side, meaning welfare differences due to preference heterogeneity are morally acceptable and should not be compensated.

Under the **control view** (Roemer), what matters is whether effort is under individual control, and preferences per se are not the relevant category --- it is the degree of effort (measured by within-type rank) that matters.

The paper notes significant tension: preferences are influenced by circumstances (endogenous preference formation). Keane and Roemer (2009) discuss the cost parameter in the utility function as potentially circumstance-influenced. The paper acknowledges that "retrieving the true parameter of preferences... is perhaps the most difficult issue in econometrics" (p. 1310, citing Fleurbaey et al. 2013 and Bargain et al. 2013 for estimation of preference heterogeneity).

# Treatment of opportunities / constraints

This paper treats opportunities as a **central theoretical object** but does not model them in the structural labor supply sense (no latent jobs, no hours restrictions, no RURO model).

The paper discusses opportunity sets in the context of:
- **Sen's capability approach:** A person's capability is the set of functionings available to them. The social-choice literature proposes ranking opportunity sets in terms of freedom of choice (Pattanaik and Xu 1990; Barbera, Bossert, and Pattanaik 2004).
- **Van de gaer's equalizing opportunity sets approach:** The integral $\int_0^1 v^t(\cdot, \varphi) d\pi$ can be viewed as a measure of the degree of opportunity available to type $t$.
- **Opportunity measures in empirical work:** The "human opportunity index" of Paes de Barros et al. (2009), the ordered pair $(Y^D, \eta)$ proposed by the authors as a two-dimensional development index.

The paper **does not model demand-side labor market constraints** explicitly. It does not use latent jobs or hours restrictions. The feasible set is implicitly defined by the circumstance type: individuals of a given type face a distribution of outcomes that reflects the opportunities available to them given their circumstances.

The paper helps distinguish:
- **Preference heterogeneity vs. opportunity heterogeneity:** This is the paper's central concern. The entire EOp framework is built on separating these two sources of outcome differences. The compensation principle addresses opportunity heterogeneity; the reward principle addresses preference (effort) heterogeneity.

# Welfare / normative object

The paper is **explicitly normative**. Multiple welfare/normative objects are discussed:

1. **Roemer's social objective (Program 1):** $\max_\varphi \int_0^1 \min_t v^t(\pi, \varphi) d\pi$ --- maximin over the lower envelope of quantile functions.

2. **Van de gaer's objective (Program 2):** $\max_\varphi \min_t \int_0^1 v^t(\pi, \varphi) d\pi$ --- maximin over type-average outcomes.

3. **Conditional equality (Eq. 6):** $u^t(e^*, \varphi_t) = u^{t'}(e^*, \varphi_{t'})$ for all $t, t'$ and reference effort $e^*$.

4. **Egalitarian equivalence (Eq. 7):** Each individual's outcome equals what they would achieve at a reference (worst-off) type $t^*$ with their actual effort.

5. **Generalized ordering (Eq. 5):** $\Gamma^{(p)}(\theta) = (\int_0^1 \theta(\pi)^p d\pi)^{1/p}$, providing a family of orderings parameterized by inequality aversion $p$.

The paper is useful for thinking about:
- **Responsibility for opportunities:** The paper provides the philosophical and formal foundations for when to compensate (circumstances) and when to respect (effort/preferences).
- **Compensation for opportunities:** The compensation principle states that outcome differences across types at the same effort level should be eliminated.
- **Actual vs. reference opportunity sets:** The conditional equality and egalitarian equivalence approaches both use counterfactuals (reference effort or reference type) to compare actual situations to hypothetical ones.
- **Decomposition of inequality:** The fairness gap (FG) and direct unfairness (DU) provide decomposition tools that separate "fair" (effort-driven) from "unfair" (circumstance-driven) inequality.

# Main findings

As a survey, the paper's main findings are:

1. **Philosophical:** The EOp approach challenges pure consequentialism by requiring attention to the source (circumstances vs. effort) of inequality, not just its level. The compensation and reward principles are generally incompatible.

2. **Theoretical:** Four main allocation rules emerge from crossing priority on compensation vs. reward with natural vs. utilitarian reward: conditional equality, egalitarian equivalence, min-of-means, mean-of-mins. Each involves trade-offs.

3. **Empirical (Scandinavia):** Sweden and Norway are close to full equality of opportunity for income. The Gini coefficient for inequality of opportunity is about 0.05 in Sweden with a fine-grained typology.

4. **Empirical (US and Europe):** Germany and the US show about 30% of permanent income inequality due to circumstances. Upper bounds (Niehues and Peichl 2014) double these to 60--70% in the US.

5. **Empirical (developing countries):** Inequality of opportunity accounts for 20--35% of income inequality in Latin American countries, and potentially over 50% in African countries.

6. **Empirical (health):** Substantial inequality of opportunity in health status exists across European countries, with lifestyles playing a key role.

7. **Inequality of opportunity is positively correlated with overall inequality** across countries (correlation about 0.67).

# Main limitations

**Identification limits:** The paper emphasizes that estimates of inequality of opportunity are lower bounds because many circumstances are unobserved. The treatment of the residual (effort vs. luck vs. unobserved circumstances) is a persistent and unresolved problem.

**Treatment of opportunities:** Opportunities are discussed conceptually but not modeled with the structural precision of a labor supply model. The paper does not engage with the RURO/latent jobs framework.

**Welfare interpretation:** The incompatibility of compensation and reward principles means that any empirical implementation involves value judgments about which principle to prioritize. The paper acknowledges this openly.

**Choice-set assumptions:** The paper does not model choice sets explicitly in the labor supply sense. The "opportunities" discussed are mostly outcome distributions by type, not explicit feasible sets of jobs.

**Relevance for decomposition:** The decomposition tools (DU, FG, entropy decomposition) are well-developed but rely on type definitions that may be coarse. The paper advocates for finer typologies and richer data.

**Integration with $W(z, R, A; y)$:** The paper provides the normative foundations but does not itself produce a structural model. It would need to be combined with a structural labor supply model (like the Dagsvik job choice model) to produce a fully operational $W(z, R, A; y)$ framework.

# Relevance for my JMP

## possible use for framing

This paper is essential for the normative framing of any JMP on well-being and feasible job sets. It provides the philosophical justification for why the opportunity set $A$ should enter welfare evaluation: outcome differences due to $A$ (circumstances) should be compensated, while differences due to $R$ (preferences/effort) may be respected. The paper's distinction between "compensating outcomes" (Roemer) and "equalizing opportunity sets" (Van de gaer) maps directly onto different ways of using $A$ in a $W(z, R, A; y)$ framework.

## possible use for model design

The paper does not provide a structural model but offers key normative desiderata that any model should satisfy: the ability to separate circumstances from effort, the ability to measure outcomes at different effort levels within types, and the ability to construct counterfactual distributions. These requirements guide model design.

## possible use for identification

The Roemer Identification Axiom (rank in within-type distribution = degree of effort) is a key identification tool. The paper also discusses the structural model approach (system of return and reaction equations) and the advantages of estimating the full structural model for separating direct and indirect effects of circumstances.

## possible use for welfare measurement

The paper provides the normative foundations for any welfare measure used in a JMP: conditional equality, egalitarian equivalence, the lower envelope criterion, and the generalized ordering $\Gamma^{(p)}$. These can be adapted to the $W(z, R, A; y)$ setting.

## possible use for decomposition

The entropy decomposition into between-type and within-type inequality, the DU/FG measures, and the Shapley-value decomposition of Chantreuil and Trannoy (2013) are directly applicable tools for decomposing inequality into opportunity and preference components.

## possible use for comparative application

The paper's cross-country comparisons using the ordered pair $(Y^D, \eta)$ and the human opportunity index provide a template for cross-country or cross-region applications.

# Research questions this paper inspires

1. Can the Roemer/Van de gaer distinction between "compensating outcomes" and "equalizing opportunity sets" be operationalized within a RURO labor supply model, where the opportunity set $A$ (latent jobs) is directly estimated?

2. How would the incompatibility between the compensation principle and the natural reward principle manifest in a structural labor supply model where preferences and opportunities are separately identified?

3. Can one construct a $W(z, R, A; y)$-based welfare measure that satisfies conditional equality for a well-defined reference effort level while respecting the natural reward principle within types?

4. Does the Roemer Identification Axiom (effort = rank in within-type distribution) produce different welfare rankings than an explicit structural model of effort choice (e.g., hours of work in a labor supply model)?

# Challenge to this paper

The paper's main limitation from a labor economics perspective is that it treats the opportunity set abstractly rather than structurally. In the EOp literature, "opportunities" are defined implicitly through type-conditional outcome distributions, which conflate demand-side constraints (job availability, hours restrictions) with supply-side factors (education, health). A structural labor supply model with explicit job opportunities (as in the Dagsvik job choice model) would allow a sharper separation: circumstances affecting $A$ (the set of available jobs) can be distinguished from circumstances affecting $R$ (preferences formed under disadvantageous conditions). The paper acknowledges the importance of structural models (citing Fleurbaey and Schokkaert 2009) but does not itself pursue this direction.

# Relation to my jobs_and_wellbeing framework

This paper provides the normative architecture for a $W(z, R, A; y)$ framework. In the EOp framework, circumstances correspond to factors shaping $A$ (the feasible job set) and $y$ (wage rates, which may be circumstance-dependent), while effort corresponds to choices governed by $R$ (preferences). The compensation principle says: equalize $W$ across individuals who differ only in $A$ (holding $R$ fixed). The natural reward principle says: do not redistribute across individuals who differ only in $R$ (holding $A$ fixed). The conditional equality criterion corresponds to evaluating $W(z, \bar{R}, A; y)$ at a reference preference $\bar{R}$, which is precisely what Jacquet, Jia, and Thoresen (2026) implement as CV^circ. The egalitarian equivalence criterion corresponds to evaluating $W(z, R, \bar{A}; y)$ at a reference opportunity set $\bar{A}$. Thus the two main fairness approaches in this survey map directly onto the two natural reference-fixing operations within $W(z, R, A; y)$.

The paper is closest to **responsibility for preferences**, **compensation for opportunities**, and **reference opportunity sets**. It provides the theoretical foundations for all of these.

# Relation to Bargain et al. (2013)

The paper cites Bargain et al. (2013) in three contexts: (1) as an example of structural estimation of cross-country preference heterogeneity in the consumption-leisure trade-off (p. 1310); (2) as a key reference in the use of discrete choice labor supply models for welfare measurement (Section 4, footnote 14); (3) as an illustration that retrieving preference parameters is feasible but difficult. Bargain et al. (2013) can be seen as providing the positive (structural) counterpart to the normative framework surveyed here: Bargain et al. estimate heterogeneous preferences across countries, which the EOp framework would then use to separate the preference (responsibility) and opportunity (circumstance) components of welfare inequality.

# Relation to opportunities vs preferences

This is the paper's central theme. The entire survey is organized around the distinction between outcomes due to circumstances (opportunities) and outcomes due to effort (preferences/choices). The paper shows that: (1) the distinction is philosophically well-founded (Dworkin, Arneson, Cohen, Roemer); (2) it can be formalized through types and effort distributions; (3) the compensation and reward principles provide normative guidance but are generally incompatible; (4) empirical measurement requires structural estimation or careful reduced-form decomposition; (5) the share of inequality due to circumstances varies widely across countries and outcomes but is consistently substantial (15--50%+ of total inequality).

# Useful quotations / formulas

**Roemer's opportunity-equalizing program (Eq. 1):**
$$\max_{\varphi \in \Phi} \int_0^1 \min_{t \in T} v^t(\pi, \varphi) \, d\pi$$

**Van de gaer's program (Eq. 2):**
$$\max_{\varphi \in \Phi} \min_{t \in T} \int_0^1 v^t(\pi, \varphi) \, d\pi$$

**Lower envelope (Eq. 4):**
$$\theta(\pi, \varphi) = \min_{t \in T} v^t(\pi, \varphi)$$

**Generalized ordering (Eq. 5):**
$$\Gamma^{(p)}(\theta) = \left(\int_0^1 \theta(\pi)^p \, d\pi\right)^{1/p}$$

**Conditional equality (Eq. 6):**
$$(\forall t, t' \in T) \quad u^{t'}(e^*, \varphi_{t'}) = u^t(e^*, \varphi_t)$$

**Egalitarian equivalence (Eq. 7):**
$$u^t(e_i, \varphi_u) = u^{t^*}(e_i, \varphi_{it^*})$$

**Return equation (Eq. 8):**
$$y_i = \mu_{y1} + \alpha_c C_i + \alpha_d D_i + \alpha_e E_i + \varepsilon_i$$

**Direct Unfairness (DU) and Fairness Gap (FG):**
$$DU = MLD(\Phi) = \log \frac{\mu}{(\mu^1)^{f^1}(\mu^2)^{f^2}}$$
$$FG = MLD(F) - MLD(\Phi)$$

"Only some kinds of inequality are ethically objectionable." (p. 1288)

"The source of inequality matters, from an ethical viewpoint." (p. 1328)

"Measures of inequality as such are not terribly useful --- unless one is a simple outcome-egalitarian who views all inequality as unjust." (p. 1328)

# Suggested tags

equality of opportunity, fairness, philosophy, Rawls, Dworkin, Sen, Roemer, Fleurbaey, Maniquet, compensation principle, reward principle, conditional equality, egalitarian equivalence, types, circumstances, effort, decomposition, inequality measurement, cross-country, fairness gap, direct unfairness, opportunity sets, survey, normative economics

# My quick takeaway

This is the essential normative and conceptual reference for a $W(z, R, A; y)$ JMP. It provides the philosophical and formal foundations for why and how to separate opportunity-driven from preference-driven welfare differences. The two main approaches (Roemer's maximin over quantile functions; Fleurbaey-Maniquet's conditional equality / egalitarian equivalence) map directly onto reference-fixing operations within $W(z, R, A; y)$: fixing $R$ at a reference and letting $A$ vary (conditional equality / CV^circ), or fixing $A$ at a reference and letting $R$ vary (egalitarian equivalence / CV^pref). The paper does not itself provide a structural labor supply model, so it needs to be combined with papers like Dagsvik and Jia (2016) or Jacquet, Jia, and Thoresen (2026) for empirical implementation. The cross-country evidence on inequality of opportunity is valuable for motivating comparative applications.
