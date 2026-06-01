---
title: "Microsimulation as a tool for evaluating redistribution policies"
authors: [François Bourguignon, Amedeo Spadaro]
year: 2006
outlet: "Journal of Economic Inequality, 4, 77--106"
country_or_context: "General / cross-country (France, UK, Brazil examples)"
population: "General (households, taxpayers)"
data_period: "N/A (methodological survey)"
shelf: "microsimulation / methodology / tax-benefit / optimal taxation / welfare"
tags: [microsimulation, arithmetical-MSM, behavioural-MSM, discrete-choice, continuous-labour-supply, tax-benefit, envelope-theorem, money-metric, social-welfare-function, optimal-taxation, inverse-problem, EUROMOD, TAXBEN, micro-macro, dynamics, methodology, survey]
priority: "high"
read_status: "extracted"
---

# Full citation

Bourguignon, F., & Spadaro, A. (2006). Microsimulation as a tool for evaluating redistribution policies. *Journal of Economic Inequality*, 4, 77--106.

# One-sentence contribution

Provides a unified methodological survey of microsimulation models (MSMs) for evaluating redistribution policies, distinguishing arithmetical MSMs (which assume fixed behaviour and are justified by the envelope theorem) from behavioural MSMs (which model labour supply responses via continuous or discrete-choice frameworks), and shows how both can be embedded in social welfare analysis using money-metric utility and the inverse optimal taxation problem.

# Why this paper matters

This is the definitive methodological reference for the microsimulation approach to tax-benefit policy evaluation. It clarifies the theoretical foundations (when is ignoring behavioural responses justified?), lays out the taxonomy of approaches (arithmetical vs. behavioural, continuous vs. discrete-choice, static vs. dynamic), and connects microsimulation to normative economics (social welfare functions, money-metric utility, optimal taxation). For the structural labour supply literature, it provides the clearest exposition of how discrete-choice models (Van Soest 1995) fit into the broader MSM toolkit and why they dominate continuous models in practice.

# Core research question

What are the methodological foundations, capabilities, and limitations of microsimulation models for evaluating redistribution policies?

# Economic setting and context

General methodological paper, not tied to a specific country or time period. Uses examples from France, UK, and Brazil (Bolsa Escola) to illustrate applications. Written at a time when MSMs were becoming standard tools for policy evaluation in OECD countries (EUROMOD for the EU, TAXBEN for the UK, various national models).

# Model / theoretical framework

The paper presents a hierarchy of MSM approaches:

**1. Arithmetical MSMs (Section 3):** Compute the mechanical effect of a tax-benefit reform on each household's disposable income, holding behaviour fixed. Formally:

$$y_i(T') - y_i(T)$$

where $y_i(T)$ is disposable income under tax-benefit schedule $T$. Justified by the envelope theorem: if $x_i^*$ maximises utility, then for a small reform $dT$:

$$dV_i = \lambda_i [dy_i^0 - dT(x_i^*)] \quad \text{(eq. 2)}$$

where $dy_i^0$ is exogenous income change and $\lambda_i$ is the marginal utility of income. The behavioural response has only second-order welfare effects because $x_i^*$ is already optimal. This justification fails for: (i) large (non-marginal) reforms, (ii) fiscal cost estimation (where the behavioural response has first-order effects on revenue), and (iii) agents not at interior optima.

**2. Behavioural MSMs -- continuous (Section 4.2):** Labour supply $h_i^*$ derived from first-order condition of utility maximisation subject to a piecewise-linear budget constraint (Burtless & Hausman 1978):

$$V(w_i, m_i; \alpha_i) = \max_h U(c, h; \alpha_i) \quad \text{s.t.} \quad c = w_i h + m_i - T(w_i h + m_i) \quad \text{(eq. 7)}$$

where $\alpha_i$ are preference parameters, $w_i$ is wage, $m_i$ is non-labour income. Reforms change the budget constraint, inducing new optimal hours $h_i^{*'}$. Estimation requires Hausman-type methods for piecewise-linear budget constraints (eq. 8--11).

**3. Behavioural MSMs -- discrete choice (Section 4.3):** Individual chooses among $J$ hours categories. Utility at hours point $j$:

$$U_{ij} = V(w_i, H_j, m_i; \alpha_i) + \varepsilon_{ij} \quad \text{(eq. 12)}$$

Choice probability (conditional logit):

$$P_{ij} = \frac{\exp V_{ij}}{\sum_k \exp V_{ik}} \quad \text{(eq. 13)}$$

Aggregate labour supply:

$$\sum_i \bar{h}_i = \sum_i \sum_j H_j P_{ij} \quad \text{(eq. 14)}$$

The paper notes that discrete-choice models are more flexible because they avoid the "virtual wage" problem of the Hausman approach and handle non-convex budget constraints naturally.

**4. Social welfare analysis (Section 4.5):** Money-metric utility (King 1983):

$$V(p, w_i, m_i; \alpha_i) = V(p^R, w_i^R, \mu_i; \alpha_i) \quad \text{(eq. 16)}$$

where $\mu_i$ is the money-metric (income level at reference prices $(p^R, w^R)$ yielding same utility). Social welfare:

$$\mathcal{W} = W(\mu_1, \ldots, \mu_N) \quad \text{(eq. 17)}$$

**5. Inverse optimal taxation (Section 4.5):** Given observed policy $T$ and estimated preferences $\alpha_i$, recover the implicit social welfare weights $\beta_i$ that rationalise the existing tax-benefit system as optimal. Reveals "social preferences" embedded in actual policy choices.

# Key objects

- **Envelope theorem (eq. 1--6):** Theoretical foundation for arithmetical MSMs. Welfare effect of a marginal reform = mechanical effect (first order); behavioural effect enters only at second order.
- **Money-metric utility $\mu_i$ (eq. 16):** Welfare measure that converts indirect utility into a monetary equivalent at reference prices. Corresponds to equivalent income in the Fleurbaey tradition.
- **Idiosyncratic error terms $\varepsilon_{ij}$ (eq. 12):** The unobserved heterogeneity in discrete-choice models. The paper emphasises that these are not just econometric noise -- they capture genuine heterogeneity in responses. Aggregating over many agents smooths out individual $\varepsilon$ effects but the individual welfare implications depend on where each person's $\varepsilon$ places them.
- **Inverse social welfare weights $\beta_i$:** Recovered from the first-order conditions of the social planner's problem, given observed taxes and estimated behaviour. If $\beta_i$ is non-monotone in income, the existing system is not second-best optimal.

# Data

Methodological survey; no original data analysis. References EUROMOD (EU-wide), TAXBEN (UK, IFS), SYSIFF (France), and various country-specific MSMs. Discusses data requirements: household surveys with detailed income, demographic, and labour market variables.

# Identification logic

Not applicable (methodological survey). The paper discusses identification issues in structural labour supply models: the Hausman approach requires exclusion restrictions for the wage equation; discrete-choice models require functional form assumptions (typically conditional logit); both assume the tax-benefit schedule provides exogenous variation in budget constraints.

# Estimation / empirical strategy

Survey of estimation approaches:
1. **Arithmetical:** No estimation; direct computation of $y_i(T') - y_i(T)$ using survey data and the MSM.
2. **Continuous (Hausman):** ML estimation of structural labour supply on piecewise-linear budget constraints. Requires solving for virtual wages at each segment. Sensitive to functional form and error distribution assumptions.
3. **Discrete choice (Van Soest):** Conditional logit ML. More robust to budget constraint shape. Can incorporate fixed costs, random coefficients. Dominates in recent applied work.
4. **Welfare:** Compute money-metric utility at estimated parameters. Aggregate via SWF.
5. **Inverse optimal tax:** Solve for weights $\beta_i$ that satisfy the planner's first-order conditions given observed $T$ and estimated responses.

# Treatment of preferences

Preferences enter through the utility function $U(c, h; \alpha_i)$ where $\alpha_i$ varies with demographics. The paper distinguishes:
- Observable heterogeneity (demographics entering as taste-shifters)
- Unobservable heterogeneity ($\varepsilon_{ij}$ in discrete choice, or random coefficients)

The paper notes a key methodological tension: money-metric utility $\mu_i$ depends on individual preferences $\alpha_i$, but interpersonal welfare comparisons using $\mu$ require either (i) common reference preferences or (ii) the Fleurbaey-Maniquet axiomatic framework that justifies using individual preferences. The paper does not resolve this tension but flags it as important for welfare analysis (Section 4.5).

# Treatment of opportunities / constraints

The paper discusses opportunities/constraints only indirectly:
- The **Hausman approach** assumes the worker can choose any hours level on the budget constraint (no demand-side constraints).
- The **discrete-choice approach** restricts hours to a finite set $\{H_1, \ldots, H_J\}$, which can be interpreted as reflecting demand-side hours restrictions (Van Soest 1995) or as a computational simplification.
- The paper mentions "rationing on the labor market" (p. 91) as a limitation of behavioural MSMs: "important practical issues relating to these models are being neglected: for instance, rationing on the labor market, tax evasion, cross-effect of various taxes, non-take-up of benefits."
- No explicit modelling of the opportunity set or distinction between voluntary and involuntary non-participation.

# Welfare / normative object

Money-metric utility $\mu_i$ (King 1983), defined implicitly by eq. 16. Social welfare $\mathcal{W} = W(\mu_1, \ldots, \mu_N)$ where $W$ is a Bergson-Samuelson SWF. The paper presents this as the natural welfare metric for MSM-based policy evaluation but notes the interpersonal comparability issue: $\mu_i$ depends on $\alpha_i$, so comparing $\mu$ across individuals with different preferences requires normative choices about whose preferences count.

The paper also discusses the inverse optimal taxation approach: rather than imposing a SWF, recover the implicit social welfare weights from observed policy. This "reveals" the government's distributional preferences.

# Main findings

1. **Arithmetical MSMs are justified for marginal reforms and welfare analysis** by the envelope theorem, but not for fiscal cost estimation (where behavioural responses have first-order effects on revenue).

2. **Discrete-choice models dominate continuous models in practice** because they handle non-convex budget constraints, avoid the virtual wage problem, and are computationally simpler. "The discrete choice methodology, with its variants, may have today become the most common specification of labor supply" (p. 91).

3. **Three fundamental limitations of behavioural MSMs:** (i) estimation difficulty (identification, functional form sensitivity), (ii) maintained structural assumptions (preferences stable across regimes, no general equilibrium), (iii) cross-sectional income effects assumed equal to time-series effects (the $dT$ reform changes income across time, but identification comes from cross-sectional variation).

4. **Money-metric utility provides the link between MSMs and welfare analysis.** The paper shows how to compute $\mu_i$ from estimated structural models and aggregate via SWFs.

5. **The inverse optimal tax approach reveals implicit social welfare weights** embedded in actual policy. If these weights are non-monotone in income, the existing system is not second-best optimal.

6. **Extensions beyond static partial equilibrium** include: (i) micro-macro linkages (CGE models feeding back prices to MSMs), (ii) top-down approaches (aggregate constraints imposed on micro behaviour), (iii) fully integrated micro-macro models (each agent in CGE is a micro unit), (iv) dynamic MSMs (intertemporal labour supply, life-cycle).

# Main limitations

- Methodological survey, not original empirical analysis
- Does not resolve the interpersonal comparability problem for money-metric utility
- Does not discuss the RURO approach or opportunity-set modelling
- Treatment of demand-side constraints is limited to acknowledging the problem
- Does not discuss the Fleurbaey-Maniquet equivalent income approach (which resolves the reference-dependence issue axiomatically)
- Dynamic MSMs discussed briefly but not the computational/identification challenges

# Relevance for my JMP

## possible use for methodological positioning
This paper provides the definitive taxonomy into which my JMP fits. My approach is a **behavioural MSM** using the **discrete-choice** framework (Van Soest/RURO variant) with **welfare analysis** via **equivalent income** (the money-metric utility $\mu_i$ in Bourguignon-Spadaro's notation, but axiomatically grounded via Fleurbaey-Maniquet rather than King 1983). Citing this paper positions my methodology within the established MSM literature.

## possible use for the envelope theorem justification
The paper's exposition of the envelope theorem (eqs. 1--6) is directly relevant to my distinction between arithmetical and behavioural approaches. The envelope theorem says behavioural responses have only second-order welfare effects -- but this applies only to marginal reforms and only when agents are at interior optima. For the large reforms I simulate (in-work benefits, universal basic income), behavioural responses have first-order effects, justifying the full structural (RURO) model.

## possible use for the welfare analysis gap
The paper's treatment of money-metric utility (eqs. 16--17) and the SWF $\mathcal{W}$ shows the standard approach to welfare in MSMs. My JMP extends this by: (i) using equivalent income (Fleurbaey-Maniquet) rather than King's money-metric (resolving the reference-dependence problem axiomatically), and (ii) decomposing equivalent income into preference and opportunity components via the RURO framework.

## possible use for the inverse optimal tax connection
The inverse optimal taxation approach (recovering implicit social welfare weights from observed policy) is a natural complement to the forward simulation approach. My JMP does forward simulation (predict welfare effects of hypothetical reforms); the inverse approach would ask "what social welfare weights rationalise the current system?" This could be a robustness check or extension.

# Research questions this paper inspires

1. The paper notes that idiosyncratic error terms $\varepsilon_{ij}$ in discrete-choice models capture genuine heterogeneity, not just noise. In the RURO framework, part of this heterogeneity is due to differences in the opportunity set $A_i$. Can the RURO decomposition attribute some of the $\varepsilon$ variation to opportunities vs. preferences?

2. The envelope theorem justifies arithmetical MSMs for welfare but not for fiscal cost. In the RURO framework, does the envelope theorem still hold for welfare when the opportunity set is binding? If an agent is at a corner solution (rationed), the envelope theorem does not apply because the first-order condition is not satisfied -- the behavioural response to a reform has first-order welfare effects for rationed agents.

3. The paper discusses the inverse optimal tax problem: recovering social welfare weights from observed policy. Could the RURO framework's separation of preferences and opportunities sharpen the inverse problem? If the planner cares about opportunities (not just outcomes), the inverse problem has additional structure.

# Challenge to this paper

The paper's treatment of welfare analysis via money-metric utility $\mu_i$ (King 1983) is standard but problematic. Money-metric utility depends on the choice of reference prices $(p^R, w^R)$, making welfare rankings potentially reference-dependent. The Fleurbaey-Maniquet equivalent income approach resolves this by providing axiomatic foundations for the choice of reference: the reference bundle corresponds to the best opportunity set (egalitarian-equivalence) or benchmark preferences (conditional equality). The paper's framework is therefore incomplete for normative analysis -- it provides the computational machinery (MSM → $\mu_i$ → $\mathcal{W}$) but not the normative foundations for choosing the reference.

Additionally, the paper's classification of behavioural MSMs does not include models that separate preferences from opportunities. The RURO framework represents a third category beyond the continuous/discrete taxonomy: a discrete-choice model with explicit opportunity-set modelling. This category is important because it changes the welfare interpretation -- non-participation may reflect constraints, not preferences, which matters for both welfare evaluation and policy design.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper provides the computational framework for the $y \to z$ mapping: the MSM computes how tax-benefit schedule changes ($y$) affect realised bundles ($z$) either mechanically (arithmetical MSM) or through behavioural responses (behavioural MSM). The money-metric utility $\mu_i$ is essentially the $z \to W$ mapping under specific assumptions about $R$ (preferences known from estimation).

[Reasonable inference for my project] In $W(z, R, A; y)$ terms: arithmetical MSMs hold $R$ and $A$ fixed and compute $\Delta z$ from $\Delta y$. Behavioural MSMs allow $z$ to respond to $\Delta y$ through $R$ (preference-driven labour supply responses) but still hold $A$ fixed (no demand-side changes). The RURO extension allows $A$ to enter: $z$ reflects both $R$-driven choices and $A$-constrained outcomes.

[Unclear from paper] How the inverse optimal tax approach interacts with opportunity constraints. If the planner observes that some agents are rationed (involuntarily non-participating), the first-order conditions for optimal taxation are different from the unconstrained case. The inverse problem would recover different social welfare weights depending on whether rationing is accounted for.

# Relation to Bargain et al. (2013)

Bourguignon-Spadaro provide the methodological foundation that Bargain et al. (2013) build upon. Specifically: (i) the discrete-choice labour supply model (Section 4.3 here = the estimation framework in Bargain et al.), (ii) the money-metric welfare analysis (Section 4.5 here = the equivalent income computation in Bargain et al., though Bargain et al. use the Fleurbaey-Maniquet axiomatisation rather than King 1983), (iii) the MSM-based policy simulation (the pipeline of estimate → simulate → evaluate that both papers follow). Bourguignon-Spadaro is the methodological survey; Bargain et al. is the application with proper welfare foundations.

# Relation to opportunities vs preferences

The paper does not distinguish opportunities from preferences. Labour supply responses are entirely preference-driven ($\alpha_i$). The $\varepsilon_{ij}$ terms in the discrete-choice model could in principle capture opportunity variation (some jobs not available to some people), but the paper does not interpret them this way. The paper acknowledges "rationing on the labor market" (p. 91) as a limitation but does not discuss how to model it. The RURO framework fills this gap by introducing the opportunity density $g(h, w)$ alongside preferences.

# Useful quotations / formulas

**On the envelope theorem justification for arithmetical MSMs (p. 82):**
"The reason why the welfare cost or gain associated with a marginal change in a price (or tax) affecting an optimizing individual only depends on the change in disposable income net of the tax change is the envelope theorem."

**On discrete-choice dominance (p. 91):**
"The discrete choice methodology, with its variants, may have today become the most common specification of labor supply."

**On the idiosyncratic terms (p. 92):**
"Strictly speaking, each individual has a unique optimum. In effect, it is only when aggregating over a large number of agents that the expected value of $\varepsilon_i$ can be equated with zero."

**On money-metric welfare (p. 95--96):**
"$\mu_i$ is the income level which, at reference prices, would give individual $i$ the same utility as observed."

**On the inverse optimal tax problem (p. 96--97):**
"Because social welfare is unobservable, one may use the information given by the set of taxes observed at a point in time along the structural model of labor supply... to identify social welfare weights... which rationalize the observed system."

**On three limitations of behavioural MSMs (p. 92):**
"First, there is an issue about the robustness of the estimations... Second, their structural nature requires particular assumptions... Third, and less obviously, the identification of structural parameters relies on the observed cross-sectional distribution of income."

# Suggested tags

microsimulation, arithmetical-MSM, behavioural-MSM, tax-benefit, envelope-theorem, money-metric, social-welfare-function, optimal-taxation, inverse-problem, discrete-choice, continuous-labour-supply, Van-Soest, Hausman, EUROMOD, TAXBEN, methodology, survey, King-1983, Bourguignon

# My quick takeaway

The definitive methodological survey of microsimulation for redistribution policy. Establishes the taxonomy (arithmetical vs. behavioural, continuous vs. discrete-choice), the theoretical foundations (envelope theorem for arithmetical; structural estimation for behavioural), and the welfare connection (money-metric utility, SWF, inverse optimal taxation). For my JMP, this paper positions the methodology: I use a behavioural MSM with discrete-choice estimation (Section 4.3), but extend it with RURO opportunity modelling and Fleurbaey-Maniquet equivalent income (rather than King's money-metric). The paper's key gap -- no distinction between voluntary and involuntary non-participation -- is exactly what the RURO framework fills.
