# Aaberge, Colombino & Strøm (1999) — Labour Supply in Italy: An Empirical Analysis of Joint Household Decisions, with Taxes and Quantity Constraints

## Bibliographic Information
- **Authors:** Rolf Aaberge, Ugo Colombino, Steinar Strøm
- **Year:** 1999
- **Title:** Labour Supply in Italy: An Empirical Analysis of Joint Household Decisions, with Taxes and Quantity Constraints
- **Journal:** *Journal of Applied Econometrics*, 14(4), 403--422
- **Keywords:** labour supply, Italy, discrete choice, job opportunities, quantity constraints, tax simulation, married couples

---

## 1. Research Question & Contribution

**Central question:** What are the labour supply elasticities and effects of tax reforms in Italy, when the model accounts simultaneously for (i) both spouses' joint decisions, (ii) the exact non-convex budget set created by Italian taxes and benefits, and (iii) quantity constraints on available jobs?

**Core contribution:** This is the **first model of Italian labour supply** that simultaneously incorporates all three features above. Previous Italian studies (Colombino & Zabalza 1982; Colombino & Del Boca 1990) used the Hausman approach (continuous choice along budget constraint), focused only on women, and ignored quantity constraints. The key innovations:

1. Applies the **Dagsvik (1994) job choice framework** to Italian data — labour supply is modeled as choosing among heterogeneous job packages with hours, wages, and non-pecuniary attributes
2. Introduces **quantity constraints** through the opportunity density $g(h,w)$ and the parameter $g_0$ (ratio of market to non-market opportunities) — $g_0 < 1$ implies rationing
3. Defines **unemployment** structurally: $\rho = (1 - g_0)\varphi(0,0)$ — the rate of excess non-participation due to insufficient market opportunities relative to the "fair environment" benchmark ($g_0 = 1$)
4. Shows that standard Hausman-approach elasticities are **biased upward** compared to the job-choice model, particularly for own-wage effects of working women

---

## 2. Relation to W(z, R, A; y)

| Component | Paper's operationalization |
|-----------|--------------------------|
| **z** (realized bundle) | Chosen job $(h_F, h_M, w_F, w_M)$; consumption $C = f(w_F h_F + w_M h_M, I)$ |
| **R** (preferences) | $v_i(C, h) \cdot \varepsilon_{ij}$ — heterogeneous via observed demographics (age, children) and unobserved random taste shifter $\varepsilon$ |
| **A** (feasible set) | Opportunity set $B_i(h, w)$ with density $g_i(h,w)$ and scale $g_{0i}$; varies by region (North/South), gender, local unemployment rate |
| **y** (pay schedule) | Italian 1987 tax-benefit system: 8-bracket progressive income tax (12%--62%), family benefits, tax credits |

**Key for framework:** The paper provides the first application of the RURO model where **opportunity constraints are central** to understanding labour supply in a country with high unemployment (especially female, especially Southern Italy). The parameter $g_0 < 1$ directly captures the **scarcity of the feasible set** $A$, and regional variation in $g_0$ shows how opportunities differ across circumstances.

**Unemployment as opportunity deficit:**
$$\rho = (1 - g_0)\varphi(0, 0)$$

This equation makes the **link between $A$ and observed outcomes** explicit: unemployment is the gap between desired and feasible participation, driven by insufficient opportunities ($g_0 < 1$).

---

## 3. Methodology

### 3.1 Labour Supply Model

**Utility:** $U_i(C, h, j) = v_i(C, h) \cdot \varepsilon_{ij}$, where $\varepsilon_{ij} \sim$ Gumbel (unit scale).

**Opportunity sets:** Each agent $i$ has:
- $B_i(h, w)$: set of market jobs at $(h, w)$ with $M_i(h,w)$ members
- $B_i(0, 0)$: non-market opportunities with $M_i(0,0)$ members
- $g_i(h,w) = M_i(h,w) / \sum_{x,y} M_i(x,y)$: conditional opportunity density
- $g_{0i} = \sum_{x,y>0} M_i(x,y) / M_i(0,0)$: ratio of market to non-market opportunities

**Choice probability:**
$$\varphi_i(h, w) = \frac{\Psi_i(h, w) \cdot g_{0i} \cdot g_i(h, w)}{\Psi_i(0, 0) + g_{0i} \sum_{x>0}\sum_{y>0} \Psi_i(x, y) g_i(x, y)}$$

where $\Psi_i(h, w) = v_i(f(wh, I), h)$.

### 3.2 Identification via Unemployment

In a "fair environment" ($g_0 = 1$), non-participation probability is $\tilde{\varphi}(0,0)$. Actual non-participation $\varphi(0,0) > \tilde{\varphi}(0,0)$ when $g_0 < 1$. The unemployment rate:
$$\rho = (1 - g_0)\varphi(0, 0)$$

$g_0$ is **non-parametrically identified** from the observed unemployment rate and participation rate.

### 3.3 Separability and Identification

Utility is assumed **separable**: $v(C, h) = v_1(C) \cdot v_2(h)$.

From the ratio $\varphi(h,w)/\varphi(0,0)$, the marginal utility of income $v_1(\cdot)$ is identified from variation in the tax function $f$ with respect to fixed costs of work $k$. The opportunity density $g_1(w|h)$ is then identified from the remaining variation.

### 3.4 Empirical Specification

**Systematic utility (couples):**
$$\log \Psi(C, h_F, h_M) = [\alpha_2(1-K_M)(1-K_F) + \alpha_3 K_F + \alpha_4 K_M] e^{\alpha_1 C}$$
$$+ [\alpha_6 + \alpha_7 \log A_M + \alpha_8(\log A_M)^2] \frac{L_M^{\alpha_5} - 1}{\alpha_5}$$
$$+ [\alpha_{10} + \alpha_{11}\log A_F + \alpha_{12}(\log A_F)^2 + \alpha_{13}CU6 + \alpha_{14}CO6] \frac{L_F^{\alpha_9} - 1}{\alpha_9}$$

where $L_k = 1 - h_k/8760$, $K_k = 1$ if spouse $k$ works, $A_k$ = age, $CU6$/$CO6$ = children under/over 6.

**Key feature:** The marginal utility of consumption differs by employment status ($K_F, K_M$) — this captures the underground economy effect in Italy, where non-reported income may supplement consumption when officially not working.

**Opportunity density of hours:** Uniform with a peak at full-time (1846--2106 annual hours, corresponding to 36--40 weekly hours):
$$g_{2k}(h) = \begin{cases} \gamma_k & h \in [0, 1846) \\ \gamma_k \theta_k & h \in [1846, 2106] \\ \gamma_k & h \in (2106, 3432] \end{cases}$$

$\theta_F = \exp(\alpha_{21})$, $\theta_M = \exp(\alpha_{22})$ — estimated full-time peaks.

**Opportunity scale:**
$$\log g_{0F} = \alpha_{15} + \alpha_{16} Reg_F + \alpha_{17} UE_F$$
$$\log g_{0M} = \alpha_{18} + \alpha_{19} Reg_M + \alpha_{20} UE_M$$

where $Reg = 1$ for northern Italy, $UE_k$ = local gender-specific unemployment-to-employment ratio.

**Wage density:** Log-normal with $\log W_k = \beta_{0k} + \beta_{1k} s_k + \beta_{2k} Exp_k + \beta_{3k} Exp_k^2 + \beta_{4k} Reg_k + \xi_k$.

---

## 4. Data

- **Country:** Italy
- **Source:** 1987 Survey of Household Income and Wealth (SHIW), Bank of Italy
- **Sample:** 2,953 married couples (husband and wife aged 20--68; excluding self-employed >20% of gross income)
- **Key descriptives (Table I):**
  - Male participation: 96%, female participation: 40%
  - Male mean hours: 1,995/year; female mean hours: 690/year
  - Male mean wage: 12,000 LIT/hour; female mean wage: 4,300 LIT/hour
  - Mean gross household income: 37,500 (1000 LIT); disposable: 27,900
- **Tax system:** 8 progressive brackets: 12% (up to 6M LIT) to 62% (over 600M LIT); individual-based since 1977

---

## 5. Key Results

### 5.1 Parameter Estimates (Tables II, III)

- Utility is strictly concave in consumption and leisure ($\alpha_1, \alpha_5, \alpha_9$ have correct signs)
- **Full-time peaks** strongly significant: $\theta_F = \exp(2.4) \approx 11$, $\theta_M = \exp(2.5) \approx 12$ — full-time jobs are about 11--12 times more prevalent than other hour levels
- **Northern region** has significantly more female opportunities ($\alpha_{16} = 0.7$, $t = 6.5$)
- **Unemployment effect** on female opportunities negative ($\alpha_{17} = -0.5$) but imprecise
- $g_{0i} < 1$ for both genders — **rationing is present**
- Wage equations: jointly estimated; education and experience returns concave; northern premium for males (0.175 log points)

### 5.2 Labour Supply Elasticities

**Aggregate (Table IV):**

| Elasticity | Males own-wage | Females own-wage |
|-----------|---------------|-----------------|
| Participation (uncomp.) | 0.046 | 0.654 |
| Conditional hours (uncomp.) | 0.007 | 0.078 |
| Unconditional hours (uncomp.) | 0.053 | 0.737 |
| Unconditional hours (comp.) | 0.098 | 0.742 |

**Key patterns:**
- Male labour supply is very inelastic (0.05 unconditional)
- Female labour supply is elastic, driven primarily by participation (0.65)
- **Strong cross-effects**: neutralize own-wage effects. A 1% wage increase for all workers yields only 0.06% increase in male hours and 0.25% in female hours (net of cross-effects)

**By income group (Table V):**

| Group | Males (uncomp. hours) | Females (uncomp. hours) |
|-------|----------------------|------------------------|
| Poorest 10% | 0.075 | 3.441 |
| Middle 80% | 0.062 | 0.832 |
| Richest 10% | —0.041 | 0.035 |

- Female elasticity for poorest decile: **3.44** — extremely responsive
- Female elasticity for richest decile: **0.04** — nearly inelastic
- Male elasticity turns **negative** for richest 10% (backward-bending)

### 5.3 Comparison with Hausman Approach (Table VI)

Colombino & Del Boca (1990) Hausman estimates for married women:
- Participation wage elasticity: 0.64 vs. this paper's 0.65 (similar)
- Unconditional hours wage elasticity: **1.18** vs. this paper's **0.74** (Hausman overstates by ~60%)

The Hausman approach exaggerates hours responses because it ignores quantity constraints and non-pecuniary job attributes.

### 5.4 Policy Simulations (Tables VII, VIII)

Three tax regimes (revenue-neutral):

| Regime | Part. F | Part. M | Gross income | Disp. income | Gini (disp.) |
|--------|---------|---------|-------------|-------------|-------------|
| 1987 rules | 0.40 | 0.96 | 36,600 | 27,300 | 0.238 |
| Proportional (26.3%) | 0.38 | 0.96 | 37,200 | 27,800 | 0.247 |
| Increased progression | 0.36 | 0.96 | 36,100 | 26,800 | 0.220 |

**Key findings:**
- **Tax changes have remarkably weak effects** on aggregate labour supply — due to strong cross-effects and inelastic male supply
- Proportional taxes: female participation drops slightly (0.40→0.38), male unchanged; disposable income Gini **rises** 4% (from 0.238 to 0.247) — redistribution worsens
- Increased progression: female participation drops to 0.36; Gini **falls** 7.6% (to 0.220) — more redistributive
- The degree of redistribution (Gini ratio): 0.94 (current) → 1.00 (proportional) → 0.86 (increased progression)

---

## 6. Theoretical Connections

### To RURO / Opportunity Models
- Extends Aaberge, Dagsvik & Strøm (1995) from Norway to Italy — same modelling framework but different institutional context (lower female participation, higher unemployment, underground economy)
- The **$g_0$ parameter** is central: Italy's low female participation is partly driven by $g_0 < 1$ (insufficient job opportunities), not just low preferences for work
- Regional variation in $g_0$ (North vs. South) directly measures **geographical inequality in opportunities**

### To Hausman Approach Comparison
- Demonstrates that the Hausman approach overstates hours elasticities by ~60% for married women — because it ignores job availability constraints and models choice along a budget constraint rather than over discrete jobs
- This finding reinforces the superiority of the job-choice framework for policy analysis

### To Equality of Opportunity
- The model structurally separates **preferences** ($v(\cdot)$) from **opportunities** ($g_0, g(\cdot)$) — this is exactly the decomposition needed for your $W(z, R, A; y)$ framework
- The definition of unemployment as $\rho = (1 - g_0)\varphi(0,0)$ is a **circumstance measure** — it captures involuntary non-participation due to insufficient opportunities
- Regional differences in $g_0$ (North vs. South Italy) are a form of **circumstance-based inequality in $A$**

---

## 7. Key Equations

**Choice probability:**
$$\varphi_i(h, w) = \frac{\Psi_i(h,w) g_{0i} g_i(h,w)}{\Psi_i(0,0) + g_{0i} \sum_{x,y>0} \Psi_i(x,y) g_i(x,y)}$$

**Unemployment rate:**
$$\rho = (1 - g_0)\varphi(0, 0)$$

**Couples choice probability:**
$$\varphi(h_F, h_M, w_F, w_M) = \frac{\Psi(h_F, h_M, w_F, w_M) g(h_F, h_M, w_F, w_M)}{D}$$

**Identification of $v_1$:**
$$\frac{\partial}{\partial k} \ln \frac{\varphi(h,w,I,k)}{\varphi(0,0,I,k)} = \frac{\partial v_1(f(hw,I,k))}{\partial f} \cdot \frac{\partial f(wh,I,k)}{\partial k} / v_1(f(wh,I,k))$$

---

## 8. Relevance to Your Job Market Paper

| Dimension | Relevance |
|-----------|-----------|
| **RURO model in different context** | Shows the Dagsvik framework works in a Southern European context with low female participation and rationing — validates cross-country applicability |
| **Opportunity constraints** | $g_0 < 1$ directly captures **scarcity of $A$**; regional variation (North/South) is a circumstance-based inequality in opportunities |
| **Structural unemployment** | $\rho = (1-g_0)\varphi(0,0)$ provides a structural decomposition of non-participation into preference-driven and opportunity-driven components — exactly the $R$ vs. $A$ decomposition |
| **Cross-country comparison** | Italy vs. Norway: much lower female participation (40% vs. 74%), much higher elasticities for poor women (3.44 vs. 1.85), illustrating how $A$ shapes observed outcomes |
| **Hausman critique** | Provides empirical evidence that the traditional approach overstates elasticities — strengthens the case for your RURO-based framework |
| **Tax simulation** | Weak aggregate effects of tax changes in Italy (due to inelastic males + cross-effects) contrasts with Norway — country-specific $A$ and $R$ matter |

---

## 9. Notable Data Points for Citation

- Italy 1987: female participation 40%, male 96%; mean female hours 690/year
- Full-time jobs ~11--12x more prevalent than other hour levels
- Female unconditional hours elasticity: 0.74 (vs. Hausman's 1.18 — 60% overstatement)
- Female elasticity by income: 3.44 (poorest 10%) vs. 0.04 (richest 10%)
- Male elasticity essentially zero (0.05) and negative for rich (—0.04)
- Proportional tax (26.3%) increases disposable income Gini from 0.238 to 0.247
- Increased progression reduces Gini from 0.238 to 0.220
- Northern Italy has significantly more female job opportunities than South
- $g_0 < 1$: rationing is empirically present in the Italian labour market
