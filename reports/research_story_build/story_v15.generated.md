# Unequal Job Opportunities and Well-Being Inequality: A Latent-Jobs Structural Decomposition

Hisham Haydar · University of Luxembourg and LISER

Build date: 15 September 2026.

## Abstract

Observed income inequality is not welfare inequality: households
differ in what they prefer and in the jobs they can reach, and observed
labour-supply choices mix the two. We estimate a random-utility,
random-opportunity model of job choice on French EU-SILC data priced through
EUROMOD, translate it into money-metric well-being under two perspectives, and
allocate counterfactual changes in the Gini with an exact Shapley rule. The
current decomposition equalises preferences, geographic/temporal job access and
systematic earning opportunities while holding household resources, needs and
composition fixed. When welfare evaluates the bundle a household actually
attains, access and earning opportunities together account for
1.9–6.7% of baseline
inequality and earning opportunities matter more than access. When welfare
evaluates the whole opportunity prospect, they account for
7.9–21.3%, and for
single-adult households access becomes about three times as important as earning
opportunities; couples show no such reversal. The importance assigned to
different labour-market inequalities therefore depends on whether welfare
evaluates the realised outcome or the opportunity prospect itself. These are
restricted structural accounting shares: they are not causal estimates and do
not estimate the total share of well-being inequality caused by unequal job
opportunities.

*Discussion draft. The attained-bundle counterfactual integration remains preliminary; the ex-ante calculation has passed its numerical checks. Both are restricted structural accounting exercises, not causal decompositions, and neither welfare perspective is designated as primary.*


# 1. Why welfare inequality is not income inequality


Two people can work the same hours for the same hourly pay and be very
differently placed. One chose that job from several that were open; the other
took the only offer available. Their incomes are identical and their
circumstances are not. This paper is about what that difference does to the
measurement of well-being inequality.

## The logical chain

**Observed income inequality is not necessarily welfare inequality.**
Households differ in their preferences over consumption and leisure, in the
constraints that shape their budgets and needs, and in the job prospects they
face. Low earnings can describe someone who values leisure and chose short
hours, someone who cannot obtain a well-paid job, or someone whose household
resources make a different arrangement affordable. A distribution of income
records outcomes with these explanations already mixed in.

**Observed labour-supply choices do not identify preferences alone.** A
household is seen in a job because it wanted that job *and* because that job
was available. If part-time work is rare in a local labour market, few people
will be observed working part time even if many would like to. Choice
frequencies therefore reflect the density of opportunities as well as tastes,
and a model that gives everyone the same set of jobs must read every difference
in behaviour as a difference in preferences.

**Therefore four steps are needed, each answering a question the previous one
leaves open.**

1. *A structural labour-supply model that separates preferences from
   opportunities.* Without it there is nothing to attribute: the econometrician
   cannot tell whether a household works little because it prefers to or
   because it cannot find more work. Section 2 sets out that model.
2. *A money-metric welfare mapping.* Estimated utility is not an interpersonal
   welfare index, because preferences differ. Comparing households requires a
   common monetary yardstick with an explicit reference. Section 3 constructs
   two, each answering a different welfare question.
3. *Structural equalisation counterfactuals.* To ask how much inequality is
   associated with a source of heterogeneity, the source is replaced by a
   common reference inside the model, welfare is recomputed and inequality is
   measured again. Section 4 defines those counterfactuals.
4. *An order-independent decomposition.* The sources interact, so the effect
   of equalising one depends on which others have already been equalised. The
   Shapley value averages over every order. Section 4 applies it.

## Why this matters

A distributional analysis based only on realised disposable income can miss
heterogeneity in the labour-market prospects that households face. Two
households with the same income may differ in how many jobs they can reach, in
the hours those jobs offer and in what they pay. Whether that heterogeneity
should count in a welfare comparison, and how much inequality is associated
with it, are empirical and normative questions that an income distribution
cannot answer.

The paper asks whether welfare inequality is associated primarily with
systematic preferences, with geographic and temporal job access, or with
systematic earning opportunities. The answer can identify which margins deserve
explicit attention in later policy analysis. It does not show that an
opportunity policy is more effective or cheaper than redistribution: that
comparison requires a policy experiment and cost estimates that are not part of
this paper.

## What the paper does and finds

The empirical strategy joins a random-utility model to a random-opportunity
model. Jobs are packages of employment, occupation, weekly hours and hourly
wages; couples choose two packages under a shared household budget. Every
package is priced through the French tax-benefit system. The model separates
systematic variation in the value of consumption and leisure from systematic
variation in employment access, hours, occupations and wage offers, subject to
explicit maintained assumptions.

Well-being is then measured from two perspectives. The attained-bundle
perspective (ATT) asks how well off a household is in the bundle it actually
attains. The ex-ante perspective (EA) asks how valuable the distribution of job
prospects it faces is. The two measures answer different welfare questions. The attained-bundle measure evaluates the bundle eventually reached against a common non-employment reference. The ex-ante measure evaluates the household's entire distribution of potential job outcomes against a reference prospect that preserves the same opportunity environment while equalising consumption across jobs.

The current decomposition equalises preferences, geographic/temporal job access and systematic earning opportunities while holding household resources, needs and composition fixed. Interactions are allocated with an exact Shapley rule,
separately for each welfare perspective and for single-adult and couple
households. A fourth pathway for household resources, needs and composition is
a planned extension, not part of the present results.

The central result is a contrast. Under attained-bundle welfare, earning
opportunities matter more than the coarse access channel, for both household
types and on both reporting scales. Under ex-ante welfare, access becomes much
more important for single-adult households—about three times earning
opportunities. Couples show no such reversal: earning opportunities remain
larger than access. The importance assigned to different labour-market inequalities depends on whether welfare evaluates the realised outcome or the opportunity prospect itself. The contrast is not a
disagreement to be resolved by choosing a winner; it shows what each welfare
question makes visible, and neither perspective is designated primary here.

## Relation to existing work

 Every ingredient here has antecedents, and the contribution is the combination and the empirical answer, not any one step.

Modelling labour supply as choice among latent jobs, with preferences and opportunity components jointly estimated under maintained functional-form and exclusion restrictions, is due to @aaberge1995 and @aaberge1999, developed by @dagsvikstrom2006 and @dagsvikjia2016, surveyed by @aaberge2018, and set out for applied work by @capeau2016. We inherit that framework, including its distinction between the intensity of an offer and the probability of a choice, and its reliance on excluded opportunity shifters to separate components that choices alone do not separate. @capeau2016 also supply two of the identifying restrictions we maintain: the wage-offer distribution is independent of offered hours, and a local unemployment measure shifts availability while being excluded from preferences. Their Belgian application already covers single women, single men and couples, so covering both household types is not itself a contribution.

Combining such a model with a monetary welfare evaluation is also established. @aaberge1995 translate attained utility into an equivalent income against a stated reference household, choice set and tax system, and @aaberge2004 evaluate reforms with joint household choice and restricted hours. @jiathoresen2021 make the case for the job-choice model in exactly this role and report a distribution of compensating variation for a Norwegian reform, and @jacquet2026 compare a standard compensating variation with one computed after replacing preference characteristics by reference values. All four evaluate a *change* between policy regimes. Our object is a cross-sectional distribution of levels under one policy system, and its attribution. A reform gain and a level have different origins and different denominators; a small preference-related reform difference would not imply a small preference share in our decomposition, and our shares do not estimate their reform gains.

The normative half draws on the literature that refuses to resolve interpersonal comparison by assuming common preferences. @fleurbaeymaniquet2006, @fleurbaeymaniquet2017 and @fleurbaeymaniquet2018 set out how a reference bundle encodes a position on compensation and responsibility; @decosterhaan2015 and @bargain2013 show empirically how much a welfare ordering moves with that choice. Their references fix a wage or an unearned-income intercept and maximize over a deterministic budget set. Here the attained-bundle perspective uses the universally available non-employment state, while the ex-ante perspective fixes consumption across the alternatives of an estimated job prospect and integrates. The two references answer different questions, which is why both are reported without designating either as primary.

The closest decomposition precedents are two. @muehlhan2023 combines a structural labour-supply model with involuntary-unemployment restrictions and a Shapley attribution, decomposing the change in German household *income* inequality into temporal factors and binary restrictions. @creedyherault2011, in the section that constructs money-metric distributions under alternative policy and population states, decompose a change in inequality and social welfare by averaging over the two orders in which policy and population can be changed; theirs is the closest money-metric welfare-inequality decomposition we know. Both are decompositions of a *change* between two situations, with policy, population or temporal factors as the factors. Ours is a decomposition of a cross-sectional *level* of well-being inequality, with the factors defined as structural operators inside an estimated job-choice model: what a household prefers, which jobs it can reach and what those jobs pay, with its budget, needs and composition held fixed. The wider behavioural-simulation decomposition tradition, @bargain2012 and @jessen2019, decomposes income changes in the same spirit.

The allocation rule is inherited outright. @shorrocks1982 states the accounting requirements a decomposition should satisfy; @shorrocks2013 places the Shapley value at the centre of distributional decomposition; @sastretrannoy2002 documents how much the answer can depend on how the exercise is set up. The three-operator exercise of Section 4 needs no grouping and uses the plain Shapley value on a three-player game. We claim no new allocation principle. Complete recomputation of every coalition, rather than a linear approximation, likewise has precedents and is better described as methodological discipline than as a contribution.

What is new, to our knowledge, is the conjunction: a random-utility random-opportunity model of job choice, two money-metric perspectives built on explicit indifference conditions, and a bounded, preliminary structural game over systematic utility heterogeneity, coarse geographic/temporal access heterogeneity and earning opportunities, with complete recomputation of welfare and inequality under every coalition. The application-specific methodological contribution is the game and its counterfactual operators, applied identically to both welfare perspectives. The cooperative-game allocation rule is inherited.


The contribution is therefore the conjunction of four elements: household-
specific latent job opportunities, a tax-benefit-consistent budget for every
work arrangement, explicit money-metric comparisons under two welfare
perspectives, and a complete interaction-aware accounting across the declared
pathways.

## Roadmap

Section 2 presents the latent-jobs model and a matched-household illustration
of what unequal opportunity means inside it. Section 3 turns choices into
well-being under the two perspectives. Section 4 defines the counterfactual
inequality object and the Shapley allocation. Section 5 reports estimates, fit,
well-being and both decompositions. Section 6 collects what remains
preliminary. Implementation, numerical verification and provenance are in the
appendix.


# 2. How the latent-jobs model separates preferences from opportunities


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

The third kind is support. An employed decider's observed hours must lie in the closed interval $[5, 70]$ hours per week and the delivered hourly wage in $[2, 590]$ euros per hour, because those are the boundaries of the supports the opportunity densities are defined on. An observed occupation must map into the four modelled groups; ISCO 0, the armed forces, does not, and the resulting exclusion is *unsupported* occupation, not missing occupation. Three single-adult households whose own observed job prices to non-positive disposable consumption are removed, because the log-consumption term is undefined at their observed choice; non-positive *simulated* alternatives receive a one-euro consumption floor before utility is evaluated. Those are sampled alternatives entering the estimated choice likelihood. They do not enter the welfare measure of Section 3, which evaluates only each household's own observed job and its home state, both already screened to strictly positive consumption.


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



### Observed raw labour-force status

The structural model has one non-work alternative, so unemployment and
inactivity are the same state inside it. The data distinguish them. The table
recovers each person's raw labour-force status from the person-level survey
file, including for spouses, whose status in the household design file records
only employed or not employed.


Table: Observed raw labour-force status, weighted shares with unweighted counts in parentheses, by sex and household type, on the final estimation samples. Spouses' raw status is recovered from the person-level survey file. The structural model maps both unemployment and inactivity to its single non-work alternative.

|Group|Employee (LES 3)|Unemployed (LES 5)|Inactive (LES 7)|N|
|---|---|---|---|---|
|Single men|88.0% (n=607)|11.4% (n=89)|0.6% (n=7)|703|
|Single women|86.4% (n=729)|13.2% (n=101)|0.4% (n=7)|837|
|Men in couples|92.3% (n=2057)|7.5% (n=155)|0.2% (n=11)|2,223|
|Women in couples|89.8% (n=2016)|8.9% (n=179)|1.3% (n=28)|2,223|



Most non-working adults in both samples are unemployed rather than inactive,
which is consistent with the sample screens that remove students and pension
recipients. Because the model maps both states to non-employment, nothing in
the estimates or welfare measures distinguishes a household that is searching
from one that is out of the labour force.

## The household budget

For a given work arrangement the tax-benefit model is given the implied gross labour inputs, weekly hours, hourly wage, and earnings split at the thirty-five hour threshold, together with the household's non-labour inputs and roster, and returns disposable income. Only deciders receive counterfactual overrides; other members keep their baseline values. Disposable income is summed over all resident members of the household.


![Weighted distributions on the estimation samples: simulated disposable income at the observed job, children under twenty, the incidence of non-labour budget inputs by family, and urbanisation. Panel (a) is a tax-benefit output evaluated at the observed choice; panel (c) reports inputs to that calculation. The two are never added, and stocks are never summed with monthly flows.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v5/figV09_resources_panel.png){width=95%}


Panel (c) of the figure reports the *incidence* of non-labour budget inputs by family, not a cash total. Some of these are stocks, some are annual flows and some are monthly; they are inputs to the tax-benefit calculation and are not added together into one income concept. The pension family is empty by construction, because pension receipt is a sample screen. Panel (a) reports the tax-benefit *output* at the observed job, which is an object of a different kind and is never added to panel (c).

Local labour-market conditions enter through a group unemployment measure, a population-weighted exposure index for the decider's region and age-education cell, stored as a fraction and entering the employment index multiplied by 10. Regional and urbanisation variation supports the access specification conditional on the exclusion restriction and the functional form; it does not by itself identify access, and no causal effect of geography is claimed anywhere in this paper.



## Jobs as packages

A job is a package $j$: an employment state $e\in\{0,1\}$ and, when employed,
an occupation $k\in\{1,\dots,4\}$, weekly hours
$h\in[5,70]$ and an hourly wage
$w\in[2,590]$. The base measure $\nu$ places mass one on
the single non-employment state $o$ and, on the employed part, counting measure
over occupations with Lebesgue measure over hours and wages. A single adult
chooses one package; a couple chooses one pair of packages under a shared
budget. Every package is priced: $C_i(j)$ is the household's monthly disposable
consumption at $j$ after taxes and transfers.

## A. Systematic utility

**Why.** A labour-supply model must say what a household gains from a job
(consumption) and what it gives up (leisure). Welfare comparisons later need
the two to be separable, because consumption is observable in euros while the
value of leisure is not.

**Object.** For a single adult of sex group $g$ the systematic utility of
package $j$ is

$$
v_i(j)=L_i(j)+\beta_c\log\!\left(\frac{C_i(j)}{\lambda_c}\right),
\qquad
L_i(j)=\beta_{\ell}^{g}(\mathbf x_i)\,
\mathcal B\!\left(\tilde\ell_i(j);\theta_{\ell}^{g}\right),
$$

$$
\beta_{\ell}^{g}(\mathbf x_i)=\beta_{\ell 0}^{g}+\beta_{\ell a}^{g}a_i
+\beta_{\ell a^{2}}^{g}a_i^{2}+\mathbb 1\{g=\text{women}\}\,\beta_{\ell k}^{g}k_i .
$$

**Interpretation.** $L_i(j)$ is the complete non-consumption value of the
package: normalised leisure $\tilde\ell_i(j)=(80-h)/10$
passed through the Box-Cox transform $\mathcal B(z;\theta)=(z^{\theta}-1)/\theta$,
with $\mathcal B(z;0)=\log z$. The household-specific weight
$\beta_{\ell}^{g}(\mathbf x_i)$ varies with centred age $a_i$ and, for women, with
the number of children $k_i$; $\theta_{\ell}^{g}$ governs curvature. The child
term is a reduced-form behavioural and time-constraint shifter, not pure
taste. $\beta_c$ is the weight on log consumption and is estimated, not fixed.
$\lambda_c$ is a units convention that cancels from every choice probability.
For a couple, $L_i(j)$ is the sum of the two spouses' leisure terms, with no
direct cross-leisure term, and $C_i(j)$ is the household's joint consumption.
The random-utility shock is i.i.d. type-I extreme value with unit scale, so
utility is measured in the natural unit of that scale.

**Empirical use.** $v_i(j)$ is the preference half of the choice law below.
Its split into $L_i$ and $\beta_c\log C_i$ is what later turns a utility
difference into a proportional consumption adjustment in both welfare
measures, and its household-specific coefficients are the preference pathway
$P$ equalised in Section 4.

## B. The choice law with opportunities

**Why.** A standard random-utility model assumes every household chooses from
the same set of jobs. Then any difference in what households do has to be a
difference in what they want. If jobs are not equally available, that reading
attributes scarcity to taste.

**Object.** In the random-utility, random-opportunity model the probability
that household $i$ is observed in package $j$ is

$$
P_i(j)=\frac{\exp\{v_i(j)\}\,g_i(j)}
{\displaystyle\int\exp\{v_i(k)\}\,g_i(k)\,d\nu(k)} .
$$

**Interpretation.** $g_i(j)$ is the household's opportunity density: the
relative intensity with which package $j$ is available to it before any choice
is made. A package is chosen often when it is valued ($v_i$ high) *or* when it
is plentiful ($g_i$ high). Observed choices therefore reflect both systematic
preferences and the density of opportunities. A common-opportunity model is the
special case in which $g_i$ is the same for everyone, so that $P_i(j)$ depends
on $v_i$ alone. Rescaling $g_i$ by a household-specific constant leaves $P_i$
unchanged, which is why only the shape of the opportunity environment, not its
level, is estimated.

**Empirical use.** This law is the likelihood that is estimated. It is also the
central distinction of the paper: because $g_i$ is household-specific, the
model can attribute part of observed behaviour to reachability rather than to
taste, and both welfare perspectives inherit that separation.

## C. The structure of opportunities

**Why.** "Opportunity" is not one object. A household may face few jobs, jobs
concentrated at particular hours, a particular occupational mix, or low offered
wages. These margins have different economic meaning and must be separable to
be equalised one at a time.

**Object.** The opportunity density factorises into four blocks, switched off
on non-employment by $E_i(j)=\mathbb 1\{h>0\}$:

$$
g_i(j)=g^{E}_i\cdot\left(g^{H}_i(h)\cdot g^{\mathrm{Occ}}_i(k)\cdot
g^{W}_i(w\mid k)\right)^{E_i(j)} .
$$

**Interpretation.**
**Access**, $g^{E}_i=\exp\{\beta_E+\beta_s s_i+\sum_{r=2}^{8}\beta_r\,\mathrm{reg}_{ir}+\beta_u u_i+\beta_m m_i\}$,
is the employment mass: it moves with the local group unemployment measure
$s_i$, region and urbanisation, and survey year where it applies.
**Hours**, $g^{H}_i(h)=\exp\{\sum_b \beta_b\mathbb 1\{h\in b\}\}$, elevates five
bands over a residual set of width 29.5 hours per week;
the narrow full-time band $[33.5,36.5)$ is a density elevation over an
interval, not an atom at thirty-five hours.
**Occupation**, $g^{\mathrm{Occ}}_i(k)=\exp\{\beta^{\mathrm{occ}}_{k,g}\}$, with
group 1 as reference.
**Wage offer**, $g^{W}_i(w\mid k)$, is log-normal with location
$\mu_i(k)=\beta_{w0}+\beta_{wL}L_i+\beta_{wH}H_i+\beta_{wx}x_i+\beta_{wx^{2}}x_i^{2}+\delta_k$
in education, potential experience and occupation, dispersion $\sigma$, and is
truncated to $[2,590]$ euros per hour and renormalised on
that support.

In the preferred specification, the dimensions that vary across households are
the access shifters (local unemployment exposure, region, urbanisation and
year), the wage-offer location (education and experience), and the sex- and
household-type-specific hours and occupation blocks. The hours and occupation
blocks do not vary with other household characteristics within a group.

The decomposition pathway $A$ equalises only the access shifters: local
unemployment exposure, region, urbanisation and year. It is the estimated geographic/temporal access channel, not all job
opportunities: personal occupation access, the hours density and every other
feature of a feasible job are left as estimated. The pathway $B$ equalises the
systematic wage-offer location, not the common wage dispersion.

**Empirical use.** The factorisation defines what the equalisation operators of
Section 4 can change. It also determines how opportunities reach welfare: in
the attained-bundle perspective only through the job eventually attained, and
in the ex-ante perspective directly, as weights on the whole prospect.


## What unequal opportunity means in this model: two matched households

The equations above say that households differ in what they can reach. A pair
of estimation households makes that concrete. The pair is a teaching device:
it is not a causal comparison and it is not representative of the population.

**How the pair was chosen.** Among employed single adults, admissible pairs
share their sex, observed occupation group, model hours band and
observed-wage quintile—the things an income or employment table would show.
Among those 9,529 pairs, only those whose estimated leisure
profiles are closest (at or below the tenth percentile of leisure-profile
distance) are retained, and the pair whose estimated opportunity densities
differ most is selected. The selected pair is therefore an extreme case under a
stated rule, not a typical one. Identifiers, exact observed values, ages,
regions and local labour-market values are withheld.


![Two matched single-adult households under the accepted specification, labelled A and B. Both are employed men in the same occupation group, hours band and observed-wage quintile, with nearly identical estimated leisure profiles. Panels: (a) leisure value of hours worked relative to non-employment; (b) employment share of opportunity mass; (c) the hours density, common to all single adults; (d) occupation mass, common within sex; (e) wage-offer density given employment; (f) relative intensity of offers paying at least a given hourly wage, log scale. Model-implied quantities for a pair selected by a stated rule; not causal and not representative.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v11/fig_matched_households_v11.png){width=95%}


**Preferences are nearly identical.** Both households are men with estimated
leisure weights of 8.22 and
8.17 and a common curvature; their leisure-value
curves in panel (a) overlap. Their leisure-profile distance is
0.019, against a selection cut-off of
0.065.

**Access differs by an order of magnitude.** Household A's employment mass is
14.5 times household B's. If both were indifferent between
all jobs and not working, employment would account for
0.75 of A's opportunity mass and
0.17 of B's (panel b). The gap comes from local
unemployment exposure and region—exactly the geographic/temporal access channel
equalised by $A$ in Section 4.

**Hours and occupation opportunities are the same by construction.** In the
preferred specification the hours density is common to all single adults and
occupation mass is common within sex (panels c and d). The illustration cannot
show differences the specification does not allow.

**Earning opportunities point the other way.** Household B's wage-offer
location is 11.5 log points higher, with the same dispersion.
Its wage-offer distribution given employment therefore first-order
stochastically dominates household A's (panel e). Yet A faces more offers paying
at least $w$ at every wage below about 356 euros per hour,
which covers essentially all offer mass (panel f), because its access advantage
outweighs B's better wage location.

**What the pair teaches.** Two men who look alike in an income table and have
almost the same estimated tastes face different opportunity environments, and
neither environment is better on every margin. A has many more jobs; B's jobs
pay more. Whether A or B is better placed depends on how welfare weighs the
number of reachable jobs against what the realised job pays—the same question
that separates the two welfare perspectives in Section 3.


## Identification, in words

Choices alone do not separate a taste for leisure from a scarcity of jobs at
that number of hours. Three kinds of restriction do the work. Preferences are
smooth in hours, while the opportunity density is a step function over bands,
so a spike in observed hours at a band is read as availability rather than as
a kink in tastes. Excluded shifters enter availability and not preferences: the
local group unemployment measure and the regional and urbanisation indicators
shift access and appear nowhere in utility. And the wage-offer distribution is
independent of offered hours conditional on occupation, which separates the
wage location from the hours density. These are the restrictions of
@capeau2016 and @dagsvikjia2016, maintained here rather than tested. The
regional variation supports the access block conditional on those
restrictions; it is not a causal design, and no causal effect of geography is
claimed.

## Estimation, in words

Because the set of possible jobs is a continuum, the likelihood is evaluated on
a set of sampled alternatives for each household, every one priced through the
tax-benefit system, with a correction that makes the sample stand in for the
full opportunity environment. The sampling device is computational: it is not
an offer, an availability or an opportunity, and it enters no welfare measure.
Standard errors are cluster-robust on the household. The sampled-set
probability, the proposal design, the optimiser and the curvature diagnostics
are reported in the appendix.


# 3. From choices to well-being: outcomes versus prospects


Estimated utility is not an interpersonal monetary welfare index. Its units are
those of the taste shock, preferences differ across households, and the same
utility number means different things for different people. To compare
households, each one's situation is translated into euros through an
indifference condition: the consumption level that would leave the household
exactly as well off in an explicitly stated reference situation. The choice of
reference is the welfare question being asked. This section asks two.

The two measures answer different welfare questions. The attained-bundle measure evaluates the bundle eventually reached against a common non-employment reference. The ex-ante measure evaluates the household's entire distribution of potential job outcomes against a reference prospect that preserves the same opportunity environment while equalising consumption across jobs.

**The deterministic construction.** Both money metrics descend from a construction in the companion theory paper, drawn below before any algebra. Two individuals, each with their own preferences and their own set of jobs they are able to take, attain different bundles. For each individual, give every job in their own set the same consumption; that individual then prefers one of those jobs, and the consumption level at which that preferred job is exactly as good as the attained bundle is their money metric. The construction's point is that the two individuals' money metrics, built this way, are directly comparable even though their preferences and job sets differ. The figure is a theoretical illustration: it contains no estimated value, no household data and no result.


![Own-set equal-consumption equivalents: the theoretical construction from the companion theory paper. Two individuals, with preferences $R_i$ and $R_h$ and ability sets $A=\{j,k\}$ and $A^{\prime}=\{k,\ell\}$, attain bundles $z_i$ and $z_h$. For each individual, a common consumption level is assigned to every job in their own set; the level at which the preferred reference job becomes indifferent to the attained bundle is that individual's money metric, $W^1_i$ and $W^1_h$. The two metrics are then directly comparable. Adapted from Haydar and Maniquet (2026), work in progress. This is the deterministic construction; the estimated ex-ante measure is its extension, defined in Section 3.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v5/theory_w1.png){width=95%}


The estimated attained-bundle measure should not be read as using a rich set of reference jobs like the one drawn here. Its reference is non-employment: on the current empirical domain non-employment is the job every household prefers when all jobs pay the same, so the reference collapses to that single state. The ex-ante measure keeps the equal-consumption idea but applies it to the household's estimated opportunity prospect instead of a known set of jobs, as Perspective 2 shows.

## Perspective 1 — ATT: how well off is the household in the bundle it actually attains?

**Why.** Households end up in particular jobs. A natural welfare question
values that realised outcome, consumption and leisure together, in a common
monetary unit.

**Object.** Let $j_i^{\mathrm{obs}}$ be the observed package and $o$ the
non-employment state, which is available to every household. The
attained-bundle money metric $M_i^{\mathrm{att}}$ solves the indifference condition

$$
L_i(o)+\beta_c\log\!\left(\frac{M_i^{\mathrm{att}}}{\lambda_c}\right)
=L_i(j_i^{\mathrm{obs}})+\beta_c\log\!\left(\frac{C_i^{\mathrm{obs}}}{\lambda_c}\right),
$$

so that

$$
\boxed{
M_i^{\mathrm{att}}
=C_i^{\mathrm{obs}}
\exp\!\left\{
\frac{L_i(j_i^{\mathrm{obs}})-L_i(o)}{\beta_c}
\right\}.}
$$

**Interpretation.** $M_i^{\mathrm{att}}$ is the monthly consumption at
non-employment that would be as good as the household's actual job and actual
consumption. The reference is non-employment, which every household can reach.
The measure values the attained bundle: observed consumption, adjusted by the
leisure the job costs relative to not working, converted at the rate
$1/\beta_c$. The normaliser $\lambda_c$ cancels. Opportunity density has no
direct term in this measure conditional on the attained bundle. Opportunities
matter because they shape which job becomes $j_i^{\mathrm{obs}}$ and what it
pays; once that job is fixed, jobs not taken play no role.

The general construction evaluates the attained bundle against the job the
household would most prefer if every job paid the same consumption. On the
current empirical domain that job is non-employment for every household in both
samples, because non-employment maximises the non-consumption index. The
measure therefore coincides with the staying-home equivalent. This is a
verified property of the estimated specification, not a general theorem: with a
different leisure specification or a different reference, the two could
separate. For non-workers, $M_i^{\mathrm{att}}=C_i^{\mathrm{obs}}$; for workers
it lies below observed consumption by the value of the leisure given up.

**Empirical use.** $M_i^{\mathrm{att}}$ is computed for every household from
its own priced consumption, its estimated leisure index and $\beta_c$. Its
distribution and its counterfactual versions under the operators of Section 4
give the attained-bundle decomposition.

## Perspective 2 — EA: how valuable is the distribution of job prospects the household faces?

**Why.** The attained-bundle measure values the outcome reached. A welfare
question about opportunities may also treat the quality of the prospect itself
as welfare-relevant: a household facing many good jobs is, before any job is
realised, in a different position from one facing few, even if both end up in
similar jobs. A second perspective values that prospect directly.

**Object.** Let $\widehat g_i$ be the household's estimated opportunity density
on its job domain $\Omega_i$. The value of the actual prospect is

$$
J_i
=\int_{\Omega_i}
\exp\{L_i(j)\}
\left(\frac{C_i(j)}{\lambda_c}\right)^{\beta_c}
\widehat g_i(j)\,d\nu(j),
$$

and the value of a reference prospect with the same opportunities and the same
preferences, but the same consumption $m$ at every job, is
$(m/\lambda_c)^{\beta_c}H_i$ with

$$
H_i
=\int_{\Omega_i}\exp\{L_i(j)\}\,\widehat g_i(j)\,d\nu(j).
$$

The ex-ante money metric $M_i^{\mathrm{EA}}$ is the common consumption at which
the reference prospect is exactly as valuable as the actual one,
$J_i^{\mathrm{ref}}(M_i^{\mathrm{EA}})=J_i$:

$$
\boxed{
M_i^{\mathrm{EA}}
=\lambda_c\exp\!\left\{
\frac{\log J_i-\log H_i}{\beta_c}
\right\}.}
$$

**Interpretation.** Four things follow.

1. $J_i$ values the household's actual consumption prospects over its whole
   estimated opportunity environment: every job enters, weighted by how
   available it is and how much the household values it.
2. $H_i$ builds the own-opportunity, flat-consumption reference: the same jobs,
   the same availability and the same preferences, with pay differences
   removed.
3. $M_i^{\mathrm{EA}}$ is the constant consumption level that makes that
   reference prospect equivalent to the actual prospect. It is in euros per
   month.
4. Opportunity composition therefore enters welfare directly. A common
   rescaling of $\widehat g_i$ multiplies $J_i$ and $H_i$ alike and cancels;
   what does not cancel is how opportunity weight is spread across jobs with
   different consumption and leisure. Access changes which jobs receive weight;
   earning opportunities change the consumption those jobs deliver.

The integrals have a random-utility reading. Under the maintained type-I
extreme-value shocks and latent-job structure, $\log J_i$ is, up to an additive
constant common to $J_i$ and $H_i$, the expected utility of the best job the
household can reach, averaged over the jobs that happen to be available and
over its taste shocks. The ex-ante measure therefore treats the dispersion of
those shocks as part of what makes a rich prospect valuable. That is a
normative position, not a consequence of estimation: if the shocks are read as
optimisation errors rather than as idiosyncratic tastes, part of the value
attributed to variety would not be welfare. The reference prospect carries the
same shocks and the same opportunity environment, which limits but does not
remove this dependence.

**Empirical use.** $J_i$ and $H_i$ are integrated numerically over each
household's estimated opportunity environment, with every integration point
priced through the tax-benefit system. The resulting $M_i^{\mathrm{EA}}$ and its
counterfactual versions give the ex-ante decomposition. Integration design,
reference-domain convention and numerical checks are in the appendix.

## Outcomes versus prospects

Neither perspective corrects the other. The attained-bundle measure answers a
question about outcomes and the ex-ante measure a question about prospects, and
both are money metrics derived from an explicit indifference condition. Because
opportunities reach them through different routes—through the realised job in
one case and as weights on the whole prospect in the other—the two can
attribute inequality to different labour-market channels. When they do, the
difference is informative about what each welfare question makes visible. The
choice between them is a substantive normative decision and is not made here.

## F. Equivalisation

**Why.** Both money metrics are household-level consumption equivalents.
Inequality comparisons across households of different size and composition
require a convention for resources and needs.

**Object.** For either perspective $p\in\{\mathrm{att},\mathrm{EA}\}$,

$$
M_i^{p,\mathrm{eq}}=\frac{M_i^{p}}{e_i},
$$

where $e_i$ is the modified-OECD equivalence scale of household $i$.

**Interpretation.** $e_i$ is a normative reporting convention, not an
estimated parameter. Every result is reported both on the raw household basis
and equivalised. Single-adult and couple households are separate estimated
populations and their welfare levels are never pooled or compared.

**Empirical use.** The convention is substantively consequential, not a
formatting choice. For couples under the ex-ante perspective, equivalising
moves the access-plus-earnings share of baseline inequality from
21.3% to
7.9% and turns the preference contribution
negative. That is why both bases are always shown.


# 4. From well-being to inequality: counterfactuals and the Shapley allocation


The current decomposition equalises preferences, geographic/temporal job access and systematic earning opportunities while holding household resources, needs and composition fixed. Household resources, needs and composition are not
equalised and receive no allocated share, so the three pathways do not exhaust
the sources of welfare inequality.

The figure maps the exercise before the formal objects. Any combination of the three channels is equalised to a common reference while household resources, needs and composition stay fixed; the resulting counterfactual household is evaluated under both welfare perspectives, inequality is measured, and the Shapley rule allocates the change.


![How the decomposition is built. Three channels can be equalised: systematic preferences; local labour-market access (local unemployment exposure, region, urban or rural location and year); and systematic earning opportunities. Household resources, needs and composition are held fixed in every coalition. Each counterfactual household is evaluated under both welfare perspectives, inequality is measured with the household-weighted Gini, and the Shapley rule averages each channel's marginal contribution over all orders.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v13/fig_v13_architecture.png){width=95%}


## G. Counterfactual inequality

**Why.** A well-being distribution alone does not say which sources of
heterogeneity it reflects. To ask how much inequality is associated with a
pathway, the pathway must be removed inside the model and welfare recomputed.

**Object.** Write household $i$'s structural inputs as
$x_i=(x_i^P,x_i^A,x_i^B,d_i)$: the characteristics that shift systematic
utility, the geographic and temporal access shifters, the characteristics that
shift the wage-offer location, and household resources, needs and composition.
The operators

$$
\begin{aligned}
T_Px_i&=(\bar x^P,x_i^A,x_i^B,d_i),\\
T_Ax_i&=(x_i^P,\bar x^A,x_i^B,d_i),\\
T_Bx_i&=(x_i^P,x_i^A,\bar x^B,d_i)
\end{aligned}
$$

replace one pathway by a common reference profile, and $T_S$ applies the
substitutions named by a coalition $S\subseteq\{P,A,B\}$ together. With
$\mathcal G$ the household-weighted Gini,

$$
I^p(S)=\mathcal G\!\left(\left\{M_i^p(T_Sx_i)\right\}_{i=1}^N\right),
\qquad
v^p(S)=I^p(\varnothing)-I^p(S).
$$

**Interpretation.** Each coalition is a structural counterfactual: the named
sources of heterogeneity are equalised, welfare is fully recomputed for every
household under perspective $p$, and inequality is measured again. $T_P$
equalises age profiles and the child-related shifter while keeping sex- and
household-type-specific blocks. $T_A$ equalises local unemployment exposure, region,
urbanisation and year where they enter access—the geographic/temporal channel,
not all job opportunities. $T_B$ equalises the education- and experience-related
wage-offer location, not wage dispersion, wage luck or selection. Estimated
coefficients are never changed, and $d_i$ is the same in every coalition, so
$I^p(\{P,A,B\})$ generally remains positive. $v^p(S)$ is the inequality removed
by equalising the pathways in $S$.

**Empirical use.** $I^p(S)$ is the bridge from the estimated model to the
decomposition: eight coalitions per perspective, household type and scale,
each with complete recomputation of welfare and inequality.

## H. Shapley allocation

**Why.** The pathways interact. The inequality removed by equalising access
depends on whether preferences or earning opportunities have already been
equalised. Reporting one ordering would make the answer depend on an arbitrary
choice.

**Object.** For $k\in\{P,A,B\}$,

$$
\phi_k^p
=\sum_{S\subseteq\{P,A,B\}\setminus\{k\}}
\frac{|S|!\,(3-|S|-1)!}{3!}
\left[v^p(S\cup\{k\})-v^p(S)\right],
\qquad
\phi_P^p+\phi_A^p+\phi_B^p=I^p(\varnothing)-I^p(\{P,A,B\})\equiv\Delta I^p .
$$

**Interpretation.** $\phi_k^p$ is the marginal contribution of pathway $k$
averaged over all $3!=6$ orders in which the three equalisations can be
introduced. The allocation adds up exactly to the movable component
$\Delta I^p$. Contributions are signed: a negative term means that, on average
over orders, equalising that pathway raises inequality. This is the standard
Shapley value from cooperative game theory, applied as in the distributional
decomposition literature; no new allocation principle is claimed.

**Empirical use.** Two denominators are kept apart. A share of $\Delta I^p$
describes how the movable component is allocated. A share of
$I^p(\varnothing)$ describes the size of a contribution relative to baseline
inequality. The headline access-plus-earnings figures are shares of each
perspective's own baseline Gini. The same operators and allocation rule are
applied to both welfare perspectives, which makes their channel orderings
comparable.

## A planned extension: household resources, needs and composition

A fourth pathway $D$, equalising household resources, needs and composition,
is a planned extension and is not part of the present results. If it is added,
$A+B$ remains the labour-market opportunity component, while $A+B+D$ would
describe broader non-preference circumstances. $A+B+D$ would not be an
opportunity share.


# 5. What the current results say


> **Main result.** Under attained-bundle welfare, earning opportunities matter
> more than the coarse access channel. Under ex-ante welfare, access becomes
> much more important for single-adult households—about three times earning
> opportunities. Couples show no such reversal. The importance assigned to different labour-market inequalities depends on whether welfare evaluates the realised outcome or the opportunity prospect itself.


## Behavioural estimates

The preference, opportunity and wage blocks are estimated separately for single adults and couples. Optimiser paths, curvature diagnostics and the complete list of maintained parameter restrictions are in the appendix.


Table: The preference block. Cluster-robust standard errors in parentheses, clustered on the household. "At bound" marks an estimate at a box endpoint, whose interval is reported under the active-set convention in the appendix. The consumption weight is common within a population and enters as $\beta_c\log(C/\lambda_c)$.

|Coefficient|Single men|Single women|Couple men|Couple women|
|---|---|---|---|---|
|Leisure weight, intercept $\beta_{\ell 0}$|8.5199 (3.5480)|5.8683 (2.1346)|3.9814 (0.7466)|13.1029 (4.7760)|
|Leisure weight, age $\beta_{\ell a}$|1.4820 (1.0236)|0.0678 (0.4792)|-0.0080 (0.0287)|-0.1228 (0.1260)|
|Leisure weight, age squared $\beta_{\ell a^2}$|0.7783 (0.7732)|1.0000 (at bound)|0.0065 (0.0030)|0.0073 (0.0103)|
|Leisure weight, children $\beta_{\ell n}$|&mdash;|0.1666 (0.4422)|&mdash;|-0.3055 (1.1472)|
|Leisure curvature $\theta_\ell$|-1.6263 (0.3301)|-0.9274 (0.2161)|-0.9761 (0.1357)|-1.6863 (0.2458)|
|Consumption weight $\beta_c$|2.0387 (0.2917)|2.0387 (0.2917)|2.1017 (0.2939)|2.1017 (0.2939)|



The consumption weight is 2.0387 with a cluster-robust standard error of 0.2917 for single adults and 2.1017 with 0.2939 for couples. Two things follow. In the closed-form welfare measure of Section 3, $\beta_c$ is the rate at which a household's non-consumption advantage at its observed job over staying home, $L_i(j_i^{\mathrm{obs}})-L_i(o)$, converts into a proportional adjustment of its own observed consumption: the same advantage moves the money metric proportionally less, the larger $\beta_c$ is, because the advantage enters the exponent divided by $\beta_c$. And because utility is on the unit-scale shock, one natural unit of the index corresponds to multiplying consumption by $\exp(1/\beta_c)$, a factor of 1.633 for single adults and 1.609 for couples. That is a proportional statement: there is no single euro value of a unit of utility independent of the consumption at which it is evaluated.


Table: The opportunity block: employment access, the hours density and occupation access. Cluster-robust standard errors in parentheses. The employment index multiplies the working indicator; the omitted references are region 1, thinly populated areas, the residual hours set of total width 29.5 hours per week, and occupation group 1. The singles occupation column reports the female coordinates; the male coordinates are in the appendix table. Hours coefficients are common across the two singles sex groups and spouse-specific for couples.

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
|Hours band: Part-time lower, [18.5, 21.5)|0.0298 (0.1972)|-1.1094 (0.3791)|-0.5173 (0.1629)|
|Hours band: Part-time upper, [29.5, 30.5)|0.7080 (0.1928)|0.0835 (0.2378)|1.1586 (0.1214)|
|Hours band: Narrow full-time, [33.5, 36.5)|2.0656 (0.0894)|2.2888 (0.0821)|2.0284 (0.0682)|
|Hours band: Full-time upper, [37.5, 40.5]|1.9387 (0.0997)|2.3801 (0.0866)|1.6825 (0.0798)|
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



Some coefficients are restricted rather than estimated: consumption enters in exact logs, the male children leisure effect in couples is zero, and couples have no direct cross-leisure term. The singles and couples models are estimated separately, so their wage blocks are not restricted to agree.


![Indifference curves in consumption and leisure, single-adult households, at one representative household of each sex. The budget set, the opportunity density and the taste shock are not drawn, so a curve is not a set of attainable bundles. The consumption axis is logarithmic; under log consumption every finite utility target is attainable at a finite positive consumption, which may lie outside the plotted range.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v5/figP01_indifference_curves_singles.png){width=95%}



![Indifference curves in consumption and each spouse’s leisure, couple households, with the partner’s leisure held at its observed value. Conditional slices of a joint object, not attainable sets.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v5/figP02_indifference_curves_couples.png){width=95%}



![Marginal rate of substitution between leisure and consumption, by age and sex, in euros per month per additional recurring weekly hour of leisure. A compensation along an indifference curve, not a behavioural response to a wage change.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v5/figP04_mrs_by_age_sex.png){width=95%}


The indifference curves and the marginal rate of substitution are the economics; the coefficients are coordinates. Note that the consumption axis is logarithmic and the curves are drawn over the plotted range only: under $L(\ell)+\beta_c\log(C/\lambda_c)$, any finite utility target at positive leisure is reached at the finite positive consumption $C=\lambda_c\exp\{(\bar u-L(\ell))/\beta_c\}$, which is strictly positive for every finite target. A curve leaving the frame has left the plotting range, not the domain of the model, and nothing here is economically infeasible.



![Marginal utility of consumption and of leisure in physical units, after the chain-rule conversion from the normalized coordinates. Levels are not comparable across separately estimated utility scales.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v5/figP03_marginal_utilities.png){width=95%}




## Predictive fit


The fit evidence is a population prediction, obtained by integrating the
estimated choice model over the opportunity distribution and the taste shocks.
It is not the probability of choosing from the finite set used in estimation
and it is not an in-sample fitted choice. The comparison therefore tests the
model away from the realised choices used to estimate it.


![Weighted extensive-margin accuracy by group against the range the estimated model itself produces by chance; groups whose statistic is too imprecise are withheld.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v7/fitext_band_v3b.png){width=95%}


The preferred specification reproduces participation and occupation margins
closely in aggregate, while its hours fit is uneven. Across all reported
population moments, the corrected mean absolute deviation is
0.0140 for single adults and 0.0119 for couples.
The correction is not an across-the-board improvement: the single-adult value
rises slightly while the couple value falls.

For the extensive margin, numerical precision is sufficient to report an
accuracy of 85.7% for single women, against a
model-simulated range of 80.0%–85.9%,
and 89.8% for coupled women, against
88.1%–91.2%.
The corresponding statistics for single men and coupled men are WITHHELD
because numerical integration error remains too large relative to sampling
variation.

The common hours mismatch is underprediction of the observed 37-hour mass
point. The observed-minus-predicted gaps are
3.8 percentage points for single women,
4.4 for coupled men,
5.2 for single men and
6.5 for coupled women. This is a finding about the
observed concentration at exactly 37 hours, not the model's neighbouring
full-time range.


![Corrected population fit: observed against predicted shares.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v7/fit_by_margin_v7.png){width=95%}


The margin-by-margin comparison below reports every population moment. The
sub-ten-hour cell is a coverage limitation of the finite integration sample,
which contains no draw between 5 and 10 hours; the long-hours reporting bin
closes at 70 hours inclusive.


Table: Corrected observed and predicted population moments, single adults. Population predictions integrate the model over opportunities and taste shocks.

|Unit|Moment|Observed|Model|Absolute deviation|Denominator|
|---|---|---|---|---|---|
|Man|Employment|0.8805|0.8675|0.0130|households|
|Man|Hours: non-employment|0.1195|0.1325|0.0130|households|
|Man|Hours: [5, 10)|0.0109|0.0000|0.0109|households|
|Man|Hours: [10, 18.5)|0.0080|0.0246|0.0166|households|
|Man|Structural PT1: [18.5, 21.5)|0.0113|0.0167|0.0054|households|
|Man|Hours: [21.5, 29.5)|0.0286|0.0646|0.0360|households|
|Man|Structural PT2: [29.5, 30.5)|0.0032|0.0187|0.0155|households|
|Man|Hours: [30.5, 33.5)|0.0107|0.0315|0.0208|households|
|Man|Hours: [33.5, 36.5)|0.2329|0.2457|0.0128|households|
|Man|Observed 37-hour mass point: [36.5, 37.5)|0.0624|0.0105|0.0519|households|
|Man|Structural FT: [37.5, 40.5]|0.2776|0.2347|0.0429|households|
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
|Woman|Hours: [10, 18.5)|0.0278|0.0317|0.0038|households|
|Woman|Structural PT1: [18.5, 21.5)|0.0290|0.0283|0.0007|households|
|Woman|Hours: [21.5, 29.5)|0.0612|0.0856|0.0245|households|
|Woman|Structural PT2: [29.5, 30.5)|0.0288|0.0236|0.0052|households|
|Woman|Hours: [30.5, 33.5)|0.0290|0.0367|0.0077|households|
|Woman|Hours: [33.5, 36.5)|0.2672|0.2581|0.0091|households|
|Woman|Observed 37-hour mass point: [36.5, 37.5)|0.0503|0.0123|0.0381|households|
|Woman|Structural FT: [37.5, 40.5]|0.1990|0.2264|0.0274|households|
|Woman|Hours: (40.5, 44.5)|0.0492|0.0446|0.0045|households|
|Woman|Hours: [44.5, 70]|0.1185|0.1192|0.0007|households|
|Woman|Occupation group 1|0.1795|0.1832|0.0036|workers|
|Woman|Occupation group 2|0.1976|0.1946|0.0031|workers|
|Woman|Occupation group 3|0.1349|0.1348|0.0002|workers|
|Woman|Occupation group 4|0.4879|0.4875|0.0004|workers|
|Woman|Mean log wage|2.5968|2.6207|0.0238|workers|




Table: Corrected observed and predicted population moments, couples. Population predictions integrate the model over opportunities and taste shocks.

|Unit|Moment|Observed|Model|Absolute deviation|Denominator|
|---|---|---|---|---|---|
|Household|Joint regime neither works|0.0222|0.0043|0.0178|households|
|Household|Joint regime man only|0.0794|0.0909|0.0115|households|
|Household|Joint regime woman only|0.0547|0.0723|0.0176|households|
|Household|Joint regime both work|0.8437|0.8324|0.0113|households|
|Man|Employment|0.9231|0.9234|0.0002|households|
|Man|Hours: non-employment|0.0769|0.0766|0.0002|households|
|Man|Structural PT1: [18.5, 21.5)|0.0037|0.0041|0.0004|households|
|Man|Structural PT2: [29.5, 30.5)|0.0093|0.0094|0.0002|households|
|Man|Hours: [33.5, 36.5)|0.2515|0.2507|0.0008|households|
|Man|Observed 37-hour mass point: [36.5, 37.5)|0.0539|0.0098|0.0441|households|
|Man|Structural FT: [37.5, 40.5]|0.2736|0.2682|0.0054|households|
|Man|Hours: [44.5, 70]|0.2576|0.2531|0.0044|households|
|Man|Occupation group 1|0.3519|0.3516|0.0003|workers|
|Man|Occupation group 2|0.0797|0.0741|0.0056|workers|
|Man|Occupation group 3|0.0464|0.0412|0.0052|workers|
|Man|Occupation group 4|0.5220|0.5331|0.0111|workers|
|Man|Mean log wage|2.7687|2.7054|0.0633|workers|
|Woman|Employment|0.8984|0.9047|0.0063|households|
|Woman|Hours: non-employment|0.1016|0.0953|0.0063|households|
|Woman|Structural PT1: [18.5, 21.5)|0.0229|0.0230|0.0001|households|
|Woman|Structural PT2: [29.5, 30.5)|0.0419|0.0439|0.0020|households|
|Woman|Hours: [33.5, 36.5)|0.2687|0.2767|0.0080|households|
|Woman|Observed 37-hour mass point: [36.5, 37.5)|0.0785|0.0134|0.0651|households|
|Woman|Structural FT: [37.5, 40.5]|0.2008|0.1938|0.0070|households|
|Woman|Hours: [44.5, 70]|0.1079|0.1002|0.0077|households|
|Woman|Occupation group 1|0.1653|0.1648|0.0005|workers|
|Woman|Occupation group 2|0.1922|0.2017|0.0095|workers|
|Woman|Occupation group 3|0.1533|0.1583|0.0050|workers|
|Woman|Occupation group 4|0.4892|0.4752|0.0140|workers|
|Woman|Mean log wage|2.6072|2.6319|0.0247|workers|



At the level of individual predictions the evidence is group-specific. For all
four groups, the association between predicted probabilities and realised
outcomes is what conditioning on realised outcomes mechanically produces under
stochastic choice. For coupled men and coupled women the remaining dispersion
is evidence of misspecification; for single men and single women numerical
integration error is too large to decide. An earlier claim of excess
predictability across three groups is withdrawn.


Table: The preferred single-adult model and the two re-estimated common-opportunity benchmarks.

|Specification|Free coordinates|Criterion|Difference|Population fit|
|---|---|---|---|---|
|Latent jobs with household-specific opportunities|41|6253.463|--|0.0140|
|Benchmark A: common opportunity distribution, preferences re-estimated|10|6403.974|+150.51|0.0273|
|Benchmark B: common opportunity shape, employment and hours moved into utility|16|6395.108|+141.64|0.0264|



The two re-estimated common-opportunity benchmarks are worse by 141.64 and by a larger margin, on the same households, the same sampled alternatives and the same criterion. The comparison is a nested one in the sense that the benchmarks restrict the opportunity block and re-estimate everything else, but we do not convert it into a formal test, because the sampled-alternative criterion is not the likelihood of the observed data and the conditions for a likelihood-ratio distribution are not established here. What the table does support is that the deterioration is concentrated where the opportunity block does its work: the population fit worsens from 0.0140 to 0.0273 and 0.0264, and the occupation margins deteriorate by an order of magnitude, from about half a percentage point to eleven. A better criterion does not by itself establish that a mechanism has been identified.


## Attained-bundle well-being



Table: Attained-bundle money-metric well-being and disposable consumption,
modified-OECD equivalised. Household euros per month, weighted using household
weights. The two populations are reported separately.

|Population|Households|Workers|Non-workers|Consumption mean|Consumption median|Consumption Gini|Money-metric mean|Money-metric median|Money-metric Gini|
|---|---|---|---|---|---|---|---|---|---|
|Single-adult|1,540|1,336|204|1,766|1,588|0.2633|1,302|1,165|0.2498|
|Couple|2,223|2,173|50|2,245|2,063|0.2268|1,311|1,237|0.1974|


On the equivalised basis, the Gini of the attained-bundle money metric is
0.2498 for single-adult households and
0.1974 for couples, compared with
0.2633 and 0.2268 for disposable
consumption in the same samples. These are within-sample dispersion
comparisons, not welfare-loss estimates: the gap between the money metric and
observed consumption reflects the leisure a job costs relative to not working,
and no loss index is constructed from it.

## Attained-bundle decomposition

Equalising systematic utility heterogeneity, coarse geographic and temporal
access, and systematic wage opportunities—while holding household resources,
needs and composition fixed—reduces the Gini by
1.8–9.9%
relative to its baseline level across household types and reporting scales.
Within this restricted exercise, the earning-opportunity channel is larger
than the coarse access channel throughout. The preference contribution changes
sign with equivalisation, so no directional claim is made about it.


Table: Complete Shapley allocation of the change in the Gini after equalising
the three modelled dimensions. Contributions are Gini points; shares refer to
$\Delta I$, not to baseline inequality. The last column reports an independent
simulation run. The preference share is left unstated because its contribution
changes sign with equivalisation.

|Population|Scale|Dimension|Economic content|Gini-point contribution|Share of $\Delta I$|Independent-run Gini-point|
|---|---|---|---|---|---|---|
|Single-adult|unequivalised|Systematic preferences|Age profiles and the child-related shifter|+0.0012|—|+0.0011|
|Single-adult|unequivalised|Coarse access|Local unemployment exposure, region, urban or rural location, and year|+0.0016|23.4%|+0.0017|
|Single-adult|unequivalised|Earning opportunities|Systematic wage-offer location|+0.0040|58.6%|+0.0042|
|Single-adult|unequivalised|$\Delta I$|Total change after all three equalizations|+0.0069|100.0%|+0.0071|
|Single-adult|equivalised|Systematic preferences|Age profiles and the child-related shifter|-0.0003|—|-0.0004|
|Single-adult|equivalised|Coarse access|Local unemployment exposure, region, urban or rural location, and year|+0.0013|29.6%|+0.0014|
|Single-adult|equivalised|Earning opportunities|Systematic wage-offer location|+0.0034|77.4%|+0.0038|
|Single-adult|equivalised|$\Delta I$|Total change after all three equalizations|+0.0045|100.0%|+0.0049|
|Couple|unequivalised|Systematic preferences|Age profiles and the child-related shifter|+0.0064|—|+0.0065|
|Couple|unequivalised|Coarse access|Local unemployment exposure, region, urban or rural location, and year|+0.0009|4.6%|+0.0009|
|Couple|unequivalised|Earning opportunities|Systematic wage-offer location|+0.0128|63.5%|+0.0127|
|Couple|unequivalised|$\Delta I$|Total change after all three equalizations|+0.0201|100.0%|+0.0201|
|Couple|equivalised|Systematic preferences|Age profiles and the child-related shifter|-0.0019|—|-0.0019|
|Couple|equivalised|Coarse access|Local unemployment exposure, region, urban or rural location, and year|+0.0007|14.6%|+0.0008|
|Couple|equivalised|Earning opportunities|Systematic wage-offer location|+0.0062|124.0%|+0.0061|
|Couple|equivalised|$\Delta I$|Total change after all three equalizations|+0.0050|100.0%|+0.0050|



![Attained-bundle welfare: exact Shapley contribution of each channel to the change in the Gini, in Gini points, for raw and equivalised reporting, with each baseline Gini stated in the panel. Access is local labour-market access (local unemployment exposure, region, urban or rural location and year). Preliminary. Household resources, needs and composition are held fixed. The preference contribution changes sign with equivalisation in both samples, so no directional claim is made about it. Values are the coalition and Shapley records of the attained-bundle decomposition.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v13/fig_v13_att_decomposition.png){width=95%}


The coalition values behind the allocation are reported in full. "Change from
actual" is the one-factor effect of each coalition; the Monte Carlo range is the
spread of the Gini level across 1,000 simulation replications, never a
confidence interval.


Table: Single adults, the eight P/A/B coalitions. Weighted Gini of money-metric well-being, household-weighted, simulated on the estimated model’s already-priced estimation panel with no re-estimation and no new pricing. "Change from actual" is the one-factor effect of that coalition. The Monte Carlo range is the spread of the Gini level across 1,000 simulation replications, never a confidence interval.

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




Table: Couples, the eight P/A/B coalitions. Weighted Gini of money-metric well-being, household-weighted, simulated on the estimated model’s already-priced estimation panel with no re-estimation and no new pricing. "Change from actual" is the one-factor effect of that coalition. The Monte Carlo range is the spread of the Gini level across 1,000 simulation replications, never a confidence interval.

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



Consumption dispersion is large relative to dispersion in log well-being: the
variance of log consumption is roughly
100–127% of the
variance of log well-being, the excess offset by a large negative covariance
between consumption and the value of leisure. Household resources, needs and
composition stay outside the allocation, as do sex-specific parameter
differences and behavioural randomness.

**Robustness.** Every coalition Gini and every Shapley contribution reproduces
closely under an independent second simulation seed, including the sign change
of the preference contribution. The simulation always includes each household's
own observed job, which 2.9% of single adults and
3.9% of couples attain under every coalition;
excluding it moves $\Delta I$ by at most 9.3% (couples,
equivalised), with no sign change in any specification.

An allocated contribution averages a pathway's marginal effect over all
coalition orders; it is not the one-factor reduction. The full allocation is
shown because interactions matter. Every coalition Gini and contribution is
closely reproduced by an independent simulation. The allocation closes to
numerical precision. These checks validate the calculation for the stated game;
they do not validate its maintained behavioural assumptions or turn it into a
causal decomposition.


## Ex-ante well-being and decomposition


The ex-ante perspective values the household's whole job prospect. Its
distribution and exact Shapley accounting, which passed the numerical checks
reported in the appendix, are:


Table: Ex-ante money-metric inequality and its exact Shapley allocation. Contributions are Gini points; access plus earnings is reported as a share of baseline inequality. Household-weighted.

|Population|Scale|Households|Mean EUR/month|Median EUR/month|Baseline Gini|Preference|Access|Earning opportunities|Access + earnings / baseline|Ordering|
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
|Single-adult|Raw household|1,540|1,290.2|1,206.2|0.1595|0.00157|0.01812|0.00555|14.8%|Access > earnings|
|Single-adult|Equivalised|1,540|1,153.1|1,114.3|0.1406|0.00020|0.02183|0.00673|20.3%|Access > earnings|
|Couple|Raw household|2,223|3,318.0|3,182.1|0.1277|0.00291|0.00667|0.02049|21.3%|Earnings > access|
|Couple|Equivalised|2,223|1,753.3|1,673.7|0.1200|-0.00212|0.00449|0.00504|7.9%|Earnings > access|



![Ex-ante welfare: exact Shapley contribution of each channel to the change in the Gini, in Gini points, for raw and equivalised reporting, with each baseline Gini stated in the panel. Access is local labour-market access (local unemployment exposure, region, urban or rural location and year). The calculation passed its numerical checks; household resources, needs and composition are held fixed. For couples the preference contribution changes sign with equivalisation.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v13/fig_v13_ea_decomposition.png){width=95%}


The access and earning-opportunity contributions together account for
7.9–21.3% of
baseline ex-ante inequality, depending on household type and scale. For
single-adult households, access is 3.3
times the earning-opportunity contribution before equivalisation and
3.2 times after it—about three times on
either basis. For couples, earning opportunities remain larger than access.

Equivalisation is materially consequential for couples. It moves the ex-ante
access-plus-earnings share from 21.3% to
7.9% of baseline inequality and turns the
preference contribution negative. The scale convention therefore changes the
substantive attribution, and no directional claim about preferences is made.


## The central result: outcomes versus prospects


![The central result. Access and earning-opportunity contributions, each as a percentage of its own perspective's baseline Gini, under attained-bundle welfare (ATT) and ex-ante welfare (EA). Access is local labour-market access (local unemployment exposure, region, urban or rural location and year). For single-adult households earning opportunities are larger under ATT and access is larger under EA, on both scales; couples show no such reversal. Household resources, needs and composition are held fixed; neither perspective is designated primary.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v13/fig_v13_central_result.png){width=95%}



Table: The same access and earning-opportunity operators under two welfare perspectives. Shares are relative to each perspective's own baseline Gini. Neither perspective is designated primary.

|Population|Scale|Attained-bundle A + B / baseline|Attained ordering|Ex-ante A + B / baseline|Ex-ante ordering|
|---|---|---:|---|---:|---|
|Single-adult|Raw household|2.4%|Earnings > access|14.8%|Access > earnings|
|Single-adult|Equivalised|1.9%|Earnings > access|20.3%|Access > earnings|
|Couple|Raw household|6.7%|Earnings > access|21.3%|Earnings > access|
|Couple|Equivalised|3.5%|Earnings > access|7.9%|Earnings > access|


The comparison applies the same operators and the same allocation rule to both
welfare perspectives. It is not a pure comparison of welfare definitions: the
attained-bundle counterfactual is integrated on a sample that covers short hours
sparsely, while the ex-ante integrals use a separate certified design
(Section 6).

Three findings stand out.

- **ATT: earning opportunities matter more than access.** When welfare values
  the attained bundle, access and earning opportunities together account for
  1.9–6.7% of
  baseline inequality, and earning opportunities are larger than access for
  both household types on both scales.
- **EA: access becomes much more important for single adults.** When welfare
  values the whole prospect, the combined share is
  7.9–21.3%, and for
  single-adult households access is
  3.3 times earning opportunities
  before equivalisation and 3.2 times
  after it.
- **Couples show no such reversal.** Earning opportunities remain larger than
  access for couples under both perspectives and on both scales.

The importance assigned to different labour-market inequalities depends on whether welfare evaluates the realised outcome or the opportunity prospect itself. The economic mechanism is the route by which
opportunities enter each measure. The attained-bundle measure sees only the
realised job, where the wage drives disposable consumption, so systematic
differences in wage offers dominate. The ex-ante measure weights every job by
its availability, so a household's coarse access environment enters welfare
directly. Why the reversal appears for single adults and not for couples is
not tested here; one reading is that a single adult's participation depends on
one earner's access, whereas a couple's joint budget and second earner leave
earning opportunities in front. The reversal is a finding for single-adult
households only. Neither measure is designated primary here.

Earlier circulated figures near 90% described all non-preference
circumstances, including household resources and composition, rather than job
opportunities alone. They are not comparable with the restricted
access-and-earnings figures reported here and are not current results.

All percentages in this section come from restricted three-pathway accounting
exercises that hold household resources, needs and composition fixed. They do
not estimate the total share of well-being inequality caused by unequal job
opportunities.


# 6. What remains preliminary


These decomposition estimates are preliminary and subject to ongoing numerical
validation of the counterfactual integration. That caveat applies especially
to the attained-bundle counterfactual, which carries realised alternatives
through a finite integration sample. The ex-ante numerical calculation has
passed its declared checks, including an independent implementation, but
certification of a calculation is not certification of the model's maintained
economic assumptions. This numerical certification establishes that the computation is correct given the model and operators; it does not establish causal identification, does not quantify statistical uncertainty in the estimated parameters, and does not establish that either welfare perspective is the normatively correct one.

## Scale and household comparison

Equivalisation is a normative convention and is materially consequential here.
For couples, dividing by the modified-OECD scale moves the ex-ante access-plus-
earnings share from 21.3% to
7.9% of baseline inequality and changes
the preference contribution from 0.00291 Gini points to
-0.00212. The latter is negative. A negative Shapley term
means that, averaged over coalition orders, equalising that pathway raises
rather than lowers inequality. It does not establish that preference
heterogeneity is equalising in a causal or welfare-theoretic sense. Because the
sign and magnitude depend on scale, no directional claim about preferences is
made.

The two household types are separate estimated populations. Their means,
medians and Ginis describe within-population distributions; welfare levels are
not compared across single-adult and couple households. Reporting both raw and
equivalised results exposes the role of the scale convention instead of hiding
it behind one preferred presentation.

## Scope of the equalisation exercise

The access pathway is coarse. It contains region, urban or rural location and
survey year where those variables enter employment access. It does not contain
personal occupation access, the concentration of offers at particular hours,
or every feature of a feasible job. The earning-opportunity pathway equalises
systematic wage-offer locations, not the common dispersion of wages, realised
wage luck or selection. Those location differences shift offered wages by at most
about 0.10 log points, against a common offer spread of
about 0.37 log points, so the operator removes a small part of
earnings dispersion by construction; this is a definitional boundary, not a
measurement error. Household resources, needs and composition are fixed
throughout and receive no allocated share; adding them as a fourth pathway is
a planned extension. The resulting percentages therefore are neither a
complete decomposition of well-being inequality nor estimates of the causal
effect of geography, education or occupation.

The Shapley allocation is exact for the declared three-pathway game. Exact
closure shows that interactions have been allocated consistently; it says
nothing about whether the pathways are normatively exhaustive. Likewise, the
independent numerical reproduction rules out many implementation mistakes but
does not remove parameter uncertainty. The reported repeat-run comparisons are
simulation checks, not confidence intervals. Estimation uncertainty has not
been propagated through either decomposition.

## Numerical and predictive boundaries

The attained-bundle exercise uses an integration sample that represents the
lower part of the modelled hours range sparsely, while a separate assessment
finds substantial model-implied mass there. Its direct effect on the
attained-bundle attribution has not been fully quantified. Coverage below ten
hours therefore remains an explicit limitation of that exercise.

The predictive evidence has a separate boundary. Women's extensive-accuracy
statistics are reportable, but the corresponding statistic for each group of
men is withheld because numerical integration error is too large relative to
sampling variation. The underprediction at exactly 37 hours is retained as its
own finding rather than absorbed into a wider full-time interval. Aggregate fit
does not eliminate these group- and margin-specific discrepancies.

The common-opportunity benchmarks carried one input defect. The first benchmark's
estimation input used a different width for the residual hours set, which shifts
its log hours density by a constant that cancels from the conditional
likelihood; its estimates, standard errors and criterion comparison are
unchanged, and the second benchmark does not use those rows. Its absolute
opportunity-mass levels were nonetheless mis-scaled, and the benchmark fit
moments reported above are the corrected ones. No downstream use of those
absolute levels was found, but the search was not exhaustive.

Wage elasticities are not reported. A valid gross-wage perturbation requires new
tax-benefit pricing of the affected job alternatives, and the priced support
used here does not contain that counterfactual.

## Maintained econometric assumptions

The separation of preferences from opportunities relies on the functional
form and exclusion restrictions in Section 2. Smooth leisure preferences,
piecewise hours opportunities, excluded local-labour-market shifters and
conditional independence of wages and hours are maintained assumptions. The
regional variation does not create causal identification, and the model does
not establish that omitted personal access dimensions are orthogonal to the
included ones.

Two observation-rule questions also remain open. The estimation sample screens
on observed hours and wages for workers, so it is selected on outcomes of the
process being modelled. In addition, the sampled-choice probability conditions
on a labelled collection of alternatives. Existing diagnostics are consistent
with the assumed sampling law but do not prove it. Finally, the weekly time
endowment is maintained rather than estimated, and the model is not invariant
to changing it. Re-estimating the model with an endowment of 75 or 90 hours
instead of 80 rebuilds physical leisure, moves the criterion materially in
opposite directions and changes which single-adult coefficients sit at their
bounds; the couples model has no coefficient at a bound in any of the three.
The 80-hour baseline is a maintained convention.


![Time-endowment sensitivity evidence. T=75 and T=90 are independent re-estimations; T=80 is the baseline used as-is and was not re-estimated.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v5/ws4_sectionC_T_v1.png){width=95%}

 These issues qualify structural interpretation without
altering the arithmetic of the reported calculations.

## The welfare comparison

The contrast between the two perspectives is computed with identical operators
and allocation rules, but not with identical numerical integration. The
attained-bundle counterfactual carries realised alternatives through a finite
integration sample that represents short hours sparsely; the ex-ante integrals
use a separate, certified integration design. Part of any numerical difference
between the two decompositions could therefore reflect integration rather than
the welfare definition alone, although the channel orderings are stable across
the reported ex-ante sensitivities.


# Bibliography

::: {#refs}
:::

<!-- V15_PROVENANCE_APPENDIX_BEGIN -->
# 7. Appendix. Technical record and provenance


This appendix contains implementation material only: the estimation device,
parameter code names, simulation and integration design, numerical diagnostics,
the illustration's selection method, pricing and certification records, and
superseded historical status statements. Every economic object and result is in
the main text.

## Implementation record: sampled-alternative likelihood and optimiser

The choice set is a continuum, so the likelihood is evaluated over sampled
alternatives. For each household we draw $R=100$ alternatives from a
proposal density $q_{ij}$ and place the observed package in the set as well,
giving a set $\mathcal C_i$ with $|\mathcal C_i|=101$ rows. Write the
sampled-set index

$$
V_{ij}=v_i(j)+\log g_i(j)-\log q_{ij},
\qquad
q_{ij}=q^{E}_{ij}\left(q^{H}_{ij}q^{W}_{ij}q^{\mathrm{Occ}}_{ij}\right)^{E_{ij}} .
$$

The contribution of household $i$ is the conditional probability of its
observed package $y$ within that set,

$$
\Pr\!\left(y\mid\mathcal C_i\right)=
\frac{n_{y}\exp V_{iy}}{\sum_{s\in\mathcal C_i}\exp V_{is}} .
$$

The denominator runs over slots rather than distinct packages, and a package
drawn more than once keeps its multiplicity $n_y$; the observed package carries
the same proposal correction as any other row. The proposal density is a
computational device, fitted out of fold so that a household's own outcome never
enters the proposal used to score it. For couples the proposal draws the joint
participation regime first and then the two spouse packages conditional on it.
Non-positive simulated consumption receives a one-euro floor inside this
likelihood only.

The estimated model has 41 free coordinates for single adults, of which 40 are interior, and 47 for couples, all interior. The criterion is 6253.463 and 10283.034 respectively. Across ten terminal paths from five starts under two polishing contracts, the criterion varies by 1.1e-10 for single adults and 1.3e-09 for couples, and the smallest eigenvalue of the exact Hessian on the interior block is 0.1669 and 0.0771. One single-adult coordinate, the female age-square term in the leisure weight, sits at a box endpoint; its interval is reported under the active-set convention in the appendix and it is excluded from the interior curvature.

Optimization uses five starts under two polishing contracts, ten terminal paths
in all. These diagnostics support a stable local solution found from the starts
tested; they are not a proof of global uniqueness.

The tax-benefit accounting identity linking original income, benefits, taxes
and social contributions to disposable income holds to machine precision at
both the person and the household-alternative level, before and after the
benefit take-up adjustment.

> **Two distinct leisure-scaling exercises.** **Analytical reparameterisation
> (zero re-estimation):** the exact $\lambda_\ell$ pullback was evaluated at 10,
> 20, 40, 43.0 and 45.623591 hours a week; choice probabilities were bitwise
> equivalent and the pre-refit objective deviation was exactly zero.
> **Independent re-estimation:** the four non-baseline $\lambda_\ell$ values were
> then independently re-estimated under the full multi-start protocol as a
> separate verification of the analytical image.


![Leisure-normalisation evidence. Analytical reparameterisation (zero re-estimation) is distinguished from the subsequent independent re-estimation of the four non-baseline normalisers.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v5/ws4_sectionC_lambda_v1.png){width=95%}


## Implementation record: estimated parameter vectors and code names

**Maintained restrictions.** Singles: `theta_c_singles = 0`; the couples preference block (`beta_l0_m`, `beta_l_age_m`, `beta_l_age2_m`, `beta_l0_f`, `beta_l_age_f`, `beta_l_age2_f`, `beta_l_nkids_f`, `theta_l_f`) does not enter the singles likelihood; and `beta_E_y2015` and `beta_E_y2017` are absent because the 2015 and 2017 data are not used. Couples: `theta_c = 0`, the male children leisure effect is structurally zero, and the direct cross-leisure term is fixed at zero. These are restrictions, not estimates. The singles and couples models are estimated separately, so their wage blocks are not restricted to agree, and the difference between the two experience profiles should not be read as a test.

One single-adult coordinate, the female age-square term, is at its box endpoint.
Under the active-set convention its interval is not reported and the interior
curvature is computed after removing it.


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



## Implementation record: attained-bundle counterfactual simulation

The attained-bundle decomposition reuses the already-priced estimation sample,
with no re-estimation and no new pricing. For each coalition, household-constant
covariates of the equalised pathways are replaced by their household-weighted
sample means; covariates that vary across a household's alternatives are
protected. Each household's attained bundle is then simulated with the
Gumbel-max rule under common random numbers, so realised taste draws are carried
through every coalition, and the attained-bundle money metric and Gini are
recomputed. The executed access substitution covers local unemployment exposure,
region, urbanisation and year.

Each coalition value is the mean over 1,000 replications at fixed estimates; the
reported Monte Carlo range is the spread across replications. An independent
second seed reproduces the allocation. A per-replication share range, which
divides by that replication's own near-zero $\Delta I$, is not informative on its
own and is not shown. The allocation closes to machine precision in every sample
and scale. The simulation sample always includes each household's observed job;
the robustness check that excludes it is reported in Section 5. Neither
counterfactual-attainment route for a final decomposition is executed here.

## Implementation record: predictive-fit numerical precision

The corrected predictive-fit diagnostics numerical-adequacy standard is applied mechanically at the preregistered 0.25 threshold. Single women (85.7%, simulated 95% band [80.0%, 85.9%], ratio 0.096) and coupled women (89.8%, [88.1%, 91.2%], ratio 0.049) clear it and are reportable. Single men (ratio 0.361) and coupled men (ratio 0.353) are quadrature-limited, so their extensive accuracy is withheld. In particular, coupled men crossed the threshold after the corrected preferred specification evaluation and the earlier reportable classification is not preserved.


![Numerical convergence of predicted participation as the number of integration points grows.](C:/Users/hisham/Repo/Job_Market_paper/manuscript/figures/v7/node_convergence_v3b.png){width=95%}


## Implementation record: matched-household illustration

The illustration is produced by `make_v11_matched_households.py`, which
evaluates the accepted single-adult leisure index and opportunity density for
every estimation household with the certified ex-ante evaluators. No
estimation, pricing, welfare or decomposition routine is called. Leisure-profile
distance is the maximum absolute gap between the two households' leisure-index
curves over 5–70 weekly hours, divided by its standard deviation among employed
single adults. Opportunity distance is the closed-form total-variation distance
between the two households' opportunity densities normalised to include
non-employment; the common hours factor cancels, and wage truncation, which
removes a negligible share of offer mass, is ignored in the distance only. The
selected pair's opportunity distance is 0.58,
against an admissible-pair median of 0.13.
The source record `reports/v11_matched_households.json` stores only rounded model
quantities and the hashes of the parameter vector, estimation frame and
evaluator code; it contains no identifier or observed record value. An induced
consumption-prospect distribution is feasible from the existing priced
integration points but is not shown, because it would require reweighting those
points outside the certified calculation.

## Implementation record: data access, software and replication

**Data.** French EU-SILC, accessed through Eurostat's harmonised release, with
2016 survey collection and a 2015 income reference year, transformed into an
input file for EUROMOD [@sutherlandfigari2013] under the French 2015 policy
system. Regional labour-market conditions come from the Eurostat regional
labour-force series. Microdata access is granted under Eurostat's research-access
conditions and the data cannot be redistributed.

**Software.** Python with JAX (0.10.1) for automatic differentiation, and the
EUROMOD connector (0.2.17).

**Replication.** Code and derived, non-confidential intermediate artefacts will
be released in a public replication archive on publication; every step is
reproducible conditional on authorised access to EU-SILC.

## Certified ex-ante calculation

This record contains implementation and verification material that is excluded
from the reader-facing audit. The numerical authority is
`MNL_wea/docs/wea_sprint_1/stage4/stage4_certification_and_results_v1.json`,
with the economist-facing summary in
`MNL_wea/docs/wea_sprint_1/WEA_SPRINT_1_result_memo_v1.md`. The welfare branch
commit is `ff7c2d51`.

### Integration design

The design was chosen before inspecting any consumption integral, welfare
level, Gini or Shapley value. Two fixed independent seed streams were used.
The smallest defensive design passing the pre-specified H-accuracy rules in
all eight coalitions was 6,400 draws for singles and 76,800 for couples.
Occupation was marginalised in the target and proposal because priced
consumption depends on employment, hours and wages rather than the occupation
label itself. The final household samples contain 1,540 singles and 2,223
couples.

### Pricing volume

The calculation priced 351,024,407 new EUROMOD states: 8,573,928 and 8,574,032
for the two singles streams, and 166,937,889 and 166,938,558 for the two couples
streams. Price-replication controls had a maximum discrepancy of EUR 0.00.
Every generated market row joined exactly one priced value; there were no
missing, extra or duplicate joins and no failed or retried production tasks.

### Reference-domain convention

The reported reference is H-F. States with non-positive consumption contribute
zero to J through the $C\to0^+$ limit but remain in H and receive the common
reference consumption. There is no one-euro floor, observed-consumption
substitution or silent household deletion. H-D drops non-positive-consumption
states from both integrals. H-X excludes households whose non-employment
consumption is non-positive. The latter excludes 73 singles and 60 couples and
is disclosed only as a sensitivity.

### Certification gates

This numerical certification establishes that the computation is correct given the model and operators; it does not establish causal identification, does not quantify statistical uncertainty in the estimated parameters, and does not establish that either welfare perspective is the normatively correct one.

|Gate|Check|Singles|Couples|
|---|---|---:|---:|
|C1|Exact H on the priced set|PASS|PASS|
|C2|Effective sample size for J and H|PASS|PASS|
|C3|Largest sampled market-node share|PASS|PASS|
|C4|Wage-tail bound and high-earnings diagnostic|PASS|PASS|
|C5|Two-seed household, Gini and Shapley stability|PASS|PASS|
|C6|Constant-consumption identity|PASS|PASS|
|C7|One-state identity|PASS|PASS|
|C8|Common intensity-rescaling invariance|PASS|PASS|
|C9|Flat-reference inversion|PASS|PASS|
|C10|Finite positive welfare for every released household|PASS|PASS|
|C11|Exact Shapley adding-up|PASS|PASS|
|C12|Independent reimplementation|PASS|PASS|

C3 was amended before any population calculation to exclude the exactly
integrated non-employment atom from a diagnostic intended to detect sampled-
market weight concentration. The originally registered atom-inclusive
statistic is retained in the source record. The first large pricing launch
exhausted memory and was discarded; no partial output from it enters the
results.

### Sensitivities

Under stream B, the access-plus-earnings shares of baseline ex-ante inequality
are 14.8%, 20.3%, 21.2% and 7.8% for singles raw, singles equivalised, couples
raw and couples equivalised. Under H-D they are 15.3%, 20.6%, 21.3% and 8.0%.
Under H-X they are 15.5%, 21.3%, 22.6% and 8.5%. Access remains larger than
earnings for singles and earnings remains larger than access for couples in
every sensitivity.


## Historical status statements, superseded before V9

*Superseded before V9.* The sentence(s) immediately below are reproduced unchanged from an earlier report version and describe that version's status only, not the current one. The ex-ante calculation has been completed and passed the numerical checks documented here. Its results remain conditional on the estimated model, reference convention and specified counterfactual operators. This numerical certification establishes that the computation is correct given the model and operators; it does not establish causal identification, does not quantify statistical uncertainty in the estimated parameters, and does not establish that either welfare perspective is the normatively correct one. See “Ex-ante well-being and decomposition” in the main text and “Certified ex-ante calculation” below for the current, certified results.

*Superseded before V9.* Earlier versions printed the following paragraph three
times: in their introduction, under the heading "The distinct ex-ante
opportunity-prospect metric", and under the heading "Numerically blocked
opportunity-prospect metric".

> $W_{EA,\mathrm{flat}}$ is a distinct ex-ante opportunity-prospect metric. Its definition is fixed but it has no numerical result. Write its eventual flat-reference inversion as $H_i^{\mathrm{reference}}(m)=J_i^{\mathrm{actual}}$. The primary H-F domain retains the full opportunity environment: states with $C\leq0$ contribute zero to $J_i^{\mathrm{actual}}$ through the $C\rightarrow0^+$ utility limit, while the reference retains those states and assigns the common consumption $m$. H-D is an estimated-domain sensitivity and H-X is a disclosed sample-restriction sensitivity. No one-euro floor, observed-consumption substitution or silent household deletion is permitted. The 260 couples lacking a priced NN state and the associated support/pricing requirements currently block numerical implementation; the first post-seminar numerical task is exact-H pre-validation before any minimum accepted pricing design is launched.

*Superseded before V9.* Earlier question "Is the ex-ante opportunity-prospect
metric a result?", with its answer:

> $W_{EA,\mathrm{flat}}$ is definition-only and numerically blocked. No number for that metric is reported.

*Superseded before V9.* Earlier status sentence of the attained-bundle
decomposition appendix:

> A preliminary P/A/B decomposition has been computed for the attained-bundle money metric, holding resources, needs and composition fixed. It is a restricted counterfactual exercise, not a comprehensive share of inequality due to all opportunities. A separately defined ex-ante metric is being reconstructed for comparison; neither historical ex-ante percentages nor a settled cross-estimand conclusion are reported here.
<!-- V15_PROVENANCE_APPENDIX_END -->
