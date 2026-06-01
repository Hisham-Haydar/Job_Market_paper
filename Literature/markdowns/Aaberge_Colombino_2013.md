# Aaberge & Colombino (2013) — Using a Microeconometric Model of Household Labour Supply to Design Optimal Income Taxes

## Bibliographic Information
- **Authors:** Rolf Aaberge, Ugo Colombino
- **Year:** 2013
- **Title:** Using a Microeconometric Model of Household Labour Supply to Design Optimal Income Taxes
- **Journal:** *The Scandinavian Journal of Economics*, 115(2), 449--475
- **Keywords:** optimal taxation, labour supply, microsimulation, social welfare, random utility, piecewise-linear taxes

---

## 1. Research Question & Contribution

**Central question:** Can we design optimal income tax rules by maximizing a social welfare function through a structural microeconometric model of labour supply, rather than relying on the restrictive assumptions of analytical optimal tax theory (Mirrlees 1971)?

**Core contribution:** The paper operationalizes the "mechanism design" approach to optimal taxation. Instead of deriving closed-form optimal tax formulas (which require homogeneous preferences, continuous labour supply, and simple budget sets), the authors embed a **random utility / random opportunity (RURO) job choice model** inside a numerical optimizer that searches over a class of piecewise-linear tax rules to maximize social welfare. This allows the model to accommodate:
- Heterogeneous preferences across household types
- Multidimensional job characteristics (hours, wages, sector)
- Complex (non-convex, non-differentiable) budget constraints
- Simultaneous decisions of couples
- Empirically estimated opportunity sets (latent job densities)

The approach is applied to Norwegian 1994 data for singles and couples, under four alternative social welfare functions.

---

## 2. Relation to W(z, R, A; y)

This paper is a **direct precursor** to the well-being decomposition framework:

| Component | Paper's operationalization |
|-----------|--------------------------|
| **z** (realized bundle) | Observed/simulated choice (h, w, s, j) — hours, wage, sector, job index |
| **R** (preferences) | Heterogeneous utility $U[f(wh, I), h, s, j] = v[f(wh, I), h, s] \cdot \varepsilon(j)$; differs across household types (single males, single females, couples) |
| **A** (feasible set / opportunities) | Opportunity density $p(h, w, s)$ — the density of available jobs at each (hours, wage, sector) triple; 78 parameters, differs by education, region, demographics |
| **y** (pay schedule / tax-benefit rule) | The **object of optimization**: piecewise-linear tax function $T(y) = \max(y - d, 0)\tau_k$ for bracket $k$, with 10 parameters $(\tau_1, \ldots, \tau_5, z_1, \ldots, z_4, d)$ |

**Welfare function:** The paper uses a **common (reference) utility function** $\log V(y,h) = \gamma_2 \frac{y^{\gamma_1}-1}{\gamma_1} + \gamma_4 \frac{L^{\gamma_3}-1}{\gamma_3}$ (where $L = 1 - h/8736$) for interpersonal comparability. This is exactly analogous to using a reference preference ordering $\bar{R}$ in the framework $W(z, \bar{R}, A; y)$.

**Key mapping:** The social welfare maximization is:
$$\max_{y \in \mathcal{Y}} W = \int_0^1 q(t) F_V^{-1}(t) \, dt$$
subject to a revenue constraint — this is the **planner's problem** over pay schedules $y$, evaluated using a common welfare metric applied to the simulated distribution of bundles $z$ chosen under heterogeneous $R$ and opportunity sets $A$.

---

## 3. Methodology

### 3.1 Labour Supply Model (RURO Job Choice)

**Choice framework:** Each household faces a universe of latent jobs $j$, each characterized by $(h_j, w_j, s_j)$. Utility is:
$$U[f(w_j h_j, I), h_j, s_j, j] = v[f(w_j h_j, I), h_j, s_j] \cdot \varepsilon(j)$$

where:
- $f(\cdot)$ is the tax-benefit function mapping gross earnings + non-labour income $I$ to disposable income
- $v[\cdot]$ is the systematic (deterministic) part of utility
- $\varepsilon(j)$ is a job-specific random taste component (Type I Extreme Value), capturing non-pecuniary job attributes

**Opportunity density:** The density of available jobs at $(h, w, s)$ is $p(h, w, s)$, modeled with 78 parameters capturing how the opportunity set varies with individual characteristics (education, experience, region, etc.).

**Choice density:** The probability of choosing a job with characteristics $(h, w, s)$ is:
$$\varphi(h, w, s) = \frac{v[f(wh, I), h, s] \cdot p(h, w, s)}{\iiint v[f(xy, I), y, z] \cdot p(y, x, z) \, dx \, dy \, dz}$$

This is a **continuous logit** model (Ben-Akiva and Watanatada 1981; Dagsvik 1994).

### 3.2 Systematic Utility Specification

**Couples:**
$$\log v(C, h_M, h_F) = \left[\alpha_0 + \sum_{k=1}^{6}\alpha_k q_k\right] \log C + \beta_0 \log(1 - h_M/8736) + \left[\delta_0 + \sum_{k=1}^{6}\delta_k q_k\right] \log(1 - h_F/8736)$$

where $q_k$ are demographic variables (age, children). Taste-shifters enter only disposable income and female leisure, reflecting observed variation in female but not male labour supply responses.

**Singles:** Similar log-linear specification with individual-specific taste-shifters.

### 3.3 Welfare Evaluation

**Common welfare function** (for interpersonal comparability):
$$\log V(y, h) = \gamma_2 \frac{y^{\gamma_1} - 1}{\gamma_1} + \gamma_4 \frac{L^{\gamma_3} - 1}{\gamma_3}$$

where $y$ = disposable income, $L = 1 - h/8736$ = leisure share. Parameters: $\gamma_1 = -2.05$, $\gamma_2 = 3.92 \times 10^7$, $\gamma_3 = 0.3$, $\gamma_4 = 1.164$.

**Social welfare function (rank-dependent):**
$$W = \int_0^1 q(t) F_V^{-1}(t) \, dt$$

Four specifications of the weight function $q(t)$:
| SWF | Weight function $q(t)$ | Character |
|-----|----------------------|-----------|
| $W_1$ (Bonferroni) | $-\log(1-t)$ | Most egalitarian |
| $W_2$ (Gini) | $2(1-t)$ | Moderately egalitarian |
| $W_3$ | $3(1-t)^2$ | Less egalitarian |
| $W_\infty$ (Utilitarian) | $1$ (constant) | No inequality aversion |

### 3.4 Optimization

**Tax rule class:** Piecewise-linear with 5 brackets:
$$T(y) = \max(y - d, 0) \cdot \tau_k \quad \text{for } z_{k-1} \leq y < z_k$$

10 parameters: marginal rates $\tau_1, \ldots, \tau_5$; bracket thresholds $z_1, \ldots, z_4$; lump-sum transfer/tax $d$.

**Constraint:** Total net tax revenue $\geq$ total net tax revenue under the 1994 system (revenue-neutral).

**Algorithm:** Numerical optimization (details in Aaberge & Colombino 2006, 2011).

---

## 4. Data

- **Country:** Norway, 1994
- **Sample:** 1,842 married/cohabiting couples; 309 single females; 312 single males
- **Source:** Statistics Norway administrative and survey data
- **Wage elasticities (Table 1):** Strong inverse relationship with income. Decile I: ~0.55 (males), ~1.68 (females, couples). Decile X: ~0.01--0.04 (nearly zero for top earners).

---

## 5. Key Results

### 5.1 Optimal Tax Structure (Table 7)

| Bracket (NOK 1994) | 1994 MTR | $W_1$ (Bonf.) | $W_2$ (Gini) | $W_3$ | $W_\infty$ (Util.) |
|---------------------|----------|--------------|-------------|-------|-------------------|
| 0--30,000 | 0 | $-2.1$ | $-0.7$ | $-0.3$ | $-0.2$ |
| 30,000--100,000 | 25.8 | 17.4 | 19.3 | 22.3 | 22.7 |
| 100,000--200,000 | 35.8 | 26.0 | 28.5 | 32.2 | 33.1 |
| 200,000--530,000 | 36.5--49.5 | 37.5 | 37.1 | 40.1 | 41.8 |
| >530,000 | 49.5 | 100.0 | 100.0 | 100.0 | 100.0 |
| Lump sum $d$ (NOK) | — | $-7,428$ | $-2,651$ | $-1,150$ | $-703$ |

**Key patterns:**
1. **Negative MTR on lowest incomes** — effectively a wage subsidy / earned income tax credit
2. **Monotonically increasing MTRs** across brackets
3. **100% top MTR** under all SWFs — justified by near-zero wage elasticity in top decile; top earners' job choices driven by non-pecuniary attributes, so earnings are "rents"
4. **Universal lump-sum tax** ($d < 0$) — implementable as a property/wealth tax
5. **More egalitarian SWF $\Rightarrow$ more progressive** tax schedule

### 5.2 Behavioural Responses (Tables 9--10)

Under optimal rules vs. 1994 system:
- **Participation rates increase** 2--6 percentage points (all groups)
- **Annual hours increase** 5--11% (especially for females in couples)
- **Disposable income increases** 5--13% for most groups
- **Strongest responses in lowest income deciles** — bottom decile labour supply increases 43--63% (singles, males) and 50--75% (couples)
- **Top decile nearly unresponsive** — confirming the 100% MTR is welfare-improving

### 5.3 Winners (Table 11)

All optimal rules would "win the referendum" — 61--83% of the population are winners (welfare higher than under 1994 system). Main losers: single women in top income deciles who lose current deductions.

---

## 6. Theoretical Connections

### Relationship to Analytical Optimal Tax Literature
- **Mirrlees (1971):** The benchmark. Requires homogeneous preferences, continuous labour supply, uni-dimensional ability. The present approach relaxes all these.
- **Diamond (1998):** U-shaped MTRs in analytical models. This paper finds **monotonically increasing** MTRs — the difference driven by the more realistic preference heterogeneity and discrete choice structure.
- **Saez (2001, 2002):** Elasticity-based optimal tax formulas. This paper's decile-specific elasticities directly inform the MTR profile.
- **Tuomala (2010):** Noted that analytical results (lump-sum + proportional tax) are "forced by the restrictive assumptions" — this paper confirms by showing qualitatively different optimal rules.

### Relationship to Equality of Opportunity
- The use of a **common welfare function** $V(y,h)$ instead of individual-specific utilities is a form of imposing a **reference preference** $\bar{R}$ — this is the same device that Fleurbaey-Maniquet use for the **conditional equality** criterion.
- The **lump-sum component** $d$ can be interpreted as partial equalization of opportunities (non-earnings endowments).

---

## 7. Methodological Innovations & Limitations

### Innovations
1. **First paper to solve for optimal piecewise-linear taxes using a full structural microsimulation model** (not just elasticity formulas)
2. **Revenue-neutral comparisons** — same total revenue as 1994 system
3. **Multiple SWFs** to show robustness of qualitative conclusions
4. **Rank-dependent welfare** — accommodates a range of inequality aversion from Bonferroni to utilitarian

### Limitations (acknowledged by authors)
- Tax rule constrained to piecewise-linear with 5 brackets — more flexible rules might yield different results
- Top MTR of 100% is "hardly realistically implementable" — driven by model's inelastic top decile
- No modelling of taxable income responses (evasion, avoidance, income shifting)
- No intercountry mobility responses
- Opportunity densities treated as invariant to the tax reform (partial equilibrium)
- Single-year cross-section; no dynamics

---

## 8. Key Equations

**Choice density:**
$$\varphi(h,w,s) = \frac{v[f(wh,I),h,s] \cdot p(h,w,s)}{\iiint v[f(xy,I),y,z] \cdot p(y,x,z) \, dx \, dy \, dz}$$

**Common welfare:**
$$\log V(y,h) = \gamma_2 \frac{y^{\gamma_1}-1}{\gamma_1} + \gamma_4 \frac{(1-h/8736)^{\gamma_3}-1}{\gamma_3}$$

**Social welfare:**
$$W = \int_0^1 q(t) F_V^{-1}(t) \, dt$$

**Tax rule:**
$$T(y) = \max(y - d, 0) \cdot \tau_k, \quad z_{k-1} \leq y < z_k$$

---

## 9. Relevance to Your Job Market Paper

| Dimension | Relevance |
|-----------|-----------|
| **Structural discrete choice** | Core model (RURO with continuous logit) is the same class you use |
| **Opportunity sets** | Opportunity density $p(h,w,s)$ is the empirical counterpart of your feasible set $A$ |
| **Reference utility** | Common welfare function $V(y,h)$ is exactly the $\bar{R}$ device for interpersonal comparability |
| **Optimal policy** | Shows how to use the structural model for normative analysis (optimal $y$), which is the ultimate purpose of your framework |
| **Norwegian data** | Same country context; 1994 data is the baseline for many subsequent papers you cite |
| **Inequality decomposition** | Decile-specific results (Tables 10--11) show how policy effects differ across the income distribution |
| **Microsimulation** | Template for how to embed structural models in policy evaluation |

**Direct connection to your framework:** This paper solves $\max_y W(z, \bar{R}, A; y)$ — finding the optimal pay schedule $y$ by maximizing welfare evaluated at a reference preference $\bar{R}$ over the distribution of realized bundles $z$ chosen under heterogeneous true preferences $R$ and opportunity sets $A$. Your framework provides the conceptual foundation; this paper provides the computational implementation.

---

## 10. Notable Data Points for Citation

- Wage elasticities inversely related to income: 0.55 (bottom decile, males) to 0.01 (top decile)
- Optimal bottom MTR negative (-0.2% to -2.1%), optimal top MTR = 100%
- 61--83% of population are "winners" under all optimal rules
- Lump-sum $d$ ranges from -703 to -7,428 NOK (i.e., a universal tax, not transfer)
- Participation increases 2--6 pp; hours increase 5--11% under optimal rules
- Bottom decile labour supply increase: 43--63% (singles), 50--75% (couples)
