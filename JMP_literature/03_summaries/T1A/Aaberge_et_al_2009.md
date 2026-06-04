# Aaberge, Colombino & Wennemo 2009 — Evaluating Alternative Representations of the Choice Sets in Models of Labor Supply

## 0. Metadata
- **BibTeX key:** AabergeColombinoWennemo2009 [verify against your `.bib`]
- **Authors:** R. Aaberge (Research Department, Statistics Norway); U. Colombino (Department of Economics, University of Turin); T. Wennemo (Research Department, Statistics Norway).
- **Year:** 2009.
- **Outlet:** *Journal of Economic Surveys*, Vol. 23, No. 3, pp. 586–612.
- **DOI:** 10.1111/j.1467-6419.2008.00573.x.
- **PDF filename:** `Aaberge_et_al_2009_Evaluating_Alternative_Representations_of_the_Choice_Sets_in_Models_of_Labor.pdf`.
- **Tier:** T1A.
- **JMP block(s) served:** estimation; identification (functional-form separation of preferences from opportunities); opportunity-mechanism (**access** = hours/market-availability density; **ability** = endogenous wage equation, but *not* as an opportunity-density channel); data-infrastructure (sampling-of-alternatives + proposal correction); recovery-test design (synthetic "true-model" Monte Carlo). **Does not serve:** welfare measurement, money-metric inversion, inequality decomposition, normative interpretation — these are *not established* in this paper.

---

## 1. One-paragraph relevance to my JMP
This is the methodological backbone for the *estimation machinery* of my RURO pipeline, not for its welfare or decomposition layers. It states the continuous/discrete RUM labour-supply model with an explicit **opportunity density** `p(h)` over hours (my **access** channel), the McFadden sampling-of-alternatives correction `−ln q(h)` (my mandatory proposal/prior correction), and a fully estimated "true" specification with a Box–Cox utility (my **preference** block) plus market/non-market and hours-peak opportunity dummies. Most directly, its central design — generate synthetic data from a *known* "true" model, re-estimate alternative specifications, and judge them by **out-of-sample policy prediction** rather than in-sample fit — is the template for my synthetic-recovery certification standard. The paper carries **no welfare object, no equivalent income, and no inequality decomposition**; its **ability** channel exists only as a simultaneously estimated wage equation, and it has **no occupation channel at all**, so it cannot be cited for those parts of my design.

---

## 2. Data and setting
- **Country / year:** Norway, 1995 (the estimation sample for the "true" model is the 1995 Norwegian Survey of Level of Living; the tax systems simulated are the 1994 system and a hypothetical revenue-constant flat tax) (p. 596, p. 597–598).
- **Dataset / sample unit:** individuals — married/cohabiting **females**, ages 20–62; other household members' behaviour held exogenous (p. 596). Although the underlying model was developed for joint couple behaviour, this paper estimates **female** supply only "to simplify the execution and the interpretation of the simulation exercise" (p. 596).
- **Sample size:** 1,842 married/cohabiting females (the "true" estimation sample). Monte Carlo: 30 synthetic samples of 1,842 each; the systematic exercise uses a large pooled synthetic sample of 6 × 1,842 = 11,052 (p. 594).
- **Key variables:** yearly hours of work `h`; gross wage `w`; exogenous (including spouse) income `I`; disposable income `f(wh, I)` via the tax-transfer function; age `A`; numbers of children below 3, 3–6, 7–14 (`C1, C2, C3`) (p. 595).
- **Budget-set construction:** `f(wh, I)` maps gross to net income through the (possibly nonlinear, nonconvex) tax-transfer rule; wages for non-workers are imputed from a two-step Heckman wage equation, and wages are treated as **endogenous** with the wage function estimated jointly by ML alongside utility and the opportunity density (notes 7–8, p. 606).
- **Transport to my setting:** **Partial.** The estimator and choice-set logic transport directly to my **France pooled 2015–2017 EUROMOD cross-section**. Differences I do *not* share / they do *not* have: their `f` is a Norwegian 1994 tax rule, not EUROMOD `ils_dispy`; they estimate **singles-female only**, not my three groups including **couples as a joint unit**; they have **no panel, no administrative match, no external opportunity instrument, no vacancy/offer data** — the same constraint I face, so it is a like-for-like cross-sectional identification setting, not a richer one.

---

## 3. Model and objects (object-by-object map)
- **Choice set vs my latent-jobs set:** Their choice object is a set of jobs/opportunities indexed by hours `h` plus unobserved attributes `j` (eq. 1, p. 589). This is the **hours-indexed** ancestor of my latent-jobs set; their jobs carry hours (and, via the wage equation, an implied wage), but **no occupation and no explicit multi-attribute job package** beyond hours and the EV1-distributed `ε(j)`. Note 3 (p. 606) records that the companion Aaberge–Colombino–Strøm models treat `B` as market *and* non-market opportunities characterised by hours, wage, and other attributes — but in *this* paper the realised object is hours-only.
- **Deterministic utility vs my preference `v`:** Their `v(f(wh,I), h)` is a **Box–Cox** form in consumption (disposable income) and leisure, with leisure shifted by `log A`, `(log A)²`, and the three children counts (eq. 10, p. 595). This is the direct analogue of my **preference** block; my locking of consumption to EUROMOD `ils_dispy` corresponds to their `f(wh,I)` argument. Explicit-in-source.
- **Opportunity / availability mechanism vs my `g`:** **Yes, explicit.** The density of opportunities `p(h)` (eq. 11, p. 595) splits into a **market/non-market** mass `p0` (parameter `θ0`, eq. 13) and, conditional on a market job, an **hours-availability** density `g(h)` that is uniform except for peaks at part-time (910–1066 h) and full-time (1898–2106 h), governed by `π1, π2` (eq. 12). In the choice index these enter additively as `θ0 d0(h) + π1 d1(h) + π2 d2(h)` (eq. 14, p. 595).
  - **hours channel:** present (`π1, π2` peaks; uniform elsewhere) → my **access**/hours sub-block.
  - **market/participation channel:** present (`θ0`, the "job" dummy) → my **access**/employment sub-block.
  - **wage channel (ability):** **not in the opportunity density.** Wage is handled as an **endogenous wage equation** estimated jointly (notes 7–8), i.e. a measurement/selection equation, *not* a `log w` channel inside `g`. So my "wage/ability sub-block of `g`" has **no exact counterpart** here — derived-by-analogy only.
  - **occupation channel:** **absent.** No occupation, ISCO, `loc4`, or any task variable. (Therefore no sector/industry conflation risk arises — there is simply nothing of the kind in the paper.)
- **Budget map vs my EUROMOD disposable income:** Their `f(wh,I)` ≈ my EUROMOD-standardised disposable income map; conceptually identical role, different implementation.
- **Attribute-in-both-channels flag:** **No double entry.** Hours enter utility `v` (through leisure and net income) *and* the opportunity density (`π1, π2` peaks), but the paper treats this as the standard separation — the smooth utility in `(consumption, leisure)` versus discrete availability dummies at specific hours ranges — and the second-order analysis (eqs. 5–8, p. 591–592) is precisely about not conflating them. No job attribute is placed in both the *systematic utility* and the *opportunity density* in a way they flag as needing an identification justification. Consistent with my "do not add occupation/sector to both utility and opportunity at the first step" rule.

---

## 4. Estimation method
- **Likelihood / estimator:** Maximum likelihood on the multinomial-logit choice probability derived from EV1 shocks (eqs. 2–4, 14–16). Wage functions and the opportunity-density parameters are estimated **jointly** with the utility parameters by ML (note 7, p. 606).
- **Choice-set construction:** Two contrasted modes. (i) **Fixed grid:** mid-values of 6 or 24 equally spaced intervals on `[0, 3640]` (eq. 16, p. 596). (ii) **Sampled alternatives:** the observed `h` plus 5 or 23 draws (→ 6 or 24 points) from the empirical offered-hours distribution; for the *true* model's own estimation, the chosen value plus **999** draws (= **1,000** alternatives) (p. 596).
- **Proposal / sampling density:** `q(h)`, the empirical density of offered hours (eq. 9; the offered-hours density `g` of eq. 12). Under simple random sampling all `q` cancel; the paper instead uses the more efficient empirical-frequency sampling (p. 593).
- **Prior/proposal correction:** **Yes — `−ln q(h)` is subtracted from the choice index** in both estimation (eq. 15, p. 596) and the consistency result (eq. 9, p. 593), attributed to McFadden (1978) and Ben-Akiva & Lerman (1985). It is **always well defined** on the support where `q(h) > 0`. This is exactly my `−log π` proposal/prior correction.
- **Normalisation / scale:** EV1 scale normalisation implicit in the logit (standard); no separate scale parameter discussed.
- **Numerical method / starting values / multistart:** Not detailed — ML is stated but the optimiser, starting values, and any multistart are **not reported** [verify; treat as not-established].
- **What pins down preferences vs the opportunity mechanism:** Functional-form separation — smooth Box–Cox `v` over `(net income, leisure)` versus additive availability dummies `θ0, π1, π2` localised to market participation and specific hours bands (eqs. 10–14). See §8.
- **Verdict — reusable for my RURO/JAX pipeline?** **Yes, for the estimation core.** The sampled-alternatives likelihood with the `−ln q` correction (eq. 15) *is* the object my engine implements; the named step to reuse is the per-alternative additive correction and the conditional-logit-with-sampling consistency argument. **No** for any welfare/decomposition step (absent here).

## 4b. Proposal / sampling-of-alternatives correction  [extract]
- **Mechanism:** Replace the true (large/continuous) set `B` by a sample `S` = chosen point + draws from `q(h)`; estimate using `φ(h|S) = exp(v − ln q(h)) / Σ_{x∈S} exp(v − ln q(x))` (eq. 9, p. 593). Each drawn alternative carries its **own** `ln q` term — i.e. a per-alternative log-prior, as in my per-row `prior` column.
- **McFadden-style?** **Yes**, explicitly (McFadden 1978; Ben-Akiva & Lerman 1985).
- **Individualised or common?** The general discussion allows the sampling frequencies to be "differentiated according to personal characteristics of the decision units" (p. 593), i.e. *partly individualised in principle*. But in *this paper's* implemented "true" model the offered-hours density `g`/`q` and the opportunity parameters `θ0, π1, π2` are **common scalars**, not functions of `x_i` (eqs. 12–14; Table A1, p. 608). So the realised proposal here is **common across units in the hours and market channels** — there is no wage- or occupation-conditioned draw, because there is no occupation and the wage is a separate equation.
- **Relation to my integrator:** This supports my importance-sampling welfare integrator's *correction form* exactly. On my proposal-individualisation concern, the paper is the **common-channel** baseline: it individualises *nothing* in the offered-hours/market proposal, whereas my proposal individualises the wage and occupation channels and leaves hours/employment common. The paper therefore corroborates the *correctness* of the `−log π` machinery but does **not** itself demonstrate an individualised proposal.

---

## 5. Opportunity mechanism  [MOST IMPORTANT — by channel]
The opportunity mechanism is a **density over alternatives** (eq. 11), not offer probabilities per firm and not a reservation-wage rule. Functional form: a binary market/non-market split `p(h) = p0·g(h)` for `h>0`, `1−p0` for `h=0` (eq. 11), with `p0/(1−p0)=exp(θ0)` (eq. 13); `g(h)` piecewise-uniform with multiplicative peaks `exp(π1)`, `exp(π2)` over the part-time and full-time hours bands (eq. 12). In the likelihood these become additive index terms `θ0 d0 + π1 d1 + π2 d2` (eqs. 14–15).

Mapping to my three sub-objects:
- **access (hours / market-participation):** **Directly present.** `θ0` = market vs non-market availability; `π1, π2` = relative density of jobs at part-time/full-time loads. This is the cleanest ancestor of my access sub-block's employment and hours-availability parameters.
- **access (region / year / occupation offers):** **Absent in the estimated model.** No regional, urbanisation, year, or occupation shifters of the density. The text notes (Section 2.3, p. 593) that *other* Aaberge–Colombino papers let the density vary with personal characteristics, but this paper does **not** estimate such variation. So my region/year/occupation access machinery is **not** evidenced here — cite the companion papers, not this one, for circumstance-varying access.
- **ability (wage technology):** **Not in `g`.** Returns to education/experience and residual productivity dispersion `σ` — my ability sub-block — have **no counterpart inside the opportunity density** here. Wage is an endogenous, jointly estimated equation (notes 7–8), conceptually adjacent but architecturally distinct from a `log w` opportunity channel. Derived-by-analogy at best; do not cite this paper for an ability *opportunity* layer.
- **Occupation as availability vs something else:** **Not present** (no occupation object). No sector/industry conflation to flag.

**What the omissions cost my decomposition:** This paper supplies the *form* of an hours/market access density and the proof that it can be estimated jointly with preferences, but it does **not** supply (i) circumstance-varying access, (ii) a wage/ability opportunity channel, or (iii) any occupation channel. My three-way access/ability/preference cut therefore draws its *structure* from later Aaberge–Colombino work and my own design, with this paper underwriting only the hours/market-access piece and the estimation correction.

---

## 6. Welfare object — and its place on my W¹–W⁶ map
**The paper computes no welfare object.** There is **no money-metric welfare, no equivalent income, no compensating/equivalent variation, and no expected-utility (inclusive-value) welfare measure** anywhere in the paper. Its "evaluation" is **outcome prediction** — participation rates, hours of work, and disposable income, in-sample (1994 tax) and out-of-sample (flat-tax reform) — compared against the synthetic "true" model (eqs. 17–18; Tables 2–7, B1–B6). No reference price/preference/bundle/set is defined, because no welfare conversion is performed.

- **Universal vs constrained set:** N/A (no welfare integral).
- **Discrete-choice welfare subtleties (log-sum, Hicksian/Marshallian, ex-ante/ex-post):** N/A for welfare. (The only log-sum appearance is the Ben-Akiva–Lerman expected-maximum used to analyse choice-set *aggregation* bias — see §6b — not as a welfare core.)
- **Location on my W¹–W⁶ map:** **None.** The paper does **not** contain W¹–W⁶, the Ind-y/Ind-A classification, or any compensation–responsibility stance. Do not attribute any measure-family content to it.
- **Verdict:** **Incompatible as a welfare source** — it is an estimation/prediction-methodology paper. For Aaberge–Colombino *welfare* content, cite the welfare-bearing companion papers, not this one.

## 6b. Inclusive value and money-metric inversion  [extract]
- **Inclusive value as welfare core?** **No.** The expected-maximum / log-sum appears once, as `v̂ℓ = v̄ℓ + ln(Nℓ) + ln(Dℓ)` (eq. 5, p. 591) — the Ben-Akiva–Lerman expected maximum over a sub-interval, used to characterise the **bias from aggregating alternatives** (eqs. 5–8). It is a choice-set-approximation diagnostic, **not** a welfare functional.
- **Money-metric inversion?** **None.** No own-utility map is inverted to a money figure; no closed-form welfare shortcut; no one-dimensional welfare solve.
- **Expectation over EV1 shocks — analytic or simulated?** For the *likelihood/choice probability*, analytic (closed-form logit). For the *prediction exercises*, **simulated**: they draw EV1 shocks per individual per alternative and take the argmax to assign the chosen alternative (p. 598, p. 601). This is the opposite of my analytic-in-shocks welfare integrator: my inclusive value is the closed-form log-sum with no shock draws, whereas their *prediction* step explicitly draws shocks and simulates the argmax.
- **Relation to my design:** Use this paper to justify the *estimation* log-sum/correction, **not** an analytic-in-shocks welfare inversion (which it does not do).

---

## 7. Inequality / decomposition content  [three-way where relevant]
- **Inequality index:** **None.** No Gini, MLD, Theil, variance-of-logs, or Atkinson.
- **Decomposition rule:** **None of the welfare kind.** There is **no** Shapley, Shorrocks, factor-component, subgroup, or RIF decomposition of welfare inequality.
- **What *is* present (do not confuse):** a **prediction-performance meta-regression** — `ln(z_k) = α0 + α1 x1k + … + interactions` (eq. 19, p. 602; Tables 8–9), regressing a model's relative prediction error `z_k` (eq. 18) on indicators for *model design features* (sampled vs fixed; 6 vs 24 alternatives; job dummy; peaks dummies). This attributes **prediction error to choice-set design choices**, which is categorically different from attributing **welfare inequality to access/ability/preference**.
- **Counterfactuals:** The only counterfactual is a policy counterfactual — a revenue-constant flat tax simulated through each model (p. 602) — used to test prediction performance, not to equalise or neutralise a welfare source.
- **Order/path-independence / exhaustiveness:** N/A (no inequality decomposition).
- **Verdict — reusable for my three-way Shapley–Shorrocks split?** **No.** The paper contributes nothing to my decomposition layer. It is **not** a two-way opportunity-vs-preference decomposition either; it has **no welfare-inequality decomposition at all**. To reach my three-way split, one would have to add (i) a welfare object, (ii) an inequality index, and (iii) a Shapley equalisation — none of which exist here. Flag this explicitly against any temptation to read the eq. 19 regression as a "decomposition."

---

## 8. Identification and the separation of preferences from opportunities  [STRICT]
- **What identifies tastes vs constraints:** **Functional-form restriction.** Preferences enter through a smooth Box–Cox `v` in `(net income, leisure)` with demographic leisure-shifters (eq. 10); opportunities enter through *additive, discrete* index terms localised to market participation (`θ0`) and to narrow hours bands at part-time/full-time (`π1, π2`) (eqs. 11–14). The identifying logic: concentration of observed hours at part-time/full-time loads, beyond what a smoothly varying utility would predict, is read as **availability** (the density peaks), not taste. Wages are separately identified via the jointly estimated wage equation with Heckman correction for non-workers (notes 7–8).
- **Ability vs access within the opportunity side:** **Not separated as such.** "Ability" (the wage equation) and "access" (the hours/market density) are *distinct parameter blocks* and so are in-principle distinguishable, but the paper does **not** frame or test an ability-vs-access identification; the wage equation is a measurement/selection device, not an opportunity channel.
- **External shifters / panel / repeated choices:** **None.** Single cross-section; no exclusion restriction from local unemployment or vacancies; no panel. Identification rests entirely on functional form plus distributional (EV1) assumptions.
- **Transport to my France pooled cross-section:** **Yes** — the functional-form-plus-distributional identification is exactly what I rely on, and the paper shares my constraint of **no panel and no external instrument**. This is therefore a *like-setting* precedent for parametric/synthetic-recovery identification, not a richer design I could borrow an instrument from.
- **Against the "your decomposition is mechanical" referee:** The paper's most useful contribution here is **methodological honesty about parametric identification** — it demonstrates (Tables 8–9, conclusions) that **in-sample fit barely discriminates between specifications**, while **out-of-sample policy prediction does**. That directly supports my standard of **synthetic recovery over in-sample fit**: a specification that fits is not thereby validated. Use this as a cited justification for recovery-based certification. (Note: the paper validates *prediction performance* across choice-set designs, not parameter recovery per se, though Table A2 does report the parameter estimates of all 16 models against the true values for inspection.)

---

## 9. Key results and magnitudes
- **"True"-model parameter estimates (Table A1, p. 608)** — population values for the synthetic exercise (estimate (std dev)): consumption Box–Cox `α1 = 0.39 (0.11)`, `α2 = 4.42 (0.44)`; leisure `α3 = −4.57 (0.53)`, `α4 = 168.88 (27.47)`; `α5 (log age) = −94.29 (15.32)`, `α6 (log age²) = 13.35 (2.16)`; children `α7 = 0.44 (0.23)`, `α8 = 1.23 (0.24)`, `α9 = 1.05 (0.19)`; opportunity density: job dummy `θ0 = −0.60 (0.10)`, part-time peak `π1 = 0.46 (0.10)`, full-time peak `π2 = 1.57 (0.07)`.
- **In-sample replication (1994 tax):** Across the 16 models, little statistically significant effect of choice-set representation; the only significant feature in the participation regression is **Job-dummy × 24-alternatives** (p. 602; Table 8). Message: "the ability of a model to replicate observed outcomes is not very informative" (p. 605).
- **Out-of-sample (flat-tax reform):** Clear, large effects. Switching from fixed to sampled alternatives reduces the **hours-of-work** relative prediction error by **83%** (model IIIa vs Ia; p. 605). Disposable-income mean relative error under the flat tax: model Ia ≈ **−4.3%** overall vs ≈ **−2.4% to −2.6%** for the richer models IIb/IIIc/IVd (Table 5, p. 600).
- **Behavioural content of the flat tax:** It stimulates labour supply, with the strongest response among **lower-income** deciles — participation rises by roughly **11% and 10%** in the two lowest deciles and **~5%** in the third, modest thereafter; high-decile females change hours little but gain the largest disposable-income increases (p. 602).
- **Variance of prediction error:** **No notable difference across models** in the standard deviation of the prediction error (motivating the second exercise's focus on the *mean*) (p. 605).
- **Population referred to:** married/cohabiting Norwegian females 20–62, 1994 vs flat-tax regimes. Magnitudes are **prediction-error** magnitudes (and elastic/parameter values), **not** welfare-share or opportunity-share findings — none of the latter exist in this paper, so it cannot benchmark my opportunity share or welfare spread.

---

## 10. Estimators, theorems, or formal results
1. **Continuous/discrete RUM choice probability with opportunity density.**
   - Statement (LaTeX): `\varphi(h) = \dfrac{\exp(v(f(wh,I),h))\,p(h)}{\int \exp(v(f(wx,I),x))\,p(x)\,dx}` (eq. 2, p. 590); discrete analogue eq. 3; equal-availability special case `p(h)=a` gives the bare logit (eq. 4).
   - Assumptions: EV1 (type-I extreme value) shocks; utility additively separable in `v` and `ε(j)`.
   - Technique: (i) random-utility maximisation; (ii) EV1 ⇒ closed-form logit; (iii) opportunity density `p(h)` weights alternatives multiplicatively.
   - Reusability: **Yes** — this is the core form of my per-alternative value before the proposal correction.
2. **Sampling-of-alternatives consistency (McFadden 1978).**
   - Statement (LaTeX): `\varphi(h\mid S) = \dfrac{\exp(v(f(wh,I),h)-\ln q(h))}{\sum_{x\in S}\exp(v(f(wx,I),x)-\ln q(x))}` (eq. 9, p. 593; with opportunity terms, eq. 15, p. 596).
   - Assumptions: positive sampling density `q(h)`; chosen point included in `S`; uniform-conditioning property for the correction.
   - Technique: (i) replace true set `B` by sample `S`; (ii) subtract per-alternative `\ln q`; (iii) consistency from McFadden (1978)/Ben-Akiva–Lerman (1985).
   - Reusability: **Yes, central** — this is exactly my `−log π` correction; reuse the per-alternative log-prior form verbatim in the engine.
3. **Aggregation-bias expansion.**
   - Statement (LaTeX): expected maximum on sub-interval `\hat v^{\ell} = \bar v^{\ell} + \ln(N^{\ell}) + \ln(D^{\ell})` (eq. 5, p. 591), with the typical literature approximation (eq. 8) dropping the `0.5\,\sigma_{hh}v_{hh} + \ln N + \ln D` terms.
   - Assumptions: second-order Taylor expansion of `v` within sub-intervals.
   - Technique: (i) Ben-Akiva–Lerman aggregation; (ii) Taylor expansion; (iii) show dropped terms bias fixed-grid estimates unless equal across intervals.
   - Reusability: **Maybe** — useful as a written justification for *sampling rather than fixing* a coarse hours grid, and for why a too-coarse grid biases estimates; not needed computationally if I already sample.

(No numbered theorems are stated in the paper; results are presented as derivations and simulation findings. Do not invent theorem numbers.)

---

## 11. Robustness and specification sensitivity
- **What they vary:** alternative generation (fixed vs sampled); number of alternatives (6 vs 24); inclusion of the job (market) dummy; inclusion of the peaks dummies — the full 2×2×2×2 = 16-model grid (Table 1, p. 597).
- **What breaks / what is robust:** the **standard deviation** of prediction error is insensitive to all four design choices; the **mean** prediction error is insensitive **in-sample** but **sensitive out-of-sample**, where sampling + heterogeneous availability sharply reduce error (Tables 2–9; conclusions p. 605–606).
- **For my recovery/stability tests:** (i) **choice-set size** matters less than sampled-vs-fixed and the availability dummies — informs my draw-count / number-of-alternatives stress test (my 101/901 alternatives are far above their 6/24, and they already used 1,000 for the true-model fit). (ii) The result that **a coarse fixed grid degrades the *tails* of predicted distributions** (lower/upper deciles, p. 599) is a direct caution for my **effective-sample-size** concern in thin-coverage households. (iii) The headline robustness lesson — **in-sample fit is uninformative; out-of-sample/recovery is the discriminating test** — is the precedent for my synthetic-recovery gate.
- **Reference-state / ability-access boundary sensitivity:** **Not studied** (no welfare references, no ability/access cut). N/A.

---

## 12. What I can cite this paper for
- The RUM labour-supply choice probability with an explicit **opportunity density** over hours, and the market/non-market plus hours-peak parameterisation (`θ0, π1, π2`) (eqs. 10–14).
- The **sampling-of-alternatives + `−ln q` proposal correction** as the consistent estimator on a sampled choice set (eqs. 9, 15), attributable here and to McFadden (1978)/Ben-Akiva–Lerman (1985).
- The methodological claim that **choice-set representation has little effect on in-sample fit but a material effect on out-of-sample policy prediction** (conclusions, p. 605–606) — my justification for valuing recovery/out-of-sample behaviour over in-sample fit.
- The synthetic **"true-model → re-estimate → compare" Monte Carlo template** as a precedent for recovery-style validation (Sections 3–5).
- That the **opportunity density can be estimated jointly with Box–Cox preferences and an endogenous wage equation by ML** (note 7).
- The bias analysis showing **fixed coarse grids bias estimates / degrade distribution tails** (eqs. 5–8; p. 599).

---

## 13. What I should NOT cite this paper for  [overclaim risks]
- **No welfare object.** It computes **no** money-metric welfare, equivalent income, or EV/CV. Do not cite it for any welfare construction or for my ex-ante inclusive-value welfare.
- **No inequality decomposition (and not even two-way).** It has **no** welfare-inequality decomposition. Do not read the eq. 19 prediction-error meta-regression as an opportunity-vs-preference (or access/ability/preference) decomposition.
- **No W¹–W⁶ / no compensation–responsibility content.** It contains none of the Ind-y/Ind-A classification or the measure family. Do not attribute these to it.
- **No ability-as-opportunity-channel.** The wage is an endogenous equation, not a `log w` channel in `g`; do not cite it for my wage/ability opportunity sub-block.
- **No circumstance-varying access in the estimated model.** The estimated opportunity density uses common scalars `θ0, π1, π2`; do not cite it for region/year/occupation-varying access (cite the companion 1995/1999/2004 papers for that, with verification).
- **No occupation / no sector.** There is no occupation object; do not cite it for `loc4` or any occupation-as-access design, and there is correspondingly no NACE/ISCO conflation in it.
- **"Random opportunities" framing:** the paper's opportunity density is a **deterministic** density estimated by ML; the randomness is in the EV1 utility shocks. Consistent with my deterministic-opportunities stance — do not import a "random opportunities" reading.
- **Theory-paper boundary:** this is an empirical/methodological paper; it has no bearing on the Haydar–Maniquet axiomatic characterisation, and nothing in it should be read as a theory contribution to the JMP.

---

## 14. Direct quotes worth citing
(Short verbatim excerpts; page numbers as printed. Use sparingly and attribute.)
- p. 593, on the correction: "consistent estimates of v(f(wh, I), h) can still be obtained when the true choice set B is replaced by S".
- p. 605, on the headline lesson: "the ability of a model to replicate observed outcomes is not very informative".
- p. 595, on the offered-hours density: peaks make it "more likely to find jobs with hours that accord with full-time and standard part-time positions".

---

## 15. Open questions and risks for my draft
- **Common vs individualised proposal.** This paper individualises *nothing* in its offered-hours/market proposal, so it cannot, by itself, justify my partly-individualised proposal (wage/occupation conditioned on `x_i`); I must lean on the proposal-individualisation audit and the companion papers, not this one.
- **Recovery ≠ prediction performance.** The paper's validation target is *out-of-sample prediction*, not *parameter recovery*; my certification claim is recovery-based. Cite carefully: it supports "in-sample fit is insufficient," but it is not itself a parameter-recovery proof (though Table A2 lets one inspect parameter dispersion across designs).
- **Integration node count.** Their true-model fit used 1,000 alternatives; my 101 (singles) is far thinner. The paper's finding that coarse sets degrade distribution tails is a flag for my thin-ESS singles households (cross-references my welfare-integration ESS gate).
- **Endogenous wage handling.** They estimate the wage equation jointly with Heckman selection; my pipeline treats the wage technology as an ability sub-block of `g`. The architectural difference must be stated so a referee does not read my ability channel as their wage equation.
- **No numerical-implementation detail.** Optimiser, starting values, and multistart are not reported [verify], so the paper cannot be cited for numerical-stability practice.

---

## 16. TL;DR for retrieval
Methodological/simulation paper establishing that, in a RUM labour-supply model with an explicit **hours/market opportunity density** and a Box–Cox **preference** utility, the sampling-of-alternatives estimator with the `−ln q` **proposal/prior correction** (McFadden 1978) is consistent, and that choice-set representation barely affects in-sample fit but strongly affects out-of-sample policy prediction — the precedent for my synthetic-recovery-over-fit standard and my `−log π` correction. It carries **no welfare object, no inequality decomposition, no ability-as-opportunity channel, and no occupation**, so it informs only the **estimation/access** and **recovery-design** parts of my JMP, never the welfare (W¹–W⁶) or three-way decomposition layers. The opportunity density is **deterministic** and estimated, consistent with my deterministic-opportunities framing; it is an empirical/methodological source with no connection to the Haydar–Maniquet theory paper.
