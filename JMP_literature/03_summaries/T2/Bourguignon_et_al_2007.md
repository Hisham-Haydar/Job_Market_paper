# Bourguignon, Ferreira & Menéndez 2007 — Inequality of Opportunity in Brazil

> Extraction produced under `JMP_T1_exhaustive_extraction_prompt_v2.md`.
> Source of truth: the attached PDF (*Review of Income and Wealth*, Series 53,
> No. 4, December 2007, pp. 585–618). Page numbers cite the printed journal
> pagination. Relevance is anchored to `JMP_project_state_v1.md` and
> `JMP_welfare_spec_v5.md`; my project design is **not** imported into the
> reading of this paper. Throughout I distinguish **explicit-in-source**,
> **derived-by-analogy**, and **not-established**.

---

## 0. Metadata

- **BibTeX key:** bourguignon2007inequality [verify exact key against my .bib]
- **Authors:** François Bourguignon (The World Bank); Francisco H. G. Ferreira (The World Bank, corresponding author); Marta Menéndez (Université Paris Dauphine and INRA, Paris-Jourdan). [explicit, p. 585]
- **Year:** 2007. [explicit]
- **Outlet:** *Review of Income and Wealth*, Series 53, Number 4, December 2007, pp. 585–618. [explicit, running heads]
- **DOI/URL:** [uncertain, needs verification — not printed on the PDF]
- **PDF filename:** `Bourguignon_et_al_2007_INEQUALITY_OF_OPPORTUNITY_IN_BRAZIL.pdf`
- **Tier:** T1A.
- **JMP block(s) served:** **decomposition** (primary); **opportunity-mechanism / normative-interpretation** (the circumstance/effort cut and its compensatory reading); **motivation** (a canonical magnitude benchmark for "opportunity share of inequality"). It does **not** serve the estimation, identification-of-preferences, welfare-construction, or data-infrastructure blocks for my design.

---

## 1. One-paragraph relevance to my JMP

This is the canonical reduced-form template for the object my decomposition layer reports: a **counterfactual-equalisation share of inequality attributable to factors beyond the individual's control**. It defines the opportunity share $\Theta_I = [I(F) - I(\tilde\Phi)]/I(F)$, where $\tilde\Phi$ is the earnings distribution simulated under equalised circumstances, and it further splits that share into a **direct** and an **indirect** component — a structure that prefigures the *anatomy* of my Shapley equalisation even though the mechanism is entirely different. For my **access** channel it is the closest classical antecedent (circumstances = factors outside individual control = the access/ability side of my cut); it has **nothing** to say about my **preference** channel, because it contains no utility function and no behavioural model — taste heterogeneity is silently absorbed into the residual. Its single most transportable methodological contribution is the **partial-identification / bounding** strategy (Monte-Carlo over admissible regressor–residual correlations) that turns an un-identified omitted-variables problem into a reported interval; this is directly relevant to my defence against the "your decomposition is mechanical" referee, though my own identification rests on synthetic recovery rather than on their sign-restricted correlation bounds.

---

## 2. Data and setting

- **Country/year:** Brazil, 1996 (a single cross-section). [explicit, p. 591]
- **Dataset:** PNAD 1996 (*Pesquisa Nacional por Amostra de Domicílios*), the annual household survey of IBGE; 1996 is used because that wave carries a special supplement on parental education and father's occupation. [explicit, pp. 591–592]
- **Sample unit:** individuals (prime-age males who are household heads or spouses). [explicit, p. 591]
- **Sample size:** the full PNAD 1996 is upward of 330,000 individuals; after restricting to urban active males aged 26–60 reporting positive earnings the sample is 37,548, falling to **28,474** after dropping observations with missing parental education/occupation. [explicit, p. 591]
- **Cohort structure:** the sample is split into seven 5-year birth cohorts, 1936–40 through 1966–70, analysed separately. [explicit, p. 592]
- **Key variables:**
  - *Outcome:* log real hourly earnings from all occupations. [explicit, pp. 592, 602 table note]
  - *Circumstances $C$:* race (Black & mixed-race vs White & Asian); region of birth; mean parental schooling; mother−father schooling difference; father's occupational status (three regrouped levels: lower / medium / higher). [explicit, pp. 592–593, 596]
  - *"Efforts" $E$:* own years of schooling; a migration dummy; labour-market status (formal employee/employer, informal employee, self-employed). [explicit, pp. 593, 596–597]
- **Budget-set construction:** **N/A** — there is no budget set, no tax-benefit map, and no choice problem; the object is an earnings regression, not a labour-supply model.
- **Transport to my France pooled 2015–2017 EUROMOD cross-section:** the *cross-sectional, single-wave, no-panel* character transports well — like me, they have neither a panel nor an external instrument and must identify a counterfactual from a single cross-section. What I do NOT share, and what they exploit, is **observed family-background circumstances** (parental education, father's occupation) — my circumstances are labour-market-side (access/ability in $g$), not intergenerational. What they do NOT have, and I do: an estimated structural model, a preference object, an explicit feasible-set/opportunity density, and a money-metric welfare layer. [explicit on their side; the contrast is derived-by-analogy]

---

## 3. Model and objects (map object-by-object to mine)

- **Choice set vs my latent-jobs set:** **none.** There is no choice set and no latent-jobs object. [explicit — the model is a reduced-form earnings function]
- **Deterministic utility vs my preference utility $v$:** **none.** There is no utility function; "efforts" are *observed proxies*, deliberately kept in quotation marks because they are themselves shaped by circumstances and luck rather than derived from optimisation. [explicit, pp. 592–593] My preference channel has **no analogue** here.
- **Opportunity/availability mechanism vs my $g$:** **no density-over-alternatives mechanism.** "Opportunity" is operationalised as the **effect of exogenous circumstance variables on earnings**, in the Roemerian circumstance/effort tradition, not as a feasible-set or offer distribution. There is no separation into hours / wage(ability) / market-participation / occupation channels; the only internal split is **direct effect on earnings** vs **indirect effect through "effort" variables** (§4 below). [explicit, pp. 593–595]
- **Budget map vs my EUROMOD disposable income:** **N/A** (no budget map).
- **Job attribute entering BOTH utility and opportunity:** **N/A by construction** — there is no utility block, so the double-entry hazard my prompt flags cannot arise here. Worth noting for contrast: father's occupational status enters as a **circumstance**, and the individual's own labour-market status enters as an **"effort"**; occupation-type objects therefore appear on *both* sides of *their* circumstance/effort cut, but this is a parent-vs-own distinction, not a utility-vs-opportunity double entry. [explicit, pp. 592–593]
- **The core model equation (explicit, p. 593, eq. 2):**
$$ w_i = f\big(C_i,\; E_i(C_i, v_i),\; u_i\big), $$
with the log-linear empirical form (explicit, pp. 596–597, eqs. 5–6):
$$ \ln w_i = \alpha C_i + \beta E_i + u_i, \qquad E_i = H C_i + v_i. $$
Substituting gives the reduced form (explicit, p. 597, eqs. 9–10):
$$ \ln w_i = \psi C_i + \varepsilon_i, \qquad \psi = \alpha + \beta H,\; \varepsilon_i = \beta v_i + u_i. $$

---

## 4. Estimation method

- **Likelihood/estimator:** ordinary least squares on the log-earnings equation, run **separately by cohort**; both the "full" equation (7) with circumstances *and* efforts and the reduced form (10) with circumstances *only* are estimated by OLS. [explicit, pp. 596–597, 601]
- **Choice-set construction / grid / proposal density:** **N/A** — no discrete choice, no sampling of alternatives.
- **Prior/proposal correction ($-\log\pi$):** **N/A** — there is no choice index and no McFadden-type correction; the question does not arise.
- **Normalisation/scale:** standard OLS; dependent variable in logs; circumstance/effort regressors as described in §2.
- **Numerical method / starting values / multistart:** **N/A** (closed-form OLS).
- **What pins down "preferences" separately from "opportunities":** nothing, because there are no preferences in the model. What is separated is the **direct** circumstance effect (coefficients $\alpha$ in the full equation, holding efforts fixed) from the **total** circumstance effect (coefficients $\psi$ in the reduced form, letting efforts adjust); the indirect effect is the residual $\psi - \alpha = \beta H$. [explicit, pp. 596–597]
- **Verdict — reusable for my RURO/JAX pipeline?** **No** for the estimator itself (OLS earnings regression is not a structural discrete-choice estimator). **Yes, conceptually,** for the *counterfactual-construction logic*: simulate an equalised distribution, recompute the inequality index, take the proportional fall as the share. That logic survives transplant into my Shapley layer; the regression engine does not.

---

## 4b. Proposal / sampling-of-alternatives correction  [extract even if brief]

**N/A.** The paper has no sampling of alternatives, no proposal distribution, and no importance-sampling integrator. There is therefore nothing to relate to my proposal-individualisation concern. Recording this explicitly so the section co-indexes with T1 sources that *do* have a proposal correction: this source contributes **zero** to my 4b design.

---

## 5. Opportunity mechanism  [MOST IMPORTANT — be exhaustive; split by channel]

**Functional form of "opportunity."** Opportunity is *not* modelled as feasibility, availability, or an offer distribution. It is the **causal contribution of exogenous circumstance variables to earnings**, in Roemer's (1998) circumstance/effort partition. Equality of opportunity is defined distributionally: it would obtain if the earnings distribution were independent of circumstances, $F(w\mid C) = F(w)$. [explicit, pp. 593–595] Given the structural form (2), this requires both (i) circumstances have no direct effect on earnings conditional on efforts, and (ii) efforts are distributed independently of circumstances. [explicit, p. 595] The empirical strategy uses the **equality-of-circumstances benchmark** $C_i = \bar C\;\forall i$, which is sufficient (not necessary) for equality of opportunity, and constructs the counterfactual earnings distribution $\tilde\Phi(w)$ under that benchmark. [explicit, p. 595]

**Mapping to my three sub-objects:**

- **access** (hours / market-participation / region / year / occupation offers): **no direct analogue.** Their nearest objects are *region of birth* (a circumstance) and *labour-market status* (an "effort"). Region of birth is a circumstance that could be read as a coarse access proxy, but it is a *background* circumstance, not a feasible-set or local-labour-demand object. There is no hours availability, no participation margin, no occupation-offer distribution. [derived-by-analogy; the access reading is mine, not theirs]
- **ability** (wage technology — returns to education and experience, residual productivity): their **own schooling** is an "effort", not an ability/opportunity object, and there is no estimated wage technology in the structural sense — returns to schooling appear as an OLS coefficient on own years of schooling, not as an identified productivity primitive. *Parental* education and father's occupation are the circumstances that shift earnings, partly *through* own schooling (the indirect channel). So the closest thing to my "ability" content sits on their **effort** side, with its *circumstance-driven part* attributed to opportunity via the indirect effect. [explicit on the variables; the ability mapping is derived-by-analogy]
- **occupation as availability vs something else:** occupation appears **twice** and neither use is my access object. *Father's* occupational status is a **circumstance** (a determinant of opportunity); the individual's own **labour-market status** (formal/informal/self-employed) is an **"effort."** Both are realised positions, not offer/availability distributions. [explicit, pp. 592–593]
- **sector/industry conflation flag:** the paper does **not** use NACE/industry; "occupation" here is a sociological status classification (a nine-level scheme regrouped to three). [explicit, p. 593] No `loc4`/`lindi` conflation risk arises *in the source*; the discipline note for my draft is only that I must not describe their father's-occupation circumstance using my own occupation-as-access vocabulary.

**The internal channel split they DO have (direct vs indirect).** This is the structurally interesting part for me. The overall opportunity share captures *both* the direct effect of circumstances on earnings (the $\partial f/\partial C$ channel) and the indirect effect operating through circumstance-shaped efforts ($G(E\mid C)$). [explicit, pp. 595–596] The direct share is computed from the full equation (5'); the overall share from the reduced form (10); the indirect share is their difference. [explicit, pp. 596–597]

**Cost of the omission for my decomposition.** Because there is no explicit feasible-set mechanism, their framework cannot distinguish a worker with good circumstances in a depressed local market from one with the same circumstances in a thriving market — exactly the access variation my opportunity density exists to capture. Their "opportunity" is **background-circumstance opportunity**, not **labour-market-feasibility opportunity**. For my three-way cut, this source informs the *reporting form* of the share and the direct/indirect anatomy, but supplies no mechanism for the access or ability channels. [derived-by-analogy]

---

## 6. Welfare object — and its place on my $W^1$–$W^6$ map

- **Does the paper compute welfare?** **No.** The decomposed object is **observed earnings inequality** (a Theil index, with a Gini robustness check), not a welfare or equivalent-income object. [explicit, pp. 607–608]
- **Money-metric / equivalent income / EV / CV / log-sum:** none of these. [explicit — there is no preference map to invert]
- **Universal vs constrained set:** **N/A** (no choice set).
- **Reference price / preference / bundle / set:** the only "reference" is the **equality-of-circumstances benchmark** $\bar C$ used to build the counterfactual *earnings* distribution; it is a reference on the *circumstance vector*, not a reference preference or reference opportunity set. [explicit, p. 595]
- **Discrete-choice subtleties (log-sum, selection, Hicksian/Marshallian, integration over heterogeneity, ex-ante/ex-post):** **N/A** across the board.
- **Location on my $W^1$–$W^6$ map:** the paper contains **no** $W^1$–$W^6$ object and **no** Independence-of-$y$/Independence-of-$A$ construction; it must **not** be cited as containing them. The *only* legitimate connection is normative-spirit: its compensatory motivation (inequality from factors beyond individual control is "more objectionable") is the same ethical premise that animates the compensation end of my spectrum. That is a *motivational* alignment, not a measure correspondence. [explicit motivation, pp. 585–586; the non-correspondence is established]
- **Verdict:** **incompatible** as a welfare construction (there is none); **adaptable** only at the level of the counterfactual-share *reporting object*, which operates on an inequality index of an outcome, not on a welfare distribution.

---

## 6b. Inclusive value and money-metric inversion  [extract if the paper uses a log-sum or an EV/CV]

**N/A.** No inclusive value, no log-sum, no EV/CV, no one-dimensional own-utility inversion, no expectation over extreme-value shocks (analytic or simulated). The paper's counterfactual is constructed by re-evaluating a fitted OLS earnings equation under equalised circumstances, $\tilde w_i = \exp(\hat\psi \bar C + \hat\varepsilon_i)$, not by inverting a utility map. [explicit, p. 597] Contributes nothing to my analytic-in-shocks importance-sampling inversion.

---

## 7. Inequality / decomposition content  [three-way where relevant]

- **Inequality index:** Theil (headline); Gini reported as a robustness check (cohort-average opportunity share 13% under Gini vs 23% under Theil). [explicit, pp. 607–608]
- **Decomposition rule:** a **counterfactual-equalisation / regression-based** decomposition, not Shapley and not Shorrocks. The overall opportunity share is
$$ \Theta_I = \frac{I(F) - I(\tilde\Phi)}{I(F)}, $$
explicitly flagged as **index-contingent** (the subscript $I$). [explicit, p. 595, eq. 3] The direct/indirect sub-decomposition is
$$ \Theta_I^d = 1 - \frac{I(\tilde\Phi^d)}{I(F)}, \qquad \Theta_I^{\text{indirect}} = \Theta_I - \Theta_I^d. $$
[explicit, p. 596, eq. 4 — I have rewritten the printed expression in clean notation; verify against the source typographic form]
- **Counterfactual construction — what is equalised / neutralised / held fixed / zeroed:**
  - *Overall share:* equalise circumstances $C_i \to \bar C$ in the **reduced form**, so circumstances are neutralised both directly and through their effect on efforts; residual $\hat\varepsilon_i$ is held at its observed value. [explicit, p. 597]
  - *Direct share:* equalise circumstances in the **full equation** while holding observed efforts $E_i$ fixed; this zeroes the direct channel only. [explicit, p. 596]
  - *Individual-circumstance contributions:* equalise one circumstance at a time, holding the others at observed values. [explicit, pp. 611–612]
  - *Upper-bound thought experiment:* treat all observed "efforts" as circumstances (equalise everything observed), leaving only $u$ as genuine effort. [explicit, pp. 608–609]
- **Order-independence / path-independence / exhaustiveness:** **not addressed as such.** The decomposition is *not* claimed to be order-independent or exhaustive in the Shapley sense; the individual-circumstance equalisations are "controlling for all others" but the paper does **not** Shapley-average over orderings, so the single-circumstance contributions need not sum to the overall share. [explicit method, p. 611; the absence of a Shapley property is established by what the paper does not claim]
- **Verdict — reusable for my three-way access/ability/preference Shapley–Shorrocks split anchored on $W^3/W^5/W^1$?** **Partially, and only at the conceptual level.** The *share-of-inequality-from-equalising-X* object and the *direct-vs-indirect anatomy* transplant cleanly into my Shapley framing. But the decomposition here is **two-way at most** (circumstance vs residual, where the residual silently bundles effort, preference heterogeneity, luck, and measurement error) and is **regression-based, not Shapley**. To reach my three channels it would have to be extended by (i) replacing the OLS-counterfactual engine with the structural welfare object, (ii) splitting the opportunity side into access vs ability — which their data cannot do, since they have no wage-technology/feasible-set separation — and (iii) imposing Shapley order-averaging to obtain exhaustiveness, which they do not do. So the source is an **antecedent and a reporting template**, not a reusable estimator. [derived-by-analogy + established]

---

## 8. Identification and the separation of preferences from opportunities  [STRICT]

- **What identifies the share:** there is **no causal point-identification**. The residual $u$ (and $\varepsilon$) is acknowledged to be correlated with the regressors because of unobserved circumstances and efforts; an IV strategy is rejected as infeasible (no plausible exclusion restrictions for circumstance variables). [explicit, pp. 597–598] Instead the paper uses a **partial-identification / bounding** strategy: it treats the regressor–residual correlation vector $\rho_{Xu}$ as unknown, draws it from a uniform distribution on $(-1,1)$, **discards draws** that violate (a) positive-semi-definiteness of the implied covariance matrix (equivalently $K \le 1$) and (b) four economically-motivated sign restrictions on key coefficients, and reports the resulting interval of bias-corrected coefficients as a **90% interval**. [explicit, pp. 598–600]
- **Preferences vs constraints:** the paper does **not** attempt this separation — it has no preference object. Its separation is **circumstance vs effort**, with effort itself partly circumstance-driven. The honest statement for my purposes: this source separates *background opportunity* from *everything else*, and the "everything else" includes the preference heterogeneity my paper exists to isolate. [explicit / established]
- **Ability vs access within the opportunity side:** **not done.** No internal split of the opportunity side into a pay/ability dimension and a feasible-set/access dimension exists here. [established]
- **Transport to my France pooled cross-section (no panel, no external instrument):** the *spirit* transports — both designs confront a single cross-section without instruments and must reason about an un-identified counterfactual. But their specific device (sign-restricted, PSD-constrained correlation bounds on an OLS earnings equation) is **not** my device; my baseline is certified by **synthetic recovery**, not by in-sample fit and not by their correlation-bound intervals. The transportable lesson is the *posture* — report a defensible interval rather than a falsely precise point — not the mechanism. [explicit on their side; the transport judgment is derived-by-analogy]
- **Referee defence ("your decomposition is mechanical"):** this paper is a useful citation that a respected literature *accepts a reduced-form, partially-identified opportunity share as informative* precisely because it is transparent about what it cannot identify. It does **not**, however, license any claim that the share is causal; it is explicitly a measure of the share *associated with observed circumstances*, conditional on maintained assumptions. Do not soften this when citing. [explicit, pp. 597–600, 614]

---

## 9. Key results and magnitudes

All magnitudes refer to **urban Brazilian males aged 26–60 with positive earnings, 1996**, by birth cohort unless stated. [explicit, p. 591]

- **Overall opportunity share (Theil):** five observed circumstances account for **10–37%** of within-cohort earnings inequality; **15–37%** excluding the youngest cohort; cross-cohort simple average of mean estimates ≈ **23%**. [explicit, pp. 607, 614]
- **Worked cohort example (1941–45):** equalising circumstances reduces the Theil index from **0.997** to a counterfactual **0.632–0.675** (mean 0.656), i.e. a **32–37%** opportunity share. [explicit, p. 607]
- **Gini robustness:** cohort-average opportunity share ≈ **13%** under the Gini (vs 23% under Theil) — a sizeable index-sensitivity. [explicit, p. 607]
- **Direct vs indirect split:** on average ≈ **60%** of the circumstance effect operates **directly** on earnings (conditional on observed efforts), ≈ **40%** indirectly through efforts; the direct-to-overall ratio averages ≈ **61–62%** with a wide bounded interval (≈ **29–82%** excluding the youngest cohort). [explicit, pp. 608–609, 614]
- **Upper-bound thought experiment (all observed efforts treated as circumstances):** opportunity share averages ≈ **36%**, bounded ≈ **23–48%** across cohorts. [explicit, pp. 608–609]
- **Individual circumstances:** **parental education** is the dominant single circumstance across all cohorts; **father's occupation** second; **race** matters and is relatively more important for younger cohorts; **region of birth** contributes little once race and family background are controlled (≈ 1–2% of inequality). Parental schooling alone accounts for ≈ 65–70% of the total observed-circumstance effect, rising to ≈ 80% when father's occupation is added. [explicit, pp. 611–614]
- **Returns to own schooling (an "effort" coefficient):** ≈ **9–12%** per year (bounds ≈ 8–13%), lower than some prior Brazilian estimates, attributed to including parental-background controls. [explicit, p. 603]
- **Cross-cohort pattern:** weak evidence that the opportunity share declines for younger cohorts, but the authors caution that cohort, age, and period effects cannot be separated in a single cross-section, and that the youngest cohort's estimate is fragile (part-time incidence inflating residual variance). [explicit, pp. 610–611]

**Benchmarking value for me:** a 10–37% (central ≈ 23%) circumstance share against *earnings* inequality is a coarse plausibility anchor for the magnitude of an opportunity share, but it is **not** directly comparable to my welfare-inequality opportunity surface — different outcome (earnings vs money-metric welfare), different circumstances (family background vs labour-market access/ability), different index treatment, and different decomposition rule. Use it as an order-of-magnitude sanity check only, with the non-comparability stated. [derived-by-analogy]

---

## 10. Estimators, theorems, or formal results

This is an applied paper; there are **no theorems**. The reusable formal objects are definitions/estimators:

1. **Overall opportunity share (p. 595, eq. 3).**
   - Statement: $\Theta_I := \dfrac{I(F) - I(\tilde\Phi)}{I(F)}$, with $\tilde\Phi$ the counterfactual earnings CDF under equalised circumstances.
   - Assumptions: a (possibly biased) reduced-form earnings model; an inequality index $I$; the equality-of-circumstances benchmark as the equalisation operator.
   - Technique: fit reduced form by OLS; simulate $\tilde w_i = \exp(\hat\psi\bar C + \hat\varepsilon_i)$; recompute $I$; take the proportional fall.
   - Reusability verdict: **maybe / conceptual yes** — the *form* of the share is reusable as my reporting object; the *engine* (OLS earnings) is replaced by my structural welfare object, and the *equalisation* is replaced by channel-equalisation in $g$ with Shapley averaging.

2. **Direct (partial) share (p. 596, eq. 4).**
   - Statement: $\Theta_I^d := 1 - \dfrac{I(\tilde\Phi^d)}{I(F)}$, with $\tilde\Phi^d$ the distribution that equalises circumstances in the earnings equation while holding observed efforts fixed.
   - Reusability verdict: **conceptual yes** — this is the antecedent of decomposing an opportunity effect into a piece that flows through the direct evaluation and a piece that flows through behaviourally-mediated channels; loosely analogous to my distinction between the direct evaluation channel and the attainment channel, though the mechanisms differ entirely. State the analogy as loose, not exact.

3. **Bias-bounding procedure (pp. 598–600).**
   - Statement: treat $\rho_{Xu}$ as unknown; the OLS bias is $B = (X'X)^{-1}\mathrm{cov}(X,u)$; draw $\rho_{Xu}\sim U(-1,1)$ componentwise; retain draws with $K \le 1$ (PSD of the implied covariance) and satisfying four sign restrictions; report a 90% interval over retained draws.
   - Reusability verdict: **no** for my pipeline (I use synthetic recovery and cluster-robust bootstrap), but a **citable precedent** for reporting an opportunity share as a defensible interval rather than a point.

---

## 11. Robustness and specification sensitivity

What they vary and what moves: [explicit unless noted]
- **Inequality index:** Theil → Gini roughly halves the cohort-average share (23% → 13%), establishing strong index-sensitivity of the opportunity share. (p. 607)
- **Circumstance partition:** single-circumstance equalisations show parental education dominant, region negligible. (pp. 611–612)
- **Effort reclassification:** treating efforts as circumstances raises the share to ≈ 36% — an internal upper bound on the observed-variable share. (pp. 608–609)
- **Sample scope:** urban-only baseline; a joint urban+rural check raises shares modestly (≈ 2–19% relative, not percentage points, excluding the youngest cohort). (pp. 607–608)
- **Selection:** a Heckman correction was tried; the Mills ratio was insignificant and second-stage coefficients were similar, so OLS is retained for prime-age urban men. (p. 601, footnote)
- **Bias bounds:** the 90% intervals over admissible correlations are the principal robustness device throughout.

**Lessons for my recovery/stability and robustness sections:**
- **Index-sensitivity is first-order.** Their Theil-vs-Gini gap is a warning that my opportunity surface must report the index explicitly and probably show more than one index; do not headline a single number whose magnitude is half-driven by the index choice. [derived-by-analogy]
- **Single-factor contributions need not sum to the total** unless order-averaged — a direct argument for my Shapley exhaustiveness gate. [derived-by-analogy]
- **An internal upper-bound construction** (their "efforts-as-circumstances") is a cheap, interpretable way to bracket a share; my access-only vs access+ability bracket plays the analogous role. [derived-by-analogy]

---

## 12. What I can cite this paper for

- A **canonical, early operationalisation** of Roemer's circumstance/effort distinction into a measurable share of *outcome* inequality attributable to factors beyond individual control. [explicit]
- The **counterfactual-equalisation definition** of an opportunity share, $\Theta_I = [I(F)-I(\tilde\Phi)]/I(F)$, and its **explicit index-dependence**. [explicit, p. 595]
- The **direct/indirect anatomy** of an opportunity effect (effect on outcomes conditional on mediators, vs effect operating through mediators). [explicit, p. 596]
- A **partial-identification posture**: reporting a *bounded interval* for an opportunity share when the underlying parameters are not point-identified, rather than a falsely precise point. [explicit, pp. 598–600]
- **Magnitude benchmark:** that a small set of background circumstances can account for on the order of 10–37% (central ≈ 23%, Theil) of earnings inequality in a high-inequality setting. [explicit, p. 614]
- The finding that **index choice (Theil vs Gini) materially changes the share**. [explicit, p. 607]

---

## 13. What I should NOT cite this paper for  [overclaim risks]

- **Two-way, not three-way.** Its cut is circumstance vs residual (effort + unobservables). It does **not** deliver an access / ability / preference three-way split; do not present it as a precedent for separating ability from access, nor for isolating preferences. [established]
- **No welfare object.** It decomposes *earnings inequality*, not money-metric welfare. Do not cite it as computing equivalent income, EV/CV, or any $W^1$–$W^6$-type object; it contains none. [established]
- **No Independence-of-$y$ / Independence-of-$A$ structure.** Do not attribute my measure taxonomy or its normative readings to this paper. [established]
- **Occupation-as-status, not occupation-as-access or sector.** Father's occupation is a sociological-status *circumstance*; own labour-market status is an *effort*. Neither is my `loc4` occupation-availability object, and neither is `lindi`/NACE industry. Do not let their "occupation" language migrate into my access vocabulary. [established]
- **No feasible-set / latent-jobs mechanism.** Do not cite it as modelling job opportunities, offers, hours availability, or local labour demand; its "opportunity" is background circumstance, not labour-market feasibility. [established]
- **No causal point identification.** Do not cite the shares as causal estimates; they are associations under maintained assumptions, with the bias bounds as the honest qualifier. [explicit, pp. 597–600]
- **Not Shapley / not order-independent.** Do not cite it for Shapley or Shorrocks exhaustiveness; the single-circumstance contributions are not order-averaged. [established]
- **Theory-paper boundary.** Irrelevant here in substance (this is not the Haydar–Maniquet companion), but the general rule stands: never read this empirical IOp paper as supplying my axiomatic/normative *characterisation* — it supplies *motivation and a reporting template*, not foundations.

---

## 14. Direct quotes worth citing

Each quote is short and used once; page numbers from the printed journal.

1. On the ethical premise (quoting Peragine within the paper), p. 585: inequalities due to factors beyond individual responsibility are inequitable and to be compensated, whereas those due to personal responsibility are not [verify exact wording against p. 585 before quoting verbatim; paraphrase preferred].
2. On the measurement gap, p. 586: the authors note that empirical use of the opportunity concept has been rare because economists have lacked agreed ways to measure inequality of opportunity. [paraphrase; verify if a verbatim phrase is wanted]
3. On the headline magnitude, p. 614: five observed circumstances account for between 10 and 37 percent of within-cohort earnings inequality, with a cross-cohort mean near 23 percent. [paraphrase of the explicit result, p. 614]

> Note: I have deliberately kept these as paraphrase/short fragments and flagged the one near-verbatim fragment for verification, to respect quotation limits. Pull exact verbatim strings from the PDF at draft time if a direct quote is required.

---

## 15. Open questions and risks for my draft

- **Index-sensitivity contaminates the headline.** Their 23%-vs-13% Theil/Gini gap is a direct warning that an opportunity share is not a primitive but an index-conditional object. My opportunity surface must be reported with the index fixed and ideally shown across at least two indices; otherwise a referee will (rightly) attribute magnitude to the index. [derived-by-analogy]
- **The "residual = everything else" trap.** Their residual silently bundles preference heterogeneity, luck, and measurement error with genuine effort. My entire contribution is to *not* do this — to put preferences in an estimated block rather than the residual. The risk is the mirror image: that my *preference* component absorbs mis-specified opportunity, which is why the synthetic-recovery gate and the wide-but-identified preference standard errors matter. Cite this paper as the thing I improve upon, and be explicit that the improvement is *moving preference out of the residual*. [derived-by-analogy]
- **Causal humility.** Even with a structural model, my decomposition shares is conditional on the maintained opportunity-density specification; their candid bounding posture is a model for how to write the identification caveat without overclaiming. [explicit on their side]
- **Single-cross-section cohort/period/age confound.** Their inability to separate cohort, age, and period effects from one 1996 wave is a caution for any temporal reading of my pooled 2015–2017 sample; I pool three adjacent waves, so temporal interpretation must stay minimal. [explicit, pp. 610–611]

---

## 16. TL;DR for retrieval

Bourguignon–Ferreira–Menéndez (2007) is the canonical reduced-form **decomposition** antecedent: it defines the opportunity share of *earnings* inequality as the proportional fall in a Theil/Gini index when observed background **circumstances** (race, region of birth, parental education, father's occupation) are equalised, and splits it into a **direct** wage effect (≈60%) and an **indirect** effect through circumstance-shaped "efforts," reporting 10–37% (central ≈23%, Theil) for urban Brazilian men in 1996 under a sign-restricted partial-identification bounding scheme. For my JMP it informs only the **reporting form** of the opportunity share and the direct/indirect anatomy on the **access** side; it has **no preference object, no welfare/equivalent-income object, no feasible-set mechanism, no ability/access split, and no Shapley property**, so it is an antecedent and a magnitude benchmark, never a source for my three-way access/ability/preference Shapley–Shorrocks welfare decomposition or my $W^1$–$W^6$ family.
