---
title: "Designing Optimal Taxes with a Microeconometric Model of Household Labour Supply"
authors: [Rolf Aaberge, Ugo Colombino]
year: 2006
outlet: "Discussion Papers No. 475, Statistics Norway"
country_or_context: "Norway"
population: "Singles and married/cohabiting couples, ages 18--54"
data_period: "1994--1995"
shelf: "optimal taxation / structural labour supply / equality of opportunity"
tags: [RURO, optimal-taxation, discrete-choice, equality-of-opportunity, Roemer, EOp, social-welfare, rank-dependent-SWF, piecewise-linear-tax, microsimulation, Norway, opportunity-density, common-welfare-function]
priority: "high"
read_status: "extracted"
---

# Full citation

Aaberge, R., & Colombino, U. (2006). Designing Optimal Taxes with a Microeconometric Model of Household Labour Supply. *Discussion Papers No. 475*, Statistics Norway, Research Department, Oslo.

# One-sentence contribution

Uses a 78-parameter RURO job-choice model estimated on Norwegian data to numerically identify optimal piecewise-linear income tax rules under both Equality of Outcome (EO) and Equality of Opportunity (EOp) social welfare criteria, finding that all optimal rules feature lower marginal rates on low/average incomes and 100% top marginal rates, and that EO and EOp criteria produce surprisingly similar tax schedules.

# Why this paper matters

This is the **working paper precursor** to Aaberge & Colombino (2013, Scand. J. Econ.), providing the first detailed implementation of optimal tax design through a structural microsimulation model rather than analytical formulas. Crucially, it introduces the **Equality of Opportunity** criterion (following Roemer 1998) alongside standard EO welfare functions, and develops an **extended EOp family** $\tilde{W}_k$ that combines between-type inequality (circumstances) with within-type inequality aversion. This is the first paper in the RURO literature to operationalize the responsibility/compensation distinction for optimal policy design.

# Core research question

What are the optimal piecewise-linear income tax rules in Norway, under revenue neutrality, when the social planner uses (i) Equality of Outcome criteria with varying inequality aversion, or (ii) Equality of Opportunity criteria that distinguish effort from circumstances (family background)?

# Economic setting and context

Norway 1994: progressive income tax with top MTR of 49.5%, exemption level at NOK 17,000. The tax system features 6 brackets with rates rising from 0% to 49.5%. The paper keeps all welfare transfers (social assistance, disability, etc.) unchanged and optimizes only over the marginal rate profile.

# Model / theoretical framework

The paper uses the **Dagsvik (1994) RURO job-choice framework** with three separate models for single females, single males, and married/cohabiting couples. The model has 78 parameters capturing heterogeneity in both preferences and opportunities.

**What the agent chooses:** A job package $(h, w, s, j)$ — hours, wage, sector (public/private), and unobserved job attributes. For couples: $(h_M, h_F, w_M, w_F, s_M, s_F)$.

**Choice probability:**
$$\varphi(h, w, s) = \frac{v[f(wh, I), h, s] \cdot p(h, w, s)}{\sum_{s=0,1} \int\int v[f(xy, I), y, s] \cdot p(y, x, s) \, dx \, dy}$$

**Opportunity density:**
$$p(h, w, s) = p_0 \cdot g_{1s}(h) \cdot g_{2s}(w) \cdot g_3(s)$$
with $p_0$ = proportion of market opportunities, $g_1$ = hours density with peaks at part-time (18--20 weekly) and full-time (37--40 weekly), $g_2$ = log-normal wage density, $g_3$ = sector density.

**Framework:** Both positive (predicting behavioural responses) and normative (maximizing social welfare). The normative exercise uses a **common individual welfare function** $V(c, h, s)$ for interpersonal comparability, distinct from the heterogeneous utility functions used in the behavioural model.

# Key objects

- **Common individual welfare function** $V(c, h, s)$: estimated separately from the behavioural utility, with Box-Cox specification and taste-shifters for age, children, and sector. Parameters: $\gamma_1 = -0.694$ (consumption curvature), $\gamma_3 = -11.862$ (leisure curvature). Couples' income equivalized by $\sqrt{2}$.
- **EO social welfare:** $W_k = \int_0^1 p_k(t) F^{-1}(t) dt$ with weight $p_k(t) = \frac{k}{k-1}(1-t^{k-1})$ for $k \geq 2$, $p_1(t) = -\log t$ (Bonferroni). $W_\infty = \mu$ (utilitarian).
- **EOp social welfare (Roemer):** $\tilde{W}_\infty = \int_0^1 \min_j F_j^{-1}(t) dt$ — average of worst-off type at each effort quantile.
- **Extended EOp:** $\tilde{W}_k = \int_0^1 p_k(t) \min_j F_j^{-1}(t) dt$ — combines EOp with within-type inequality aversion.
- **Circumstance types:** 3 types defined by father's years of education: <5 years (Type 1), 5--8 years (Type 2), >8 years (Type 3).
- **Piecewise-linear tax rule:** 6 parameters: exemption $E$, three marginal rates $(\tau_1, \tau_2, \tau_3)$, two bracket limits $(\bar{Z}_1, \bar{Z}_2)$.

# Data

Norwegian 1994/1995 data from Statistics Norway (Survey of Level of Living, administrative tax records). Sample: 1,842 married/cohabiting couples; 309 single females; 312 single males. Ages 18--54.

# Identification logic

Identification follows the standard RURO approach. Utility parameters identified from variation in the tax-benefit function $f(\cdot)$ across income levels and household types. Opportunity density parameters identified from observed hours/wage distributions. The common welfare function $V$ is estimated using the same likelihood framework but with a common specification across all individuals (rather than type-specific utility functions).

# Estimation / empirical strategy

1. Estimate the RURO model (78 parameters) on Norwegian data by maximum likelihood — three separate models for singles (male/female) and couples.
2. Estimate the common welfare function $V(c, h, s)$ with 13 parameters (Table 4.1).
3. For each candidate tax rule (6 parameters), simulate labour supply responses and compute the distribution of welfare levels.
4. Maximize $W_k$ or $\tilde{W}_k$ over the 6 tax parameters subject to revenue neutrality.
5. Two exercises: unconstrained (allows $\tau_3 = 1$) and constrained ($\tau_3 \leq 0.60$).

# Treatment of preferences

Three separate utility functions for single females, single males, and couples — each with Box-Cox specification over disposable income and leisure, with taste-shifters for age, children, sector, and (for couples) leisure interaction. The common welfare function $V$ imposes a single preference ordering for interpersonal comparability, allowing variation only through age, children, and sector.

# Treatment of opportunities / constraints

The opportunity density $p(h, w, s)$ is fully specified with:
- **Hours density** $g_{1s}(h)$: uniform with peaks at part-time (18--20 weekly hours) and full-time (37--40 weekly hours), sector-specific.
- **Wage density** $g_{2s}(w)$: log-normal with education, experience, and sector effects.
- **Sector/scale** $g_0 g_3(s)$: captures the overall availability of market opportunities and relative prevalence of public vs. private sector jobs.

Opportunities vary by gender and sector. For couples, male and female opportunity densities are independent conditional on sector. The opportunity structure is held fixed under tax reforms (partial equilibrium).

# Welfare / normative object

The paper uses **two distinct normative frameworks**:

1. **Equality of Outcome (EO):** Rank-dependent SWFs $W_k$ with $k = 1$ (Bonferroni, most egalitarian), $k = 2$ (Gini), $k = 3$, and $k = \infty$ (utilitarian). These maximize a weighted sum of individual welfare levels, with higher weights on the worse-off.

2. **Equality of Opportunity (EOp):** Following Roemer (1998), individuals are classified into types by father's education (circumstance). Within-type welfare differences reflect effort (responsibility); between-type differences reflect circumstances (compensation). The pure EOp criterion $\tilde{W}_\infty$ maximizes the average welfare of the worst-off type at each effort quantile. The extended EOp $\tilde{W}_k$ adds within-type inequality aversion.

The key conceptual innovation is the **extended EOp family** $\tilde{W}_k$ (eq. 5.6), which can be decomposed as $\tilde{W}_k = \tilde{W}_\infty(1 - \tilde{I}_k)$ where $\tilde{I}_k$ measures inequality within the worst-off type distribution $\tilde{F}$.

# Main findings

**Optimal tax structure (Tables 6.2--6.3):**

Unconstrained:
- All SWFs produce $\tau_3 = 1.00$ (100% top marginal rate) — driven by near-zero elasticity of top earners
- $\tau_1$ ranges from 0.11--0.23 (much lower than 1994's ~25--30%)
- $\tau_2$ ranges from 0.32--0.41
- More egalitarian SWFs produce more progressive schedules
- Exemption $E$ ranges from NOK 2,000 (utilitarian) to NOK 2,000 (Bonferroni)

Constrained ($\tau_3 \leq 0.60$):
- $\tau_1$ ranges from 0.12--0.24, $\tau_2$ from 0.33--0.41, $\tau_3 = 0.60$
- Similar pattern: lower MTRs on low/average incomes, higher on top

**EO vs. EOp comparison:**
- The optimal tax rules under EO and EOp are **remarkably similar** — "the differences implied by using the EO or the EOp criterion seem negligible" (p. 22)
- EOp produces slightly more progressive schedules in some cases
- This is surprising since EOp is usually interpreted as less interventionist

**Behavioural responses (Tables 6.4--6.5):**
- Participation increases 2--7 percentage points under all optimal rules
- Annual hours increase 4--11%
- Disposable income increases 5--14%
- **Strongest responses from lowest income deciles**: bottom decile hours increase 28--90% (singles), 37--66% (couples)
- Top decile nearly unresponsive (0--2% change)

**Winners (Table 6.6):**
- 60--80% of population are winners under all optimal rules
- Winners span all income deciles but proportions vary by gender and marital status

**Key policy insight:** Optimal tax reform should lower marginal rates on low and average incomes (not top rates), contrary to the direction of tax reforms implemented in many countries during the 1980s--1990s.

# Main limitations

- Working paper version; the published version (Aaberge & Colombino 2013) uses 10 parameters and 5 brackets instead of 6 parameters and 4 brackets.
- 100% top MTR is "hardly realistically implementable" — driven by model's inelastic top decile without modelling tax avoidance or evasion.
- Partial equilibrium: opportunity densities fixed under reforms.
- EOp types based solely on father's education (3 types) — coarse proxy for circumstances.
- Revenue neutrality constrains the optimization; alternative levels of public goods provision are not considered.
- No modelling of taxable income responses (avoidance, shifting, evasion).

# Relevance for my JMP

## possible use for framing
The paper provides the first operationalization of Roemer's EOp criterion within a structural RURO model. The finding that EO and EOp produce similar optimal taxes is striking and suggests that the responsibility/compensation distinction may matter less for the optimal tax *schedule* than for the *interpretation* of welfare effects. This motivates asking whether a more refined framework (like $W(z, R, A; y)$) would produce more discriminating policy implications.

## possible use for model design
The paper demonstrates the full computational pipeline: estimate RURO model → estimate common welfare function → simulate under candidate tax rules → optimize. This is exactly the pipeline needed for my framework, with the addition of decomposing welfare into opportunity and preference components.

## possible use for identification
The common welfare function $V(c, h, s)$ with 13 parameters is estimated using the same likelihood framework as the behavioural model but with a common specification. This is the empirical counterpart of using a reference preference $\bar{R}$ in the $W(z, R, A; y)$ framework.

## possible use for welfare measurement
The extended EOp family $\tilde{W}_k$ is a hybrid between outcome equality and opportunity equality. In my framework's terms, it partially implements the compensation principle (equalizing across types/circumstances) while remaining agnostic about whether within-type inequality reflects genuine effort or unobserved circumstances.

## possible use for decomposition
The paper classifies individuals by circumstance type (father's education) but does not decompose welfare into preference vs. opportunity components in the Fleurbaey-Maniquet sense. My framework could refine this by using the structural distinction between $R$ and $A$ rather than relying on reduced-form type classifications.

# Research questions this paper inspires

1. Why do EO and EOp produce such similar optimal tax schedules? Is this because the structural model already captures opportunity constraints through $p(h, w, s)$, making the type-based EOp classification redundant?

2. Would a finer classification of circumstances (beyond father's education) produce more divergence between EO and EOp optimal taxes?

3. Can the $W(z, R, A; y)$ framework produce a welfare criterion that is more discriminating than both EO and EOp — by using the structural decomposition of preferences and opportunities rather than reduced-form type classifications?

4. How would the optimal tax schedule change if the opportunity density $p(h, w, s)$ were allowed to respond endogenously to the tax reform (general equilibrium)?

# Challenge to this paper

The paper uses a **common individual welfare function** $V(c, h, s)$ for interpersonal comparability, but this function is estimated from observed choices — which reflect the interaction of preferences and opportunities. If individuals with different opportunity sets make systematically different choices (e.g., women with fewer job opportunities choose fewer hours), the estimated common welfare function may conflate preference-driven and opportunity-driven variation in choices. This means the welfare evaluation may not correctly distinguish between individuals who work few hours because they prefer leisure and those who work few hours because they lack opportunities. The EOp criterion addresses this partially through type classification, but the 3-type partition based on father's education is very coarse and likely misses much opportunity heterogeneity that the structural model actually captures through $p(h, w, s)$.

# Relation to my jobs_and_wellbeing framework

[Reasonable inference for my project] The paper's common welfare function $V(c, h, s)$ plays exactly the role of the reference preference $\bar{R}$ in the $W(z, R, A; y)$ framework. It is used for interpersonal comparability, allowing the planner to rank outcomes across individuals with heterogeneous true preferences. The paper's EO criterion corresponds to maximizing $W(z, \bar{R}, A; y)$ aggregated with rank-dependent weights. The EOp criterion adds a partial implementation of the compensation principle by conditioning on circumstance types (father's education), but it does not use the structural distinction between $R$ and $A$ that the RURO model actually provides.

[Explicit in paper] The paper explicitly discusses the need for a common welfare function to solve the interpersonal comparability problem (Section 4, p. 12--13). It cites Fleurbaey and Maniquet (2006) on optimal redistribution with heterogeneous preferences for leisure (footnote 5). The EOp framework follows Roemer (1998) with types defined by father's education.

[Unclear from paper] Whether the common welfare function $V$ satisfies any of the axioms in my framework (Full Compensation, Independence of $A$, Full Responsibility, etc.). The use of a common $V$ is conceptually close to Compensation for Reference Preferences, but the paper does not discuss this connection. It is also unclear whether the near-equivalence of EO and EOp results would hold under a more refined decomposition of welfare inequality into $R$ and $A$ components.

The paper is closest to: **reference preferences for interpersonal comparability**, **Roemer's EOp framework**, and **numerical optimal tax design**.

# Relation to Bargain et al. (2013)

This paper and Bargain et al. (2013) both use structural discrete-choice models for welfare evaluation under heterogeneous preferences, and both address the problem of interpersonal comparability. The key difference: this paper introduces a separate **common welfare function** $V$ estimated from data, while Bargain et al. impose a **reference preference ordering** $\bar{R}$ directly on the utility function. This paper additionally introduces the EOp criterion with type classification, which Bargain et al. do not use. The finding that EO and EOp are nearly equivalent is relevant for Bargain et al.'s framework: it suggests that adding a responsibility/compensation dimension to welfare evaluation may not change policy conclusions much, at least within the RURO framework.

# Relation to opportunities vs preferences

The paper structurally separates preferences (utility functions $v(\cdot)$) from opportunities ($p(h, w, s)$ with 78 parameters), but the **normative evaluation** only partially exploits this distinction. The EO criterion ignores the preference/opportunity distinction entirely. The EOp criterion uses a reduced-form proxy (father's education types) rather than the structural $R$ vs. $A$ decomposition. This is a missed opportunity: the model provides all the ingredients to decompose welfare inequality into preference-driven and opportunity-driven components, but the paper does not do so. My framework $W(z, R, A; y)$ is designed to fill exactly this gap.

# Useful quotations / formulas

**Common welfare function (eq. 4.1):**
$$\log V(c, h, s) = \gamma_2 \frac{c^{\gamma_1} - 1}{\gamma_1} + (\gamma_4 + \gamma_5 \log A + \gamma_6 (\log A)^2 + \gamma_7 s + \ldots) \frac{L^{\gamma_3} - 1}{\gamma_3}$$

**EO social welfare (eq. 5.1):**
$$W_k = \int_0^1 p_k(t) F^{-1}(t) dt, \quad k = 1, 2, \ldots$$

**EOp social welfare — pure Roemer (eq. 5.5):**
$$\tilde{W}_\infty = \int_0^1 \min_j F_j^{-1}(t) dt$$

**Extended EOp (eq. 5.6):**
$$\tilde{W}_k = \int_0^1 p_k(t) \min_j F_j^{-1}(t) dt, \quad k = 1, 2, \ldots$$

**On the similarity of EO and EOp (p. 22):** "The differences implied by using the EO or the EOp criterion seem negligible. This is interesting since EOp is usually interpreted as a less interventionist criterion than EO."

**On the direction of optimal reform (p. 22):** "All the optimal rules imply — with respect to the current rule — lower marginal rates on low and/or average income levels and higher marginal rates on sufficiently high income levels."

# Suggested tags

optimal-taxation, RURO, equality-of-opportunity, Roemer, EOp, EO, rank-dependent-SWF, Bonferroni, Gini, common-welfare-function, piecewise-linear-tax, microsimulation, Norway, opportunity-density, reference-preferences, interpersonal-comparability

# My quick takeaway

This working paper is the detailed precursor to Aaberge & Colombino (2013) and uniquely introduces the EOp criterion (Roemer 1998) into the RURO optimal tax framework. The most striking finding — that EO and EOp produce nearly identical optimal taxes — raises the question of whether coarse type classifications (father's education) adequately capture the responsibility/compensation distinction. For my JMP, this motivates using the structural $R$ vs. $A$ decomposition from the RURO model itself, rather than reduced-form type proxies, to implement a more refined version of the compensation principle. The paper also provides the complete computational pipeline (estimate → simulate → optimize) that my framework would follow.
