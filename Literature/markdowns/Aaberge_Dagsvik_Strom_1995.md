# Aaberge, Dagsvik & Strøm (1995) — Labor Supply Responses and Welfare Effects of Tax Reforms

## Bibliographic Information
- **Authors:** Rolf Aaberge, John K. Dagsvik, Steinar Strøm
- **Year:** 1995
- **Title:** Labor Supply Responses and Welfare Effects of Tax Reforms
- **Journal:** *The Scandinavian Journal of Economics*, 97(4), 635--659
- **Keywords:** labour supply, tax reform, equivalent variation, random utility, job choice, opportunity sets, Norway

---

## 1. Research Question & Contribution

**Central question:** What are the labour supply responses and distributional welfare effects of moving from Norway's highly progressive 1979 tax system toward (i) proportional taxation and (ii) the actual 1992 tax reform?

**Core contribution:** This is one of the **earliest applications** of the Dagsvik (1994) discrete/continuous job choice framework to tax reform evaluation. Key innovations:
1. Uses the **random utility job choice model** (precursor to RURO) where labour supply is modeled as choosing among heterogeneous "job packages" with hours, wages, and non-pecuniary attributes
2. Computes **Equivalent Variation (EV)** as the welfare metric — the money that must be added to disposable income under the initial system to make the household indifferent to the reform
3. Reports the **full distribution** of EV across households, not just the mean — showing that mean welfare gains can mask extreme heterogeneity across income groups
4. Demonstrates a **paradox**: proportional taxation reduces income inequality (Gini falls) while simultaneously benefiting the rich far more in welfare terms (EV)

---

## 2. Relation to W(z, R, A; y)

| Component | Paper's operationalization |
|-----------|--------------------------|
| **z** (realized bundle) | Chosen job $(h, w)$ — hours and wage rate; consumption $C = f(wh, I)$ |
| **R** (preferences) | Heterogeneous utility $U_i(C, h, j) = v(C, h) \cdot \varepsilon_{ij}(h, w)$ with systematic part $v(\cdot)$ varying by demographics and random taste shifter $\varepsilon$ varying across jobs and agents |
| **A** (feasible set) | Opportunity set $B_i(h, w)$ — set of jobs with hours $h$ and wage $w$ feasible to agent $i$; captured by opportunity density $g(h, w)$ and scale parameter $g_0$ |
| **y** (pay schedule) | Tax-benefit function $f(\cdot)$: three regimes compared — 1979 progressive, proportional (20.1% flat rate), and 1992 rules |

**Welfare metric:** Equivalent Variation defined via indirect utility:
$$\tilde{V}_i(0, f_1) = \tilde{V}_i(\text{EV}, f_0)$$
where $f_0$ is the initial (1979) tax system and $f_1$ is the alternative. This is **individual-specific** (uses each household's own $R$), so it is closer to $W(z, R, A; y)$ than to the common-welfare approach used in Aaberge & Colombino (2013).

**Key insight for framework:** The paper shows that even when you evaluate reforms using each household's own preferences (no reference $\bar{R}$), the **distributional implications** are highly sensitive to where you look in the distribution. The rich gain more in EV from proportional taxes despite income inequality falling — because the poor's welfare gain from increased consumption is offset by their welfare loss from reduced leisure (they work much harder).

---

## 3. Methodology

### 3.1 Labour Supply Model

**Utility structure:**
$$U_i(f(wh, I), h, j) = v(f(wh, I), h) \cdot \varepsilon_{ij}(h, w)$$

where $\varepsilon_{ij}(h,w)$ captures non-pecuniary job attributes (Gumbel distributed).

**Conditional indirect utility:**
$$V_i(h, w) = \psi(h, w) \cdot e_i(h, w)$$

where $\psi(h,w) = v(f(wh, I), h)$ is the systematic utility and $e_i(h,w) = \max_{j \in B_i(h,w)} \varepsilon_{ij}(h,w)$ is the best taste-draw among feasible jobs at $(h,w)$.

**Choice probability (continuous logit):**
$$\varphi(h, w) = \frac{\psi(h, w) \cdot g_0 g(h, w)}{\psi(0, 0) \cdot g_0 + \sum_{x>0}\sum_{y>0} \psi(x, y) \cdot g(x, y)}$$

where $g(h, w)$ is the conditional opportunity density — the fraction of feasible jobs with hours $h$ and wage $w$.

### 3.2 Couples Extension

For married couples (joint decision), the choice probability becomes:
$$\varphi(h_F, h_M, w_F, w_M) = \frac{\psi(h_F, h_M, w_F, w_M) \cdot g_{0FM} g_F(h_F, w_F) \cdot g_M(h_M, w_M)}{D}$$

where $D$ sums over all combinations of male/female/non-participation states, and $\psi(\cdot) = v(f(h_F w_F + h_M w_M, I), h_F, h_M)$.

### 3.3 Empirical Specification

**Systematic utility (couples):**
$$\log v(C, h_M, h_F) = \alpha_2 \frac{(10^{-4}C)^{\alpha_1} - 1}{\alpha_1} + \left(\frac{L_M^{\alpha_3} - 1}{\alpha_3}\right)(\alpha_4 + \alpha_5 \log A_M + \alpha_6(\log A_M)^2) + \left(\frac{L_F^{\alpha_7} - 1}{\alpha_7}\right)(\alpha_8 + \alpha_9 \log A_F + \alpha_{10}(\log A_F)^2) + \alpha_{11} CU6 + \alpha_{12} CO6 + \alpha_{13} L_F L_M$$

where $L_k = 1 - h_k/8760$, $A_k$ = age of spouse $k$, $CU6$ and $CO6$ = number of children under/over 6.

**Box-Cox nesting:** If $\alpha_1 = \alpha_3 = \alpha_7 = 0$, utility is log-linear; if $= 1$, linear. Estimated values allow flexible curvature.

**Opportunity density of hours:**
- Females: $\log g_{1F}(h_F) = d_F + \alpha_{19} D_1(h_F) + \alpha_{20} D_2(h_F)$ (peaks at full-time and part-time)
- Males: $\log g_{1M}(h_M) = d_M + \alpha_{18} D_1(h_M)$ (peak at full-time only)

**Wage opportunity density:** Log-normal, $E\log W_k = \beta_0 + \beta_1 s_k + \beta_2 \text{Exp}_k + \beta_3 \text{Exp}_k^2$

### 3.4 Welfare Measure: Equivalent Variation

**Definition:** $\tilde{V}_i(0, f_1) = \tilde{V}_i(\text{EV}, f_0)$

The unconditional indirect utility depends on:
- Preferences $v(\cdot)$
- Tax system $f$
- Non-taxable income $y$
- Opportunity density $g_0 g(\cdot)$ (kept fixed across reforms — partial equilibrium)

EV is simulated by drawing random $\theta_i(h,w)$ from the Gumbel distribution.

---

## 4. Data

- **Country:** Norway
- **Base year:** 1979 (tax return data + labour market data)
- **Sample:** Married couples (size not explicitly stated but implied ~1,800--2,000 from Statistics Norway registers)
- **Tax regimes compared:**
  1. **1979 rules:** Highly progressive; top MTR = 74% (decile X), bottom MTR = 32% (decile I)
  2. **Proportional tax:** Flat rate 20.1% (revenue-neutral with 1979)
  3. **1992 rules:** Moderately progressive; substantial reduction in top MTRs from 1979

---

## 5. Key Results

### 5.1 Labour Supply Elasticities (Table 3)

| Elasticity type | Males (poorest→richest) | Females (poorest→richest) |
|----------------|------------------------|--------------------------|
| Participation (Cournot) | 1.89→0.29 | 1.85→0.83 |
| Hours conditional (Cournot) | 0.29→0.03 | 1.04→0.99 |
| Unconditional hours (Cournot) | 2.23→0.06 | 3.09→1.49 |
| Unconditional hours (Slutsky) | 4.15→0.02 | 5.68→0.07 |

**Key finding:** Elasticities are **sharply declining with income** — the poor are far more responsive. Aggregate Slutsky elasticity: 0.33 (males), 1.59 (females).

### 5.2 Behavioural Responses (Table 4)

| Regime | Participation F | Participation M | Hours F | Hours M | Gross income | Disp. income |
|--------|----------------|----------------|---------|---------|-------------|-------------|
| 1979 | 74.2% | 93.7% | 1,043 | 2,132 | 136,279 | 95,656 |
| Proportional | 84.3% | 99.5% | 1,642 | 2,790 | 208,449 | 167,825 |
| 1992 | 74.5% | 96.0% | 1,178 | 2,331 | 156,720 | 107,911 |

Proportional taxes: +10 pp female participation, +6 pp male; hours +57% (F), +31% (M); gross income +53%.

### 5.3 Welfare Effects

**Proportional vs. 1979 (Tables 5A, 5B):**
- Mean EV = NOK 25,956 (64% of 1979 tax revenue) — large efficiency gain
- 99.4% of households are winners; only 0.6% losers
- **But:** The top 10% who gain most have mean EV = NOK 45,400 (avg gross income NOK 182,800). The bottom 10% who gain least have mean EV = NOK 1,600 (avg gross income NOK 84,500).
- Gini of EV gains = 0.303 for winners — **highly unequal welfare gains**

**1992 vs. 1979 (Tables 5A, 5B):**
- Mean EV = NOK 1,588
- Only 56.8% winners, 42.8% losers — much more contested
- Mean EV for top 10% gainers = NOK 4,572; bottom 10% losers = NOK -2,356

### 5.4 Inequality Paradox (Table 6)

| Regime | Gini (gross income) | Gini (disposable income) |
|--------|--------------------|-----------------------|
| 1979 | 0.196 | 0.161 |
| Proportional | 0.152 | 0.152 |
| 1992 | 0.205 | 0.177 |

**Paradox:** Proportional taxation **reduces** the Gini of both gross and disposable income (from 0.196/0.161 to 0.152/0.152) — but the rich gain far more in welfare (EV). The mechanism: the poor work much harder under proportional taxes (high elasticity), earning more but losing leisure. The rich's hours barely change but their disposable income rises sharply from lower MTRs.

### 5.5 Supply-Side Potential (Table 7)

Under lump-sum taxes (no distortion benchmark):
- Female hours: 48.2% of potential (1979), 76.0% (proportional), 54.5% (1992)
- Male hours: 72.2% of potential (1979), 94.5% (proportional), 78.9% (1992)
- Proportional taxes bring the economy to ~88% of its gross income potential

---

## 6. Theoretical Connections

### To Equality of Opportunity Framework
- The paper uses **own-preference EV** (not a common welfare function) — so welfare reflects individual $R$, not reference $\bar{R}$
- The **inequality paradox** (less income inequality but more welfare inequality for the rich) directly motivates the need for frameworks that separate **responsibility** (preferences/effort) from **circumstances** (opportunities): the poor work harder under proportional taxes because they have higher elasticities, not because of different preferences *per se*, but because their pre-reform choices were more distorted
- This tension between income equality and welfare equality is a key motivation for the Fleurbaey-Maniquet approach

### To Dagsvik (1994) / RURO
- This is one of the **first empirical applications** of the Dagsvik continuous choice framework
- The opportunity density $g(h,w)$ with peaks at full-time/part-time hours is the empirical precursor to the RURO opportunity measures used in later papers (Aaberge & Colombino 2006, 2013; Capeau et al. 2015)

---

## 7. Key Equations

**Utility:**
$$U_i(C, h, j) = v(C, h) \cdot \varepsilon_{ij}(h, w), \quad P(\varepsilon \leq y) = \exp(-1/y)$$

**Choice probability:**
$$\varphi(h, w) = \frac{\psi(h,w) \cdot g_0 g(h,w)}{\psi(0,0)g_0 + \sum_{x,y>0} \psi(x,y) g(x,y)}$$

**Equivalent variation:**
$$\tilde{V}_i(0, f_1) = \tilde{V}_i(\text{EV}, f_0)$$

**Indirect utility:**
$$\tilde{V}_i(y, f) = \max\left[\max_{h>0,w>0} \left(v(f(wh,I)+y, h) \cdot g_0 g(h,w) \cdot \theta_i(h,w)\right), v(f(0,I)+y, 0) \cdot \theta_i(0,0)\right]$$

---

## 8. Relevance to Your Job Market Paper

| Dimension | Relevance |
|-----------|-----------|
| **RURO / job choice** | First empirical implementation of Dagsvik (1994) continuous logit for policy evaluation — direct ancestor of your modelling approach |
| **Opportunity density** | $g(h,w)$ with hours peaks is the empirical $A$ in your framework; same identification strategy used in later papers |
| **EV welfare measure** | Uses own-preference EV, contrasting with common-welfare approaches — illustrates the choice your framework must make between $R$ and $\bar{R}$ |
| **Inequality paradox** | Income inequality falls but welfare inequality rises under proportional taxes — motivates the need for your decomposition of $W$ into preference vs. opportunity components |
| **Norwegian data** | Same institutional context; 1979 baseline complements the 1994 baseline used in Aaberge & Colombino (2013) |
| **Elasticity heterogeneity** | Sharply declining elasticities with income are a structural feature that drives all subsequent optimal tax results in this literature |

---

## 9. Notable Data Points for Citation

- Norway 1979: top MTR = 74%, bottom MTR = 32%
- Revenue-neutral proportional rate = 20.1%
- Mean EV from 1979→proportional = NOK 25,956 (64% of tax revenue)
- 99.4% of households are winners from proportional reform
- But top 10% gainers get EV = NOK 45,400; bottom 10% get only NOK 1,600
- Proportional taxes reduce disposable income Gini from 0.161 to 0.152
- Female participation: 74.2% (1979) → 84.3% (proportional) → 74.5% (1992)
- Aggregate unconditional Slutsky elasticity: 0.33 (males), 1.59 (females)
- Economy reaches 88% of supply-side potential under proportional taxes vs. 58--72% under 1979
