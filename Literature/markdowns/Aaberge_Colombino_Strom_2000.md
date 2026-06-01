# Aaberge, Colombino & Strøm (2000) — Labor Supply Responses and Welfare Effects from Replacing Current Tax Rules by a Flat Tax: Empirical Evidence from Italy, Norway and Sweden

## Bibliographic Information
- **Authors:** Rolf Aaberge, Ugo Colombino, Steinar Strøm
- **Year:** 2000
- **Title:** Labor Supply Responses and Welfare Effects from Replacing Current Tax Rules by a Flat Tax: Empirical Evidence from Italy, Norway and Sweden
- **Journal:** *Journal of Population Economics*, 13(4), 595--621
- **JEL:** D19, H31, J22
- **Keywords:** labor supply, taxation, microeconometrics, cross-country analysis

---

## 1. Research Question & Contribution

**Central question:** What are the labour supply responses and welfare effects (measured by Equivalent Variation) of replacing the 1992 progressive tax systems in Italy, Norway, and Sweden with a revenue-neutral flat tax on total income?

**Core contribution:** This is the **first cross-country comparison** using the same structural RURO job-choice model estimated on data from three countries with very different labour markets and tax systems. The key findings are:

1. **Efficiency costs of progressive taxation** are positive in all three countries but vary enormously: 34.2% of tax revenue in Norway, 4.8% in Sweden, only 1.5% in Italy
2. **Rich households gain more** from flat tax in welfare (EV) terms in all three countries — a universal distributional pattern
3. **Majorities differ**: Norway has a majority of winners (99%), while Italy (59% losers) and Sweden (57% losers) have majorities of losers
4. **Cross-country differences in responses** are driven by differences in opportunity sets (hours rigidity, job availability) and initial tax progressivity, not just preferences

---

## 2. Relation to W(z, R, A; y)

| Component | Paper's operationalization |
|-----------|--------------------------|
| **z** (realized bundle) | Simulated $(h_F, h_M, w_F, w_M, C)$ for each household |
| **R** (preferences) | Country-specific Box-Cox utility $v(C, h_M, h_F)$; heterogeneous via demographics and random $\varepsilon$ |
| **A** (feasible set) | Country-specific opportunity densities $g_0 g(h, w)$; vary by region (Italy: North/South), education (Norway), unemployment (Italy) |
| **y** (pay schedule) | 1992 progressive tax system vs. flat tax at 23% (Italy), 25% (Norway), 29% (Sweden) |

**Key insight for framework:** The paper demonstrates that **the same policy experiment** (flat tax) produces dramatically different outcomes across countries because $R$ and $A$ differ. Norway's high efficiency cost (34.2%) stems from its very progressive 1992 system combined with elastic female labour supply and flexible opportunity sets. Italy's low efficiency cost (1.5%) reflects rigid hours, low female participation, and already-moderate progressivity. This is direct evidence that $W(z, R, A; y)$ is not separable — the interaction of preferences, opportunities, and the tax schedule matters.

---

## 3. Methodology

### 3.1 Model (Same RURO Framework)

The model is identical to Aaberge et al. (1995, 1999):

**Choice probability:**
$$\varphi_i(h, w, I) = \frac{\psi_i(h, w, I) g_{i0} g_i(h, w)}{\psi_i(0, 0, I) + g_{i0} \int\int \psi_i(x, y, I) g_i(x, y) \, dx \, dy}$$

**Equivalent variation:**
$$\tilde{V}_i(\text{EV}, f_0) = \tilde{V}_i(0, f_1)$$

where $f_0$ is the 1992 tax system and $f_1$ is the flat tax.

### 3.2 Country-Specific Specifications

**Utility functions:** Box-Cox transformation of disposable income (household consumption) and leisure for male and female. For Italy, an exponential form for consumption with participation dummies (to capture underground economy effects). For Norway and Sweden, standard Box-Cox.

**Opportunity densities:**
- **Hours:** Uniformly distributed with peaks at full-time for males (all countries). For females: full-time peak only in Italy/Sweden (rigid markets); both full-time and part-time peaks in Norway (flexible market with 46.5% part-time ratio)
- **Wages:** Log-normal with education, experience, and region effects
- **Job availability ($g_0$):** Estimated for Italy (depends on region and unemployment); for Norway (depends on education); not needed for Sweden (near-universal participation in 1981)

### 3.3 Data

| Country | Data source | Year | Sample size | Female part. |
|---------|-----------|------|-------------|-------------|
| Italy | SHIW (Bank of Italy) | 1987 | 2,960 couples | 38% |
| Norway | Tax return + survey | 1986/1992 | 1,640 couples | 77% |
| Sweden | HINK survey | 1981 | 1,700 couples | ~95% |

All samples: married couples, ages 20--68, self-employment income <20% of total.

---

## 4. Key Results

### 4.1 Labour Supply Elasticities (Tables 1--6)

**Aggregate uncompensated elasticities:**

| Country | Male (unconditional hours) | Female (unconditional hours) |
|---------|--------------------------|----------------------------|
| Italy | 0.053 | 0.737 |
| Norway | 0.28 | 0.91 |
| Sweden | −0.020 (conditional only) | 0.070 (conditional only) |

**Income-dependent pattern (universal across countries):**
- Poorest 10%: elasticities much higher (Italy F: 3.44, Norway F: 3.09)
- Richest 10%: elasticities near zero or negative (Italy F: 0.04, Norway F: 0.19, Sweden M: −0.047)
- This declining pattern is **consistent across all three countries**

**Cross-country differences in elasticity levels:**
- Norway highest (flexible hours, high part-time availability)
- Italy moderate (high participation elasticity, low hours elasticity due to rigidity)
- Sweden lowest (already near-full employment for both genders; rigid hours)

### 4.2 Labour Supply Responses to Flat Tax (Tables 7--9)

**Italy (flat rate 23.3%):**
- Female participation: 38.2% → 36.4% (slight decrease overall, but poorest rise 4.3→4.3%)
- Male participation: ~96% (unchanged)
- Weak aggregate effects due to hours rigidity and low initial progressivity

**Norway (flat rate 25.4%):**
- Female participation: 75.4% → 81.4% (large increase, especially poorest: 41.5→73.2%)
- Male participation: ~96→99% (approaches full employment)
- Conditional hours increase substantially for women: 1494→1756 (poorest), 2279→2311 (richest)
- Strong responses driven by flexible labour market and high initial progressivity

**Sweden (flat rate 29.5%):**
- Conditional hours: modest increases for females (1147→1188 poorest, 1847→1874 middle)
- Male hours slightly decrease for richest
- Weak effects due to already high participation and rigid hours regulation

### 4.3 Income Inequality (Table 10)

| Country | Gini (gross, 1992) | Gini (disp., 1992) | Gini (gross, flat) | Gini (disp., flat) |
|---------|-------------------|-------------------|--------------------|-------------------|
| Italy | 0.243 | 0.234 | 0.238 | 0.238 |
| Norway | 0.205 | 0.177 | 0.165 | 0.165 |
| Sweden | 0.192 | 0.164 | 0.202 | 0.202 |

**Key findings:**
- **Norway:** Both gross and disposable income inequality **decrease** under flat tax (Gini: 0.177→0.165) — poor households work much more, narrowing the income gap
- **Sweden:** Inequality **increases** (0.164→0.202) — rich benefit more from lower MTRs without offsetting labour supply responses from poor
- **Italy:** Near-unchanged (0.234→0.238) — weak behavioural responses in both directions

### 4.4 Welfare Distribution — Equivalent Variation (Tables 11--13)

**Norway (Table 12):**
- Mean EV = NOK 40,804 (34.2% of tax revenue) — very high efficiency cost of progressivity
- 99% winners; only 8.6% of poorest and 0.3% of middle are losers
- Mean EV for poorest winners: NOK 24,132; for richest winners: NOK 80,811
- Rich gain more in EV, confirming the inequality paradox

**Italy (Table 11):**
- Mean EV = ITL 164,000 (1.5% of tax revenue) — small efficiency cost
- **59% losers** overall; mean loss ITL −1,029; mean gain ITL 1,890
- Losers are concentrated in poorest (58.5%) and middle (60.1%)
- Rich have higher proportion of winners (48.2%) and larger gains

**Sweden (Table 13):**
- Mean EV = SEK 5,722 (4.8% of tax revenue)
- **57% losers** overall; 95.2% of poorest lose, 58.4% of middle lose
- Only richest have a majority of winners (96.4%)
- Mean loss: SEK −8,525; mean gain among richest winners: SEK 52,139

### 4.5 Cross-Country Pattern

In **all three countries**, the rich benefit more from the flat tax in welfare terms. But:
- Norway: almost everyone wins (including poor), and inequality actually falls
- Italy & Sweden: majority loses, and the welfare gains are concentrated among the rich
- The difference is entirely driven by different **behavioural responses** — which depend on **opportunity sets** (hours flexibility, job availability) and initial **tax progressivity**

---

## 5. Theoretical Connections

### To Equality of Opportunity / W(z,R,A;y)
- The cross-country comparison shows that the **same policy** produces different distributional consequences depending on the interaction of $R$, $A$, and $y$ — this is central to your framework
- The **EV welfare measure** uses own preferences (not reference $\bar{R}$), so the welfare comparison incorporates both efficiency and leisure-income tradeoffs
- The paper explicitly notes that **aggregating EV assumes utilitarian SWF** and requires cardinal comparable utility — motivating the search for more robust welfare criteria (like your framework)

### To Opportunity Constraints
- Norway's high part-time ratio (46.5%) vs. Italy/Sweden's rigidity (~20--21%) is a direct measure of **differences in $A$ across countries**
- The paper states: "Rigidity of working hours may explain why labor supply elasticities are low" — i.e., $A$ constrains the responsiveness of $z$ to changes in $y$
- Italy's $g_0 < 1$ (rationing) further constrains the feasible set

### To Optimal Tax Design
- Norway's 34.2% efficiency cost suggests the 1992 system was far from optimal — motivating the optimal tax exercise in Aaberge & Colombino (2006, 2013)
- Italy's low efficiency cost (1.5%) suggests its 1992 system was already near the efficiency frontier (though not necessarily optimal for equity)

---

## 6. Key Equations

**Choice probability:**
$$\varphi_i(h, w, I) = \frac{\psi_i(h,w,I) g_{i0} g_i(h,w)}{\psi_i(0,0,I) + g_{i0} \iint \psi_i(x,y,I) g_i(x,y) \, dx \, dy}$$

**Indirect utility:**
$$\tilde{V}_i(\text{EV}, f) = \max_{h,w} \max_{j \in B_i(h,w)} U_i(\text{EV} + f(hw, I), h, j)$$

**Equivalent variation:**
$$\tilde{V}_i(\text{EV}, f_0) = \tilde{V}_i(0, f_1)$$

---

## 7. Relevance to Your Job Market Paper

| Dimension | Relevance |
|-----------|-----------|
| **Cross-country comparison** | First application of RURO to 3 countries — shows $R$, $A$, and $y$ interact to produce different outcomes; validates the need for a framework like $W(z,R,A;y)$ |
| **Opportunity set differences** | Part-time ratios (Norway 46.5% vs Italy/Sweden ~20%) and $g_0$ directly measure cross-country differences in $A$ |
| **Inequality paradox** | Universal finding: rich gain more in EV from flat tax, even when income inequality falls (Norway) — motivates separating responsibility from circumstances |
| **Efficiency costs** | Vary 1.5%--34.2% across countries — demonstrates that welfare effects of $y$ depend on $A$ and $R$ |
| **Welfare measure limitations** | Authors acknowledge EV aggregation assumes utilitarianism and cardinality — motivating more robust approaches |
| **Elasticity heterogeneity** | Declining elasticities with income universal across 3 countries — robust structural feature |

---

## 8. Notable Data Points for Citation

- Revenue-neutral flat tax rates: 23% (Italy), 25% (Norway), 29% (Sweden)
- Efficiency costs of 1992 progressivity: 1.5% (Italy), 34.2% (Norway), 4.8% (Sweden) of tax revenue
- Norway: 99% winners from flat tax; Italy: 59% losers; Sweden: 57% losers
- Norway Gini (disposable) falls: 0.177→0.165 under flat tax
- Sweden Gini rises: 0.164→0.202 under flat tax
- Part-time ratio: 46.5% (Norway) vs. 23.5% (Sweden) vs. 20.9% (Italy)
- Female unconditional hours elasticity: 0.74 (Italy), 0.91 (Norway), 0.07 (Sweden)
- Poorest decile female elasticity: 3.44 (Italy), 3.09 (Norway) — extremely responsive
- Norwegian poorest female participation: 41.5%→73.2% under flat tax
