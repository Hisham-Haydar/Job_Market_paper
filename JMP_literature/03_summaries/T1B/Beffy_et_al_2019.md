# Beffy, Blundell, Bozio, Laroque & Tô 2019 — Labour supply and taxation with restricted choices

> **Provenance note.** This summary is produced from the attached PDF (the accepted
> "Article in Press" version, HAL `halshs-01883898`), which is internally paginated
> **1–31**; the published article is *Journal of Econometrics* 211(1), **pp. 16–46**.
> All page citations below use the **in-press internal numbering (1–31)** visible in
> the PDF; add 15 to map to published pages approximately. Equation, table, and lemma
> numbers are as printed in the PDF. Tags used throughout: **[explicit]** = stated in
> the source; **[analogy]** = derived-by-analogy to my JMP, not in the source;
> **[not established]** = the source does not contain this; **[verify]** = metadata I
> could not confirm from the PDF.

---

## 0. Metadata

- **BibTeX key:** `BeffyBlundellBozioLaroqueTo2019` [verify — house convention].
- **Authors:** Magali Beffy (CREST), Richard Blundell (UCL/IFS), Antoine Bozio (PSE/IFS), Guy Laroque (UCL/IFS/Sciences-Po), Maxime Tô (UCL/IFS). [explicit, p. 1]
- **Year:** 2019 (online 2018). [explicit]
- **Outlet:** *Journal of Econometrics* 211(1), pp. 16–46. [explicit, HAL cover]
- **DOI:** 10.1016/j.jeconom.2018.12.004. [explicit]
- **HAL Id:** halshs-01883898. **PDF filename:** `Beffy_et_al_2019_Labour_supply_and_taxation_with_restricted_choices.pdf`. License: CC BY (open access). [explicit]
- **Tier:** T1A.
- **JMP block(s) served:** **identification** (primary); **opportunity-mechanism → access** (primary, hours channel only); **estimation** (secondary, identification logic and Monte-Carlo recovery); **motivation** (secondary). **Not** welfare, **not** decomposition, **not** ability (wage-technology) opportunity, **not** normative-interpretation. [analogy — relevance routing]

---

## 1. One-paragraph relevance to my JMP

This is the canonical structural restricted-choice labour-supply paper and the direct methodological ancestor of my JMP's **access** channel: it models observed hours as the joint product of preferences and an estimated **offer distribution over hours**, and—uniquely useful for me—it proves the conditions under which preferences and the offer distribution are *separately* identified. It speaks almost entirely to the **access** dimension (hours availability) and to the **identification** backbone (separating preferences from constraints), plus its Monte-Carlo work is a published precedent for my synthetic-recovery standard of evidence. It contains **no** welfare, equivalent-income, inclusive-value, or inequality/decomposition content, and **no** ability (wage-technology) or occupation opportunity object—so its relevance is concentrated in access + identification, and I must not lean on it for the welfare layer, the decomposition, or the ability/access cut.

---

## 2. Data and setting

- **Country / years:** United Kingdom, 1997–2002 (chosen deliberately to span major tax-credit/welfare reforms, generating budget-constraint variation). [explicit, p. 2, p. 11]
- **Dataset:** UK Family Expenditure Survey (FES); the complete nonlinear budget constraint per family from the IFS-Taxben microsimulation model. [explicit, p. 2, p. 11]
- **Sample unit:** the **woman** (single or married mother) within a household with children; spouse choices and family composition are treated as fixed exogenous inputs. [explicit, p. 3, p. 11]
- **Sample size:** ≈ **10,575** women, spread fairly evenly across the six years. [explicit, p. 11, Table 1]
- **Key variables:** usual weekly hours, gross hourly wage, consumption expenditure, education (3 levels), number and age of children, cohabitation, London residence, year, birth-cohort (yob ≷ 1963). [explicit, Tables 1–3]
- **Budget-set construction:** full tax / tax-credit / welfare schedule (income support, family credit, rent rebate, local tax rebate) with large nonconvexities and flat segments (income support conditional on working < 16 h). [explicit, p. 4, Fig. 1]
- **Consumption** is used to make the static hours model life-cycle-consistent (Blundell–Walker). [explicit, p. 3]

**Transport to my France pooled 2015–2017 EUROMOD cross-section — PARTIAL.**
- *Shared:* a cross-sectional micro sample with a **microsimulated nonlinear budget set** (IFS-Taxben ↔ EUROMOD `ils_dispy`); identification leaning on **budget-constraint heterogeneity**; consumption anchored to disposable income (their FES consumption ↔ my `ils_dispy`, 2016-real). [analogy]
- *Features I do NOT have / differences:* their sample is **women-with-children only** (not my three groups: single males, single females, and couples-as-joint-unit); their offers are **hours-only**; there is **no occupation, no panel, no external instrument, no vacancy/offer data**; and their identifying budget variation is partly **reform-driven** (1997–2002), which my pooled cross-section does not exploit as a designed reform instrument. [explicit on their side; analogy on the gap]

---

## 3. Model and objects (map object-by-object to mine)

- **Choice set.** A finite hours set $\mathcal{H}=\{h_1,\dots,h_I\}$; agents choose on a **random subset** (a small number of offered points), not the universal set. The paper focuses on the **two-offer** case: two i.i.d. offers drawn from offer distribution $g$, with non-work always available. [explicit, p. 4–5, eqs. (1)–(2)]
  - *Map to my latent-jobs set:* PARTIAL analogue. My RURO engine samples a large alternative set from a proposal $\pi$ and applies a McFadden-style $-\log\pi$ correction; Beffy et al. enumerate a 2-offer consideration set and the offer density $g$ enters the likelihood **combinatorially** ($g_i^2 + 2g_i\sum_{j\ne i}g_j p_{ij}$). The "latent feasible set" *idea* is shared; the mechanics differ. [analogy + explicit]
- **Deterministic utility $v$.** $u(c,h)=\dfrac{c^{1-\gamma}}{1-\gamma}+a\,\dfrac{(L-h)^{1-\phi}}{1-\phi}$, $L=100$, additively separable, with $\ln a = Z^a\beta^a+\sigma^a\varepsilon^a$ (leisure taste-shifter). [explicit, eqs. (13),(15)]
  - *Map to my preference utility $v$:* same role (consumption + leisure). **Difference:** additively-separable CRRA-type, **not Box–Cox** (my spec). Their taste-shifters (cohabiting, youngest-kid age, number of kids, cohort) ≈ my demographic leisure shifters. [analogy]
- **Opportunity / availability mechanism analogous to my $g$:** YES, but **only one channel — hours.** $g(h\mid Z^o)$ is a discretised mixture of two truncated normals (modes part-time ≈ 15 h, full-time ≈ 38 h); the mixture weight $p_1(Z^o)$ depends on education / London / year in Model 3. [explicit, p. 12, Table 5]
  - **hours →** my **access** (hours availability). [explicit channel; analogy mapping]
  - **wage (ability):** present only as a reduced-form **wage equation** $\ln w = Z^w\beta^w+\sigma^w\varepsilon^w$ (returns to age, education, kids, London, year; dispersion $\sigma^w$)—but the wage is a **worker attribute feeding the budget $R(w,h)$**, *not* an offer/availability object. Maps to my **ability** content **by analogy only**, and the difference matters (see §5). [explicit; analogy]
  - **market / participation:** governed by **fixed costs of work** $b=Z^b\beta^b+\sigma^b\varepsilon^b$ (eq. (16)) and an always-available non-work option—**not** a separate market-offer probability. Differs from my market/employment-availability access sub-channel. [explicit]
  - **occupation:** **absent.** No ISCO / occupation / sector / industry variable at all. [explicit, by absence]
- **Budget map = my EUROMOD disposable income?** Their $R(w,h)$ = after-tax-and-benefit income from IFS-Taxben ≈ my `ils_dispy` from EUROMOD. [analogy]
- **FLAG — any attribute in BOTH utility and opportunity?** No attribute enters *both* utility and the offer mechanism. But **education** enters **both** the wage equation (human-capital / ability-like) **and** the hours-offer mixture weight (access-like) in Model 3 [explicit, Table 5]. They treat this as an exclusion-restriction design (a covariate shifting offers), not as an identification hazard. *For me:* this is a useful **precedent that education legitimately straddles the ability/access boundary**—exactly the contested re-allocation I flag as a deferred robustness. [analogy]
- **No sector/industry conflation** to flag, because there is no occupation/sector object at all. [explicit, by absence]

---

## 4. Estimation method

- **Estimator:** maximum likelihood of the two-offer sample likelihood, with a **two-step control function** for consumption endogeneity (reduced-form consumption residual $\varepsilon^c$ added as a regressor in the utility/cost/wage equations; Blundell–Powell). [explicit, p. 13]
- **Choice-set construction:** **not** a sampled-alternatives MNL over a fixed large grid; two offers drawn from $g$, with the $n$-offer generalisation noted to converge to the unrestricted model as $n\to\infty$. [explicit, p. 6]
- **Proposal / sampling density:** none in my sense (see §4b).
- **Prior/proposal correction ($-\log\pi$):** **not used.** No log-prior is subtracted from a choice index; the offer density $g$ enters the likelihood **directly** (so $g$ is simultaneously the structural object and a likelihood ingredient). My mandatory $-\log\pi$ has **no counterpart** here. [explicit, by construction of eq. (2)]
- **Normalisation / scale:** $V_I$ normalised to 0 (only utility *differences* identified); RUM with a differentiable CDF $F_{ij}$ of $\varepsilon_i-\varepsilon_j$. [explicit, p. 7]
- **Numerical method / starts:** ML; the Monte-Carlo uses **several starting values** including random starts. [explicit, Appendix C]
- **What pins preferences separately from the opportunity mechanism:** see §8.
- **Verdict — reusable for my RURO/JAX pipeline?** *Partly.* The 2-offer combinatorial likelihood is **not** portable as an estimator (my engine is sampled-MNL with an analytic log-sum). The **control-function** treatment of consumption endogeneity is a portable idea **only if** I later treat consumption as endogenous—currently I lock $c=$ `ils_dispy`, so likely not needed. The genuinely reusable content is the **identification logic** of §8, not the estimator.

---

## 4b. Proposal / sampling-of-alternatives correction  [extract even if brief]

- Largely **N/A**: there is **no McFadden sampling-of-alternatives correction**.
- The object that plays the "what's available" role is $g(h\mid Z^o)$, which is **partly individualised**: the mixture **weight** $p_1$ depends on covariates (education, London, year in Model 3) while the component means/sds ($m_1,\sigma_1,m_2,\sigma_2$) are **common**. [explicit, Table 5]
- This is a loose parallel to my **partly-individualised proposal** (in my design, wage/occupation channels are individualised, hours/employment common). The directions differ: here the offer **weight** is individualised by covariates while the hours **modes** are common; in my proposal the wage **mean** is individualised while hours/employment are common. [analogy]
- **No per-alternative log-prior is carried** (no importance sampling). Relate to my IS welfare integrator: I sample-and-reweight with a per-row $-\log\pi$; they enumerate two offers and put $g$ straight into the likelihood—conceptually $g \leftrightarrow$ my $g$, but their $g$ is never a proposal to be corrected away. [explicit; analogy]

---

## 5. Opportunity mechanism  [MOST IMPORTANT — split by channel]

**Form.** An explicit offer distribution over **hours**. Two i.i.d. draws from $g$; the agent chooses the utility-maximising offered point or non-work; likelihood $\ell_{2i}=g_i^2+2g_i\sum_{j\ne i}g_j\,p_i(\{i,j\})$. [explicit, eq. (2)] $g$ is a discretised mixture of two truncated normals on $[0,66]$ with covariate-dependent weight $p_1(Z^o)$. [explicit, p. 12]

**access (hours / market / region / year / occupation offers):**
- **hours:** YES — the core object; twin-peaked offers, part-time mode ≈ 15 h and full-time mode ≈ 38 h. [explicit, Table 5, p. 15]
- **market / participation:** via **fixed costs** $b$, not a separate offer probability; non-work always feasible. [explicit]
- **region:** London enters the fixed cost $b$ and the wage equation; in Model 3 it is also a (statistically **insignificant**) offer-weight covariate. [explicit, p. 15]
- **year:** year dummies in the offer weight (Model 3, **insignificant**) and in the wage equation. [explicit, Tables 5–6]
- **occupation offers:** **ABSENT.** [explicit, by absence]

**ability (wage technology — returns to education/experience, residual productivity):**
- Present as a **wage equation** (returns to age, education, kids, London, year; dispersion $\sigma^w$), but **not** part of $g$; the wage is a worker attribute feeding $R(w,h)$. Maps to my **ability** sub-block **by analogy**, with the explicit caveat that here the wage technology is a *reduced-form wage equation, not an opportunity density*. [explicit; analogy]

**occupation as availability vs. something else:** N/A (absent); **no sector/industry conflation** to flag. [explicit, by absence]

**Does it vary with observable circumstances?** YES — the offer **weight** varies with **education** (more educated → higher full-time-offer probability) and (insignificantly) London/year. [explicit, p. 15, Table 5] *Note:* education is placed in the **access** object here, whereas my baseline places education in **ability**; this is a concrete precedent for treating education on either side of the ability/access boundary. [analogy]

**Functional form:** mixture of two truncated normals, discretised to a pmf $g(h\mid Z^o)=p(h{+}1\mid Z^o)-p(h\mid Z^o)$. [explicit, p. 12]

**Cost of the omissions for my access/ability/preference decomposition.** Because offers are **hours-only**, the paper supports the **hours-access** channel and its identification, but provides **no** transportable content for wage(ability)-as-opportunity, occupation-as-access, or an explicit market-offer channel. Indeed, the paper's treatment of the wage as a *worker attribute* (not an opportunity object) is exactly the modelling choice my JMP departs from by folding the wage technology into $g$ (the ability sub-block). [analogy]

---

## 6. Welfare object — and its place on my $W^1$–$W^6$ map

- **Does the paper compute welfare?** **No.** [not established] There is no money-metric welfare, no equivalent income, no compensating/equivalent variation, no inclusive-value welfare object, and no reference-preference / reference-set construction. The empirical outputs are parameter estimates, model fit, rejection shares, elasticities, and behavioural **policy simulations** (employment, hours, a 10% wage increase). [explicit, §5]
- **Place on my $W^1$–$W^6$ map:** **none.** The paper cannot be located on the family map; it constructs no equivalent-income measure and takes no Ind-$y$/Ind-$A$ stance. [not established]
- **Verdict:** **incompatible** as a welfare source. Do not cite it for welfare, equivalent income, or any $W^k$.

---

## 6b. Inclusive value and money-metric inversion

- **N/A / [not established].** No log-sum/inclusive-value welfare core is computed and no own-utility map is inverted to money. The identification RUM (§3) uses a general $F_{ij}$, with IIA/logit handled as a special case in Appendix B (Lemma 3), but the **inclusive value is never used as a welfare object**, and the expectation over shocks is not taken as a welfare log-sum. [explicit; not established for welfare use]

---

## 7. Inequality / decomposition content  [three-way where relevant]

- **Inequality index:** none. [not established]
- **Decomposition rule:** none — the paper is **not** a decomposition paper (neither two-way opportunity/preference nor my three-way access/ability/preference). [not established]
- **Counterfactual construction present?** The paper **does** run structural counterfactual **simulations** — **constrained (two-offer) vs. unconstrained** employment and hours, and a 10% wage rise — but these are *behavioural* simulations, **not** welfare-inequality decompositions; nothing is "equalised/neutralised" in a welfare sense. [explicit, p. 19–21]
- **Verdict — reusable for my three-way Shapley–Shorrocks split (anchored on $W^3/W^5/W^1$)?** **No.** The only transferable *idea* is the **turn-restrictions-off counterfactual**, which loosely parallels my "equalise access" thought-experiment, but it is conducted on employment/hours (not a welfare distribution) and is **not Shapley-organised**. To serve my decomposition it would have to be re-expressed as an equalisation of a channel within a money-metric, recomputed through a welfare core, and Shapley-averaged — none of which the paper does. [analogy]

---

## 8. Identification and the separation of preferences from opportunities  [STRICT — the paper's core value to me]

The paper's central theoretical contribution is precisely my identification problem, stated cleanly for the hours-offer case.

- **Lemma 1** [explicit, p. 7]: if the offer distribution $g$ is **known**, preferences (the random utilities $V_i$) are **identified** — the system $\ell_i=g_i^2+2g_i\sum_{j\ne i}g_j F_{ij}(V_i-V_j)$ has at most a unique $V$ (proof via Gale–Nikaido, dominant-diagonal Jacobian).
- **Lemma 2** [explicit, p. 8]: if the choice probabilities $p_{ij}$ are **known**, the offer distribution $g$ is **recovered** uniquely (Brouwer fixed point on a simplex map; uniqueness via dominant diagonal).
- **Joint problem:** **without restrictions, $g$ and the preferences are NOT separately identified** (Lemmas 1+2 together). [explicit, p. 8]
- **Three routes to joint identification:**
  1. **Parametric** (3.3.1) [explicit, p. 9]: restrict $g(\gamma)$ and $p(\beta)$ to finite parameters with $\dim[\beta:\gamma]\le I-1$, and require full column rank of $\Pi=[\partial Q/\partial\beta,\ \partial Q/\partial\gamma]$ (eqs. (7)–(12)). Flat budget segments give $\partial p_{ij}/\partial\beta=0$ for some pairs (those pairs inform $g$, not preferences).
  2. **Semi-parametric via exclusion restrictions** (3.3.2) [explicit, p. 9–10]: a covariate $Z$ (e.g. wage / other income) that shifts the **budget constraint $R$** without shifting the **offer distribution $g$**; identification requires enough variation in $Z$ (with discrete $Z$ over $K$ values: $(I-1)\times K$ likelihood contributions vs. $I-1+\dim(\beta)$ unknowns).
  3. **Nonparametric via dominated regions** (3.3.3) [explicit, p. 11]: where the nonlinear budget has flat/decreasing segments, dominated hours satisfy $p_{ij}=1$ regardless of $\beta$, so Lemma 2 recovers $g$ on that subpopulation, after which Lemma 1 recovers preferences on households facing increasing budgets.
- **Monte-Carlo recovery** (Appendix C, Tables 13–14) [explicit, p. 23–30]: with a **single** budget constraint, estimates are biased/imprecise (preference parameters especially, when the budget is near-linear); with **≥ 2 distinct** budget constraints, recovery is well-behaved. Budget-constraint heterogeneity functions as the exclusion variable.

**Transport to my France pooled cross-section (no panel, no external instrument):**
- The **exclusion-restriction logic transports in spirit** [analogy]: EUROMOD's nonlinear tax-benefit schedule generates household-specific **budget-constraint heterogeneity** (via demographics, region, other income) that shifts $R$ without (by assumption) shifting the opportunity density — a legitimate identification source I share. *(That budget heterogeneity identifies the split is [explicit]; that EUROMOD supplies it for me is [analogy].)*
- The **dominated-regions** route also transports in principle (EUROMOD nonconvexities exist). [analogy]
- Crucially, my **certification is by synthetic recovery at production resolution**, which is the *same epistemic move* as their Monte-Carlo recovery. This is published support that (i) parametric RURO-type identification must be *demonstrated by recovery*, and (ii) **budget-constraint heterogeneity is what makes recovery succeed** — directly arming me against the "your separation is mechanical / functional-form-driven" referee. [analogy]
- **Honest caveat:** Beffy et al. identify a **hours-offer distribution vs. preferences**. They do **not** identify a wage- or occupation-offer distribution, so they provide **no transportable identification argument for my ability-vs-access split**. That finer cut rests on my own functional-form + synthetic-recovery argument, not on this paper. [explicit limitation; analogy on consequence]

---

## 9. Key results and magnitudes

- **Nonparametric rejection:** ≈ **2.6%** of working women observed at strictly dominated hours; an additional **0.4%** would earn more out of work. [explicit, p. 16–17, Table 8]
- **Parametric rejection** at the Model-3 $\phi$: **7.9%** of working women violate the revealed-preference inequality. [explicit, p. 17–18, Tables 8–9]
- **Offer modes:** part-time ≈ **15 h**, full-time ≈ **38 h**; more educated women have higher full-time-offer probability; no significant location/year offer differences. [explicit, p. 15, Table 5]
- **Frisch elasticity (mean):** 0.58 (M1) / 0.59 (M2) / **0.30** (M3). **Marshallian (mean):** 0.58 / 0.48 / **0.20** (M3). [explicit, Table 10, p. 19] — accounting for unobserved-heterogeneity correlations and offer heterogeneity roughly **halves** the elasticities.
- **Employment:** **71%** unconstrained vs. **62.5%** constrained; mean hours **35.5** vs. **26.2**. [explicit, p. 19]
- **10% wage rise:** intensive margin **0.35** (unconstrained) vs. **0.16** (constrained); extensive **0.25** vs. **0.27**. [explicit, Table 11, p. 21]
- **Who is constrained:** poorer households, shorter hours, lower wages, more often lone mothers. [explicit, Table 9, p. 17–18; abstract]
- **Benchmark for me:** that estimated preferences/elasticities move *materially* once hours restrictions are modelled is direct evidence for my **sub-question 1** (unmodelled opportunity is absorbed into estimated tastes). The magnitudes (elasticities ≈ halving; employment 71→62.5) give a plausibility range for "how much do restrictions matter," but on **UK women-with-children**, not France — use as order-of-magnitude only. [explicit numbers; analogy on benchmarking]

---

## 10. Estimators, theorems, or formal results

- **Lemma 1** — *Given $g$, at most one $V$ (with $V_I=0$) solves $\ell_i=g_i^2+2g_i\sum_{j\ne i}g_j F_{ij}(V_i-V_j)$.* Assumptions: $\ell,g$ in the positive simplex; $F_{ij}$ differentiable. Technique: (i) stack $I-1$ equations; (ii) show Jacobian is a dominant-diagonal matrix; (iii) invoke Gale–Nikaido for univalence. **Reuse verdict:** the *identification logic* is reusable; the estimator is not (my likelihood is a sampled-MNL log-sum). [explicit]
- **Lemma 2** — *Given $p_{ij}$ (with $p_{ij}+p_{ji}=1$), a unique $g$ in the simplex solves $\ell_i=g_i^2+2g_i\sum_{j\ne i}g_j p_{ij}$.* Technique: Brouwer fixed point for existence + dominant-diagonal univalence for uniqueness. **Reuse:** logic reusable as the "recover offers given choices" half. [explicit]
- **Lemma 3** (Appendix B, IIA/logit special case) — analogous unique-solution result under IIA, $\ell_i=g_i^2+2g_ip_i\sum_{j\ne i}g_j/(p_i+p_j)$. **Reuse:** closest to my MNL setting (logit special case), but still 2-offer-structured; reusable as a conceptual bridge, not as my estimator. [explicit]
- **Rank condition** (eqs. (7)–(12)) — full column rank of $\Pi$ for joint parametric identification. **Reuse:** a *template* for arguing my parametric identification, but I rely on synthetic recovery rather than an explicit rank proof. [explicit; analogy on reuse]

---

## 11. Robustness and specification sensitivity

- **Number of offers:** the two-offer model is acknowledged restrictive; it converges to the standard unrestricted model as $n\to\infty$. [explicit, p. 6, p. 22] → informs my **choice-set-size sensitivity** (101 singles / 901 couples).
- **Single vs. multiple budget constraints (Monte-Carlo):** a single budget constraint → biased/weak recovery (preferences worst when the budget is near-linear); dominated regions → precise $g$ but **less precise preferences**; combining constraints → recovers both. [explicit, Tables 13–14, p. 23–30] → informs my **recovery/stability tests** and the **effective-information** concern.
- **Three model variants** (M1 exogenous wage/consumption; M2 correlated unobservables; M3 covariates in the offer weight): **M3 fits the hours distribution best.** [explicit, p. 15–16, Fig. 2, Table 8] → supports adding **circumstance covariates to the access channel**.
- **Identification trade-off:** dominated budget regions sharpen $g$ but blur preferences; monotone budgets sharpen preferences. [explicit, p. 9, p. 30] → **corroborates** my reported standard-error asymmetry (tight opportunity block, wide preference block) as a *generic feature of this model class*, not a defect. [analogy]

---

## 12. What I can cite this paper for

- That a structural labour-supply model can **separate preferences from an estimated offer (opportunity) distribution**, with formal identification conditions (Lemmas 1–2, §3). [explicit]
- That **budget-constraint heterogeneity / nonlinear tax-benefit variation** is an identification source for the offer-vs-preference split, **demonstrated by Monte-Carlo recovery** (§3.3, Appendix C). [explicit]
- That observed **twin-peaked hours reflect hours-offer restrictions**, not preferences alone, with ≈ 2.6% nonparametric and 7.9% parametric rejection of the unrestricted model (§2.2, §5.3). [explicit]
- That **accounting for hours restrictions materially changes estimated preferences/elasticities and counterfactual employment** (§5). [explicit] — support for my sub-question 1.
- As the canonical **consideration-set / restricted-choice antecedent** of my access channel and as motivation for modelling a household-specific feasible set (Intro, §2.3). [explicit]
- That **near-linear/monotone budget constraints weakly identify the offer distribution, while dominated regions weakly identify preferences** (Appendix C). [explicit]

---

## 13. What I should NOT cite this paper for  [overclaim risks]

- **No welfare content.** Do not cite for any welfare, equivalent-income, money-metric, CV/EV, or inclusive-value-as-welfare claim — the paper computes none.
- **No decomposition.** Do not cite for any inequality index or decomposition (two-way *or* three-way) — it is not a decomposition paper.
- **Hours-only opportunity.** Do not present its offer distribution as covering **wage/ability**, **occupation**, or **market** opportunity. Offers are hours-only; the wage is a worker attribute; occupation is absent.
- **Random-opportunity framing (boundary flag).** The paper uses a genuinely **random** offer-draw framing (choices made on a random subset of possible hours). My JMP treats opportunities as **deterministic feasible sets** (the "RO" in RURO is estimation machinery). Cite this paper as **random-consideration-set** and explicitly differentiate it from my deterministic stance; do not import its randomness as if it were mine.
- **Not a sampled-MNL-with-log-sum estimator.** It is a 2-offer combinatorial likelihood in which $g$ sits *inside* the likelihood; it has **no $-\log\pi$ proposal correction**. Do not describe it as my estimation machinery.
- **Theory-paper boundary.** Nothing here is the Haydar–Maniquet axioms/characterisation. Do not attribute any $W^1$–$W^6$ reading or normative claim to this paper, and do not read this paper as a theory contribution.
- **Population caveat.** UK women-with-children, 1997–2002. Do not generalise its magnitudes to my French three-group sample without qualification.

---

## 14. Direct quotes worth citing

> **Note on reproduction.** I am keeping verbatim reproduction minimal. One short verbatim
> quote is given; the remaining entries are **page-located paraphrases** so you can pull
> the exact wording yourself from the open-access (CC-BY) PDF if you want a verbatim
> citation. This is deliberate, not an omission.

- **Verbatim (abstract, p. 1):** "observed hours reflect both the distribution of preferences and restrictions on choices."
- **Paraphrase, intro (p. 1–2):** the standard unrestricted-hours model has long been recognised as ill-suited to distinguish individual preferences from external (demand-side) constraints. [locator for verbatim pull]
- **Paraphrase, intro (p. 2):** their interpretation is rational choice from a set of job *packages* limited by the hours employers offer (a labour-supply analogue of the consideration set). [locator]
- **Paraphrase, §2.3.2 / conclusion (p. 6, p. 22):** as the number of offers grows the model converges to the standard unrestricted-choice model. [locator]
- **Paraphrase, Monte-Carlo conclusion (p. 31):** estimates are well-behaved when the simulated population faces two different budget constraints, and biased when it faces only one. [locator]

---

## 15. Open questions and risks for my draft

- **"What is your $Z$?"** Their identification leans on budget-constraint heterogeneity + dominated regions + an exclusion restriction shifting $R$ but not $g$. My pooled cross-section has no reform instrument, so I must **name the concrete EUROMOD shifters** (demographic / regional / other-income variation in the tax-benefit map) that play the role of their $Z$ — the referee will ask.
- **Ability-vs-access has no precedent here.** This paper identifies hours-offers vs preferences only; the identification of my finer **ability/access** cut is entirely my own burden (functional form + synthetic recovery) and cannot be propped up with this citation.
- **Random vs deterministic framing.** I must reconcile the lineage in prose: borrow the restricted-choice *machinery* and identification logic while making clear my opportunities are deterministic feasible sets, not random draws.
- **Weak preference identification under near-linear budgets.** Their Monte-Carlo warns that near-linear budgets weakly identify preferences. This **corroborates** my wide singles-preference block as a generic feature — but a referee could equally read it as a weak-identification risk; I should frame it as identification-with-imprecision and lean on synthetic recovery.
- **Consumption endogeneity.** They model it with a control function; I lock $c=$ `ils_dispy`, which removes that endogeneity channel. I should note this as a deliberate simplification (a channel they had to model that I sidestep), not pretend the issue is absent.

---

## 16. TL;DR for retrieval

Beffy, Blundell, Bozio, Laroque & Tô (2019, *J. Econometrics*) estimate a structural labour-supply model in which observed hours reflect both preferences and an estimated **hours-offer distribution** $g$, and prove that preferences and $g$ are *separately* identified given budget-constraint heterogeneity, exclusion restrictions, and dominated regions — making this my primary citation for the **access** channel and for the **identification** backbone (and, via its Monte-Carlo recovery, for my synthetic-recovery standard). It is hours-only and contains **no ability/occupation opportunity object, no money-metric welfare, no inclusive value, and no inequality decomposition**, so it must not be cited for the welfare layer, the three-way decomposition, or the ability/access cut. Its **random-offer** framing must be explicitly differentiated from my **deterministic** feasible sets, and none of it touches the companion Haydar–Maniquet theory paper.
