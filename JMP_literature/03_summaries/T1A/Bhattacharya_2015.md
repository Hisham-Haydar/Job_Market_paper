# Bhattacharya 2015 — Nonparametric Welfare Analysis for Discrete Choice

> Extraction produced against `JMP_T1_exhaustive_extraction_prompt_v2.md`.
> Source of truth: the attached PDF (Econometrica 83(2), 617–649). Project
> anchors (`JMP_project_state_v1.md`, `JMP_welfare_spec_v5.md`) used only for
> relevance judgments. Page numbers refer to the journal pagination (617–649)
> printed on the PDF. Tags used below: **[explicit]** = stated in the source;
> **[analogy]** = derived by analogy to my JMP, not in the source;
> **[not-established]** = the source does not establish this; **[verify]** =
> metadata or detail I could not confirm from the PDF text.

---

## 0. Metadata

- **BibTeX key:** Bhattacharya2015 [verify — key not specified in source]
- **Authors:** Debopam Bhattacharya (Dept. of Economics, University of Oxford). [explicit, p. 649]
- **Year:** 2015 (manuscript received June 2014; final revision November 2014). [explicit, p. 649]
- **Outlet:** *Econometrica*, Vol. 83, No. 2 (March 2015), pp. 617–649. [explicit, p. 617]
- **DOI/URL:** 10.3982/ECTA12574. [explicit, p. 617]
- **PDF filename:** `Bhattacharya_2015_Nonparametric_Welfare_Analysis_for_Discrete_Choice.pdf`. [explicit, upload]
- **Tier:** T1A.
- **JMP blocks served:** welfare (money-metric EV/CV from discrete choice), identification (preference heterogeneity of unspecified dimension), estimation (the parametric MNL welfare integrator as a special case), motivation/defence (the "your decomposition is mechanical / driven by functional form" referee). It does **not** serve the opportunity-mechanism, decomposition, or normative-interpretation blocks directly. [analogy, on relevance]

---

## 1. One-paragraph relevance to my JMP

This is the canonical statement that money-metric welfare for discrete choice — the marginal distributions of equivalent variation (EV) and compensating variation (CV) under a price change — is point-identified as a closed-form functional of conditional choice probabilities, under arbitrary, unspecified-dimension preference heterogeneity and without specifying the utility functional form. [explicit, pp. 617–618] For my JMP it speaks almost entirely to the **preference** channel and to the welfare-object construction: it is the cleanest reference for the claim that my equivalent-income objects are *preference-respecting* and need not identify the full heterogeneity distribution to be well-defined, and it is my strongest defence against the referee who suspects my welfare numbers are artefacts of the Box–Cox functional form. Its negative result for ordered choice (and the link to Hausman–Newey set-identification for continuous choice) is the analytic backdrop for why a *discrete* unordered job menu with alternative-specific budgets is a favourable setting for welfare measurement. [explicit, pp. 617–618, 634] It says nothing about an opportunity mechanism, heterogeneous feasible sets, or a three-way decomposition; on those it is silent and must not be over-read.

---

## 2. Data and setting

**None.** The paper is purely theoretical/methodological; there is no empirical dataset, sample unit, or country. [explicit — the introduction frames the microdata setting abstractly (p. 617) and §2 onward is formal; the only computation is a worked multinomial-logit integrator (pp. 632–633)] The "setting" is an individual with observed income $Y$ and observed prices $P$ choosing a discrete good, with covariates suppressed for notational clarity ("the entire analysis should be thought of as implicitly conditioned on these observed covariates"). [explicit, p. 621]

**Transport to my France pooled 2015–2017 EUROMOD cross-section.** The *theory* transports: it is a single-cross-section, one-time-choice result and explicitly states this is the setup of all existing empirical welfare-analysis work it is aware of. [explicit, p. 634, "Sequential Choice"] What I do **not** have / what differs:

- The paper's welfare experiment is a **price change** for a good. My JMP has **no price change**: my welfare object is a *level* (an ex-ante equivalent income against a reference state), not a CV/EV for a counterfactual price movement. This is the single most important mapping caveat — see §6. [analogy]
- The paper requires **own-price and income variation** across observed units to trace the welfare CDF nonparametrically. [explicit, p. 631, "Computational Issues"] My budget variation comes from the EUROMOD tax-benefit map across alternatives, not from exogenous price variation; I do not attempt nonparametric identification.
- The paper assumes a **common, universal choice set** (same menu for every consumer). [explicit — §2.2 sets up a fixed alternative set $\{0,1,\dots,J\}$ common to all, p. 629] My JMP's defining feature is *heterogeneous feasible sets*; the paper has no analogue.
- No panel, no administrative match, no external instrument, no vacancy/offer data appears or is required (consistent with my own data constraints; the paper simply does not need them for its identification result). [explicit]

---

## 3. Model and objects (map object-by-object to mine)

| Their object | Their definition (source) | My object | Match? |
|---|---|---|---|
| Choice set $\{0,1,\dots,J\}$, alternative-specific prices $p_j$ | Mutually exclusive discrete alternatives, common to all consumers (p. 629) | latent-jobs set $\mathcal C_i$ | **Partial.** Both are unordered discrete menus; theirs is universal/common, mine is household-specific and feasibility-constrained. [analogy] |
| Deterministic-plus-heterogeneity utility $U_j(Y-p_j,\eta)$ | Continuous, strictly increasing in numeraire; $\eta$ of unknown dimension/distribution, arbitrary entry (Assumption 1, p. 622; Assumption 2, p. 630) | preference utility $v$ (Box–Cox in $c,\ell$, taste-shifters) | **Object-analogous, assumptions much weaker.** Theirs imposes only monotonicity+continuity in the numeraire; mine is a parametric Box–Cox. [explicit for theirs; analogy for the map] |
| Budget: $W + PQ = Y$, consumption $= Y - p_j$ | Numeraire after discrete purchase (p. 621) | EUROMOD disposable income $c_j = $ `ils_dispy_real` at alternative $j$ | **Analogous role, different map.** Theirs is linear price-subtraction; mine is the nonlinear tax-benefit transform. [analogy] |
| Opportunity / availability mechanism | **None.** Universal choice set; all welfare variation is preference heterogeneity. (p. 632, summary; §2.2 setup) | opportunity density $g$ (hours / wage-ability / market / occupation-access) | **No analogue in the source.** [explicit — the paper has no $g$] |

**Separation of hours / wage(ability) / market / occupation channels:** absent. The paper has no opportunity mechanism, hence no channel split. [explicit]

**Does any attribute enter BOTH utility and an opportunity mechanism?** Not applicable — there is no opportunity mechanism, so the double-entry hazard I track does not arise here. The paper's only "all else" object is the heterogeneity vector $\eta$ inside utility. [explicit]

**Key structural difference to flag for my draft:** the paper's welfare object is generated by *price variation on a fixed menu*; mine is generated by *menu variation across households at fixed policy*. The identification logic (slice the population by reservation price; sweep prices to trace the CDF) does not port to my setting, where I am not perturbing a price. [analogy]

---

## 4. Estimation method

The paper is **about identification, not estimation**; a full inference treatment is deferred to a companion (Bhattacharya and Lee 2014, unpublished at the time). [explicit, pp. 632–633, "Inference"]

- **Likelihood / estimator:** none for the main results. The identification result expresses welfare CDFs as functionals of the structural choice probability $\bar q(\cdot,\cdot)$ (the "average structural function" in the sense of Blundell–Powell 2003). [explicit, p. 622] $\bar q$ is to be recovered by nonparametric regression of the buy indicator on price and income when these are independent of $\eta$ given covariates, or via control functions under endogeneity. [explicit, p. 622]
- **Choice-set construction:** fixed, common, finite menu; **no sampling of alternatives, no proposal density.** [explicit — §2.2]
- **Proposal / prior correction:** **none.** There is no sampling-of-alternatives step, so no $\log\pi$ correction exists or is needed. [explicit] (See §4b.)
- **Normalisation / scale:** in the parametric MNL example, utilities $U_j(a,\eta)=\beta_j a + \varepsilon_j$ with i.i.d. extreme-value $\varepsilon$ independent of price and income; the $\beta$'s are estimable by ML. [explicit, p. 632, eq. (23)] No explicit scale-normalisation discussion beyond the standard logit form.
- **Numerical method:** for the parametric case, the mean-welfare integral over the price interval is computed by averaging the estimated integrand over a uniform grid $r_k = p_{10} + \frac{k}{K+1}(p_{11}-p_{10})$. [explicit, pp. 632–633, eq. after (24)]
- **What pins preferences vs the opportunity mechanism:** not applicable — there is no opportunity mechanism to separate from preferences. The paper's separation problem is instead "welfare distribution vs heterogeneity distribution," and its result is that the former does not require the latter. [explicit, Remark 1 p. 627; Appendix example pp. 646–647]

**Verdict (reusable for my RURO/JAX pipeline?):** **No for the estimator** (there is none), **Yes for one downstream step** — the parametric MNL welfare integrator (eqs. 23–24, p. 632) is the textbook template for integrating a closed-form choice-probability expression over a price/parameter grid, and my analytic-in-shocks log-sum welfare core is a relative of it. But I do **not** reuse its nonparametric identification machinery, because I do not perturb a price and I do estimate a parametric structure. [analogy]

## 4b. Proposal / sampling-of-alternatives correction

**Not present.** The paper uses a fixed, common, fully enumerated choice set; there is no sampling of alternatives, no proposal density $\pi$, no individualised draw, and therefore no McFadden-style correction and no per-alternative $\log\text{prior}$. [explicit — confirmed by the absence of any sampling step in §§2.1–2.2 and by the direct enumeration in the MNL example, eq. (23)]

**Relation to my importance-sampling welfare integrator and proposal-individualisation concern:** the paper offers **no** guidance on the $-\log\pi$ correction, on partly-individualised proposals, or on effective-sample-size diagnostics, because it never samples alternatives. My proposal-correction obligations and my ESS finding are entirely outside this paper's scope; it should not be cited on them. [explicit absence → not-established for my purposes]

---

## 5. Opportunity mechanism  [MOST IMPORTANT]

**There is no explicit opportunity mechanism.** The choice set is a fixed, universal menu identical for every consumer; feasibility, offer probabilities, reservation-wage/participation restrictions, and circumstance-varying availability are **not modelled**. All cross-individual variation in welfare arises from preference heterogeneity $\eta$, with prices and income observed and (conditionally) independent of $\eta$. [explicit — §2 setup; summary p. 632]

Mapping to my three sub-objects:

- **access** (hours / market-participation / region / year / occupation offers): **absent.** [explicit]
- **ability** (wage technology; returns to education/experience; residual dispersion): **absent.** [explicit]
- **occupation as availability vs something else:** not present; no occupation object, hence **no sector/industry conflation risk** to flag. [explicit]

**Functional form of the mechanism:** N/A.

**Cost of this omission for my access/ability/preference decomposition.** Because the paper holds the feasible set fixed and common, it cannot — even in principle — separate access or ability from preference; everything it calls "heterogeneity" lives inside utility ($\eta$) and is, in my taxonomy, **preference** (with the important caveat that the paper's $\eta$ is *unrestricted* and could in a richer reading absorb what I would call ability/access if those were folded into utility). The paper is therefore a model of the *limiting case my JMP argues against*: the universal-choice-set world in which opportunity differences are invisible and would be loaded entirely onto tastes. This makes it useful **as the foil** for sub-question 1 ("do models without constrained opportunities overstate preference heterogeneity?") — Bhattacharya formalises welfare in exactly the world where that overstatement is unavoidable because no opportunity object exists. [analogy — the paper does not itself make this framing; it is my use of it]

---

## 6. Welfare object — and its place on my $W^1$–$W^6$ map

**Does it compute welfare?** Yes. The objects are the **marginal distributions of EV and CV** (and their means) for a discrete *price change* $p_0 \to p_1$. [explicit, Theorems 1–2, pp. 626, 631]

- **Money-metric?** Yes — EV and CV are income-compensation measures (units of the numeraire). [explicit, p. 617]
- **Equivalent income / equivalent variation?** It is **Hicksian** EV/CV for a price change, *not* an equivalent-income level against a reference state. [explicit] This differs from my object, which is an equivalent-income *level* against a normative reference set. [analogy]
- **Compensating / equivalent variation?** Both, defined as the income $S$ solving the indifference equations (5)–(6) for binary choice and (15)–(16)/(17)–(18) for multinomial. [explicit, pp. 624–625, 630]
- **Universal vs constrained feasible set?** **Universal** common set. [explicit] My welfare object is over a **constrained, household-specific** set. This is a fundamental mismatch. [analogy]
- **Reference price / preference / bundle / set:** the reference is the *post-change* (or pre-change) price situation under the consumer's **own** preferences; there is no reference-preference swap and no reference *set* — the menu is fixed. [explicit]
- **Discrete-choice subtleties:** handled via the composite-outside-option reduction — multinomial welfare for a price change in alternative 1 is reduced to a binary problem against $U^*(p_{-1},y,\eta)=\max\{U_0,U_2,\dots,U_J\}$, then Theorem 1 is applied (Theorem 2, Assumption 2). [explicit, pp. 629–631] Marshallian vs Hicksian: average EV equals the change in average Marshallian consumer surplus *even without quasilinearity*; average CV $\ge$ average EV for a normal good. [explicit, Corollary 1 and implications, p. 628] Integration over unobserved heterogeneity is the population integral $\int \cdot\, dF(\eta)$, and crucially does **not** require $F$ to be known or identified. [explicit, Remark 1, p. 627]
- **Ex-ante vs ex-post:** the welfare object is **per-type then aggregated** — for each $\eta$ the individual EV/CV is a deterministic number (Lemmas 1–2), and the paper reports the *marginal distribution* of that number across $\eta$. [explicit, pp. 625–626] There is **no inclusive-value / expected-maximum (log-sum) welfare core** in the main results: the extreme-value shocks appear only in the parametric MNL *example* (eqs. 23–24), not in the identification theorems. This is the opposite of my **ex-ante log-sum** stance. [explicit; contrast is analogy]

**Locating the paper on my $W^1$–$W^6$ family map.** The paper does **not** contain, reference, or correspond to my $W^1$–$W^6$ family, and contains no Ind-$y$ / Ind-$A$ classification. [explicit absence → **the source does NOT contain $W^1$–$W^6$**] Any correspondence is by analogy only: Bhattacharya's EV/CV use the consumer's *own* preferences and the *own* (universal) menu, so in spirit they sit at the **Full-Responsibility / own-everything** corner that my $W^2$/$W^3$ occupy — the consumer is evaluated against her own choice situation with no compensation of pay or set. But this is a loose analogy: his object is a *change* measure (a difference induced by a price move), not a *level* against a reference, so it is not literally any of my six. [analogy — explicitly flagged as not-established in the source]

**Verdict:** **Adaptable in spirit, not directly usable.** Usable as authority for "preference-respecting money-metric welfare is well-defined and computable without identifying the heterogeneity distribution." Not usable as a template for my ex-ante, reference-level, constrained-set equivalent income. [analogy]

## 6b. Inclusive value and money-metric inversion

- **Inclusive value (log-sum / expected maximum) as welfare core?** **No.** The identification results do not use a log-sum welfare core; welfare per type is obtained from the utility-indifference equations directly, then aggregated to a distribution. [explicit] The extreme-value structure enters only in the parametric MNL worked example (eq. 23), and even there the welfare *integral* is over the price grid, not an expected-maximum over shocks reported as the welfare number. [explicit, eqs. 23–24]
- **Money-metric by inversion of an own-utility map?** **Yes, conceptually, at the individual level.** The switcher's EV/CV is literally an inverse-utility solve: e.g. $S^{EV}=y-p_0-U_1^{-1}(U_0(y,\eta),\eta)$ for the switching type (Lemma 1, case ii), and the CV switcher solve $S^{CV}=U_0^{-1}(U_1(y-p_0,\eta),\eta)-y$ (Lemma 2, case ii). [explicit, p. 625] This one-dimensional inversion of an own-utility map is the **same kind of operation** as my bracketing root-solve of the own-utility map for $W^k$. [analogy] The difference: the paper inverts to recover a *price-change compensation*, then aggregates the closed form into choice probabilities; I invert to recover a *level* against a reference and integrate the shocks analytically via the log-sum.
- **Expectation over shocks analytic vs simulated?** In the nonparametric results there are no parametric shocks; the population integral over $\eta$ is collapsed analytically into choice probabilities $\bar q$ (no simulation). [explicit] In the MNL example the choice probability is the closed-form logit (analytic in the EV1 shocks), and only the price-grid integral is done numerically. [explicit, eqs. 23–24] This is **consistent in flavour** with my analytic-in-shocks importance-sampling inversion, and is a fair citation for "the expectation over the extreme-value shocks can be taken in closed form." [analogy]

---

## 7. Inequality / decomposition content

- **Inequality index:** **none.** The paper produces *welfare distributions* (CDFs of EV/CV) and their means, but applies **no** inequality index (no Gini, MLD, Theil, variance of logs, Atkinson). [explicit]
- **Decomposition rule:** **none.** There is no Shapley, Shorrocks, factor-component, subgroup, RIF, or regression decomposition. [explicit]
- **Counterfactual construction:** the only counterfactual is a *price change* $p_0\to p_1$; nothing is "equalised," "neutralised," or "zeroed out" across individuals in a decomposition sense. [explicit]
- **Order/path-independence/exhaustiveness:** N/A (no decomposition).

**Verdict (reusable for my three-way access/ability/preference Shapley–Shorrocks split?):** **No.** The paper supplies the *welfare distribution* that a decomposition would operate on, but contributes no decomposition machinery and is neither two-way nor three-way. To reach my three-channel split one would have to (i) replace the price-change CV/EV with my ex-ante reference-level equivalent income, (ii) introduce the opportunity object the paper lacks, and (iii) add the Shapley–Shorrocks counterfactual layer entirely from elsewhere (Shorrocks 2013 etc.). The paper is upstream of, and orthogonal to, the decomposition. [analogy]

---

## 8. Identification and the separation of preferences from opportunities  [STRICT]

**What the paper identifies and how.** The marginal distributions of EV/CV are point-identified as closed-form functionals of the conditional choice probabilities $\bar q(p,y)$ under a *single substantive assumption*: utilities are continuous and strictly increasing in the numeraire (Assumption 1 / Assumption 2). [explicit, pp. 622, 630] The identifying source is **own-price and income variation** that sweeps the population's reservation-price boundary: $\Pr\{S^{EV}\le a\}=1-\bar q(p_0+a,y)$ exploits that the fraction not buying at price $p_0+a$ is exactly the fraction with reservation price below $p_0+a$. [explicit, Theorem 1 + "Some Intuition," p. 626]

**Preferences vs opportunities:** the paper does **not** separate preferences from opportunities, because it has no opportunity object. What it *does* establish — and this is the load-bearing import for my identification note — is a different, stronger separation: **welfare distributions are identified without identifying the preference-heterogeneity distribution, or even its dimension.** [explicit, Remark 1 p. 627; Appendix worked example pp. 646–647, where two different $\eta_1$ distributions (uniform vs degenerate) produce identical choice probabilities and hence identical, point-identified welfare distributions, yet the dimension of $\eta$ is itself unidentified.]

**Ability vs access within the opportunity side:** N/A — no opportunity side. [explicit]

**Transport to my France pooled cross-section (no panel, no external instrument):** The reassuring transportable lesson is that **I do not need to identify my full heterogeneity distribution to have a well-defined, preference-respecting money-metric welfare object** — a direct shield for the "your welfare numbers are a functional-form artefact" referee. [analogy, grounded in explicit Remark 1 / Appendix] The non-transportable part: Bhattacharya's *nonparametric* identification needs continuous own-price variation that I do not have and do not invoke; my identification of the *structural* opportunity/preference split rests instead on parametric functional-form restrictions and is **certified by synthetic recovery, not in-sample fit** (per project state §3.7, §8). The honest statement for my draft is: Bhattacharya licenses the welfare-*object* well-definedness under unrestricted heterogeneity; it does **not** license my *structural separation* of access/ability/preference, which is a parametric identification claim the paper neither makes nor supports. [analogy]

**On the "mechanical decomposition" referee, with a caution.** The paper's Remark 3 (pp. 638–639) is a double-edged sword I must cite carefully: it shows that for *ordered* choice a parametric model would *appear* to point-identify the welfare distribution, but that this apparent identification is "driven entirely by functional form assumptions" and is "artificial." [explicit, p. 639] This is exactly the charge a referee could level at my parametric RURO decomposition. I can cite Bhattacharya to show I am *aware* of the functional-form-identification hazard and to motivate my synthetic-recovery certification as the answer; I must **not** cite him as having *cleared* parametric structural models of the charge — he does the opposite for the ordered case. [analogy — strict]

---

## 9. Key results and magnitudes

No empirical magnitudes (no data). The substantive results are analytic:

- **Theorem 1 (binary):** for a price rise $p_0\to p_1$, $\Pr\{S^{EV}\le a\}=1-\bar q(p_0+a,y)$ and $\Pr\{S^{CV}\le a\}=1-\bar q(p_0+a,y+a)$ on $[0,p_1-p_0]$. [explicit, p. 626]
- **Corollary 1:** $\mu^{EV}(y,p_0,p_1)=\int_{p_0}^{p_1}\bar q(p,y)\,dp$ = change in average Marshallian consumer surplus (no quasilinearity needed); $\mu^{CV}=\int_{p_0}^{p_1}\bar q(p,y+p-p_0)\,dp$. [explicit, p. 628]
- **Implications:** for a normal good, $E(S^{EV})\le E(S^{CV})$; deadweight-loss formulas for a per-unit tax follow. [explicit, p. 628]
- **Theorem 2 (unordered multinomial):** same CDF forms with $\bar q_1$ (composite outside option). [explicit, p. 631]
- **Negative result (ordered choice, $\ge 3$ alternatives, uniform unit price):** EV/CV distributions are **not** nonparametrically point-identified; linked to Hausman–Newey (2014) set-identification for continuous choice as a limiting case. [explicit, §3, pp. 634–639]
- **Appendix example:** heterogeneity dimension unidentified yet welfare distributions point-identified. [explicit, pp. 646–647]

Benchmarking value for my own opportunity-share / welfare-spread plausibility: **none** — no shares or spreads are reported. [explicit]

---

## 10. Estimators, theorems, or formal results

For each, statement (near-verbatim in LaTeX), assumptions, technique, reusability verdict.

**Assumption 1.** For each $\eta$, $U_0(a,\eta)$ and $U_1(a,\eta)$ are continuous and strictly increasing in $a$; inverses $U_j^{-1}(b,\eta)$ are uniquely defined. [explicit, p. 622]
*Technique/role:* the sole substantive restriction; guarantees the inverse-utility solves are well-defined. *Reusability:* **yes** — my Box–Cox utility satisfies continuity+monotonicity in consumption, so my one-dimensional inversion inherits the same well-definedness guarantee. [analogy]

**Lemma 1 (EV, three cases).** Under Assumption 1: (i) non-buyers at $p_0$ → $S^{EV}=0$; (ii) switchers → $S^{EV}=y-p_0-U_1^{-1}(U_0(y,\eta),\eta)$; (iii) buyers at both prices → $S^{EV}=p_1-p_0$. [explicit, p. 625]
*Reusability:* the *form* (welfare is a piecewise inverse-utility object) is instructive; not directly portable (price-change object). [analogy]

**Lemma 2 (CV, three cases).** Symmetric, with $S^{CV}=U_0^{-1}(U_1(y-p_0,\eta),\eta)-y$ for the switching case. [explicit, p. 625] Same verdict.

**Theorem 1.** Statement as in §9. [explicit, p. 626]
*Technique (3–5 bullets):* (a) per-type welfare from Lemmas 1–2; (b) the event $\{S\le a\}$ maps to a no-purchase event at a shifted price/income; (c) aggregate over $F(\eta)$, which collapses to $\bar q$; (d) point masses at $0$ and $p_1-p_0$. *Reusability:* **maybe** for the welfare *integrator* idea (express welfare via choice probabilities), **no** for the price-change identification. [analogy]

**Theorem 2.** Multinomial extension via composite outside option $U^*=\max\{U_0,U_2,\dots,U_J\}$ under Assumption 2 (all $U_j$ continuous, strictly increasing). [explicit, pp. 630–631]
*Reusability:* the composite-max reduction is a clean device; my log-sum core already aggregates over the whole menu analytically, so I do not need it, but it is a citable precedent for handling the multinomial structure. [analogy]

**Corollary 1.** As in §9. [explicit, p. 628] *Reusability:* the Marshallian-surplus equivalence is a teaching point, not used in my pipeline. [analogy]

**Section 3 negative result + Remark 3.** Ordered-choice non-identification; parametric "identification" is functional-form artefact. [explicit, pp. 634–639] *Reusability:* **yes, as a cited caution** in my identification section (see §8). [analogy]

---

## 11. Robustness and specification sensitivity

The paper is analytic, so "robustness" is about identification boundaries rather than estimation stress-tests:

- **Monotonicity of the CDF:** requires $\bar q(p_0+a,y)$ (EV) and $\bar q(p_0+a,y+a)$ (CV) nonincreasing in $a$; these follow from Assumption 1 and can be imposed or tested after estimating an unrestricted $\bar q$. [explicit, pp. 627–628]
- **Endogenous income:** control functions recover $\bar q$; Remark 2 distinguishes the marginal welfare distribution at hypothetical income $y$ (the parameter of interest) from the conditional distribution for the subpopulation with realised income $y'$ (an ATE-vs-ATT analogy). [explicit, pp. 622, 633]
- **Parametric vs nonparametric reporting:** the author advises reporting both parametric (e.g. mixed logit) and nonparametric welfare numbers and examining sensitivity to smoothing. [explicit, p. 633]
- **Out-of-support prices / limited price variation:** if hypothetical prices lie outside the observed range, or $P_1$ varies too little, one must either go parametric or only *bound* mean EV/CV; the conclusions of Theorems 1–2 are unaffected, but $\bar q$ at out-of-range points cannot be obtained nonparametrically. [explicit, p. 631]

**What this informs in my work:** (i) the parametric-vs-checked discipline echoes my synthetic-recovery gate; (ii) the "limited variation → only bounds" point is a useful analogue to my effective-sample-size concern (thin coverage → degraded identification of the integrand), though the mechanism differs (their thinness is in observed price support; mine is in importance-sampling node coverage). [analogy] The paper does **not** vary choice-set size, number of draws/starts, opportunity-set definitions, circumstance partitions, or an ability/access boundary — none of those exist here. [explicit absence]

---

## 12. What I can cite this paper for

- That **money-metric welfare (EV/CV) for discrete choice is point-identified from choice probabilities under arbitrary, unspecified-dimension preference heterogeneity**, requiring only monotonicity+continuity of utility in the numeraire. [explicit, pp. 617–618, 622, Theorem 1]
- That **the preference-heterogeneity distribution need not be identified — nor even its dimension — for welfare distributions to be well-defined and point-identified** (Remark 1; Appendix example). [explicit, pp. 627, 646–647] *(This is the key citation for my "welfare object is preference-respecting and robust to not pinning down full heterogeneity" claim.)*
- That **average EV equals the change in average Marshallian consumer surplus even without quasilinear utility**, and average CV $\ge$ EV for a normal good (Corollary 1). [explicit, p. 628]
- That **welfare can be computed directly from choice probabilities without reconstructing expenditure functions / utility primitives**, including under a parametric MNL approximation (eqs. 23–24). [explicit, pp. 632, 640]
- As **methodological precedent and caution** that parametric welfare calculations can rest on functional-form-driven identification (Remark 3 / ordered-choice result) — used to motivate my synthetic-recovery certification. [explicit, pp. 638–640]
- For the **EV/CV–as–inverse-utility-solve** construction (Lemmas 1–2), as a relative of my own bracketing inversion. [explicit, p. 625]

---

## 13. What I should NOT cite this paper for  [overclaim risks]

- **Not** for any opportunity / access / ability mechanism, heterogeneous feasible sets, or rationing — the paper has a **universal common choice set** and no opportunity object. [explicit absence]
- **Not** for a **two-way or three-way decomposition** of welfare inequality — it has **no decomposition and no inequality index** at all. Do not present it as opportunity-vs-preference or access/ability/preference. [explicit absence]
- **Not** for an **ex-ante / inclusive-value (log-sum) welfare core** — its welfare object is a per-type price-change EV/CV aggregated to a distribution; the log-sum appears only in a parametric example, not as the welfare number. Do not read my ex-ante stance into it. [explicit]
- **Not** as containing or endorsing my **$W^1$–$W^6$ family** or any **Ind-$y$ / Ind-$A$** classification — it does not. The loose "Full-Responsibility corner" analogy is mine, not the source's; flag it as such. [**source does NOT contain $W^1$–$W^6$**]
- **Not** for a **reference-level equivalent income** — its object is a *price-change* compensation, not a level against a normative reference state/preference/set. [explicit]
- **Not** for **occupation/industry** anything; no occupation, no sector, no NACE/ISCO content. No `loc4`/`lindi` mapping. [explicit absence]
- **Not** for a **random-opportunity** reading — the paper has deterministic, common menus and stochastic *preferences*; its randomness is in $\eta$, not in opportunities. Consistent with my deterministic-opportunities stance, but do not cite it as evidence about opportunities at all. [explicit]
- **Not** to clear parametric structural decompositions of the "mechanical / functional-form" charge — Remark 3 cuts the other way for ordered choice. [explicit, p. 639]
- **Theory-paper boundary:** this is a welfare-*measurement* econometrics paper; it has nothing to do with the Haydar–Maniquet axiomatic characterisation, and must never be enrolled to support axioms, characterisations, or proofs, nor read as a theory contribution of my JMP. [boundary]

---

## 14. Direct quotes worth citing

(Short, exact, with page numbers. Use sparingly.)

1. "the marginal distributions of EV and CV can be expressed as simple closed-form functionals of conditional choice probabilities" (abstract, p. 617).
2. "These results hold even when the distribution and dimension of unobserved heterogeneity are neither known nor identified" (abstract, p. 617).
3. "average EV for a price rise equals the change in average Marshallian consumer surplus" (abstract, p. 617).
4. "more numeraire is better" (gloss on strict monotonicity, p. 622).
5. "the identification result underlying this calculation is artificial in that it is driven entirely by functional form assumptions" (Remark 3, ordered choice, p. 639).
6. "identifiability of the heterogeneity distribution or even correct specification of its dimension is not a requirement for identifiability of welfare distributions" (Appendix, p. 647).

[All verbatim from the PDF; each under the quote-length limit. Quote 5 must be cited with the §8 caution, not as endorsement.]

---

## 15. Open questions and risks for my draft

- **Object mismatch risk.** My equivalent-income *level* against a reference set is not the same object as Bhattacharya's price-change EV/CV. If I cite him as authority for "money-metric welfare from discrete choice," a careful referee will note the object differs (change vs level; universal vs constrained set). I should cite him precisely for the *preference-respecting, heterogeneity-robust* property, not for the object form. [risk]
- **Inference is deferred in the source.** Bhattacharya defers full inference to Bhattacharya–Lee (2014); I cannot lean on this paper for standard errors on welfare distributions. My cluster-robust bootstrap is my own and is not supported by this paper. [risk — verify Bhattacharya–Lee status if I need an inference citation]
- **The functional-form caution (Remark 3) is a live referee weapon.** It strengthens my motivation for synthetic-recovery certification but also names the exact vulnerability of my parametric RURO; I must address it head-on rather than cite around it. [risk]
- **Nonparametric ideal vs my parametric reality.** The paper's nonparametric ideal needs price variation I lack; positioning must make clear I adopt its *welfare-well-definedness lesson* while operating parametrically with a different identification warrant (recovery, not in-sample fit). [risk]
- **No opportunity object.** The paper cannot speak to the central empirical bet of my JMP (that opportunity differences are large and compensation-relevant); it is upstream infrastructure only. Do not let its prominence crowd the opportunity-mechanism citations (Aaberge–Colombino–Strøm, Dagsvik, Aaberge–Colombino) in the positioning. [risk]

---

## 16. TL;DR for retrieval

Bhattacharya (2015, *Econometrica*) point-identifies the marginal distributions of EV/CV from a discrete *price change* as closed-form functionals of conditional choice probabilities, under arbitrary unspecified-dimension **preference** heterogeneity and only monotonicity+continuity of utility in the numeraire — the canonical authority that my preference-respecting money-metric welfare object is well-defined without identifying the heterogeneity distribution. It has **no opportunity mechanism, no inequality index, no decomposition, no $W^1$–$W^6$ family, and no inclusive-value welfare core**, so it informs only the **preference** channel and the welfare-object's robustness, never access/ability or the three-way split. Its ordered-choice negative result and Remark 3 are a double-edged citation: useful to motivate my synthetic-recovery certification against the functional-form-identification charge, but not a clearance of parametric structural decompositions.
