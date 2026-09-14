# Unequal Job Opportunities and Well-Being Inequality: A Latent-Jobs Structural Decomposition

Hisham Haydar · University of Luxembourg and LISER

Build date: 14 September 2026.

## Abstract

We study how unequal job opportunities contribute to inequality in money-metric well-being. Our normative reference retains each household's own preferences and its own set of reachable jobs, while assigning the same disposable-consumption level to every job in that reference set; the money metric is the level at which the household's ex-ante evaluation of the reference matches the evaluation of the prospect it actually faces. We model labour supply as a choice among latent jobs and estimate preferences, job access and earning opportunities jointly on French EU-SILC data, with EUROMOD computing taxes, benefits and disposable income at every alternative work arrangement. Attributing the resulting inequality to preferences and circumstances in full requires a counterfactual-attainment estimand that is still under design; ahead of it, we introduce and implement a bounded, preliminary structural exercise, holding household resources, needs and composition fixed and simulating each household's attained well-being under counterfactual equalizations of preferences, local labour-market access and earning opportunities, with the interactions allocated by an exact three-player Shapley value. The movable inequality this bounded exercise reaches, $\Delta I$, is a small share of baseline inequality by construction, -1.8 to -9.9 per cent across samples and scales, because resources, needs and composition are held fixed throughout and those account for the large majority of the variance of log well-being. Within that bounded movable share, earning opportunities dominate local labour-market access for both single-adult and couple households, at every scale we report; the sign of the preference contribution is not robust between the unequivalised and equivalised reporting conventions in either sample, so we make no directional claim about it. This is a preliminary, model-based reading, not the paper's final decomposition architecture.

*Preliminary results throughout. The three-factor preferences/access/earnings decomposition in Section 5 is a bounded exercise ahead of the paper’s final decomposition architecture, which requires a counterfactual-attainment estimand still under design; it is reported with Monte Carlo simulation ranges and an independent second-seed check, never confidence intervals, and household resources, needs and composition are held fixed rather than decomposed.*

# 1. Introduction

Two people can work the same hours for the same hourly pay and be very differently placed. One chose that job from several that were open; the other took the only offer available. Their earnings are identical and their circumstances are not. Income comparisons record the outcome and cannot separate the two cases, and the difference matters for how unequal we should judge well-being to be.

The same ambiguity runs through the whole distribution. Low earnings can describe someone who values leisure highly and chose short hours, someone who cannot obtain a well-paid job, or someone whose family resources make a different work choice affordable. These are observationally entangled and economically different. A distribution of income is a distribution of outcomes with the explanations already mixed in.

The ambiguity matters for measurement, not only for interpretation. If we want to know how much of the inequality we observe is associated with unequal access to employment, hours arrangements and wage offers, we need two things that an income distribution does not supply. We need a behavioural model that separates what a household wanted from what it could reach, and we need a rule for comparing people whose opportunities and whose tastes both differ. Neither is optional: without the first there is nothing to attribute, and without the second there is no defensible way to say who is better off.

**The normative reference.** Comparing well-being when individuals face different job opportunities requires a reference that specifies how those opportunities enter the comparison. We draw on the own-set equal-consumption criterion of Haydar and Maniquet (2026), work in progress. In its deterministic formulation, the criterion assigns to an attained situation the consumption level that would make the individual's preferred job within their own ability set equally good, when every feasible job provides that same consumption. The reference therefore retains the individual's own opportunities and own preferences while removing variation in pay from the reference bundles. Writing $A_i$ for the jobs available to $i$ and $z_i$ for the attained situation, the reference level solves

$$u_i(z_i)=\max_{j\in A_i}\,u_i(W_i,j).$$

The argument being solved for is an amount of consumption, so the measure is money-metric by construction; there is no second conversion from an index into euros.


![**Own-set equal-consumption equivalents.** The theoretical W1 construction from the companion theory paper. Individuals with preferences $R_i,R_h$ and ability sets $A=\{j,k\}$ and $A^{\prime}=\{k,\ell\}$ attain $z_i$ and $z_h$. For each individual, a common consumption level is assigned to every job in their own set; the level at which the preferred reference job becomes indifferent to the attained bundle is the money metric. Adapted from Haydar and Maniquet (2026), work in progress. This is the deterministic construction; the estimated measure is its ex-ante extension, defined in Section 4.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v5/theory_w1.png){width=95%}


The first figure depicts the theoretical W1 construction adapted from the companion theory paper by Haydar and Maniquet (2026). It constructs a deterministic own-set equal-consumption equivalent, using each individual's preferred reference job. We then adapt this principle to an estimated distribution of latent jobs. The empirical object is its stochastic, ex-ante counterpart: the household's evaluation of the reference prospect, integrated over the jobs it may reach, is set equal to its evaluation of the prospect it actually faces. Section 4 states that implementation and derives its closed form; the deterministic figure does not depict an estimated welfare result.

One comparative static is worth stating plainly at the outset, because it is easy to misread. Holding the attained situation fixed, a person with a larger reference menu may need less uniform consumption to reach the same satisfaction. When actual opportunities change, however, both the attainment and the reference menu change. The net effect on equivalent consumption depends on both. Measuring attainment against one's own opportunities is therefore not a claim that larger menus are intrinsically better, and we make no such claim.

**The empirical approach.** The behavioural half is a random-utility, random-opportunity model of job choice. A job is a package: an employment state, an occupation, a weekly hours arrangement and an hourly wage. Households rank packages by consumption and leisure, and the packages differ in how available they are. Both the preferences and the household-specific intensity of availability enter one likelihood and are estimated jointly; neither is observed as a complete schedule. Every package is priced through the French tax-benefit system, so a change of hours or occupation moves disposable income through the actual schedule of taxes and transfers rather than a linear approximation. We estimate the model separately on 1,540 single-adult and 2,223 couple households drawn from French EU-SILC, with couples choosing jointly under a shared household budget.

The normative half then yields, for each household, an equivalent flat consumption level. Attributing its inequality to preferences and to circumstances in full requires a counterfactual-attainment estimand for the bundle a household would attain under a counterfactual environment, and that estimand is still under design. Ahead of it we report a bounded, preliminary exercise: we define three structural equalization operators, one for preferences, one for local labour-market access and one for earning opportunities, holding household resources, needs and composition fixed throughout; we recompute every household's welfare level, and the inequality of the resulting distribution, under each of the eight coalitions of those three operators, reusing the model's own already-priced estimation panel with no re-estimation and no new pricing; and we allocate the interactions among them with an exact three-player Shapley value. The allocation is exhaustive by construction and the closure is verified numerically rather than imposed.

**What we find.** The movable inequality this bounded exercise reaches, $\Delta I=I(\text{actual})-I(\text{P,A,B equalized})$, is small by construction: -1.8 to -9.9 per cent of baseline inequality across samples and reporting scales. That is a property of the design, not evidence that opportunities are unimportant: household resources, needs and composition are held fixed in every coalition, and that fixed component alone accounts for 127 to 100 per cent of the variance of log well-being. Within the movable share, earning opportunities dominate local labour-market access for both household types, at every scale we report, from 58.6 per cent of $\Delta I$ (single adults, unequivalised) to 124.0 per cent (couples, equivalised); local labour-market access is second and smaller throughout. We report that ordering as a finding and do not attach a mechanism to it.

Two qualifications belong with the headline. First, the preference contribution's sign is not robust between the unequivalised and equivalised reporting conventions, in either sample: we therefore make no directional claim about it, only about the ordering of access against earnings. Second, an allocated share is an average of marginal contributions over coalition orders. It is not the reduction that equalizing that factor alone would achieve; Section 5 reports both and explains why they can differ, and reports the exact scale at which excluding the model's anchored-attainment arm moves $\Delta I$, as a robustness check on the design rather than on the estimates. This is a bounded, preliminary reading, reported ahead of the paper's final decomposition architecture, and it should be read as such throughout.

**Relation to existing work.** Every ingredient here has antecedents, and the contribution is the combination and the empirical answer, not any one step.

Modelling labour supply as choice among latent jobs, with preferences and offer intensities identified jointly from one likelihood, is due to @aaberge1995 and @aaberge1999, developed by @dagsvikstrom2006 and @dagsvikjia2016, surveyed by @aaberge2018, and set out for applied work by @capeau2016. We inherit that framework, including its distinction between the intensity of an offer and the probability of a choice, and its reliance on excluded opportunity shifters to separate components that choices alone identify only jointly. @capeau2016 also supply two of the identifying restrictions we maintain: the wage-offer distribution is independent of offered hours, and a local unemployment measure shifts availability while being excluded from preferences. Their Belgian application already covers single women, single men and couples, so covering both household types is not itself a contribution.

Combining such a model with a monetary welfare evaluation is also established. @aaberge1995 translate attained utility into an equivalent income against a stated reference household, choice set and tax system, and @aaberge2004 evaluate reforms with joint household choice and restricted hours. @jiathoresen2021 make the case for the job-choice model in exactly this role and report a distribution of compensating variation for a Norwegian reform, and @jacquet2026 compare a standard compensating variation with one computed after replacing preference characteristics by reference values. All four evaluate a *change* between policy regimes. Our object is a cross-sectional distribution of levels under one policy system, and its attribution. A reform gain and a level have different origins and different denominators; a small preference-related reform difference would not imply a small preference share in our decomposition, and our shares do not estimate their reform gains.

The normative half draws on the literature that refuses to resolve interpersonal comparison by assuming common preferences. @fleurbaeymaniquet2006, @fleurbaeymaniquet2017 and @fleurbaeymaniquet2018 set out how a reference bundle encodes a position on compensation and responsibility; @decosterhaan2015 and @bargain2013 show empirically how much a welfare ordering moves with that choice. Their references fix a wage or an unearned-income intercept and maximize over a deterministic budget set. Ours fixes consumption across the alternatives of an estimated opportunity distribution and integrates. That is a different reference and, as Section 6 records, the ordering is sensitive to it.

The closest decomposition precedents are two. @muehlhan2023 combines a structural labour-supply model with involuntary-unemployment restrictions and a Shapley attribution, decomposing the change in German household *income* inequality into temporal factors and binary restrictions. @creedyherault2011, in the section that constructs money-metric distributions under alternative policy and population states, decompose a change in inequality and social welfare by averaging over the two orders in which policy and population can be changed; theirs is the closest money-metric welfare-inequality decomposition we know. Both are decompositions of a *change* between two situations, with policy, population or temporal factors as the factors. Ours is a decomposition of a cross-sectional *level* of well-being inequality, with the factors defined as structural operators inside an estimated job-choice model: what a household prefers, which jobs it can reach, what those jobs pay, and what its budget and needs are. The wider behavioural-simulation decomposition tradition, @bargain2012 and @jessen2019, decomposes income changes in the same spirit.

The allocation rule is inherited outright. @shorrocks1982 states the accounting requirements a decomposition should satisfy; @shorrocks2013 places the Shapley value at the centre of distributional decomposition; @owen1977 supplies the value for games with a priori unions, which is what a grouped allocation requires; @sastretrannoy2002 documents how much the answer can depend on how the exercise is set up; and @audoly2025 give the contemporary practitioner's account of the grouped nonlinear case we use. We claim no new allocation principle. Complete recomputation of every coalition, rather than a linear approximation, likewise has precedents and is better described as methodological discipline than as a contribution.

What is new, to our knowledge, is the conjunction: a random-utility random-opportunity model of job choice, an opportunity-sensitive money-metric welfare level built on the own-set equal-consumption reference, a structural preference/access/earnings/resources game whose operators are defined inside that estimated model, complete recomputation of welfare and inequality under every coalition, and a grouped allocation of the result. The application-specific methodological contribution is the game and its counterfactual operators. The cooperative-game allocation rule is inherited.

**Roadmap.** Section 2 describes the data and the household budget construction. Section 3 presents the latent-jobs model, its identifying restrictions and its estimation. Section 4 defines the money-metric welfare measure and the structural decomposition. Section 5 reports the behavioural and welfare results for both household types. Section 6 examines sensitivity and states the limitations. Section 7 concludes.

# 2. Data

The data are French EU-SILC, collection year 2016, with income reference year 2015. Taxes, benefits and disposable income are computed by EUROMOD [@sutherlandfigari2013] under the French 2015 policy system, which is the system in force over the income reference period. We use the same three dates consistently: the survey is collected in 2016, incomes refer to 2015, and the simulated policy system is 2015.

## The estimation samples


Table: Sample construction. Unweighted households remaining after each screen, from the France 2016 EUROMOD input file to the two estimation samples. Rows are sequential; the counts are read from the frame records and are not reconstructed by subtraction.

|Screen|Single-adult|Couple|
|---|---|---|
|the raw France 2016 input file|4,038|5,965|
|one- or two-adult households (composition screen)|4,038|5,965|
|every adult aged 20 to 60|2,131|3,662|
|no adult still in education|2,036|3,521|
|no old-age, disability or survivor pension receipt|1,755|3,218|
|labour status in scope|1,598|2,412|
|no other employable or earning member|1,564|2,323|
|observed hours and wage inside the calibrated support|1,555|2,275|
|hours outside [5,70] or unsupported military occupation (ISCO 0) on an employed decider|1,543|2,223|
|observed chosen alternative priced at non-positive disposable consumption|1,540|2,223|
|**Estimation sample**|**1,540**|**2,223**|



The screens are of three kinds and it is worth separating them. The first two define the decision unit: the household must contain either one unpartnered adult or two mutually linked adults of opposite sex, and every decider must be between twenty and sixty. This is the largest exclusion and it is structural. Multi-generational households, flat-shares, adult children living with parents and same-sex couples are outside the estimated population, and no result extends to them. Because the age screen binds on both spouses, it removes proportionally more couples than singles.

The second kind removes households for whom the model does not define an offer set: adults in full-time education, households receiving an old-age, disability or survivor pension, and deciders whose labour-market status lies outside employment, unemployment and inactivity. Together with the pension screen this is why the surviving employment rate is high. The employment share below should be read as a share among people for whom working is a live option, not as a French employment rate.

The third kind is support. An employed decider's observed hours must lie in the closed interval $[5, 70]$ hours per week and the delivered hourly wage in $[2, 590]$ euros per hour, because those are the boundaries of the supports the opportunity densities are defined on. An observed occupation must map into the four modelled groups; ISCO 0, the armed forces, does not, and the resulting exclusion is *unsupported* occupation, not missing occupation. Three single-adult households whose own observed job prices to non-positive disposable consumption are removed, because the log-consumption term is undefined at their observed choice; non-positive *simulated* alternatives receive a one-euro consumption floor before utility is evaluated. The floor applies to 22,597 single-adult and 59,821 couple node-evaluations; these alternatives enter both the attained integral $J$ and the reference integral $H$.


Table: The four occupation groups. ISCO-08 major groups are aggregated into four modelled groups; group 1 is the omitted reference in the estimated occupation block. This is a research aggregation adopted for this paper, not an ILO classification. ISCO 0, the armed forces, has no modelled alternative and is a sample screen; that is unsupported occupation, not missing occupation.

|Model group|ISCO-08 major groups|Description|
|---|---|---|
|1 (reference)|6--9|Skilled agricultural, craft, plant and machine operators, and elementary occupations|
|2|5|Service and sales workers|
|3|4|Clerical support workers|
|4|1--3|Managers, professionals, technicians and associate professionals|



## What the households look like


Table: Descriptive means on the estimation samples. Weighted by the household cross-sectional weight; one row per household, with spouse-specific variables carried on the household row. Hours and wages are conditional on employment. These are observed inputs, not model predictions.

|Measure|Single-adult decider|Couple man|Couple woman|
|---|---|---|---|
|Age (years)|41.1|39.8|37.8|
|Children under 20|--|--|--|
|Usual weekly hours, employed|37.6|41.1|35.8|
|Delivered hourly wage, employed (EUR/hour)|--|--|--|
|Households (unweighted)|1,540|2,223||




![Weighted distributions on the estimation samples: age, usual weekly hours among employed deciders, education, and the delivered hourly wage input. Observed inputs, not model predictions.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v5/figV08_data_panel.png){width=95%}


Education is the three-level ISCED grouping, with the medium level as the omitted reference in the wage equation. Potential experience is years since leaving education, entering the wage equation in units of 20 years, with the square recomputed after scaling rather than carried forward. A child is any resident household member under 20, counted without a parent link. Age enters preferences centred on the sample mean decider age and divided by 10 years.


Table: Observed joint participation regimes among the 2,223 estimated couple households. These are joint regimes, not two spouse marginals.

|Regime|Meaning|Weighted share|Mean hours, man|Mean hours, woman|
|---|---|---|---|---|
|BB|both spouses employed|0.8435|41.0|35.9|
|MO|man employed, woman not employed|0.0796|41.5|0.0|
|WO|woman employed, man not employed|0.0547|0.0|35.0|
|NN|neither spouse employed|0.0222|0.0|0.0|



## The household budget

For a given work arrangement the tax-benefit model is given the implied gross labour inputs, weekly hours, hourly wage, and earnings split at the thirty-five hour threshold, together with the household's non-labour inputs and roster, and returns disposable income. Only deciders receive counterfactual overrides; other members keep their baseline values. The accounting identity linking original income, benefits, taxes and social contributions to disposable income holds to machine precision at both the person and the household-alternative level, before and after the benefit take-up adjustment. Disposable income is summed over all resident members of the household.


![Weighted distributions on the estimation samples: simulated disposable income at the observed job, children under twenty, the incidence of non-labour budget inputs by family, and urbanisation. Panel (a) is a tax-benefit output evaluated at the observed choice; panel (c) reports inputs to that calculation. The two are never added, and stocks are never summed with monthly flows.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v5/figV09_resources_panel.png){width=95%}


Panel (c) of the figure reports the *incidence* of non-labour budget inputs by family, not a cash total. Some of these are stocks, some are annual flows and some are monthly; they are inputs to the tax-benefit calculation and are not added together into one income concept. The pension family is empty by construction, because pension receipt is a sample screen. Panel (a) reports the tax-benefit *output* at the observed job, which is an object of a different kind and is never added to panel (c).

Local labour-market conditions enter through a group unemployment measure, a population-weighted exposure index for the decider's region and age-education cell, stored as a fraction and entering the employment index multiplied by 10. Regional and urbanisation variation supports the access specification conditional on the exclusion restriction and the functional form; it does not by itself identify access, and no causal effect of geography is claimed anywhere in this paper.

# 3. A latent-jobs model of household labour supply

A job is a package $j$: an employment state $e\in\{0,1\}$ and, when employed, an occupation $k\in\{1,\dots,4\}$, weekly hours $h\in[5,70]$ and an hourly wage $w\in[2,590]$. The base measure $\nu$ places counting mass on the single non-employment point and, on the employed part, counting measure over occupations with Lebesgue measure over hours and wages. A household chooses one package; a couple chooses one pair of packages under a shared budget.

## Preferences

Let $C_i(j)$ be priced monthly disposable consumption at $j$ and $\ell_i(j)$ normalized leisure, $(80-h)/10$ hours per week, floored at one hour. For a single adult of sex group $g$, deterministic utility is

$$
u_{ij}=\underbrace{\beta_{\ell}^{g}(\mathbf x_i)\;
\mathcal B\!\left(\tilde\ell_{ij};\theta_{\ell}^{g}\right)}_{L_{ij}}
\;+\;\beta_c\log\tilde c_{ij},
\qquad
\beta_{\ell}^{g}(\mathbf x_i)=\beta_{\ell 0}^{g}+\beta_{\ell a}^{g}a_i
+\beta_{\ell a^{2}}^{g}a_i^{2}
+\mathbb 1\{g=\text{women}\}\,\beta_{\ell k}^{g}k_i,
$$

where $\mathcal B(z;\theta)=(z^{\theta}-1)/\theta$ with $\mathcal B(z;0)=\log z$, $\tilde\ell_{ij}$ is normalized leisure, $\tilde c_{ij}=C_{ij}/\lambda_c$, $a_i$ is centred age in decades and $k_i$ is the child count. For a couple the index is additive across spouses with no direct cross-leisure term,

$$
u_{ij}=\beta_{\ell}^{m}(\mathbf x_i)\,\mathcal B(\tilde\ell^{m}_{ij};\theta_{\ell}^{m})
      +\beta_{\ell}^{f}(\mathbf x_i)\,\mathcal B(\tilde\ell^{f}_{ij};\theta_{\ell}^{f})
      +\beta_c\log\tilde c_{ij},
$$

with consumption the tax-unit sum over all members. We write $L_i(j)$ throughout for the complete non-consumption part of the index, which for a couple contains both leisure terms.

Three features of this specification are decisions and are worth naming. The consumption curvature is exactly zero, so the consumption term is $\beta_c\log(C/\lambda_c)$ and the marginal utility of consumption is $\beta_c/C$, independent of the normalizer. The consumption weight $\beta_c$ is **estimated**, not fixed at one. And the random-utility shock is i.i.d. type-I extreme value with scale one, so utility is measured in the natural unit of that scale. Fixing the shock scale is a normalization; additionally fixing $\beta_c$ would be a substantive restriction relative to that normalization, and estimating $\beta_c$ removes it. Neither step identifies an absolute cardinal utility scale, and fixing the consumption functional form is not by itself what identifies the shock scale.

The normalizer $\lambda_c$ is a units convention. Under exact log consumption it enters the index as the alternative-invariant constant $-\beta_c\log\lambda_c$, so it cancels from every choice probability and, as shown below, exactly from the welfare measure.


> **Why the leisure coefficients are not the preferences.** A leisure weight is a coordinate in a chosen normalization, not an economic magnitude. Changing the leisure normalizer $\lambda_\ell$ multiplies the weight and its box endpoints by the same factor, and the indifference curves and the marginal rate of substitution are unchanged exactly. The panels below therefore show the invariant objects; the coefficient table is a coordinate readout. Reparameterization also does not bear on whether a bound binds, since the endpoint moves with the coefficient. What settles that is re-estimation with wider bounds, and nothing else.


![Leisure-normalizer sensitivity. Under a change of normalizer the coefficients move by more than an order of magnitude while the indifference curves and the marginal rate of substitution coincide exactly. This is a coordinate change of the estimated model, not a re-estimation, and it does not bear on whether a bound binds: reparameterization multiplies a coefficient and its box endpoint by the same factor.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v5/figP06_normalization_sensitivity.png){width=95%}



## Opportunities

The opportunity density gives the relative intensity with which packages are available to household $i$, before any choice is made. It is a product of **four** factors, switched off on non-employment by the employment indicator $E_{ij}=\mathbb 1\{h_{ij}>0\}$:

$$
g_{ij}=g^{E}_{ij}\cdot\left(g^{H}_{ij}\cdot g^{\mathrm{Occ}}_{ij}\cdot g^{W}_{ij}\right)^{E_{ij}} .
$$

**Access**, $g^{E}_{ij}=\exp\{\beta_E+\beta_s s_i+\sum_{r=2}^{8}\beta_r\,\mathrm{reg}_{ir}+\beta_u u_i+\beta_m m_i\}$, carries the local group unemployment measure $s_i$, the region indicators and urbanisation, and is the factor inside which local-market access lives. **Hours**, $g^{H}_{ij}=\exp\{\sum_b \beta_b\mathbb 1\{h_{ij}\in b\}\}$, elevates five bands over a residual reference set of total width 26.5 hours per week, so every band coefficient is read against that residual and none of the five is normalized to zero; the narrow full-time band $[33.5,36.5)$ is a density elevation over an interval, not an atom at thirty-five hours. **Occupation**, $g^{\mathrm{Occ}}_{ij}=\exp\{\beta^{\mathrm{occ}}_{k,g}\}$ with $\beta^{\mathrm{occ}}_{1,g}\equiv 0$. **Wage offer**, $g^{W}_{ij}$, is log-normal with location $\mu_i=\beta_{w0}+\beta_{wL}L_i+\beta_{wH}H_i+\beta_{wx}x_i+\beta_{wx^{2}}x_i^{2}+\delta_{\mathrm{occ}}$ and dispersion $\sigma$, truncated to $[2,590]$ euros per hour and renormalized on that support.

Two properties of the normalization matter later. Write $\widehat g_{ij}=g_{ij}/Z_i$ for the density normalized to unit mass on the whole package space. The wage factor integrates to one *conditional on employment and occupation*, because the truncated density is renormalized on its own support; and the non-consumption index $L_{ij}$ has no wage argument. Together these give the reference the pay-neutrality property established in Section 4.

The four blocks are what the decomposition later separates. Employment and occupation access are one mechanism; the distribution of wages conditional on an occupation is another; neither is the same as non-labour resources or household needs.


> **What the kernel adds, concretely.** Two employed single adults can share an employment state, an occupation group, an hours band and an observed-wage quintile, and still differ substantially in their estimated opportunity kernels: the mass the kernel places on employment, the shape of the hours density, the occupation mass and the conditional wage location are all household-specific. Two people who look identical in an income table are, in this model, facing different menus. An earlier draft illustrated this with a matched pair of households; that illustration was drawn at the superseded consumption numeraire and is not reproduced here rather than shipped with a disclaimer.


## Identification, in words

Choices alone do not separate a taste for leisure from a scarcity of jobs at that number of hours. Three kinds of restriction do the work. Preferences are smooth in hours through the leisure index, while the opportunity density is a step function over bands, so a spike in observed hours at a band is read as availability rather than as a kink in tastes. Excluded shifters enter availability and not preferences: the local group unemployment measure and the regional and urbanisation indicators shift the employment index and appear nowhere in utility. And the wage-offer distribution is specified as independent of offered hours conditional on occupation, which separates the wage location from the hours density. These are the restrictions of @capeau2016 and @dagsvikjia2016, maintained here rather than tested. The regional variation supports the access block conditional on those restrictions; it does not establish separate identification on its own, and it is not a causal design.

## Estimation

The choice set is a continuum, so the likelihood is evaluated over sampled alternatives. For each household we draw $R=100$ alternatives from a proposal density $q_{ij}$ and place the observed package in the set as well, giving a set $\mathcal C_i$ with $|\mathcal C_i|=101$ rows. Write the sampled-set index

$$
V_{ij}=u_{ij}+\log g_{ij}-\log q_{ij},
\qquad
q_{ij}=q^{E}_{ij}\left(q^{H}_{ij}q^{W}_{ij}q^{\mathrm{Occ}}_{ij}\right)^{E_{ij}} .
$$

The contribution of household $i$ is then the conditional probability of its observed package $y$ within that set,

$$
\Pr\!\left(y\mid\mathcal C_i\right)=
\frac{n_{y}\exp V_{iy}}{\sum_{s\in\mathcal C_i}\exp V_{is}} .
$$

The denominator runs over slots rather than distinct packages, and a package drawn more than once keeps its multiplicity, $n_y$; the observed package carries the same proposal correction as any other row. The proposal density is a computational device and never an economic object: it is not an offer, an availability or an opportunity. The proposal is fitted out of fold, so a household's own outcome never enters the proposal used to score it. For couples the proposal draws the joint participation regime first and then the two spouse packages conditional on it.

Standard errors are cluster-robust on the household. Optimization uses five starts under two polishing contracts, ten terminal paths in all; we report the spread of the criterion across those paths and the eigenvalues of the exact Hessian at the selected optimum. Those diagnostics support a stable local solution found from the starts tested. They are not a proof of global uniqueness, and we do not claim one.



# 4. Money-metric well-being and structural inequality decomposition

## The measure

Fix a household $i$ and a coalition state $S$, which determines the utility index $L_{i,S}$, the normalized opportunity density $\widehat g_{i,S}$ and the priced consumption $C_{i,S}$ at every package. Define the attained ex-ante value and the reference mass

$$
J_{i,S}=\int e^{L_{i,S}(j)}\left(\frac{C_{i,S}(j)}{\lambda_c}\right)^{\beta_c}\widehat g_{i,S}(j)\,d\nu(j),
\qquad
H_{i,S}=\int e^{L_{i,S}(j)}\,\widehat g_{i,S}(j)\,d\nu(j).
$$

The proposal also enters the finite-node welfare algebra. For singles, write $a_{ir}=\omega_r\exp[L_i(j_r)+\log\widehat g_i(j_r)-\log q_i^W(j_r)]$, where $\omega_r$ is the integration weight. Then $J_i\simeq\sum_r a_{ir}(C_{ir}/\lambda_c)^{\beta_c}$ and $H_i\simeq\sum_r a_{ir}$, with the same nodes and the one-euro floor in the attained consumption. For couples the common-proposal importance terms enter the corresponding joint-regime sums for both integrals. The proposal carries no economic content, but its importance correction is explicit in the welfare calculation as well as in estimation.

The reference offers the same flat monthly amount $m$ at every package while retaining that state's $L$ and $\widehat g$, so the value of the reference is

$$
\Phi_{i,S}(m)=\beta_c\log(m/\lambda_c)+\log H_{i,S},
\qquad \Phi_{i,S}'(m)=\beta_c/m>0 .
$$

The money metric is the amount at which the reference reaches the attained value, $\Phi_{i,S}(W_{i,S})=\log J_{i,S}$, which inverts in closed form:

$$
\boxed{\;W_{i,S}=\lambda_c\exp\!\left[\frac{\log J_{i,S}-\log H_{i,S}}{\beta_c}\right].\;}
$$

Writing $r_{i,S}(dj)=e^{L_{i,S}(j)}\widehat g_{i,S}(j)\,d\nu(j)/H_{i,S}$ for the reference probability measure, the same object is

$$
\boxed{\;W_{i,S}=\left[\int C_{i,S}(j)^{\beta_c}\,r_{i,S}(dj)\right]^{1/\beta_c}.\;}
$$

The measure is therefore a **weighted power mean of consumption of order $\beta_c$**, taken under a reference measure that weights packages by their non-consumption value and their availability. It is an arithmetic mean only at $\beta_c=1$. The normalizer $\lambda_c$ cancels between the two forms, which is why the constant is a units convention and not a modelling choice; we verify this numerically to a maximum relative deviation of 2.7e-15 across four widely separated values.


![The consumption coefficient as the order of a power mean. Left: the contribution an alternative makes to the consumption power moment, relative to the median alternative, against the linear comparison at $\beta_c=1$. Right: the marginal effect of that alternative’s consumption on the resulting equivalent amount, which carries exponent $\beta_c-1$, against the flat comparison at $\beta_c=1$. Neither curve is a reference probability weight: holding the reference measure fixed, those weights do not vary with consumption at all.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v5/figV07_power_mean.png){width=95%}


Three quantities are easy to conflate and are distinct. The reference probability weight $r_j$ does not vary with consumption at all when the reference measure is held fixed. The *contribution* an alternative makes to the power moment is proportional to $C_j^{\beta_c}$, so an alternative paying twice the median contributes 4.11 times as much at the estimated single-adult coefficient. The *marginal effect* of that alternative's consumption on the resulting amount is $\partial W/\partial C_j=r_jC_j^{\beta_c-1}W^{1-\beta_c}$, with exponent $\beta_c-1$. The figure plots the second and the third and labels each; neither is a statement that the alternative is more available.

$\beta_c$ is simultaneously the order of this power mean, the coefficient on log consumption, and the elasticity of an alternative's implied consumption-dependent weight $C_j^{\beta_c}$ in its own consumption. This elasticity concerns the power-moment contribution, holding $r_j$ fixed, rather than the normalized reference probability. It is not the consumption curvature, which is exactly zero here, and it is not an inequality-aversion parameter across households, which belongs to the index applied in Section 5 and not to the household's own aggregator.

## What the reference does and does not do to pay

Under the stated factorization the reference is invariant to the conditional wage density: that density integrates to one on its support and the non-consumption index has no wage argument, so replacing it leaves $H_{i}$ unchanged exactly, by construction of the formula above -- not as a numerical approximation. The accepted literal reference construction (Mapping F, Deputy ruling R1) makes the same point even more directly: its home reference is a fixed singleton state whose systematic utility carries no opportunity-density, proposal, behavioural-shock or intensity argument, so none of those four objects enters it at all.

Changes in earning opportunities nevertheless change the measure, because they change what the household attains, not the reference it is compared against. The correct statement is therefore narrow and we make only it: *the reference is directly pay-neutral, and earning opportunities reach the measure through the attained evaluation.* We do not report a magnitude for that attained-side channel here: quantifying it under a counterfactual equalization of earning opportunities is a decomposition question, and Section 5 reports only the bounded, preliminary exercise available for that. A qualitative channel existing does not establish that the deterministic independence-of-pay axiom fails for this stochastic functional. That would require fixing the primitives the axiom holds fixed and proving the property, which we have not done and do not claim.


### A worked household, in the current model

Take the weighted-median single-adult household of the sample: a man in his early fifties with medium education, no children, employed for eighteen hours a week at a delivered wage near fourteen euros an hour, receiving about 1,259 euros a month of simulated disposable income at that job. His money-metric level is 4,139 euros a month at the sample median, and the closed form is checkable by hand: since $W=\lambda_c\exp[(\log J-\log H)/\beta_c]$, the attained-minus-reference gap is $\log J-\log H=\beta_c\log(W/\lambda_c)$. Equalizing his preferences to the reference profile moves his level by about a quarter of a per cent; equalizing all his non-preference circumstances moves it by about eighteen per cent. That asymmetry, household by household, is what the decomposition adds up.

For a transparent two-alternative calculation with equal reference probabilities and consumption of 1,000 and 2,000 euros, the single-adult estimate gives $W=[(1000^{2.0387}+2000^{2.0387})/2]^{1/2.0387}\approx1,584$ euros. The numerator sums powered consumption and the outer exponent is essential. More generally, $r_{ir}=a_{ir}/\sum_s a_{is}$ gives $W=[\sum_r r_{ir}C_{ir}^{\beta_c}]^{1/\beta_c}$; dividing a plain consumption sum by a plain weight sum would be valid only at $\beta_c=1$.

The level is above his own disposable income, and for the median couple it is below theirs. Two things are happening. The reference measure weights packages by non-consumption value and availability, not by how often they are chosen; and the power mean of order $\beta_c>1$ rewards dispersion in reachable consumption. Levels are therefore not an income concept, and they are not comparable between the two household types, each of which carries its own reference construction. We report the levels, use them only within type, and do not offer a mechanism for the between-type difference.


## Interpersonal comparison and the unit

The measure is defined at the household. Comparing households of different size requires an equivalence scale, which is a normative choice and not an estimate. We report every result on two bases: a raw household basis, and an equivalized basis using the modified OECD scale. We never pool the two household types into one distribution, because the two applications carry different reference constructions and the levels are not comparable; every share below is a share of the baseline inequality of its own population.

## The preliminary structural decomposition

A complete attribution of measured inequality to preferences and to circumstances requires a counterfactual-attainment estimand: under a counterfactual environment, which bundle does the household attain? Two candidate estimands are under design -- a realised-bundle route conditioning the behavioural latent state on the observed choice, and an ex-ante route integrating the measure over the model-implied counterfactual choice distribution -- and neither is executed here, because the inequality of expected welfare is not the expected inequality of welfare and the two routes answer different questions. Ahead of that design choice, this section reports a bounded, explicitly preliminary exercise that reuses the model's own already-priced estimation panel, with no re-estimation and no new pricing, and simulates each household's attained bundle under a counterfactual environment by carrying the household's realised draws through it directly.

Let $X_i=(P_i,A_i,B_i)$ collect three structural inputs for household $i$:

- $P_i$ systematic utility heterogeneity: the leisure-weight covariates and the sex- or spouse-specific preference block, including the reduced-form time-constraint shifters this pathway also carries;
- $A_i$ local labour-market access (region, urban/rural, year): the employment index covariates and the occupation access table;
- $B_i$ earning opportunities: the covariates entering the offered-wage location.

Household resources, needs and composition are held fixed throughout this exercise rather than treated as a fourth operator: they are not equalized in any coalition and no share is attributed to them. Let $\mathcal I$ be the Gini index and $W_i(\cdot)$ the money metric of the previous subsection, so the baseline is $I_\varnothing=\mathcal I\{W_i(X_i)\}_{i=1}^N$. For each factor define a **structural equalization operator** $T_P,T_A,T_B$, which replaces that factor's arguments across all households by a common reference profile and leaves the estimated coefficients in place. For a coalition $S\subseteq\{P,A,B\}$ let $X^S=T_S(X)$ be the state in which exactly the factors in $S$ are equalized, and set

$$
I_S=\mathcal I\{W_i(T_S X)\}_{i=1}^{N},
\qquad
v(S)=I_\varnothing-I_S .
$$

$v$ is a cooperative game on three players: the worth of a coalition is the inequality it removes when its factors are equalized together. $T_S$ is a single simultaneous substitution map, not an ordered product $\prod_{k\in S}T_k$, and an operator changes a *pathway*, not every occurrence of a raw characteristic.


Table: The three structural equalization operators of the preliminary decomposition (Section 5). Each operator replaces the arguments of one structural pathway with a common reference profile and leaves the estimated coefficients in place; it does not equalize every occurrence of a raw characteristic. Operators are applied as one simultaneous substitution map, not as an ordered product. Household resources, needs and composition are held fixed throughout this exercise -- not a fourth operator here -- pending the counterfactual-attainment estimand the paper’s final decomposition architecture requires.

|Operator|What is replaced|What is retained|
|---|---|---|
|$T_P$ preferences (systematic utility heterogeneity)|Singles: the arguments of the leisure weight and the complete reference-sex leisure block. Couples: the medoid spouse arguments, with own spouse coefficients retained|Access and wage pathways of the same characteristics|
|$T_A$ local labour-market access|The arguments of the employment index and the occupation access table|Preferences, wage location; sex-specific occupation coefficients|
|$T_B$ earning opportunities|The arguments of the offered-wage location: education shares and experience moments, with squares recomputed rather than averaged|The estimated wage coefficients and dispersion; the preference and access pathways of the same characteristics|



Welfare and inequality are then recomputed from the model for all eight coalitions of $\{P,A,B\}$. There is no linearisation and no re-estimation: coefficients are held at their estimates throughout, and only the arguments move.

The interactions are allocated with the **exact Shapley value** [@shorrocks2013] on the three-player game $v$: the average of each factor's marginal contribution over all orderings in which the three factors can be equalized. With three players this average has a closed form over $3!=6$ orderings and requires no grouping. The allocation is exhaustive: the contributions sum to $\Delta I=I_\varnothing-I_{\{P,A,B\}}$, and we report $\Delta I$ itself rather than treat it as identically zero, because household resources, needs and composition remain in the residual $I_{\{P,A,B\}}$ along with sex-block parameter differences and behavioural randomness.

Uncertainty is reported two ways, never merged into a confidence interval: a Monte Carlo range across 1,000 simulation replications at fixed estimates, and an independent check under a second simulation seed. Neither is a parameter-uncertainty interval; propagating the estimation covariance into this exercise is future work.


> **What is new and what is inherited, in this preliminary exercise.**
>
> *Inherited.* The latent-jobs model of labour supply and its identifying restrictions; the joint estimation of preferences and offer intensities; the use of a microsimulation model to price alternatives; the money-metric idea and the discipline of stating the reference; the Shapley value as the allocation rule for a cooperative game with additively separable worth.
>
> *Application-specific contribution.* The bounded three-factor game itself: preferences, local labour-market access and earning opportunities as pathways inside an estimated job-choice model, holding resources, needs and composition fixed by design pending a counterfactual-attainment estimand.
>
> *Not claimed.* A new Shapley rule; that this is the paper's final decomposition; that the small movable share, $\Delta I$, means opportunities are unimportant, rather than that most of what determines the money metric's dispersion is held fixed in this exercise by construction.


# 5. Empirical results

## Behavioural estimates

The estimated model has 41 free coordinates for single adults, of which 40 are interior, and 47 for couples, all interior. The criterion is 6253.463 and 10283.034 respectively. Across ten terminal paths from five starts under two polishing contracts, the criterion varies by 1.1e-10 for single adults and 1.3e-09 for couples, and the smallest eigenvalue of the exact Hessian on the interior block is 0.1669 and 0.0771. One single-adult coordinate, the female age-square term in the leisure weight, sits at a box endpoint; its interval is reported under the active-set convention in the appendix and it is excluded from the interior curvature.


Table: The preference block. Cluster-robust standard errors in parentheses, clustered on the household. "At bound" marks an estimate at a box endpoint, whose interval is reported under the active-set convention in the appendix. The consumption weight is common within a population and enters as $\beta_c\log(C/\lambda_c)$.

|Coefficient|Single men|Single women|Couple men|Couple women|
|---|---|---|---|---|
|Leisure weight, intercept $\beta_{\ell 0}$|8.5199 (3.5480)|5.8683 (2.1346)|3.9814 (0.7466)|13.1029 (4.7760)|
|Leisure weight, age $\beta_{\ell a}$|1.4820 (1.0236)|0.0678 (0.4792)|-0.0080 (0.0287)|-0.1228 (0.1260)|
|Leisure weight, age squared $\beta_{\ell a^2}$|0.7783 (0.7732)|1.0000 (at bound)|0.0065 (0.0030)|0.0073 (0.0103)|
|Leisure weight, children $\beta_{\ell n}$|&mdash;|0.1666 (0.4422)|&mdash;|-0.3055 (1.1472)|
|Leisure curvature $\theta_\ell$|-1.6263 (0.3301)|-0.9274 (0.2161)|-0.9761 (0.1357)|-1.6863 (0.2458)|
|Consumption weight $\beta_c$|2.0387 (0.2917)|2.0387 (0.2917)|2.1017 (0.2939)|2.1017 (0.2939)|



The consumption weight is 2.0387 with a cluster-robust standard error of 0.2917 for single adults and 2.1017 with 0.2939 for couples. Two things follow. Because the estimate exceeds one, the money metric of Section 4 is a power mean of order above one rather than an arithmetic mean. And because utility is on the unit-scale shock, one natural unit of the index corresponds to multiplying consumption by $\exp(1/\beta_c)$, a factor of 1.633 for single adults and 1.609 for couples. That is a proportional statement: there is no single euro value of a unit of utility independent of the consumption at which it is evaluated.


Table: The opportunity block: employment access, the hours density and occupation access. Cluster-robust standard errors in parentheses. The employment index multiplies the working indicator; the omitted references are region 1, thinly populated areas, the residual hours set of total width 26.5 hours per week, and occupation group 1. The singles occupation column reports the female coordinates; the male coordinates are in the appendix table. Hours coefficients are common across the two singles sex groups and spouse-specific for couples.

|Coefficient|Singles|Couple men|Couple women|
|---|---|---|---|
|Employment constant $\beta_E$|-3.1735 (0.4053)|-2.1233 (0.3195)|-2.8148 (0.3021)|
|Group unemployment rate $\beta_{E,gsur}$|-1.4422 (0.2356)|-1.1924 (0.1557)|shared with the man|
|Densely populated $\beta_{E,u}$|-0.0288 (0.2209)|-0.1823 (0.1657)|shared with the man|
|Intermediate density $\beta_{E,m}$|0.0641 (0.2614)|-0.4174 (0.1861)|shared with the man|
|Region 2 $\beta_{E,2}$|-0.3780 (0.3292)|-0.1546 (0.2442)|shared with the man|
|Region 3 $\beta_{E,3}$|-0.1117 (0.3891)|0.0873 (0.2808)|shared with the man|
|Region 4 $\beta_{E,4}$|-0.8218 (0.3810)|0.0150 (0.3068)|shared with the man|
|Region 5 $\beta_{E,5}$|-0.5162 (0.3274)|-0.1455 (0.2555)|shared with the man|
|Region 6 $\beta_{E,6}$|-0.7222 (0.3528)|-0.2844 (0.2748)|shared with the man|
|Region 7 $\beta_{E,7}$|-0.5374 (0.3503)|-0.1396 (0.2651)|shared with the man|
|Region 8 $\beta_{E,8}$|-0.4512 (0.3401)|-0.1659 (0.2660)|shared with the man|
|Hours band: Part-time lower, [17.5, 21.5)|0.0298 (0.1972)|-1.1094 (0.3791)|-0.5173 (0.1629)|
|Hours band: Part-time upper, [28.5, 30.5)|0.7080 (0.1928)|0.0835 (0.2378)|1.1586 (0.1214)|
|Hours band: Narrow full-time, [33.5, 36.5)|2.0656 (0.0894)|2.2888 (0.0821)|2.0284 (0.0682)|
|Hours band: Full-time upper, [36.5, 40.5]|1.9387 (0.0997)|2.3801 (0.0866)|1.6825 (0.0798)|
|Hours band: Long hours, [44.5, 70]|-0.0834 (0.1772)|0.6977 (0.1335)|-0.3109 (0.1615)|
|Occupation 2 $\xi_2$|0.1135 (0.1374)|-1.5097 (0.0967)|0.2074 (0.0891)|
|Occupation 3 $\xi_3$|-0.4060 (0.1440)|-2.2532 (0.1244)|-0.1804 (0.0923)|
|Occupation 4 $\xi_4$|0.5632 (0.1225)|0.1594 (0.0618)|0.8159 (0.0799)|




Table: The wage block and the consumption weight. The offered log wage is normal with mean $\mu_i(k)$ and dispersion $\sigma$, truncated to [2, 590] EUR/hour and renormalized on that support. Experience enters in units of twenty years. Slopes and $\sigma$ are common across the two singles sex groups and across spouses within couples; the singles and couples models are estimated separately, so the two columns are not restricted to agree.

|Coefficient|Singles|Couples|
|---|---|---|
|Intercept $\beta_{w0}$|2.0138 (0.0561)|2.0480 (0.0335)|
|Low education $\beta_{wL}$|0.0566 (0.0372)|-0.0433 (0.0217)|
|High education $\beta_{wH}$|0.1491 (0.0308)|0.1817 (0.0197)|
|Potential experience $\beta_{wx}$|0.2408 (0.0862)|0.5643 (0.0546)|
|Experience squared $\beta_{wx^2}$|-0.0282 (0.0390)|-0.1598 (0.0243)|
|Occupation 2 $\delta_2$|-0.0347 (0.0399)|-0.0740 (0.0231)|
|Occupation 3 $\delta_3$|0.0622 (0.0383)|0.0394 (0.0228)|
|Occupation 4 $\delta_4$|0.2785 (0.0368)|0.2146 (0.0223)|
|Log-wage dispersion $\sigma$|0.3815 (0.0133)|0.3631 (0.0072)|
|Consumption weight $\beta_c$|2.0387 (0.2917)|2.1017 (0.2939)|



**Maintained restrictions.** Singles: `theta_c_singles = 0`; the couples preference block (`beta_l0_m`, `beta_l_age_m`, `beta_l_age2_m`, `beta_l0_f`, `beta_l_age_f`, `beta_l_age2_f`, `beta_l_nkids_f`, `theta_l_f`) does not enter the singles likelihood; and `beta_E_y2015` and `beta_E_y2017` are absent because the 2015 and 2017 data are not used. Couples: `theta_c = 0`, the male children leisure effect is structurally zero, and the direct cross-leisure term is fixed at zero. These are restrictions, not estimates. The singles and couples models are estimated separately, so their wage blocks are not restricted to agree, and the difference between the two experience profiles should not be read as a test.


![Indifference curves in consumption and leisure, single-adult households, at one representative household of each sex. The budget set, the opportunity density and the taste shock are not drawn, so a curve is not a set of attainable bundles. The consumption axis is logarithmic; under log consumption every finite utility target is attainable at a finite positive consumption, which may lie outside the plotted range.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v5/figP01_indifference_curves_singles.png){width=95%}



![Indifference curves in consumption and each spouse’s leisure, couple households, with the partner’s leisure held at its observed value. Conditional slices of a joint object, not attainable sets.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v5/figP02_indifference_curves_couples.png){width=95%}



![Marginal rate of substitution between leisure and consumption, by age and sex, in euros per month per additional recurring weekly hour of leisure. A compensation along an indifference curve, not a behavioural response to a wage change.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v5/figP04_mrs_by_age_sex.png){width=95%}


The indifference curves and the marginal rate of substitution are the economics; the coefficients are coordinates. Note that the consumption axis is logarithmic and the curves are drawn over the plotted range only: under $L(\ell)+\beta_c\log(C/\lambda_c)$, any finite utility target at positive leisure is reached at the finite positive consumption $C=\lambda_c\exp\{(\bar u-L(\ell))/\beta_c\}$, which is strictly positive for every finite target. A curve leaving the frame has left the plotting range, not the domain of the model, and nothing here is economically infeasible.



![Marginal utility of consumption and of leisure in physical units, after the chain-rule conversion from the normalized coordinates. Levels are not comparable across separately estimated utility scales.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v5/figP03_marginal_utilities.png){width=95%}



![The euro value of one nat of utility under log consumption. The value is proportional rather than fixed: it rises with the consumption at which it is evaluated and has no single euro figure independent of a baseline.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v5/figP05_euro_value_of_one_nat.png){width=95%}


The euro value of one natural unit of the index is proportional rather than fixed: it rises with the consumption at which it is evaluated, so there is no single euro figure for a unit of utility independent of a baseline. This is a reading aid for the estimated scale, not an economic result.


## Fit

The fit reported here is a population prediction, computed by integrating the estimated model over the opportunity distribution and the taste shocks. It is not a sampled-menu choice probability and it is not an in-sample fitted value.


![Observed against model population shares, margin by margin, for both estimated specifications. Model shares are population predictions computed by direct integration over the estimated opportunity distribution, not sampled-menu choice probabilities.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v5/figV06_fit_by_margin.png){width=95%}



Table: Observed against model population shares, singles. The model column is a population prediction computed by direct integration over the estimated opportunity distribution and the taste shocks; it is not a sampled-menu choice probability and not an in-sample fitted value. The denominator column states the population each share is taken over.

|Unit|Moment|Observed|Model|Absolute deviation|Denominator|
|---|---|---|---|---|---|
|Man|Employment|0.8805|0.8675|0.0130|households|
|Man|Hours: non-employment|0.1195|0.1325|0.0130|households|
|Man|Hours: [5, 10)|0.0109|0.0000|0.0109|households|
|Man|Hours: [10, 17.5)|0.0075|0.0198|0.0123|households|
|Man|Hours: [17.5, 21.5)|0.0118|0.0215|0.0097|households|
|Man|Hours: [21.5, 28.5)|0.0278|0.0548|0.0269|households|
|Man|Hours: [28.5, 30.5)|0.0039|0.0285|0.0246|households|
|Man|Hours: [30.5, 33.5)|0.0107|0.0315|0.0208|households|
|Man|Hours: [33.5, 36.5)|0.2329|0.2457|0.0128|households|
|Man|Hours: [36.5, 40.5]|0.3400|0.2452|0.0948|households|
|Man|Hours: (40.5, 44.5)|0.0691|0.0488|0.0203|households|
|Man|Hours: [44.5, 70]|0.1658|0.1717|0.0059|households|
|Man|Occupation group 1|0.3823|0.3774|0.0049|workers|
|Man|Occupation group 2|0.1069|0.1014|0.0054|workers|
|Man|Occupation group 3|0.0516|0.0545|0.0029|workers|
|Man|Occupation group 4|0.4593|0.4667|0.0074|workers|
|Man|Mean log wage|2.6876|2.6309|0.0567|workers|
|Woman|Employment|0.8642|0.8665|0.0024|households|
|Woman|Hours: non-employment|0.1358|0.1335|0.0024|households|
|Woman|Hours: [5, 10)|0.0042|0.0000|0.0042|households|
|Woman|Hours: [10, 17.5)|0.0243|0.0254|0.0010|households|
|Woman|Hours: [17.5, 21.5)|0.0325|0.0346|0.0022|households|
|Woman|Hours: [21.5, 28.5)|0.0603|0.0737|0.0134|households|
|Woman|Hours: [28.5, 30.5)|0.0297|0.0355|0.0058|households|
|Woman|Hours: [30.5, 33.5)|0.0290|0.0367|0.0077|households|
|Woman|Hours: [33.5, 36.5)|0.2672|0.2581|0.0091|households|
|Woman|Hours: [36.5, 40.5]|0.2493|0.2386|0.0107|households|
|Woman|Hours: (40.5, 44.5)|0.0492|0.0446|0.0045|households|
|Woman|Hours: [44.5, 70]|0.1185|0.1192|0.0007|households|
|Woman|Occupation group 1|0.1795|0.1832|0.0036|workers|
|Woman|Occupation group 2|0.1976|0.1946|0.0031|workers|
|Woman|Occupation group 3|0.1349|0.1348|0.0002|workers|
|Woman|Occupation group 4|0.4879|0.4875|0.0004|workers|
|Woman|Mean log wage|2.5968|2.6207|0.0238|workers|




Table: Observed against model population shares, couples. The model column is a population prediction computed by direct integration over the estimated opportunity distribution and the taste shocks; it is not a sampled-menu choice probability and not an in-sample fitted value. The denominator column states the population each share is taken over.

|Unit|Moment|Observed|Model|Absolute deviation|Denominator|
|---|---|---|---|---|---|
|Household|Joint regime neither works|0.0222|0.0043|0.0178|households|
|Household|Joint regime man only|0.0794|0.0909|0.0115|households|
|Household|Joint regime woman only|0.0547|0.0723|0.0176|households|
|Household|Joint regime both work|0.8437|0.8324|0.0113|households|
|Man|Employment|0.9231|0.9234|0.0002|households|
|Man|Hours: non-employment|0.0769|0.0766|0.0002|households|
|Man|Hours: [17.5, 21.5)|0.0059|0.0046|0.0013|households|
|Man|Hours: [28.5, 30.5)|0.0095|0.0189|0.0094|households|
|Man|Hours: [33.5, 36.5)|0.2515|0.2507|0.0008|households|
|Man|Hours: [36.5, 40.5]|0.3274|0.2780|0.0494|households|
|Man|Hours: [44.5, 70]|0.2576|0.2531|0.0044|households|
|Man|Occupation group 1|0.3519|0.3516|0.0003|workers|
|Man|Occupation group 2|0.0797|0.0741|0.0056|workers|
|Man|Occupation group 3|0.0464|0.0412|0.0052|workers|
|Man|Occupation group 4|0.5220|0.5331|0.0111|workers|
|Man|Mean log wage|2.7687|2.7054|0.0633|workers|
|Woman|Employment|0.8984|0.9047|0.0063|households|
|Woman|Hours: non-employment|0.1016|0.0953|0.0063|households|
|Woman|Hours: [17.5, 21.5)|0.0283|0.0335|0.0052|households|
|Woman|Hours: [28.5, 30.5)|0.0462|0.0572|0.0110|households|
|Woman|Hours: [33.5, 36.5)|0.2687|0.2767|0.0080|households|
|Woman|Hours: [36.5, 40.5]|0.2793|0.2072|0.0721|households|
|Woman|Hours: [44.5, 70]|0.1079|0.1002|0.0077|households|
|Woman|Occupation group 1|0.1653|0.1648|0.0005|workers|
|Woman|Occupation group 2|0.1922|0.2017|0.0095|workers|
|Woman|Occupation group 3|0.1533|0.1583|0.0050|workers|
|Woman|Occupation group 4|0.4892|0.4752|0.0140|workers|
|Woman|Mean log wage|2.6072|2.6319|0.0247|workers|



The mean absolute deviation over all population moments is 0.0129 for single adults and 0.0136 for couples, but the informative content is margin by margin. Employment and the joint participation regimes are matched closely; the narrow full-time band around thirty-five hours is matched closely for both sexes; occupation shares given work are matched to within about one percentage point. The largest single discrepancy in both models is the upper full-time band $[36.5,40.5]$, which the model under-predicts by about nine percentage points for single men and seven for women in couples, with the mass appearing in the adjacent bands. The sub-ten-hour fit cell is also a genuine prediction error: the realized integration panel predicts zero against observed shares around one per cent. Both the structural hours density and the proposal assign positive mass to $(5,10)$: about 4.15 per cent of normalized structural hours mass and 0.00019 per cent conditional proposal mass. With an expected draw count of only 0.249, the realized panel contains no draw there. This is a tail-coverage limitation of the integration panel, distinct from the adjacent-band fit discrepancy. The long-hours bin closes at 70 inclusive, and the observed singles hours partitions close separately by sex.


Table: The estimated model against two re-estimated common-opportunity benchmarks, on the same 1,540 single-adult households, the same sampled alternatives and the same criterion. A better maximized criterion does not by itself establish that a mechanism has been identified; the margin-by-margin comparison in the fit table and figure is the substantive evidence.

|Specification|Free coordinates|Criterion|Difference|Population fit|
|---|---|---|---|---|
|Latent jobs with household-specific opportunities|41|6253.463|--|0.0129|
|Benchmark A: common opportunity distribution, preferences re-estimated|10|6403.974|+150.51|0.0270|
|Benchmark B: common opportunity shape, employment and hours moved into utility and re-estimated|16|6395.108|+141.64|0.0261|



The two re-estimated common-opportunity benchmarks are worse by 141.64 and by a larger margin, on the same households, the same sampled alternatives and the same criterion. The comparison is a nested one in the sense that the benchmarks restrict the opportunity block and re-estimate everything else, but we do not convert it into a formal test, because the sampled-alternative criterion is not the likelihood of the observed data and the conditions for a likelihood-ratio distribution are not established here. What the table does support is that the deterioration is concentrated where the opportunity block does its work: the population fit worsens from 0.0129 to 0.0270 and 0.0261, and the occupation margins deteriorate by an order of magnitude, from about half a percentage point to eleven. A better criterion does not by itself establish that a mechanism has been identified.

## Money-metric well-being


Table: The distribution of money-metric well-being, and the priced disposable income it replaces. Levels are in euros per month of equivalent flat consumption, weighted. Levels are not comparable between the two household types: each type carries its own reference construction, and the Gini of the money metric and the Gini of income are not two estimates of one quantity.

|Population|Basis|Mean|p10|Median|p90|Gini|
|---|---|---|---|---|---|---|
|Single-adult|Household|4,354|2,643|4,139|6,219|0.1936|
|Single-adult|Equivalized|3,957|2,286|3,722|5,819|0.2089|
|Single-adult|Priced disposable income|--|--|--|--|0.2533|
|Couple|Household|1,839|1,353|1,767|2,326|0.1325|
|Couple|Equivalized|972|721|928|1,229|0.1274|
|Couple|Priced disposable income|--|--|--|--|0.2310|




![The distribution of money-metric well-being, by household type and basis, with weighted medians marked. Levels are not comparable across the two panels: each household type carries its own reference construction.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v5/figV02_welfare_distributions.png){width=95%}



![Lorenz curves of money-metric well-being and of the priced disposable income it replaces, over the same households and the same weights. The two curves answer different questions about the same households; their Gini values are not two estimates of one quantity.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v5/figV01_welfare_lorenz.png){width=95%}


The money metric is less unequal than the priced disposable income it replaces, for both household types: the Gini falls from 0.253 to 0.194 for single adults and from 0.231 to 0.132 for couples. The two Ginis are not two estimates of one quantity. The income Gini describes an outcome; the welfare Gini describes an ex-ante monetary level built from each household's own preferences and own reachable jobs, and the difference between them is not a correction but a change of object.

Levels differ from income in opposite directions for the two types, and the levels are not comparable between them: each application carries its own reference construction, with a female-primary reference block for single adults and a medoid-spouse reference for couples, and the couples index adds two leisure terms. We use levels only within type and offer no mechanism for the between-type difference in levels.

## The preliminary decomposition


Table: Single adults, the eight P/A/B coalitions. Weighted Gini of money-metric well-being, dwt-weighted, simulated on the accepted model’s already-priced estimation panel with no re-estimation and no new pricing. "Change from actual" is the one-factor effect of that coalition. The Monte Carlo range is the spread of the Gini level across 1,000 simulation replications, never a confidence interval.

|Scale|Coalition|I(S), Gini|Change from actual|MC range (min–max)|
|---|---|---|---|---|
|unequivalised|Actual (no equalization)|0.2337|+0.0000|0.2203–0.2509|
|unequivalised|P|0.2326|-0.0011|0.2180–0.2491|
|unequivalised|A|0.2319|-0.0018|0.2178–0.2480|
|unequivalised|B|0.2298|-0.0039|0.2148–0.2452|
|unequivalised|P + A|0.2310|-0.0027|0.2177–0.2478|
|unequivalised|P + B|0.2282|-0.0054|0.2138–0.2437|
|unequivalised|A + B|0.2282|-0.0055|0.2135–0.2411|
|unequivalised|P + A + B|0.2268|-0.0069|0.2127–0.2431|
|equivalised|Actual (no equalization)|0.2451|+0.0000|0.2284–0.2663|
|equivalised|P|0.2456|+0.0005|0.2304–0.2647|
|equivalised|A|0.2436|-0.0014|0.2264–0.2631|
|equivalised|B|0.2419|-0.0032|0.2264–0.2592|
|equivalised|P + A|0.2443|-0.0008|0.2304–0.2624|
|equivalised|P + B|0.2418|-0.0033|0.2263–0.2594|
|equivalised|A + B|0.2405|-0.0046|0.2245–0.2582|
|equivalised|P + A + B|0.2406|-0.0045|0.2248–0.2580|




Table: Couples, the eight P/A/B coalitions. Weighted Gini of money-metric well-being, dwt-weighted, simulated on the accepted model’s already-priced estimation panel with no re-estimation and no new pricing. "Change from actual" is the one-factor effect of that coalition. The Monte Carlo range is the spread of the Gini level across 1,000 simulation replications, never a confidence interval.

|Scale|Coalition|I(S), Gini|Change from actual|MC range (min–max)|
|---|---|---|---|---|
|unequivalised|Actual (no equalization)|0.2035|+0.0000|0.1936–0.2144|
|unequivalised|P|0.1956|-0.0079|0.1858–0.2059|
|unequivalised|A|0.2025|-0.0010|0.1938–0.2140|
|unequivalised|B|0.1892|-0.0143|0.1803–0.2018|
|unequivalised|P + A|0.1946|-0.0089|0.1844–0.2046|
|unequivalised|P + B|0.1842|-0.0193|0.1742–0.1962|
|unequivalised|A + B|0.1883|-0.0152|0.1796–0.2000|
|unequivalised|P + A + B|0.1834|-0.0201|0.1731–0.1944|
|equivalised|Actual (no equalization)|0.1971|+0.0000|0.1871–0.2075|
|equivalised|P|0.1969|-0.0002|0.1873–0.2069|
|equivalised|A|0.1963|-0.0008|0.1869–0.2055|
|equivalised|B|0.1887|-0.0084|0.1789–0.1998|
|equivalised|P + A|0.1961|-0.0010|0.1861–0.2049|
|equivalised|P + B|0.1927|-0.0044|0.1829–0.2039|
|equivalised|A + B|0.1880|-0.0091|0.1775–0.1985|
|equivalised|P + A + B|0.1921|-0.0050|0.1821–0.2033|




![The eight P/A/B counterfactual coalitions, built from the accepted model by equalising household-constant covariates within a block. Node-level alternative characteristics are preserved in every coalition; only household-constant covariates are equalised. Preliminary, model-based.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v5/fig_preseminar_pab_architecture_v1.png){width=95%}


The eight rows per scale are the coalition values of the three-player game. $\Delta I=I(\varnothing)-I(\{P,A,B\})$ is small in every sample and scale -- -1.8 per cent of baseline inequality for single adults equivalised, up to -9.9 per cent for couples unequivalised -- and that is a property of what this exercise holds fixed, not a finding that job opportunities are unimportant: household resources, needs and composition are held fixed in every coalition, and that fixed component alone accounts for 127 to 100 per cent of the variance of log well-being (variance-decomposition detail in the discussion notebook, Section 8). Sex-block parameter differences and behavioural randomness also remain in the residual and are not attributed to $P$, $A$ or $B$.


Table: The exact three-player Shapley allocation of $\Delta I$ across P, A and B. Gini-point contribution beside the share of $\Delta I$ (not of baseline inequality), and an independent second-seed reproduction. No directional claim is made about P: its sign changes between unequivalised and equivalised reporting in both samples, so its share of $\Delta I$ is not stated. A Monte Carlo per-replication share range, which divides by that replication’s own near-zero $\Delta I$ and is not informative on its own, is reported in the technical gallery, not here.

|Population|Scale|Factor|Label|Gini-point contribution|Share of $\Delta I$|Second-seed Gini-point|
|---|---|---|---|---|---|---|
|Single-adult|unequivalised|P|Preferences (systematic utility heterogeneity)|+0.0012|—|+0.0011|
|Single-adult|unequivalised|A|Local labour-market access (region, urban/rural, year)|+0.0016|23.4%|+0.0017|
|Single-adult|unequivalised|B|Earning opportunities|+0.0040|58.6%|+0.0042|
|Single-adult|unequivalised|$\Delta I$|I(actual) $-$ I(P,A,B equalized)|+0.0069|100.0%|+0.0071|
|Single-adult|equivalised|P|Preferences (systematic utility heterogeneity)|-0.0003|—|-0.0004|
|Single-adult|equivalised|A|Local labour-market access (region, urban/rural, year)|+0.0013|29.6%|+0.0014|
|Single-adult|equivalised|B|Earning opportunities|+0.0034|77.4%|+0.0038|
|Single-adult|equivalised|$\Delta I$|I(actual) $-$ I(P,A,B equalized)|+0.0045|100.0%|+0.0049|
|Couple|unequivalised|P|Preferences (systematic utility heterogeneity)|+0.0064|—|+0.0065|
|Couple|unequivalised|A|Local labour-market access (region, urban/rural, year)|+0.0009|4.6%|+0.0009|
|Couple|unequivalised|B|Earning opportunities|+0.0128|63.5%|+0.0127|
|Couple|unequivalised|$\Delta I$|I(actual) $-$ I(P,A,B equalized)|+0.0201|100.0%|+0.0201|
|Couple|equivalised|P|Preferences (systematic utility heterogeneity)|-0.0019|—|-0.0019|
|Couple|equivalised|A|Local labour-market access (region, urban/rural, year)|+0.0007|14.6%|+0.0008|
|Couple|equivalised|B|Earning opportunities|+0.0062|124.0%|+0.0061|
|Couple|equivalised|$\Delta I$|I(actual) $-$ I(P,A,B equalized)|+0.0050|100.0%|+0.0050|




![Single-adult estimation sample: coalition Gini levels and the exact Shapley allocation of $\Delta I$ across P, A and B, with the sign instability of P annotated. Modified-OECD-equivalised $W^1_F$; Monte Carlo ranges over 1,000 replications, not confidence intervals. Preliminary, model-based.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v5/fig_preseminar_pab_decomposition_singles_v1.png){width=95%}



![Couple estimation sample: coalition Gini levels and the exact Shapley allocation of $\Delta I$ across P, A and B, with the sign instability of P annotated. Modified-OECD-equivalised $W^1_F$; Monte Carlo ranges over 1,000 replications, not confidence intervals. Preliminary, model-based.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v5/fig_preseminar_pab_decomposition_couples_v1.png){width=95%}


Within the movable share $\Delta I$, earning opportunities dominate local labour-market access for both household types, at every scale we report: from 58.6 per cent of $\Delta I$ for single adults unequivalised to 124.0 per cent for couples equivalised, against 4.6 to 29.6 per cent for local labour-market access. We make no directional claim about the preference contribution's sign: it changes between the unequivalised and equivalised reporting conventions in both samples, from 0.0012 to -0.0003 Gini points for single adults and 0.0064 to -0.0019 for couples.

The allocated shares are not one-factor effects. An allocated share is an average of marginal contributions over the orders in which coalitions can form; the coalition table above reports the one-factor effect directly, as the change from the actual coalition for the single-letter row. The two can differ, and with three players and an exact Shapley value the difference is fully accounted for by the interaction terms, which the closed form makes explicit.

**Robustness.** Every coalition Gini level and every Shapley contribution reproduces closely under an independent second simulation seed, including the sign instability of the preference contribution, which appears in both runs. Excluding the estimation panel's anchor node -- the household's own observed choice, inserted deterministically in every coalition, which mechanically anchors counterfactual attainment toward the observed outcome to a small, roughly common degree (2.9 per cent of single adults and 3.9 per cent of couples attain it under any coalition) -- moves $\Delta I$ by at most 9.3 per cent (couples, equivalised), with no sign flip in any specification.


A Monte Carlo share range for each factor -- the across-replication spread of one replication's own share, dividing by that replication's own near-zero $\Delta I$ -- is available in the discussion notebook's technical gallery alongside this table, with its own caveat that it is reported for completeness and is not informative on its own. It is not reproduced here: the Gini-point contribution and the second-seed check above are the informative comparison for a reader of this report.


The allocation is exhaustive to numerical precision: the residual after summing $P$, $A$, $B$ and $\Delta I$ back to $I_\varnothing$ is zero to machine precision in every sample and scale, verified rather than imposed. That is a computational validation of the accounting for the declared game. It does not validate the identification of the model, the normative content of the operators, or a resolution of the counterfactual-attainment question this exercise is deliberately bounded around.

# 6. Sensitivity and limitations

## Equivalization and the preliminary decomposition

Equivalization is a normative choice, and the preliminary decomposition of Section 5 moves with it. On the equivalized basis the movable share $\Delta I$ is larger relative to baseline inequality for both household types than on the raw household basis, and the earning-opportunities/local-access ordering is unchanged in every case: earning opportunities dominate at both scales, for both household types. The preference contribution's sign already differs between the two scales at the raw comparison reported in Section 5; equivalization is one of the two axes that sign instability spans, not an independent further concern. Both bases are reported throughout; neither is the correct one, and the choice between them is not settled by the data. We do not report a male-primary or other alternative reference-block variant of this preliminary exercise; that sensitivity, reported for the welfare baseline itself in Section 4, has not been re-run through the bounded decomposition.

## Two open econometric questions

The sample screens on the observed hours and wage of employed deciders. The estimation sample is therefore selected on an outcome of the process being modelled, and the conditional sampled-set likelihood, which is the right object given a sampled choice set, is not automatically the right object given an outcome-selected sample. We have not established which correction the screen requires, or that none is required. This is an econometric question and not a presentational one, and it is not resolved by the diagnostics reported above.

Separately, the sampled-set probability is derived by conditioning on a labelled collection of slots. Small observed cross-coordinate correlations and a multiplicity distribution consistent with independent draws are diagnostics; they do not by themselves establish the sampling law that the derivation assumes. Both questions are recorded here as open.

## The bridge to the compensation-side reference

The flat-consumption reference of Section 4 is one member of a family. A natural comparison is the reference that flattens consumption only at the non-work bundle, which sits on the compensation side of the same family. If non-work maximizes the non-consumption index and the opportunity density integrates to one on the domain the reference mass uses, then $H_i\le e^{L_i(o)}$, so the gap $\Delta_i=L_i(o)-\log H_i$ must be non-negative for every household and the ratio of the two measures is bounded on one side.

The first premise holds for every household in both samples. The second does not: the opportunity object entering the reference mass is an unnormalized index whose median mass on that domain is 0.077283 for single adults and 147.963 for couples. Omitting that mass makes the comparison depend on an arbitrary multiplicative scale, and it is the reason earlier signed gaps had the wrong sign for couples and happened not to reverse for single adults. Both earlier levels are withdrawn.


Table: The bridge between the two monetary references, after the premise audit. The second column reports whether non-work maximizes the non-consumption index for every household; the third reports the median mass of the opportunity kernel on the domain the reference integral uses. That mass is not one, which is the premise that failed and the reason the earlier signed gaps were scale artefacts. The remaining columns are the bridge after normalizing the kernel on exactly that domain.

|Population|Non-work maximizes $L$|Median $\int\hat g$|Median $W^4/W^1$|Range|Median $\Delta$ (nats)|$\Delta\ge 0$ everywhere|
|---|---|---|---|---|---|---|
|Single-adult|yes|0.077283|0.9843|[0.9169, 0.9990]|0.0322|yes|
|Couple|yes|147.962795|0.6242|[0.5211, 0.7171]|0.9906|yes|



After normalizing the kernel on exactly the domain the reference mass uses, the bridge is well behaved: the gap is non-negative for every household in both samples and the ratio is at most one everywhere, as the premises require. The median ratio is 0.9843 for single adults and 0.6242 for couples. We report the reconciled bridge as a property comparison between two references and do not use it as a competing headline distribution.

## The consumption normalizer


Table: The consumption normalizer. Three constants were in circulation. Under exact log consumption the normalizer enters utility as the alternative-invariant term $-\beta_c\log\lambda_c$, so it cancels from every choice probability and exactly from the money metric. The paper reports the estimation-frame constant throughout.

|Panel|Single-adult (EUR/month)|Couple (EUR/month)|Role|
|---|---|---|---|
|Estimation frame, 101 sampled alternatives per household|1,938.238719|4,247.875047|Constant of record|
|Welfare panel, 2,048 common integration nodes|1,774.518218|3,821.448012|Recomputed over its own rows; inert|
|Predecessor frames, before the sample correction|1,911.108058|3,821.448012|Superseded|



Three normalizing constants were in circulation between the estimation frames and the welfare panel, because each panel computes the constant as a mean over its own rows. Under exact log consumption the constant is alternative-invariant, so it cancels from every choice probability and exactly from the money metric; the deviation over four widely separated values is 2.7e-15. No reported quantity changes. The paper reports the estimation-frame constant throughout, and the discrepancy is recorded here rather than silently harmonised.

## What is not established

The preliminary decomposition is an accounting of a structural model under declared operators. It is not a causal analysis. No regional, educational or occupational effect reported here is identified as a causal effect, and the exhaustiveness of the allocation validates the accounting for the declared game, not the identification of the model or the normative content of the operators.

Section 5's decomposition is bounded and preliminary in three specific ways, stated together here. It holds household resources, needs and composition fixed rather than decomposing them, so no share is attributed to that circumstance and the movable inequality it reaches is correspondingly small. It reuses the model's already-priced estimation panel to simulate counterfactual attainment, which anchors that attainment toward the observed outcome to a small, checked degree, rather than resolving the counterfactual-attainment estimand the paper's final decomposition architecture requires. And its uncertainty is reported as a Monte Carlo simulation range and an independent second-seed check, not as a parameter-uncertainty interval propagated from the estimation covariance. None of the three is a defect in what is reported; together they are why it is reported as preliminary rather than as the paper's decomposition result.

# 7. Conclusion

Observed hours and earnings do not say whether a household chose its position or settled for it, and that ambiguity is not a nuisance for welfare measurement: it is the substance of it. This paper takes the ambiguity seriously in both halves of the problem. On the behavioural side it estimates a model in which the jobs a household can reach and the way it ranks them are identified jointly, with every alternative priced through the tax-benefit system. On the normative side it evaluates well-being with a reference that keeps each household's own preferences and own reachable jobs and removes variation in pay from the reference bundles.

A complete decomposition of the resulting inequality into preferences and circumstances awaits a counterfactual-attainment estimand still under design. Ahead of it, a bounded preliminary exercise asks how a small, structurally-fixed share of measured inequality divides between preferences, local labour-market access and earning opportunities, holding resources, needs and composition fixed. For both French single-adult and couple households, earning opportunities dominate local labour-market access within that movable share, at every scale reported; the preference contribution's sign is not robust between reporting conventions, so no directional claim is made about it.

Three limits should travel with that reading. It is preliminary and bounded by construction, not the paper's final decomposition. The allocation is exhaustive for the declared three-player game, which validates the accounting and not the identification or the ethics of the operators. And two questions about the observation rule remain genuinely open, unrelated to the decomposition itself. What the exercise offers is not a causal account of why opportunities differ, and not yet a complete attribution of measured inequality, but a disciplined, preliminary statement of which of two circumstance channels dominates, once preferences and a structural model are made explicit and the reference is stated.

# 8. Appendix A. The estimated parameter vectors

The tables below report only coordinates estimated on the reported sample. **Maintained restrictions.** Singles: `theta_c_singles = 0`; the couples preference block (`beta_l0_m`, `beta_l_age_m`, `beta_l_age2_m`, `beta_l0_f`, `beta_l_age_f`, `beta_l_age2_f`, `beta_l_nkids_f`, `theta_l_f`) does not enter the singles likelihood; and `beta_E_y2015` and `beta_E_y2017` are absent because the 2015 and 2017 data are not used. Couples: `theta_c = 0`, the male children leisure effect is structurally zero, and the direct cross-leisure term is fixed at zero. These are restrictions, not estimates.

One single-adult coordinate, the female age-square term, is at its box endpoint. Under the active-set convention its interval is not reported, the interior curvature is computed after removing it, and the parameter draws used for the welfare intervals hold it at its estimate.


Table: The singles estimated coordinates. Standard errors are cluster-robust on the household; boundary-active estimates are marked at bound. Maintained restrictions are stated once in the accompanying note.

|Coordinate|Estimate|CR1 s.e.|z|Box|Status|
|---|---|---|---|---|---|
|\path{beta_l0_sm}|8.51993|3.54798|2.401|[0.05, 50]|estimated|
|\path{beta_l_age_sm}|1.48195|1.02361|1.448|[-5, 5]|estimated|
|\path{beta_l_age2_sm}|0.778284|0.773158|1.007|[-1, 1]|estimated|
|\path{theta_l_sm}|-1.62627|0.330058|-4.927|[-8, 0.95]|estimated|
|\path{beta_l0_sf}|5.86829|2.13459|2.749|[0.05, 50]|estimated|
|\path{beta_l_age_sf}|0.0677662|0.479217|0.141|[-5, 5]|estimated|
|\path{beta_l_age2_sf}|1|--|--|[-1, 1]|at bound|
|\path{beta_l_nkids_sf}|0.166636|0.442236|0.377|[-5, 5]|estimated|
|\path{theta_l_sf}|-0.927353|0.216128|-4.291|[-8, 0.95]|estimated|
|\path{beta_E}|-3.17353|0.405337|-7.829|[-25, 25]|estimated|
|\path{beta_h_pt1}|0.0297672|0.197247|0.151|[-10, 10]|estimated|
|\path{beta_h_pt2}|0.707971|0.192788|3.672|[-10, 10]|estimated|
|\path{beta_h_ft}|1.93873|0.0996968|19.446|[-10, 10]|estimated|
|\path{beta_h_lh}|-0.0833752|0.177201|-0.471|[-10, 10]|estimated|
|\path{beta_E_gsur}|-1.44224|0.235591|-6.122|[-10, 10]|estimated|
|\path{beta_E_drgn2}|-0.377963|0.32925|-1.148|[-10, 10]|estimated|
|\path{beta_E_drgn3}|-0.111713|0.38912|-0.287|[-10, 10]|estimated|
|\path{beta_E_drgn4}|-0.821813|0.380963|-2.157|[-10, 10]|estimated|
|\path{beta_E_drgn5}|-0.516158|0.327362|-1.577|[-10, 10]|estimated|
|\path{beta_E_drgn6}|-0.722159|0.35278|-2.047|[-10, 10]|estimated|
|\path{beta_E_drgn7}|-0.537369|0.350308|-1.534|[-10, 10]|estimated|
|\path{beta_E_drgn8}|-0.45119|0.340074|-1.327|[-10, 10]|estimated|
|\path{beta_E_drgur}|-0.0287689|0.220916|-0.130|[-10, 10]|estimated|
|\path{beta_E_drgmd}|0.064133|0.261352|0.245|[-10, 10]|estimated|
|\path{beta_occ_2_m}|-1.37371|0.158147|-8.686|[-15, 15]|estimated|
|\path{beta_occ_3_m}|-2.10963|0.202248|-10.431|[-15, 15]|estimated|
|\path{beta_occ_4_m}|-0.325897|0.121341|-2.686|[-15, 15]|estimated|
|\path{beta_occ_2_f}|0.113492|0.137399|0.826|[-15, 15]|estimated|
|\path{beta_occ_3_f}|-0.406009|0.144045|-2.819|[-15, 15]|estimated|
|\path{beta_occ_4_f}|0.563216|0.122467|4.599|[-15, 15]|estimated|
|\path{beta_w0}|2.01382|0.0560922|35.902|[-10, 20]|estimated|
|\path{beta_w_educL}|0.0566261|0.0372485|1.520|[-5, 5]|estimated|
|\path{beta_w_educH}|0.149054|0.0308408|4.833|[-5, 5]|estimated|
|\path{beta_w_pexp}|0.24077|0.0862223|2.792|[-1, 1]|estimated|
|\path{beta_w_pexp2}|-0.0281739|0.0389905|-0.723|[-0.1, 0.1]|estimated|
|\path{sigma}|0.381505|0.0132752|28.738|[0.1, 20]|estimated|
|\path{delta_occ_2}|-0.0347155|0.039899|-0.870|[-4, 4]|estimated|
|\path{delta_occ_3}|0.0622139|0.0382749|1.625|[-4, 4]|estimated|
|\path{delta_occ_4}|0.278494|0.0367705|7.574|[-4, 4]|estimated|
|\path{beta_h_f35}|2.06556|0.0894479|23.092|[-10, 10]|estimated|
|\path{beta_c}|2.03873|0.291729|6.988|[0.05, 50]|estimated|




Table: The couples estimated coordinates. Standard errors are cluster-robust on the household; boundary-active estimates are marked at bound. Maintained restrictions are stated once in the accompanying note.

|Coordinate|Estimate|CR1 s.e.|z|Box|Status|
|---|---|---|---|---|---|
|\path{beta_l0_m}|3.98136|0.746569|5.333|[1e-06, 50]|estimated|
|\path{beta_l_age_m}|-0.00799228|0.0287174|-0.278|[-5, 5]|estimated|
|\path{beta_l_age2_m}|0.00648336|0.00297388|2.180|[-1, 1]|estimated|
|\path{theta_l_m}|-0.976109|0.135663|-7.195|[-8, 0.95]|estimated|
|\path{beta_l0_f}|13.1029|4.77604|2.743|[0.05, 50]|estimated|
|\path{beta_l_age_f}|-0.122813|0.126048|-0.974|[-5, 5]|estimated|
|\path{beta_l_age2_f}|0.00730709|0.0102503|0.713|[-1, 1]|estimated|
|\path{beta_l_nkids_f}|-0.305471|1.14719|-0.266|[-5, 5]|estimated|
|\path{theta_l_f}|-1.68631|0.245846|-6.859|[-8, 0.95]|estimated|
|\path{beta_E_m}|-2.12326|0.319457|-6.646|[-25, 25]|estimated|
|\path{beta_E_f}|-2.81476|0.302078|-9.318|[-25, 25]|estimated|
|\path{beta_h_pt1_m}|-1.10936|0.379086|-2.926|[-10, 10]|estimated|
|\path{beta_h_pt1_f}|-0.517276|0.162932|-3.175|[-10, 10]|estimated|
|\path{beta_h_pt2_m}|0.0835202|0.237788|0.351|[-10, 10]|estimated|
|\path{beta_h_pt2_f}|1.15858|0.121438|9.541|[-10, 10]|estimated|
|\path{beta_h_f35_m}|2.2888|0.0821348|27.866|[-10, 10]|estimated|
|\path{beta_h_f35_f}|2.02835|0.0682392|29.724|[-10, 10]|estimated|
|\path{beta_h_ft_m}|2.38012|0.0865569|27.498|[-10, 10]|estimated|
|\path{beta_h_ft_f}|1.68251|0.0798241|21.078|[-10, 10]|estimated|
|\path{beta_h_lh_m}|0.69767|0.133487|5.226|[-10, 10]|estimated|
|\path{beta_h_lh_f}|-0.310873|0.161533|-1.925|[-10, 10]|estimated|
|\path{beta_E_gsur}|-1.19243|0.155667|-7.660|[-10, 10]|estimated|
|\path{beta_E_drgn2}|-0.154617|0.24423|-0.633|[-10, 10]|estimated|
|\path{beta_E_drgn3}|0.0872501|0.280833|0.311|[-10, 10]|estimated|
|\path{beta_E_drgn4}|0.0150136|0.306753|0.049|[-10, 10]|estimated|
|\path{beta_E_drgn5}|-0.145472|0.255453|-0.569|[-10, 10]|estimated|
|\path{beta_E_drgn6}|-0.284391|0.274814|-1.035|[-10, 10]|estimated|
|\path{beta_E_drgn7}|-0.139569|0.265133|-0.526|[-10, 10]|estimated|
|\path{beta_E_drgn8}|-0.165927|0.26603|-0.624|[-10, 10]|estimated|
|\path{beta_E_drgur}|-0.182322|0.165665|-1.101|[-10, 10]|estimated|
|\path{beta_E_drgmd}|-0.417356|0.1861|-2.243|[-10, 10]|estimated|
|\path{beta_occ_2_m}|-1.50975|0.0967347|-15.607|[-15, 15]|estimated|
|\path{beta_occ_3_m}|-2.25319|0.124405|-18.112|[-15, 15]|estimated|
|\path{beta_occ_4_m}|0.159368|0.061796|2.579|[-15, 15]|estimated|
|\path{beta_occ_2_f}|0.207379|0.0891054|2.327|[-15, 15]|estimated|
|\path{beta_occ_3_f}|-0.180381|0.0923137|-1.954|[-15, 15]|estimated|
|\path{beta_occ_4_f}|0.81589|0.079925|10.208|[-15, 15]|estimated|
|\path{beta_w0}|2.048|0.0335421|61.058|[-10, 20]|estimated|
|\path{beta_w_educL}|-0.0433046|0.0216643|-1.999|[-5, 5]|estimated|
|\path{beta_w_educH}|0.181652|0.0197059|9.218|[-5, 5]|estimated|
|\path{beta_w_pexp}|0.56435|0.0545928|10.337|[-3, 3]|estimated|
|\path{beta_w_pexp2}|-0.15983|0.0242888|-6.580|[-0.3, 0.3]|estimated|
|\path{sigma}|0.363075|0.0072235|50.263|[0.1, 20]|estimated|
|\path{delta_occ_2}|-0.0740322|0.0231318|-3.200|[-4, 4]|estimated|
|\path{delta_occ_3}|0.0393566|0.0228|1.726|[-4, 4]|estimated|
|\path{delta_occ_4}|0.214559|0.0223344|9.607|[-4, 4]|estimated|
|\path{beta_c}|2.10172|0.293879|7.152|[0.05, 50]|estimated|



# 9. Appendix B. Inequality indices and the allocation rule

The preliminary decomposition of Section 5 uses the Gini index only, on a weighted distribution of strictly positive money-metric levels with mean $\mu$: $\mathcal I=\frac{1}{2\mu}\,\mathbb{E}\lvert W-\tilde W\rvert$, for $W,\tilde W$ independent draws from the distribution. Extending the exercise to further indices, as an earlier, retired version of this decomposition did across six indices, is future work and is not reported here.

The exact Shapley value on the three-player game $v(S)=I_\varnothing-I_S$, $S\subseteq\{P,A,B\}$, allocates to factor $k$ the average of its marginal contribution $v(S\cup\{k\})-v(S)$ over all $3!=6$ orderings in which the three factors can be introduced:

$$
C_k=\frac{1}{6}\sum_{\pi}\big[v(S_\pi(k)\cup\{k\})-v(S_\pi(k))\big],
$$

where $S_\pi(k)$ is the set of factors preceding $k$ in ordering $\pi$. With three players this has a closed form and requires no grouping into unions, unlike the Owen extension for the additional operator an earlier, retired version of this decomposition used. Contributions are signed and are never renormalised to sum to one hundred by construction: they sum to $\Delta I=I_\varnothing-I_{\{P,A,B\}}$ because the game closes, and the closure is verified.

# 10. Appendix C. The bridge between the two monetary references

Write $M_i=\int\widehat g_i\,d\nu$ for the mass of the opportunity object on the domain the reference integral uses, and $o$ for the non-work bundle. The two references satisfy

$$
\beta_c\log(W^{1}_i/\lambda_c)=\log J_i-\log H_i,
\qquad
\beta_c\log(W^{4}_i/\lambda_c)=\log J_i-\log M_i-L_i(o),
$$

so that $\log(W^{4}_i/W^{1}_i)=\big(\log H_i-\log M_i-L_i(o)\big)/\beta_c$ and $\Delta_i=L_i(o)+\log M_i-\log H_i$. Omitting $\log M_i$ is valid only when $M_i=1$, and it is not: the audit reports median mass 0.077283 for single adults and 147.963 for couples. The premise that failed is therefore the unit mass of the kernel on that domain, not the maximality of the non-work bundle, which holds for every household in both samples, and not the orientation of the comparison.

After renormalizing the kernel on exactly that domain, the median gap is 0.0322 nats for single adults and 0.9906 for couples, the gap is non-negative for every household, and the ratio lies in $[0.9169, 0.9990]$ for single adults and $[0.5211, 0.7171]$ for couples. The identity above is satisfied to machine precision at the corrected normalization.

A separate point concerns the low-temperature limit. Attained and reference values must be indexed by the same shock scale for the limit to be meaningful. The statement that survives is that the two consistently indexed measures converge as the scale goes to zero; convergence to the value of staying at home evaluated at a different fixed scale is not the same statement and is not made.

# 11. Appendix D. Data, software and replication

**Data.** French EU-SILC, accessed through Eurostat's harmonised release, with 2016 survey collection and a 2015 income reference year. The harmonised survey is transformed into an input file for EUROMOD [@sutherlandfigari2013], which applies the French 2015 policy system. Regional labour-market conditions come from the Eurostat regional labour-force series. Access to EU-SILC microdata is granted by Eurostat under its research-access conditions and the data cannot be redistributed with this document.

**Sample.** 1,540 single-adult and 2,223 couple households, constructed by the screens of Section 2.

**Estimator and inference.** Conditional likelihood over 100 sampled alternatives per household plus the observed choice, with an out-of-fold proposal correction; cluster-robust standard errors on the household. Optimization is checked by five starts under two polishing contracts and curvature by exact Hessian eigenvalues.

**Welfare computation.** A common integration panel of 2,048 nodes per household, evaluated under all sixteen coalition states. Integration error is measured by 8 randomized quasi-Monte Carlo scrambles; parameter uncertainty by 100 draws from the cluster-robust covariance rebuilt from the Hessian and the household scores, holding maintained restrictions and bound-active coordinates at their values. The two are reported separately and are never combined into one band.

**Software.** Python with JAX (0.10.1) for automatic differentiation, and the EUROMOD connector (0.2.17).

**Replication.** Code and derived, non-confidential intermediate artefacts will be made available in a public repository on publication. Confidential microdata remain in their permitted environment, so the replication package reproduces every step conditional on authorised access to EU-SILC.

# 12. The research notebook

The project keeps one canonical research notebook, `JMP_research_lab.ipynb`, in the estimation repository. Two things about it need saying precisely, because both have been overstated before.

**It is a replay and refit interface, not a source-to-results interface.** What it exposes, by calling the production functions rather than reimplementing them: loading a frozen engine-ready frame; evaluating the criterion and its gradient at a given parameter vector; refitting from a chosen start; rebuilding the cluster-robust covariance from the Hessian and the household scores; computing population predictions by direct integration; evaluating the money metric and the coalition states on a saved integration panel; and regenerating the figures from their saved plotted-number files. What it does *not* do: reconstruct the raw survey input from source, generate a new set of alternatives, or price alternatives through the tax-benefit model. Those three stages run as separate authorised jobs against the microdata environment and are not callable from the notebook. So the notebook reproduces every stage from the frozen priced frame onwards, and describing it as end-to-end would be inaccurate.

**Its machinery is current; the artifacts it is pointed at are not.** The utility construction in the notebook is specification-driven: it reads the consumption coefficient from the specification and carries an estimated one wherever the specification leaves it free, so nothing in the code assumes the superseded numeraire. But the frames, specification and result files it currently loads are the generation that preceded the specifications of record reported here. Re-pointing it is a mechanical change and re-running it is not, and a notebook that had been re-pointed but not re-run would be worse than one that is honestly labelled. It is therefore left as it stands, and re-binding it to the current specifications and welfare record is the one capability gap this document reports.

# 13. Scientific history of this result

This section records how the reported specifications and results came to be what they are. It is here so that the argument above does not have to carry it, and so that a reader comparing this version with an earlier one can see what changed and why. Nothing in it is a competing model.

**The consumption specification.** Earlier drafts reported a specification in which the consumption coefficient was fixed at one as a numeraire, and one in which the single-adult consumption curvature was estimated at $\theta_c\approx0.168$. Neither is the reported model. The current specification fixes the shock scale, fixes the consumption curvature at exactly zero, and estimates the consumption weight instead. That change improves the criterion by 23.753 log-points for single adults and 15.659 for couples, and it changes the welfare aggregator from an arithmetic mean of reachable consumption to a power mean of order $\beta_c$. Every welfare quantity computed under the earlier convention is superseded, and the corresponding figures were regenerated rather than relabelled.

**The sample.** The predecessor frames contained 1,555 single-adult and 2,275 couple households. Twelve single-adult and fifty-two couple households were removed when the hours support and the occupation mapping were applied to the observed rows, and three further single-adult households were removed because their own observed job prices to non-positive disposable consumption. The current descriptive tables are computed on the resulting 1,540 and 2,223 households, not on the predecessor frames, and the funnel in Section 2 ends where the estimation begins.

**The disposable-income convention.** Single-adult disposable income was previously aggregated over the decider only; it is now aggregated over all resident household members, which is the convention the couples application always used. The two applications are now on the same accounting convention.

**The decomposition result.** The decomposition reported in this document has been rewritten twice. An early draft reported household endowments and needs as the largest component for single adults, and a one-factor figure of about seventy-seven per cent; both were withdrawn. A subsequent draft reported a four-factor preferences/access/earnings/resources-and-needs decomposition across six inequality indices, with a grouped Shapley--Owen--Shorrocks allocation; that entire apparatus is now also withdrawn, having been found by a later lineage audit to rest on a generation of run artifacts that an earlier ruling had already retired, reproduced here as a matter of record rather than as a competing result: those numbers are no longer stated as current anywhere in this document, and the retired artifacts themselves are named in the audit record, not here. Section 5 now reports a bounded, explicitly preliminary three-factor exercise (preferences, local labour-market access, earning opportunities, with resources, needs and composition held fixed), sourced from an independent replication run, separate from the retired generation, and reported with Monte Carlo simulation ranges and a second-seed check rather than parameter-uncertainty intervals, ahead of the paper's final decomposition architecture, which awaits a counterfactual-attainment estimand still under design.

**The bridge between references.** The signed gap between the flat-consumption reference and the non-work-bundle reference was previously reported with the wrong sign for couples. The premise audit in Section 6 locates the cause in the normalization of the opportunity kernel on the domain the reference mass uses, and the corrected bridge satisfies the inequality the premises require in both samples.

**The relative-index companion measure and the pay-neutrality diagnostic, removed.** An earlier draft reported bracketing counts for a third, resource-and-pay reference and a numerical wage-density-invariance residual, both cited to a since-retired welfare-record artifact. On repointing the citations, the relative-index measure did not survive: the accepted measure-correspondence audit classifies it as a different object from its theory definition, not reusable for a literal computation and not required by any current ruling, so it is removed rather than recited elsewhere. The pay-neutrality claim survives, more strongly than before: under the accepted reference construction (Mapping F, Deputy ruling R1) the home reference carries no opportunity-density, proposal, shock or intensity argument at all, an exact property of the construction rather than a numerical residual, so Section 4 states it without a magnitude.

**The consumption normalizer.** Three values of $\lambda_c$ were in circulation because different panels recomputed it over their own rows. Under exact log consumption the constant cancels from the money metric, so no result changed; the paper now reports one constant per population.

# Questions for presentation preparation

## 1. What is the question, in one sentence?

How much well-being inequality is associated with unequal job opportunities once preferences and household circumstances are made explicit? See the discussion notebook, Section 0, Scope.

## 2. What is a latent job?

An employment state, occupation, hours arrangement and wage, priced through the tax-benefit system. Availability and preferences jointly determine choices. See the discussion notebook, Section 4, The estimated model.

## 3. Which dates does the data cover?

EU-SILC collection year 2016, income reference year 2015, and EUROMOD policy year 2015. See the report Data section and its sample-funnel table.

## 4. What is the first figure showing?

The deterministic W1 construction adapted from the companion theory paper, Haydar and Maniquet (2026). See the figure Own-set equal-consumption equivalents. The stochastic implementation follows in Section 4 and the discussion notebook's Construction and the power-mean identity.

## 5. Does log consumption make welfare an arithmetic mean?

Only at $\beta_c=1$. With $\theta_c=0$ and estimated $\beta_c$, $W=[\sum_r r_{ir}C_{ir}^{\beta_c}]^{1/\beta_c}$. The estimated orders are 2.0387 and 2.1017. See the power-mean figure and the discussion notebook's Construction and the power-mean identity.

## 6. What does $\beta_c$ mean for an alternative paying twice the median?

It is both the mean's order and the own-consumption elasticity of the implied weight $C^{\beta_c}$, holding the reference probability fixed. Doubling consumption multiplies that contribution by about 4.1 (singles) or 4.3 (couples). See the power-mean figure.

## 7. Does the normalizer $\lambda_c$ affect welfare?

It cancels under exact log consumption; the numerical invariance deviation is 2.7e-15. See the discussion notebook, Section 7, Construction and the power-mean identity.

## 8. Does the proposal enter welfare, or only estimation?

It enters both: $-\log q_i^W$ corrects the singles welfare sums, and common-proposal terms correct the couples sums. It carries no economic content. See the discussion notebook, Section 7, Construction and the power-mean identity.

## 9. What happens to simulated non-positive consumption?

A one-euro floor is applied before utility evaluation: 22,597 singles and 59,821 couples node-evaluations. Those alternatives enter $J$ and $H$ alike. See the discussion notebook, Section 7, Construction and the power-mean identity.

## 10. Why is predicted mass below ten hours zero?

The panel contains no draw in $(5,10)$ despite positive structural and proposal mass; its expected count is 0.249. This tail-coverage limitation produces a genuine fit error. See the observed-versus-model fit table in the discussion notebook, Section 6.

## 11. Do the hours partitions close?

Yes. The long-hours bin includes 70, and observed singles partitions close separately by sex. See the hours-fit table in the discussion notebook, Section 6.

## 12. Is the measure independent of pay?

The reference mass is directly pay-neutral, but earning opportunities change attained welfare. This does not establish the deterministic axiom for the stochastic functional. See the reference-bridge table in Appendix C.

## 13. What do the three preliminary operators equalize, and why is a fourth one absent?

Preferences, local labour-market access and earning opportunities, each through its named pathway with coefficients fixed. Household resources, needs and composition are held fixed rather than equalized: they are not a fourth operator in this bounded exercise, and no share is attributed to them. See Section 5.

## 14. Why an exact Shapley value, and not the grouped Owen rule an earlier draft used?

With three players the exact Shapley value has a closed form over $3!=6$ orderings and needs no grouping into a priori unions. The Owen rule an earlier, now-withdrawn draft used was needed only because that draft had an additional operator, for resources and needs, to group against preferences. See Appendix B.

## 15. Is the movable share $\Delta I$ small because job opportunities do not matter?

No. It is small because household resources, needs and composition are held fixed in every coalition of this bounded exercise, and that fixed component accounts for 127 to 100 per cent of the variance of log well-being. See Section 5.

## 16. Which ordering is robust across unequivalised and equivalised reporting?

Earning opportunities dominate local labour-market access for both single adults and couples, at both scales. The preference contribution's sign is not robust between the two scales in either sample, so no directional claim is made about it. See Section 5.

## 17. How uncertain are the preliminary shares?

Two ways, never merged into a confidence interval: a Monte Carlo range across 1,000 simulation replications, and an independent check under a second simulation seed. A parameter-uncertainty interval propagated from the estimation covariance is not yet computed for this exercise. See Section 5.

## 18. What does exhaustiveness establish here?

The contributions of $P$, $A$, $B$ and the residual close to the baseline inequality to machine precision; this checks accounting for the declared three-player game, not identification of the model or resolution of the counterfactual-attainment question the game is bounded around. See Section 5.

## 19. Can welfare levels be compared across the two populations?

Each population has its own preference and opportunity reference. Results are compared within population, with raw and equivalized conventions separate. See the welfare state-level table in the discussion notebook, Section 7.

## 20. Is a nested subdivision of resources and needs available, the way an earlier draft reported one?

No. Resources, needs and composition are held fixed rather than decomposed in this bounded preliminary exercise, so there is nothing to subdivide. An earlier, now-withdrawn draft's nested resources-versus-composition split was part of the retired four-factor architecture and is not carried forward.

## 21. What happened to the earlier decomposition numbers entirely?

They are withdrawn, not corrected: the entire four-factor preferences/access/earnings/resources-and-needs architecture they were computed on traced to artifacts retired by the DECOMP-PRESEMINAR-1 ruling. See the Scientific history section for the full record and Section 5 for what is reported in its place.

## 22. What remains unresolved?

Outcome-based sample selection and the construction of the labelled-slot sampling law remain open econometric items, unrelated to the decomposition. Separately, the decomposition itself remains bounded pending a counterfactual-attainment estimand under design; Section 5 and Section 6 state exactly what that bound means for the reported shares.

## 23. Is this causal?

The decomposition is structural accounting under declared operators; it does not identify causal regional, educational or occupational effects. See the discussion notebook, Section 9, What is robust and what is not.

## 24. Can the notebooks reproduce everything?

The discussion notebook executes checks and renders current results. The research lab replays from priced inputs, with an artifact-generation caveat; raw-data preparation and pricing are separate. See the report's The research notebook section and the discussion notebook, Section 0.

# Bibliography

::: {#refs}
:::
