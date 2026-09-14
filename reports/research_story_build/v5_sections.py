"""Shared economic prose for the v5 paper and the v5 research report.

One model, one welfare formula, one result population, in both outputs.  The
report explains each step and carries the worked examples, the history and the
question-and-answer material; the paper carries the argument.  Numerical tokens
resolve at build time against the S11 specifications of record and the S12
welfare record, and a token with no source fails the build.

Block markers:
  {{paper-only}} ... {{/paper-only}}     kept in the LaTeX paper only
  {{report-only}} ... {{/report-only}}   kept in the HTML report only
"""

TITLE = ('Unequal Job Opportunities and Well-Being Inequality: '
         'A Latent-Jobs Structural Decomposition')

ABSTRACT = r'''We study how unequal job opportunities contribute to inequality in money-metric well-being. Our normative reference retains each household's own preferences and its own set of reachable jobs, while assigning the same disposable-consumption level to every job in that reference set; the money metric is the amount of consumption that, paid at the household's reference job, leaves it exactly as well off as at the situation it actually attains. We model labour supply as a choice among latent jobs and estimate preferences, job access and earning opportunities jointly on French EU-SILC data, with EUROMOD computing taxes, benefits and disposable income at every alternative work arrangement. Attributing the resulting inequality to preferences and circumstances in full requires a counterfactual-attainment estimand that is still under design; ahead of it, we introduce and implement a bounded, preliminary structural exercise, holding household resources, needs and composition fixed and simulating each household's attained well-being under counterfactual equalizations of preferences, local labour-market access and earning opportunities, with the interactions allocated by an exact three-player Shapley value. The movable inequality this bounded exercise reaches, $\Delta I$, is a small share of baseline inequality by construction, {{n:d2_deltaI_pct_singles_eq|.1f}} to {{n:d2_deltaI_pct_couples_uneq|.1f}} per cent across samples and scales, because resources, needs and composition are held fixed throughout and those account for the large majority of the variance of log well-being. Within that bounded movable share, earning opportunities dominate local labour-market access for both single-adult and couple households, at every scale we report; the sign of the preference contribution is not robust between the unequivalised and equivalised reporting conventions in either sample, so we make no directional claim about it. The quantitative opportunity decomposition is preliminary and work in progress: this is a bounded, model-based reading, not the paper's final decomposition architecture.'''

PRELIM_NOTE = ('Preliminary results throughout. The three-factor '
               'preferences/access/earnings decomposition in Section 5 is a '
               'bounded exercise ahead of the paper’s final decomposition '
               'architecture, which requires a counterfactual-attainment '
               'estimand still under design; it is reported with Monte Carlo '
               'simulation ranges and an independent second-seed check, never '
               'confidence intervals, and household resources, needs and '
               'composition are held fixed rather than decomposed.')


# =========================================================================== #
INTRO = r'''
Two people can work the same hours for the same hourly pay and be very differently placed. One chose that job from several that were open; the other took the only offer available. Their earnings are identical and their circumstances are not. Income comparisons record the outcome and cannot separate the two cases, and the difference matters for how unequal we should judge well-being to be.

The same ambiguity runs through the whole distribution. Low earnings can describe someone who values leisure highly and chose short hours, someone who cannot obtain a well-paid job, or someone whose family resources make a different work choice affordable. These are observationally entangled and economically different. A distribution of income is a distribution of outcomes with the explanations already mixed in.

The ambiguity matters for measurement, not only for interpretation. If we want to know how much of the inequality we observe is associated with unequal access to employment, hours arrangements and wage offers, we need two things that an income distribution does not supply. We need a behavioural model that separates what a household wanted from what it could reach, and we need a rule for comparing people whose opportunities and whose tastes both differ. Neither is optional: without the first there is nothing to attribute, and without the second there is no defensible way to say who is better off.

**The normative reference.** Comparing well-being when individuals face different job opportunities requires a reference that specifies how those opportunities enter the comparison. We draw on the own-set equal-consumption criterion of Haydar and Maniquet (2026), work in progress. In its deterministic formulation, the criterion assigns to an attained situation the consumption level that would make the individual's preferred job within their own ability set equally good, when every feasible job provides that same consumption. The reference therefore retains the individual's own opportunities and own preferences while removing variation in pay from the reference bundles. Writing $A_i$ for the jobs available to $i$ and $z_i$ for the attained situation, the reference level solves

$$u_i(z_i)=\max_{j\in A_i}\,u_i(W_i,j).$$

The argument being solved for is an amount of consumption, so the measure is money-metric by construction; there is no second conversion from an index into euros.

{{figure:theory}}

The first figure depicts the theoretical W1 construction adapted from the companion theory paper by Haydar and Maniquet (2026). It constructs a deterministic own-set equal-consumption equivalent, using each individual's preferred reference job. Section 4 states the empirical implementation on the current estimated model -- Mapping F, an accepted simplification that holds because staying at home maximises the non-consumption index for every household in both samples -- and derives its closed form; the deterministic figure does not depict an estimated welfare result.

One comparative static is worth stating plainly at the outset, because it is easy to misread. Holding the attained situation fixed, a person with a larger reference menu may need less uniform consumption to reach the same satisfaction. When actual opportunities change, however, both the attainment and the reference menu change. The net effect on equivalent consumption depends on both. Measuring attainment against one's own opportunities is therefore not a claim that larger menus are intrinsically better, and we make no such claim.

**The empirical approach.** The behavioural half is a random-utility, random-opportunity model of job choice. A job is a package: an employment state, an occupation, a weekly hours arrangement and an hourly wage. Households rank packages by consumption and leisure, and the packages differ in how available they are. Both the preferences and the household-specific intensity of availability enter one likelihood and are estimated jointly; neither is observed as a complete schedule. Every package is priced through the French tax-benefit system, so a change of hours or occupation moves disposable income through the actual schedule of taxes and transfers rather than a linear approximation. We estimate the model separately on {{n:n_singles}} single-adult and {{n:n_couples}} couple households drawn from French EU-SILC, with couples choosing jointly under a shared household budget.

The normative half then yields, for each household, an equivalent flat consumption level. Attributing its inequality to preferences and to circumstances in full requires a counterfactual-attainment estimand for the bundle a household would attain under a counterfactual environment, and that estimand is still under design. Ahead of it we report a bounded, preliminary exercise: we define three structural equalization operators, one for preferences, one for local labour-market access and one for earning opportunities, holding household resources, needs and composition fixed throughout; we recompute every household's welfare level, and the inequality of the resulting distribution, under each of the eight coalitions of those three operators, reusing the model's own already-priced estimation panel with no re-estimation and no new pricing; and we allocate the interactions among them with an exact three-player Shapley value. The allocation is exhaustive by construction and the closure is verified numerically rather than imposed.

**What we find.** The movable inequality this bounded exercise reaches, $\Delta I=I(\text{actual})-I(\text{P,A,B equalized})$, is small by construction: {{n:d2_deltaI_pct_singles_eq|.1f}} to {{n:d2_deltaI_pct_couples_uneq|.1f}} per cent of baseline inequality across samples and reporting scales. That is a property of the design, not evidence that opportunities are unimportant: household resources, needs and composition are held fixed in every coalition, and that fixed component alone accounts for {{n:d2_varshare_logC_couples|.0f}} to {{n:d2_varshare_logC_singles|.0f}} per cent of the variance of log well-being. Within the movable share, earning opportunities dominate local labour-market access for both household types, at every scale we report, from {{n:d2_shareB_singles_uneq|.1f}} per cent of $\Delta I$ (single adults, unequivalised) to {{n:d2_shareB_couples_eq|.1f}} per cent (couples, equivalised); local labour-market access is second and smaller throughout. We report that ordering as a finding and do not attach a mechanism to it.

Two qualifications belong with the headline. First, the preference contribution's sign is not robust between the unequivalised and equivalised reporting conventions, in either sample: we therefore make no directional claim about it, only about the ordering of access against earnings. Second, an allocated share is an average of marginal contributions over coalition orders. It is not the reduction that equalizing that factor alone would achieve; Section 5 reports both and explains why they can differ, and reports the exact scale at which excluding the model's anchored-attainment arm moves $\Delta I$, as a robustness check on the design rather than on the estimates. This is a bounded, preliminary reading, reported ahead of the paper's final decomposition architecture, and it should be read as such throughout.

**Relation to existing work.** Every ingredient here has antecedents, and the contribution is the combination and the empirical answer, not any one step.

Modelling labour supply as choice among latent jobs, with preferences and offer intensities identified jointly from one likelihood, is due to @aaberge1995 and @aaberge1999, developed by @dagsvikstrom2006 and @dagsvikjia2016, surveyed by @aaberge2018, and set out for applied work by @capeau2016. We inherit that framework, including its distinction between the intensity of an offer and the probability of a choice, and its reliance on excluded opportunity shifters to separate components that choices alone identify only jointly. @capeau2016 also supply two of the identifying restrictions we maintain: the wage-offer distribution is independent of offered hours, and a local unemployment measure shifts availability while being excluded from preferences. Their Belgian application already covers single women, single men and couples, so covering both household types is not itself a contribution.

Combining such a model with a monetary welfare evaluation is also established. @aaberge1995 translate attained utility into an equivalent income against a stated reference household, choice set and tax system, and @aaberge2004 evaluate reforms with joint household choice and restricted hours. @jiathoresen2021 make the case for the job-choice model in exactly this role and report a distribution of compensating variation for a Norwegian reform, and @jacquet2026 compare a standard compensating variation with one computed after replacing preference characteristics by reference values. All four evaluate a *change* between policy regimes. Our object is a cross-sectional distribution of levels under one policy system, and its attribution. A reform gain and a level have different origins and different denominators; a small preference-related reform difference would not imply a small preference share in our decomposition, and our shares do not estimate their reform gains.

The normative half draws on the literature that refuses to resolve interpersonal comparison by assuming common preferences. @fleurbaeymaniquet2006, @fleurbaeymaniquet2017 and @fleurbaeymaniquet2018 set out how a reference bundle encodes a position on compensation and responsibility; @decosterhaan2015 and @bargain2013 show empirically how much a welfare ordering moves with that choice. Their references fix a wage or an unearned-income intercept and maximize over a deterministic budget set. Ours fixes consumption across the alternatives of an estimated opportunity distribution and integrates. That is a different reference and, as Section 6 records, the ordering is sensitive to it.

The closest decomposition precedents are two. @muehlhan2023 combines a structural labour-supply model with involuntary-unemployment restrictions and a Shapley attribution, decomposing the change in German household *income* inequality into temporal factors and binary restrictions. @creedyherault2011, in the section that constructs money-metric distributions under alternative policy and population states, decompose a change in inequality and social welfare by averaging over the two orders in which policy and population can be changed; theirs is the closest money-metric welfare-inequality decomposition we know. Both are decompositions of a *change* between two situations, with policy, population or temporal factors as the factors. Ours is a decomposition of a cross-sectional *level* of well-being inequality, with the factors defined as structural operators inside an estimated job-choice model: what a household prefers, which jobs it can reach, what those jobs pay, and what its budget and needs are. The wider behavioural-simulation decomposition tradition, @bargain2012 and @jessen2019, decomposes income changes in the same spirit.

The allocation rule is inherited outright. @shorrocks1982 states the accounting requirements a decomposition should satisfy; @shorrocks2013 places the Shapley value at the centre of distributional decomposition; @sastretrannoy2002 documents how much the answer can depend on how the exercise is set up. The preliminary three-operator exercise of Section 5 needs no grouping and uses the plain Shapley value on a three-player game; @owen1977's extension to games with a priori unions, and the grouped nonlinear practitioner's account of @audoly2025, are the tools an earlier, now-withdrawn four-operator version of this exercise required, cited here for completeness rather than as machinery the current preliminary exercise uses. We claim no new allocation principle. Complete recomputation of every coalition, rather than a linear approximation, likewise has precedents and is better described as methodological discipline than as a contribution.

What is new, to our knowledge, is the conjunction: a random-utility random-opportunity model of job choice, an opportunity-sensitive money-metric welfare level built on the own-set equal-consumption reference, and a bounded, preliminary structural preference/access/earnings game whose operators are defined inside that estimated model, with complete recomputation of welfare and inequality under every coalition. The application-specific methodological contribution is the game and its counterfactual operators, reported as preliminary and work in progress pending the counterfactual-attainment estimand of Section 4. The cooperative-game allocation rule is inherited.

**Roadmap.** Section 2 describes the data and the household budget construction. Section 3 presents the latent-jobs model, its identifying restrictions and its estimation. Section 4 defines the money-metric welfare measure and the structural decomposition. Section 5 reports the behavioural and welfare results for both household types. Section 6 examines sensitivity and states the limitations. Section 7 concludes.
'''

# =========================================================================== #
DATA = r'''
The data are French EU-SILC, collection year {{n:collection_year}}, with income reference year {{n:income_year}}. Taxes, benefits and disposable income are computed by EUROMOD [@sutherlandfigari2013] under the French {{n:policy_year}} policy system, which is the system in force over the income reference period. We use the same three dates consistently: the survey is collected in {{n:collection_year}}, incomes refer to {{n:income_year}}, and the simulated policy system is {{n:policy_year}}.

## The estimation samples

{{table:funnel}}

The screens are of three kinds and it is worth separating them. The first two define the decision unit: the household must contain either one unpartnered adult or two mutually linked adults of opposite sex, and every decider must be between twenty and sixty. This is the largest exclusion and it is structural. Multi-generational households, flat-shares, adult children living with parents and same-sex couples are outside the estimated population, and no result extends to them. Because the age screen binds on both spouses, it removes proportionally more couples than singles.

The second kind removes households for whom the model does not define an offer set: adults in full-time education, households receiving an old-age, disability or survivor pension, and deciders whose labour-market status lies outside employment, unemployment and inactivity. Together with the pension screen this is why the surviving employment rate is high. The employment share below should be read as a share among people for whom working is a live option, not as a French employment rate.

The third kind is support. An employed decider's observed hours must lie in the closed interval $[{{n:hours_floor}}, {{n:hours_cap}}]$ hours per week and the delivered hourly wage in $[{{n:wage_lo}}, {{n:wage_hi}}]$ euros per hour, because those are the boundaries of the supports the opportunity densities are defined on. An observed occupation must map into the four modelled groups; ISCO 0, the armed forces, does not, and the resulting exclusion is *unsupported* occupation, not missing occupation. Three single-adult households whose own observed job prices to non-positive disposable consumption are removed, because the log-consumption term is undefined at their observed choice; non-positive *simulated* alternatives receive a one-euro consumption floor before utility is evaluated. The floor applies to 22,597 single-adult and 59,821 couple node-evaluations, all of them sampled alternatives entering the estimated choice likelihood. It does not affect the welfare measure of Section 4, which evaluates only each household's own observed job and its home state, both already screened to strictly positive consumption.

{{table:occmap}}

## What the households look like

{{table:descriptives}}

{{figure:datapanel}}

Education is the three-level ISCED grouping, with the medium level as the omitted reference in the wage equation. Potential experience is years since leaving education, entering the wage equation in units of {{n:experience_scale}} years, with the square recomputed after scaling rather than carried forward. A child is any resident household member under {{n:child_cutoff}}, counted without a parent link. Age enters preferences centred on the sample mean decider age and divided by {{n:age_scale}} years.

{{table:regimes}}

## The household budget

For a given work arrangement the tax-benefit model is given the implied gross labour inputs, weekly hours, hourly wage, and earnings split at the thirty-five hour threshold, together with the household's non-labour inputs and roster, and returns disposable income. Only deciders receive counterfactual overrides; other members keep their baseline values. The accounting identity linking original income, benefits, taxes and social contributions to disposable income holds to machine precision at both the person and the household-alternative level, before and after the benefit take-up adjustment. Disposable income is summed over all resident members of the household.

{{figure:resources}}

Panel (c) of the figure reports the *incidence* of non-labour budget inputs by family, not a cash total. Some of these are stocks, some are annual flows and some are monthly; they are inputs to the tax-benefit calculation and are not added together into one income concept. The pension family is empty by construction, because pension receipt is a sample screen. Panel (a) reports the tax-benefit *output* at the observed job, which is an object of a different kind and is never added to panel (c).

Local labour-market conditions enter through a group unemployment measure, a population-weighted exposure index for the decider's region and age-education cell, stored as a fraction and entering the employment index multiplied by {{n:gsur_scale}}. Regional and urbanisation variation supports the access specification conditional on the exclusion restriction and the functional form; it does not by itself identify access, and no causal effect of geography is claimed anywhere in this paper.
'''

# =========================================================================== #
MODEL = r'''
A job is a package $j$: an employment state $e\in\{0,1\}$ and, when employed, an occupation $k\in\{1,\dots,{{n:n_occ}}\}$, weekly hours $h\in[{{n:hours_floor}},{{n:hours_cap}}]$ and an hourly wage $w\in[{{n:wage_lo}},{{n:wage_hi}}]$. The base measure $\nu$ places counting mass on the single non-employment point and, on the employed part, counting measure over occupations with Lebesgue measure over hours and wages. A household chooses one package; a couple chooses one pair of packages under a shared budget.

## Preferences

Let $C_i(j)$ be priced monthly disposable consumption at $j$ and $\ell_i(j)$ normalized leisure, $({{n:time_endowment}}-h)/{{n:leisure_scale}}$ hours per week, floored at one hour. For a single adult of sex group $g$, deterministic utility is

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

The normalizer $\lambda_c$ is a units convention. Under exact log consumption it enters the index as the alternative-invariant constant $-\beta_c\log\lambda_c$, so it cancels from every choice probability; it does not appear in the accepted welfare measure of Section 4 at all.

{{report-only}}
> **Why the leisure coefficients are not the preferences.** A leisure weight is a coordinate in a chosen normalization, not an economic magnitude. Changing the leisure normalizer $\lambda_\ell$ multiplies the weight and its box endpoints by the same factor, and the indifference curves and the marginal rate of substitution are unchanged exactly. The panels below therefore show the invariant objects; the coefficient table is a coordinate readout. Reparameterization also does not bear on whether a bound binds, since the endpoint moves with the coefficient. What settles that is re-estimation with wider bounds, and nothing else.

{{figure:normalization}}
{{/report-only}}

## Opportunities

The opportunity density gives the relative intensity with which packages are available to household $i$, before any choice is made. It is a product of **four** factors, switched off on non-employment by the employment indicator $E_{ij}=\mathbb 1\{h_{ij}>0\}$:

$$
g_{ij}=g^{E}_{ij}\cdot\left(g^{H}_{ij}\cdot g^{\mathrm{Occ}}_{ij}\cdot g^{W}_{ij}\right)^{E_{ij}} .
$$

**Access**, $g^{E}_{ij}=\exp\{\beta_E+\beta_s s_i+\sum_{r=2}^{8}\beta_r\,\mathrm{reg}_{ir}+\beta_u u_i+\beta_m m_i\}$, carries the local group unemployment measure $s_i$, the region indicators and urbanisation, and is the factor inside which local-market access lives. **Hours**, $g^{H}_{ij}=\exp\{\sum_b \beta_b\mathbb 1\{h_{ij}\in b\}\}$, elevates five bands over a residual reference set of total width {{n:hours_reference_width}} hours per week, so every band coefficient is read against that residual and none of the five is normalized to zero; the narrow full-time band $[33.5,36.5)$ is a density elevation over an interval, not an atom at thirty-five hours. **Occupation**, $g^{\mathrm{Occ}}_{ij}=\exp\{\beta^{\mathrm{occ}}_{k,g}\}$ with $\beta^{\mathrm{occ}}_{1,g}\equiv 0$. **Wage offer**, $g^{W}_{ij}$, is log-normal with location $\mu_i=\beta_{w0}+\beta_{wL}L_i+\beta_{wH}H_i+\beta_{wx}x_i+\beta_{wx^{2}}x_i^{2}+\delta_{\mathrm{occ}}$ and dispersion $\sigma$, truncated to $[{{n:wage_lo}},{{n:wage_hi}}]$ euros per hour and renormalized on that support.

Two properties of the normalization matter later, for estimation and for the identification argument below. Write $\widehat g_{ij}=g_{ij}/Z_i$ for the density normalized to unit mass on the whole package space. The wage factor integrates to one *conditional on employment and occupation*, because the truncated density is renormalized on its own support; and the non-consumption index $L_{ij}$ has no wage argument. The pay-neutrality property of the welfare reference established in Section 4 rests on a simpler fact than either of these: the reference job itself, staying at home, carries no opportunity-density argument at all, so none of $g$, the proposal, the shock or an intensity parameter enters the reference.

The four blocks are what the decomposition later separates. Employment and occupation access are one mechanism; the distribution of wages conditional on an occupation is another; neither is the same as non-labour resources or household needs.

{{report-only}}
> **What the kernel adds, concretely.** Two employed single adults can share an employment state, an occupation group, an hours band and an observed-wage quintile, and still differ substantially in their estimated opportunity kernels: the mass the kernel places on employment, the shape of the hours density, the occupation mass and the conditional wage location are all household-specific. Two people who look identical in an income table are, in this model, facing different menus. An earlier draft illustrated this with a matched pair of households; that illustration was drawn at the superseded consumption numeraire and is not reproduced here rather than shipped with a disclaimer.
{{/report-only}}

## Identification, in words

Choices alone do not separate a taste for leisure from a scarcity of jobs at that number of hours. Three kinds of restriction do the work. Preferences are smooth in hours through the leisure index, while the opportunity density is a step function over bands, so a spike in observed hours at a band is read as availability rather than as a kink in tastes. Excluded shifters enter availability and not preferences: the local group unemployment measure and the regional and urbanisation indicators shift the employment index and appear nowhere in utility. And the wage-offer distribution is specified as independent of offered hours conditional on occupation, which separates the wage location from the hours density. These are the restrictions of @capeau2016 and @dagsvikjia2016, maintained here rather than tested. The regional variation supports the access block conditional on those restrictions; it does not establish separate identification on its own, and it is not a causal design.

## Estimation

The choice set is a continuum, so the likelihood is evaluated over sampled alternatives. For each household we draw $R={{n:n_draws}}$ alternatives from a proposal density $q_{ij}$ and place the observed package in the set as well, giving a set $\mathcal C_i$ with $|\mathcal C_i|={{n:n_alt_rows}}$ rows. Write the sampled-set index

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

{{paper-only}}
Two features of the observation rule remain genuinely open and are stated here rather than in a footnote. The sample screens on the observed hours and wage of employed deciders, so the estimation sample is selected on an outcome of the process being modelled. The conditional likelihood above is the correct object for a sampled choice set; it is not automatically the correct object for an outcome-selected sample, and we have not established which correction, if any, the screen requires. Separately, the derivation of the sampled-set probability conditions on a labelled collection of slots; small observed cross-coordinate correlations and a binomial-looking multiplicity distribution are consistent with independent draws but do not by themselves establish the sampling law. Both are recorded as unresolved in Section 6.
{{/paper-only}}
'''

# =========================================================================== #
WELFARE = r'''
## The verified Mapping-F $W^1_F$ construction

The accepted welfare measure (Deputy ruling R1, Mapping F, `JMP_W1_fork_ruling_v1.md`) is the amount of consumption that, paid at a fixed reference job $o$, leaves the household exactly as well off as at its attained situation:

$$
W^1_{i,F}=m_i(o;z_i), \qquad u_i\big(m_i(o),o\big)=u_i(z_i).
$$

This is the theoretical own-set equal-consumption criterion above (Measure 1), $u_i(z_i)=\max_{j\in A_i}u_i(W_i,j)$, specialised to the reference job $o$ that the maximisation over the household's own reachable set actually selects. On the current empirical domain the selected reference job is always staying at home: for every household in both samples, non-employment maximises the non-consumption index, so the maximisation collapses to a single evaluation at the household's own observed job against its own home state, $o$. Under the log-consumption specification of Section 3 this gives the closed form

$$
\boxed{\;W^1_{i,F}=C_i^{\mathrm{obs}}\exp\!\left[\frac{L_i(j_i^{\mathrm{obs}})-L_i(o)}{\beta_c}\right],\;}
$$

where $C_i^{\mathrm{obs}}$ is the household's own priced disposable consumption at its observed job, $L_i(j_i^{\mathrm{obs}})$ and $L_i(o)$ are the non-consumption index at the observed job and at the home state, and $\beta_c$ is the estimated consumption weight. Four objects do not enter this construction at all: the opportunity density $\widehat g$, the numerical proposal $q$, the behavioural shock, and any latent-set intensity parameter -- opportunities act on this measure only through the attained bundle $j_i^{\mathrm{obs}}$, never through an average or an integral over jobs the household did not take. That home always maximises the non-consumption index, so that $W^1$ coincides here with the staying-home equivalent, is an empirical-domain property of this specification and this estimated model, verified directly rather than assumed; it is not a theorem of the Haydar-Maniquet framework, which defines the reference job $o$ as whichever job the maximisation selects and does not guarantee it is staying at home.

The construction is independently verified. A reconstruction that does not import the production code reproduces every pre-registered check -- non-workers equal their own observed consumption exactly, workers strictly below it, no route by which $\widehat g$, $q$, the shock, or an intensity parameter can enter -- and reproduces the committed sample aggregates for both populations to machine precision (`baseline_f1_verification_v1.md`, MNL commit `6048c9f7`, independently verified `b5550af5`).

{{report-only}}
## A retired alternative construction

An earlier draft evaluated welfare with a different, model-integrated construction: an ex-ante inclusive-value functional built from two integrals, $J_{i,S}$ and $H_{i,S}$, over the estimated opportunity density and the behavioural shock, equal to a weighted power mean of consumption of order $\beta_c$ under a reference measure derived from that density. The measure-correspondence audit (`JMP_measure_map_v1.md` and its acceptance record) classifies that functional as a DIFFERENT OBJECT from the theoretical own-set equal-consumption criterion, not the literal Measure 1 computation, and Deputy ruling R2 (`JMP_W1_fork_ruling_v1.md`) retired it. It produced no reported number anywhere in this document: every welfare level, Gini and decomposition share reported here and in Section 5 is computed from the verified Mapping-F $W^1_F$ construction above. It is recorded here, retired, as a matter of history, not as an alternative reading of the paper's measure.
{{/report-only}}

## What the reference does and does not do to pay

The reference does not depend on pay. The accepted construction's home reference (Mapping F, Deputy ruling R1) is a fixed singleton state whose systematic utility carries no opportunity-density, proposal, behavioural-shock or intensity argument, so none of those four objects enters it at all.

Changes in earning opportunities nevertheless change the measure, because they change what the household attains, not the reference it is compared against. The correct statement is therefore narrow and we make only it: *the reference is directly pay-neutral, and earning opportunities reach the measure through the attained evaluation.* We do not report a magnitude for that attained-side channel here: quantifying it under a counterfactual equalization of earning opportunities is a decomposition question, and Section 5 reports only the bounded, preliminary exercise available for that. A qualitative channel existing does not establish that the deterministic independence-of-pay axiom fails for this stochastic functional. That would require fixing the primitives the axiom holds fixed and proving the property, which we have not done and do not claim.

{{report-only}}
### A worked illustration, in the current construction

Not a description of any real household. Consider a household whose observed job's non-consumption index exceeds the index at staying home by exactly one nat, $L_i(j_i^{\mathrm{obs}})-L_i(o)=1$. The closed form then gives $W^1_{i,F}=C_i^{\mathrm{obs}}\exp(1/\beta_c)$: its welfare equals its own observed consumption scaled up by exactly the same factor the natural-unit conversion above reports, {{n:nat_factor_singles|.3f}} for the single-adult specification and {{n:nat_factor_couples|.3f}} for couples. A one-nat gap in the other direction scales consumption down by the reciprocal of that factor instead. This is a mechanical property of the closed form, not an empirical claim about any household in the sample; realised gaps and the resulting levels, for the sample households, are in the table above.
{{/report-only}}

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

{{table:operators}}

Welfare and inequality are then recomputed from the model for all eight coalitions of $\{P,A,B\}$. There is no linearisation and no re-estimation: coefficients are held at their estimates throughout, and only the arguments move.

The interactions are allocated with the **exact Shapley value** [@shorrocks2013] on the three-player game $v$: the average of each factor's marginal contribution over all orderings in which the three factors can be equalized. With three players this average has a closed form over $3!=6$ orderings and requires no grouping. The allocation is exhaustive: the contributions sum to $\Delta I=I_\varnothing-I_{\{P,A,B\}}$, and we report $\Delta I$ itself rather than treat it as identically zero, because household resources, needs and composition remain in the residual $I_{\{P,A,B\}}$ along with sex-block parameter differences and behavioural randomness.

Uncertainty is reported two ways, never merged into a confidence interval: a Monte Carlo range across 1,000 simulation replications at fixed estimates, and an independent check under a second simulation seed. Neither is a parameter-uncertainty interval; propagating the estimation covariance into this exercise is future work.

{{report-only}}
> **What is new and what is inherited, in this preliminary exercise.**
>
> *Inherited.* The latent-jobs model of labour supply and its identifying restrictions; the joint estimation of preferences and offer intensities; the use of a microsimulation model to price alternatives; the money-metric idea and the discipline of stating the reference; the Shapley value as the allocation rule for a cooperative game with additively separable worth.
>
> *Application-specific contribution.* The bounded three-factor game itself: preferences, local labour-market access and earning opportunities as pathways inside an estimated job-choice model, holding resources, needs and composition fixed by design pending a counterfactual-attainment estimand.
>
> *Not claimed.* A new Shapley rule; that this is the paper's final decomposition; that the small movable share, $\Delta I$, means opportunities are unimportant, rather than that most of what determines the money metric's dispersion is held fixed in this exercise by construction.
{{/report-only}}
'''

# =========================================================================== #
RESULTS = r'''
## Behavioural estimates

The estimated model has {{n:kfree_singles}} free coordinates for single adults, of which {{n:kint_singles}} are interior, and {{n:kfree_couples}} for couples, all interior. The criterion is {{n:negll_singles|.3f}} and {{n:negll_couples|.3f}} respectively. Across ten terminal paths from five starts under two polishing contracts, the criterion varies by {{n:spread_singles}} for single adults and {{n:spread_couples}} for couples, and the smallest eigenvalue of the exact Hessian on the interior block is {{n:mineig_singles|.4f}} and {{n:mineig_couples|.4f}}. One single-adult coordinate, the female age-square term in the leisure weight, sits at a box endpoint; its interval is reported under the active-set convention in the appendix and it is excluded from the interior curvature.

{{table:pref}}

The consumption weight is {{n:beta_c_singles|.4f}} with a cluster-robust standard error of {{n:beta_c_se_singles|.4f}} for single adults and {{n:beta_c_couples|.4f}} with {{n:beta_c_se_couples|.4f}} for couples. Two things follow. In the closed-form welfare measure of Section 4, $\beta_c$ is the rate at which a household's non-consumption advantage at its observed job over staying home, $L_i(j_i^{\mathrm{obs}})-L_i(o)$, converts into a proportional adjustment of its own observed consumption: the same advantage moves the money metric proportionally less, the larger $\beta_c$ is, because the advantage enters the exponent divided by $\beta_c$. And because utility is on the unit-scale shock, one natural unit of the index corresponds to multiplying consumption by $\exp(1/\beta_c)$, a factor of {{n:nat_factor_singles|.3f}} for single adults and {{n:nat_factor_couples|.3f}} for couples. That is a proportional statement: there is no single euro value of a unit of utility independent of the consumption at which it is evaluated.

{{table:access}}

{{table:wage}}

**Maintained restrictions.** Singles: `theta_c_singles = 0`; the couples preference block (`beta_l0_m`, `beta_l_age_m`, `beta_l_age2_m`, `beta_l0_f`, `beta_l_age_f`, `beta_l_age2_f`, `beta_l_nkids_f`, `theta_l_f`) does not enter the singles likelihood; and `beta_E_y2015` and `beta_E_y2017` are absent because the 2015 and 2017 data are not used. Couples: `theta_c = 0`, the male children leisure effect is structurally zero, and the direct cross-leisure term is fixed at zero. These are restrictions, not estimates. The singles and couples models are estimated separately, so their wage blocks are not restricted to agree, and the difference between the two experience profiles should not be read as a test.

{{figure:prefsingles}}

{{figure:prefcouples}}

{{figure:mrs}}

The indifference curves and the marginal rate of substitution are the economics; the coefficients are coordinates. Note that the consumption axis is logarithmic and the curves are drawn over the plotted range only: under $L(\ell)+\beta_c\log(C/\lambda_c)$, any finite utility target at positive leisure is reached at the finite positive consumption $C=\lambda_c\exp\{(\bar u-L(\ell))/\beta_c\}$, which is strictly positive for every finite target. A curve leaving the frame has left the plotting range, not the domain of the model, and nothing here is economically infeasible.

{{report-only}}
{{figure:marginal}}

{{figure:nat}}

The euro value of one natural unit of the index is proportional rather than fixed: it rises with the consumption at which it is evaluated, so there is no single euro figure for a unit of utility independent of a baseline. This is a reading aid for the estimated scale, not an economic result.
{{/report-only}}

## Fit

The fit reported here is a population prediction, computed by integrating the estimated model over the opportunity distribution and the taste shocks. It is not a sampled-menu choice probability and it is not an in-sample fitted value. We report it band-referenced: each group's weighted extensive-margin accuracy is compared not to a 100 per cent target -- a correctly specified stochastic-choice model does not attain one -- but to the 95 per cent band that model itself would produce by chance, from 500 outcome vectors simulated at the fitted estimates.

{{figure:fitband}}

Aggregate participation and occupation margins are reproduced reasonably closely, while hours fit is uneven. Individual-level predictive diagnostics raise possible excess stochastic dispersion in some groups; the group-level classification is not used as a headline result.

The figure below shows each group's weighted extensive-margin accuracy against its own simulated 95 per cent band, restricted to the groups whose extensive-accuracy statistic clears the pre-registered numerical-adequacy gate (Monte Carlo simulation error at most 0.25 times the same sampling variation): coupled women, coupled men and single women clear it on the weighted statistic and are shown; single men do not and are withheld rather than shown with a caveat, because a statistic the quadrature cannot resolve is not a weaker finding, it is not a finding. Coupled men clear the weighted gate only narrowly -- ratio 0.240 against the 0.25 threshold -- and miss the unweighted version, 0.250; the weighted rule is applied throughout. Within the three shown, observed accuracy is inside its band for coupled women and single women, and above the top of its band for coupled men. Clearing this extensive-accuracy gate is a narrower question than the group-level fit classification discussed in the limitations below, which draws on a wider set of statistics and is inconclusive -- not passing -- for single women specifically. Section 6 records where the fuller diagnostic set -- calibration by predicted decile, the joint hours/occupation confusion structure, and the group withheld here -- still has open questions.

{{report-only}}
### The full margin-by-margin comparison

{{figure:fit}}

{{table:fitsingles}}

{{table:fitcouples}}

The mean absolute deviation over all population moments is {{n:mae_singles|.4f}} for single adults and {{n:mae_couples|.4f}} for couples, but the informative content is margin by margin. Employment and the joint participation regimes are matched closely; the narrow full-time band around thirty-five hours is matched closely for both sexes; occupation shares given work are matched to within about one percentage point. The largest single discrepancy in both models is the upper full-time band $[36.5,40.5]$, which the model under-predicts by about nine percentage points for single men and seven for women in couples, with the mass appearing in the adjacent bands. The sub-ten-hour fit cell is also a genuine prediction error: the realized integration panel predicts zero against observed shares around one per cent. Both the structural hours density and the proposal assign positive mass to $(5,10)$: about 4.15 per cent of normalized structural hours mass and 0.00019 per cent conditional proposal mass. With an expected draw count of only 0.249, the realized panel contains no draw there. This is a tail-coverage limitation of the integration panel, distinct from the adjacent-band fit discrepancy. The long-hours bin closes at 70 inclusive, and the observed singles hours partitions close separately by sex.

{{table:benchmark}}

The two re-estimated common-opportunity benchmarks are worse by {{n:rum_gap|.2f}} and by a larger margin, on the same households, the same sampled alternatives and the same criterion. The comparison is a nested one in the sense that the benchmarks restrict the opportunity block and re-estimate everything else, but we do not convert it into a formal test, because the sampled-alternative criterion is not the likelihood of the observed data and the conditions for a likelihood-ratio distribution are not established here. What the table does support is that the deterioration is concentrated where the opportunity block does its work: the population fit worsens from {{n:mae_singles|.4f}} to {{n:mae_ruma|.4f}} and {{n:mae_rumb|.4f}}, and the occupation margins deteriorate by an order of magnitude, from about half a percentage point to eleven. A better criterion does not by itself establish that a mechanism has been identified.
{{/report-only}}

## Within-sample equivalised results

{{table:baselinef1}}

The verified $W^1_F$ construction gives, on the modified-OECD-equivalised basis, a weighted Gini of {{n:w1f_eq_gini_singles|.4f}} for single-adult households and {{n:w1f_eq_gini_couples|.4f}} for couples, against {{n:ceq_gini_singles|.4f}} and {{n:ceq_gini_couples|.4f}} for equivalised disposable consumption in the same samples. This is a within-sample descriptive dispersion comparison, not a welfare-loss statement: the ratio $W^1_F/C^{\mathrm{obs}}$ reflects the systematic leisure term at the observed job relative to home leisure, and we do not construct a loss index from it. Singles and couples are reported separately throughout, with no pooled distribution and no cross-sample level comparison: the two are separate estimation frames with different welfare units, and a comparison of the two levels is not drawn here or elsewhere in this paper.

## The preliminary decomposition

{{table:pabcoalitionsingles}}

{{table:pabcoalitioncouples}}

{{figure:pabarch}}

The eight rows per scale are the coalition values of the three-player game. $\Delta I=I(\varnothing)-I(\{P,A,B\})$ is small in every sample and scale -- {{n:d2_deltaI_pct_singles_eq|.1f}} per cent of baseline inequality for single adults equivalised, up to {{n:d2_deltaI_pct_couples_uneq|.1f}} per cent for couples unequivalised -- and that is a property of what this exercise holds fixed, not a finding that job opportunities are unimportant: household resources, needs and composition are held fixed in every coalition, and that fixed component alone accounts for {{n:d2_varshare_logC_couples|.0f}} to {{n:d2_varshare_logC_singles|.0f}} per cent of the variance of log well-being (variance-decomposition detail in the discussion notebook, Section 8). Sex-block parameter differences and behavioural randomness also remain in the residual and are not attributed to $P$, $A$ or $B$.

{{table:pabshapley}}

{{figure:pabdecompsingles}}

{{figure:pabdecompcouples}}

Within the movable share $\Delta I$, earning opportunities dominate local labour-market access for both household types, at every scale we report: from {{n:d2_shareB_singles_uneq|.1f}} per cent of $\Delta I$ for single adults unequivalised to {{n:d2_shareB_couples_eq|.1f}} per cent for couples equivalised, against {{n:d2_shareA_couples_uneq|.1f}} to {{n:d2_shareA_singles_eq|.1f}} per cent for local labour-market access. We make no directional claim about the preference contribution's sign: it changes between the unequivalised and equivalised reporting conventions in both samples, from {{n:d2_giniP_singles_uneq|.4f}} to {{n:d2_giniP_singles_eq|.4f}} Gini points for single adults and {{n:d2_giniP_couples_uneq|.4f}} to {{n:d2_giniP_couples_eq|.4f}} for couples.

The allocated shares are not one-factor effects. An allocated share is an average of marginal contributions over the orders in which coalitions can form; the coalition table above reports the one-factor effect directly, as the change from the actual coalition for the single-letter row. The two can differ, and with three players and an exact Shapley value the difference is fully accounted for by the interaction terms, which the closed form makes explicit.

**Robustness.** Every coalition Gini level and every Shapley contribution reproduces closely under an independent second simulation seed, including the sign instability of the preference contribution, which appears in both runs. Excluding the estimation panel's anchor node -- the household's own observed choice, inserted deterministically in every coalition, which mechanically anchors counterfactual attainment toward the observed outcome to a small, roughly common degree ({{n:d2_anchorshare_singles|.1f}} per cent of single adults and {{n:d2_anchorshare_couples|.1f}} per cent of couples attain it under any coalition) -- moves $\Delta I$ by at most {{n:d2_anchormove_pct|.1f}} per cent ({{n:d2_anchormove_cell}}), with no sign flip in any specification.

{{report-only}}
A Monte Carlo share range for each factor -- the across-replication spread of one replication's own share, dividing by that replication's own near-zero $\Delta I$ -- is available in the discussion notebook's technical gallery alongside this table, with its own caveat that it is reported for completeness and is not informative on its own. It is not reproduced here: the Gini-point contribution and the second-seed check above are the informative comparison for a reader of this report.
{{/report-only}}

The allocation is exhaustive to numerical precision: the residual after summing $P$, $A$, $B$ and $\Delta I$ back to $I_\varnothing$ is zero to machine precision in every sample and scale, verified rather than imposed. That is a computational validation of the accounting for the declared game. It does not validate the identification of the model, the normative content of the operators, or a resolution of the counterfactual-attainment question this exercise is deliberately bounded around.
'''

# =========================================================================== #
SENSITIVITY = r'''
## Equivalization and the preliminary decomposition

Equivalization is a normative choice, and the preliminary decomposition of Section 5 moves with it. On the equivalized basis the movable share $\Delta I$ is larger relative to baseline inequality for both household types than on the raw household basis, and the earning-opportunities/local-access ordering is unchanged in every case: earning opportunities dominate at both scales, for both household types. The preference contribution's sign already differs between the two scales at the raw comparison reported in Section 5; equivalization is one of the two axes that sign instability spans, not an independent further concern. Both bases are reported throughout; neither is the correct one, and the choice between them is not settled by the data. We do not report a male-primary or other alternative reference-block variant of this preliminary exercise; that sensitivity, reported for the welfare baseline itself in Section 4, has not been re-run through the bounded decomposition.

## Two open econometric questions

The sample screens on the observed hours and wage of employed deciders. The estimation sample is therefore selected on an outcome of the process being modelled, and the conditional sampled-set likelihood, which is the right object given a sampled choice set, is not automatically the right object given an outcome-selected sample. We have not established which correction the screen requires, or that none is required. This is an econometric question and not a presentational one, and it is not resolved by the diagnostics reported above.

Separately, the sampled-set probability is derived by conditioning on a labelled collection of slots. Small observed cross-coordinate correlations and a multiplicity distribution consistent with independent draws are diagnostics; they do not by themselves establish the sampling law that the derivation assumes. Both questions are recorded here as open.

{{report-only}}
## The consumption normalizer

{{table:lambda}}

Three normalizing constants were in circulation between the estimation frames and the welfare panel, because each panel computes the constant as a mean over its own rows. Under exact log consumption the constant is alternative-invariant, so it cancels from every choice probability; it does not enter the accepted $W^1_F$ welfare measure at all (Section 4), so none of the three values changes any reported welfare quantity. The paper reports the estimation-frame constant throughout, for the choice-probability role it actually plays, and the discrepancy across panels is recorded here rather than silently harmonised.

A retired alternative construction that did once carry $\lambda_c$ into a welfare formula, and a bridge comparing it against a second reference, are recorded in the Scientific history section rather than here: both traced to the ex-ante inclusive-value functional Deputy ruling R2 retired, and neither is reported as a result anywhere in this document.
{{/report-only}}

## Limitations

Six limitations travel with the results above, named together here rather than scattered through the text they qualify.

**Local labour-market access runs only through geography and year in this specification.** The operator $A_i$ of Section 4 -- local labour-market access -- carries region, urban/rural status and survey year; it does not carry any individual capability, education-specific or occupation-specific access channel. What the preliminary decomposition attributes to $A$ is therefore the coarse geographic and temporal component of access, not access in the fuller sense of what an individual with particular skills or credentials can reach; a more personal access channel, if identified, would move some inequality currently attributed elsewhere into $A$, in a direction we do not sign.

**$\Delta I$ is bounded by design, because $D$ is held fixed.** Household resources, needs and composition are not equalized in any coalition of the preliminary decomposition; they remain in the residual throughout. The movable inequality the exercise can possibly reach, $\Delta I$, is correspondingly a small share of baseline inequality by construction ({{n:d2_deltaI_pct_singles_eq|.1f}} to {{n:d2_deltaI_pct_couples_uneq|.1f}} per cent), and that boundedness is a property of what the exercise holds fixed, not a finding that job opportunities are unimportant.

**The preference contribution's sign depends on the reporting scale.** $\phi_P$, the exact Shapley contribution of preferences, changes sign between the unequivalised and equivalised reporting conventions in both samples. We therefore make no directional claim about the preference contribution, only about the ordering of access against earnings, which is scale-robust.

**Single men's fit could not be established to the same standard as the other three groups.** Extensive-margin accuracy for single men fails the pre-registered numerical-adequacy gate and is withheld rather than reported at all (Section 5); the raw employment rate is matched closely ({{n:singlesmale_emp_gap_pp|.1f}} percentage points), but on the margin where this group's fit is worst, the near-full-time hours band, the record specification under-predicts by {{n:singlesmale_hours_gap_pp|.1f}} percentage points, the largest single discrepancy in either sample. This is a genuine, group-specific fit limitation, not a tail-coverage artefact of the kind reported for the sub-ten-hour cell.

**The time endowment, $T={{n:time_endowment}}$ hours a week, is a convention the model is not indifferent to.** A diagnostic re-estimation at $T=75$ and $T=90$, holding the rest of the certified protocol fixed, moves the criterion materially in both directions and changes which coordinates are interior: at $T=90$ a second leisure-curvature coefficient joins the boundary that is interior at $T={{n:time_endowment}}$. $T={{n:time_endowment}}$ is therefore a maintained convention, not a free normalization the results are invariant to, and it has not itself been estimated or justified.

**Individual-level predictive diagnostics raise possible excess stochastic dispersion in some groups; the group-level classification is not used as a headline result.** The pre-registered composite decision rule flags couples (both sexes) and single men, on the weighted statistics, with a misspecification-evidence verdict against the model's own simulated variation, rather than a mechanical consequence of conditioning on outcomes. Single women's verdict is inconclusive, but not because they fail the extensive-margin numerical-adequacy gate reported above -- they clear that gate on both weighted and unweighted statistics. Their inconclusive verdict traces instead to a different set of statistics (the prediction-conditioned regression-to-the-mean check and several hard-classification and reliability statistics) failing their own, separately applied adequacy gate. Two of the four group verdicts are themselves sensitive to the weighting convention -- coupled men's underlying gate status and single men's misspecification verdict do not survive switching from weighted to unweighted statistics. This is diagnostic evidence from a composite decision rule, not a single statistic, it is sensitive to unsupported finite-panel regions being floored rather than excluded, and the underlying verdicts remain open pending further review; we report it as an open question about the model's implied stochasticity, not as an established fact about it.

## What is not established

The preliminary decomposition is an accounting of a structural model under declared operators. It is not a causal analysis. No regional, educational or occupational effect reported here is identified as a causal effect, and the exhaustiveness of the allocation validates the accounting for the declared game, not the identification of the model or the normative content of the operators.

Section 5's decomposition is bounded and preliminary in three specific ways, stated together here. It holds household resources, needs and composition fixed rather than decomposing them, so no share is attributed to that circumstance and the movable inequality it reaches is correspondingly small. It reuses the model's already-priced estimation panel to simulate counterfactual attainment, which anchors that attainment toward the observed outcome to a small, checked degree, rather than resolving the counterfactual-attainment estimand the paper's final decomposition architecture requires. And its uncertainty is reported as a Monte Carlo simulation range and an independent second-seed check, not as a parameter-uncertainty interval propagated from the estimation covariance. None of the three is a defect in what is reported; together they are why it is reported as preliminary rather than as the paper's decomposition result.
'''

# =========================================================================== #
CONCLUSION = r'''
Observed hours and earnings do not say whether a household chose its position or settled for it, and that ambiguity is not a nuisance for welfare measurement: it is the substance of it. This paper takes the ambiguity seriously in both halves of the problem. On the behavioural side it estimates a model in which the jobs a household can reach and the way it ranks them are identified jointly, with every alternative priced through the tax-benefit system. On the normative side it evaluates well-being with a reference that keeps each household's own preferences and own reachable jobs and removes variation in pay from the reference bundles.

A complete decomposition of the resulting inequality into preferences and circumstances awaits a counterfactual-attainment estimand still under design. Ahead of it, a bounded preliminary exercise asks how a small, structurally-fixed share of measured inequality divides between preferences, local labour-market access and earning opportunities, holding resources, needs and composition fixed. For both French single-adult and couple households, earning opportunities dominate local labour-market access within that movable share, at every scale reported; the preference contribution's sign is not robust between reporting conventions, so no directional claim is made about it.

Three limits should travel with that reading. The quantitative opportunity decomposition is preliminary and work in progress, bounded by construction, not the paper's final decomposition. The allocation is exhaustive for the declared three-player game, which validates the accounting and not the identification or the ethics of the operators. And several questions named in Section 6 -- about the observation rule, about the model's own scope, and about where it under- or over-predicts -- remain genuinely open, unrelated to the decomposition itself. What the exercise offers is not a causal account of why opportunities differ, and not yet a complete attribution of measured inequality, but a disciplined, preliminary statement of which of two circumstance channels dominates, once preferences and a structural model are made explicit and the reference is stated.
'''

# =========================================================================== #
APP_COEF = r'''
The tables below report only coordinates estimated on the reported sample. **Maintained restrictions.** Singles: `theta_c_singles = 0`; the couples preference block (`beta_l0_m`, `beta_l_age_m`, `beta_l_age2_m`, `beta_l0_f`, `beta_l_age_f`, `beta_l_age2_f`, `beta_l_nkids_f`, `theta_l_f`) does not enter the singles likelihood; and `beta_E_y2015` and `beta_E_y2017` are absent because the 2015 and 2017 data are not used. Couples: `theta_c = 0`, the male children leisure effect is structurally zero, and the direct cross-leisure term is fixed at zero. These are restrictions, not estimates.

One single-adult coordinate, the female age-square term, is at its box endpoint. Under the active-set convention its interval is not reported, the interior curvature is computed after removing it, and the parameter draws used for the welfare intervals hold it at its estimate.

{{table:fullsingles}}

{{table:fullcouples}}
'''

APP_INDEX = r'''
The preliminary decomposition of Section 5 uses the Gini index only, on a weighted distribution of strictly positive money-metric levels with mean $\mu$: $\mathcal I=\frac{1}{2\mu}\,\mathbb{E}\lvert W-\tilde W\rvert$, for $W,\tilde W$ independent draws from the distribution. Extending the exercise to further indices, as an earlier, retired version of this decomposition did across six indices, is future work and is not reported here.

The exact Shapley value on the three-player game $v(S)=I_\varnothing-I_S$, $S\subseteq\{P,A,B\}$, allocates to factor $k$ the average of its marginal contribution $v(S\cup\{k\})-v(S)$ over all $3!=6$ orderings in which the three factors can be introduced:

$$
C_k=\frac{1}{6}\sum_{\pi}\big[v(S_\pi(k)\cup\{k\})-v(S_\pi(k))\big],
$$

where $S_\pi(k)$ is the set of factors preceding $k$ in ordering $\pi$. With three players this has a closed form and requires no grouping into unions, unlike the Owen extension for the additional operator an earlier, retired version of this decomposition used. Contributions are signed and are never renormalised to sum to one hundred by construction: they sum to $\Delta I=I_\varnothing-I_{\{P,A,B\}}$ because the game closes, and the closure is verified.
'''

APP_PROVENANCE = r'''
**Data.** French EU-SILC, accessed through Eurostat's harmonised release, with {{n:collection_year}} survey collection and a {{n:income_year}} income reference year. The harmonised survey is transformed into an input file for EUROMOD [@sutherlandfigari2013], which applies the French {{n:policy_year}} policy system. Regional labour-market conditions come from the Eurostat regional labour-force series. Access to EU-SILC microdata is granted by Eurostat under its research-access conditions and the data cannot be redistributed with this document.

**Sample.** {{n:n_singles}} single-adult and {{n:n_couples}} couple households, constructed by the screens of Section 2.

**Estimator and inference.** Conditional likelihood over {{n:n_draws}} sampled alternatives per household plus the observed choice, with an out-of-fold proposal correction; cluster-robust standard errors on the household. Optimization is checked by five starts under two polishing contracts and curvature by exact Hessian eigenvalues.

**Welfare computation.** A common integration panel of {{n:n_nodes}} nodes per household, evaluated under all sixteen coalition states. Integration error is measured by {{n:n_scrambles}} randomized quasi-Monte Carlo scrambles; parameter uncertainty by {{n:cr1_draws}} draws from the cluster-robust covariance rebuilt from the Hessian and the household scores, holding maintained restrictions and bound-active coordinates at their values. The two are reported separately and are never combined into one band.

**Software.** Python with JAX ({{n:installed_jax}}) for automatic differentiation, and the EUROMOD connector ({{n:installed_euromod}}).

**Replication.** Code and derived, non-confidential intermediate artefacts will be made available in a public repository on publication. Confidential microdata remain in their permitted environment, so the replication package reproduces every step conditional on authorised access to EU-SILC.
'''

HISTORY = r'''
This section records how the reported specifications and results came to be what they are. It is here so that the argument above does not have to carry it, and so that a reader comparing this version with an earlier one can see what changed and why. Nothing in it is a competing model.

**The consumption specification.** Earlier drafts reported a specification in which the consumption coefficient was fixed at one as a numeraire, and one in which the single-adult consumption curvature was estimated at $\theta_c\approx0.168$. Neither is the reported model. The current specification fixes the shock scale, fixes the consumption curvature at exactly zero, and estimates the consumption weight instead. That change improves the criterion by {{n:gain_singles|.3f}} log-points for single adults and {{n:gain_couples|.3f}} for couples, and it changes how a given non-consumption advantage converts into the money metric: under the closed form of Section 4, that advantage now enters divided by the estimated $\beta_c$ rather than by the fixed numeraire it previously used. Every welfare quantity computed under the earlier convention is superseded, and the corresponding figures were regenerated rather than relabelled.

**The sample.** The predecessor frames contained 1,555 single-adult and 2,275 couple households. Twelve single-adult and fifty-two couple households were removed when the hours support and the occupation mapping were applied to the observed rows, and three further single-adult households were removed because their own observed job prices to non-positive disposable consumption. The current descriptive tables are computed on the resulting {{n:n_singles}} and {{n:n_couples}} households, not on the predecessor frames, and the funnel in Section 2 ends where the estimation begins.

**The disposable-income convention.** Single-adult disposable income was previously aggregated over the decider only; it is now aggregated over all resident household members, which is the convention the couples application always used. The two applications are now on the same accounting convention.

**The decomposition result.** The decomposition reported in this document has been rewritten twice. An early draft reported household endowments and needs as the largest component for single adults, and a one-factor figure of about seventy-seven per cent; both were withdrawn. A subsequent draft reported a four-factor preferences/access/earnings/resources-and-needs decomposition across six inequality indices, with a grouped Shapley--Owen--Shorrocks allocation; that entire apparatus is now also withdrawn, having been found by a later lineage audit to rest on a generation of run artifacts that an earlier ruling had already retired, reproduced here as a matter of record rather than as a competing result: those numbers are no longer stated as current anywhere in this document, and the retired artifacts themselves are named in the audit record, not here. Section 5 now reports a bounded, explicitly preliminary three-factor exercise (preferences, local labour-market access, earning opportunities, with resources, needs and composition held fixed), sourced from an independent replication run, separate from the retired generation, and reported with Monte Carlo simulation ranges and a second-seed check rather than parameter-uncertainty intervals, ahead of the paper's final decomposition architecture, which awaits a counterfactual-attainment estimand still under design.

**The bridge between references, retired.** An earlier draft compared the flat-consumption reference against a second, non-work-bundle reference, both computed from the ex-ante inclusive-value functional ($J_{i,S}$, $H_{i,S}$, integrated over the estimated opportunity density). That comparison went through two states -- a wrong sign for couples, later a premise audit that corrected the normalization of the opportunity kernel -- before the measure-correspondence audit classified the underlying functional itself as a different object from the paper's literal measure and Deputy ruling R2 retired it. The bridge is not reported in this document in any form; both its earlier, incorrect version and its later, corrected version relied on a construction that is no longer the paper's welfare measure.

**The relative-index companion measure and the pay-neutrality diagnostic, removed.** An earlier draft reported bracketing counts for a third, resource-and-pay reference and a numerical wage-density-invariance residual, both cited to a since-retired welfare-record artifact. On repointing the citations, the relative-index measure did not survive: the accepted measure-correspondence audit classifies it as a different object from its theory definition, not reusable for a literal computation and not required by any current ruling, so it is removed rather than recited elsewhere. The pay-neutrality claim survives, more strongly than before: under the accepted reference construction (Mapping F, Deputy ruling R1) the home reference carries no opportunity-density, proposal, shock or intensity argument at all, an exact property of the construction rather than a numerical residual, so Section 4 states it without a magnitude.

**The consumption normalizer.** Three values of $\lambda_c$ were in circulation because different panels recomputed it over their own rows. Under exact log consumption the constant is alternative-invariant and cancels from every choice probability; it does not enter the accepted $W^1_F$ welfare measure at all, so no welfare result is affected by which value is used. The paper now reports one constant per population, for the choice-probability role it actually plays.
'''

REPORT_NOTEBOOK = r'''
The project keeps one canonical research notebook, `JMP_research_lab.ipynb`, in the estimation repository. Two things about it need saying precisely, because both have been overstated before.

**It is a replay and refit interface, not a source-to-results interface.** What it exposes, by calling the production functions rather than reimplementing them: loading a frozen engine-ready frame; evaluating the criterion and its gradient at a given parameter vector; refitting from a chosen start; rebuilding the cluster-robust covariance from the Hessian and the household scores; computing population predictions by direct integration; evaluating the money metric and the coalition states on a saved integration panel; and regenerating the figures from their saved plotted-number files. What it does *not* do: reconstruct the raw survey input from source, generate a new set of alternatives, or price alternatives through the tax-benefit model. Those three stages run as separate authorised jobs against the microdata environment and are not callable from the notebook. So the notebook reproduces every stage from the frozen priced frame onwards, and describing it as end-to-end would be inaccurate.

**Its machinery is current; the artifacts it is pointed at are not.** The utility construction in the notebook is specification-driven: it reads the consumption coefficient from the specification and carries an estimated one wherever the specification leaves it free, so nothing in the code assumes the superseded numeraire. But the frames, specification and result files it currently loads are the generation that preceded the specifications of record reported here. Re-pointing it is a mechanical change and re-running it is not, and a notebook that had been re-pointed but not re-run would be worse than one that is honestly labelled. It is therefore left as it stands, and re-binding it to the current specifications and welfare record is the one capability gap this document reports.
'''

# =========================================================================== #
SECTIONS = [
    {'key': 'intro', 'title': 'Introduction', 'body': INTRO},
    {'key': 'data', 'title': 'Data', 'body': DATA},
    {'key': 'model', 'title': 'A latent-jobs model of household labour supply',
     'body': MODEL},
    {'key': 'welfare',
     'title': 'Money-metric well-being and structural inequality decomposition',
     'body': WELFARE},
    {'key': 'results', 'title': 'Empirical results', 'body': RESULTS},
    {'key': 'sensitivity', 'title': 'Sensitivity and limitations',
     'body': SENSITIVITY},
    {'key': 'conclusion', 'title': 'Conclusion', 'body': CONCLUSION},
    {'key': 'appcoef', 'title': 'Appendix A. The estimated parameter vectors',
     'body': APP_COEF, 'appendix': True},
    {'key': 'appindex',
     'title': 'Appendix B. Inequality indices and the allocation rule',
     'body': APP_INDEX, 'appendix': True},
    {'key': 'appprov', 'title': 'Appendix C. Data, software and replication',
     'body': APP_PROVENANCE, 'appendix': True},
    {'key': 'notebook', 'title': 'The research notebook',
     'body': REPORT_NOTEBOOK, 'paper': False, 'collapse': True},
    {'key': 'history', 'title': 'Scientific history of this result',
     'body': HISTORY, 'appendix': True, 'collapse': True},
]

# =========================================================================== #
QA = [
 ('What is the question, in one sentence?',
  r'''How much well-being inequality is associated with unequal job opportunities once preferences and household circumstances are made explicit? See the discussion notebook, Section 0, Scope.'''),
 ('What is a latent job?',
  r'''An employment state, occupation, hours arrangement and wage, priced through the tax-benefit system. Availability and preferences jointly determine choices. See the discussion notebook, Section 4, The estimated model.'''),
 ('Which dates does the data cover?',
  r'''EU-SILC collection year {{n:collection_year}}, income reference year {{n:income_year}}, and EUROMOD policy year {{n:policy_year}}. See the report Data section and its sample-funnel table.'''),
 ('What is the first figure showing?',
  r'''The deterministic W1 construction adapted from the companion theory paper, Haydar and Maniquet (2026). See the figure Own-set equal-consumption equivalents. Section 4 states the empirical implementation on the current estimated model, Mapping F, and derives its closed form.'''),
 ('Does log consumption make welfare an arithmetic mean?',
  r'''The accepted measure is not an arithmetic mean of anything: $W^1_{i,F}=C_i^{\mathrm{obs}}\exp[(L_i(j_i^{\mathrm{obs}})-L_i(o))/\beta_c]$ evaluates a single observed job against a single home state, with no averaging or integration over jobs. $\beta_c$ sets the rate at which the non-consumption gap between those two states converts into a proportional adjustment of the household's own observed consumption. The estimated values are {{n:beta_c_singles|.4f}} and {{n:beta_c_couples|.4f}}. See Section 4.'''),
 ('Does the normalizer $\\lambda_c$ affect welfare?',
  r'''No. It cancels under exact log consumption from every choice probability, but it does not appear in the accepted $W^1_F$ closed form at all -- not as a cancelling term, simply absent. See Section 4.'''),
 ('Does the proposal enter welfare, or only estimation?',
  r'''Only estimation. The proposal density $q$ corrects the sampled-alternative choice probabilities; it carries no economic content there either. It does not enter the accepted $W^1_F$ welfare measure at all: only the household's own observed job and its home state enter the closed form, and neither involves a proposal correction. See Section 4.'''),
 ('What happens to simulated non-positive consumption?',
  r'''A one-euro floor is applied before utility evaluation, for the sampled alternatives used in estimation: 22,597 singles and 59,821 couples node-evaluations. None of those alternatives enters the welfare measure, which evaluates only each household's own observed job and its home state, both already screened to strictly positive consumption. See Section 2 and Section 4.'''),
 ('Why is predicted mass below ten hours zero?',
  r'''The panel contains no draw in $(5,10)$ despite positive structural and proposal mass; its expected count is 0.249. This tail-coverage limitation produces a genuine fit error. See the observed-versus-model fit table in the discussion notebook, Section 6.'''),
 ('Do the hours partitions close?',
  r'''Yes. The long-hours bin includes 70, and observed singles partitions close separately by sex. See the hours-fit table in the discussion notebook, Section 6.'''),
 ('Is the measure independent of pay?',
  r'''The reference is directly pay-neutral: the home state carries no opportunity-density, proposal, shock or intensity argument, so none of them enters the reference at all. Earning opportunities nevertheless change attained welfare, because they change what the household attains, not the reference it is compared against. See Section 4, What the reference does and does not do to pay.'''),
 ('What do the three preliminary operators equalize, and why is a fourth one absent?',
  r'''Preferences, local labour-market access and earning opportunities, each through its named pathway with coefficients fixed. Household resources, needs and composition are held fixed rather than equalized: they are not a fourth operator in this bounded exercise, and no share is attributed to them. See Section 5.'''),
 ('Why an exact Shapley value, and not the grouped Owen rule an earlier draft used?',
  r'''With three players the exact Shapley value has a closed form over $3!=6$ orderings and needs no grouping into a priori unions. The Owen rule an earlier, now-withdrawn draft used was needed only because that draft had an additional operator, for resources and needs, to group against preferences. See Appendix B.'''),
 ('Is the movable share $\\Delta I$ small because job opportunities do not matter?',
  r'''No. It is small because household resources, needs and composition are held fixed in every coalition of this bounded exercise, and that fixed component accounts for {{n:d2_varshare_logC_couples|.0f}} to {{n:d2_varshare_logC_singles|.0f}} per cent of the variance of log well-being. See Section 5.'''),
 ('Which ordering is robust across unequivalised and equivalised reporting?',
  r'''Earning opportunities dominate local labour-market access for both single adults and couples, at both scales. The preference contribution's sign is not robust between the two scales in either sample, so no directional claim is made about it. See Section 5.'''),
 ('How uncertain are the preliminary shares?',
  r'''Two ways, never merged into a confidence interval: a Monte Carlo range across 1,000 simulation replications, and an independent check under a second simulation seed. A parameter-uncertainty interval propagated from the estimation covariance is not yet computed for this exercise. See Section 5.'''),
 ('What does exhaustiveness establish here?',
  r'''The contributions of $P$, $A$, $B$ and the residual close to the baseline inequality to machine precision; this checks accounting for the declared three-player game, not identification of the model or resolution of the counterfactual-attainment question the game is bounded around. See Section 5.'''),
 ('Can welfare levels be compared across the two populations?',
  r'''Each population has its own preference and opportunity reference. Results are compared within population, with raw and equivalized conventions separate. See the welfare state-level table in the discussion notebook, Section 7.'''),
 ('Is a nested subdivision of resources and needs available, the way an earlier draft reported one?',
  r'''No. Resources, needs and composition are held fixed rather than decomposed in this bounded preliminary exercise, so there is nothing to subdivide. An earlier, now-withdrawn draft's nested resources-versus-composition split was part of the retired four-factor architecture and is not carried forward.'''),
 ('What happened to the earlier decomposition numbers entirely?',
  r'''They are withdrawn, not corrected: the entire four-factor preferences/access/earnings/resources-and-needs architecture they were computed on traced to artifacts retired by the DECOMP-PRESEMINAR-1 ruling. See the Scientific history section for the full record and Section 5 for what is reported in its place.'''),
 ('What remains unresolved?',
  r'''Outcome-based sample selection and the construction of the labelled-slot sampling law remain open econometric items, unrelated to the decomposition. Separately, the decomposition itself remains bounded pending a counterfactual-attainment estimand under design; Section 5 and Section 6 state exactly what that bound means for the reported shares.'''),
 ('Is this causal?',
  r'''The decomposition is structural accounting under declared operators; it does not identify causal regional, educational or occupational effects. See the discussion notebook, Section 9, What is robust and what is not.'''),
 ('Can the notebooks reproduce everything?',
  r'''The discussion notebook executes checks and renders current results. The research lab replays from priced inputs, with an artifact-generation caveat; raw-data preparation and pricing are separate. See the report's The research notebook section and the discussion notebook, Section 0.'''),
]
