---
title: "Welfare Reform in European Countries: A Microsimulation Analysis"
authors: [Henrik Immervoll, Henrik Jacobsen Kleven, Claus Thustrup Kreiner, Emmanuel Saez]
year: 2007
outlet: "The Economic Journal, 117 (January), 1--44"
country_or_context: "EU-15 (15 European countries)"
population: "Working-age adults (18--59), all demographic groups"
data_period: "1998 tax-benefit systems (EUROMOD microsimulation)"
shelf: "optimal taxation / extensive margin / in-work benefits / microsimulation / equity-efficiency trade-off"
tags: [extensive-margin, participation-elasticity, intensive-elasticity, in-work-benefits, demogrant, working-poor, EITC, EUROMOD, microsimulation, equity-efficiency, welfare-reform, marginal-tax-rates, participation-tax-rates, Saez, Immervoll, Kleven, Kreiner]
priority: "high"
read_status: "extracted"
---

# Full citation

Immervoll, H., Kleven, H. J., Kreiner, C. T. and Saez, E. (2007). Welfare Reform in European Countries: A Microsimulation Analysis. *The Economic Journal*, 117 (January), 1--44.

# One-sentence contribution

Combines Saez (2002) optimal transfer formulas with the EUROMOD microsimulation model to compare the equity-efficiency trade-offs of two archetypal welfare reforms -- a demogrant (universal lump-sum transfer) and a working poor policy (in-work benefit) -- across 15 EU countries, showing that the working poor policy dominates because extensive-margin labour supply responses generate positive fiscal externalities that offset the deadweight loss of redistribution.

# Why this paper matters

This paper operationalises the Saez (2002) extensive-margin optimal tax theory for the first time in a cross-country European setting. It demonstrates that when participation elasticities are non-trivial (the empirical consensus), in-work benefit reforms dominate traditional demogrant/welfare expansions on equity-efficiency grounds across virtually all EU countries. The paper also provides the first systematic documentation of marginal and participation tax rates by earnings decile for all 15 EU countries, making the institutional heterogeneity across European welfare states quantitatively visible. It bridges theory and policy by showing that the post-1998 European trend toward in-work benefits (EITC-type programmes) is welfare-improving.

# Core research question

For 15 European countries, which type of small welfare reform produces a better equity-efficiency trade-off: (a) a traditional demogrant that increases transfers to all the poor (working and non-working), or (b) an in-work benefit that targets transfers exclusively to the working poor?

# Economic setting and context

EU-15 countries in 1998: Austria, Belgium, Denmark, Finland, France, Germany, Greece, Ireland, Italy, Luxembourg, Netherlands, Portugal, Spain, Sweden, United Kingdom. Institutional context varies enormously: Nordic countries have high taxes, high benefits, compressed wage distributions; Anglo-Saxon/Southern countries have lower taxes, more inequality. Several countries had not yet introduced in-work benefits as of 1998 (France introduced PPE in 2001, Netherlands ETC in 2001, Belgium EITC 2002--2004, Germany Mainzer Modell 2002, Finland and Denmark small programmes later). The UK and Ireland had existing in-work benefit programmes (WFTC/FIS).

# Model / theoretical framework

**Labour supply model (Section 1):** Continuum of agents $j = 1, \ldots, J$ earning $w_j$ when working. Quasilinear utility:
$$u_j = c - v_j(l) - q \cdot \mathbb{1}(l > 0)$$
where $c$ = consumption, $l$ = hours, $v_j(l)$ = disutility of work, $q$ = fixed cost of participation. Budget: $c = w_j l - T(w_j l)$ when working, $c = -T(0)$ when not working.

**Two behavioural margins:**
- *Intensive margin:* hours-of-work elasticity $\varepsilon$ (assumed constant across deciles, benchmark $\varepsilon = 0.1$)
- *Extensive margin:* participation elasticity $\eta_j$ (varies by decile, benchmark average $\eta = 0.2$, decreasing from 0.4 in decile 1 to 0 in deciles 9--10)

**Two reforms (revenue-neutral, marginal):**
1. *Demogrant:* uniform lump-sum transfer $\delta$ to everyone, financed by uniform increase in all marginal tax rates $d\tau$. Both extensive and intensive margins create efficiency losses.
2. *Working poor policy:* in-work benefit $\delta$ to all workers, financed by same $d\tau$. The extensive margin now generates a *positive* fiscal externality (new workers pay taxes and stop receiving benefits), partially or fully offsetting intensive-margin efficiency losses.

**Equity-efficiency trade-off measure $\Psi$:**
$$\Psi = -\frac{dL}{dG}$$
where $dG$ = welfare gain to gainers, $dL$ = welfare loss to losers, both in money-metric terms (equivalent variation). A lower $\Psi$ means the reform is cheaper per unit of welfare transferred:
- $\Psi = 1$: pure transfer, no deadweight loss
- $\Psi > 1$: each euro to the poor costs $\Psi$ euros to the rich
- $\Psi \to 0$: Pareto improvement (self-financing)

**Key formulas:**

Deadweight loss fraction for demogrant:
$$D_d = 1 - \frac{dR^{\text{mech}}}{d\tau} \cdot \frac{d\tau}{dR^{\text{total}}}$$

For working poor:
$$D_w = D_d \text{ (same deadweight from intensive margin)}$$
but the crucial difference is that $(1 - D_w)$ can be augmented by extensive-margin fiscal externalities.

Demogrant trade-off (eq. 16):
$$\Psi_d = 1 + \frac{D_d}{p_g(1 - D_d) - s_g}$$

Working poor trade-off (eq. 19):
$$\Psi_w = 1 + \frac{D_w}{e_g(1 - D_w) - s_g}$$

where $p_g$ = fraction of population gaining, $e_g$ = fraction of employed gaining, $s_g$ = fraction of switchers (non-workers induced into work). Key insight: $\Psi_d > \Psi_w$ always.

Ratio of deadweight contributions:
$$(1 - D_d)/(1 - D_w) = 1 - \sum_{j=1}^{J} \frac{a_j}{1 - a_j} \eta_j e_j$$
where $a_j$ = participation tax rate, $e_j$ = employment share. When participation tax rates $a_j$ are high at the bottom and participation elasticities $\eta_j$ are large there, the working poor policy has a much larger efficiency advantage.

# Key objects

- **$\Psi$ (equity-efficiency trade-off ratio):** welfare cost to losers per euro of welfare gain to gainers. The central evaluation metric.
- **$D_d$, $D_w$ (deadweight loss fractions):** fraction of mechanical revenue lost to behavioural responses. For demogrant, extensive responses always reduce revenue. For working poor, extensive responses can *increase* revenue.
- **Participation tax rate $a_j$:** $(T(w_j l_j) - T(0))/(w_j l_j)$, the fraction of earnings taxed away when moving from non-work to work. Reported by decile in Figure 2 for all 15 countries.
- **Marginal tax rate:** reported by decile in Figure 1 for all 15 countries, including income tax + SSC + benefit withdrawal.
- **Critical participation elasticities (Table 3):** threshold elasticities at which (a) working poor dominates demogrant, (b) working poor generates zero efficiency loss, (c) working poor is Pareto-improving.

# Data

EUROMOD -- the EU-wide tax-benefit microsimulation model -- applied to 1998 national household survey data for all 15 EU members. The model computes disposable income under counterfactual tax-benefit rules for every individual in each national survey. Marginal and participation tax rates are computed for each earnings decile by simulating small earnings changes. Population: adults aged 18--59, excluding students, retirees, and disability benefit recipients. Earnings deciles based on gross employment income among those with positive earnings. Unemployment benefit recipients estimated using OECD Labour Force Survey data on unemployment spells and statutory duration limits.

# Identification logic

Not causal identification in the econometric sense. The paper combines:
1. *Structural model:* Saez (2002) optimal transfer theory with known sufficient statistics (elasticities, tax rates, earnings distribution)
2. *Calibrated sufficient statistics:* participation and intensive elasticities drawn from the empirical literature
3. *Microsimulation:* EUROMOD computes the tax-benefit variables (marginal rates, participation rates, benefit levels) needed to evaluate the theoretical formulas

The approach is a calibrated welfare analysis: given elasticities and the existing tax-benefit system, what are the welfare consequences of marginal reforms?

# Estimation / empirical strategy

No econometric estimation. The paper is a calibrated simulation exercise. Key calibration choices:

**Participation elasticities (benchmark):** average $\eta = 0.2$, distributed as $\eta = 0.4$ (deciles 1--2), $\eta = 0.3$ (deciles 3--4), $\eta = 0.2$ (deciles 5--6), $\eta = 0.1$ (deciles 7--8), $\eta = 0$ (deciles 9--10). Based on extensive literature review: Eissa and Liebman (1996) find $\eta \approx 0.6$ for single mothers from EITC expansion; Blundell et al. (2000) find 2.2 pp participation increase for single mothers from WFTC; Card and Robins (1998) find treatment group nearly doubled participation from Canadian SSP experiment; structural estimates for European women find elasticities 0.5--1 (Van Soest 1995, Aaberge et al. 1999).

**Intensive elasticity (benchmark):** $\varepsilon = 0.1$ constant across deciles. Based on Blundell and MaCurdy (1999) survey: hours-of-work elasticity close to zero for prime-age males, small for females conditional on participation.

**Sensitivity analysis:** $\varepsilon \in \{0, 0.1, 0.2\}$; $\eta \in \{0, 0.1, 0.2, 0.3, 0.4\}$ averages; heterogeneous elasticities by demographic group (married women + lone parents vs. married men + singles).

# Treatment of preferences

Preferences enter only through two behavioural elasticities ($\varepsilon$, $\eta$). The quasilinear utility $u = c - v(l) - q$ rules out income effects on labour supply. Preferences are heterogeneous through the fixed cost $q$ (which generates the extensive margin) and the disutility function $v_j(l)$ (which generates the intensive margin). No cardinal utility comparisons are needed: the welfare criterion $\Psi$ uses money-metric (equivalent variation) welfare measures. The social planner is assumed to value consumption of the poor (gainers) and the rich (losers) equally in the $\Psi$ measure -- $\Psi$ measures efficiency, not equity. Higher welfare weight on the poor would make both reforms more desirable, but the *relative* ranking ($\Psi_w < \Psi_d$) is independent of welfare weights.

# Treatment of opportunities / constraints

The model assumes a perfectly competitive labour market: every individual can choose any hours level $l$ at their fixed wage $w_j$. The only constraint is the tax-benefit schedule $T(\cdot)$, which creates a wedge between gross and net income. The extensive margin is driven by fixed costs $q$ of participation (childcare, commuting, stigma), not by demand-side job availability constraints. Non-workers are assumed to be voluntarily not working given the tax-benefit system. Section 3 discusses (but does not model) labour market imperfections: minimum wages, unions, efficiency wages, search frictions. The paper argues that involuntary unemployment would *strengthen* the case for in-work benefits (discrete welfare gains for those obtaining jobs) and *weaken* the case for demogrants (increased unemployment from higher taxes).

# Welfare / normative object

The equity-efficiency trade-off $\Psi = -dL/dG$ is a positive measure, not a welfare function. It measures the efficiency cost of redistribution in money-metric terms. The paper does not commit to a specific social welfare function; instead, it provides the $\Psi$ values and notes that any redistributive SWF would prefer the reform with lower $\Psi$. The paper also examines majority support (fraction of population gaining) and distributional incidence (fraction gaining by family income decile) in Table 7.

The implicit welfare framework is utilitarian-compatible: social welfare improves when $\Psi < 1 + (1 - g)/g$ where $g$ is the social marginal welfare weight on the poor relative to the rich. For a Rawlsian ($g \to \infty$), any $\Psi < \infty$ is acceptable.

# Main findings

1. **Demogrant trade-offs are unfavourable (Table 2a):** For the benchmark case ($\eta = 0.2$, $\varepsilon = 0.1$), $\Psi_d$ ranges from 1.52 (Spain) to 25.25 (Denmark). Nordic countries have extremely high trade-offs (Denmark 25.25, Sweden 8.35, Finland 6.17) because generous existing benefits create large efficiency losses. Continental Europe has moderate trade-offs (France 4.32, Germany 4.38, Belgium 4.83). Southern/Anglo-Saxon countries have the lowest (Spain 1.52, Greece 1.66, UK 1.88).

2. **Working poor trade-offs are much more favourable (Table 2a):** $\Psi_w$ ranges from 0.00 (Denmark, Portugal) to 4.93 (Finland). For Denmark, Ireland, France, Portugal, and Spain, $\Psi_w < 1$, meaning the working poor policy generates an aggregate welfare *gain* -- it costs less than 1 euro from the rich to give 1 euro to the working poor. For many countries, $\Psi_w$ is close to 1 (Austria 1.50, UK 1.06, Netherlands 1.37).

3. **$\Psi_d > \Psi_w$ always (Theorem):** The working poor policy dominates the demogrant on equity-efficiency grounds in every country, for every elasticity specification tested.

4. **Participation elasticity is the key driver (Table 2b):** When participation elasticities are set to zero, both policies produce the same efficiency losses $-D$, but the demogrant has a *better* trade-off because it spreads gains more widely. The dominance of the working poor policy comes entirely from extensive-margin fiscal externalities.

5. **Critical elasticities are low (Table 3):** The average participation elasticity needed for the working poor to dominate the demogrant ($\Psi_w = \Psi_d$) is only 0.03--0.18 across countries (Panel a). The elasticity for the working poor to generate zero efficiency loss ($\Psi_w = 1$) is 0.10--0.45 (Panel b). The elasticity for a Pareto improvement ($\Psi_w \to 0$) is 0.20--1.15 (Panel c). Since empirical elasticities are generally above 0.2, the working poor policy is desirable in most countries.

6. **Hours-of-work elasticity matters for levels, not ranking (Table 4):** Higher $\varepsilon$ worsens both trade-offs proportionally, but the relative advantage of the working poor policy is preserved. At $\varepsilon = 0.2$, some country-reform combinations become infeasible ("No Gainers").

7. **Results are robust to unemployment benefit treatment (Table 5):** Excluding unemployment benefits narrows the gap slightly but the qualitative ranking is unchanged.

8. **Results are robust to elasticity heterogeneity (Table 6):** Concentrating participation elasticities on married women and lone parents (zero for married men and singles) produces very similar results.

9. **Majority support (Table 7):** The working poor policy commands majority support among the employed in most countries (column 2: 40--72% gaining). The demogrant commands majority support of the whole population only in Spain and Italy (column 1: 19--53%). The fraction of employed gaining from working poor is highest in bottom deciles (columns 3--12), so the policy redistributes toward low-income families despite being defined at the individual level.

10. **Discussion -- labour market imperfections (Section 3):** Involuntary unemployment strengthens the case for in-work benefits: newly employed workers get discrete utility gains. Minimum wages and search frictions mean a working poor policy increases job opportunities (lower equilibrium wages), while a demogrant reduces them. Dual labour market concerns (Kleven and Sorensen 2004) are a caveat: promoting bad jobs at the expense of good jobs may reduce welfare.

11. **Discussion -- externalities and behavioural economics (Section 3):** Positive externalities of employment (fiscal, reduced crime, role models for children) further favour in-work benefits. Behavioural economics (time inconsistency, procrastination in leaving welfare) also favours in-work benefits as they help correct internalities.

# Main limitations

- **No demand-side constraints:** The model assumes competitive labour markets with no rationing. Workers can always find jobs at their wage $w_j$. No job search, no unemployment duration, no vacancy constraints.
- **No general equilibrium effects:** Reforms may change wages and prices, but these effects are ignored.
- **Quasilinear utility:** No income effects, which simplifies the analysis but may overstate labour supply responses for some groups.
- **Static model:** No dynamics, no life-cycle considerations, no human capital accumulation, no savings.
- **Fixed elasticities:** The participation elasticity is assumed constant (or varies only by decile/demographic group), not estimated from the data.
- **Marginal reforms only:** The analysis applies to small perturbations of the existing system, not large reforms. The welfare analysis is local (first-order).
- **No non-workers benefit from in-work reform:** The working poor policy leaves non-workers (arguably the most disadvantaged) unaffected. If the government has strong Rawlsian preferences, the demogrant may be preferred despite higher $\Psi$ because it reaches the poorest.
- **Individual vs. family:** The reform is defined at the individual level, but welfare comparisons use family income deciles. A low-wage worker married to a high-wage spouse benefits equally.

# Relevance for my JMP

## direct relevance for the extensive-margin policy analysis
The paper provides the most comprehensive cross-country analysis of how participation tax rates and participation elasticities interact to determine the welfare effects of tax-benefit reforms. Since my RURO framework explicitly models the extensive margin through the opportunity density $g(h, w)$ and the participation decision, the paper's theoretical framework (Saez 2002 applied to EUROMOD) is a natural benchmark. My framework can extend this analysis by allowing the participation response to depend on job availability (demand-side), not just on preferences (supply-side).

## direct relevance for the equity-efficiency trade-off methodology
The $\Psi = -dL/dG$ measure is a money-metric welfare criterion that avoids specifying a full social welfare function. This is closely related to the equivalent-income approach: both measure welfare in money units. The paper demonstrates that the choice of reform type (demogrant vs. working poor) matters enormously for the efficiency cost of redistribution -- a finding my JMP can refine by incorporating demand-side constraints.

## direct relevance for the role of the participation tax rate
The paper shows that high participation tax rates at the bottom of the earnings distribution (Figure 2) are the key driver of the working poor policy's advantage. In my RURO framework, the effective participation tax rate includes not just the fiscal wedge $T(wl) - T(0)$ but also the opportunity cost of the jobs available (restricted by the opportunity density). Countries where low-skilled workers face both high fiscal participation taxes and limited job opportunities would have even stronger cases for in-work benefits.

# Research questions this paper inspires

1. How does the equity-efficiency trade-off $\Psi$ change when non-participation is partly involuntary (demand-side rationing)? If some non-workers cannot find jobs even with in-work benefits, the fiscal externality from extensive-margin responses is reduced, potentially narrowing the gap between $\Psi_d$ and $\Psi_w$. But the discrete welfare gain to those who do find jobs is larger (moving from involuntary unemployment to employment is a larger utility gain than from voluntary non-participation).

2. Can the RURO opportunity density $g(h, w)$ be used to decompose the participation elasticity $\eta_j$ into a supply component (preferences) and a demand component (job availability)? This would allow the $\Psi$ analysis to distinguish between countries where low participation is due to high taxes (supply) vs. few available jobs (demand).

3. The paper notes that the working poor policy leaves non-workers unaffected (p. 35, footnote 33). If we use Fleurbaey-Maniquet egalitarian-equivalent preferences (maximin over equivalent income), the non-workers with the lowest equivalent income would be the priority group. How does the optimal reform change when the SWF is explicitly Rawlsian rather than efficiency-focused?

# Challenge to this paper

The fundamental assumption is that non-workers are voluntarily non-participating: they choose not to work because the fixed cost $q$ exceeds the net-of-tax earnings gain. In European labour markets with high unemployment (especially youth and low-skilled), a significant fraction of non-workers may be involuntarily unemployed -- they would work at the prevailing wage but cannot find a job. For these workers, the participation elasticity with respect to in-work benefits is zero (they cannot respond to incentives because no jobs are available), and the fiscal externality from the working poor policy is smaller. The paper acknowledges this in Section 3 but does not model it. The RURO framework, where the opportunity density $g(h, w)$ can be thin or zero at low wages, captures exactly this constraint. In countries with high involuntary unemployment (e.g., Spain, Greece, Italy with participation rates of 59--64%), the effective participation elasticity may be much lower than the assumed $\eta = 0.2$, potentially making the working poor policy less dominant than the paper suggests.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The labour supply model with fixed costs (extensive margin) and continuous hours choice (intensive margin) maps directly into the RURO framework: $w_j$ is the wage, $l$ is hours, $T(\cdot)$ is the tax schedule, and $q$ is the fixed participation cost. The key difference is that the RURO model allows $w_j$ and $l$ to be drawn from an opportunity set $A_j$, while Immervoll et al. assume every worker faces a single fixed wage.

[Reasonable inference for my project] The $\Psi$ trade-off can be rewritten in terms of the RURO model's objects. The participation tax rate $a_j$ corresponds to $1 - (c_1 - c_0)/(w_j l_j)$ where $c_1$ is consumption when working and $c_0$ when not. The participation elasticity $\eta_j$ in the RURO model would depend not only on preferences (fixed cost $q$) but on the density of available jobs near the participation margin. Countries with thin opportunity densities at low hours/wages would have lower effective $\eta_j$ and hence smaller fiscal externalities from in-work benefits.

[Unclear from paper] How to integrate the $\Psi$ welfare criterion with the equivalent-income social welfare function used in Fleurbaey-Maniquet. The $\Psi$ measure is preference-free (money-metric), while equivalent income depends on a reference wage $\tilde{w}$. The two are complementary but their formal connection is not established.

# Relation to Bargain et al. (2013)

Direct methodological connection. Bargain et al. (2013) use EUROMOD and structural labour supply models to evaluate welfare in EU countries using the equivalent-income criterion (Fleurbaey-Maniquet). Immervoll et al. (2007) use the same EUROMOD infrastructure but with a different welfare criterion ($\Psi$ trade-off) and a different theoretical framework (Saez sufficient statistics rather than structural estimation). Both papers analyse marginal reforms; both emphasise the extensive margin; both use 1998 EU data. The papers are complementary: Immervoll et al. focus on the *type* of reform (demogrant vs. working poor), while Bargain et al. focus on *measuring* well-being under existing policies.

# Relation to opportunities vs preferences

The paper is entirely on the preferences/supply side: non-participation is voluntary (driven by fixed costs $q$ in preferences), and the participation elasticity measures the preference-side response to financial incentives. The opportunity set is assumed to be unrestricted -- any worker can work any hours at their wage. The paper's discussion section (Section 3) acknowledges that labour market imperfections create demand-side constraints (involuntary unemployment, wage rigidity, job rationing) and that these would likely strengthen the case for in-work benefits in some respects (discrete utility gains for the involuntarily unemployed who find jobs) but weaken it in others (lower effective participation elasticity). The RURO framework's explicit modelling of the opportunity density $g(h, w)$ addresses exactly this gap.

# Useful quotations / formulas

**On the central result (p. 1):**
"Our main finding is that, in most countries and for moderate elasticity values, the in-work benefit reform is significantly more efficient than the traditional demogrant reform."

**On the mechanism (p. 7, eq. 16 and 19):**
$$\Psi_d = 1 + \frac{D_d}{p_g(1 - D_d) - s_g}, \quad \Psi_w = 1 + \frac{D_w}{e_g(1 - D_w) - s_g}$$

**On critical elasticities (p. 28--29):**
"The participation elasticities are extremely low for most countries, typically around 0.05--0.1 and never above 0.2... the average participation elasticities at which the working poor policy generates zero efficiency loss... remain in the moderate range (around 0.25) for most countries."

**On the role of participation elasticities (p. 26):**
"The efficiency implications of welfare reform depend crucially on who is targeted by the reform, the poor or the working poor."

**On labour market imperfections (p. 36):**
"Following the introduction of in-work benefits, those who obtain jobs would experience a discrete (as opposed to an infinitesimal) increase in utility because some of them were previously involuntarily unemployed. This reinforces the positive effect of the working poor policy on welfare."

**On the caveat for Rawlsians (p. 35):**
"In the in-work benefit case, people with no earnings receive no additional support and redistribution benefits only the working poor... if the government had extreme redistributive tastes and put a much higher welfare weight on those with no incomes than on the working poor... increasing traditional welfare would be more desirable than introducing in-work benefits."

**On the dominance formula (p. 28):**
$$(1 - D_d)/(1 - D_w) = 1 - \sum_{j=1}^{J} \frac{a_j}{1 - a_j} \eta_j e_j$$

# Suggested tags

extensive-margin, participation-elasticity, intensive-elasticity, in-work-benefits, demogrant, working-poor, EITC, WFTC, EUROMOD, microsimulation, equity-efficiency, welfare-reform, marginal-tax-rates, participation-tax-rates, sufficient-statistics, Saez, Immervoll, Kleven, Kreiner, EU-15, cross-country, fiscal-externality, Pareto-improvement, labour-supply, fixed-costs

# My quick takeaway

The most comprehensive cross-country application of the Saez (2002) extensive-margin optimal tax theory, showing that in-work benefits dominate traditional welfare expansion (demogrants) across virtually all EU countries because the fiscal externality from participation responses more than offsets intensive-margin deadweight losses. The key quantitative finding is that the critical participation elasticity for this dominance is very low (0.03--0.18), well below empirical estimates. For my JMP, this paper establishes the baseline case for in-work benefits under the assumption of unconstrained labour markets -- my RURO framework can then ask how this conclusion changes when job availability is restricted. The paper also provides the essential EUROMOD infrastructure for any European welfare analysis and the $\Psi$ metric for evaluating reforms without committing to a specific SWF.
