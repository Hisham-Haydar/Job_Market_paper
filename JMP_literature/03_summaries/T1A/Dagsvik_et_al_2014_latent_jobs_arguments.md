# Dagsvik, Jia, Kornstad & Thoresen 2014 — Theoretical and Practical Arguments for Modeling Labor Supply as a Choice among Latent Jobs

> **Extraction note.** This is a **survey / methodological-arguments** paper, not
> an empirical estimation paper. Its empirical figures are borrowed from Dagsvik
> & Jia (2012a). The primary technical derivations of the latent-jobs model live
> in **Dagsvik & Strøm (2006)** and **Dagsvik & Jia (2012a)**, to which this paper
> repeatedly defers; cite those for the machinery, this one for the *argument and
> interpretation*. Throughout I flag **[explicit]** (stated in this source),
> **[analogy]** (derived by mapping to the JMP), and **[not established]** (absent
> from this source). Pages cited from the running headers in the supplied PDF;
> ambiguous locations marked **[verify]**.

---

## 0. Metadata

- **BibTeX key:** `dagsvik_jia_kornstad_thoresen_2014`
- **Authors:** John K. Dagsvik (Statistics Norway and Ragnar Frisch Centre for Economic Research); Zhiyang Jia, Tom Kornstad, Thor O. Thoresen (Statistics Norway).
- **Year:** 2014 (© 2013).
- **Outlet:** *Journal of Economic Surveys*, Vol. 28, No. 1, pp. 134–151.
- **DOI:** 10.1111/joes.12003 [explicit, p.134].
- **PDF:** `Dagsvik_et_al__-_2014_-_THEORETICAL_AND_PRACTICAL_ARGUMENTS_FOR_MODELING_LABOR_SUPPLY_AS_A_CHOICE_AMONG_LATENT_JOBS.pdf`
- **Tier:** T1A (as filed). Qualifier: it is the *programmatic statement* of the latent-jobs research program rather than its technical core.
- **JMP block(s) it serves:** **model-foundation / motivation**; **estimation** (the latent-jobs likelihood form); **identification** (the preference-vs-opportunity separation result); **opportunity-mechanism — access** (hours availability $g(h)$ and total job availability $\theta$). It does **not** serve the **welfare** or **decomposition** blocks (no welfare measure, no inequality index, no decomposition is computed), and it speaks to **ability** only obliquely (a separately estimated qualifications-based wage equation, not an opportunity-density channel).

---

## 1. One-paragraph relevance to my JMP

This is the canonical theoretical justification for the object at the centre of my structural layer: it shows that the *ad hoc* part-time/full-time dummies of the conventional van Soest discrete-choice model can be re-read as an **explicit, structural opportunity term** $\log(\theta g(h))$ inside the choice index, i.e. that my opportunity-density terms ($\log h$, $\log\text{market}$) have a demand-side foundation rather than being a fitting device [explicit, pp.139–141]. It speaks directly to my **access** channel (the hours-opportunity distribution $g(h)$ and the total-job-availability scalar $\theta$, the latter linkable to the unemployment rate) and supplies the foundational **identification** result I must defend: preferences and the opportunity distribution are separable only up to an additive function of hours unless one imposes functional form (Box–Cox) or uses desired-hours data [explicit, p.143]. It does **not** separate **ability** from **access** within the opportunity object, computes **no** welfare measure, and contains **no** decomposition — so it anchors my estimation and identification prose, not my welfare or decomposition prose.

---

## 2. Data and setting

- This paper is a survey; it has no estimation dataset of its own. The empirical illustrations are **lifted from Dagsvik & Jia (2012a)**: **Norwegian married couples**, base year **1997**, Labour Force Survey data, with out-of-sample validation against 2006 LFS data and 2003 income-tax-return data [explicit, pp.144–145].
- **Sample unit in the illustration:** married couples (a joint decision unit) [explicit, p.144]. This matches my couples unit in spirit, but the figures are illustrative, not re-estimated here.
- **Key variables in the illustration:** annual hours of work discretised into eight intervals with positive-hours medians **260, 780, 1040, 1560, 1960, 2340, 2600** [explicit, p.144]; household disposable income (Figure 3) [explicit, p.146 [verify]].
- **Budget-set construction:** $C=f(hw,I)$, where $f(\cdot)$ maps gross income to after-tax household income and "can in principle capture all details of the tax and benefit system" [explicit, p.139, eq. (4)]. This is the same role my EUROMOD disposable-income map plays [analogy].
- **Transport to my France pooled 2015–2017 EUROMOD cross-section:** the *model* transports cleanly (static, discrete, tax-benefit budget). The *identification and validation strategy does not transport directly*: the paper's out-of-sample assessment exploits a **tax reform** (2006) and a second data source, and one of its two identification routes requires **desired/preferred-hours data** (Euwals & van Soest 1999; Bloemen 2008) [explicit, p.143]. I have **no panel, no desired-hours instrument, and no exploited reform**; I rely instead on functional form plus **synthetic recovery** (which this paper does not use). Features named here that I do **not** have: a tax-reform natural experiment for out-of-sample validation; desired-hours data; job-specific wage data of the Dagsvik–Jia (2012a) "general case."

---

## 3. Model and objects (object-by-object map to mine)

- **Choice set = my latent-jobs set?** **Yes, conceptually [explicit].** The agent chooses among *jobs* $z=1,2,\dots$ (with $z=0$ the non-market alternative), each job carrying fixed job-specific hours $H(z)$ and non-pecuniary attributes; observed hours and income are those of the chosen job [explicit, pp.139–140, eq. (8)]. The choice sets $\{B(h)\}$ (available jobs with hours $h$) are latent to the researcher [explicit, p.140]. This is exactly my latent-jobs framing.
- **Deterministic utility = my preference utility $v$?** **Yes [explicit].** $U(C,h,z)=v(C,h)+\varepsilon(z)$ with $\varepsilon(z)$ iid Gumbel; $v(C,h)$ is the systematic preference term [explicit, p.139, eq. (8)]. The recommended functional form is **generalized Box–Cox in consumption and leisure with an interaction term** (eq. (15)) [explicit, p.143] — the same family as my preference block.
- **Explicit opportunity / availability mechanism analogous to my $g$?** **Yes, but only over hours and total count [explicit].** The number of available jobs at hours $h$ is $m(h)$; with $\theta=\sum_x m(x)$ and $g(h)=m(h)/\theta$, the term $\theta g(h)$ is the **opportunity measure** and $g(h)$ the **opportunity distribution** [explicit, p.141]. It enters the choice index additively as $\log(\theta g(h))$ (eq. (14)) [explicit, p.141].
  - **hours channel:** present, as $g(h)$ [explicit].
  - **market / participation channel:** present, as $\theta$ (total job availability; depends on education and a constant; linkable to the unemployment rate) and the single non-market alternative $m(0)=1$ [explicit, pp.140–141, 143; footnote 12 p.148].
  - **wage (ability) channel:** **not in the opportunity density of this exposition.** The baseline assumes the wage "only depends on individual qualifications and does not vary across jobs" [explicit, p.139]; wages are predicted from a **separately estimated wage equation** [explicit, p.144]. Job-specific wages are deferred to the cited Dagsvik & Jia (2012a) "more general case" [explicit, p.139].
  - **occupation channel:** **absent in the baseline** ("the jobs are latent and thus job characteristics do not appear") [explicit, p.144]. The cited Dagsvik & Strøm (2006) extension classifies jobs into **two observable sectors (public and private)** [explicit, p.144].
- **Budget map = my EUROMOD disposable income?** Functionally yes (eq. (4)); their $f$ is my EUROMOD map [analogy].
- **Does any job attribute enter BOTH utility and the opportunity mechanism?** **No [explicit].** Hours enter utility via $v(C,h)$ and availability via $g(h)$, but these are distinct objects whose **non-separability is the paper's central identification caveat** (§8), not a deliberate double-entry. They do not place wage or occupation in both blocks; in fact the baseline keeps occupation out of both. No identification-driven double-entry is asserted.

**Differences to record.** (i) Their opportunity object is **one-dimensional over hours** (plus the scalar $\theta$); my $g$ additionally carries a **wage/ability** sub-block and an **occupation** access sub-block, which are beyond this paper [explicit vs. JMP]. (ii) They use a **fixed finite hours grid $D$ with multiplicities $m(h)$**, not a **sampled** alternative set; consequently there is **no sampling-of-alternatives correction** in their likelihood (see §4b). (iii) Their "sector" (public/private) is an **institutional** partition — it is *neither* my occupation (`loc4`/ISCO) *nor* my industry (`lindi`/NACE); do not map it onto either.

---

## 4. Estimation method

- **Likelihood / estimator:** multinomial-logit-type choice probabilities derived from the iid-Gumbel RUM, with representative utilities $\{\psi(h)\}$ **weighted by job frequencies $\{m(h)\}$** (eqs. (10)–(11)) and re-expressed as $\exp(\psi(h)+\log(\theta g(h)))$ in the denominator-normalised form (eq. (14)) [explicit, pp.140–141]. Maximum likelihood, with the wage equation, choice probabilities, and opportunity measure specified jointly [explicit, p.144]. No GMM, no simulated argmax in the exposition.
- **Choice-set construction:** **fixed discrete grid** of hours points $D$ (the illustration uses eight intervals). Discretisation is argued to be inessential and arbitrarily refinable [explicit, pp.139, 144].
- **Proposal / sampling density:** **none** — the grid is fixed, not sampled (see §4b).
- **Prior/proposal correction ($-\log\pi$ subtracted from the choice index)?** **Not established / not present.** The additive term inside the index is the **structural** $\log(\theta g(h))$, not a nuisance sampling correction. It is always well defined for $g(h)>0$ [analogy]; the question of an importance-sampling prior does not arise here.
- **Normalisation / scale:** the summability constraint $\sum_h g(h)=1$ need **not** be imposed at estimation because $\theta g(h)$ enters jointly and the normalisation can be applied post-estimation [explicit, p.143]. Fixed cost can be folded into $\theta$ as $\theta\exp(c)$ (Cogan 1981) [explicit, p.141].
- **What pins preferences apart from the opportunity mechanism:** functional-form restrictions (Box–Cox, eq. (15)) — see §8. Without them the two are confounded up to an additive $d(h)$ [explicit, p.143].
- **Numerical method / starting values / multistart:** not discussed in this survey [not established]. (Box–Cox estimation difficulties are flagged — §11.)
- **Verdict — reusable for my RURO/JAX pipeline?** **Partly — as the structural template, not as a runnable recipe.** Reuse: the $\exp(\text{utility}+\log\text{opportunity})$ index structure (eq. (14)) is exactly my per-alternative value's structural backbone, **minus** my $-\log\pi$ correction (which my pipeline needs because I *sample* alternatives, whereas they use a fixed grid). Do **not** reuse: their fixed-grid construction in place of my sampled set; and there is no estimation code or numerical protocol to reuse here (it is in the cited companions).

## 4b. Proposal / sampling-of-alternatives correction  [extract even if brief]

**Not present in this paper.** Alternatives are a **fixed finite grid** of hours points with structural multiplicities $m(h)$; there is no random sampling of alternatives and therefore no McFadden-style sampling correction and no per-alternative log-prior [explicit, pp.139–141]. The additive log-term $\log(\theta g(h))$ that appears inside the choice index (eq. (14)) is a **structural opportunity weight** (the object of interest), **not** a proposal/prior correction — this is the single most important place a careless reader could conflate their model with my pipeline. Mapping to my design: their $\log(\theta g(h))$ is the analogue of my **structural** $[\log h + \log w + \log\text{market}]$ block, **not** of my $-\log\pi(j;x_i)$. My $-\log\pi$ exists only because I integrate over *sampled* draws; it has no counterpart here. Relation to my proposal-individualisation concern (wage/occupation individualised; hours/employment common): **not addressed** — the question is meaningless for a fixed grid [not established].

## 5. Opportunity mechanism  [MOST IMPORTANT — split by channel]

The mechanism is a **deterministic density over hours plus a total-availability scalar**, derived from latent job multiplicities. Formally: $B(h)$ is the set of available jobs with hours $h$; $m(h)=|B(h)|$; $m(0)=1$; $\theta=\sum_{x\in D} m(x)$; $g(h)=m(h)/\theta$; the **opportunity measure** is $\theta g(h)$ [explicit, pp.140–141]. The $\{m(h)\}$ are **sufficient statistics** for the latent choice sets under the iid-Gumbel assumption [explicit, p.141]. Equilibrium foundation: $\theta$ can be derived from a two-sided matching model (Dagsvik 2000; Dagsvik & Jia 2012b), but the paper uses a **reduced-form** representation [explicit, p.142] — as do I [analogy].

Mapping to my three sub-objects:

- **access (hours / market / region / year / occupation offers).**
  - *Hours availability:* **explicit and central** — $g(h)$. The standard empirical specification is **$g(h)$ uniform apart from peaks at part-time and full-time hours** [explicit, p.143], implemented as $\log(\theta g(h))$ **linear in length of schooling plus part-time and full-time dummies** [explicit, p.144]. This is the demand-side reinterpretation of van Soest's hours dummies — the foundation for treating my hours-availability terms as structural access rather than fitted taste.
  - *Market / participation:* **explicit** — $\theta$ (total job availability), allowed to depend on education and a constant, and linkable to the unemployment rate and business-cycle variation [explicit, pp.141, 143; footnote 12, p.148]. The non-market alternative is the single $z=0$ with $m(0)=1$.
  - *Region / year:* **not modelled** in this paper [not established]. (My access sub-block's regional, urbanisation, and year shifters are beyond it.)
  - *Occupation offers:* **not in the baseline** [explicit, p.144]. The cited two-sector (public/private) extension is institutional, not occupational.
- **ability (wage technology: returns to education/experience, residual productivity).** **Present but outside the opportunity density.** Wages depend on individual **qualifications** through a separately estimated wage equation, with random effects giving a **mixed multinomial logit** that also relaxes IIA (McFadden & Train 2000; used by Dagsvik & Strøm 2006, Dagsvik & Jia 2012a, Kornstad & Thoresen 2007) [explicit, pp.142, 144]. This is the closest object to my **ability** sub-block, but the paper does **not** fold it into $g$ as a job-availability channel, and does **not** separate ability from access *within* opportunity [explicit + not established]. My ability-in-$g$ design is therefore an **extension beyond** this source.
- **occupation as availability vs. something else.** In the baseline, occupation is **absent** (jobs latent, characteristics suppressed) [explicit, p.144]. In the cited extension it is an **observable sector (public/private)** entering as an additional discrete dimension [explicit, p.144]. **Flag:** their "sector" is an institutional split; it must **not** be mapped to my occupation-as-access (`loc4`, ISCO-type) nor to my reserved industry object (`lindi`, NACE). The paper does **not** conflate occupation with industry — it simply does not use either; the conflation risk is on the *reader's* side, not the source's.

**Functional form:** $g(h)$ piecewise-constant with PT/FT peaks; $\log(\theta g(h))$ linear in schooling and PT/FT dummies [explicit, pp.143–144]. **Deterministic** in the baseline ("So far we treat the terms $\{m(h)\}$ as deterministic") [explicit, p.140]; the paper *also* offers a **stochastic-choice-set** interpretation (Dagsvik 1994; Dagsvik & Strøm 2006; Dagsvik & Jia 2006; Dickens–Lundberg) that accommodates unobserved heterogeneity in opportunities [explicit, pp.141–142] — which I do **not** adopt (my opportunities are deterministic). 

**Cost to my decomposition if the mechanism were omitted:** the source itself states the payoff — without an explicit $\log(\theta g(h))$, the PT/FT peaks would have to be absorbed into $v(C,h)+\gamma(h)$ as taste, making the model non-structural and policy simulation uninterpretable [explicit, pp.138–139]. That is precisely my motivation for putting access in $g$ rather than letting it masquerade as preference; this paper is the cleanest citation for that argument.

## 6. Welfare object — and its place on my $W^1$–$W^6$ map

**The paper computes no welfare measure. [explicit / not established]** It motivates structural modelling by noting that counterfactual policy effects "are at the core of discussions on welfare effects of policy changes" [explicit, p.136] and cites Chetty (2009) on sufficient statistics for welfare analysis [explicit, footnote 3, p.148], but it constructs **no** money-metric welfare, **no** equivalent income, **no** compensating/equivalent variation, and **no** inclusive-value welfare object. The only distributional output is a **descriptive** predicted disposable-income distribution for model assessment (Figure 3) [explicit, p.146 [verify]].

**Placement on my $W^1$–$W^6$ map:** **N/A.** The source does **not** contain $W^1$–$W^6$, does not use Independence-of-$y$ / Independence-of-$A$, and takes no compensation–responsibility stance. Do not attribute any welfare-measure family to it. **Verdict: incompatible as a welfare source** (it is upstream of welfare — it supplies the structural utility/opportunity primitives the welfare layer consumes, nothing more).

## 6b. Inclusive value and money-metric inversion  [extract if used]

**Not established as a welfare construction.** The **log-sum denominator** appears in the choice probabilities (eqs. (10)–(14)) [explicit], and the expectation over the Gumbel shocks is taken **analytically** (this is what yields the closed-form MNL form) [explicit, by construction]. But the paper never elevates the log-sum to an **inclusive-value welfare** object and never performs a **money-metric inversion** (no one-dimensional solve to a money figure, no EV/CV). So: *analytic-in-shocks* — **yes, shared** [explicit, structurally]; *inclusive value as welfare core* — **not in this paper** [not established]; *inversion to money* — **absent** [not established]. My analytic-in-shocks, importance-sampling inversion shares only the analytic-expectation step with this source.

## 7. Inequality / decomposition content  [three-way where relevant]

**None. [explicit / not established]** No inequality index (no Gini/MLD/Theil/Atkinson), no decomposition rule (no Shapley/Shorrocks/factor/subgroup/RIF), no counterfactual equalisation. The disposable-income *distribution* in Figure 3 is a goodness-of-fit display, not an inequality analysis [explicit, p.146 [verify]]. **Verdict: not reusable for my three-way access/ability/preference Shapley–Shorrocks split.** The paper is silent on decomposition entirely; it is neither two-way nor three-way. To connect it to my decomposition would require building the entire welfare-and-decomposition layer *on top of* its structural model — which is exactly my contribution, not theirs.

## 8. Identification and the separation of preferences from opportunities  [STRICT]

This is the paper's most load-bearing contribution for me.

- **The confounding result [explicit, p.143].** For positive $h$, the choice index contains $\psi(h)+\log g(h)=v(f(hw,I),h)+\log g(h)$. Assuming the offered wage does **not** depend on hours and parameters are constant across the population, Dagsvik & Jia (2012a) show $v(C,h)$ is identified **only up to an additive term $d(h)$ depending on hours** — i.e. **preferences and the opportunity distribution are non-parametrically separable only up to an additive function of $h$.**
- **What restores full identification [explicit, p.143].** Either (i) **functional-form assumptions** — the Box–Cox form (eq. (15)), justified on invariance-principle grounds (Dagsvik & Røine Hoff 2011; Dagsvik 2012), under which the model is identified; or (ii) **data on desired/preferred hours** (Euwals & van Soest 1999; Bloemen 2008).
- **Policy-simulation escape clause [explicit, p.143].** For counterfactuals that only change the budget $f$, one need **not** separate the hours-utility term from $g(h)$, because neither depends on $f$. (This does *not* help me: my decomposition *requires* the separation, since I equalise channels.)
- **Ability vs. access within opportunity:** **not addressed [not established].** The paper's identification argument is **preference vs. (hours) opportunity** only. It offers **no** argument separating a wage/ability sub-block from an access sub-block inside $g$. My three-way cut's ability/access boundary therefore cannot be supported by this paper; it rests on my own functional-form-plus-channel-assignment, and is exactly the part a "your decomposition is mechanical" referee will press.
- **Transport to my France pooled cross-section.** The functional-form route (i) **transports** — it is precisely my strategy (Box–Cox preferences). The desired-hours route (ii) does **not** — I have no desired-hours data. The paper's *assessment* standard is **out-of-sample prediction across a tax reform**, **not synthetic recovery** [explicit, pp.144–145]; so this paper does **not** license my synthetic-recovery certification — I must cite it for the *identification logic* (separation is parametric, not nonparametric) and source the recovery-as-evidence standard elsewhere. Honest net statement: **Dagsvik et al. establishes that preference/opportunity separation in latent-jobs models is inherently parametric and defensible on functional-form grounds; it does not, and cannot, certify the finer ability/access separation my decomposition needs.**

## 9. Key results and magnitudes

The paper reports **no estimated parameters of its own**; magnitudes are illustrative or borrowed.

- **Wage elasticities (borrowed from Dagsvik & Jia 2012a):** "of moderate magnitude, with married females more responsive than males," broadly in line with the literature; **no numerical values given here** [explicit, p.146]. The discrete-choice literature (including theirs) typically reports **gross** (pre-tax) wage elasticities, unlike the Hausman-type post-tax convention [explicit, p.146].
- **Illustrative logit elasticity arithmetic [explicit, p.147]:** for $P(w,X)=1/(1+\exp(-\alpha\log w - X\beta))$, the participation wage elasticity is $(1-P)\alpha$; at $P=0.6$ it is $0.4\alpha$, at $P=0.8$ it is $0.2\alpha$. This is a pedagogical point that **nonlinear models yield sample-dependent elasticities**, not an estimate.
- **Out-of-sample fit (Norway):** the 2006 tax reform cut the top marginal rate from **55.3% to 47.8%** [explicit, p.144]; the model's predicted **female** hours distribution for 2006 tracks the actual better than the 1997 baseline, while **male** responses are not well reproduced [explicit, pp.144–145]; the 2003 predicted disposable-income distribution matches the data closely [explicit, p.145].
- **Benchmarking value for me:** "females more responsive than males, both moderate" is a sanity band for my own elasticities **if** I compute them (currently deferred); there are **no opportunity-share or welfare-spread magnitudes** here to benchmark my decomposition against.

## 10. Estimators, theorems, or formal results

No numbered theorems. The reusable formal objects are the choice-probability derivations and the functional form.

1. **Latent-jobs choice probability (eq. (14)) [explicit, p.141].**
   $$\varphi(h)=\frac{\exp\!\big(\psi(h)+\log(\theta g(h))\big)}{\exp(\psi(0))+\sum_{x\in D}\exp\!\big(\psi(x)+\log(\theta g(x))\big)}.$$
   - Assumptions: iid Gumbel shocks $\varepsilon(z)$; $v(C,h)+\varepsilon(z)$ utility; fixed-hours jobs; $m(h)$ deterministic (baseline).
   - Technique: McFadden RUM → MNL; sum over $z\in B(h)$ collapses the job-level probability (eq. (9)) into the hours-level probability via the multiplicity $m(h)$; $\{m(h)\}$ are sufficient statistics for the latent sets.
   - **Reusability: yes** — this *is* the structural form of my per-alternative value, minus the $-\log\pi$ sampling correction my pipeline adds.
2. **Box–Cox systematic utility (eq. (15)) [explicit, p.143].**
   $$v(C,h)=\gamma\frac{C^{\alpha}-1}{\alpha}+\delta\frac{(M-h)^{\beta}-1}{\beta}+\mu\frac{(C^{\alpha}-1)\big((M-h)^{\beta}-1\big)}{\alpha\beta}.$$
   - Assumptions: $\alpha<1,\beta<1,\gamma>0,\delta>0$, $\mu$ constrained → strict concavity; $M$ = maximum feasible hours.
   - Technique: derived from qualitative-measurement / invariance axioms (Dagsvik & Røine Hoff 2011; Dagsvik 2012); under it the model is identified.
   - **Reusability: yes** — same preference family as my utility block (consumption, leisure, interaction). Note my baseline carries demographic taste-shifters and gender that this generic form does not write out.
3. **Identification-up-to-$d(h)$ result [explicit, p.143].** Statement and assumptions as in §8. **Reusability: yes, as a cited identification primitive** for the preference/opportunity separation; **no** for ability/access separation.

## 11. Robustness and specification sensitivity

- **Box–Cox vs. quadratic [explicit, p.143]:** Box–Cox yields roughly the same fit as quadratic; quadratic can fail to be increasing in leisure; Box–Cox is harder to estimate (nonlinear in parameters). **Mastrogiacomo et al. (2011)** report estimation difficulties; **Blundell & Shepard (2012)** obtained an unacceptable estimate of one Box–Cox parameter. → A direct warning for my own Box–Cox estimation; relevant to my pinned/at-bound parameters.
- **Number of discrete alternatives [explicit, pp.139, 144]:** discretisation is argued inessential and arbitrarily refinable; the discrete setting may even be the "true" one. → Supports my fixed-resolution grids as defensible, not a mere approximation.
- **IIA relaxation [explicit, pp.142]:** nested MNL, random effects, or a random-effects wage equation (mixed MNL) relax IIA without ad hoc terms. → Optionality for my robustness, though my baseline does not need it.
- **Elasticities sample-dependent in nonlinear models [explicit, pp.146–147].** → Caution for any elasticity reporting I add.
- **Model assessment = out-of-sample prediction [explicit, pp.144–145].** Their stress test is predicting a different year / a reform, **not** synthetic recovery. → My recovery-based certification is a *different* (and, for my no-reform setting, more available) standard; cite this for the limits of in-sample fit, not for recovery.

## 12. What I can cite this paper for

- That the conventional discrete-choice (van Soest) model's PT/FT **dummies can be reinterpreted as a structural opportunity term** $\log(\theta g(h))$ arising from demand-side job availability — the foundation for treating my access terms as structural rather than as fitted taste [pp.138–141].
- The **definitions** of the opportunity measure $\theta g(h)$ and opportunity distribution $g(h)$, with $\theta$ as total job availability (education-dependent, unemployment-linked) [pp.140–141].
- The **identification result** that preferences and the opportunity distribution separate only up to an additive $d(h)$ absent functional-form or desired-hours information, hence that **the separation is parametric** [p.143].
- That **Box–Cox** preferences are the invariance-justified, identification-securing functional form for this class of models [p.143].
- That the latent-jobs model **rationalises hours peaks structurally** and thereby keeps counterfactual simulation interpretable, where dummy-augmented conventional models do not [pp.138–139].
- That a **reduced-form** opportunity measure has an **equilibrium (two-sided matching)** foundation [p.142].
- General methodological cautions: Box–Cox estimation fragility; nonlinear elasticity sample-dependence; discretisation as inessential [pp.143, 146–147].

## 13. What I should NOT cite this paper for  [overclaim risks]

- **Any welfare measure.** It computes none; do **not** cite it for money-metric welfare, equivalent income, EV/CV, or inclusive-value welfare. **It does not contain $W^1$–$W^6$** or any compensation–responsibility / Independence-of-$y$ / Independence-of-$A$ framing.
- **Any decomposition.** No inequality index, no Shapley/Shorrocks, no opportunity-vs-preference split — and certainly no **three-way access/ability/preference** split. Citing it for a decomposition (even two-way) would be an overclaim.
- **Ability/access separation within opportunity.** Its identification logic is preference-vs-(hours-)opportunity only. Do not read it as licensing my ability/access cut.
- **Occupation/sector language.** Its only occupational object is a cited **public/private institutional sector** extension. Do **not** present this as my **occupation-as-access** (`loc4`/ISCO), and do **not** let it drift into **industry** (`lindi`/NACE) language. The paper does not conflate the two; I must not introduce the conflation.
- **Random vs. deterministic opportunities.** The paper offers a **stochastic-choice-set** interpretation alongside the deterministic baseline. Map only the **deterministic** reading to my design; do not import the random-choice-set framing.
- **Synthetic-recovery certification.** Its assessment standard is out-of-sample prediction, not parameter recovery. Do not cite it as precedent for my recovery gate.
- **Theory-paper boundary.** This is empirical-methods literature; it has no bearing on the companion Haydar–Maniquet axiomatic paper. Do not let any of its content migrate into the theory paper's territory, and do not read the JMP as a theory contribution because it cites this.

## 14. Direct quotes worth citing

To respect copyright I reproduce one short verbatim phrase and give page-anchored pointers for the rest (pull exact wording directly from the PDF at these locations):

- p.141, defining the central object (verbatim): "We shall call θg(h) the opportunity measure and g(h) the opportunity distribution."
- p.141 [pointer]: the sentence stating that $\log g(h)+\log\theta$ in eq. (14) is an explicit representation of demand-side choice restrictions, no longer an ad hoc addition.
- p.143 [pointer]: the sentence stating preferences and the opportunity distribution can be separated only up to an additive term depending on $h$.
- p.143 [pointer]: the sentence that full identification requires functional-form assumptions (or desired-hours data).
- p.144 [pointer]: the sentence stating that in this version jobs are latent and job characteristics do not appear, with the public/private two-sector extension referenced to Dagsvik & Strøm (2006).
- p.140 [pointer]: the sentence treating $\{m(h)\}$ as deterministic ("So far we treat the terms $\{m(h)\}$ as deterministic").

## 15. Open questions and risks for my draft

- **The parametric-separation risk is inherited, not solved.** The paper is candid that separation rests on functional form; my decomposition inherits this, and the referee point ("the access/preference split is a functional-form artefact") is *not* answered by citing Dagsvik — it is *named* by it. My synthetic-recovery evidence is the load-bearing answer, and this paper does not supply it.
- **Ability/access has no identification anchor here.** My finer cut needs its own defence (channel assignment as an explicit normative-cum-functional assumption); I cannot lean on this source for it.
- **Validation-standard mismatch.** Their out-of-sample/reform standard is unavailable to me (no exploited reform, no panel); I must justify recovery-based certification on its own terms.
- **No welfare/decomposition scaffolding to borrow.** Everything downstream of the structural model — the inclusive-value welfare inversion, the $-\log\pi$ welfare integrator, the Shapley split — is mine to build; this paper ends exactly where my contribution begins.
- **Wage/ability modelling choice.** They keep wages in a separate qualifications equation (job-invariant in the baseline). My decision to carry wage returns *inside* $g$ as an ability channel is a deliberate departure I should flag against this baseline, citing Dagsvik & Jia (2012a)'s job-specific-wage general case as the closer precedent.

## 16. TL;DR for retrieval

Dagsvik–Jia–Kornstad–Thoresen (2014) is the programmatic survey that reinterprets van Soest's ad hoc hours dummies as a **structural opportunity term** $\log(\theta g(h))$ — supplying the foundation and citation for my **access** channel (hours availability $g(h)$, total job availability $\theta$) and for the **preference-vs-opportunity identification** result (separable only up to an additive $d(h)$ absent Box–Cox functional form or desired-hours data). It treats **ability** only as a separate qualifications-based wage equation (not an opportunity-density channel), keeps occupation latent (with a cited public/private *sector* extension that is neither my ISCO occupation nor NACE industry), and contains **no welfare measure, no $W^1$–$W^6$, and no decomposition** — it is strictly upstream of my welfare/decomposition layers and informs only my estimation and identification prose.
