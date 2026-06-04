# Jacquet, Jia & Thoresen 2026 — How Much Does Responsibility Matter in Fairness Measurement?

> Extraction produced under `JMP_T1_exhaustive_extraction_prompt_v2.md`.
> Source of truth: the attached CESifo WP 12418 PDF. Relevance anchored to
> `JMP_project_state_v1.md` and `JMP_welfare_spec_v5.md` only.
> Three-way **access / ability / preference** vocabulary used throughout; the
> source's own two-way **preference / circumstance** language is flagged as the
> source's, not adopted.
> Tags: **explicit-in-source** / **derived-by-analogy** / **not-established**;
> uncertain metadata marked `[verify]`.

---

## 0. Metadata

- **BibTeX key:** JacquetJiaThoresen2026 `[verify exact key against your .bib]`
- **Authors:** Laurence Jacquet (CY Cergy Paris Université and THEMA); Zhiyang Jia (Research Department, Statistics Norway); Thor O. Thoresen (Research Department, Statistics Norway; Norwegian Fiscal Studies, Department of Economics, University of Oslo).
- **Year / outlet:** 2026, CESifo Working Papers No. 12418, January 2026.
- **DOI/URL:** SSRN `https://ssrn.com/abstract=6112587`. No journal DOI yet (working paper).
- **PDF filename:** `Jacquet_et_al_2026_How_Much_Does_Responsibility_Matter_in_Fairness_Measurement.pdf`.
- **JEL:** H31, I31, J22, C25. **Keywords:** money metric utility, fairness, tax reform, structural labor supply model.
- **Tier:** T1A (core; this is the single closest cousin of the JMP — same estimator family, same money-metric apparatus, overlapping author set with the companion theory paper, and Maniquet appears in the acknowledgements).
- **JMP block(s) served:** estimation; welfare; normative-interpretation; opportunity-mechanism (**access only**); motivation. **Not** decomposition (no inequality decomposition is performed); **not** ability (no structural wage technology); **not** data-infrastructure for France (Norwegian register/survey merge).

**Boundary note carried from the start.** Maniquet is thanked in the acknowledgements; this paper is **not** the companion Haydar–Maniquet theory paper and must never be cited as such. It is also not the JMP. It is the empirical paper whose method the JMP most directly extends and differentiates from.

---

## 1. One-paragraph relevance to my JMP

This is the empirical template the JMP is built against and must out-position: it estimates the same **latent-jobs / "job choice" model** (Dagsvik 1994; Dagsvik and Jia 2016) on a cross-section of couples, and it produces **money-metric** welfare figures by inverting the household's own utility to money (McFadden 1999 simulation). It speaks directly to the **preference** channel (its Box–Cox utility block = my $v$) and to the **access** channel (its $\log Q(h)$ hours-availability term and the education-scaled job-availability measure $\theta_F$ = my hours/access sub-block of $g$). It does **not** instantiate my **ability** channel — wages are taken as observed data, not modelled as a structural wage technology — and it performs **no inequality decomposition**: it compares two welfare-*change* measures (standard CV vs. a preference-neutralised CVcirc, with a Conditional-Equality cross-check) and reads off *where on the income distribution* they diverge. For my purposes its single most load-bearing contribution is the **reference-preference neutralisation device** (set taste-shifters to sample medians; impose a common error term) and the demonstration that, in a Norwegian reform, neutralising preference heterogeneity barely moves the welfare distribution except at the very top. It is the paper I cite for the estimator and the money-metric inversion, and the paper I must explicitly distinguish from on four axes: **level vs. change**, **two-measure comparison vs. Shapley decomposition**, **preference-neutralising reference vs. preference-respecting equivalent income**, and **bundled circumstances vs. an access/ability split**.

---

## 2. Data and setting

- **Country / unit:** Norway; **married couples** (with or without children), treated as **unitary** (harmonised joint decision over both spouses' labour supply, common budget). **Explicit-in-source.**
- **Year / dataset:** Cross-section, **2015**. Built by merging, on personal identification numbers, the **Labour Force Survey** (Statistics Norway 2024) and the **Income and Wealth Statistics of Households** (Statistics Norway 2019). The LFS supplies actual and formal working time for main/secondary jobs plus background variables including demographic characteristics and **occupation**; conditional on participation, respondents self-classify as self-employed or employee. **Explicit-in-source.**
- **Sample size:** **1,594 couples** (Table C2). **Explicit-in-source.** Summary statistics in Table C1.
- **Sample restrictions:** couples excluded if one adult has self-employment income > NOK 115,000 (2015 prices); excluded if weekly hours > 80 or wage outside NOK [70, 600] (2015 prices). A person "works" if ≥ 1 hour/week. Hours = formal hours in main + second job. Nominal hourly wage = labour income / total annual hours. **Explicit-in-source.**
- **Budget-set construction:** disposable income obtained via the **LOTTE** family of tax-benefit microsimulation models (Jia et al. 2024); piecewise-linear, possibly non-convex budget sets. **Explicit-in-source.**

**Transport to my setting.** Partial. Same broad object (couples, cross-section, microsimulated nonlinear budget), so the *estimator and welfare apparatus transport cleanly*. But the **data infrastructure does not transport**: this is an admin/survey **register merge with personal IDs**, not EUROMOD on EU-SILC. **Features I do not have that they rely on:** (i) a clean **employee/self-employed** self-report (they exclude high self-employment couples on it); (ii) **occupation in the data** as a usable background variable (they have it but, note §3, do **not** use it in the model); (iii) precise formal-vs-actual hours from an LFS. They have **no panel, no external opportunity instrument** either — so on the identification axis they are in the same cross-sectional boat as my France pooled 2015–2017 EUROMOD sample (§8).

---

## 3. Model and objects (mapped object-by-object to mine)

| My object | Theirs | Match? |
|---|---|---|
| Latent-jobs choice set $\mathcal C_i$ | Latent jobs $z=1,2,\dots$ market, $z=-1,-2,\dots$ non-market; set $B(h)$ of jobs at hours $h$, size $Q(h)$ unobserved | **Same family** (explicit). Theirs is a fixed discrete **hours grid** (56 couple alternatives), not sampled draws. |
| Preference utility $v$ (Box–Cox over $c,\ell$, demographic shifters, gender) | $u(C,h_F,h_M)$, Box–Cox in consumption and leisure with leisure shifters (age, children) and a leisure interaction $\alpha_{15}$ (Eq. 4.10) | **Direct match** (explicit). Their taste-shifters = my demographic shifters. |
| Opportunity density $g$ | $\log Q_F(h_F) + \log Q_M(h_M)$ in the indirect utility (Eq. 4.3); $Q(h)=\theta\,g(h)$, $g$ the **opportunity density of hours**; $\theta$ = relative size of the job set vs. non-work | **Partial match.** Theirs is an **access/hours** density only. |
| **access** sub-block (hours/employment/region/year/occupation) | hours-availability density $g(h)$ (uniform off-peak, with **part-time and full-time peaks**) + $\theta_F$ scaled by **education**: $\log\theta_F = \gamma_{F1}+\gamma_{F2}S$ (Eq. 4.5); $\theta_M$ normalised to 1 (males ≈ all employed) | **access match** (explicit). No region/year/occupation in their access block. |
| **ability** sub-block (structural wage technology: returns to education/experience, residual $\sigma$) | **Absent.** Wages are **observed data** (income/hours), entering only the budget map $C=f(\cdot)$. A reference wage appears only in the **unimplemented** CVpref (Appendix D.2) | **No match.** This is my channel, not theirs (see §5, §13). |
| occupation as access (`loc4`) | Occupation is **in the data but not in the model** — not in utility, not in $g$, not in the wage | **No match.** They neither use occupation nor conflate it with industry. **Not-established** that occupation does anything structural here. |
| EUROMOD disposable income $c_{ij}$ | LOTTE disposable income $C=f(h_Fw_F,h_Mw_M,I)$ | **Functional match**, different microsimulator. |

**Does any attribute enter BOTH utility and the opportunity mechanism?** **No** (explicit). Hours enter both *as an argument* ($u$ depends on $h$; $g$ is a density over $h$), but this is the standard latent-jobs separation — preferences value the hours, the opportunity density governs their **availability** — not a double-loading of a covariate. Wage enters only the budget; occupation enters nothing. No identification-by-double-entry issue arises, and none is claimed.

**Key structural reading.** Their indirect utility (Eq. 4.3) cleanly splits into a **preference part** $u(\cdot)+\eta$ and a **circumstance part** $\log Q_F+\log Q_M$. In my vocabulary the circumstance part is **access only**; their "circumstances" therefore equal my **access**, *not* my access + ability, because the wage (my ability locus) is not inside their $g$. This is the single most important mapping fact in the paper for me.

---

## 4. Estimation method

- **Estimator:** Maximum Likelihood in a **conditional logit**, choice probability Eq. 4.4. Log-likelihood Eq. 4.11: $\sum_i \log\varphi(h_{iF},h_{iM}\mid w_{iF},w_{iM},I_i)$. **Explicit.**
- **Choice set:** **fixed discrete grid** — 56 couple alternatives = **7 male × 8 female** options (males have 7 because there is no data support for a male non-market alternative). **Not** sampled alternatives. **Explicit.**
- **Proposal / sampling density:** **none** — there is no sampling-of-alternatives step (see §4b). **Explicit.**
- **What pins preferences vs. opportunities apart:** functional form + the observed **bunching at part-time/full-time hours peaks** (which identifies the opportunity density's shape) + the joint hours density $\varphi$; $\theta_F$ identified off **education** variation (Eq. 4.5); $\theta_M$ normalised to 1; $Q_F(0)=Q_M(0)=1$ normalisation. They defer to **Dagsvik and Jia (2016)** for the formal cross-sectional identification conditions. **Explicit.**
- **Numerics / starts / multistart:** not described in detail `[verify — no multistart or starting-value protocol stated in the main text]`.
- **Fit:** $N=1{,}594$; log-likelihood $-3070.9$; McFadden's $\rho^2=0.52$ (Table C2). **Explicit.**

**Verdict: reusable for my RURO/JAX pipeline? Partly.** The **likelihood and the indirect-utility decomposition (Eq. 4.3–4.4) are directly reusable** as the conceptual backbone (my model is the same family). **Not reusable as-is:** their *estimation* uses a small fixed grid with no proposal correction; my pipeline uses **sampled alternatives with a per-row $-\log\pi$ correction** at 901 (couples) / 101 (singles) resolution. Their grid approach is the older Dagsvik–Jia implementation; my sampling-plus-correction is the scaling step they do not take. Reuse the model, not the choice-set machinery.

---

## 4b. Proposal / sampling-of-alternatives correction

**Not present in estimation.** Estimation is over a **complete fixed grid** of 56 alternatives, so there is no McFadden-style sampling correction and no $-\log\pi$ term in the likelihood. The structural analogue of an "opportunity weight" is the **estimated** $\log Q(h)=\log\theta + \log g(h)$ term, but this is a *model primitive jointly estimated with preferences*, **not** a sampling instrument to be divided out. **Explicit / derived-by-analogy.**

**On the welfare side, simulation enters but not as a proposal.** CV is computed by **drawing Gumbel error terms** $\{\eta_i^k(h)\}$ and solving Eq. (D.1) numerically per draw (McFadden 1999). These are **shock draws over a common grid**, not importance draws over an individualised proposal. There is therefore **no individualised proposal** here at all — neither wage-conditioned nor occupation-conditioned — because wages are fixed data and occupation is unused. **Explicit.**

**Relation to my proposal-individualisation concern.** Direct contrast, useful for my §5.3 audit: my proposal is **partly individualised** (wage mean $\mu_i=X_ib+\delta_{\text{occ}}[\text{loc4}_i]$ and occupation stratum condition on $x_i$; hours/employment common). JJT have **no proposal individualisation** because their two high-dispersion channels (wage, occupation) are simply not stochastic in their model. So they cannot illuminate the well-conditioning of importance sampling — they don't importance-sample — but they **do** confirm that the *welfare* expectation, when shocks are simulated, requires a per-draw one-dimensional solve. My analytic-in-shocks log-sum (§6b) is the efficiency improvement over exactly their D.1 simulation.

---

## 5. Opportunity mechanism  [most important — split by channel]

The mechanism is a **density over hours alternatives**, scaled by an aggregate availability measure. Explicitly (Eq. 4.3–4.5, Appendix B):

- The latent jobs $z$ at hours $h$ form a set $B(h)$ of unobserved size $Q(h)$. Taking the max over $B(h)$ of i.i.d. Gumbel taste shocks (Appendix B derivation) yields an indirect utility shifted by $\log Q(h)$ — i.e. **more available jobs at $h$ ⇒ higher choice value at $h$**. This is the entire opportunity channel.
- $Q(h)=\theta\, g(h)$ with $g(h)$ the **opportunity density of hours** (share of available jobs at $h$) and $\theta$ the **size of the market opportunity set relative to non-work**. Normalisations: $Q(0)=1$.
- $g(h)$ is **uniform for nonstandard hours with a part-time peak and a full-time peak**, matching the observed hours distribution. **Explicit.**

**Mapping to my three sub-objects.**
- **access (hours / participation / job availability):** **YES, this is the whole mechanism.** Hours availability via $g(h)$ with the two peaks; aggregate participation/availability via $\theta$. Females: $\log\theta_F=\gamma_{F1}+\gamma_{F2}S$ — **job availability rises with education** (their interpretation). Males: $\theta_M$ **not identified**, normalised to 1 (near-universal male employment). **Explicit.**
- **ability (wage technology):** **ABSENT from the mechanism.** Wages are observed and enter only the budget. There is **no** structural return to education/experience inside $g$, and **no** residual productivity dispersion $\sigma$. The closest object is the **reference wage** $\bar w$ of the **CVpref** alternative (Appendix D.2), where they explicitly reason that "abilities predominantly result from circumstances beyond the individual's control" and so a common reference wage neutralises ability-driven inequality — **but CVpref is defined and then left for future research, not implemented.** So ability exists here only as an *unexecuted* neutralisation, not as an estimated channel. **Explicit (that it is deferred).**
- **occupation:** treated as **nothing** — observed in data, absent from the model. **No** sector/industry conflation to flag, because occupation is simply unused.

**Functional form:** opportunity density piecewise-uniform with two estimated peak parameters per gender (Table C2: male full-time 2.8936, female full-time 1.5027, male part-time −0.1512, female part-time −0.0451), plus $\theta_F=\exp(\gamma_{F1}+\gamma_{F2}S)$ with $\gamma_{F1}=-2.9199$ and $\gamma_{F2}=0.1653$ (SE 0.389 — **the education→availability slope is statistically insignificant**; flag this, §9).

**What the omission of an ability channel costs my access/ability/preference decomposition.** A great deal, and this is exactly why my paper exists. By folding all of "circumstances" into **hours/job availability** and treating wages as data, JJT **cannot separate access from ability** — they have only a two-way preference/circumstance cut where "circumstance" = access. My added structural wage technology (occupation-conditioned wage draws, returns to education/experience, $\sigma$) is what lets the **ability** dimension exist as a distinct, estimable channel. Cite JJT as the paper that *bundles* the opportunity side; position my ability/access split as the resolution of that bundling.

---

## 6. Welfare object — and its place on my $W^1$–$W^6$ map

**What they compute.** Three objects, all **welfare *changes* of a tax reform**, not welfare levels:
1. **CV** — standard compensating variation: the income that equates max utility before and after the reform under the household's **own** preferences (Eq. 4.12; McFadden 1999). Money-metric, **own-preference-respecting**, defined over the **constrained** latent-job set (it carries the $\log Q$ terms — Eq. 4.12 explicitly includes $\log Q_{iF}+\log Q_{iM}$). CV is **stochastic** in the $\eta$ draws.
2. **CVcirc** — circumstance-CV: identical computation but with the **deterministic utility $\bar u$ and the random term $\bar\eta$ set to common reference values** (taste-shifters — gender, age, children — at sample medians; $\alpha_1$–$\alpha_4$ common), so "households differ only in circumstances" (Eq. 4.13, Appendix D.2). **Preference heterogeneity is neutralised.**
3. **$\Delta$CE** — change in the **Conditional Equality** criterion (Fleurbaey 2008): max **reference-preference** utility on a **hypothetical linear equivalent budget** (slope = wage, lump-sum tax $T$ as intercept), Eq. 3.2–3.3, following Carpantier and Sapata (2016); $\Delta\text{CE}=\text{CE}_1-\text{CE}_0$. Reference preferences again at medians.

**Discrete-choice subtleties handled:** CV is the **conditional indirect utility of the most-preferred job within the latent set** (so it is a *constrained-choice* CV); the $\eta$ terms are held fixed pre/post (the standard McFadden assumption), and because the pre- and post-maxima need not fall on the same alternative, CV does **not** collapse to a closed form and is obtained by simulation. **Ex-post element:** for CE they "do not exploit information about actual choices" — they draw shocks and assume the household picks the utility-maximising alternative — so the CE construction is itself an **ex-ante-by-simulation** object over the grid, though it conditions the equivalent budget on the household's own wage. **Explicit.**

**Locating the paper on my $W^1$–$W^6$ map.** Handle with care; the correspondence is **partial and derived-by-analogy**, and the level/change mismatch means *none of these is literally a $W^k$*.
- **Standard CV** respects own preferences **and** own circumstances (own wage, own $Q$) — "own everything." Its *stance* is closest to my **Full-Responsibility** corner ($W^2/W^3$): nothing is neutralised. **Derived-by-analogy**, with the caveat that it is a *change* and that all my $W^k$ read attained $V_i$ whereas CV reads a utility *difference*.
- **CVcirc / CE** neutralise **preferences** (set to a reference), leaving circumstances individual. This does **not** map to any single $W^k$, because my family holds **preferences as the responsibility object across all six** and varies *which circumstance dimension* (Ind-$y$ / pay vs. Ind-$A$ / set) is compensated. CVcirc varies the *preference* axis, which my menu does **not** traverse. The honest statement: **CVcirc/CE belong to the reference-preference / Conditional-Equality tradition, which is a different normative device from my preference-respecting equivalent-income family.** My $W^k$ use the household's **own** indifference map; CVcirc/CE substitute a **common reference** map. (`JMP_welfare_spec_v5.md` §1.1 is explicit that my $W^k$ invert the *own*-utility map "never by a closed-form shortcut that would bypass the household's preferences" — the exact opposite design choice from CVcirc.)
- **CVpref** (their unimplemented dual, Appendix D.2) neutralises **circumstances** instead (reference wage $\bar w$, reference opportunity $\bar Q$). *This* is the object whose **stance** is nearest my compensation corner / my $W^5$ (compensate the set; with reference wage, also compensate pay). But it is **not-established empirically** — defined, deferred, never computed.

**Verdict:** the **estimator and the CV inversion are directly adaptable**; the **CVcirc/CE objects are conceptually adjacent but normatively distinct** from my family (reference-preference vs. preference-respecting) and are **changes not levels**; treat them as the *contrast case*, not as instances of $W^1$–$W^6$.

---

## 6b. Inclusive value and money-metric inversion

- **Inclusive value:** Yes, partially and analytically — the $\log Q(h)$ terms in Eq. 4.3 are precisely the **expected-maximum (log-sum) over the latent jobs at a given hours point**, derived in Appendix B from the Gumbel max. So the inclusive value *within* an hours cell is closed-form. **Explicit.**
- **But welfare is obtained by simulation, not by a closed-form log-sum.** Because CV is **nonlinear in income**, no closed form exists (they cite Dagsvik and Karlström 2005 for the distribution/moments); they **draw $K$ Gumbel vectors and solve a one-dimensional equation per draw** (Eq. D.1), then average. **Explicit.**
- **Money-metric inversion:** Yes — CV is a **one-dimensional solve** that equates pre- and post-reform maximised utility under own preferences (Eq. D.1); CE solves for the lump-sum tax $T$ (Eq. 3.2). Both are own-/reference-utility inversions to a money figure, **not** closed-form shortcuts that bypass preferences. **Explicit.**
- **Expectation over shocks: by simulation**, not analytic. **Explicit.**

**Relation to my integrator.** This is the cleanest single point of methodological differentiation. My welfare layer takes the **expectation over the extreme-value shocks analytically** (the ex-ante inclusive value is the closed-form expected maximum; `JMP_welfare_spec_v5.md` §1.1: "the welfare layer requires no shock draws and no simulated argmax"), and inverts by a one-dimensional bracketing root-solve on the **importance-sampled** log-sum. JJT do the inversion by **per-draw simulation over a fixed grid**. Same money-metric inversion logic; **my analytic-in-shocks + importance-sampling step is the efficiency and the ex-ante-access improvement over their D.1 simulation.** Cite D.1 as the simulation baseline I improve on.

---

## 7. Inequality / decomposition content  [three-way where relevant]

**There is no inequality index and no decomposition in this paper.** No Gini/MLD/Theil/Atkinson; no Shapley, Shorrocks, factor-component, subgroup, RIF, or Owen-grouped decomposition. **Explicit (by absence).**

What they do instead:
- Report **means and standard deviations** of the three welfare-change measures (Table 1): the SD is the only dispersion object, used informally to say preference-neutralisation "slightly reduces the spread" (5,458 → 5,188 NOK under CV → CVcirc).
- Report a **rank-transition matrix** across quintiles, CV vs. CVcirc (Table 2): 71–93% stay in the same quintile.
- Plot welfare effects **by income decile** (Figures 4–5) and identify the decile where CV and CVcirc diverge.

The conceptual cut is **two-way** and, in the source's own words, **preference vs. circumstance** — and it is operationalised as a **comparison of two measures**, not as an additive attribution. The "amount that responsibility matters" is *defined* as the gap between CV and CVcirc, not as a component share.

**Verdict: not reusable as a decomposition method.** To serve my **three-way access / ability / preference Shapley–Shorrocks** split (anchored on $W^3$ for total source-composition and the $W^5$/$W^1$ duals for the access/ability faces) it would need three extensions, each substantial: **(i)** move the object from welfare **change** to welfare **level**; **(ii)** replace the two-measure gap with a genuine **order-independent additive decomposition** of an inequality index; **(iii)** **split circumstances into access and ability**, which their model cannot do because ability (wages) is not a modelled channel. The paper is the *motivation* for a decomposition ("how much does responsibility/preference matter") executed by a cruder instrument; my decomposition is the instrument it lacks.

---

## 8. Identification and the separation of preferences from opportunities  [strict]

**What separates tastes from constraints.** The split rests entirely on **functional form + distributional assumptions + the shape of the observed hours distribution**:
- Preferences enter through the Box–Cox $u(\cdot)$ and its taste-shifters; constraints enter **only** through $\log Q(h)$. The two are separately identified because the opportunity density is pinned to the **bunching at part-time and full-time peaks** (a feature preferences alone, on a smooth Box–Cox, would not generate), while the smooth trade-off identifies tastes.
- $\theta_F$'s level and education slope are identified off cross-sectional **education** variation (Eq. 4.5); $\theta_M$ is **conceded non-identified** and normalised (a candid admission worth citing).
- They defer the formal conditions to **Dagsvik and Jia (2016)**: latent-jobs identification from **cross-sectional micro data** under the Gumbel/Luce structure. **Explicit.**

**Can they separate ability from access?** **No.** Within "circumstance" there is only access (hours/job availability); wages are data, so there is no ability sub-model to identify. The would-be ability neutralisation (CVpref reference wage) is deferred. **Explicit / not-established.**

**Transport to my France pooled cross-section.** **Yes, and this is the backbone of my identification defence.** JJT identify the preference/opportunity separation **without a panel and without an external instrument** — exactly my constraint — relying on parametric/functional-form identification plus the observed hours distribution. This is precisely the structure my baseline uses, and my baseline is additionally **certified by synthetic recovery** rather than in-sample fit. So I can write: *the separation of preferences from opportunities in a cross-section is established practice in this literature (Dagsvik–Jia 2016; Jacquet–Jia–Thoresen 2026); my contribution is (a) to push it to a three-way access/ability/preference split by adding a structural wage channel, and (b) to discipline the resulting specification by a synthetic-recovery gate rather than in-sample fit.* This is also my answer to the "your decomposition is mechanical" referee: the *same* parametric identification underwrites a published, peer-relevant CV/CVcirc exercise; what is new in mine is the channel split and the recovery certification, not the act of separating tastes from constraints in a cross-section. **Do not soften: the identification is parametric, and I should own that rather than overclaim nonparametric content.**

---

## 9. Key results and magnitudes

- **Average welfare effects (Table 1):** CV = **NOK 18,384** (SD 5,458); CVcirc = **NOK 18,677** (SD 5,188); $\Delta$CE = **0.356** (SD 0.108, different unit/scale). Neutralising preferences **raises** the mean slightly and **lowers** the SD by ~5%. **Explicit.**
- **Rank stability (Table 2):** 71–93% of households stay in the same income quintile across CV vs. CVcirc; bottom and top quintiles most stable (84.9% and 92.5%). **Explicit.**
- **Across the distribution (Figure 4):** CV and CVcirc track each other up through decile 9 (~NOK 25,000 gain at decile 9, where disposable income ≈ NOK 1 million), then **drop in decile 10**; **decile 10 is the only group where the two diverge significantly.** **Explicit.**
- **Mechanism:** under CVcirc, women who initially had stronger leisure preferences are assigned **lower returns to leisure**, so **female labour supply rises across the distribution**; male labour supply is unchanged except in the top decile, where it **falls**. The top-decile welfare divergence is driven by **women's** re-optimised labour supply, where pre-reform female hours were low. **Explicit.**
- **$\Delta$CE robustness (Figure 5):** $\Delta$CE closely mirrors CVcirc across deciles 1–9; mild divergence at the top (smaller gains), interpreted as methodological noise. **Explicit.**
- **Estimation (Table C2):** $N=1{,}594$; logL $-3070.9$; $\rho^2=0.52$; consumption exponent $\alpha_1=0.6694$; female leisure exponent $\alpha_3=-1.1490$; male leisure exponent $\alpha_4=0.2309$ (SE 0.308 — **imprecise**); leisure interaction $\alpha_{15}=1.2111$ (SE 0.863 — **imprecise**); $\gamma_{F2}=0.1653$ (SE 0.389 — **education→availability insignificant**). **Explicit.**

**Benchmark for my plausibility checks.** The headline economic message — **neutralising preference heterogeneity barely changes the welfare distribution except at the very top** — is a (weak, change-based, single-reform, Norway) prior that the **preference channel contributes modestly** to welfare-effect dispersion, with action concentrated among high-income women's labour supply. If my France **level** decomposition returns a small preference component and a larger opportunity component overall, JJT is consistent corroboration; but it is a *change* in a different country, so it bounds plausibility only loosely. Their ~5% SD reduction from full preference-neutralisation is the closest single number to compare against my preference component — note that mine should be **larger in principle** because I decompose a *level* and split out *access*, but do not assert this until computed.

---

## 10. Estimators, theorems, or formal results

No theorems. Key formal objects (LaTeX near-verbatim; **explicit**), with reuse verdicts:

1. **Indirect utility with opportunity terms (Eq. 4.3):**
$$V(h_F,h_M,I)=u\big(f(h_Fw_F,h_Mw_M,I),h_F,h_M\big)+\log Q_F(h_F)+\log Q_M(h_M)+\eta_{h_F,h_M}.$$
*Technique:* max of i.i.d. Gumbel over $B(h)$ ⇒ a $\log Q$ shift, $\eta$ retains Gumbel (Appendix B). **Reuse: yes** — this is my model's core identity.

2. **Choice probability (Eq. 4.4):**
$$\varphi(h_F,h_M)=\frac{Q_F(h_F)Q_M(h_M)\exp\big(u(f(\cdot),h_F,h_M)\big)}{\sum_{x,y}Q_F(x)Q_M(y)\exp\big(u(f(\cdot),x,y)\big)}.$$
**Reuse: yes** as the likelihood kernel; my version replaces the full-grid sum with a sampled-alternatives sum plus $-\log\pi$.

3. **Opportunity scaling (Eq. 4.5):** $\log\theta_F=\gamma_{F1}+\gamma_{F2}S$. **Reuse: maybe** — an education-as-access shifter; relevant to my §6.3 "education-as-access" deferred robustness cut, but note its insignificance here.

4. **Box–Cox utility (Eq. 4.10)** in $(C-C_0)$ and leisure $L_F,L_M$ with a leisure interaction $\alpha_{15}$ and demographic shifters in $\beta_F,\beta_M$. **Reuse: yes** as a specification template (my preference block is the same family).

5. **CV definition (Eq. 4.12)** and **CVcirc (Eq. 4.13):** constrained-choice CV with $\log Q$ terms; CVcirc replaces $u_i,\eta_i$ by common $\bar u,\bar\eta$. **Reuse: yes as templates**, but for *changes*; my levels need the reference-package inversion, not a pre/post-reform difference.

6. **CE (Eq. 3.2–3.3):** lump-sum tax $T_i$ implicitly defined by $u(c_i,h_i;\gamma_i)=\max_h\{u(c,h;\gamma_i)\mid c\le w_ih-T_i\}$; then $\text{CE}_i=\max_h\{\bar u(c,h;\bar\gamma)\mid c\le w_ih-T_i\}$. **Reuse: maybe** — relevant to my secondary "ex-post chosen-alternative CE" cross-check (`JMP_welfare_spec_v5.md` D3), but their CE uses reference preferences whereas my correction-free CE cross-check is own-preference.

7. **CV simulation (Eq. D.1)** — per-draw one-dimensional solve over $\eta$. **Reuse: as the contrast** my analytic-in-shocks integrator replaces (§6b).

**Discrepancy to flag (`[verify]`).** The subsistence consumption $C_0$ is stated as **NOK 64,000** in the §4.2.3 text but **57,000** in Table C2; $L_0=5{,}110$ hours is consistent across both. Treat $C_0$ as `[verify]` before quoting a number.

---

## 11. Robustness and specification sensitivity

- **Reference-value sensitivity:** medians of taste-shifters replaced by **10th/90th-percentile** values — results "remain robust." **Explicit.** (Directly relevant to my reference-state robustness in the decomposition.)
- **CV aggregation:** two routes — per-individual mean across draws (their choice) vs. pooling all draws across observationally identical groups; they use the former. **Explicit.**
- **Choice-set size:** fixed at 56; **not varied.** No effective-sample-size / draw-count study (because estimation is not simulation-based). **Number of welfare draws $K$ not stated `[verify]`.**
- **Ability/access boundary:** **not stress-tested** — there is no ability channel; the CVpref reference-wage neutralisation that would probe it is **deferred to future research.** **Explicit.**

**What this tells me to stress-test.** (i) My reference-state choice (their 10th/90th-percentile check is the template I should replicate across measures). (ii) My **draw-count / ESS stability** — JJT give me *no* guidance here (they don't importance-sample), which underscores that my §6 welfare-integration gate and the ESS diagnostic are genuinely my own contribution, not borrowed. (iii) The **ability/access boundary** is exactly the axis they could not test; my education-as-access vs. ability re-allocation (`JMP_project_state_v1.md` §6.3) is the test they flagged-by-omission.

---

## 12. What I can cite this paper for

- The **latent-jobs / "job choice" model** as the vehicle that "intrinsically" separates preferences (tastes over leisure) from circumstances (job opportunities) (Dagsvik 1994; Dagsvik and Jia 2016), and that the opportunity term is $\log Q(h)$ entering indirect utility additively (Eq. 4.3).
- The **bunching-at-peaks** empirical justification for an opportunity density (most jobs offer full-time or part-time schedules).
- The **reference-preference neutralisation device**: set taste-modifying variables to sample medians and impose a common error term to construct a preference-neutralised welfare measure (CVcirc).
- The **McFadden (1999) simulation** for CV in discrete-choice models nonlinear in income, and the **constrained-choice** reading of CV (it carries $\log Q$).
- The **link between a reference-preference CV and the Conditional Equality criterion** (Fleurbaey 2008; Carpantier and Sapata 2016), and that the two deliver "remarkably close" distributions empirically.
- The **unitary-couples** joint-choice assumption over $(h_F,h_M)$ as standard in this literature.
- The empirical finding (Norway, bracket-tax reform) that **preference heterogeneity matters little for the welfare distribution except at the top**.
- The candid **non-identification of $\theta_M$** and its normalisation, as precedent for honest normalisation choices.
- Money-metric utility's "revival" in the fair-allocation literature, with their cite chain (Fleurbaey 2008; Fleurbaey and Maniquet 2011, 2018; Bosmans–Decancq–Ooghe 2018; Schlee–Khan 2022) as a ready-made positioning paragraph.

---

## 13. What I should NOT cite this paper for  [overclaim risks]

- **Not** a three-way decomposition. It is a **two-measure comparison** along a **preference / circumstance** axis, and not even a formal additive decomposition. Never imply it decomposes inequality into access/ability/preference shares.
- **Not** a welfare **level** object. Everything here is a **welfare *change*** (CV of a tax reform). Do not present CV/CVcirc/$\Delta$CE as instances of my level equivalent-income family, and do not read their "spread reduction" as a level inequality result.
- **Not** an **access/ability** split. "Circumstance" here = **access (hours/job availability) only**; wages are data, ability is unmodelled, CVpref is deferred. Do not attribute a separate ability channel to this paper.
- **Not** an **occupation-as-access** result. Occupation is in the data but **unused** in the model. Do not cite for `loc4`/occupation opportunity, and do not say they "use occupation."
- **No industry/sector** content at all — so there is no sector/occupation conflation to inherit, but equally nothing to cite on industry.
- **Reference-preference ≠ preference-respecting.** CVcirc/CE substitute a **common reference** indifference map; my $W^1$–$W^6$ use the household's **own** map. Do not equate CVcirc with a preference-respecting equivalent income, and do not claim this paper computes my family.
- **Random-vs-deterministic:** the latent jobs are **latent** (count $Q(h)$ unobserved) but the opportunity sizes are **deterministic parameters**; the randomness is in the **taste shocks** $\eta$. This is **consistent** with my deterministic-opportunities stance — so cite it to *support* that framing, but do **not** describe their opportunities as "random."
- **Theory-paper boundary:** Maniquet is acknowledged, but this paper proves no axioms and characterises no welfare family. Never attribute the Haydar–Maniquet axioms/characterisation to it, and never read it (or my JMP) as a theory contribution.
- **McFadden (1999)** is used here for **welfare simulation**, not for **sampling-of-alternatives in estimation**. Do not cite it via this paper as a sampling correction.

---

## 14. Direct quotes worth citing

Deliberately minimal; verify each against the PDF before use. Page numbers are the printed paper pages.

- On the model's central virtue (p. 1): the job choice model holds features that *"mirror the distinction between preferences and circumstances."*
- On the definition of when responsibility matters (p. 1): *"Responsibility matters whenever the two metrics display different values."*
- On the structural split of indirect utility (p. 10): the opportunity part *"represents the labor market opportunities facing the household."*
- On the headline empirical result (p. 19, summarising): preferences may *"not matter so much in fairness measurement, except at the very top."*

(If more quotation is needed, pull it directly from the PDF rather than from this file — I am keeping verbatim text minimal here on purpose.)

---

## 15. Open questions and risks for my draft

- **Simulation vs. analytic integration error.** Their CV is simulated over $K$ Gumbel draws with no stated $K$ or convergence diagnostic (`[verify]`). My analytic-in-shocks + ESS-gated importance sampling is the disciplined alternative — but it means *I* carry the burden of demonstrating integration adequacy (the §6 three-part gate), since this literature offers no off-the-shelf standard. Frame my ESS diagnostic as filling that gap.
- **Normative basis of the reference.** "Median preferences as the responsibility reference" is asserted, not derived; their 10th/90th-percentile robustness is reassuring but does not address *why* the median. My family-of-measures design sidesteps this by reporting a *spectrum* rather than committing to one reference — a defensible positioning move against the "arbitrary reference" critique.
- **Bundled circumstances.** Their inability to separate access from ability is the gap my paper fills, but it also warns me: **is the structural wage technology separately identified from preferences in a cross-section?** JJT avoid the question by not modelling wages; I cannot. This is the sharpest identification risk for my ability channel and must be defended (synthetic recovery of the wage block, not in-sample fit — consistent with my certification discipline).
- **External validity of "responsibility matters only at the top."** Reform-specific and Norway-specific (individual taxation, dual income tax). My France level decomposition need not replicate it; do not anchor expectations to it.
- **Change vs. level confusion is a live referee risk.** Because JJT is my nearest neighbour and is a *change* paper, a reader may assume my decomposition is also reform-based. The intro must state the level/change distinction early and explicitly.

---

## 16. TL;DR for retrieval

Jacquet–Jia–Thoresen (2026) estimate the **same latent-jobs "job choice" model** (Dagsvik–Jia) on 1,594 Norwegian couples and compute **money-metric welfare *changes*** of a bracket-tax reform — standard CV vs. a **preference-neutralised CVcirc** (taste-shifters at medians) plus a Conditional-Equality cross-check — finding preferences barely move the welfare distribution except in the top decile. For my JMP it is the **estimator-and-inversion template** and the source of the **reference-preference device**, speaking to my **preference** and **access** channels but offering **no ability channel** (wages are data; CVpref is deferred) and **no inequality decomposition** (a two-measure comparison, not a Shapley split). It is the paper I cite for cross-sectional preference/opportunity identification and money-metric CV, and the paper I must distinguish from on **level-vs-change**, **decomposition-vs-comparison**, **preference-respecting-vs-reference-preference**, and **access/ability split vs. bundled circumstance**.
