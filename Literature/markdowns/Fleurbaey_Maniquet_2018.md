---
title: "Optimal Income Taxation Theory and Principles of Fairness"
authors: [Marc Fleurbaey, Francois Maniquet]
year: 2018
outlet: "Journal of Economic Literature, 56(3), 1029--1079"
country_or_context: "Theoretical (US calibration for illustrations)"
population: "General (Mirrlees economy with heterogeneous preferences and skills)"
data_period: "N/A (theoretical; US 2013 tax for Figure 6; calibrated US economy for Figures 7--8)"
shelf: "optimal taxation / fairness / equivalent income / money-metric utility / social welfare / survey"
tags: [optimal-taxation, fairness, equivalent-income, money-metric-utility, egalitarian-equivalent, libertarian, Mirrlees, maximin, social-welfare-function, Saez-formula, income-weights, compensation, laissez-faire, responsible-preferences, survey, JEL]
priority: "high"
read_status: "extracted"
---

# Full citation

Fleurbaey, M., & Maniquet, F. (2018). Optimal Income Taxation Theory and Principles of Fairness. *Journal of Economic Literature*, 56(3), 1029--1079.

# One-sentence contribution

A comprehensive JEL survey that shows how the theory of fair allocation -- using money-metric utility indexes $m_i(\tilde{w}, z_i)$ in place of raw utilities -- can incorporate fairness principles (compensation for unequal skills, respect for individual effort, avoidance of penalizing the talented) into optimal income taxation, yielding a two-parameter family of social objectives indexed by $\lambda$ (egalitarian-equivalent vs libertarian) and $\tilde{\ell}$ (priority to work-averse vs work-loving), with practical tools for both reform evaluation (the $f$-function graphical criterion) and optimal tax computation.

# Why this paper matters

This is the definitive survey connecting fair allocation theory to optimal taxation. It demonstrates that the conventional utilitarian approach suffers from four fundamental shortcomings (no safety net, penalizes talented, violates horizontal equity through tagging, ignores responsibility) and that these can be resolved by replacing raw utilities with appropriately constructed money-metric utility indexes while retaining the social welfare function apparatus. For empirical work, the paper provides: (1) the theoretical justification for using equivalent income/wage as a welfare metric (as in Bargain et al. 2013), (2) a practical graphical tool (the $f$-function) for comparing taxes without knowing population characteristics beyond $w_{\min}$, and (3) a taxonomy of ethical choices that practitioners must make when selecting welfare indexes.

# Core research question

How can principles of fairness -- specifically the distinction between deserved and undeserved income, the importance of laissez-faire for responsible choices, and the priority given to the worst off -- be incorporated into optimal income taxation theory through the selection of appropriate utility indexes?

# Economic setting and context

The paper works within the standard Mirrlees (1971) income tax model: agents choose labour-consumption bundles $z_i = (\ell_i, c_i)$ subject to a tax schedule $T(y)$ where $y_i = w_i \ell_i$ is pre-tax income. The innovation is in the social objective: rather than using raw utility $U_i(z_i)$ in a utilitarian SWF $\sum \alpha_i U_i$, the paper replaces utilities with money-metric indexes $m_i(\tilde{w}, z_i)$ that respect individual ordinal preferences while enabling interpersonal comparisons grounded in fairness axioms. Illustrations use the 2013 US income tax schedule (Figure 6) and a calibrated US economy with 300 household types (Figures 7--8).

# Model / theoretical framework

**Mirrlees economy:** Agents have heterogeneous preferences $U_i(\ell, c)$ and productivities $w_i$. Budget constraint: $c \leq y - T(y)$ where $y = w_i \ell_i$.

**Money-metric utility (Section 5.1):**

$$m_i(\tilde{w}, z_i) = \min\{t \in \mathbb{R} \mid \exists (\ell, c) \in X,\; c = t + \tilde{w}\ell,\; U_i(\ell, c) \geq U_i(z_i)\}$$

This is the lump-sum transfer needed at reference wage $\tilde{w}$ to achieve the same satisfaction as bundle $z_i$. It converts ordinal preferences into a cardinal, interpersonally comparable index grounded in the budget set at $\tilde{w}$.

**Generalized index (Section 8):**

$$m_i(\tilde{w}_i, z_i) + \tilde{w}_i \tilde{\ell}$$

where $\tilde{w}_i = \lambda \tilde{w} + (1-\lambda) w_i$. Two key parameters:
- $\lambda = 1$ (egalitarian-equivalent): all agents evaluated at the same reference wage $\tilde{w}$; seeks to eliminate inequalities due to skills
- $\lambda = 0$ (libertarian): each agent evaluated at their own wage $w_i$; seeks equal lump-sum transfers for equally skilled agents
- $\tilde{\ell}$: reference labour level; low $\tilde{w}$ or high $\tilde{\ell}$ favours work-averse; high $\tilde{w}$ or $\tilde{\ell} = 0$ favours hardworking agents

**Four ethical choices (Section 8.1):**
1. Trust subjective utility or rely only on ordinal preferences?
2. Reduce inequalities due to skills or let individuals keep talent fruits?
3. Prioritize compensation (skill inequalities) or equal tax treatment (same-skill individuals)?
4. Pay special attention to individuals with high or low work aversion?

**Equivalent wage (Section 5.2, linking to Fleurbaey & Maniquet 2006):**

$$W_i(z_i) = \max\{w \geq 0 \mid \forall \ell,\; z_i \; R_i \; (\ell, w\ell)\}$$

The wage at which the agent, freely choosing labour, would be just as well off as at $z_i$. Used in Fleurbaey & Maniquet (2006) for the maximin social ordering.

**Key fairness axioms (from the broader literature, summarized here):**
- **Compensation:** reduce inequalities among agents with identical preferences but unequal skills
- **Laissez-faire:** do not redistribute among agents with identical skills but different preferences
- **Transfer principle:** Pigou-Dalton transfers among same-preference agents improve social welfare

# Key objects

- **$m_i(\tilde{w}, z_i)$:** Reference-wage money-metric utility (egalitarian-equivalent class)
- **$m_i(w_i, z_i)$:** Personal-wage money-metric utility (libertarian class)
- **$f(y)$ function (Section 9.1):** Piecewise linear upper bound for evaluating arbitrary taxes graphically:

$$f(y) = \begin{cases} k^* + (\lambda\tilde{w} + (1-\lambda)w_{\min})\frac{y}{w_{\min}} - \tilde{\ell} & \text{for } y \leq w_{\min} \\ k^* + (\lambda\tilde{w} + (1-\lambda)y)(1-\tilde{\ell}) & \text{for } y \geq w_{\min} \end{cases}$$

  The tax $T$ is better when the tangent intercept $k^*$ between $f$ and $y - T(y)$ is higher.

- **Optimal tax formula (Section 9.2, eq. 3, Jacquet-Lehmann):**

$$\frac{T'(y)}{1-T'(y)} = \frac{1}{\epsilon(y)} \cdot \frac{1-H(y)}{yh(y)} \left(1 - \frac{\int_y^\infty [g(z) + \eta(z)T'(z)]h(z)\,dz}{1-H(y)}\right)$$

  where $\epsilon(y)$ = elasticity, $H$/$h$ = CDF/density, $g(z)$ = marginal social value, $\eta(z)$ = income effect derivative.

- **Zero marginal rate result (Section 7):** For the maximin planner using $m_i(w_{\min}, z_i)$, the marginal tax rate is zero for all incomes below $w_{\min}$. Above $w_{\min}$, the standard Saez formula applies with zero social weights.
- **Income weights (Section 7, eq. 2):** $-\sum_I \alpha_i \frac{\partial U_i}{\partial c_i} \delta T(y_i)$ -- Saez-Stantcheva shift from weighting utilities to weighting incomes.

# Data

No primary data. Theoretical paper with calibrated illustrations:
- **Figure 6:** US 2013 income tax for a couple with two children, data from OECD Tax Benefit Calculator
- **Figures 7--8:** Calibrated US economy, 300 household types, wages lognormally distributed $(\mu, \sigma) = (2.2, 0.6)$, quasi-linear preferences $c - a_i \ell^{1+1/\varepsilon}$ with $\varepsilon = 0.5$, household minimum wage $w_{\min} = \$25,000$

# Identification logic

Not applicable (theoretical paper). The paper derives results from axioms and incentive-compatibility constraints in the Mirrlees model. The $f$-function and optimal tax formulas are analytical objects, not estimated.

# Estimation / empirical strategy

Not applicable. Calibration for illustrations uses:
1. Lognormal wage distribution matching US census quintiles
2. Preference heterogeneity ($a_i$ varies to produce 45%, 43%, 12% full-time rates across types)
3. $\varepsilon = 0.5$ for labour supply elasticity
4. Optimal piecewise linear tax computed over 16 brackets, maximum income 500

# Treatment of preferences

Preferences are taken as given individual ordinal rankings $U_i(\ell, c)$. The paper explicitly argues for using ordinal preferences over subjective utility declarations (Section 3: problems of expensive tastes, adaptation, cardinal comparability; Section 8.1.1). The money-metric utility $m_i(\tilde{w}, z_i)$ respects ordinal preferences: it is ordinally equivalent to $U_i$ for intrapersonal comparisons and provides interpersonal comparability through the reference wage $\tilde{w}$.

The paper allows heterogeneous preferences across agents, with a key distinction between:
- **Responsible preferences:** differences in tastes for leisure/consumption that are the agent's own responsibility (laissez-faire principle applies)
- **Circumstance-driven preferences:** if family background influences preferences, the agent should be assessed using "ideal" preferences free from the alleged influence (Section 5.4, but the fairness literature is reluctant to drop the Pareto principle)

The parameter $\tilde{w}$ in the money-metric utility determines how work aversion is treated: a low $\tilde{w}$ favours work-averse agents (who have lower implicit budgets), while a high $\tilde{w}$ (especially $\tilde{w} = w_{\min}$) favours hardworking agents. This is a normative choice, not an empirical one.

# Treatment of opportunities / constraints

The paper works within the standard Mirrlees framework where opportunities are characterised entirely by the wage $w_i$ and the tax schedule $T(y)$. **Demand-side constraints, job rationing, and involuntary unemployment are not modelled.** All non-employment is voluntary. The opportunity set is the budget set $\{(\ell, c) : c \leq w_i \ell - T(w_i \ell), \; 0 \leq \ell \leq 1\}$.

The paper briefly notes the importance of incorporating other dimensions: public goods (Section 5.1, where $w_i(g) = w_i h(g)$), random shocks (Section 5.5, Saez-Stantcheva luck vs desert), and dynamic contexts (Section 10). But the main analysis remains within the static, full-employment, supply-side framework.

# Welfare / normative object

The central normative object is the social welfare function applied to money-metric utility indexes:

$$\text{Maximize } W\left(m_i(\tilde{w}_i, z_i) + \tilde{w}_i \tilde{\ell}\right)_{i \in N}$$

under incentive compatibility and resource constraints. The paper focuses on the maximin (leximin) case: maximize the minimum $m_i(\tilde{w}_i, z_i) + \tilde{w}_i \tilde{\ell}$ across agents. But it also considers less extreme inequality aversion (Section 8.2, Section 9.2 simulations with different $\rho$ values for $\frac{1}{1-\rho}\sum_i u_i^{1-\rho}$).

The key innovation relative to standard utilitarianism ($\sum \alpha_i U_i$): the utility indexes $m_i$ are normatively selected to embody fairness principles, rather than being arbitrary cardinal representations of preferences.

**Section 6** proves that weighted utilitarianism ($\sum \alpha_i U_i$) cannot generally replicate the rankings of fair social orderings because: (1) weights $\alpha_i$ are allocation-specific (depend on the whole population profile), (2) they cannot be computed before identifying the optimal allocation, (3) they may not evaluate suboptimal allocations correctly. Conclusion: replacing utilities with well-being indexes is necessary; weighting alone is insufficient.

# Main findings

1. **Four shortcomings of utilitarianism (Sections 2--4):** (i) No guaranteed safety net: the utilitarian optimum may leave some agents arbitrarily poor. (ii) Penalizes the talented: agents with higher productivity may be assigned lower utility at the optimum (Mirrlees 1974). (iii) Tagging violates horizontal equity: utilitarian criterion supports discriminating by observable characteristics (Akerlof 1978) even among agents with identical preferences. (iv) Ignores responsibility: does not distinguish deserved from undeserved income components.

2. **Money-metric utility resolves these shortcomings (Section 5):** $m_i(\tilde{w}, z_i)$ achieves compensation (reduces indifference curve inequalities among same-preference agents with unequal skills) and approximate laissez-faire (equal lump-sum transfers for agents with similar wages). The maximin over $m_i(w_{\min}, z_i)$ gives absolute priority to the hardworking poor, guaranteeing a safety net.

3. **Weighted utilitarianism is inadequate (Section 6):** Pareto weights $\alpha_i$ are allocation-specific and cannot generally mimic the fairness properties of money-metric social orderings. Lockwood-Weinzierl weights $\alpha_n = E[1/g^{LF}(\theta_i \bar{w}) | n_i = n]$ work only for the optimal allocation, not for reform evaluation.

4. **Income weights and the zero marginal rate result (Section 7):** Under the maximin with $m_i(w_{\min}, z_i)$, only incomes at $y^*$ (the tangent point in the $[0, w_{\min}]$ range) receive positive weight. The optimal marginal tax rate is zero for $y \leq w_{\min}$ (everyone gets the same lump-sum subsidy) and follows the Saez (2001) formula with zero weights for $y > w_{\min}$. This is a precise formula for the optimal tax.

5. **The $f$-function graphical tool (Section 9.1):** Any tax $T$ can be evaluated by computing $k^*$ (the tangent intercept between $f$ and $y - T(y)$). Higher $k^*$ = better tax. This requires knowing only $w_{\min}$, not the full population distribution. Different ethical positions (egalitarian-equivalent vs libertarian, different $\tilde{w}$ and $\tilde{\ell}$) produce different $f$-function slopes.

6. **US tax evaluation (Figure 6):** For the egalitarian-equivalent criterion ($\lambda = 1$, $\tilde{w} = 0.76 w_{\min}$), earnings with positive weight are zero and $w_{\min}$ (\$25K). For the libertarian criterion ($\lambda = 0$, $\tilde{\ell} = 0.4$), focus is on both low incomes (~\$50K) and high incomes. The US 2013 tax's $f$-function crosses the budget curve around \$650K, making the top earners the worst off under the libertarian criterion.

7. **Optimal tax simulations (Figures 7--8):** Utilitarian taxes go from inverted-U marginal rates (low aversion) to U-shaped (high aversion). Egalitarian-equivalent optimal taxes: flat budget up to $w_{\min}$ (lump-sum transfer), then depending on $\tilde{w}$. Libertarian optimal taxes: from pure laissez-faire ($\tilde{\ell} = 0$) to most redistributive ($\tilde{\ell} = 1$, coincides with most redistributive utilitarian).

8. **Impossibility of unidimensional screening (Section 8.2):** The money-metric utility $m_i(\tilde{w}, z_i)$ generally cannot be written as a function of a single parameter combining preferences and skills (unlike the Lockwood-Weinzierl $n_i = \theta_i w_i$ assumption). This means optimal tax analysis with heterogeneous preferences requires multidimensional tools.

# Main limitations

- Works entirely within the standard Mirrlees framework: no demand-side constraints, involuntary unemployment, or job rationing
- Static model: no dynamics, human capital, or risk (except brief discussion in Section 10)
- Labour-consumption model only: does not capture other dimensions of well-being (health, family, social connections)
- The choice of $\tilde{w}$ and $\tilde{\ell}$ remains normatively open: the paper provides a taxonomy but no definitive recommendation
- Behavioural complications acknowledged but not resolved: individuals may not know their budget sets, preferences may be unstable (Section 10)
- Calibrated illustrations use quasi-linear preferences (no income effect), which simplifies but limits realism
- No empirical estimation: the paper is entirely theoretical with calibrated examples

# Relevance for my JMP

## possible use for the theoretical foundation of the welfare metric
This paper provides the definitive theoretical justification for using equivalent income (money-metric utility at a reference wage) as the welfare metric in my JMP. The key argument: $m_i(\tilde{w}, z_i)$ simultaneously (1) respects individual ordinal preferences, (2) enables interpersonal comparisons, (3) achieves compensation for unequal skills, and (4) approximately satisfies laissez-faire for responsible choices. The choice of $\tilde{w} = w_{\min}$ (as in Fleurbaey & Maniquet 2006) gives priority to the hardworking poor and yields a zero marginal tax rate on low incomes.

## possible use for the ethical choice taxonomy
The four ethical choices in Section 8 provide a framework for discussing the normative decisions embedded in my RURO welfare analysis. In particular: (1) I use ordinal preferences (Choice 1); (2) I seek to compensate for demand-side constraints / opportunity restrictions (extending Choice 2 from skills to opportunities); (3) the $\lambda$ parameter maps directly to whether I treat opportunity restrictions as analogous to skill restrictions (egalitarian-equivalent, $\lambda = 1$) or as the agent's own responsibility (libertarian, $\lambda = 0$); (4) the $\tilde{\ell}$ / $\tilde{w}$ choice determines whether involuntarily non-participating agents (who may be "work-loving" but constrained) receive priority.

## possible use for the limitation the RURO framework addresses
The paper works entirely within the Mirrlees supply-side framework where the opportunity set is determined by $w_i$ alone. My JMP extends this by incorporating the opportunity density $g(h, w)$ from the RURO model, so that the welfare metric can account for demand-side constraints. An agent with high $w_i$ but restricted job availability (low $\theta$ or unfavourable $g(h)$) would have lower welfare than the Mirrlees model predicts, because their effective opportunity set is smaller than $\{(\ell, c) : c \leq w_i \ell - T(w_i \ell)\}$.

# Research questions this paper inspires

1. How should the money-metric utility $m_i(\tilde{w}, z_i)$ be modified when the opportunity set is not the full budget set $\{c \leq w\ell - T(w\ell)\}$ but is restricted by demand-side constraints? If agent $i$ can only access jobs in $A_i \subset \{(h, w)\}$, then $m_i$ should be computed over the restricted set. This is essentially what the RURO framework does: the opportunity density $g(h, w)$ defines the effective choice set.

2. The paper shows that $\tilde{w} = w_{\min}$ gives priority to the hardworking poor. In the RURO framework, who are the "hardworking poor"? They are low-skilled agents who work full-time despite poor job options. Does the opportunity density $g(h)$ affect whether these agents are identified correctly?

3. The impossibility result (Section 8.2) -- money-metric utility cannot be reduced to a unidimensional parameter -- implies that optimal tax analysis with heterogeneous preferences requires multidimensional tools. Does the RURO framework's separation of preferences $R$ from opportunities $A$ help or complicate this dimensionality problem?

# Challenge to this paper

The paper's entire analysis assumes that agents can freely choose any point on their budget constraint $c = w\ell - T(w\ell)$. In labour markets with demand-side constraints -- limited job availability, fixed hours contracts, involuntary unemployment -- the effective choice set is a strict subset of the budget set. The money-metric utility $m_i(\tilde{w}, z_i)$ computed over the full budget set overstates welfare for constrained agents (who cannot access all points on their budget line) and understates welfare for agents who happen to hold a "good" job (one that pays a rent above the budget line). The RURO framework, by modelling the opportunity density $g(h, w)$ explicitly, provides the ingredients to compute a more accurate money-metric utility that accounts for the actual feasible set rather than the theoretical budget set.

More specifically, the zero marginal rate result on low incomes (Section 7) depends on the assumption that lowest-wage agents can freely choose any labour supply in $[0, 1]$. If these agents face hours restrictions (e.g., can only work full-time or not at all), the optimal tax schedule may need positive marginal rates at low incomes to affect the participation margin, which is the relevant margin when hours are rationed.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper provides the theoretical foundation for the welfare metric $W$ in my $W(z, R, A; y)$ framework. The money-metric utility $m_i(\tilde{w}, z_i)$ is the formal expression for $W$ when $A$ is the full budget set. The reference wage $\tilde{w}$ is a normative parameter that determines how preferences $R$ affect the welfare ranking. The tax schedule $y$ enters through the budget constraint $c = y - T(y)$. Preferences $R$ are respected ordinally.

[Reasonable inference for my project] The paper's framework maps to my $W(z, R, A; y)$ as follows: $z$ = realised bundle $(\ell_i, c_i)$; $R$ = individual ordinal preferences $U_i$; $A$ = budget set (in the paper) or opportunity set (in my extension); $y$ = tax schedule $T(\cdot)$. The money-metric utility $m_i(\tilde{w}, z_i)$ is a specific functional form for $W$ that the paper justifies axiomatically. The gap: $A$ in the paper is always the full budget set, not the restricted opportunity set from the RURO model. My JMP fills this gap.

[Unclear from paper] How to compute $m_i(\tilde{w}, z_i)$ when the opportunity set $A_i$ is a subset of the budget set and varies across agents. The paper assumes identical opportunity sets (all agents face the same budget constraint at each wage level), so interpersonal comparisons of $m_i$ reflect only skill and preference differences. When $A_i$ varies (as in RURO), $m_i$ may need to be adjusted to account for opportunity restrictions, or a different metric (like the equivalent wage from Fleurbaey & Maniquet 2006, adjusted for opportunities) may be needed.

# Relation to Bargain et al. (2013)

This paper provides the theoretical justification for the welfare metrics used in Bargain et al. (2013). Specifically:
- The money-metric utility $m_i(\tilde{w}, z_i)$ is the foundation for the equivalent income measure computed in Bargain et al.
- The four ethical choices (Section 8) correspond to the welfare criteria compared in Bargain et al.: egalitarian-equivalent (compensation for skills), conditional equality (a variant), utilitarian, and King's money-metric utility.
- The paper's argument that weighted utilitarianism is inadequate (Section 6) supports Bargain et al.'s decision to use explicit money-metric indexes rather than social welfare weights.
- The $f$-function tool (Section 9.1) provides a simpler alternative to the full microsimulation approach of Bargain et al. for evaluating existing taxes, but it cannot account for behavioural responses.

# Relation to opportunities vs preferences

The paper cleanly separates the normative treatment of preferences from skills but does not address the preferences-vs-opportunities distinction that is central to the RURO framework. In the Mirrlees model, the "opportunity set" is fully determined by the wage $w_i$ and the tax schedule $T$. There is no separate opportunity channel: all variation in outcomes conditional on $w_i$ is attributed to preferences.

The paper acknowledges two relevant extensions:
1. **Luck/desert (Section 5.5):** Random shocks to income can be treated as a circumstance (to be compensated) or as desert (to be kept). The resource-egalitarian approach treats shocks as circumstances, applying laissez-faire only among agents with the same skill and shock.
2. **Public goods (Section 5.1):** When public goods affect productivity ($w_i(g) = w_i h(g)$), the personalized reference wage $\tilde{w}_i = (1-\lambda)w_i$ may also capture virtual wage adjustments.

Neither extension addresses the RURO framework's central concern: that the set of available jobs $\{(h, w) : g(h, w) > 0\}$ varies across agents and constrains their choices beyond the budget set.

# Useful quotations / formulas

**On money-metric utility (Section 5.1, p. 1047):**
$$m_i(\tilde{w}, z_i) = \min\{t \in \mathbb{R} \mid \exists (\ell, c) \in X,\; c = t + \tilde{w}\ell,\; U_i(\ell, c) \geq U_i(z_i)\}$$

**On the generalized index (Section 8, p. 1061):**
"$m_i(\tilde{w}_i, z_i) + \tilde{w}_i \tilde{\ell}$, where $\tilde{w}_i = \lambda \tilde{w} + (1-\lambda) w_i$"

**On why weighted utilitarianism fails (Section 6, p. 1053):**
"Whatever the precise formula for the weights, the evaluation of allocations in the actual economy is not geared toward the laissez-faire in a systematic way."

**On the zero marginal rate (Section 7, p. 1058):**
"$\forall y \leq w_{\min}, \quad T'(y) = 0$" and "$\forall y \geq w_{\min}, \quad \frac{T'(y)}{1-T'(y)} = \frac{1-F(y)}{\epsilon(y) y f(y)}$"

**On the $f$-function (Section 9.1, p. 1067):**
"The computation of $k^*$ requires no knowledge at all of the characteristics of the population, except the value of $w_{\min}$."

**On the choice of $\tilde{w}$ (Section 8.1.4, p. 1064):**
"With a low value for $\tilde{w}$, individuals who are more averse to work tend to obtain lower implicit budgets... And the contrary occurs with a high value for $\tilde{w}$."

**On the first-best avoiding slavery of the talented (Section 9.2, p. 1070):**
"In summary, with the $m_i(\tilde{w}_i, z_i) + \tilde{w}_i \tilde{\ell}$ class of utilities, if one wants to fully avoid the risk of penalizing any individual for being more productive, one has to pick either $\lambda = 1$ or $\ell = 0$."

**On the need for ordinal preferences (Section 8.1.1, p. 1060):**
"It is commonly believed that no interpersonal comparisons can be made on the basis of individual ordinal noncomparable preferences. In the rest of this section, we focus on indexes that are based on ordinal noncomparable preferences in order to show the wide array of possibilities offered by this informational basis."

**On behavioural challenges (Section 10, p. 1075):**
"Individuals may not be aware of their budget options (Chetty, Looney, and Kroft 2009 and Chetty, Friedman, and Saez 2013), and their preferences can be unstable and unreliable."

# Suggested tags

optimal-taxation, fairness, equivalent-income, money-metric-utility, egalitarian-equivalent, libertarian, Mirrlees, maximin, leximin, social-welfare-function, Saez-formula, income-weights, Pareto-weights, compensation, laissez-faire, responsible-preferences, hardworking-poor, slavery-of-talented, tagging, horizontal-equity, f-function, reform-evaluation, survey, JEL, Fleurbaey, Maniquet

# My quick takeaway

The definitive theoretical survey connecting fair allocation theory to optimal taxation. The paper's core contribution for my JMP is threefold: (1) it provides the axiomatic justification for money-metric utility $m_i(\tilde{w}, z_i)$ as the welfare metric, showing it resolves the four fundamental problems of utilitarianism; (2) it maps out the full space of ethical choices through the $(\lambda, \tilde{\ell})$ parameterisation, giving practitioners a transparent menu; (3) it develops the $f$-function as a practical evaluation tool. The key limitation for my purposes is that the entire analysis assumes the opportunity set equals the budget set -- the RURO framework's explicit modelling of demand-side constraints via $g(h, w)$ is the natural next step, and would modify both the welfare metric (money-metric utility computed over the restricted feasible set) and the optimal tax results (the zero marginal rate on low incomes may not survive hours rationing).
