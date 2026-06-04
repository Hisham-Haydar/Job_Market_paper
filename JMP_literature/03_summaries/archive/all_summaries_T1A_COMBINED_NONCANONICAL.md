# Aaberge, Colombino & Wennemo 2009 â€” Evaluating Alternative Representations of the Choice Sets in Models of Labor Supply

## 0. Metadata
- **BibTeX key:** AabergeColombinoWennemo2009 [verify against your `.bib`]
- **Authors:** R. Aaberge (Research Department, Statistics Norway); U. Colombino (Department of Economics, University of Turin); T. Wennemo (Research Department, Statistics Norway).
- **Year:** 2009.
- **Outlet:** *Journal of Economic Surveys*, Vol. 23, No. 3, pp. 586â€“612.
- **DOI:** 10.1111/j.1467-6419.2008.00573.x.
- **PDF filename:** `Aaberge_et_al_2009_Evaluating_Alternative_Representations_of_the_Choice_Sets_in_Models_of_Labor.pdf`.
- **Tier:** T1A.
- **JMP block(s) served:** estimation; identification (functional-form separation of preferences from opportunities); opportunity-mechanism (**access** = hours/market-availability density; **ability** = endogenous wage equation, but *not* as an opportunity-density channel); data-infrastructure (sampling-of-alternatives + proposal correction); recovery-test design (synthetic "true-model" Monte Carlo). **Does not serve:** welfare measurement, money-metric inversion, inequality decomposition, normative interpretation â€” these are *not established* in this paper.

---

## 1. One-paragraph relevance to my JMP
This is the methodological backbone for the *estimation machinery* of my RURO pipeline, not for its welfare or decomposition layers. It states the continuous/discrete RUM labour-supply model with an explicit **opportunity density** `p(h)` over hours (my **access** channel), the McFadden sampling-of-alternatives correction `âˆ’ln q(h)` (my mandatory proposal/prior correction), and a fully estimated "true" specification with a Boxâ€“Cox utility (my **preference** block) plus market/non-market and hours-peak opportunity dummies. Most directly, its central design â€” generate synthetic data from a *known* "true" model, re-estimate alternative specifications, and judge them by **out-of-sample policy prediction** rather than in-sample fit â€” is the template for my synthetic-recovery certification standard. The paper carries **no welfare object, no equivalent income, and no inequality decomposition**; its **ability** channel exists only as a simultaneously estimated wage equation, and it has **no occupation channel at all**, so it cannot be cited for those parts of my design.

---

## 2. Data and setting
- **Country / year:** Norway, 1995 (the estimation sample for the "true" model is the 1995 Norwegian Survey of Level of Living; the tax systems simulated are the 1994 system and a hypothetical revenue-constant flat tax) (p. 596, p. 597â€“598).
- **Dataset / sample unit:** individuals â€” married/cohabiting **females**, ages 20â€“62; other household members' behaviour held exogenous (p. 596). Although the underlying model was developed for joint couple behaviour, this paper estimates **female** supply only "to simplify the execution and the interpretation of the simulation exercise" (p. 596).
- **Sample size:** 1,842 married/cohabiting females (the "true" estimation sample). Monte Carlo: 30 synthetic samples of 1,842 each; the systematic exercise uses a large pooled synthetic sample of 6 Ã— 1,842 = 11,052 (p. 594).
- **Key variables:** yearly hours of work `h`; gross wage `w`; exogenous (including spouse) income `I`; disposable income `f(wh, I)` via the tax-transfer function; age `A`; numbers of children below 3, 3â€“6, 7â€“14 (`C1, C2, C3`) (p. 595).
- **Budget-set construction:** `f(wh, I)` maps gross to net income through the (possibly nonlinear, nonconvex) tax-transfer rule; wages for non-workers are imputed from a two-step Heckman wage equation, and wages are treated as **endogenous** with the wage function estimated jointly by ML alongside utility and the opportunity density (notes 7â€“8, p. 606).
- **Transport to my setting:** **Partial.** The estimator and choice-set logic transport directly to my **France pooled 2015â€“2017 EUROMOD cross-section**. Differences I do *not* share / they do *not* have: their `f` is a Norwegian 1994 tax rule, not EUROMOD `ils_dispy`; they estimate **singles-female only**, not my three groups including **couples as a joint unit**; they have **no panel, no administrative match, no external opportunity instrument, no vacancy/offer data** â€” the same constraint I face, so it is a like-for-like cross-sectional identification setting, not a richer one.

---

## 3. Model and objects (object-by-object map)
- **Choice set vs my latent-jobs set:** Their choice object is a set of jobs/opportunities indexed by hours `h` plus unobserved attributes `j` (eq. 1, p. 589). This is the **hours-indexed** ancestor of my latent-jobs set; their jobs carry hours (and, via the wage equation, an implied wage), but **no occupation and no explicit multi-attribute job package** beyond hours and the EV1-distributed `Îµ(j)`. Note 3 (p. 606) records that the companion Aabergeâ€“Colombinoâ€“StrÃ¸m models treat `B` as market *and* non-market opportunities characterised by hours, wage, and other attributes â€” but in *this* paper the realised object is hours-only.
- **Deterministic utility vs my preference `v`:** Their `v(f(wh,I), h)` is a **Boxâ€“Cox** form in consumption (disposable income) and leisure, with leisure shifted by `log A`, `(log A)Â²`, and the three children counts (eq. 10, p. 595). This is the direct analogue of my **preference** block; my locking of consumption to EUROMOD `ils_dispy` corresponds to their `f(wh,I)` argument. Explicit-in-source.
- **Opportunity / availability mechanism vs my `g`:** **Yes, explicit.** The density of opportunities `p(h)` (eq. 11, p. 595) splits into a **market/non-market** mass `p0` (parameter `Î¸0`, eq. 13) and, conditional on a market job, an **hours-availability** density `g(h)` that is uniform except for peaks at part-time (910â€“1066 h) and full-time (1898â€“2106 h), governed by `Ï€1, Ï€2` (eq. 12). In the choice index these enter additively as `Î¸0 d0(h) + Ï€1 d1(h) + Ï€2 d2(h)` (eq. 14, p. 595).
  - **hours channel:** present (`Ï€1, Ï€2` peaks; uniform elsewhere) â†’ my **access**/hours sub-block.
  - **market/participation channel:** present (`Î¸0`, the "job" dummy) â†’ my **access**/employment sub-block.
  - **wage channel (ability):** **not in the opportunity density.** Wage is handled as an **endogenous wage equation** estimated jointly (notes 7â€“8), i.e. a measurement/selection equation, *not* a `log w` channel inside `g`. So my "wage/ability sub-block of `g`" has **no exact counterpart** here â€” derived-by-analogy only.
  - **occupation channel:** **absent.** No occupation, ISCO, `loc4`, or any task variable. (Therefore no sector/industry conflation risk arises â€” there is simply nothing of the kind in the paper.)
- **Budget map vs my EUROMOD disposable income:** Their `f(wh,I)` â‰ˆ my EUROMOD-standardised disposable income map; conceptually identical role, different implementation.
- **Attribute-in-both-channels flag:** **No double entry.** Hours enter utility `v` (through leisure and net income) *and* the opportunity density (`Ï€1, Ï€2` peaks), but the paper treats this as the standard separation â€” the smooth utility in `(consumption, leisure)` versus discrete availability dummies at specific hours ranges â€” and the second-order analysis (eqs. 5â€“8, p. 591â€“592) is precisely about not conflating them. No job attribute is placed in both the *systematic utility* and the *opportunity density* in a way they flag as needing an identification justification. Consistent with my "do not add occupation/sector to both utility and opportunity at the first step" rule.

---

## 4. Estimation method
- **Likelihood / estimator:** Maximum likelihood on the multinomial-logit choice probability derived from EV1 shocks (eqs. 2â€“4, 14â€“16). Wage functions and the opportunity-density parameters are estimated **jointly** with the utility parameters by ML (note 7, p. 606).
- **Choice-set construction:** Two contrasted modes. (i) **Fixed grid:** mid-values of 6 or 24 equally spaced intervals on `[0, 3640]` (eq. 16, p. 596). (ii) **Sampled alternatives:** the observed `h` plus 5 or 23 draws (â†’ 6 or 24 points) from the empirical offered-hours distribution; for the *true* model's own estimation, the chosen value plus **999** draws (= **1,000** alternatives) (p. 596).
- **Proposal / sampling density:** `q(h)`, the empirical density of offered hours (eq. 9; the offered-hours density `g` of eq. 12). Under simple random sampling all `q` cancel; the paper instead uses the more efficient empirical-frequency sampling (p. 593).
- **Prior/proposal correction:** **Yes â€” `âˆ’ln q(h)` is subtracted from the choice index** in both estimation (eq. 15, p. 596) and the consistency result (eq. 9, p. 593), attributed to McFadden (1978) and Ben-Akiva & Lerman (1985). It is **always well defined** on the support where `q(h) > 0`. This is exactly my `âˆ’log Ï€` proposal/prior correction.
- **Normalisation / scale:** EV1 scale normalisation implicit in the logit (standard); no separate scale parameter discussed.
- **Numerical method / starting values / multistart:** Not detailed â€” ML is stated but the optimiser, starting values, and any multistart are **not reported** [verify; treat as not-established].
- **What pins down preferences vs the opportunity mechanism:** Functional-form separation â€” smooth Boxâ€“Cox `v` over `(net income, leisure)` versus additive availability dummies `Î¸0, Ï€1, Ï€2` localised to market participation and specific hours bands (eqs. 10â€“14). See Â§8.
- **Verdict â€” reusable for my RURO/JAX pipeline?** **Yes, for the estimation core.** The sampled-alternatives likelihood with the `âˆ’ln q` correction (eq. 15) *is* the object my engine implements; the named step to reuse is the per-alternative additive correction and the conditional-logit-with-sampling consistency argument. **No** for any welfare/decomposition step (absent here).

## 4b. Proposal / sampling-of-alternatives correction  [extract]
- **Mechanism:** Replace the true (large/continuous) set `B` by a sample `S` = chosen point + draws from `q(h)`; estimate using `Ï†(h|S) = exp(v âˆ’ ln q(h)) / Î£_{xâˆˆS} exp(v âˆ’ ln q(x))` (eq. 9, p. 593). Each drawn alternative carries its **own** `ln q` term â€” i.e. a per-alternative log-prior, as in my per-row `prior` column.
- **McFadden-style?** **Yes**, explicitly (McFadden 1978; Ben-Akiva & Lerman 1985).
- **Individualised or common?** The general discussion allows the sampling frequencies to be "differentiated according to personal characteristics of the decision units" (p. 593), i.e. *partly individualised in principle*. But in *this paper's* implemented "true" model the offered-hours density `g`/`q` and the opportunity parameters `Î¸0, Ï€1, Ï€2` are **common scalars**, not functions of `x_i` (eqs. 12â€“14; Table A1, p. 608). So the realised proposal here is **common across units in the hours and market channels** â€” there is no wage- or occupation-conditioned draw, because there is no occupation and the wage is a separate equation.
- **Relation to my integrator:** This supports my importance-sampling welfare integrator's *correction form* exactly. On my proposal-individualisation concern, the paper is the **common-channel** baseline: it individualises *nothing* in the offered-hours/market proposal, whereas my proposal individualises the wage and occupation channels and leaves hours/employment common. The paper therefore corroborates the *correctness* of the `âˆ’log Ï€` machinery but does **not** itself demonstrate an individualised proposal.

---

## 5. Opportunity mechanism  [MOST IMPORTANT â€” by channel]
The opportunity mechanism is a **density over alternatives** (eq. 11), not offer probabilities per firm and not a reservation-wage rule. Functional form: a binary market/non-market split `p(h) = p0Â·g(h)` for `h>0`, `1âˆ’p0` for `h=0` (eq. 11), with `p0/(1âˆ’p0)=exp(Î¸0)` (eq. 13); `g(h)` piecewise-uniform with multiplicative peaks `exp(Ï€1)`, `exp(Ï€2)` over the part-time and full-time hours bands (eq. 12). In the likelihood these become additive index terms `Î¸0 d0 + Ï€1 d1 + Ï€2 d2` (eqs. 14â€“15).

Mapping to my three sub-objects:
- **access (hours / market-participation):** **Directly present.** `Î¸0` = market vs non-market availability; `Ï€1, Ï€2` = relative density of jobs at part-time/full-time loads. This is the cleanest ancestor of my access sub-block's employment and hours-availability parameters.
- **access (region / year / occupation offers):** **Absent in the estimated model.** No regional, urbanisation, year, or occupation shifters of the density. The text notes (Section 2.3, p. 593) that *other* Aabergeâ€“Colombino papers let the density vary with personal characteristics, but this paper does **not** estimate such variation. So my region/year/occupation access machinery is **not** evidenced here â€” cite the companion papers, not this one, for circumstance-varying access.
- **ability (wage technology):** **Not in `g`.** Returns to education/experience and residual productivity dispersion `Ïƒ` â€” my ability sub-block â€” have **no counterpart inside the opportunity density** here. Wage is an endogenous, jointly estimated equation (notes 7â€“8), conceptually adjacent but architecturally distinct from a `log w` opportunity channel. Derived-by-analogy at best; do not cite this paper for an ability *opportunity* layer.
- **Occupation as availability vs something else:** **Not present** (no occupation object). No sector/industry conflation to flag.

**What the omissions cost my decomposition:** This paper supplies the *form* of an hours/market access density and the proof that it can be estimated jointly with preferences, but it does **not** supply (i) circumstance-varying access, (ii) a wage/ability opportunity channel, or (iii) any occupation channel. My three-way access/ability/preference cut therefore draws its *structure* from later Aabergeâ€“Colombino work and my own design, with this paper underwriting only the hours/market-access piece and the estimation correction.

---

## 6. Welfare object â€” and its place on my WÂ¹â€“Wâ¶ map
**The paper computes no welfare object.** There is **no money-metric welfare, no equivalent income, no compensating/equivalent variation, and no expected-utility (inclusive-value) welfare measure** anywhere in the paper. Its "evaluation" is **outcome prediction** â€” participation rates, hours of work, and disposable income, in-sample (1994 tax) and out-of-sample (flat-tax reform) â€” compared against the synthetic "true" model (eqs. 17â€“18; Tables 2â€“7, B1â€“B6). No reference price/preference/bundle/set is defined, because no welfare conversion is performed.

- **Universal vs constrained set:** N/A (no welfare integral).
- **Discrete-choice welfare subtleties (log-sum, Hicksian/Marshallian, ex-ante/ex-post):** N/A for welfare. (The only log-sum appearance is the Ben-Akivaâ€“Lerman expected-maximum used to analyse choice-set *aggregation* bias â€” see Â§6b â€” not as a welfare core.)
- **Location on my WÂ¹â€“Wâ¶ map:** **None.** The paper does **not** contain WÂ¹â€“Wâ¶, the Ind-y/Ind-A classification, or any compensationâ€“responsibility stance. Do not attribute any measure-family content to it.
- **Verdict:** **Incompatible as a welfare source** â€” it is an estimation/prediction-methodology paper. For Aabergeâ€“Colombino *welfare* content, cite the welfare-bearing companion papers, not this one.

## 6b. Inclusive value and money-metric inversion  [extract]
- **Inclusive value as welfare core?** **No.** The expected-maximum / log-sum appears once, as `vÌ‚â„“ = vÌ„â„“ + ln(Nâ„“) + ln(Dâ„“)` (eq. 5, p. 591) â€” the Ben-Akivaâ€“Lerman expected maximum over a sub-interval, used to characterise the **bias from aggregating alternatives** (eqs. 5â€“8). It is a choice-set-approximation diagnostic, **not** a welfare functional.
- **Money-metric inversion?** **None.** No own-utility map is inverted to a money figure; no closed-form welfare shortcut; no one-dimensional welfare solve.
- **Expectation over EV1 shocks â€” analytic or simulated?** For the *likelihood/choice probability*, analytic (closed-form logit). For the *prediction exercises*, **simulated**: they draw EV1 shocks per individual per alternative and take the argmax to assign the chosen alternative (p. 598, p. 601). This is the opposite of my analytic-in-shocks welfare integrator: my inclusive value is the closed-form log-sum with no shock draws, whereas their *prediction* step explicitly draws shocks and simulates the argmax.
- **Relation to my design:** Use this paper to justify the *estimation* log-sum/correction, **not** an analytic-in-shocks welfare inversion (which it does not do).

---

## 7. Inequality / decomposition content  [three-way where relevant]
- **Inequality index:** **None.** No Gini, MLD, Theil, variance-of-logs, or Atkinson.
- **Decomposition rule:** **None of the welfare kind.** There is **no** Shapley, Shorrocks, factor-component, subgroup, or RIF decomposition of welfare inequality.
- **What *is* present (do not confuse):** a **prediction-performance meta-regression** â€” `ln(z_k) = Î±0 + Î±1 x1k + â€¦ + interactions` (eq. 19, p. 602; Tables 8â€“9), regressing a model's relative prediction error `z_k` (eq. 18) on indicators for *model design features* (sampled vs fixed; 6 vs 24 alternatives; job dummy; peaks dummies). This attributes **prediction error to choice-set design choices**, which is categorically different from attributing **welfare inequality to access/ability/preference**.
- **Counterfactuals:** The only counterfactual is a policy counterfactual â€” a revenue-constant flat tax simulated through each model (p. 602) â€” used to test prediction performance, not to equalise or neutralise a welfare source.
- **Order/path-independence / exhaustiveness:** N/A (no inequality decomposition).
- **Verdict â€” reusable for my three-way Shapleyâ€“Shorrocks split?** **No.** The paper contributes nothing to my decomposition layer. It is **not** a two-way opportunity-vs-preference decomposition either; it has **no welfare-inequality decomposition at all**. To reach my three-way split, one would have to add (i) a welfare object, (ii) an inequality index, and (iii) a Shapley equalisation â€” none of which exist here. Flag this explicitly against any temptation to read the eq. 19 regression as a "decomposition."

---

## 8. Identification and the separation of preferences from opportunities  [STRICT]
- **What identifies tastes vs constraints:** **Functional-form restriction.** Preferences enter through a smooth Boxâ€“Cox `v` in `(net income, leisure)` with demographic leisure-shifters (eq. 10); opportunities enter through *additive, discrete* index terms localised to market participation (`Î¸0`) and to narrow hours bands at part-time/full-time (`Ï€1, Ï€2`) (eqs. 11â€“14). The identifying logic: concentration of observed hours at part-time/full-time loads, beyond what a smoothly varying utility would predict, is read as **availability** (the density peaks), not taste. Wages are separately identified via the jointly estimated wage equation with Heckman correction for non-workers (notes 7â€“8).
- **Ability vs access within the opportunity side:** **Not separated as such.** "Ability" (the wage equation) and "access" (the hours/market density) are *distinct parameter blocks* and so are in-principle distinguishable, but the paper does **not** frame or test an ability-vs-access identification; the wage equation is a measurement/selection device, not an opportunity channel.
- **External shifters / panel / repeated choices:** **None.** Single cross-section; no exclusion restriction from local unemployment or vacancies; no panel. Identification rests entirely on functional form plus distributional (EV1) assumptions.
- **Transport to my France pooled cross-section:** **Yes** â€” the functional-form-plus-distributional identification is exactly what I rely on, and the paper shares my constraint of **no panel and no external instrument**. This is therefore a *like-setting* precedent for parametric/synthetic-recovery identification, not a richer design I could borrow an instrument from.
- **Against the "your decomposition is mechanical" referee:** The paper's most useful contribution here is **methodological honesty about parametric identification** â€” it demonstrates (Tables 8â€“9, conclusions) that **in-sample fit barely discriminates between specifications**, while **out-of-sample policy prediction does**. That directly supports my standard of **synthetic recovery over in-sample fit**: a specification that fits is not thereby validated. Use this as a cited justification for recovery-based certification. (Note: the paper validates *prediction performance* across choice-set designs, not parameter recovery per se, though Table A2 does report the parameter estimates of all 16 models against the true values for inspection.)

---

## 9. Key results and magnitudes
- **"True"-model parameter estimates (Table A1, p. 608)** â€” population values for the synthetic exercise (estimate (std dev)): consumption Boxâ€“Cox `Î±1 = 0.39 (0.11)`, `Î±2 = 4.42 (0.44)`; leisure `Î±3 = âˆ’4.57 (0.53)`, `Î±4 = 168.88 (27.47)`; `Î±5 (log age) = âˆ’94.29 (15.32)`, `Î±6 (log ageÂ²) = 13.35 (2.16)`; children `Î±7 = 0.44 (0.23)`, `Î±8 = 1.23 (0.24)`, `Î±9 = 1.05 (0.19)`; opportunity density: job dummy `Î¸0 = âˆ’0.60 (0.10)`, part-time peak `Ï€1 = 0.46 (0.10)`, full-time peak `Ï€2 = 1.57 (0.07)`.
- **In-sample replication (1994 tax):** Across the 16 models, little statistically significant effect of choice-set representation; the only significant feature in the participation regression is **Job-dummy Ã— 24-alternatives** (p. 602; Table 8). Message: "the ability of a model to replicate observed outcomes is not very informative" (p. 605).
- **Out-of-sample (flat-tax reform):** Clear, large effects. Switching from fixed to sampled alternatives reduces the **hours-of-work** relative prediction error by **83%** (model IIIa vs Ia; p. 605). Disposable-income mean relative error under the flat tax: model Ia â‰ˆ **âˆ’4.3%** overall vs â‰ˆ **âˆ’2.4% to âˆ’2.6%** for the richer models IIb/IIIc/IVd (Table 5, p. 600).
- **Behavioural content of the flat tax:** It stimulates labour supply, with the strongest response among **lower-income** deciles â€” participation rises by roughly **11% and 10%** in the two lowest deciles and **~5%** in the third, modest thereafter; high-decile females change hours little but gain the largest disposable-income increases (p. 602).
- **Variance of prediction error:** **No notable difference across models** in the standard deviation of the prediction error (motivating the second exercise's focus on the *mean*) (p. 605).
- **Population referred to:** married/cohabiting Norwegian females 20â€“62, 1994 vs flat-tax regimes. Magnitudes are **prediction-error** magnitudes (and elastic/parameter values), **not** welfare-share or opportunity-share findings â€” none of the latter exist in this paper, so it cannot benchmark my opportunity share or welfare spread.

---

## 10. Estimators, theorems, or formal results
1. **Continuous/discrete RUM choice probability with opportunity density.**
   - Statement (LaTeX): `\varphi(h) = \dfrac{\exp(v(f(wh,I),h))\,p(h)}{\int \exp(v(f(wx,I),x))\,p(x)\,dx}` (eq. 2, p. 590); discrete analogue eq. 3; equal-availability special case `p(h)=a` gives the bare logit (eq. 4).
   - Assumptions: EV1 (type-I extreme value) shocks; utility additively separable in `v` and `Îµ(j)`.
   - Technique: (i) random-utility maximisation; (ii) EV1 â‡’ closed-form logit; (iii) opportunity density `p(h)` weights alternatives multiplicatively.
   - Reusability: **Yes** â€” this is the core form of my per-alternative value before the proposal correction.
2. **Sampling-of-alternatives consistency (McFadden 1978).**
   - Statement (LaTeX): `\varphi(h\mid S) = \dfrac{\exp(v(f(wh,I),h)-\ln q(h))}{\sum_{x\in S}\exp(v(f(wx,I),x)-\ln q(x))}` (eq. 9, p. 593; with opportunity terms, eq. 15, p. 596).
   - Assumptions: positive sampling density `q(h)`; chosen point included in `S`; uniform-conditioning property for the correction.
   - Technique: (i) replace true set `B` by sample `S`; (ii) subtract per-alternative `\ln q`; (iii) consistency from McFadden (1978)/Ben-Akivaâ€“Lerman (1985).
   - Reusability: **Yes, central** â€” this is exactly my `âˆ’log Ï€` correction; reuse the per-alternative log-prior form verbatim in the engine.
3. **Aggregation-bias expansion.**
   - Statement (LaTeX): expected maximum on sub-interval `\hat v^{\ell} = \bar v^{\ell} + \ln(N^{\ell}) + \ln(D^{\ell})` (eq. 5, p. 591), with the typical literature approximation (eq. 8) dropping the `0.5\,\sigma_{hh}v_{hh} + \ln N + \ln D` terms.
   - Assumptions: second-order Taylor expansion of `v` within sub-intervals.
   - Technique: (i) Ben-Akivaâ€“Lerman aggregation; (ii) Taylor expansion; (iii) show dropped terms bias fixed-grid estimates unless equal across intervals.
   - Reusability: **Maybe** â€” useful as a written justification for *sampling rather than fixing* a coarse hours grid, and for why a too-coarse grid biases estimates; not needed computationally if I already sample.

(No numbered theorems are stated in the paper; results are presented as derivations and simulation findings. Do not invent theorem numbers.)

---

## 11. Robustness and specification sensitivity
- **What they vary:** alternative generation (fixed vs sampled); number of alternatives (6 vs 24); inclusion of the job (market) dummy; inclusion of the peaks dummies â€” the full 2Ã—2Ã—2Ã—2 = 16-model grid (Table 1, p. 597).
- **What breaks / what is robust:** the **standard deviation** of prediction error is insensitive to all four design choices; the **mean** prediction error is insensitive **in-sample** but **sensitive out-of-sample**, where sampling + heterogeneous availability sharply reduce error (Tables 2â€“9; conclusions p. 605â€“606).
- **For my recovery/stability tests:** (i) **choice-set size** matters less than sampled-vs-fixed and the availability dummies â€” informs my draw-count / number-of-alternatives stress test (my 101/901 alternatives are far above their 6/24, and they already used 1,000 for the true-model fit). (ii) The result that **a coarse fixed grid degrades the *tails* of predicted distributions** (lower/upper deciles, p. 599) is a direct caution for my **effective-sample-size** concern in thin-coverage households. (iii) The headline robustness lesson â€” **in-sample fit is uninformative; out-of-sample/recovery is the discriminating test** â€” is the precedent for my synthetic-recovery gate.
- **Reference-state / ability-access boundary sensitivity:** **Not studied** (no welfare references, no ability/access cut). N/A.

---

## 12. What I can cite this paper for
- The RUM labour-supply choice probability with an explicit **opportunity density** over hours, and the market/non-market plus hours-peak parameterisation (`Î¸0, Ï€1, Ï€2`) (eqs. 10â€“14).
- The **sampling-of-alternatives + `âˆ’ln q` proposal correction** as the consistent estimator on a sampled choice set (eqs. 9, 15), attributable here and to McFadden (1978)/Ben-Akivaâ€“Lerman (1985).
- The methodological claim that **choice-set representation has little effect on in-sample fit but a material effect on out-of-sample policy prediction** (conclusions, p. 605â€“606) â€” my justification for valuing recovery/out-of-sample behaviour over in-sample fit.
- The synthetic **"true-model â†’ re-estimate â†’ compare" Monte Carlo template** as a precedent for recovery-style validation (Sections 3â€“5).
- That the **opportunity density can be estimated jointly with Boxâ€“Cox preferences and an endogenous wage equation by ML** (note 7).
- The bias analysis showing **fixed coarse grids bias estimates / degrade distribution tails** (eqs. 5â€“8; p. 599).

---

## 13. What I should NOT cite this paper for  [overclaim risks]
- **No welfare object.** It computes **no** money-metric welfare, equivalent income, or EV/CV. Do not cite it for any welfare construction or for my ex-ante inclusive-value welfare.
- **No inequality decomposition (and not even two-way).** It has **no** welfare-inequality decomposition. Do not read the eq. 19 prediction-error meta-regression as an opportunity-vs-preference (or access/ability/preference) decomposition.
- **No WÂ¹â€“Wâ¶ / no compensationâ€“responsibility content.** It contains none of the Ind-y/Ind-A classification or the measure family. Do not attribute these to it.
- **No ability-as-opportunity-channel.** The wage is an endogenous equation, not a `log w` channel in `g`; do not cite it for my wage/ability opportunity sub-block.
- **No circumstance-varying access in the estimated model.** The estimated opportunity density uses common scalars `Î¸0, Ï€1, Ï€2`; do not cite it for region/year/occupation-varying access (cite the companion 1995/1999/2004 papers for that, with verification).
- **No occupation / no sector.** There is no occupation object; do not cite it for `loc4` or any occupation-as-access design, and there is correspondingly no NACE/ISCO conflation in it.
- **"Random opportunities" framing:** the paper's opportunity density is a **deterministic** density estimated by ML; the randomness is in the EV1 utility shocks. Consistent with my deterministic-opportunities stance â€” do not import a "random opportunities" reading.
- **Theory-paper boundary:** this is an empirical/methodological paper; it has no bearing on the Haydarâ€“Maniquet axiomatic characterisation, and nothing in it should be read as a theory contribution to the JMP.

---

## 14. Direct quotes worth citing
(Short verbatim excerpts; page numbers as printed. Use sparingly and attribute.)
- p. 593, on the correction: "consistent estimates of v(f(wh, I), h) can still be obtained when the true choice set B is replaced by S".
- p. 605, on the headline lesson: "the ability of a model to replicate observed outcomes is not very informative".
- p. 595, on the offered-hours density: peaks make it "more likely to find jobs with hours that accord with full-time and standard part-time positions".

---

## 15. Open questions and risks for my draft
- **Common vs individualised proposal.** This paper individualises *nothing* in its offered-hours/market proposal, so it cannot, by itself, justify my partly-individualised proposal (wage/occupation conditioned on `x_i`); I must lean on the proposal-individualisation audit and the companion papers, not this one.
- **Recovery â‰  prediction performance.** The paper's validation target is *out-of-sample prediction*, not *parameter recovery*; my certification claim is recovery-based. Cite carefully: it supports "in-sample fit is insufficient," but it is not itself a parameter-recovery proof (though Table A2 lets one inspect parameter dispersion across designs).
- **Integration node count.** Their true-model fit used 1,000 alternatives; my 101 (singles) is far thinner. The paper's finding that coarse sets degrade distribution tails is a flag for my thin-ESS singles households (cross-references my welfare-integration ESS gate).
- **Endogenous wage handling.** They estimate the wage equation jointly with Heckman selection; my pipeline treats the wage technology as an ability sub-block of `g`. The architectural difference must be stated so a referee does not read my ability channel as their wage equation.
- **No numerical-implementation detail.** Optimiser, starting values, and multistart are not reported [verify], so the paper cannot be cited for numerical-stability practice.

---

## 16. TL;DR for retrieval
Methodological/simulation paper establishing that, in a RUM labour-supply model with an explicit **hours/market opportunity density** and a Boxâ€“Cox **preference** utility, the sampling-of-alternatives estimator with the `âˆ’ln q` **proposal/prior correction** (McFadden 1978) is consistent, and that choice-set representation barely affects in-sample fit but strongly affects out-of-sample policy prediction â€” the precedent for my synthetic-recovery-over-fit standard and my `âˆ’log Ï€` correction. It carries **no welfare object, no inequality decomposition, no ability-as-opportunity channel, and no occupation**, so it informs only the **estimation/access** and **recovery-design** parts of my JMP, never the welfare (WÂ¹â€“Wâ¶) or three-way decomposition layers. The opportunity density is **deterministic** and estimated, consistent with my deterministic-opportunities framing; it is an empirical/methodological source with no connection to the Haydarâ€“Maniquet theory paper.
# Audoly, McGee, Ocampo & Paz-Pardo 2025 â€” A Practitioner's Note on the Shapley-Owen-Shorrocks Decomposition

> Source of truth: the attached PDF (FRBNY Staff Reports no. 1163, August 2025).
> All page references below are to that PDF. Claims are tagged
> **[explicit]** (stated in the source), **[analogy]** (derived by me, mapping to
> my JMP), or **[not-established]** (the source does not address it). `[verify]`
> marks anything I could not confirm directly in the PDF.

---

## 0. Metadata

- **BibTeX key:** `audoly_mcgee_ocampo_pazpardo_2025` `[verify exact key]`
- **Authors:** Richard Audoly (FRB New York); Rory McGee (UWO & IFS);
  Sergio Ocampo (UWO); Gonzalo Paz-Pardo (ECB). **[explicit, p. 2]**
- **Year:** 2025 (August). **[explicit, p. 2]**
- **Outlet:** Federal Reserve Bank of New York Staff Reports, no. 1163.
  **[explicit, p. 2]**
- **DOI/URL:** https://doi.org/10.59576/sr.1163 **[explicit, p. 2]**
- **PDF filename:** `Audoly_et_al_2025_A_Practitioner_s_Note_on_the_Shapley-Owen-Shorrocks_Decomposition.pdf`
- **Tier:** T1A.
- **JMP block(s) served:** **decomposition** (primary); secondarily
  **welfare** (the note explicitly flags welfare-decomposition-from-counterfactuals
  as an application, p. 9) and **methodology / data-infrastructure** (it ships a
  reference algorithm and Matlab implementation, pp. 4, 12). It does **not** serve
  estimation, identification, the opportunity mechanism, or normative
  interpretation. **[explicit + analogy]**
- **JEL / keywords (source's own):** JEL B4; keywords "decomposition,
  methodology." **[explicit, p. 2]**
- **Provenance:** the note previously appeared as an appendix to the authors'
  paper "The Life-Cycle Dynamics of Wealth Mobility." **[explicit, p. 2]**

---

## 1. One-paragraph relevance to my JMP

This is the methodological primitive behind my **headline three-way
access/ability/preference Shapleyâ€“Shorrocks decomposition of welfare
inequality**. It states, defines, and proves-by-property exactly the
decomposition I invoke when I write "Shapleyâ€“Shorrocks, order-independent,
exhausts total inequality": the four axioms (exact additivity, symmetry,
null-factor zeroing, linearity in the decomposed function) and the closed-form
weighted-permutation contribution formula. **[explicit, pp. 2â€“4]** It speaks to
**none** of my three economic channels directly â€” access, ability, and
preference are *my* economic labelling of the inputs; the note is channel-blind
and treats inputs as abstract "players." Its decisive contributions for me are
(i) the **Owen generalisation to unions of players**, which is the formal license
for my channels being *groups* of parameters (preference = 20 params, ability =
6, access = 23) rather than single inputs **[explicit, p. 3]**; and (ii) the
explicit statement that this machinery applies to a decomposed function that is
itself **a Gini coefficient or any sample transformation** **[explicit, p. 4]**,
which is precisely my $I(\Omega^k)$. It is a citation for *method validity and
order-independence*, not for any economic finding.

---

## 2. Data and setting

**N/A as a data paper.** The note has no dataset, no country, no sample unit,
no sample size, no estimation. **[explicit â€” it is a methodological note,
pp. 1â€“9]** Its examples are algebraic toy models (a linear three-variable model,
two nonlinear three-variable models, and an $R^2$ decomposition of a linear
regression), not empirical applications. **[explicit, pp. 4â€“8]**

**Transport to my France pooled 2015â€“2017 EUROMOD cross-section:** the *method*
transports completely and is setting-agnostic â€” it places **no** requirement on
panel structure, administrative match, instruments, or offer/vacancy data.
**[explicit by omission + analogy]** What it does **not** supply, and what I
therefore do not have from this source: any guidance on standard errors /
inference for the decomposition components (the note is silent on sampling
variability of the Shapley shares), and any treatment of *how* the inputs are
identified or estimated â€” it takes the function $f$ and its inputs as given.
**[not-established]** My cluster-robust bootstrap on `idorighh` and my synthetic-
recovery certification are entirely outside this note's scope.

---

## 3. Model and objects (map object-by-object to mine)

The note has **no structural labour-supply model, no choice set, no utility, no
opportunity mechanism, no budget map.** **[explicit]** It is one level of
abstraction above all of these: it decomposes an *arbitrary* function
$Y = f(X_1,\dots,X_n)$ into the contributions of its arguments. **[explicit,
p. 4]** Object-by-object:

- **Their "function $f$" â†” my decomposed object.** For me, $f$ is the inequality
  index $I(\Omega^k)$ (a Gini) of the welfare distribution of measure $W^k$. The
  note explicitly licenses $f$ being "a transformation of the sample, for example
  the Gini coefficient." **[explicit, p. 4; analogy for the $W^k$ mapping]**
- **Their "arguments $X_j$" â†” my channels.** For me the arguments are the
  *equalisation operations* on access, ability, and preference (each channel a
  *group* of structural parameters). The note's arguments are abstract inputs â€”
  "a variable, policy function, or price." **[explicit, p. 3]** The grouping is
  legitimised by the Owen union extension (Â§3, p. 3) â€” see Â§7.
- **Their "null value $\varnothing_j$" â†” my "equalised-to-reference" state.** The
  note formalises sub-models by replacing absent arguments with a null value
  $\varnothing_j$, noting this can mean "setting some parameters to a
  predetermined value or excluding certain model components." **[explicit,
  footnote 2, p. 3]** In my design the "null"/baseline is the *equalised-to-
  reference-environment* state of a channel; this is a clean correspondence
  **[analogy]**, but note the difference: the note's canonical null is "zero"
  (zero regressor / zero parameter), whereas my null is "equalised to a reference
  distribution," not zero. The note's footnote 2 explicitly accommodates a
  predetermined non-zero null, so the mapping holds, but I must state my null
  state explicitly rather than inheriting "zero."

**Does any job attribute enter both utility and the opportunity mechanism?**
**N/A** â€” the note has no utility and no opportunity mechanism, so the
double-entry flag does not apply here. (This flag is for my structural sources;
this is a decomposition-method source.)

---

## 4. Estimation method

**N/A â€” no estimator, no likelihood, no choice-set construction, no proposal
density, no sampling-of-alternatives correction.** **[explicit]** The note's
"method" is a deterministic combinatorial formula evaluated over pre-computed
function values, not a statistical estimator.

**Verdict (reusable for my RURO/JAX pipeline?):** **Not applicable to the
estimation step.** The note is reusable for the **post-estimation decomposition
step only**. Concretely: after $\hat\theta$ is certified and the welfare layer
produces $\Omega_i^k$, the note's algorithm (p. 4) is the exact procedure that
turns "welfare distribution under each channel-equalisation sub-model" into the
additive access/ability/preference shares. Name the step: **decomposition
post-processing of $I(\Omega^k)$**, not estimation.

---

## 4b. Proposal / sampling-of-alternatives correction

**N/A.** **[explicit]** The note contains no alternative sampling, no proposal
density, no McFadden-style correction, and no log-prior. Its "sampling" language
(the $\frac{(n-k-1)!\,k!}{n!}$ weight interpreted as the probability of drawing a
particular sub-model of size $k$ when all model sizes are equally likely, p. 4)
is the **combinatorial averaging weight inside the Shapley formula** â€” a weighting
over *permutation orders of inputs*, **not** an importance-sampling correction over
choice alternatives. **Do not conflate** this weight with my $-\log\pi$ proposal
correction; they are unrelated objects that both happen to involve probabilities.
**[explicit + flag]**

---

## 5. Opportunity mechanism

**N/A.** **[explicit]** The note has **no** opportunity mechanism, no
feasibility/availability model, no offer probabilities, no reservation-wage or
participation restriction, no density over alternatives. It does not vary
anything with region, education, demographic type, or local labour market,
because it has no economic content of that kind.

**Cost of this omission for my access/ability/preference decomposition:** none
introduced by the note â€” the note is simply silent. The note supplies the
*aggregator* (how to attribute a non-linear outcome to grouped inputs); the
*economic content* of access, ability, and preference â€” and the decision that
occupation (`loc4`, ISCO) is an **access** object and never industry (`lindi`,
NACE) â€” comes entirely from my model and my welfare spec, not from here. The note
neither helps nor hinders the access/ability boundary; it only guarantees that
*whatever* grouping I choose, the resulting shares are additive, symmetric, and
exhaustive.

---

## 6. Welfare object â€” and its place on my $W^1$â€“$W^6$ map

**The note does not compute welfare and does not contain any equivalent-income,
money-metric, EV/CV, or inclusive-value object of its own.** **[explicit]** It
therefore has **no** position on my $W^1$â€“$W^6$ family, and **does not contain
$W^1$â€“$W^6$** in any form. `[explicit â€” the $W^1$â€“$W^6$ family is my/Haydarâ€“
Maniquet content, wholly absent here]`

**What the note does say about welfare** (and the *only* thing it says):
in the Summary (p. 9) it observes that the decomposition "can also be useful in
the context of welfare decompositions from counterfactual exercises," citing
FlodÃ©n (2001) and Conesaâ€“Kitaoâ€“Krueger (2009) as exercises that **separate the
roles of changes in the aggregate level and distributions of consumption and
leisure for welfare**, and Moschiniâ€“Tran Xuan (2025) extending these to separate
gains from redistribution over the life cycle and across generations. It notes
such welfare decompositions are in general **order-dependent**, and that the
symmetry of Shapley-Owen-Shorrocks "can therefore enhance the interpretability of
welfare decompositions at little additional cost." **[explicit, p. 9]** This is a
**motivating pointer**, not a worked welfare construction.

**Verdict:** for the welfare *object* â€” **incompatible / inapplicable** (the note
has no welfare object). For my welfare-*inequality decomposition* â€” **directly
usable as the aggregator**: it is the formal warrant that my channel shares of
$I(\Omega^k)$ are well-defined and order-independent.

---

## 6b. Inclusive value and money-metric inversion

**N/A.** **[explicit]** The note uses no inclusive value / log-sum, no EV/CV, no
own-utility inversion, and takes no expectation over extreme-value shocks
(analytically or by simulation). None of my analytic-in-shocks importance-sampling
inversion machinery has any counterpart here. Do not cite this note for anything
about the inclusive value or money-metric inversion.

---

## 7. Inequality / decomposition content  [the core of this source]

This is the substance the note exists to deliver. **[explicit, pp. 2â€“9]**

- **Decomposition rule:** **Shapley-Owen-Shorrocks** â€” the Shapley value
  (Shapley 1953) for attributing a non-linear aggregate to its inputs, extended to
  *inequality* decomposition by Shorrocks (1999, 2013), and to *unions/groups of
  players* by Owen (1977). **[explicit, pp. 2â€“3]**
- **Inequality index:** **index-agnostic.** The note does not privilege Gini, MLD,
  Theil, etc.; it states the decomposed function $f$ can be "the Gini coefficient"
  or any sample transformation. **[explicit, p. 4]** â†’ My choice of Gini for
  $I(\Omega^k)$ is fully supported, and so would MLD/Theil be.
- **The four characterising properties** (the note's central formal claim; it
  asserts the decomposition is the **unique** decomposition satisfying all four):
  **[explicit, pp. 4â€“5]**
  1. **Exact decomposition under addition** â€” $\sum_{j=1}^n C_j = f(X_1,\dots,X_n)$
     (eq. 1, p. 4), so $C_j/f(\cdot)$ is the share attributable to $X_j$
     (interpretable as a proportion *as long as $f$ is non-negative*; the note
     flags that with negative $f$, components can be $C_j<0$ and the share reading
     can mislead â€” footnote 1, p. 5). **[explicit]**
  2. **Symmetry w.r.t. argument order** â€” the order in which $X_j$ is removed does
     not alter $C_j$. **[explicit, p. 5]** *This is the property I invoke as
     "order-independent."*
  3. **Null-factor zeroing (irrelevance normalisation)** â€” a factor that never
     changes the outcome gets $C_j=0$. **[explicit, p. 5]**
  4. **Linearity of the attribution operator in the decomposed function** â€” a
     closure requirement implying contributions rescale linearly with the outcome.
     **[explicit, p. 5]**
- **Closed-form contribution (eq. 2, p. 5):**
  $$
  C_j=\sum_{k=0}^{n-1}\frac{(n-k-1)!\,k!}{n!}
  \sum_{\substack{s\subseteq S_k\setminus\{X_j\}:\,|s|=k}}
  \big[f(s\cup\{X_j\})-f(s)\big].
  $$
  **[explicit]** The weight $\frac{(n-k-1)!\,k!}{n!}$ is the probability that a
  size-$k$ sub-model is selected when all model sizes are equally likely; this
  weighting is what delivers symmetry. **[explicit, pp. 5, 8]**
- **Counterfactual / "zeroing-out" construction:** each input is included or
  excluded across all $2^n$ sub-models; an excluded input is set to its **null
  value $\varnothing_j$** (zero regressor/parameter in the regression examples, or
  "setting some parameters to a predetermined value or excluding certain model
  components" in structural models â€” footnote 2, p. 3). The decomposition is
  additive **relative to the null model** (the all-excluded reference): the
  worked nonlinear example shows the intercept $\beta_0$ drops out, i.e. the
  decomposition recovers $f(X_1,X_2,X_3)-f(\varnothing_1,\varnothing_2,\varnothing_3)$,
  **not** the level including the null-model value. **[explicit, pp. 6â€“7]** For the
  $R^2$ example the null model has $R^2(\varnothing)=0$, so there the
  decomposition recovers the *full* $R^2$ level. **[explicit, p. 8]**
  â†’ **Design consequence for me:** my reported channel shares sum to
  $I(\Omega^k)-I(\text{null/all-equalised})$, **not** to $I(\Omega^k)$ outright,
  unless my all-channels-equalised state has zero inequality. I must declare what
  my "all-equalised" reference produces and whether my exhaustiveness gate targets
  $I(\Omega^k)$ or $I(\Omega^k)-I(\text{reference})$. The note makes this reference
  dependence explicit and is the right citation for stating it.
- **Owen grouping (decisive for my three channels):** the same concept applies
  "when a group of inputs moves together, as is the case when changing all prices
  or initial conditions in counterfactuals," via Owen's (1977) generalisation to
  unions of players. **[explicit, p. 3]** The Summary adds that **judiciously
  grouping factors can minimise the computational cost**, which grows
  substantially with the number of factors. **[explicit, p. 9]** â†’ This is the
  formal warrant for treating preference / ability / access as three *grouped*
  players rather than ~47 individual parameters, and the practical argument for
  doing so (cost $\sim 2^n$).
- **Cost:** $2^n$ sub-model evaluations; the note states the cost "grows
  substantially with the number of factors" and recommends grouping to contain it.
  **[explicit, pp. 8â€“9]** â†’ With $n=3$ channels this is $2^3=8$ welfare-distribution
  evaluations per measure, trivial; the $n$ that matters for me is the channel
  count, not the parameter count, *because* of Owen grouping.

**Verdict (reusable for my three-way access/ability/preference split anchored on
$W^3$/$W^5$/$W^1$?):** **Yes, directly.** This note *is* the method I cite for
that split. It is **not two-way** and imposes no two-way restriction â€” it is
$n$-ary and group-aware, so it accommodates three channels natively with **no
extension required**. (Contrast: a source that only did factor-component or a
two-way opportunity-vs-preference cut would need extending; this one does not.)

---

## 8. Identification and the separation of preferences from opportunities

**N/A â€” and important to state plainly.** **[explicit]** The note contributes
**nothing** to identification. It assumes the inputs $X_j$ and the function $f$
are already given, and says nothing about what identifies tastes vs constraints,
nor about distinguishing ability from access. The clean separation of preference
from opportunity, and of ability from access, is an **identifying normative and
econometric assumption made in my model and welfare spec** (the parameter-to-
channel membership table), **not** something this note supplies or validates.

**Defence against the "your decomposition is mechanical" referee â€” what this note
does and does not buy me.** It buys me that, *given* a channel partition, the
attribution is the unique additive, symmetric, exhaustive one â€” so the referee
cannot attack the *aggregation rule* as arbitrary or order-dependent. It does
**not** buy me the *channel partition itself*: the note is explicit that
contributions are defined relative to a chosen null and chosen inputs, so a
referee can still legitimately contest *which parameters are access vs ability vs
preference* and *what the equalised reference is*. That contest is mine to win
with the model and the synthetic-recovery argument, not with this citation. **Do
not oversell this note as resolving the mechanicalness critique â€” it resolves only
the order-dependence half of it.** **[explicit + analogy]**

---

## 9. Key results and magnitudes

**No empirical magnitudes** â€” the note reports no elasticities, welfare effects,
opportunity shares, or decomposition shares from data. **[explicit]** Its
"results" are algebraic identities from the toy examples, useful only as
worked checks:

- **Linear model** $Y=\beta_1X_1+\beta_2X_2+\beta_3X_3$: $C_j=\beta_jX_j$ exactly;
  order is irrelevant; the Shapley decomposition coincides with the usual
  regression decomposition. **[explicit, pp. 6â€“7]**
- **Nonlinear example I** $Y=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_3X_2$:
  $C_1=\beta_1X_1$ (linear entrant), and the interaction term is **split evenly** â€”
  $C_2=\beta_2X_2+\tfrac12\beta_3X_2X_3$, $C_3=\tfrac12\beta_3X_2X_3$. The intuition
  the note draws: $\beta_2X_2$ appears in all sub-models (probability 1 of
  appearing), the interaction $\beta_3X_2X_3$ appears in 2 of 4 (probability
  $\tfrac12$); weighting by probability of appearance enforces symmetry.
  **[explicit, pp. 6â€“9; eqs. 7â€“8]** â†’ **This is the single most useful takeaway for
  my decomposition's interpretation:** interaction effects between channels are
  **shared equally** between the interacting channels, not assigned to one. So any
  accessÃ—ability or preferenceÃ—access interaction in my welfare inequality is
  split 50/50 between the two channels involved â€” I should expect and report this,
  not be surprised by it.
- **$R^2$ example:** decomposing $R^2=\mathrm{SSE}/\mathrm{SST}$ of a linear
  regression is a **nonlinear** decomposition even though the model is linear; the
  null model gives $R^2(\varnothing)=0$ so the components recover the full $R^2$;
  the Shapley $R^2$ differs from the standard **partial $R^2$**, and the partial
  $R^2$ fails the exact-decomposition requirement and (applied iteratively) the
  symmetry requirement. **[explicit, pp. 7â€“8, 11; eqs. 11â€“16]**

**Benchmarking my own numbers:** the note offers no external benchmark for the
plausibility of my opportunity share or welfare spread. **[not-established]**

---

## 10. Estimators, theorems, or formal results

**Result R1 â€” uniqueness of the Shapley-Owen-Shorrocks decomposition.**
*Statement (near-verbatim, p. 4):* the decomposition is "the unique decomposition
satisfying four important properties" â€” (i) exact additivity
$\sum_{j=1}^n C_j=f(X_1,\dots,X_n)$; (ii) symmetry in argument order; (iii) zero
contribution to null-effect factors; (iv) linearity of the attribution operator
in the decomposed function. **[explicit]**
*Assumptions:* a function $f$ with a well-defined null value $\varnothing_j$ for
each argument; finite input set. **[explicit, footnote 2]**
*Technique (bullets):*
- treat each input as a player, the outcome as the surplus of the coalition;
- average the marginal contribution $f(s\cup\{X_j\})-f(s)$ over all sub-models $s$
  not containing $j$;
- weight each sub-model size $k$ by $\frac{(n-k-1)!\,k!}{n!}$ (equal probability
  over model sizes), which enforces symmetry;
- Owen (1977) extends the same averaging to unions of players (groups).
*Verdict (reusability):* **Yes** for my **decomposition layer** â€” this is the
theorem I cite for additivity + order-independence + exhaustiveness of the
access/ability/preference shares. **No** for my estimation or welfare-inversion
layers (out of scope).

**Result R2 â€” closed-form contribution (eq. 2, p. 5).** Statement reproduced in
Â§7. *Reusability:* **Yes** â€” directly implementable; for $n=3$ channels it is the
8-row sub-model enumeration. The note ships a **Matlab reference implementation**
(`shapley_owen_shorrocks(X_ind, f_vals)`, p. 12) taking a binary $2^n\times n$
sub-model indicator matrix and a $2^n$ vector of function values, returning the
$n\times1$ contribution vector. **[explicit]** â†’ I should port this to
Python/JAX as my decomposition post-processor and unit-test it against the note's
toy examples (linear â†’ $C_j=\beta_jX_j$; nonlinear I â†’ the half-split) as exact
recovery checks. **[analogy â€” porting/test plan is mine, not the note's]**

**Algorithm A1 â€” the SOS algorithm (p. 4).** For each input $j$: initialise
$C(j)=0$; loop sub-model sizes $k=0,\dots,n-1$; weight $\omega_k=\frac{(n-k-1)!\,k!}{n!}$;
find rows with $k$ inputs excluding $j$; accumulate
$C(j)\mathrel{+}=\omega_k\,[F(s\cup\{j\})-F(s)]$. **[explicit]** *Reusability:*
**Yes**, this is the spec for my implementation.

---

## 11. Robustness and specification sensitivity

The note's relevant "robustness" content is methodological, not empirical:

- **Reference/null-state dependence.** The decomposition is additive *relative to
  the null model*; what the components sum to depends on the null
  ($f(\cdot)-f(\varnothing)$ in nonlinear example I; full level in the $R^2$ case
  where $f(\varnothing)=0$). **[explicit, pp. 7â€“8]** â†’ My robustness section must
  report sensitivity to the **equalised-reference definition** (my null), exactly
  the cut my welfare spec flags (e.g. education-as-access vs education-as-ability
  re-allocation; pinned-preference held-vs-swapped). The note is the citation for
  *why* this matters formally.
- **Grouping choice.** Because cost is $2^n$ and grouping is legitimate (Owen),
  *how* I group parameters into channels is a specification choice with both
  cost and interpretation consequences. **[explicit, pp. 3, 9]** â†’ Robustness to
  the ability/access boundary (my Â§6.3 deferred re-allocation) is a *grouping*
  robustness in this note's language.
- **Order-robustness as the selling point vs alternatives.** The note praises
  Nakajimaâ€“Telyukova (2020) for providing robustness to alternative elimination
  orders, and criticises decompositions that report only one order (De Nardi et
  al. 2025) or are non-additive. **[explicit, p. 9]** â†’ This is my argument for
  choosing SOS over a single-order "zero-out" decomposition in the first place.

What it does **not** tell me to stress-test: choice-set size, number of draws,
number of starts, opportunity-set definitions, circumstance partitions â€” all
**out of scope** (no structural model here). **[not-established]**

---

## 12. What I can cite this paper for

- The **definition and four characterising axioms** of the
  Shapley-Owen-Shorrocks decomposition, and its **uniqueness** as the
  decomposition satisfying them (additivity, symmetry/order-independence,
  null-factor zeroing, linearity). **[explicit, pp. 4â€“5]**
- The **closed-form contribution formula** (eq. 2) and the **algorithm**
  (p. 4) I implement. **[explicit]**
- That the decomposed function $f$ **may be a Gini coefficient or any sample
  transformation** â€” i.e. that decomposing $I(\Omega^k)$ is a legitimate use.
  **[explicit, p. 4]**
- The **Owen (1977) union/grouping extension**: the formal license to decompose
  **groups of inputs that move together** (my preference/ability/access channels),
  and the practical point that **grouping contains the $2^n$ cost**. **[explicit,
  pp. 3, 9]**
- That **interaction effects are split symmetrically** between interacting inputs
  (the half-split in nonlinear example I). **[explicit, pp. 6â€“9]**
- That the decomposition is **additive relative to a declared null/reference
  state**, with the components summing to $f(\cdot)-f(\varnothing)$. **[explicit,
  pp. 7â€“8]**
- That **Shapley-Owen-Shorrocks is well-suited to welfare decompositions from
  counterfactual exercises**, where single-order eliminations are otherwise
  order-dependent (citing FlodÃ©n 2001; Conesaâ€“Kitaoâ€“Krueger 2009;
  Moschiniâ€“Tran Xuan 2025). **[explicit, p. 9]**
- The **distinction from partial $R^2$** (Shapley $R^2 \ne$ partial $R^2$; partial
  $R^2$ violates exactness and, iterated, symmetry) â€” useful if a referee proposes
  a partial/sequential alternative. **[explicit, pp. 7â€“8, 11]**
- As a **recent, practitioner-facing secondary citation** for the method,
  alongside the **primary** Shorrocks (1999, 2013) and the game-theoretic roots
  Shapley (1953) / Owen (1977). **[explicit, references pp. 10â€“11]**

---

## 13. What I should NOT cite this paper for  [overclaim risks]

- **Not** for any **economic finding, magnitude, elasticity, welfare effect, or
  opportunity share** â€” it reports none. **[explicit]**
- **Not** as a source of the **access/ability/preference channels** themselves,
  nor of any opportunity/preference economics â€” it is channel-blind; the channels
  are my model's content. Do not let the note's authority bleed into the channel
  partition.
- **Not** for **identification** of preferences vs opportunities, or ability vs
  access â€” silent on all of it (Â§8). Do not cite it against the "mechanical
  decomposition" referee on the *partition* question; it answers only the
  *order-dependence* question.
- **Not** for **inference / standard errors** on the decomposition shares â€” the
  note gives no sampling theory for the Shapley components. My cluster-robust
  bootstrap is unsupported by this source.
- **Not** for any **welfare object** ($W^1$â€“$W^6$, equivalent income, EV/CV,
  inclusive value, money-metric inversion). The note **does not contain
  $W^1$â€“$W^6$** and constructs no welfare metric; its welfare relevance is a
  one-paragraph pointer (p. 9), not a construction.
- **Boundary flags:**
  - **Two-way vs three-way:** N/A as a limitation here â€” the note is $n$-ary, so
    it does *not* impose a two-way structure; do not describe it as a two-factor
    method.
  - **Ex-post / universal-set welfare:** N/A â€” no welfare object to mischaracterise.
  - **"Sectoral"/industry language:** the note never mentions occupation or
    industry; do not import its "inputs/players" abstraction as if it endorsed
    occupation-as-access. The occupation (`loc4`, ISCO) vs industry (`lindi`,
    NACE) distinction is entirely mine.
  - **Random vs deterministic opportunities:** the note's probability language is
    the **permutation-order weight** inside the Shapley formula, **not** any claim
    about random opportunities. Do not read it as bearing on the random-vs-
    deterministic-opportunity framing.
  - **Theory-paper boundary:** trivially respected â€” the note is unrelated to the
    Haydarâ€“Maniquet axioms; never let "uniqueness/characterisation" language in
    *this* note be confused with the companion paper's *welfare-measure*
    characterisation. They are different objects (a decomposition operator vs a
    family of welfare measures).

---

## 14. Direct quotes worth citing

Short, exact, verbatim, with page numbers (each â‰¤ 1 quote per use, kept brief):

1. p. 4: "the order in which the arguments are removed matters in general for the
   decomposition." `[verify exact wording â€” p. 4]`
2. p. 5: "Symmetry with respect to the order of the arguments." (property heading)
   **[explicit]**
3. p. 4: the decomposition "can be ... the Gini coefficient." `[verify exact
   wording â€” p. 4]`
4. p. 3: "the same concept applies when a group of inputs moves together."
   `[verify exact wording â€” p. 3]`
5. p. 9: the symmetry of the decomposition "can therefore enhance the
   interpretability of welfare decompositions at little additional cost."
   `[verify exact wording â€” p. 9]`

> I have paraphrased rather than transcribed long passages; the five above are
> short fragments. Verify each against the PDF before quoting in the draft.

---

## 15. Open questions and risks for my draft

- **Null/reference state must be declared.** The note makes the decomposition
  reference-dependent (sums to $f(\cdot)-f(\varnothing)$). My draft must state what
  the all-channels-equalised welfare inequality is and whether my exhaustiveness
  gate targets $I(\Omega^k)$ or $I(\Omega^k)-I(\text{reference})$. Leaving this
  implicit is a referee opening.
- **Inference gap is mine to fill.** The note gives no variance theory for the
  shares; my cluster-robust bootstrap on `idorighh` is the right instrument but
  cannot cite this note for it. Budget the bootstrap cost (it scales with the
  measure menu Ã— the $2^n$ sub-models).
- **Interaction-splitting must be communicated.** Because cross-channel
  interactions are split 50/50, a reader expecting interactions assigned to "the
  opportunity side" will misread the shares. Pre-empt this in the decomposition
  section.
- **Grouping is a specification choice, not a neutral act.** The ability/access
  boundary (education-as-ability vs education-as-access) changes the *grouping*
  and hence the shares; the note frames this as legitimate but consequential.
  Tie my Â§6.3 re-allocation robustness to this explicitly.
- **Non-negativity caveat (footnote 1, p. 5).** Share interpretation $C_j/f$ is
  clean only for non-negative $f$. A Gini is non-negative, so this is satisfied for
  $I(\Omega^k)$; but if I ever decompose a *signed* welfare gap, components can go
  negative and the proportion reading breaks. Note this where relevant.

---

## 16. TL;DR for retrieval

A FRBNY practitioner note (Audolyâ€“McGeeâ€“Ocampoâ€“Paz-Pardo 2025) that defines the
**Shapley-Owen-Shorrocks decomposition** of an arbitrary non-linear function into
additive, order-independent, exhaustive contributions of its inputs â€” the exact
method I cite for my **three-way access/ability/preference** decomposition of
welfare-inequality $I(\Omega^k)$, with the **Owen union extension** licensing
*grouped* channels and bounding the $2^n$ cost. It carries **no economic content,
no welfare object, no $W^1$â€“$W^6$, no identification, and no inference theory** â€”
it informs the **decomposition aggregator only**, supplying the uniqueness axioms
(eq. 1), the contribution formula (eq. 2), a Matlab reference implementation, and
the key interpretive facts (interactions split symmetrically; additivity is
relative to a declared null). It speaks to **none** of the access/ability/
preference channels economically and bears on **no** welfare measure; its sole
welfare relevance is a one-paragraph pointer (p. 9) that SOS improves the
interpretability of order-dependent counterfactual welfare decompositions.
# Bargain, Decoster, Dolls, Neumann, Peichl & Siegloch 2013 â€” Welfare, labor supply and heterogeneous preferences: evidence for Europe and the US

> Retrieval-oriented T1A summary for *"Unequal Job Opportunities and Well-Being
> Inequality: A Latent-Jobs Structural Decomposition"* (Haydar 2026). Source of
> truth: the attached PDF. Page numbers refer to the journal pagination
> (789â€“817) as printed on the PDF pages. Convention: **explicit-in-source** =
> stated in the paper; **derived-by-analogy** = my mapping to the JMP, not the
> paper's claim; **not-established** = the paper does not do this.

---

## 0. Metadata

- **BibTeX key:** `Bargain_et_al_2013`
- **Authors:** Olivier Bargain; AndrÃ© Decoster; Mathias Dolls; Dirk Neumann; Andreas Peichl; Sebastian Siegloch.
- **Year:** 2013 (received 3 Nov 2011; accepted 8 Oct 2012; published online 19 Oct 2012).
- **Outlet:** *Social Choice and Welfare*, vol. 41, pp. 789â€“817. Issue number 41(4) [verify â€” only the volume and page range are printed on the PDF].
- **DOI:** 10.1007/s00355-012-0707-x (p. 789).
- **PDF filename:** `Bargain_et_al_2013_Welfare__labor_supply_and_heterogeneous_preferences.pdf`
- **Tier:** T1A.
- **JMP block(s) served:** welfare (primary); estimation; normative-interpretation; data-infrastructure; motivation. **Does not** serve opportunity-mechanism (access/ability) or decomposition design in my sense â€” see Â§5, Â§7, Â§13.

---

## 1. One-paragraph relevance to my JMP

This is the canonical empirical statement of the preference-respecting,
money-metric **equivalent-income** welfare programme on EUROMOD discrete-choice
labour supply, and my welfare layer is the same construction lineage (King 1983;
Fleurbaey 2006, 2008): a single estimated Boxâ€“Cox preference, a *menu* of
money-metric references, and the spread across the menu as the object of
interest. It speaks directly to my **preference** channel and to the welfare
object's computational core (deterministic-utility indifference curves, expected
utility over the random-utility distribution, tangency-search inversion). Its
normative menu â€” "rent", "rent + reference wage", "wage" â€” is a
compensationâ€“responsibility spectrum, but the axis is **responsibility for
work preferences (willingness-to-work)**, which is near-orthogonal to my
Independence-of-pay / Independence-of-access axis; the three metrics are
therefore *not* my $W^1$â€“$W^6$ and must not be presented as such (Â§6, Â§13). Its
load-bearing relevance for the JMP's *motivation* is its own concession that the
model omits demand-side opportunity constraints and that estimated
country-specific "preferences" plausibly absorb opportunity/institutional
differences â€” precisely the conflation my opportunity layer exists to undo.

---

## 2. Data and setting

- **Countries/years:** 11 European countries (AT, BE, DK, FI, FR, GE/DE, IE, NL, PT, SW, UK) plus the US (p. 790, fn. 1). EU microdata are tied to tax-benefit systems for **1998 or 2001** (p. 800); the US uses **2006 IPUMS-CPS** data covering income **year 2005** (p. 800). France in their data is a single cross-section circa **2001** (Table 1, p. 802).
- **Dataset:** harmonised household surveys combined with national tax-benefit simulation, as described in Bargain et al. (2012) for the EU; IPUMS-CPS for the US (p. 800). [The specific EU survey per country is listed in the Acknowledgements, p. 815: ECHP / EU-SILC and national equivalents; FR is the INSEE EBF â€” explicit-in-source.]
- **Sample unit:** "unitary" household; **couples treated as a single decision maker**, with the analysis modelling **married women's** labour supply and **husbands' hours held fixed** (p. 798). Sample restricted to households where husbands work $\geq 30$ h/week, women aged 18â€“59 and available for the market (p. 800).
- **Sample size:** **42,975 households** pooled across countries (Table 1 note, p. 802).
- **Key variables:** household net income, non-labour income (incl. husband's earnings), female hourly wage, female weekly hours, participation (Table 1, p. 802). Taste-shifters $z_i$: ages of both spouses, woman's education, children <3 / 3â€“6 / 7â€“12, region (p. 799, eq. 6).
- **Budget set:** net income $c_{ij}=f(w_i h_{ij}, I_i, x_i)$ computed at each discrete hours point by **EUROMOD** (EU) and **TAXSIM** (US) (p. 800). Female wages **predicted for all observations** with a standard selection-bias correction (p. 800).
- **Discretisation:** $J=7$ hours categories â€” non-participation, two part-time, two full-time, two over-time, spanning 0â€“60 h/week in steps of 10 h (p. 800).

**Transport to my France pooled 2015â€“2017 EUROMOD cross-section.** Strong on the
welfare-and-budget machinery: same EUROMOD disposable-income budget construction,
same Boxâ€“Cox discrete-choice family, and France is one of their countries (FR
2001). Weak on unit and scope: they are **married women, couples-as-unitary with
the husband fixed**, a single cross-section per country; my baseline is **three
groups (single males, single females, couples as a *joint* two-decider unit),
pooled across 2015/2016/2017**. Features they do **not** have, and that I also
do not have (so no advantage transfers): panel, administrative match, external
opportunity instrument, vacancy/offer data. Their cross-country dimension is
irrelevant to my within-France design.

---

## 3. Model and objects (object-by-object map to mine)

- **Choice set.** Fixed, **common** grid of $J=7$ hours alternatives (p. 800). This is **not** my latent-jobs set: it is a universal hours grid, not a household-specific feasible-job distribution. *(not-established: any household-specific feasible set.)*
- **Deterministic utility = my preference utility $v$.** Boxâ€“Cox over consumption and leisure (p. 798, eq. 5):
$$
u_i\big(c_{ij},\,T-h_{ij}\big)=\beta_c\,\frac{c_{ij}^{\alpha_c}-1}{\alpha_c}+\beta_{li}\,\frac{(T-h_{ij})^{\alpha_l}-1}{\alpha_l}.
$$
  Same functional family as my preference block; monotonicity/concavity hold under $\beta_c,\beta_{li}>0$, $\alpha_c,\alpha_l<1$ (p. 799), which is exactly why they (and I) use Boxâ€“Cox for tangency-based welfare. **Explicit-in-source.**
- **Random utility.** $V_{ij}=u_i(c_{ij},T-h_{ij})+\varepsilon_{ij}$ with i.i.d. EV-I shocks, giving conditional-logit choice probabilities (p. 798â€“799, eq. 4). My RURO per-alternative value adds opportunity-density terms and a proposal correction that this model does **not** contain (see Â§4, Â§5).
- **Opportunity / availability mechanism analogous to my $g$.** **None.** There is no opportunity density, no offer probabilities, no participation/hours-availability sub-block, no occupation channel. Opportunities enter *only* through the budget (wages + tax-benefit). They state plainly that they "do not model potential demand side restrictions on the labor market nor fixed costs of work" (p. 799). **Explicit-in-source (the absence is stated).**
- **Budget map = my EUROMOD disposable income.** Yes, in spirit: $c_{ij}=f(\cdot)$ via EUROMOD/TAXSIM = my `ils_dispy`-based consumption. **Explicit-in-source.**
- **Heterogeneity.** Country-specific deep parameters $(\alpha_c,\alpha_l,\beta_c,\beta_{l0})$ estimated separately per country; within-country household heterogeneity only through the leisure intercept $\beta_{li}=\beta_{l0}+\beta_{lz}z_i$ (p. 799, eq. 6). All systematic between-household variation is loaded into the **preference** block. **Explicit-in-source.**
- **Does any job attribute enter BOTH utility and the opportunity mechanism?** N/A â€” there is no opportunity mechanism, so the both-sides flag cannot fire. The structurally relevant observation for me is the *converse*: everything (including whatever is truly opportunity-driven) is absorbed into utility, by construction. **Derived-by-analogy (the implication for my taxonomy).**

---

## 4. Estimation method

- **Likelihood/estimator.** Conditional-logit maximum likelihood (McFadden 1974); EV-I shocks deliver closed-form logistic choice probabilities; estimated **separately by country** (p. 799). **Explicit-in-source.**
- **Choice-set construction.** Fixed common grid of $J=7$ alternatives â€” **not** sampled alternatives, no fixed-grid-of-draws (p. 800). **Explicit-in-source.**
- **Proposal/sampling density; prior/proposal correction.** **None** â€” because the grid is enumerated, not sampled, there is no McFadden sampling-of-alternatives correction and **no $\log(\text{prior})$ term**. **Explicit-in-source (by construction of the enumerated grid).** This is a first-order contrast with my RURO engine (Â§4b).
- **Normalisation/scale.** Standard logit scale via the EV-I assumption; consumption scale carried by $\beta_c$ (estimated, not normalised to 1 here â€” contrast with my `beta_c=1`). **Explicit-in-source.**
- **Numerical method / starting values / multistart.** Not detailed in the printed text [verify â€” likely in Bargain et al. 2011/2012 companions]. **Not-established here.**
- **What pins preferences separately from the opportunity mechanism.** Nothing â€” there is no opportunity mechanism to separate from. Preferences are identified from observed choices over nonlinear tax-benefit budgets (van Soest logic; see Â§8). **Explicit-in-source.**

**Verdict (reuse for my RURO/JAX pipeline):** *partial / how* â€” the
**estimator is too thin** (a pure hours-grid conditional logit with no $g$ and no
proposal correction is the model my design departs from). What is reusable is the
**utility block** (Boxâ€“Cox specification and its tangency-friendly properties)
and the **welfare-computation steps** (Â§6, Â§6b), not the estimation architecture.

---

## 4b. Proposal / sampling-of-alternatives correction

**Not applicable / not present.** The model enumerates a common $J=7$ hours grid,
so there is no proposal distribution, no per-alternative log-prior, and no
McFadden correction (p. 800). There is consequently nothing to "individualise":
the only individualised input is the **predicted female wage** (Heckman-corrected,
p. 800), which feeds the *budget*, not a sampling proposal. **Relevance to my
importance-sampling welfare integrator:** none as a method to import; the value is
as the **null model** â€” it shows that the standard equivalent-income welfare
literature operates with *no* proposal correction at all because it never samples
a feasible set, which is exactly the machinery my ex-ante constrained-set object
adds and must defend. **Explicit-in-source (absence); derived-by-analogy (the
contrast).**

---

## 5. Opportunity mechanism  [MOST IMPORTANT]

**There is no explicit opportunity mechanism.** Stated exhaustively, channel by
channel against my three sub-objects:

- **access (hours / market-participation / region / year / occupation offers).** **Absent.** The hours set is a common universal grid; there is no offer probability, no participation restriction beyond the sample-selection rules, no region/year/local-labour-market variation in *feasibility*. Region enters only as a *taste-shifter* inside $\beta_{li}$ (p. 799), i.e. on the **preference** side, not as access. **Explicit-in-source.**
- **ability (wage technology: returns to education/experience, residual productivity $\sigma$).** **Not present as an opportunity object.** Wages are *imputed* once via a Heckman-corrected wage equation and then enter the budget as a fixed input (p. 800). There is no structural wage-return sub-block inside an opportunity density and no residual-productivity dispersion parameter analogous to my $\sigma$. So my **ability** channel has no counterpart here. **Explicit-in-source (wages are an imputation input); derived-by-analogy (the absence of an ability *opportunity* object).**
- **occupation.** **Not modelled at all** â€” no occupation, no sector/industry. There is therefore **no sector/occupation conflation to flag**, and equally no occupation-as-access content to borrow. **Explicit-in-source (absence).**

**Functional form of the (non-)mechanism:** opportunities are encoded entirely by
the budget $c_{ij}=f(w_ih_{ij},I_i,x_i)$ and the common hours grid. The paper is
candid about the omission and names it as future work: it flags **demand-side
constraints, fixed costs of work, and "country-specific choice opportunities"**
as needed extensions left undone (pp. 799, 826). **Explicit-in-source.**

**Cost to my access/ability/preference decomposition if I inherited this design.**
Total: the decomposition would be impossible. With no $g$, every opportunity
difference is folded into the estimated preference parameters, so an
"opportunity vs preference" (let alone three-way) split cannot be formed â€” the
opportunity content would be mechanically zero and the preference content would
be inflated by exactly the absorbed access/ability variation. This is the
identification gap my opportunity layer is built to close, and Bargain et al. is
the cleanest citable instance of the gap. **Derived-by-analogy (consequence for
my design); the underlying absorption concern is explicit-in-source (pp. 799,
826).**

---

## 6. Welfare object â€” and its place on my $W^1$â€“$W^6$ map

**Yes, the paper computes welfare:** individual-level, **money-metric**,
preference-respecting **equivalent income**, defined over the
**consumptionâ€“leisure** space and evaluated on the *deterministic* utility (so
indifference curves are well-behaved). Three metrics (p. 795, eqs. 1â€“3):

- **"wage" metric** â€” minimum hypothetical net wage delivering utility $u$ at **zero** virtual non-labour income:
$$
\nu_i^{W}(u,\mu_r=0)=\min_{\tilde w_i}\big[\tilde w_i \mid v_i(\tilde w_i,\mu_r=0)\ge u\big]. \quad (\text{eq. 1})
$$
- **"rent + reference wage" metric** â€” virtual non-labour income (expenditure function) at a **reference wage** $w_r$:
$$
\nu_i^{RW}(u,w_r)=e_i(u,w_r)=\min_{\mu_i}\big[c_i-w_r h_i \mid u_i(c_i,h_i)\ge u\big]. \quad (\text{eq. 2})
$$
- **"rent" metric** â€” consumption at zero hours (IC intercept with the ordinate), $w_r=h_r=0$:
$$
\nu_i^{R}(u,h_r=0)=c_i(u,0)=\min_{c_i}\big[c_i \mid u_i(c_i,0)\ge u\big]. \quad (\text{eq. 3})
$$

- **Universal vs constrained set.** Defined on each household's own indifference curve over the **common** consumptionâ€“leisure space; there is **no constrained-feasible-set** object, because there is no opportunity set in the model. **Explicit-in-source.**
- **References used.** A reference virtual wage and/or virtual non-labour income. The "rent + reference wage" metric uses reference wages at **p25/p50/p75 of the pooled wage distribution** (Tables 3â€“4, pp. 807â€“808); "wage" sets $\mu_r=0$; "rent" sets $w_r=0$. **Explicit-in-source.**
- **Discrete-choice subtleties.** Handled by computing an **expected** welfare base over EV-I draws and then deriving deterministic ICs from it (full detail in Â§6b); the chosen-alternative selection is via per-draw argmax; integration over unobserved heterogeneity is by simulation, not analytically. **Explicit-in-source.**
- **Ex-ante vs ex-post.** The welfare base is the **simulated expected deterministic utility of the *chosen* alternative** (p. 801), i.e. an expected-realised-utility object â€” **not** my analytic ex-ante log-sum inclusive value over a feasible set. **Explicit-in-source.**

**Place on my $W^1$â€“$W^6$ map.** The paper **does not contain $W^1$â€“$W^6$** and
makes no Independence-of-$\mathbf{y}$ / Independence-of-$A$ classification.
*(not-established.)* Its three metrics span a compensationâ€“responsibility
spectrum on a **different axis**: responsibility for **work preferences /
willingness-to-work**. The "rent" metric compensates most for low
willingness-to-work (favours the work-averse, p. 796); the "wage" metric holds
individuals **maximally responsible** for willingness-to-work (p. 797, fn. 7);
"rent + reference wage" is intermediate. This is the *preference-axis* analogue
of a compensationâ€“responsibility spectrum â€” near-**orthogonal** to my
access/pay axis, in the same way JJT vary the preference axis (welfare spec Â§1.3).
Concretely: **all** my $W^1$â€“$W^6$ hold preferences *respected* and vary the
*opportunity* treatment (pay vs access), a dimension Bargain et al. do not have;
**their** three metrics hold the (absent) opportunity treatment fixed and vary
the *preference-responsibility* treatment, a dimension my family collapses by
respecting preferences throughout. So no single $W^k$ corresponds to a Bargain
metric. **Derived-by-analogy (the axis comparison); explicit-in-source (their
metrics' own responsibility readings, pp. 796â€“797).**

**Verdict:** the **construction** (Boxâ€“Cox ICs; rent analytic intercept; tangency
search for rent+RW and wage) is **directly adaptable** to my welfare core; the
**normative classification is incompatible with my $W$-map** and must be cited
only as the *preference-responsibility* precedent, never as my access/ability
menu.

---

## 6b. Inclusive value and money-metric inversion

- **Inclusive value (log-sum)?** **No.** The welfare base is **not** the log-sum expected maximum. They draw $r=1,\dots,R$ EV-I shocks, take the **argmax alternative per draw**, record the **deterministic** utility of that alternative $u^{\max}_r$, and average: $\bar u=\tfrac1R\sum_r u^{\max}_r$, the "expected optimal utility", from which ICs are derived (p. 801). This is $\mathbb E[u(\text{chosen bundle})]$, deliberately stripping $\varepsilon$ from the welfare base â€” distinct from my analytic $\log\sum_j\exp(\cdot)$ inclusive value (which would retain the shock expectation). **Explicit-in-source.**
- **Expectation analytic or simulated?** **Simulated** (R draws), not analytic. Direct contrast with my **analytic-in-shocks** log-sum, which uses no FrÃ©chet/EV draws and no simulated argmax. **Explicit-in-source.**
- **Money-metric inversion.** The "rent" metric has a **closed-form** solution (set $h=0$ in the IC, read off consumption â€” the ordinate intercept). The "rent + reference wage" and "wage" metrics have **no analytic solution** under Boxâ€“Cox and are obtained by a **numerical tangency search**, incrementing hours from 0 to $T$ in steps of **0.01 h/week** along the IC until the MRS matches the reference (p. 801). This is a one-dimensional solve along the own-preference IC â€” the same shape as my **1-D bracketing root-solve** of the own-utility map, and importantly it does **not** bypass the household's own preferences. **Explicit-in-source.**

**Relevance:** the inversion step is reusable almost verbatim; the **expectation
step is not** â€” I should cite Bargain et al. for the equivalent-income inversion
and explicitly distinguish my analytic inclusive value from their simulated
expected-chosen-utility base (this difference is the substance of my welfare
spec guardrail "stochastic-choice analogue, stated").

---

## 7. Inequality / decomposition content

- **Inequality index.** **None of Gini/MLD/Theil/variance-of-logs/Atkinson.** The welfare comparison is **ordinal**: average **percentile rank** position by country in the pooled distribution, rank correlations, and CDF comparisons (Fig. 2 p. 805; Tables 3â€“4 pp. 807â€“808). No cardinal inequality index is decomposed. **Explicit-in-source.**
- **Decomposition rule.** A **two-scenario counterfactual swap**, not Shapley/Shorrocks. Holding individual **budgets and observed $(c,h)$ fixed** and **without re-estimation**, they switch on heterogeneity from one source at a time â€” country-specific **preference parameters** vs **socio-demographic composition** â€” and read off how the percentile rankings move (Â§5.3, pp. 810â€“812; Tables 5â€“6). **Explicit-in-source.**
- **Counterfactual construction.** Start from a **reference household** (median-MRS); introduce either demographic heterogeneity only (Table 6a) or preference-parameter heterogeneity only (Table 6b); recompute metrics and ranks. What is equalised: preferences set to the reference; what is varied: one source. **Explicit-in-source.**
- **Order-independence / path-independence / exhaustiveness.** **Not addressed** â€” it is a scenario comparison, not a Shapley average over orderings; no exhaustiveness identity is imposed. **Not-established.**

**Verdict (reuse for my three-way access/ability/preference Shapleyâ€“Shorrocks
split):** **not reusable as a decomposition method.** Two structural mismatches:
(i) it is **two-way**, and **both** sources (preference parameters, demographics)
live **inside my single preference channel** â€” it says nothing about access or
ability; (ii) it decomposes **ordinal reranking**, not a cardinal inequality
index, and is **not** Shapley. To reach my three-way split I would need an
opportunity object they lack **and** a Shorrocks index decomposition they do not
perform. What *does* carry over conceptually is the **"hold budgets and observed
choices fixed, swap one source at a time"** counterfactual logic; my Shapley
equalisation generalises that logic (averaging over orderings, summing to
$I(\Omega^k)$). **Derived-by-analogy.**

---

## 8. Identification and the separation of preferences from opportunities  [STRICT]

- **What identifies tastes.** Observed labour-supply choices over **known, nonlinear** tax-benefit budget constraints (van Soest 1995 logic). The tax-benefit system's nonlinearities and discontinuities generate **variation in net wages for the same gross wage** across households with different circumstances; this cross-sectional variation is the identifying source (p. 800, fn. 11). No panel, no external instrument. **Explicit-in-source.**
- **Separation of preferences from opportunities.** **Not attempted, and conceded as a limitation.** Because there is no opportunity object, identification of "preferences" is *conditional* on the common hours grid being the true feasible set. The paper explicitly warns that country-specific "preferences" may capture cross-country differences in **opportunities/institutions** (childcare, part-time availability, demand-side restrictions) (pp. 799, 826). So their "preference" estimates are, on their own admission, potentially **contaminated by access**. **Explicit-in-source.**
- **Ability vs access *within* opportunity.** N/A â€” no opportunity side to subdivide. **Not-established.**
- **Transport to my France pooled cross-section.** The **van Soest tax-benefit identification of preferences transports** (I use the same EUROMOD-budget nonlinearity). What does **not** transport â€” because they never attempt it â€” is the harder task my paper owns: identifying the **opportunity density separately from preferences without a panel or external instrument**. **My defence against the "your decomposition is mechanical" referee cannot lean on Bargain et al.**; they are the exhibit of *not* separating, and the burden falls on my **synthetic-recovery certification** (project state Â§3.6). They identify off cross-sectional tax-benefit variation, **not** synthetic recovery. **Explicit-in-source (their identification); derived-by-analogy (the transport judgement).**

---

## 9. Key results and magnitudes

- **MRS heterogeneity (Table 2, p. 804).** Full-sample mean MRS between consumption and hours $=8.7$ PPP-USD/h at the mean bundle; range from **Portugal 3.7** and **Finland 3.8** (low willingness-to-work compensation) to **Ireland 17.6**, **Austria 13.2**, **Germany 13.2**, **Netherlands 13.2** (high); **France 9.5**. A near **5Ã— spread** across countries. Units: 2001 PPP-USD per hour. **Explicit-in-source.**
- **Metric-dependent reranking (Table 3, p. 807).** Average percentile position shifts between the "rent" and "wage" metrics of **at least 15 percentage points for 7 of 12 countries** (abstract; Table 3 col. 8). Examples: **Ireland +27.4**, **Austria +19.7**, **Netherlands +17.2**, **Germany +14.5** (up); **Finland âˆ’20.4**, **Sweden âˆ’18.2**, **Denmark âˆ’16.7** (down). The **US** falls from income rank **63.3** to "wage" **56.7**; **Ireland** rises from **53.1** (income) to **73.9** ("wage"). **Explicit-in-source.**
- **Source of the reranking (Â§5.3, Tables 5â€“6, pp. 810â€“812).** **Country-specific preference parameters**, **not** demographic composition, drive the metric-dependent reranking (Table 6b mirrors the full result; Table 6a shows demographics alone move ranks little). France is a partial exception where demographics matter more (p. 812, fn. 24). **Explicit-in-source.**

**Benchmark value for my paper.** The *existence of a large across-measure spread*
(tens of percentile points) is encouraging for my welfare spec Â§5.2 expectation
that my own six-measure family will spread materially â€” but the **mechanism
differs**: their spread is **preference-driven across countries**; mine would be
**access/ability-driven within France**. I therefore use this only as *a priori*
reason to expect spread, **not** as a numerical benchmark for my opportunity
share or welfare gap. **Derived-by-analogy.**

---

## 10. Estimators, theorems, or formal results

The paper proves no theorems; it **applies** Fleurbaey's axiomatic results (cited,
not re-derived). The formal objects worth importing:

- **Three welfare metrics** (eqs. 1â€“3, p. 795) â€” restated in Â§6 above. *Assumptions:* well-behaved (continuous, increasing, quasi-concave) $u$; nonlinear budgets; tangency conditions. *Technique:* indirect utility / expenditure function on the deterministic IC; reference wage or reference non-labour income fixes the metric. **Verdict:** **reusable** as the inversion targets of my welfare core, with the normative-axis caveat of Â§6.
- **Boxâ€“Cox deterministic utility** (eq. 5, p. 798) â€” *Verdict:* **reusable**; it is already my preference family.
- **Random-utility / conditional-logit choice probability** (eq. 4 + EV-I, pp. 798â€“799). *Verdict:* **partial** â€” my RURO adds the opportunity-density and proposal-correction terms this lacks.
- **Taste-shifter parameterisation** $\beta_{li}=\beta_{l0}+\beta_{lz}z_i$ (eq. 6, p. 799). *Verdict:* **reusable** as the demographic-shifter form on the preference block.

No estimator is novel; all are standard MLE/numerical-inversion. **Explicit-in-source.**

---

## 11. Robustness and specification sensitivity

From Â§5.4 (pp. 812â€“814), with full detail deferred to Bargain et al. (2011):

- **Functional form.** Boxâ€“Cox vs **constrained quadratic** utility (with monotonicity/concavity imposed): MRS "very similar" (p. 813). Informs my preference-form robustness.
- **Choice-set size.** $J=7$ vs **13 categories** (5 h steps): estimation results robust (p. 813, fn. 25). Informs my grid-resolution / effective-sample-size concern â€” though note their grid is enumerated, so this is *not* evidence about importance-sampling node counts.
- **Welfare-metric computation.** Three handlings of the random component â€” baseline (expected utility over draws), (1) metrics per draw then average the *metrics*, (2) probability-weighted sum over discrete categories â€” leave the **orderings almost unaffected** (p. 813). Mild comfort that the welfare base choice is not knife-edge; **but** it does not speak to my analytic-log-sum-vs-simulated-argmax gap, which is a different object, nor to my ESS degeneracy for singles.
- **Reference household.** p10/p50/p90 of the MRS distribution as alternative references: levels move, **core results unchanged** (pp. 813â€“814). Direct precedent for my required **reference-preference sensitivity** report.

**What to stress-test in my paper, prompted by this:** preference functional form;
choice-set/integration resolution; the welfare-base/expectation method; and the
reference-preference choice. **Explicit-in-source.**

---

## 12. What I can cite this paper for

- The **canonical empirical implementation** of preference-respecting, money-metric **equivalent-income** welfare on EUROMOD discrete-choice labour supply (King/Fleurbaey lineage).
- The **three metric formulas** ("rent", "rent + reference wage", "wage") and their per-metric responsibility readings on the **willingness-to-work** axis (pp. 795â€“797, eqs. 1â€“3).
- The empirical fact that the **normative treatment of preference heterogeneity materially moves welfare rankings** ($\geq 15$ pp for 7/12 countries) (abstract; Table 3, p. 807).
- The **Boxâ€“Cox discrete-choice labour-supply specification** with demographic taste-shifters as a standard, welfare-suitable form (eqs. 5â€“6, pp. 798â€“799).
- The explicit **acknowledgement that standard models omit demand-side opportunity constraints**, and that estimated "preferences" may **absorb opportunity/institutional differences** â€” my motivation citation (pp. 799, 826).
- The **expected-utility-over-the-random-utility-distribution** approach to welfare in a logit model, and its **robustness** to the computation method and reference household (pp. 801, 813â€“814).
- The **counterfactual-swap** logic for attributing reranking to preference parameters vs demographic composition, holding budgets and observed choices fixed (Â§5.3).

---

## 13. What I should NOT cite this paper for  [overclaim risks]

- **NOT a three-way (or even opportunity-vs-preference) decomposition.** Its Â§5.3 decomposition is **two-way and entirely within my preference channel** (preference parameters vs demographics); it isolates **no access or ability** component.
- **NOT my $W^1$â€“$W^6$ family.** It contains **three** metrics on a **responsibility-for-preferences** axis, **not** the Independence-of-pay / Independence-of-access axis. Do **not** claim it contains, characterises, or instantiates any $W^k$.
- **NOT an ex-ante inclusive-value (log-sum) welfare object.** Its welfare base is the **simulated expected deterministic utility of the chosen alternative**, not the analytic log-sum over a feasible set. Do not present it as my constrained ex-ante object.
- **NOT an opportunity model.** No opportunity density, no access/ability object, no latent jobs, no offer probabilities. Do not cite for opportunity-mechanism design.
- **NOT a cardinal inequality decomposition.** Its inequality content is **ordinal percentile reranking**; there is no Gini/Theil/Atkinson and no Shorrocks decomposition.
- **"sectoral"/industry language.** It has **no occupation or sector object at all** â€” so do not attribute any occupation-as-access (or industry/NACE) content to it, in either direction.
- **random-opportunity framing.** N/A â€” there is no opportunity randomness; do not read any "RO" content into it. (Opportunities in my design are deterministic anyway.)
- **theory-paper boundary.** It grounds its metrics in **Fleurbaey (2006, 2008)** and **Fleurbaeyâ€“Maniquet (2006)** â€” a *different* reference set. Do **not** attribute the companion **Haydarâ€“Maniquet** axioms/characterisation/proofs to it, and do not let its presence in my welfare citations blur into the theory paper.
- **Sample boundary.** Married women, couples-as-unitary with **husbands' hours fixed**, single cross-section. Do not cite it for singles, for joint two-decider couples (my unit), or for pooled multi-year estimation.

---

## 14. Direct quotes worth citing

1. (Abstract, p. 790) "The resulting welfare rankings clearly depend on the normative treatment of preference heterogeneity with alternative metrics."
2. (p. 795) "The key feature of the metrics introduced above is that they fully respect preferences: all metrics increase when the individual moves to a bundle on a higher indifference curve of her own preference ordering."
3. (p. 796) "First, the 'rent' metric asks for the amount of (hypothetical) net income which would be enough to remain equally well off compared to the initial situation if one did no longer have to earn it."
4. (p. 797, fn. 7) "The 'wage' metric might thus be interpreted as holding individuals maximally responsible for their willingness-to-work."
5. (p. 799) "This particularly implies that we do not model potential demand side restrictions on the labor market nor fixed costs of work."
6. (p. 801) "This 'expected optimal utility' $\bar u$ is used to empirically derive individual indifference curves."
7. (p. 826) "Here, a specific and additionally demanding requirement in the present context would have been to determine country-specific choice opportunities."

---

## 15. Open questions and risks for my draft

- **The contamination they concede is the claim I must prove I undo.** They state that "preferences" may absorb opportunities (pp. 799, 826). A referee will ask whether my opportunity layer *genuinely* re-allocates that variation or merely **relabels** preference heterogeneity as access. My answer must be the **synthetic-recovery** certification (project state Â§3.6) and the standard-error asymmetry (opportunity tightly estimated, preference wide, Â§3.8) â€” not an appeal to Bargain et al.
- **My welfare base differs from theirs and I must defend "ex-ante".** Their simulated expected-chosen-utility vs my analytic log-sum inclusive value: I must name the realised-bundle-vs-inclusive-value gap explicitly (welfare spec guardrail 2) and justify the ex-ante stance as the only one that can carry the access channel (project state Â§2.3).
- **Integration error is a different beast for me.** Their robustness shows the *expectation method* barely moves orderings, but they **enumerate** the grid; my importance-sampling **ESS degeneracy for singles** (project state Â§7.1) has no analogue in their setting and cannot borrow comfort from their result.
- **Reference-preference sensitivity is mandatory, not optional.** Their results are robust to the reference household; my family computation must report the analogous **reference-preference sensitivity** for the preference-equalisation step of the decomposition.
- **Do not import their magnitude as my benchmark.** Their large spread is *cross-country preference-driven*; mine is *within-France access/ability-driven*. Borrowing "$\geq 15$ pp" as an expectation for my opportunity share would be a category error.

---

## 16. TL;DR for retrieval

Bargain et al. (2013) is the canonical EUROMOD discrete-choice implementation of
**preference-respecting money-metric equivalent income**, computing three
metrics ("rent" / "rent + reference wage" / "wage") that span a
compensationâ€“responsibility spectrum on the **preference (willingness-to-work)**
axis â€” informing my **preference** channel and my welfare-inversion core
(Boxâ€“Cox ICs, rent analytic intercept, tangency search), but **not** my
$W^1$â€“$W^6$ access/ability menu. It has **no opportunity mechanism** (no $g$, no
access/ability object, common hours grid) and explicitly concedes that estimated
"preferences" may absorb omitted opportunity constraints â€” making it the primary
**motivation** citation for my opportunity layer. Its Â§5.3 "decomposition" is a
**two-way preference-vs-demographics counterfactual swap on ordinal ranks**, not
a cardinal three-way Shapleyâ€“Shorrocks split, so it informs the
hold-fixed-and-swap *logic* but supplies neither the channels nor the method.
# Bhattacharya 2015 â€” Nonparametric Welfare Analysis for Discrete Choice

> Extraction produced against `JMP_T1_exhaustive_extraction_prompt_v2.md`.
> Source of truth: the attached PDF (Econometrica 83(2), 617â€“649). Project
> anchors (`JMP_project_state_v1.md`, `JMP_welfare_spec_v5.md`) used only for
> relevance judgments. Page numbers refer to the journal pagination (617â€“649)
> printed on the PDF. Tags used below: **[explicit]** = stated in the source;
> **[analogy]** = derived by analogy to my JMP, not in the source;
> **[not-established]** = the source does not establish this; **[verify]** =
> metadata or detail I could not confirm from the PDF text.

---

## 0. Metadata

- **BibTeX key:** Bhattacharya2015 [verify â€” key not specified in source]
- **Authors:** Debopam Bhattacharya (Dept. of Economics, University of Oxford). [explicit, p. 649]
- **Year:** 2015 (manuscript received June 2014; final revision November 2014). [explicit, p. 649]
- **Outlet:** *Econometrica*, Vol. 83, No. 2 (March 2015), pp. 617â€“649. [explicit, p. 617]
- **DOI/URL:** 10.3982/ECTA12574. [explicit, p. 617]
- **PDF filename:** `Bhattacharya_2015_Nonparametric_Welfare_Analysis_for_Discrete_Choice.pdf`. [explicit, upload]
- **Tier:** T1A.
- **JMP blocks served:** welfare (money-metric EV/CV from discrete choice), identification (preference heterogeneity of unspecified dimension), estimation (the parametric MNL welfare integrator as a special case), motivation/defence (the "your decomposition is mechanical / driven by functional form" referee). It does **not** serve the opportunity-mechanism, decomposition, or normative-interpretation blocks directly. [analogy, on relevance]

---

## 1. One-paragraph relevance to my JMP

This is the canonical statement that money-metric welfare for discrete choice â€” the marginal distributions of equivalent variation (EV) and compensating variation (CV) under a price change â€” is point-identified as a closed-form functional of conditional choice probabilities, under arbitrary, unspecified-dimension preference heterogeneity and without specifying the utility functional form. [explicit, pp. 617â€“618] For my JMP it speaks almost entirely to the **preference** channel and to the welfare-object construction: it is the cleanest reference for the claim that my equivalent-income objects are *preference-respecting* and need not identify the full heterogeneity distribution to be well-defined, and it is my strongest defence against the referee who suspects my welfare numbers are artefacts of the Boxâ€“Cox functional form. Its negative result for ordered choice (and the link to Hausmanâ€“Newey set-identification for continuous choice) is the analytic backdrop for why a *discrete* unordered job menu with alternative-specific budgets is a favourable setting for welfare measurement. [explicit, pp. 617â€“618, 634] It says nothing about an opportunity mechanism, heterogeneous feasible sets, or a three-way decomposition; on those it is silent and must not be over-read.

---

## 2. Data and setting

**None.** The paper is purely theoretical/methodological; there is no empirical dataset, sample unit, or country. [explicit â€” the introduction frames the microdata setting abstractly (p. 617) and Â§2 onward is formal; the only computation is a worked multinomial-logit integrator (pp. 632â€“633)] The "setting" is an individual with observed income $Y$ and observed prices $P$ choosing a discrete good, with covariates suppressed for notational clarity ("the entire analysis should be thought of as implicitly conditioned on these observed covariates"). [explicit, p. 621]

**Transport to my France pooled 2015â€“2017 EUROMOD cross-section.** The *theory* transports: it is a single-cross-section, one-time-choice result and explicitly states this is the setup of all existing empirical welfare-analysis work it is aware of. [explicit, p. 634, "Sequential Choice"] What I do **not** have / what differs:

- The paper's welfare experiment is a **price change** for a good. My JMP has **no price change**: my welfare object is a *level* (an ex-ante equivalent income against a reference state), not a CV/EV for a counterfactual price movement. This is the single most important mapping caveat â€” see Â§6. [analogy]
- The paper requires **own-price and income variation** across observed units to trace the welfare CDF nonparametrically. [explicit, p. 631, "Computational Issues"] My budget variation comes from the EUROMOD tax-benefit map across alternatives, not from exogenous price variation; I do not attempt nonparametric identification.
- The paper assumes a **common, universal choice set** (same menu for every consumer). [explicit â€” Â§2.2 sets up a fixed alternative set $\{0,1,\dots,J\}$ common to all, p. 629] My JMP's defining feature is *heterogeneous feasible sets*; the paper has no analogue.
- No panel, no administrative match, no external instrument, no vacancy/offer data appears or is required (consistent with my own data constraints; the paper simply does not need them for its identification result). [explicit]

---

## 3. Model and objects (map object-by-object to mine)

| Their object | Their definition (source) | My object | Match? |
|---|---|---|---|
| Choice set $\{0,1,\dots,J\}$, alternative-specific prices $p_j$ | Mutually exclusive discrete alternatives, common to all consumers (p. 629) | latent-jobs set $\mathcal C_i$ | **Partial.** Both are unordered discrete menus; theirs is universal/common, mine is household-specific and feasibility-constrained. [analogy] |
| Deterministic-plus-heterogeneity utility $U_j(Y-p_j,\eta)$ | Continuous, strictly increasing in numeraire; $\eta$ of unknown dimension/distribution, arbitrary entry (Assumption 1, p. 622; Assumption 2, p. 630) | preference utility $v$ (Boxâ€“Cox in $c,\ell$, taste-shifters) | **Object-analogous, assumptions much weaker.** Theirs imposes only monotonicity+continuity in the numeraire; mine is a parametric Boxâ€“Cox. [explicit for theirs; analogy for the map] |
| Budget: $W + PQ = Y$, consumption $= Y - p_j$ | Numeraire after discrete purchase (p. 621) | EUROMOD disposable income $c_j = $ `ils_dispy_real` at alternative $j$ | **Analogous role, different map.** Theirs is linear price-subtraction; mine is the nonlinear tax-benefit transform. [analogy] |
| Opportunity / availability mechanism | **None.** Universal choice set; all welfare variation is preference heterogeneity. (p. 632, summary; Â§2.2 setup) | opportunity density $g$ (hours / wage-ability / market / occupation-access) | **No analogue in the source.** [explicit â€” the paper has no $g$] |

**Separation of hours / wage(ability) / market / occupation channels:** absent. The paper has no opportunity mechanism, hence no channel split. [explicit]

**Does any attribute enter BOTH utility and an opportunity mechanism?** Not applicable â€” there is no opportunity mechanism, so the double-entry hazard I track does not arise here. The paper's only "all else" object is the heterogeneity vector $\eta$ inside utility. [explicit]

**Key structural difference to flag for my draft:** the paper's welfare object is generated by *price variation on a fixed menu*; mine is generated by *menu variation across households at fixed policy*. The identification logic (slice the population by reservation price; sweep prices to trace the CDF) does not port to my setting, where I am not perturbing a price. [analogy]

---

## 4. Estimation method

The paper is **about identification, not estimation**; a full inference treatment is deferred to a companion (Bhattacharya and Lee 2014, unpublished at the time). [explicit, pp. 632â€“633, "Inference"]

- **Likelihood / estimator:** none for the main results. The identification result expresses welfare CDFs as functionals of the structural choice probability $\bar q(\cdot,\cdot)$ (the "average structural function" in the sense of Blundellâ€“Powell 2003). [explicit, p. 622] $\bar q$ is to be recovered by nonparametric regression of the buy indicator on price and income when these are independent of $\eta$ given covariates, or via control functions under endogeneity. [explicit, p. 622]
- **Choice-set construction:** fixed, common, finite menu; **no sampling of alternatives, no proposal density.** [explicit â€” Â§2.2]
- **Proposal / prior correction:** **none.** There is no sampling-of-alternatives step, so no $\log\pi$ correction exists or is needed. [explicit] (See Â§4b.)
- **Normalisation / scale:** in the parametric MNL example, utilities $U_j(a,\eta)=\beta_j a + \varepsilon_j$ with i.i.d. extreme-value $\varepsilon$ independent of price and income; the $\beta$'s are estimable by ML. [explicit, p. 632, eq. (23)] No explicit scale-normalisation discussion beyond the standard logit form.
- **Numerical method:** for the parametric case, the mean-welfare integral over the price interval is computed by averaging the estimated integrand over a uniform grid $r_k = p_{10} + \frac{k}{K+1}(p_{11}-p_{10})$. [explicit, pp. 632â€“633, eq. after (24)]
- **What pins preferences vs the opportunity mechanism:** not applicable â€” there is no opportunity mechanism to separate from preferences. The paper's separation problem is instead "welfare distribution vs heterogeneity distribution," and its result is that the former does not require the latter. [explicit, Remark 1 p. 627; Appendix example pp. 646â€“647]

**Verdict (reusable for my RURO/JAX pipeline?):** **No for the estimator** (there is none), **Yes for one downstream step** â€” the parametric MNL welfare integrator (eqs. 23â€“24, p. 632) is the textbook template for integrating a closed-form choice-probability expression over a price/parameter grid, and my analytic-in-shocks log-sum welfare core is a relative of it. But I do **not** reuse its nonparametric identification machinery, because I do not perturb a price and I do estimate a parametric structure. [analogy]

## 4b. Proposal / sampling-of-alternatives correction

**Not present.** The paper uses a fixed, common, fully enumerated choice set; there is no sampling of alternatives, no proposal density $\pi$, no individualised draw, and therefore no McFadden-style correction and no per-alternative $\log\text{prior}$. [explicit â€” confirmed by the absence of any sampling step in Â§Â§2.1â€“2.2 and by the direct enumeration in the MNL example, eq. (23)]

**Relation to my importance-sampling welfare integrator and proposal-individualisation concern:** the paper offers **no** guidance on the $-\log\pi$ correction, on partly-individualised proposals, or on effective-sample-size diagnostics, because it never samples alternatives. My proposal-correction obligations and my ESS finding are entirely outside this paper's scope; it should not be cited on them. [explicit absence â†’ not-established for my purposes]

---

## 5. Opportunity mechanism  [MOST IMPORTANT]

**There is no explicit opportunity mechanism.** The choice set is a fixed, universal menu identical for every consumer; feasibility, offer probabilities, reservation-wage/participation restrictions, and circumstance-varying availability are **not modelled**. All cross-individual variation in welfare arises from preference heterogeneity $\eta$, with prices and income observed and (conditionally) independent of $\eta$. [explicit â€” Â§2 setup; summary p. 632]

Mapping to my three sub-objects:

- **access** (hours / market-participation / region / year / occupation offers): **absent.** [explicit]
- **ability** (wage technology; returns to education/experience; residual dispersion): **absent.** [explicit]
- **occupation as availability vs something else:** not present; no occupation object, hence **no sector/industry conflation risk** to flag. [explicit]

**Functional form of the mechanism:** N/A.

**Cost of this omission for my access/ability/preference decomposition.** Because the paper holds the feasible set fixed and common, it cannot â€” even in principle â€” separate access or ability from preference; everything it calls "heterogeneity" lives inside utility ($\eta$) and is, in my taxonomy, **preference** (with the important caveat that the paper's $\eta$ is *unrestricted* and could in a richer reading absorb what I would call ability/access if those were folded into utility). The paper is therefore a model of the *limiting case my JMP argues against*: the universal-choice-set world in which opportunity differences are invisible and would be loaded entirely onto tastes. This makes it useful **as the foil** for sub-question 1 ("do models without constrained opportunities overstate preference heterogeneity?") â€” Bhattacharya formalises welfare in exactly the world where that overstatement is unavoidable because no opportunity object exists. [analogy â€” the paper does not itself make this framing; it is my use of it]

---

## 6. Welfare object â€” and its place on my $W^1$â€“$W^6$ map

**Does it compute welfare?** Yes. The objects are the **marginal distributions of EV and CV** (and their means) for a discrete *price change* $p_0 \to p_1$. [explicit, Theorems 1â€“2, pp. 626, 631]

- **Money-metric?** Yes â€” EV and CV are income-compensation measures (units of the numeraire). [explicit, p. 617]
- **Equivalent income / equivalent variation?** It is **Hicksian** EV/CV for a price change, *not* an equivalent-income level against a reference state. [explicit] This differs from my object, which is an equivalent-income *level* against a normative reference set. [analogy]
- **Compensating / equivalent variation?** Both, defined as the income $S$ solving the indifference equations (5)â€“(6) for binary choice and (15)â€“(16)/(17)â€“(18) for multinomial. [explicit, pp. 624â€“625, 630]
- **Universal vs constrained feasible set?** **Universal** common set. [explicit] My welfare object is over a **constrained, household-specific** set. This is a fundamental mismatch. [analogy]
- **Reference price / preference / bundle / set:** the reference is the *post-change* (or pre-change) price situation under the consumer's **own** preferences; there is no reference-preference swap and no reference *set* â€” the menu is fixed. [explicit]
- **Discrete-choice subtleties:** handled via the composite-outside-option reduction â€” multinomial welfare for a price change in alternative 1 is reduced to a binary problem against $U^*(p_{-1},y,\eta)=\max\{U_0,U_2,\dots,U_J\}$, then Theorem 1 is applied (Theorem 2, Assumption 2). [explicit, pp. 629â€“631] Marshallian vs Hicksian: average EV equals the change in average Marshallian consumer surplus *even without quasilinearity*; average CV $\ge$ average EV for a normal good. [explicit, Corollary 1 and implications, p. 628] Integration over unobserved heterogeneity is the population integral $\int \cdot\, dF(\eta)$, and crucially does **not** require $F$ to be known or identified. [explicit, Remark 1, p. 627]
- **Ex-ante vs ex-post:** the welfare object is **per-type then aggregated** â€” for each $\eta$ the individual EV/CV is a deterministic number (Lemmas 1â€“2), and the paper reports the *marginal distribution* of that number across $\eta$. [explicit, pp. 625â€“626] There is **no inclusive-value / expected-maximum (log-sum) welfare core** in the main results: the extreme-value shocks appear only in the parametric MNL *example* (eqs. 23â€“24), not in the identification theorems. This is the opposite of my **ex-ante log-sum** stance. [explicit; contrast is analogy]

**Locating the paper on my $W^1$â€“$W^6$ family map.** The paper does **not** contain, reference, or correspond to my $W^1$â€“$W^6$ family, and contains no Ind-$y$ / Ind-$A$ classification. [explicit absence â†’ **the source does NOT contain $W^1$â€“$W^6$**] Any correspondence is by analogy only: Bhattacharya's EV/CV use the consumer's *own* preferences and the *own* (universal) menu, so in spirit they sit at the **Full-Responsibility / own-everything** corner that my $W^2$/$W^3$ occupy â€” the consumer is evaluated against her own choice situation with no compensation of pay or set. But this is a loose analogy: his object is a *change* measure (a difference induced by a price move), not a *level* against a reference, so it is not literally any of my six. [analogy â€” explicitly flagged as not-established in the source]

**Verdict:** **Adaptable in spirit, not directly usable.** Usable as authority for "preference-respecting money-metric welfare is well-defined and computable without identifying the heterogeneity distribution." Not usable as a template for my ex-ante, reference-level, constrained-set equivalent income. [analogy]

## 6b. Inclusive value and money-metric inversion

- **Inclusive value (log-sum / expected maximum) as welfare core?** **No.** The identification results do not use a log-sum welfare core; welfare per type is obtained from the utility-indifference equations directly, then aggregated to a distribution. [explicit] The extreme-value structure enters only in the parametric MNL worked example (eq. 23), and even there the welfare *integral* is over the price grid, not an expected-maximum over shocks reported as the welfare number. [explicit, eqs. 23â€“24]
- **Money-metric by inversion of an own-utility map?** **Yes, conceptually, at the individual level.** The switcher's EV/CV is literally an inverse-utility solve: e.g. $S^{EV}=y-p_0-U_1^{-1}(U_0(y,\eta),\eta)$ for the switching type (Lemma 1, case ii), and the CV switcher solve $S^{CV}=U_0^{-1}(U_1(y-p_0,\eta),\eta)-y$ (Lemma 2, case ii). [explicit, p. 625] This one-dimensional inversion of an own-utility map is the **same kind of operation** as my bracketing root-solve of the own-utility map for $W^k$. [analogy] The difference: the paper inverts to recover a *price-change compensation*, then aggregates the closed form into choice probabilities; I invert to recover a *level* against a reference and integrate the shocks analytically via the log-sum.
- **Expectation over shocks analytic vs simulated?** In the nonparametric results there are no parametric shocks; the population integral over $\eta$ is collapsed analytically into choice probabilities $\bar q$ (no simulation). [explicit] In the MNL example the choice probability is the closed-form logit (analytic in the EV1 shocks), and only the price-grid integral is done numerically. [explicit, eqs. 23â€“24] This is **consistent in flavour** with my analytic-in-shocks importance-sampling inversion, and is a fair citation for "the expectation over the extreme-value shocks can be taken in closed form." [analogy]

---

## 7. Inequality / decomposition content

- **Inequality index:** **none.** The paper produces *welfare distributions* (CDFs of EV/CV) and their means, but applies **no** inequality index (no Gini, MLD, Theil, variance of logs, Atkinson). [explicit]
- **Decomposition rule:** **none.** There is no Shapley, Shorrocks, factor-component, subgroup, RIF, or regression decomposition. [explicit]
- **Counterfactual construction:** the only counterfactual is a *price change* $p_0\to p_1$; nothing is "equalised," "neutralised," or "zeroed out" across individuals in a decomposition sense. [explicit]
- **Order/path-independence/exhaustiveness:** N/A (no decomposition).

**Verdict (reusable for my three-way access/ability/preference Shapleyâ€“Shorrocks split?):** **No.** The paper supplies the *welfare distribution* that a decomposition would operate on, but contributes no decomposition machinery and is neither two-way nor three-way. To reach my three-channel split one would have to (i) replace the price-change CV/EV with my ex-ante reference-level equivalent income, (ii) introduce the opportunity object the paper lacks, and (iii) add the Shapleyâ€“Shorrocks counterfactual layer entirely from elsewhere (Shorrocks 2013 etc.). The paper is upstream of, and orthogonal to, the decomposition. [analogy]

---

## 8. Identification and the separation of preferences from opportunities  [STRICT]

**What the paper identifies and how.** The marginal distributions of EV/CV are point-identified as closed-form functionals of the conditional choice probabilities $\bar q(p,y)$ under a *single substantive assumption*: utilities are continuous and strictly increasing in the numeraire (Assumption 1 / Assumption 2). [explicit, pp. 622, 630] The identifying source is **own-price and income variation** that sweeps the population's reservation-price boundary: $\Pr\{S^{EV}\le a\}=1-\bar q(p_0+a,y)$ exploits that the fraction not buying at price $p_0+a$ is exactly the fraction with reservation price below $p_0+a$. [explicit, Theorem 1 + "Some Intuition," p. 626]

**Preferences vs opportunities:** the paper does **not** separate preferences from opportunities, because it has no opportunity object. What it *does* establish â€” and this is the load-bearing import for my identification note â€” is a different, stronger separation: **welfare distributions are identified without identifying the preference-heterogeneity distribution, or even its dimension.** [explicit, Remark 1 p. 627; Appendix worked example pp. 646â€“647, where two different $\eta_1$ distributions (uniform vs degenerate) produce identical choice probabilities and hence identical, point-identified welfare distributions, yet the dimension of $\eta$ is itself unidentified.]

**Ability vs access within the opportunity side:** N/A â€” no opportunity side. [explicit]

**Transport to my France pooled cross-section (no panel, no external instrument):** The reassuring transportable lesson is that **I do not need to identify my full heterogeneity distribution to have a well-defined, preference-respecting money-metric welfare object** â€” a direct shield for the "your welfare numbers are a functional-form artefact" referee. [analogy, grounded in explicit Remark 1 / Appendix] The non-transportable part: Bhattacharya's *nonparametric* identification needs continuous own-price variation that I do not have and do not invoke; my identification of the *structural* opportunity/preference split rests instead on parametric functional-form restrictions and is **certified by synthetic recovery, not in-sample fit** (per project state Â§3.7, Â§8). The honest statement for my draft is: Bhattacharya licenses the welfare-*object* well-definedness under unrestricted heterogeneity; it does **not** license my *structural separation* of access/ability/preference, which is a parametric identification claim the paper neither makes nor supports. [analogy]

**On the "mechanical decomposition" referee, with a caution.** The paper's Remark 3 (pp. 638â€“639) is a double-edged sword I must cite carefully: it shows that for *ordered* choice a parametric model would *appear* to point-identify the welfare distribution, but that this apparent identification is "driven entirely by functional form assumptions" and is "artificial." [explicit, p. 639] This is exactly the charge a referee could level at my parametric RURO decomposition. I can cite Bhattacharya to show I am *aware* of the functional-form-identification hazard and to motivate my synthetic-recovery certification as the answer; I must **not** cite him as having *cleared* parametric structural models of the charge â€” he does the opposite for the ordered case. [analogy â€” strict]

---

## 9. Key results and magnitudes

No empirical magnitudes (no data). The substantive results are analytic:

- **Theorem 1 (binary):** for a price rise $p_0\to p_1$, $\Pr\{S^{EV}\le a\}=1-\bar q(p_0+a,y)$ and $\Pr\{S^{CV}\le a\}=1-\bar q(p_0+a,y+a)$ on $[0,p_1-p_0]$. [explicit, p. 626]
- **Corollary 1:** $\mu^{EV}(y,p_0,p_1)=\int_{p_0}^{p_1}\bar q(p,y)\,dp$ = change in average Marshallian consumer surplus (no quasilinearity needed); $\mu^{CV}=\int_{p_0}^{p_1}\bar q(p,y+p-p_0)\,dp$. [explicit, p. 628]
- **Implications:** for a normal good, $E(S^{EV})\le E(S^{CV})$; deadweight-loss formulas for a per-unit tax follow. [explicit, p. 628]
- **Theorem 2 (unordered multinomial):** same CDF forms with $\bar q_1$ (composite outside option). [explicit, p. 631]
- **Negative result (ordered choice, $\ge 3$ alternatives, uniform unit price):** EV/CV distributions are **not** nonparametrically point-identified; linked to Hausmanâ€“Newey (2014) set-identification for continuous choice as a limiting case. [explicit, Â§3, pp. 634â€“639]
- **Appendix example:** heterogeneity dimension unidentified yet welfare distributions point-identified. [explicit, pp. 646â€“647]

Benchmarking value for my own opportunity-share / welfare-spread plausibility: **none** â€” no shares or spreads are reported. [explicit]

---

## 10. Estimators, theorems, or formal results

For each, statement (near-verbatim in LaTeX), assumptions, technique, reusability verdict.

**Assumption 1.** For each $\eta$, $U_0(a,\eta)$ and $U_1(a,\eta)$ are continuous and strictly increasing in $a$; inverses $U_j^{-1}(b,\eta)$ are uniquely defined. [explicit, p. 622]
*Technique/role:* the sole substantive restriction; guarantees the inverse-utility solves are well-defined. *Reusability:* **yes** â€” my Boxâ€“Cox utility satisfies continuity+monotonicity in consumption, so my one-dimensional inversion inherits the same well-definedness guarantee. [analogy]

**Lemma 1 (EV, three cases).** Under Assumption 1: (i) non-buyers at $p_0$ â†’ $S^{EV}=0$; (ii) switchers â†’ $S^{EV}=y-p_0-U_1^{-1}(U_0(y,\eta),\eta)$; (iii) buyers at both prices â†’ $S^{EV}=p_1-p_0$. [explicit, p. 625]
*Reusability:* the *form* (welfare is a piecewise inverse-utility object) is instructive; not directly portable (price-change object). [analogy]

**Lemma 2 (CV, three cases).** Symmetric, with $S^{CV}=U_0^{-1}(U_1(y-p_0,\eta),\eta)-y$ for the switching case. [explicit, p. 625] Same verdict.

**Theorem 1.** Statement as in Â§9. [explicit, p. 626]
*Technique (3â€“5 bullets):* (a) per-type welfare from Lemmas 1â€“2; (b) the event $\{S\le a\}$ maps to a no-purchase event at a shifted price/income; (c) aggregate over $F(\eta)$, which collapses to $\bar q$; (d) point masses at $0$ and $p_1-p_0$. *Reusability:* **maybe** for the welfare *integrator* idea (express welfare via choice probabilities), **no** for the price-change identification. [analogy]

**Theorem 2.** Multinomial extension via composite outside option $U^*=\max\{U_0,U_2,\dots,U_J\}$ under Assumption 2 (all $U_j$ continuous, strictly increasing). [explicit, pp. 630â€“631]
*Reusability:* the composite-max reduction is a clean device; my log-sum core already aggregates over the whole menu analytically, so I do not need it, but it is a citable precedent for handling the multinomial structure. [analogy]

**Corollary 1.** As in Â§9. [explicit, p. 628] *Reusability:* the Marshallian-surplus equivalence is a teaching point, not used in my pipeline. [analogy]

**Section 3 negative result + Remark 3.** Ordered-choice non-identification; parametric "identification" is functional-form artefact. [explicit, pp. 634â€“639] *Reusability:* **yes, as a cited caution** in my identification section (see Â§8). [analogy]

---

## 11. Robustness and specification sensitivity

The paper is analytic, so "robustness" is about identification boundaries rather than estimation stress-tests:

- **Monotonicity of the CDF:** requires $\bar q(p_0+a,y)$ (EV) and $\bar q(p_0+a,y+a)$ (CV) nonincreasing in $a$; these follow from Assumption 1 and can be imposed or tested after estimating an unrestricted $\bar q$. [explicit, pp. 627â€“628]
- **Endogenous income:** control functions recover $\bar q$; Remark 2 distinguishes the marginal welfare distribution at hypothetical income $y$ (the parameter of interest) from the conditional distribution for the subpopulation with realised income $y'$ (an ATE-vs-ATT analogy). [explicit, pp. 622, 633]
- **Parametric vs nonparametric reporting:** the author advises reporting both parametric (e.g. mixed logit) and nonparametric welfare numbers and examining sensitivity to smoothing. [explicit, p. 633]
- **Out-of-support prices / limited price variation:** if hypothetical prices lie outside the observed range, or $P_1$ varies too little, one must either go parametric or only *bound* mean EV/CV; the conclusions of Theorems 1â€“2 are unaffected, but $\bar q$ at out-of-range points cannot be obtained nonparametrically. [explicit, p. 631]

**What this informs in my work:** (i) the parametric-vs-checked discipline echoes my synthetic-recovery gate; (ii) the "limited variation â†’ only bounds" point is a useful analogue to my effective-sample-size concern (thin coverage â†’ degraded identification of the integrand), though the mechanism differs (their thinness is in observed price support; mine is in importance-sampling node coverage). [analogy] The paper does **not** vary choice-set size, number of draws/starts, opportunity-set definitions, circumstance partitions, or an ability/access boundary â€” none of those exist here. [explicit absence]

---

## 12. What I can cite this paper for

- That **money-metric welfare (EV/CV) for discrete choice is point-identified from choice probabilities under arbitrary, unspecified-dimension preference heterogeneity**, requiring only monotonicity+continuity of utility in the numeraire. [explicit, pp. 617â€“618, 622, Theorem 1]
- That **the preference-heterogeneity distribution need not be identified â€” nor even its dimension â€” for welfare distributions to be well-defined and point-identified** (Remark 1; Appendix example). [explicit, pp. 627, 646â€“647] *(This is the key citation for my "welfare object is preference-respecting and robust to not pinning down full heterogeneity" claim.)*
- That **average EV equals the change in average Marshallian consumer surplus even without quasilinear utility**, and average CV $\ge$ EV for a normal good (Corollary 1). [explicit, p. 628]
- That **welfare can be computed directly from choice probabilities without reconstructing expenditure functions / utility primitives**, including under a parametric MNL approximation (eqs. 23â€“24). [explicit, pp. 632, 640]
- As **methodological precedent and caution** that parametric welfare calculations can rest on functional-form-driven identification (Remark 3 / ordered-choice result) â€” used to motivate my synthetic-recovery certification. [explicit, pp. 638â€“640]
- For the **EV/CVâ€“asâ€“inverse-utility-solve** construction (Lemmas 1â€“2), as a relative of my own bracketing inversion. [explicit, p. 625]

---

## 13. What I should NOT cite this paper for  [overclaim risks]

- **Not** for any opportunity / access / ability mechanism, heterogeneous feasible sets, or rationing â€” the paper has a **universal common choice set** and no opportunity object. [explicit absence]
- **Not** for a **two-way or three-way decomposition** of welfare inequality â€” it has **no decomposition and no inequality index** at all. Do not present it as opportunity-vs-preference or access/ability/preference. [explicit absence]
- **Not** for an **ex-ante / inclusive-value (log-sum) welfare core** â€” its welfare object is a per-type price-change EV/CV aggregated to a distribution; the log-sum appears only in a parametric example, not as the welfare number. Do not read my ex-ante stance into it. [explicit]
- **Not** as containing or endorsing my **$W^1$â€“$W^6$ family** or any **Ind-$y$ / Ind-$A$** classification â€” it does not. The loose "Full-Responsibility corner" analogy is mine, not the source's; flag it as such. [**source does NOT contain $W^1$â€“$W^6$**]
- **Not** for a **reference-level equivalent income** â€” its object is a *price-change* compensation, not a level against a normative reference state/preference/set. [explicit]
- **Not** for **occupation/industry** anything; no occupation, no sector, no NACE/ISCO content. No `loc4`/`lindi` mapping. [explicit absence]
- **Not** for a **random-opportunity** reading â€” the paper has deterministic, common menus and stochastic *preferences*; its randomness is in $\eta$, not in opportunities. Consistent with my deterministic-opportunities stance, but do not cite it as evidence about opportunities at all. [explicit]
- **Not** to clear parametric structural decompositions of the "mechanical / functional-form" charge â€” Remark 3 cuts the other way for ordered choice. [explicit, p. 639]
- **Theory-paper boundary:** this is a welfare-*measurement* econometrics paper; it has nothing to do with the Haydarâ€“Maniquet axiomatic characterisation, and must never be enrolled to support axioms, characterisations, or proofs, nor read as a theory contribution of my JMP. [boundary]

---

## 14. Direct quotes worth citing

(Short, exact, with page numbers. Use sparingly.)

1. "the marginal distributions of EV and CV can be expressed as simple closed-form functionals of conditional choice probabilities" (abstract, p. 617).
2. "These results hold even when the distribution and dimension of unobserved heterogeneity are neither known nor identified" (abstract, p. 617).
3. "average EV for a price rise equals the change in average Marshallian consumer surplus" (abstract, p. 617).
4. "more numeraire is better" (gloss on strict monotonicity, p. 622).
5. "the identification result underlying this calculation is artificial in that it is driven entirely by functional form assumptions" (Remark 3, ordered choice, p. 639).
6. "identifiability of the heterogeneity distribution or even correct specification of its dimension is not a requirement for identifiability of welfare distributions" (Appendix, p. 647).

[All verbatim from the PDF; each under the quote-length limit. Quote 5 must be cited with the Â§8 caution, not as endorsement.]

---

## 15. Open questions and risks for my draft

- **Object mismatch risk.** My equivalent-income *level* against a reference set is not the same object as Bhattacharya's price-change EV/CV. If I cite him as authority for "money-metric welfare from discrete choice," a careful referee will note the object differs (change vs level; universal vs constrained set). I should cite him precisely for the *preference-respecting, heterogeneity-robust* property, not for the object form. [risk]
- **Inference is deferred in the source.** Bhattacharya defers full inference to Bhattacharyaâ€“Lee (2014); I cannot lean on this paper for standard errors on welfare distributions. My cluster-robust bootstrap is my own and is not supported by this paper. [risk â€” verify Bhattacharyaâ€“Lee status if I need an inference citation]
- **The functional-form caution (Remark 3) is a live referee weapon.** It strengthens my motivation for synthetic-recovery certification but also names the exact vulnerability of my parametric RURO; I must address it head-on rather than cite around it. [risk]
- **Nonparametric ideal vs my parametric reality.** The paper's nonparametric ideal needs price variation I lack; positioning must make clear I adopt its *welfare-well-definedness lesson* while operating parametrically with a different identification warrant (recovery, not in-sample fit). [risk]
- **No opportunity object.** The paper cannot speak to the central empirical bet of my JMP (that opportunity differences are large and compensation-relevant); it is upstream infrastructure only. Do not let its prominence crowd the opportunity-mechanism citations (Aabergeâ€“Colombinoâ€“StrÃ¸m, Dagsvik, Aabergeâ€“Colombino) in the positioning. [risk]

---

## 16. TL;DR for retrieval

Bhattacharya (2015, *Econometrica*) point-identifies the marginal distributions of EV/CV from a discrete *price change* as closed-form functionals of conditional choice probabilities, under arbitrary unspecified-dimension **preference** heterogeneity and only monotonicity+continuity of utility in the numeraire â€” the canonical authority that my preference-respecting money-metric welfare object is well-defined without identifying the heterogeneity distribution. It has **no opportunity mechanism, no inequality index, no decomposition, no $W^1$â€“$W^6$ family, and no inclusive-value welfare core**, so it informs only the **preference** channel and the welfare-object's robustness, never access/ability or the three-way split. Its ordered-choice negative result and Remark 3 are a double-edged citation: useful to motivate my synthetic-recovery certification against the functional-form-identification charge, but not a clearance of parametric structural decompositions.
# CapÃ©au & Decoster 2016 â€” Getting tired of work, or re-tiring in absence of decent job opportunities? Some insights from an estimated Random Utility/Random Opportunity model on Belgian data

## 0. Metadata
- **BibTeX key:** CapeauDecoster2016 *(suggested; verify against your `.bib`)*
- **Authors:** Bart CapÃ©au (KU Leuven, Dept. of Economics); AndrÃ© Decoster (KU Leuven, Dept. of Economics).
- **Year:** 2016 (May 2016; subsumes an October 2015 version, CES DPS15.25).
- **Outlet:** EUROMOD Working Paper No. EM4/16, ISER, University of Essex.
- **DOI/URL:** handle `https://hdl.handle.net/10419/197590` (EconStor). No journal DOI in source. [verify]
- **PDF filename:** `CapÃ©au_Decoster_2016_Getting_tired_of_work__or_re-tiring_in_absence_of_decent_job_opportunities.pdf`
- **Tier:** T1A.
- **JMP block(s) served:** opportunity-mechanism (access + ability); estimation; identification; data-infrastructure (EUROMOD/EU-SILC, couples joint unit, importance sampling); motivation. It does **not** serve the welfare or decomposition blocks directly (see Â§6, Â§7) â€” its closest contact with welfare is the counterfactual-utility scatter (Â§9), which is an ex-post utility comparison, not a money-metric.

## 1. One-paragraph relevance to my JMP
This is the closest published cousin of my structural layer: a fully estimated RURO/latent-jobs job-choice model on EU-SILC processed through EUROMOD, with couples as a joint (unitary) decision unit, estimated by importance-sampling of sampled wageâ€“hours alternatives with an explicit prior/proposal correction â€” i.e. the exact estimation machinery of my pipeline. It separates an opportunity side (a job-offer-intensity function, a wage-offer density, and an offered-hours density) from a preference side (Boxâ€“Cox utility over consumption and leisure), which maps onto my **access** (job-offer intensity, region, hours availability) and **ability** (the wage-offer technology: returns to education and potential experience) channels versus my **preference** block. Its central exercise â€” two counterfactual simulations that separately neutralise age heterogeneity in *opportunities* (EO) versus *preferences* (EP) â€” is a non-money-metric, two-way precursor to my three-way access/ability/preference decomposition, and is the most directly transportable identification and counterfactual template I have. It is explicitly **not** a welfare paper and contains no equivalent-income measure and no inequality decomposition.

## 2. Data and setting
- **Country/year:** Belgium, EU-SILC 2007 (single wave).
- **Microsimulation:** EUROMOD version F5.5 used to compute net disposable income for every element of each household's choice set; full take-up of social assistance assumed when eligibility is met.
- **Sample unit:** three sub-samples estimated together â€” single females, single males, and opposite-sex couples (unitary household). Self-employed, early-retired, sick/disabled, students, and (pre)retired are excluded; only persons available for the labour market (aged 16â€“64, employee jobs) are kept; mixed households where only one partner is available, and households with labour-market-age children still co-residing, are dropped.
- **Sample size:** 1,457 couple households, 571 single females, 449 single males. Full EU-SILC 2007 BE is 6,348 households / 15,493 individuals before selection.
- **Key variables:** disposable income `c` (= consumption, static model, from EUROMOD); gross hourly wage; weekly hours; education (low/middle/high); region (Brussels/Flanders/Wallonia, by residence); age; potential experience (age minus 15/19/23 by education level â€” age itself excluded from the wage equation due to collinearity); number/age of children; **external type-specific unemployment rate** by ageÃ—sexÃ—education (Eurostat 2007), used as an opportunity-side exclusion shifter.
- **Transport to my France pooled 2015â€“2017 EUROMOD cross-section:** *Mostly transports.* Same data family (EU-SILC), same microsimulation engine (EUROMOD), same unitary-couple treatment, same income-as-consumption static convention. **Features they have that I should note:** (i) a single wave (no pooling, so no year channel â€” I pool three waves and carry a year shifter in access); (ii) an **external opportunity instrument** (type-specific unemployment rate as an exclusion restriction on the offer-intensity function) â€” my project state records I currently have *no* external instrument, so this is a feature I lack, not one I share. **Features I have that they lack:** an occupation (`loc4`) access channel; an explicit welfare/decomposition layer. **Features neither has:** panel, administrative match, vacancy/offer data.

## 3. Model and objects (object-by-object map)
- **Choice set = my latent-jobs set?** Yes in spirit. Their alternative `z` is either a non-market alternative (`(w,h)=(0,0)`) or a job package `(w,h)` â€” a wageâ€“hours pair â€” drawn from a latent offer process. This is my latent-jobs set; their job package is `(w,h)` only (plus unobserved attributes folded into the random term), whereas my packages additionally carry occupation (`loc4`). **Explicit-in-source.**
- **Deterministic utility = my preference utility `v`?** Yes. Their systematic utility `Î¨(w,h)` (equivalently `V(c,Tâˆ’h)`) is Boxâ€“Cox in consumption and leisure with demographic taste-shifters on the leisure term â€” structurally my Boxâ€“Cox preference block. They additionally carry a *multiplicative* FrÃ©chet random term `Îµ(s(z))` for unobserved job attributes; the log of a standard FrÃ©chet is EV-Type-I, so the model collapses to a logit-type choice probability (the FrÃ©chet/multiplicative form is their route to the same closed form I get additively in EV-I). **Explicit-in-source.**
- **Opportunity / availability mechanism analogous to my `g`?** Yes, and it is the paper's core. Modelled as an **inhomogeneous spatial Poisson process** of job-offer arrivals, with intensity factorising into three pieces (their notation): `g2(h)` offered-hours density, `g1(w|h)` (identified as `g1(w)` under an independence assumption) wage-offer density, and `Î»1(v)=Ï€1Â·v^{-2}` the job-offer intensity, with `q(x_q)=Ï€1/Ï€0` the relative intensity of market vs non-market alternatives. **Map to my channels:**
  - their **`g1(w)` wage-offer density** â†” my **ability** sub-block (wage technology; returns to education and potential experience; dispersion `Ïƒ`);
  - their **`g2(h)` offered-hours density** â†” my **access** (hours-availability) channel;
  - their **`q(x_q)` job-offer intensity** (region, education, age, unemployment rate) â†” my **access** (market/participation availability + region) channel.
- **Budget map = my EUROMOD disposable income?** Yes â€” `c=f(w,h;x_f)` is the EUROMOD gross-to-net map; identical convention to my `ils_dispy`-based consumption. **Explicit-in-source.**
- **Does any job attribute enter BOTH utility and the opportunity mechanism?** **No double-entry of an observed structural object**, and this is favourable for my design. Wage `w` and hours `h` enter utility `Î¨(w,h)` and *also* index the offer densities `g1`, `g2` â€” but the *covariates* are kept separate (Table 3): preferences `x_V` use region, education, age, children, gender; offer intensity `x_q` uses region, education, age, gender, **and the unemployment rate** (excluded from preferences by assumption); the wage density `x_g1` uses education, gender, potential experience; the hours density `x_g2` uses gender only. So education and region appear in *both* the preference and the opportunity covariate vectors â€” they justify this on identification grounds (observationally-equivalent-group argument, Â§8) and on a functional-form normalisation, **not** by adding the same attribute as a free regressor to two utility-relevant places. **This is the well-behaved pattern my contract enforces** (occupation in opportunity only); their education/region overlap is a circumstance shifter common to taste and offer, identified by within-group hours/wage variation, not a free taste+offer double load.

## 4. Estimation method
- **Likelihood/estimator:** simulated maximum likelihood on a sampled choice set. Per-alternative contribution (singles, their eq. 19): `Î¨(w,h)Â·q(x_q)Â·g1(w)Â·g2(h)` in the numerator over a denominator summing the non-market term `Î¨(0,0)` plus the integral/sum of market terms; the couples likelihood (their eq. 19â€³) is the joint four-outcome form over `(w1,h1,w2,h2)` with partner-specific `q^j, g1^j, g2^j`. **Explicit-in-source.**
- **Choice-set construction:** sampled alternatives, **not** a fixed grid. Alternatives `(w,h)` are drawn from a prior `P(w,h;x_P)`; the observed choice is always included. **Importance sampling with replacement**, with the number of non-market draws treated as random (expected `Ï€0^obsÂ·(ns+1)`). **Explicit-in-source.** Grid size `ns` per observation is described in Appendix II but the exact production `ns` is **not stated numerically in the excerpt** [verify].
- **Proposal/sampling density:** wages drawn lognormal with *prior* location `Âµ` and scale `Ï‚`; hours uniform on `[Hmin,Hmax)`; non-market with fixed prior probability `Ï€0^obs`. Reported priors: males `Ï€0^obs=.104, Âµ=2.71, Ï‚=.308`; females `.246, 2.63, .297`. **Explicit-in-source** (footnote 23).
- **Prior/proposal correction â€” is `log(prior)` subtracted?** **Yes, equivalently.** Their corrected sampled likelihood (their eqs. 27, a.14, a.17) divides each alternative's term by its sampling density `P(w,h;x_P)` (equivalently `/Ï†(j)`), i.e. importance-sampling reweighting. This is the multiplicative analogue of my additive `âˆ’log Ï€(j)` correction; subtracting `log Ï€` inside `exp(Â·)` â‰¡ dividing by `Ï€` outside. **Always well defined?** Yes â€” they require the **positive conditioning property** (`Ï€(D|j;C)>0 â‡’ Ï€(D|k;C)>0`) which their importance scheme satisfies; the non-market alternative carries strictly positive prior `Ï€0^obs`, so no zero-division. **Explicit-in-source** (Appendix II).
- **Normalisation/scale:** FrÃ©chet shape `Î±=1` throughout (so the EV-I scale is fixed); `Î¨(0,0)` is normalised because `Î¨` is a utility (lets them identify `q`); `Ï€0+Ï€1â‰¡1` normalisation on the fixed-capacity-stock interpretation; the offer-intensity constant `exp(Î·_{q,0})` and the hours-baseline `Î³1` are **not separately identified** and `Î³1` is pinned by the density-integration constraint (their eq. 28). **Explicit-in-source.**
- **Numerical method / starting values / multistart:** the optimiser, gradient method, and any multistart are **not described in the excerpt** [verify]. (Acknowledgement thanks T. Wennemo for the estimation program â€” Statistics Norway lineage.)
- **What pins preferences apart from the opportunity mechanism:** see Â§8.
- **Verdict â€” reusable for my RURO/JAX pipeline?** **Yes, as the canonical reference for: (a) the importance-sampling-with-replacement choice-set construction and its correction (Appendix II is a clean, citable derivation linking McFadden-1978 to Aabergeâ€“Colombinoâ€“Wennemo-2009 â€” directly supports my `âˆ’log Ï€` step); (b) the factorised offer intensity `qÂ·g1Â·g2` as the template for my access/ability split.** Not reusable as-is for: the FrÃ©chet/Poisson derivation route (I use an additive EV-I/log-sum form analytically; theirs is multiplicative-FrÃ©chet â€” same closed form, different bookkeeping) and the welfare layer (absent).

## 4b. Proposal / sampling-of-alternatives correction  [extracted]
- **How sampled and corrected:** importance sampling with replacement; observed choice force-included; each drawn alternative reweighted by `1/Ï†(j)` (their `1/P(w,h;x_P)`). Couples: independent per-partner draws, joint prior `F(w1,h1,w2,h2)=P1Â·P2` (their eq. a.22); the joint sampling probability `Î (Dc)` is the product form in eq. a.23. **Explicit-in-source.**
- **Partly individualised or common?** **Partly individualised** â€” but *less* individualised than my proposal. The *prior* `P(w,h;x_P)` they actually use is **common within sex** (sex-specific `Ï€0^obs, Âµ, Ï‚` for the wage prior; common uniform hours prior), i.e. individualised only by gender, not by education/region/occupation. My proposal individualises the wage mean by `X_i b + Î´_occ[loc4_i]` and occupation by genderÃ—education stratum â€” **more** individualisation than theirs. Their *estimated* offer densities `g1(w;x_g1)`, `q(x_q)` do condition on education/region/age, but those enter the structural `g`, not the sampling prior. **This distinction matters for my proposal-individualisation audit:** CapÃ©auâ€“Decoster individualise the structural offer density richly but the *sampling instrument* only by sex â€” the mirror of my design choice, and a useful contrast point.
- **McFadden-style?** Yes â€” Appendix II derives their correction as the RURO instance of McFadden (1978) sampling-of-alternatives, via Ben-Akivaâ€“Lerman (1985) and Aabergeâ€“Colombinoâ€“Wennemo (2009). **Explicit-in-source.**
- **Each drawn alternative carries its own log-prior?** Yes (the `1/Ï†(j)` weight is per-alternative). **Explicit-in-source.**

## 5. Opportunity mechanism  [MOST IMPORTANT â€” split by channel]
The feasibility of jobs is a **density over latent alternatives**, generated by an inhomogeneous spatial Poisson process; not offer probabilities per se, not a reservation-wage rule. Three multiplicatively-separable pieces:

- **ACCESS â€” job-offer intensity `q(x_q)=Ï€1/Ï€0`.** `ln q(x_q)=Î·_q' x_q`, linear in covariates: **region** (Brussels/Wallonia vs Flanders reference), **education** (low/middle/high), **age** (entered as `ln(age)` and `ln(age)Â²`), **gender**, and the **type-specific unemployment rate** (the exclusion shifter). `Ï€1` is interpreted as the share of an individual's fixed capacity stock that is currently demanded on the job market (range `(0,1)`), with `Ï€0+Ï€1â‰¡1`. Headline access findings: offer intensity is inverse-U in age, peaking â‰ˆ30 and falling sharply after ~50; markedly lower in Brussels and Wallonia than Flanders; small/imprecise education effects (see Â§9). **This is my access channel** (region + market/participation availability), with the addition of an external local-labour-market shifter I do not currently have.
- **ACCESS â€” offered-hours density `g2(h)`.** Piecewise-uniform with peaks at half-time (18.5â€“20.5h), three-quarter-time (29.5â€“30.5h), and full-time (37.5â€“40.5h); `Hmin=1`, `Hmax=70`; only covariate is **sex**. Females receive relatively more part-time and fewer full-time offers. **This is my hours-availability access channel.** Note their explicit caveat (Â§8, fn 26) that `Î¨` and `g2(h)` are **not separately non-parametrically identified** â€” directly relevant to my hours-availability identification.
- **ABILITY â€” wage-offer density `g1(w)`.** Lognormal: `ln w ~ N(Î´_g1' x_g1, ÏƒÂ²)` with `x_g1 =` education + potential experience (+ experienceÂ², gender). A higher education level shifts the offer distribution right; experience raises mean offers (turning slightly negative past ~35â€“39 years, absorbing an age effect). `Ïƒâ‰ˆ0.266` (M) / `0.263` (F). **This is exactly my ability sub-block** (returns to education and experience plus residual dispersion `Ïƒ`) â€” the single tightest object-level correspondence in the paper. They emphasise these wage-offer estimates are "very precise and robust to different specifications."
- **Occupation?** **Absent.** There is **no occupation/`loc4` access object** and no industry/sector object in this model; jobs are `(w,h)` packages only, with all other attributes absorbed into the unobserved multiplicative term. **No sector/industry conflation occurs â€” because neither is present.** (Do not cite this paper for an occupation-as-access treatment; that is my addition.)
- **Functional form summary:** offer intensity `Î»1(v)=Ï€1Â·v^{-2}`; `Î»0(Îµ)=Ï€0Â·Îµ^{-2}` for non-market; both generate FrÃ©chet (`Âµ=0, Î±=1`) maxima, yielding the logit-type choice probabilities. **Explicit-in-source.**
- **Does availability vary with circumstances?** Yes â€” region, education, age, sex, and the local unemployment rate (and, for hours, sex). **Explicit-in-source.**

## 6. Welfare object â€” and its place on my WÂ¹â€“Wâ¶ map
- **Does the paper compute welfare?** **No money-metric welfare object is computed.** There is **no** equivalent income, **no** compensating/equivalent variation, **no** money-metric of any kind, and **no inclusive-value welfare aggregate reported as welfare.** The only utility object used downstream is the **ex-post utility of the simulated chosen alternative** (`ln Î¨(w*,h*) + Îµ(w*,h*)`), plotted baseline-vs-EO-counterfactual in Figures 13â€“15. **Explicit-in-source.**
- **Universal or constrained-feasible set?** The simulated choice (hence the plotted utility) is over a *drawn* feasible set under estimated offer intensities â€” constrained â€” but it is **ex post** (the realised argmax), not the ex-ante inclusive value I use.
- **Reference price/preference/bundle/set?** None â€” no reference construction exists because there is no equivalent-income inversion.
- **Discrete-choice subtleties:** they take the **ex-post realised-job utility**, not the log-sum expected maximum; no Hicksian/Marshallian welfare object; integration over unobserved heterogeneity is via the simulation draws of `Îµ`. **ex-ante vs ex-post: strictly ex-post for the utility comparison.** This is precisely the object my spec relegates to a *diagnostic cross-check* and rejects as the baseline because it "cannot carry the access channel."
- **Location on my WÂ¹â€“Wâ¶ family:** **Not located â€” the paper contains no member of the family.** It does **not** contain WÂ¹â€“Wâ¶, does not contain any Ind-y/Ind-A construction, and must not be cited as if it did. The conceptual contact is only that their EO counterfactual (equalise opportunity) is a behavioural-utility analogue of the *idea* behind an access-compensating exercise â€” but realised as ex-post utility change, not as a money metric and not anchored on a responsibility stance.
- **Verdict:** **Incompatible as a welfare source; usable only as the estimation/counterfactual antecedent.** Their own conclusion flags welfare measurement (citing Decosterâ€“Haan 2015) as *future* work â€” confirming welfare is out of this paper's scope.

## 6b. Inclusive value and money-metric inversion  [extracted]
- **Inclusive value as welfare core?** **No.** The log-sum/inclusive value appears implicitly as the choice-probability denominator but is **never used as a welfare object**. **Not-established in source.**
- **Money-metric by inverting an own-utility map?** **No** â€” no inversion, no one-dimensional money solve. **Not-established.**
- **Expectation over shocks analytic or simulated?** For *estimation*, analytic (the FrÃ©chet/Poisson derivation yields closed-form choice probabilities â€” the log-sum is implicit). For *simulation/fit/counterfactuals*, **by simulation** â€” they draw EV-I shocks `Îµ(wr,hr)` and take the simulated argmax (their Â§3.5, eq. 32). This contrasts with my welfare layer, which is **analytic in the shocks** (closed-form expected maximum, no shock draws). **Explicit-in-source.**

## 7. Inequality / decomposition content  [three-way where relevant]
- **Inequality index:** **None.** No Gini/MLD/Theil/Atkinson/variance-of-logs is computed. **Not-established in source.**
- **Decomposition rule:** **No formal decomposition** (no Shapley, no Shorrocks, no factor-component, no RIF). What exists is a **two-counterfactual simulation contrast**: baseline vs "EO" (every individual given the age-30 maximal offer intensity `Ï€1`, partially equalising age heterogeneity in *opportunities*) vs "EP" (every individual given the subgroup-specific flattest-indifference-curve age, equalising age heterogeneity in *preferences*). Differences in participation/hours between counterfactuals and baseline are read off descriptively (Table 9). **Explicit-in-source.**
- **Counterfactual construction:** EO equalises *only the age dimension of the offer-intensity function `Ï€1`* (not wages, not hours availability) to its age-30 maximum; EP equalises *only the age dimension of leisure-preference intensity* to its subgroup minimum. Wage offers, hours offers, and region are **held fixed** in both. Nothing is "zeroed out"; the equalisation is a level reset along one covariate (age). **Explicit-in-source.**
- **Order/path-independence/exhaustiveness:** **Not addressed** â€” because it is not a formal additive decomposition, only two separate counterfactuals. There is no claim that EO and EP effects sum to total observed age heterogeneity. **Not-established.**
- **Verdict â€” reusable for my three-way access/ability/preference Shapleyâ€“Shorrocks split?** **Partially, as a conceptual and counterfactual antecedent, not as a method.** Their EO/EP contrast is a **two-way** (opportunity vs preference) *behavioural* counterfactual along a single covariate (age), with no inequality index and no Shapley exhaustiveness. To reach my three-way decomposition it would have to be extended on three fronts: (i) split their single "opportunity" counterfactual into **access** (`q`, `g2`) and **ability** (`g1` wage offers) sub-equalisations â€” they bundle these as "opportunity"; (ii) replace the descriptive participation/hours read-out with an **inequality index of a money-metric welfare object** (which they do not compute); (iii) impose **Shapley/Shorrocks order-independence and exhaustiveness** over the {access, ability, preference} equalisation set. Cite it for the *legitimacy and economic interpretation* of opportunity-vs-preference counterfactual equalisation in an estimated RURO model; do **not** cite it for a decomposition methodology.

## 8. Identification and the separation of preferences from opportunities  [STRICT]
- **What identifies tastes vs constraints:** a **choice-set/observationally-equivalent-group argument** (their Â§3.2, following Aabergeâ€“Colombinoâ€“StrÃ¸m 1999 and Dagsvikâ€“StrÃ¸m 2004/2006, Dagsvikâ€“Jia 2014). Within a group sharing all conditioning variables: (i) people on the same wage but different hours identify `Î¨(w,h)Â·g2(h)` (their eq. 21); (ii) people on the same hours but different wages then identify `g1(w)`, using that `g1` integrates to 1 (eq. 22); (iii) participants vs non-participants identify `q` given the `Î¨(0,0)` normalisation (eq. 23). **Explicit-in-source.**
- **Ability vs access within the opportunity side?** Their structure separates the **wage-offer technology `g1` (my ability)** from **offer intensity `q` and hours `g2` (my access)** by the two-step within-group argument above â€” so the ability/access boundary *is* identified in their framework by functional-form-plus-within-group-variation. **Derived-by-analogy** to my vocabulary (they do not use "ability/access"), but the underlying separation is **explicit-in-source**.
- **The exact identifying sources, named:**
  1. **Functional-form restrictions:** Boxâ€“Cox preferences (justified non-parametrically via Dagsvikâ€“RÃ¸ine-Hoff 2011, Dagsvik 2013); the `Î»âˆv^{-2}` intensity form (guarantees IIA); lognormal `g1`; piecewise-uniform `g2`. **Explicit.**
  2. **An exclusion restriction / external opportunity shifter:** the **type-specific (ageÃ—sexÃ—education) unemployment rate**, assumed to shift offer intensity `q` but **not** preferences. They state they "tried to improve upon the non-parametric identification of `q`" with this restriction. **Explicit** (Â§3.2, Â§4). *This is the single most important transport caveat for me.*
  3. **Distributional assumptions on unobservables:** FrÃ©chet/EV-I with `Î±=1`. **Explicit.**
- **Honest non-identification admissions (do not soften):** they state plainly that **`Î¨(w,h)` and `g2(h)` are NOT separately non-parametrically identified** (Â§3.2, and fn 26: "if one would like to explain this peak pattern by differences in preferences, we cannot tell this to be wrong on pure empirical grounds"). The hours-offer peaks vs hours-preference are observationally entangled; separation rests on the *functional-form justification* of Boxâ€“Cox preferences, not on the data alone. **Explicit-in-source â€” and a direct warning for my hours-availability access channel.**
- **Transport to my France pooled cross-section:** **Mixed.** The within-group/functional-form identification transports (I use the same Boxâ€“Cox + offer-density architecture and certify by synthetic recovery, which is the parametric-identification route they lean on implicitly). **But their key empirical identifying lever â€” the external unemployment-rate exclusion restriction on `q` â€” I do not currently have** (project state: no external instrument). This is exactly the gap my "region-level continuous covariate merging (unemployment rate Ã— regionÃ—year)" open question is contemplating, and CapÃ©auâ€“Decoster is the precedent for that move. Their reliance is *not* on panel or admin data (they have neither â€” single cross-section), which matches my situation; the burden in both cases falls on functional form + (for them) the external shifter. For me, synthetic recovery substitutes for in-sample identification confidence.
- **Against the "your decomposition is mechanical" referee:** the usable defence from this paper is that the opportunity/preference separation in an estimated RURO model is identified by within-observationally-equivalent-group hours/wage variation plus a functional-form-justified preference family â€” **not** purely mechanical â€” *but* I must concede (as they do) that the hours-offer-vs-hours-preference margin is the weak point, and that they buttress it with an external labour-demand shifter that I would need an analogue of.

## 9. Key results and magnitudes
- **Offer intensity vs age:** inverse-U, peak â‰ˆ30 years, sharp decline after ~50; steeper decline for females. **Regional:** offer intensity (Table 7, age 30, unemployment 6%, middle education) e.g. males Flanders 75.5%, Wallonia 61.8%, Brussels 44.4%; females Flanders 75.0%, Wallonia 64.7%, Brussels 56.2%. Education effects small and imprecise (counter-intuitively, high education lowers male offer intensity, low education raises female offer intensity â€” both with large SEs).
- **Wage offers (Table 5, gross â‚¬/hour):** rise with education and experience; e.g. high-education male 13.08 (10y exp) â†’ 15.74 (25y); male/female gaps small. `Ïƒ_M=0.266`, `Ïƒ_F=0.263`.
- **Aggregate wage elasticities (Table 8):** female total elasticity 0.5034 (couples) / 0.4786 (single); male 0.3104 (couples) / 0.2858 (single); some negative cross-/own- entries for the partner not shifted. They flag these as **larger than typical Marshallian micro estimates** (cf. Keane 2011) and conceptually closer to macro elasticities, partly because the "wage shift" is a shift of the whole offer distribution, not an exogenous wage change.
- **EO vs EP counterfactual (Table 9, the headline finding):** equalising age heterogeneity in **opportunities (EO)** raises the pooled four-group participation rate by **+6.9 ppt** (82.0%â†’88.9%), working **primarily on the extensive margin** (negligible/slightly negative effect on hours-conditional-on-participation). Equalising age heterogeneity in **preferences (EP)** raises participation by only **+2.6 ppt** (82.0%â†’84.6%) but **does move the intensive margin** (+1.9 hours conditional on participation). Subgroup EO participation gains: males-in-couples +3.1 ppt, females-in-couples +8.9 ppt, single males +6.7 ppt, single females +11.6 ppt.
- **Headline qualitative claim:** opportunity decline with age is *at least as important* as rising leisure preference in explaining low elderly participation; opportunities act on the extensive margin, preferences more on the intensive margin.
- **Counterfactual utility (Figs 13â€“15):** EO is **not Pareto-improving** â€” some individuals lose utility because raising market offer intensity mechanically lowers non-market availability (the `Ï€0+Ï€1â‰¡1` fixed-capacity-stock assumption). **A flagged unattractive model property** â€” relevant to how I interpret access-equalisation.
- **Benchmark value for me:** their participation responses are behavioural, not welfare; they give **no opportunity-share or welfare-spread number** I can benchmark my decomposition shares against. The transportable benchmark is qualitative (opportunity â‰ˆ extensive margin; preference â‰ˆ intensive margin) plus the elasticity magnitudes for plausibility-checking my estimated offer densities.

## 10. Estimators, theorems, or formal results
For each, statement (LaTeX), assumptions, technique, reusability verdict.

1. **Singles choice probability (their eq. 19).**
   $$\varphi(w,h)=\frac{q(x_q)\,\Psi(w,h)\,g_1(w)\,g_2(h)}{\Psi(0,0)+q(x_q)\!\int_{\mathcal W}\!\!\int_{\mathcal H}\Psi(s,t)\,g_1(s)\,g_2(t)\,dt\,ds}$$
   *Assumptions:* FrÃ©chet attribute term (`Î±=1`), independent Poisson offer/non-market processes, `g1(w|h)=g1(w)`. *Technique:* ratio of FrÃ©chet scale parameters = probability of being the max (3â€“5 lines: independence â‡’ product of CDFs â‡’ FrÃ©chet-max â‡’ scale ratio). *Reuse:* **yes** â€” this is structurally my per-household choice probability; cite for the closed form linking offer densities to choice probabilities.
2. **Couples joint choice probabilities (their eq. 19â€³, four outcomes; with `A,B,C` integral terms).** *Assumptions:* unitary household; **independent** per-partner offer/non-market processes; joint Boxâ€“Cox utility over `(c, Tâˆ’h1, Tâˆ’h2)` with a leisure-complementarity interaction `Î²_{h1,h2}`. *Technique:* product of partner-specific offer intensities Ã— joint utility, normalised by the four-outcome denominator. *Reuse:* **yes, directly** â€” my couples are a joint unit at 901 alternatives; this is the canonical joint-RURO likelihood and the right citation for the independence-of-partner-processes assumption.
3. **Sampled/importance-corrected likelihood (their eqs. 27, a.10, a.14, a.17, a.21, a.24).**
   $$\tilde\varphi(w,h\mid D)=\frac{\Psi(w,h)\,q\,g_1\,g_2\,\big/\,P(w,h;x_P)}{\frac{\Psi(0,0)}{P(0,0)}+\sum_{(s,t)\in D\setminus\{0\}}\Psi(s,t)\,q\,g_1\,g_2\big/P(s,t;x_P)}$$
   *Assumptions:* positive conditioning property (a.11); observed choice in `D`; importance weights `1/Ï†(j)`. *Technique:* Bayes' law on `Î¸_C(D,j)=Ï€(D|j)Â·P_{j,C}=P_{j,D}Â·Î (D)`. *Reuse:* **yes â€” load-bearing** for my `âˆ’log Ï€` proposal correction; Appendix II is the cleanest citable bridge from McFadden (1978) to Aabergeâ€“Colombinoâ€“Wennemo (2009) for the RURO case.
4. **Offer-intensity normalisation `Î³1` (their eq. 28) and `qÌƒ=Î³1Â·q` reparameterisation (eqs. 29).** *Assumptions:* `g2` integrates to 1 over `[Hmin,Hmax]`; `Ï€0+Ï€1â‰¡1`. *Technique:* density-integration constraint pins `Î³1`; the offer-intensity constant and `Î³1` are not separately identified. *Reuse:* **maybe** â€” useful as a caution on which constants are jointly unidentified in offer-density specifications; my parameterisation differs.
5. **Identification argument (their Â§3.2, eqs. 21â€“23).** Already covered in Â§8. *Reuse:* **yes** â€” the within-observationally-equivalent-group identification narrative is exactly my "what identifies preferences vs opportunities" citation, with the honest `Î¨`/`g2` non-separability caveat retained.

## 11. Robustness and specification sensitivity
- **What they vary / report robust:** the **wage-offer distribution estimates are stated to be very precise and robust to alternative specifications of other model parts** (Â§5.2) â€” a useful precedent that the ability (wage-offer) block is the well-behaved piece, mirroring my finding that the opportunity/wage block is tightly estimated while preferences are wide.
- **What is fragile / breaks:** (i) **`Î¨` vs `g2(h)` non-separability** (Â§3.2, fn 26) â€” the hours-offer-vs-hours-preference margin is not data-identified; (ii) **age effects on preferences are imprecise** for single males and females-in-couples (their own statement: "precision of the estimates for age of females in couples and that of single males is poor"); (iii) **education effects on offer intensity are small with large SEs**; (iv) the **EO counterfactual's non-Pareto property** is a structural sensitivity to the `Ï€0+Ï€1â‰¡1` fixed-capacity assumption.
- **Choice-set size / draws / starts sensitivity:** Appendix II discusses with-vs-without-replacement and fixed-vs-random non-market counts (efficiency trade-offs, citing Lempâ€“Kockelman 2012), but **no empirical sensitivity table over `ns` or number of starts is reported in the excerpt** [verify]. *This is a gap relative to my effective-sample-size concern: they do not report an ESS or draw-count stability check, so I cannot cite them for one.*
- **For my stress-tests:** the transportable lessons are (a) expect the wage/ability block to be robust and the preference/age block to be imprecise; (b) treat the hours-availability vs hours-preference split as the identification weak point requiring an external lever or a functional-form defence; (c) the offer-intensity normalisation is delicate.

## 12. What I can cite this paper for
- An estimated **RURO/latent-jobs job-choice model on EU-SILC via EUROMOD** with couples as a unitary joint decision unit (Belgium 2007). **Explicit.**
- The **factorised opportunity structure** `q(x_q)Â·g1(w)Â·g2(h)` separating offer intensity (access), wage-offer technology (ability), and offered-hours (access). **Explicit.**
- The **importance-sampling-with-replacement choice-set construction and its sampling-of-alternatives correction**, and the formal McFadden-1978 â†” Aabergeâ€“Colombinoâ€“Wennemo-2009 link (Appendix II). **Explicit.**
- The **within-observationally-equivalent-group identification argument** for separating preferences from opportunities, *including* the honest admission that `Î¨` and `g2(h)` are not separately non-parametrically identified. **Explicit.**
- The use of an **external type-specific unemployment rate as an exclusion restriction** on offer intensity â€” the precedent for my contemplated regionÃ—year unemployment-rate merge. **Explicit.**
- The **opportunity-vs-preference counterfactual-equalisation idea** in an estimated RURO model, and the qualitative finding that **opportunity differences act mainly on the extensive margin, preference differences more on the intensive margin** (Belgium, ageing). **Explicit.**
- That **welfare measurement in this RURO tradition was, as of 2016, flagged as future work** (their conclusion, citing Decosterâ€“Haan 2015) â€” useful for positioning my welfare layer as the unfilled extension. **Explicit.**

## 13. What I should NOT cite this paper for  [overclaim risks]
- **NOT** for any **money-metric welfare**, equivalent income, EV/CV, or inclusive-value welfare object â€” the paper computes none. Their downstream utility object is **ex-post realised-job utility**, not my ex-ante inclusive-value money metric. **(ex-post / no-money-metric flag.)**
- **NOT** for any **inequality index or formal decomposition** â€” there is no Gini/Theil/Atkinson and no Shapley/Shorrocks. The EO/EP exercise is two descriptive behavioural counterfactuals, **two-way (opportunity vs preference) and not three-way**, with no exhaustiveness or order-independence. **(two-way-not-three-way flag.)**
- **NOT** for an **occupation-as-access** or any **occupation/`loc4`** treatment â€” occupation is entirely absent; jobs are `(w,h)` only. Do not let their "job attributes" language be read as occupation or sector. **(occupation/sector flag â€” by absence, not conflation.)**
- **NOT** for a **deterministic** opportunity framing â€” their opportunities are genuinely **stochastic** (inhomogeneous Poisson offer arrivals; the literal "Random Opportunity" of RURO). When mapping to my design I treat opportunities as deterministic and the "RO" as estimation machinery; **do not attribute a deterministic-opportunity stance to this paper.** **(random-vs-deterministic flag.)**
- **NOT** for WÂ¹â€“Wâ¶ or any Ind-y/Ind-A construction â€” none present. **Do not claim the source contains the welfare family.**
- **NOT** as the **Haydarâ€“Maniquet theory paper** nor as any axiomatic/characterisation result â€” this is an empirical estimation paper; keep it strictly on the JMP estimation/identification side of the boundary and never read it as supplying the theory paper's axioms or proofs. **(theory-paper boundary flag.)**
- **NOT** for an ESS / draw-count / multistart stability result â€” not reported in the excerpt. **(do not invent a robustness claim.)**

## 14. Direct quotes worth citing
*(Short verbatim, with page numbers from the EconStor PDF pagination shown in the source.)*
1. "we use the estimated model to simulate two counterfactuals" â€” Abstract, p.3. *(verify exact page label)*
2. "opportunities which decline with age are at least as an important factor in explaining low participation rates for the elderly" â€” Abstract, p.3.
3. "The effect of opportunities seems to work primarily through the extensive margin, whereas the effect of preferences is more outspoken in the intensive than in the extensive margin." â€” Abstract, p.3.
4. "the ruro model is the first one that derives these restrictions from an explicit model of a job arrival process" â€” Introduction, p.3 (PDF p.7).
5. "The utility function Î¨(w,h) and the distribution of offered labour time regimes g2(h) are however not separately nonâ€“parametrically identified." â€” Â§3.2, p.18 (PDF p.21).
6. "a group specific unemployment rate is added as an explanatory variable for q. We assume that this variable does not affect individual preferences" â€” Â§3.2, p.18 (PDF p.21).
7. "increasing the intensity of job offers does not imply a Pareto improvement" â€” Â§7, p.50 (PDF p.53).

## 15. Open questions and risks for my draft
- **The hours-offer vs hours-preference non-separability** is an admitted, unresolved identification problem they paper over with the Boxâ€“Cox functional-form justification. My access channel's hours-availability piece inherits this risk; I should either (a) lean explicitly on synthetic recovery as my identification certificate, or (b) source an external hours-availability shifter. Their paper is the citation that this is a *known* limitation, not a flaw unique to me.
- **The external instrument gap:** they identify `q` partly via the unemployment-rate exclusion restriction; I currently lack one. Risk: a referee asks what plays this role in my pooled cross-section. The paper both motivates and pressures my regionÃ—year unemployment-rate merge.
- **Elasticity magnitude:** their RURO elasticities are large and "conceptually different" from Marshallian estimates; if I report behavioural responses I should pre-empt the same comparison and frame them as offer-distribution shifts, not exogenous wage changes.
- **The `Ï€0+Ï€1â‰¡1` non-Pareto property:** any access-equalisation I run risks the same artefact (raising market availability mechanically removes non-market availability). My welfare design reads attained utility under every measure, so I should check my access-equalisation counterfactual does not inherit a mechanical non-monotonicity.
- **No welfare/decomposition precedent here:** the entire welfare+decomposition contribution of my JMP is *downstream* of where this paper stops â€” which is good for novelty but means I cannot borrow a welfare validation template from it.

## 16. TL;DR for retrieval
CapÃ©auâ€“Decoster (2016, EUROMOD WP EM4/16) estimate a Belgian (EU-SILC 2007 / EUROMOD) RURO/latent-jobs job-choice model with unitary couples, importance-sampled `(w,h)` choice sets and an explicit sampling-of-alternatives correction, factorising opportunities into job-offer intensity `q` and offered-hours `g2` (my **access**) and a lognormal wage-offer density `g1` (my **ability**), against a Boxâ€“Cox **preference** utility â€” the tightest published antecedent of my structural and proposal-correction layers and the key precedent for an external unemployment-rate exclusion restriction on offer intensity. Its substantive payoff is a **two-way, non-money-metric** EO/EP counterfactual showing opportunity decline with age operates on the extensive margin and preference change on the intensive margin â€” a precursor to, but not an instance of, my three-way access/ability/preference decomposition. It contains **no equivalent income, no inequality index, no decomposition, no occupation channel, and no WÂ¹â€“Wâ¶**, and must be cited only for the estimation/identification/opportunity-mechanism blocks, never for welfare, decomposition, occupation-as-access, a deterministic-opportunity stance, or the companion theory paper.
# CapÃ©au, Decoster & Dekkers 2016 â€” Estimating and Simulating with a Random Utility Random Opportunity Model of Job Choice: Presentation and Application to Belgium

> Source of truth: the attached PDF (*International Journal of Microsimulation* (2016) 9(2) 144â€“191). The journal masthead dates the article 2016; the project's working citation key uses 2015. Both are recorded; the **2016** outlet date is what the PDF prints. Pages cited below are the printed journal pages (144â€“191).
> Extraction discipline: claims are tagged **[explicit]** (stated in the PDF), **[analogy]** (derived by mapping to my JMP, not stated in the source), or **[not established]** (absent from the source). `[verify]` marks anything I could not confirm against the PDF text.

## 0. Metadata

- **BibTeX key:** `Capeau_et_al_2015_RURO` (project key; printed outlet year is 2016) [explicit: outlet year 2016]
- **Authors:** Bart CapÃ©au (KU Leuven), AndrÃ© Decoster (KU Leuven), Gijs Dekkers (Federal Planning Bureau) [explicit, p.144]
- **Year:** 2016 (printed); 2015 (project key) [explicit / project convention]
- **Outlet:** *International Journal of Microsimulation*, 9(2), 144â€“191 [explicit, p.144]
- **DOI/URL:** [verify] â€” no DOI printed on the supplied pages; the IJM volume/issue/page string (9(2) 144â€“191) is the locator.
- **PDF filename:** `CapÃ©au_et_al__-_2015_-_Estimating_and_Simulating_with_a_Random_Utility_Random_Opportunity_Model_of_Job_ChoicePresentation_a.pdf`
- **Tier:** T1A.
- **JMP blocks served:** estimation; identification; opportunity-mechanism (access **and** ability); data-infrastructure (EUROMOD/EU-SILC); motivation. It does **not** serve the welfare or decomposition blocks (the paper computes no welfare object and no inequality decomposition â€” Â§6, Â§7 below).

## 1. One-paragraph relevance to my JMP

This is the closest published methodological template for my structural layer: it is a worked RURO/latent-jobs estimation on EU-SILC processed through EUROMOD, the same data-and-microsimulation infrastructure I use, with the choice modelled as selection among job packages of (wage, hours) plus a non-market alternative, and with disposable income for every sampled alternative computed by EUROMOD rather than from a stored income column [explicit, pp.148â€“149, 162]. It speaks directly to all three of my channels: the wage-offer distribution `g1(w)` is my **ability** sub-block (returns to education and potential experience, lognormal dispersion `Ïƒ`); the hours-offer density `g2(h)` and the job-offer intensity `q(x_opp)` are my **access** sub-block (hours availability and market/participation intensity, with a group-specific unemployment-rate shifter on `q`); and the Boxâ€“Cox `Î¨`/`V` over consumption and leisure is my **preference** block [explicit, pp.158â€“159]. It is the canonical statement of the sampling-of-alternatives correction I must carry (the `P(0,0)/P(w,h)` proposal weight, eq. 23/25), and of the `q`/`Î³1` non-separability normalisation [explicit, pp.161â€“162]. Its limits relative to my paper are equally informative: it is **two-side** (preferences vs opportunities), not three-way; it computes **no** welfare measure and **no** decomposition; it has **no occupation channel** (occupation/sector appear nowhere in the opportunity mechanism); and it frames opportunities as genuinely **random** (Poisson offer arrivals), which is exactly the framing my design removes.

## 2. Data and setting

- **Country / year:** Belgium, EU-SILC **2007** (collected 2007) [explicit, p.163].
- **Dataset:** Belgian EU-SILC; full dataset 6,348 households / 15,493 individuals, representative of Belgian private households (collective households/institutions excluded) [explicit, p.163].
- **Sample unit:** three separately estimated sub-samples â€” **couples** (different-sex reference person + partner), **single females**, **single males** [explicit, p.163].
- **Sample sizes:** **1,457 couple households, 571 single females, 449 single males** [explicit, pp.164â€“165, Table 1].
- **Selection:** reference person (and partner, for couples) aged 16â€“64 and available for the labour market; excluded if sick, in education, disabled, or (pre)retired; **self-employed excluded** (unreliable hours/income); mixed households where only one partner is available excluded; households with labour-market-age children still co-resident dropped [explicit, pp.163â€“164].
- **Key variables:** gross household labour income (sum of members' earnings); disposable income via EUROMOD (taxes and employee SSC deducted, social transfers added, full take-up of social assistance assumed) [explicit, p.164]; **potential experience** (age âˆ’ 15 low-educ, age âˆ’ 19 middle, age âˆ’ 23 high; age excluded from the wage equation due to collinearity) [explicit, p.164]; education in three levels (low/middle/high); region (Brussels/Flanders/Wallonia); number/age-bands of children; gender [explicit, Tables 1, 3].
- **External data:** **type-specific unemployment rate** (by age Ã— sex Ã— education, Eurostat 2007) merged as a proxy for job availability and used as an exclusion restriction on `q` [explicit, pp.164â€“165, Table 2; p.157].
- **Budget-set construction:** disposable income `c = f(w,h;x_f)` is **not** given a functional form; for each drawn `(w,h)` it is computed from Belgian tax rules in **EUROMOD version F5.5** using SILC information on non-earned income and household characteristics [explicit, p.162; p.190 n.15].

**Transport to my France pooled 2015â€“2017 EUROMOD cross-section:** strong on infrastructure, partial on design. Same family of data (EU-SILC) and same microsimulator (EUROMOD) used to price every alternative â€” directly transportable [analogy]. Differences I must record: single cross-section (2007) vs my **pooled three-wave** design (no pooling/clustering issue arises for them); **no occupation variable** in their model vs my `loc4` access object; their identifying opportunity shifter is the **type-specific unemployment rate**, an external merge analogous to (but coarser than) the regionÃ—year continuous covariates I have considered. **Features they have that I do not / do differently:** an explicit **external opportunity instrument** (type-specific unemployment) entering `q` under an exclusion restriction [explicit, p.157] â€” I currently have **no external instrument**; they rely on a single cross-section and on functional-form/identification arguments rather than synthetic recovery. **Features I have that they lack:** an occupation access channel; a pooled multi-year sample; a welfare-and-decomposition layer.

## 3. Model and objects (object-by-object map to mine)

| Their object | Symbol / form | My object | Match? |
|---|---|---|---|
| Latent job set + non-market alternatives | jobs `j âˆˆ J`, non-market `i âˆˆ I`, `Z = I âˆª J` | latent-jobs set `C_i` | **Yes** [explicit, pp.148â€“149] |
| Systematic utility | `V(c, Tâˆ’h; x_V)`, Boxâ€“Cox; induces `Î¨(w,h)` via `c=f(w,h;x_f)` | preference utility `v_i(c,â„“)` | **Yes** (both Boxâ€“Cox in consumption & leisure) [explicit, pp.149â€“150, 158] |
| Random utility term | `Îµ(z)` enters **multiplicatively**, `U = VÂ·Îµ`, with `U_B` FrÃ©chet (Î±=1) | additive EV1 shock, log-sum inclusive value | **Functionally equivalent, different parameterisation** â€” their multiplicative-FrÃ©chet form is the log-level of my additive-Gumbel form [analogy; the FrÃ©chet/Î±=1 result is explicit, pp.152â€“155] |
| Hours-offer density | `g2(h)`, piecewise-uniform with peaks at half/three-quarter/full time | `log h` access term | **Yes â€” access** [explicit, p.159] |
| Wage-offer density | `g1(w)`, lognormal, mean depends on education + potential experience, dispersion `Ïƒ` | `log w` (ability) sub-block | **Yes â€” ability** [explicit, p.159] |
| Job-offer intensity | `q(x_opp) = exp(Î·_q' x_opp)`; relative intensity of market vs non-market | `log market` access term | **Yes â€” access/participation** [explicit, p.158] |
| Budget map | `c = f(w,h;x_f)` via EUROMOD | EUROMOD disposable income | **Yes** [explicit, p.162] |
| Occupation/sector channel | **none** | `loc4` occupation access | **Absent in source** [explicit by omission â€” Table 3, p.166] |
| Couples | unitary joint model, leisure assignable, leisure-complementarity term `Î²_{h1,h2}` | couples joint decision unit | **Yes** [explicit, p.158, Appendix A2 p.186] |

**Wage as a job attribute, not a fixed characteristic.** A defining feature, shared with my design: the wage is **part of the job offer**, drawn from `g1(w)`, not a fixed individual productivity endowment; the denominator of the choice probability therefore sums over `(w,h)` pairs, not over hours alone for a fixed wage (their eq. 15 vs eq. 16) [explicit, p.156; p.190 n.2].

**Does any attribute enter BOTH utility and the opportunity mechanism?** Examined directly via their specification table (Table 3, p.166): **education** enters preferences (`x_V`), job-offer intensity (`x_opp`), and the wage equation (`x_w`); **region** enters preferences and job-offer intensity; **gender** enters all blocks. So education and region appear in *both* the utility side and the opportunity side [explicit, Table 3]. The paper does **not** flag this as a problem and offers **no** dedicated identification defence of the double-entry beyond the general non-parametric identification argument and the unemployment-rate exclusion restriction on `q` (Â§8 below) [explicit by absence]. This is directly relevant to my own discipline of *not* putting occupation in both blocks at baseline: their precedent shows education/region double-entry is treatable when an external `q`-shifter and functional-form restrictions carry identification, but they do not isolate the cost of the double-entry [analogy].

## 4. Estimation method

- **Likelihood:** the choice probability of a job `(w,h)` is `Ï†(w,h) = Î¨(w,h)Â·qÂ·g1(w)Â·g2(h) / [Î¨(0,0) + âˆ«âˆ« Î¨(r,t)Â·qÂ·g1(r)Â·g2(t) dt dr]` (eq. 15), with `Ï†(0,0)` the non-market analogue (eq. 15â€²) [explicit, p.156]. Couples: a four-case likelihood (both work / only partner 1 / only partner 2 / neither), eq. 15â€³ in Appendix A2 [explicit, p.186].
- **Choice-set construction:** the offer sets `W`, `H` are unobserved, so a set `D` of `(w,h)` alternatives is **sampled from a prior `P(w,h)`**; the observed choice is always included [explicit, p.160]. Wages drawn lognormal `(m, Ï‚)`; hours drawn uniform on `[H_min, H_max)`; the non-market alternative drawn with the observed inactivity rate `Ï€0_obs` (males: `Ï€0=.104, m=2.71, Ï‚=.308`; females: `.246, 2.63, .297`) [explicit, p.162; p.191 n.14].
- **Proposal / prior correction:** **yes** â€” the simulated likelihood (eq. 23, reduced to eq. 25) carries the weight `P(0,0)/P(w,h)` on every non-base term, via Bayes' law from `P(D|(w,h))` (eq. 20â€“22) [explicit, pp.160â€“161]. This is the McFadden sampling-of-alternatives correction (they cite McFadden 1978, Ben-Akivaâ€“Lerman 1985, Train 2009) [explicit, p.191 n.13]. **Always well defined here:** `P(0,0)=Ï€0_obs>0` and `P(w,h)>0` on the lognormalÃ—uniform support, so the ratio is finite [analogy â€” they do not state a degeneracy check].
- **Normalisation / scale:** `Î¨(0,0)` normalised (a utility-level normalisation) to identify `q` (eq. 19) [explicit, p.157]. Critical non-separability: the offer-intensity constant `exp(Î·_{q,0})` and the hours-density base level `Î³1` enter the likelihood only as a product and **cannot be estimated separately**; `Î³1` is pinned by the density's integrate-to-one identity (eq. 24), and `Î·_{q,0}` is then backed out (eq. 25 uses rescaled `gÌƒ2 = g2/Î³1`, `qÌƒ = Î³1Â·q`) [explicit, pp.161â€“162].
- **Numerical method / starting values / multistart:** [verify] â€” the supplied pages state a maximum-simulated-likelihood construction but do **not** report the optimiser, starting values, or any multistart procedure. **[not established]** in the text provided.
- **What separates preferences from the opportunity mechanism:** the non-parametric identification argument (Â§8 below) plus the unemployment-rate exclusion restriction on `q` [explicit, p.157]. Note the honest caveat that `Î¨(w,h)` and `g2(h)` are **not** separately non-parametrically identified â€” the hours peaks could in principle be attributed to preferences instead (p.157, p.191 n.17).

**Verdict â€” reusable for my RURO/JAX pipeline?** **Yes, as the structural template.** Reusable steps: (i) the sampled-choice-set + `P(0,0)/P(w,h)` correction maps exactly onto my per-row `prior` column and `âˆ’log Ï€` term; (ii) the EUROMOD-prices-every-alternative loop is my build pattern; (iii) the `q`/`Î³1` non-separability is a normalisation I must replicate or consciously break. **Not reusable as-is:** their multiplicative-FrÃ©chet algebra (I use additive-Gumbel/log-sum); their lack of occupation; their single-cross-section identification. **[verify]** their optimiser before citing any numerical-implementation detail.

## 4b. Proposal / sampling-of-alternatives correction

- **How alternatives are sampled:** from `P(w,h)` = lognormal in `w` Ã— uniform in `h`, plus the non-market point mass at `Ï€0_obs` (eq. 26) [explicit, p.162].
- **Is the proposal individualised?** **Partly, but less than mine.** The prior `P(w,h)` as written uses **common** lognormal parameters `(m, Ï‚)` within gender (separate male/female values given) and a **common** inactivity probability `Ï€0_obs` within gender [explicit, p.162, n.14] â€” i.e. individualised by gender only, *not* by household covariates. There is **no occupation-conditioned draw** (no occupation in the model). This contrasts with my proposal, whose wage mean is household-specific (`Î¼_i = X_i b + Î´_occ[loc4_i]`) and whose occupation channel is genderÃ—education-stratified [analogy â€” the contrast is to my own design, not stated in the source].
- **Is the correction McFadden-style?** **Yes** â€” Bayes'-law reweighting of sampled alternatives, citing McFadden (1978) and Ben-Akivaâ€“Lerman (1985) [explicit, p.191 n.13].
- **Does each drawn alternative carry its own log-prior?** **Yes** â€” the `P(0,0)/P(w_i,h_i)` factor is per-alternative (eq. 20, 23) [explicit, pp.160â€“161].
- **Relation to my importance-sampling welfare integrator:** their estimation-stage correction is the exact analogue of my welfare-stage `âˆ’log Ï€(j)` term; my concern that only wage/occupation are individualised while hours/employment are common is *more* acute in their setup, where the **entire** proposal is common-within-gender. Their design therefore does not test the well-conditioning question my proposal audit addresses; it is a precedent for the *form* of the correction, not for proposal individualisation [analogy].

## 5. Opportunity mechanism â€” [MOST IMPORTANT; split by channel]

The opportunity side is a **genuine stochastic offer process**: jobs and non-market activities arrive via **independent inhomogeneous spatial Poisson processes**, so the number of offers of any type with utility â‰¥ u is Poisson, and the max attainable utility over a region is FrÃ©chet (location 0, shape Î±=1) [explicit, pp.151â€“155, Appendix A1 pp.184â€“185]. This is the literal "random opportunities" content my design deliberately drops. The intensity is `g2(h)Â·g1(w|h)Â·Î»1(Ï…)` with `Î»1(Ï…)=q/Ï…Â²` (and `Î»0(Ï…)=1/Ï…Â²` for non-market), the inverse-square form guaranteeing IIA in the job-choice probabilities (Dagsvik 1994) [explicit, pp.151â€“154].

Mapping to my three sub-objects:

- **access â€” hours availability.** `g2(h)`: piecewise-uniform density over labour-time regimes with a baseline level `Î³1` and **peaks** (estimated bumps `Î³1Â·exp(Î³_{k+1})`) around half time (18.5â€“20.5h), three-quarter time (29.5â€“30.5h), and full time (37.5â€“40.5h); `H_min=1h`, `H_max=70h` (p.162); the only covariate allowed to shift it is **gender** [explicit, p.159, Fig. 1]. Maps to my `log h` access term.
- **access â€” market/participation intensity.** `q(x_opp) = exp(Î·_q' x_opp)`: the relative intensity of suitable job offers vs non-market opportunities; covariates are a constant, region, education, gender, and the **group-specific unemployment rate** (the exclusion restriction) [explicit, pp.157â€“159, Table 3]. Reported normalised as `q/(1+q)` in figures (p.191 n.18). Maps to my `log market` access term.
- **ability â€” wage technology.** `g1(w;x_w)`: lognormal with mean a function of **education** and **potential experience** (quadratic) and dispersion `Ïƒ`; gender-specific [explicit, p.159, Table A3]. This is exactly my ability sub-block (returns to education + experience, residual dispersion `Ïƒ`). Estimated `Ïƒ â‰ˆ 0.26` for both sexes; education and experience shift the offer distribution rightward, with a turning point in experience (â‰ˆ37y males, â‰ˆ32y females) [explicit, pp.168, 188].
- **occupation.** **None.** Occupation/sector enters neither utility nor opportunities; there is no `loc4`-type object and no industry/NACE object anywhere in the model (Table 3, p.166) [explicit by omission]. **No sector/industry conflation risk arises** because neither concept is present.

**Does feasibility vary with circumstances?** Yes: by gender (all offer blocks), education and region (`q` and `g1`), potential experience (`g1`), and the external ageÃ—sexÃ—education unemployment rate (`q`) [explicit, Table 3, pp.158â€“159].

**Functional forms (exact):**
- `ln q(x_opp) = Î·_q' x_opp` (log-linear) [explicit, p.158].
- `g1(w;x_w) = (1/(wÂ·ÏƒÂ·âˆš(2Ï€)))Â·exp(âˆ’Â½((ln w âˆ’ Î´_{g1}' x_w)/Ïƒ)Â²)` (lognormal) [explicit, p.159].
- `g2(h)` piecewise-uniform with peak multipliers `exp(Î³_{k+1})` (form on p.159).
- `Î»1(Ï…)=q/Ï…Â²`, `Î»0(Ï…)=1/Ï…Â²` (p.151, p.154).

**Cost to my decomposition if such a mechanism were absent:** they *have* the mechanism, so the relevant lesson is the converse â€” their honest statement that `Î¨(w,h)` and `g2(h)` are not separately non-parametrically identified (p.157) is precisely the preference/access confound my access component must survive; without the `q`-exclusion restriction the access channel would not be cleanly separated from preferences [explicit caveat, p.157].

## 6. Welfare object â€” and its place on my WÂ¹â€“Wâ¶ map

**The paper computes NO welfare object.** There is no money-metric, no equivalent income, no equivalent/compensating variation, and no inclusive-value welfare statistic anywhere in the supplied text [explicit by exhaustive omission â€” the results sections are Â§5 estimation, Â§6 fit/elasticities, Â§7 an education counterfactual on participation/hours]. The "fit" exercise compares simulated vs observed disposable-income, wage, and hours **distributions** (Figs 6â€“11), and the counterfactual reports **participation rates and mean hours** (Tables 6â€“7), not welfare [explicit, pp.171â€“178].

**Place on my WÂ¹â€“Wâ¶ map:** **N/A â€” the source contains none of WÂ¹â€“Wâ¶ and makes no compensation/responsibility (Ind-y / Ind-A) distinction.** Any mapping would be invented. I must **not** cite this paper for welfare-measure content.

**Verdict:** incompatible as a welfare source; it is an *estimation and simulation* template only. The one bridge to my welfare layer is purely computational: the same `Î¨`, `g`, and proposal correction they estimate are the inputs my ex-ante inclusive value `V_i` is built from â€” but they never form that inclusive value as a welfare quantity.

## 6b. Inclusive value and money-metric inversion

- **Inclusive value as welfare core:** **No.** The FrÃ©chet/log-sum structure is used to derive **choice probabilities** (the denominator of eq. 15), not as a welfare statistic [explicit, pp.155â€“156].
- **Money-metric inversion:** **N/A** â€” no money figure is recovered by inverting an own-utility map; no EV/CV is computed [explicit by omission].
- **Expectation over shocks analytic or simulated?** For **estimation**, the expectation is taken **analytically** â€” the Poisson/FrÃ©chet algebra yields the closed-form choice probability with no shock draws (eqs. 13â€“15) [explicit, pp.155â€“156]. For **simulation/fit**, they *do* draw FrÃ©chet shocks `Îµ(w_s,h_s)` per sampled alternative and take the simulated argmax (p.163) [explicit] â€” i.e. simulation is by drawn shocks, estimation is analytic. This is relevant to my design choice to keep the welfare expectation **analytic in the shocks** (closed-form log-sum): their estimation step is the precedent; their simulation step is the thing I avoid for welfare [analogy].

## 7. Inequality / decomposition content â€” [three-way where relevant]

**No inequality index and no decomposition of any kind.** No Gini/MLD/Theil/Atkinson; no Shapley/Shorrocks/factor/subgroup/RIF decomposition [explicit by omission].

The **only** "decomposition-flavoured" content is the **preferences-vs-opportunities channel attribution in Table 7** (p.178): they re-simulate the education counterfactual switching the education level *only in preferences* ("alt pref") vs *only in the opportunity blocks* ("alt opp"), and read off which channel drives the change in **participation and mean hours**. They conclude the education effect "run[s] predominantly through the channel of opportunities rather than through preferences" [explicit, pp.178â€“179]. This is a **two-way, behavioural (participation/hours), counterfactual-simulation** attribution â€” **not** a welfare-inequality decomposition, **not** Shapley, **not** order-independent, and it equalises nothing; it swaps a covariate's value between blocks.

**Verdict â€” reusable for my three-way access/ability/preference Shapleyâ€“Shorrocks split?** **No, not as a decomposition.** It is useful only as (a) a conceptual precedent that the preference/opportunity channels can be separately *toggled* once the structural model is estimated, and (b) a warning that their toggle is on **behaviour**, not on a **welfare** object, and is **two-way** (preference vs opportunity), not three-way. To reach my split it would need: a welfare object (absent), an inequality index (absent), the Shapley equalisation machinery (absent), and the ability/access subdivision *within* opportunities (they keep wage and hours/`q` separate in estimation but never separate them as inequality sources) [explicit by absence].

## 8. Identification and the separation of preferences from opportunities â€” [STRICT]

The identification argument (their Â§3.2, pp.157â€“158) is the backbone item for my identification note. Stated explicitly:

1. **Identify `Î¨(w,h)Â·g2(h)`:** take two observationally-equivalent groups working different hours `h1, h2` at the **same** wage `w`; the population ratio `Ï†(w,h1)/Ï†(w,h2) = [Î¨(w,h1)g2(h1)]/[Î¨(w,h2)g2(h2)]` (eq. 17); varying `w` traces out `Î¨(w,h)g2(h)` [explicit].
2. **Identify `g1(w)`:** take groups at the **same** hours `h`, different wages `w1,w2`; the ratio (eq. 18) isolates `g1(w1)/g1(w2)`, pinned to a density by `âˆ« g1 = 1` [explicit].
3. **Identify `q`:** compare workers vs non-workers in an observationally-equivalent group (eq. 19); with `Î¨(0,0)` normalised, `q` is identified [explicit].
4. **Exclusion restriction:** a **group-specific unemployment rate** is added to `q`, assumed to shift labour demand but **not** preferences â€” improving identification of `q` beyond the non-parametric argument [explicit, p.157].

**Honest non-identification caveat (critical to carry):** `Î¨(w,h)` and `g2(h)` are **NOT** separately non-parametrically identified; the observed hours peaks could be explained by preferences instead, and the resolution is a **functional-form justification** of Boxâ€“Cox preferences (citing Dagsvikâ€“RÃ¸ine Hoff 2011, Dagsvik 2013) [explicit, pp.157â€“158, p.191 n.17]. They also flag that including gross wage *and* hours separately in `f` (for the Belgian work bonus) may threaten non-parametric identification (p.190 n.5).

**Transport to my France pooled cross-section (no panel, no external instrument):** Their argument is **cross-sectional** (observationally-equivalent groups), so it transports in principle to a cross-section â€” good news for me [analogy]. But two of their load-bearing devices I currently lack: (i) the **external unemployment-rate exclusion restriction** on `q` â€” I have no external instrument at baseline, though regionÃ—year continuous covariates are the natural analogue I have considered; (ii) their reliance on the **functional-form justification** of Boxâ€“Cox to break the `Î¨`/`g2` confound â€” I share Boxâ€“Cox, so I inherit both the device and its fragility. My defence against the "your decomposition is mechanical" referee should note that **the preference/access confound is acknowledged in the founding RURO-estimation paper itself** and is resolved there by functional form + an exclusion restriction, not by data variation alone [explicit, pp.157â€“158]. My synthetic-recovery standard is a *stronger* discipline than their in-sample/functional-form argument; the source does not use synthetic recovery [explicit by absence â€” they report no recovery experiment].

## 9. Key results and magnitudes

All figures **[explicit]**, Belgium EU-SILC 2007, from the named tables.

- **Aggregate wage elasticities (Table 4, p.174):** shift each gender's wage-offer distribution right by 10% (add ln 1.1 to the location). Total elasticities: couple female **0.6445**, couple male (own, male shift) **0.3304**, single female **0.6877**, single male **0.4569**; **cross** (partner) elasticities negative (couple male under female shift **âˆ’0.1734**; couple female under male shift **âˆ’0.2014**). Intensive-margin and part-in/part-out components tabulated. They note these totals are "rather large" vs micro Marshallian estimates but argue they are conceptually macro-like (include the extensive margin) and that RURO frictions push them *down* relative to macro figures [explicit, pp.174â€“175].
- **Wage-offer dispersion:** `Ïƒ â‰ˆ 0.264` (M), `0.261` (F) (Table A3, p.189) [explicit].
- **Wage-offer education/experience gradient:** high education `+0.260` (M), `+0.291` (F) on log wage; low education `âˆ’0.147` (M), `âˆ’0.095` (F); experience enters with a positive linear and negative quadratic term (turning points â‰ˆ37y M, â‰ˆ32y F) [explicit, pp.168, 189].
- **Offer intensity `q`:** education raises offer availability per se; for **males** a higher type-specific unemployment rate *raises* estimated suitable-offer intensity (coefficient `+0.338`, tâ‰ˆ1.50, not significant), partially offsetting education; for **females** the unemployment-rate coefficient is small/negative (`âˆ’0.072`) [explicit, pp.169â€“170, 189].
- **Fit (Â§6.1):** couples mean simulated consumption â‚¬3,070/m vs â‚¬3,143 observed; single-male consumption â‚¬1,585 fitted vs â‚¬1,588 observed; non-participation over-estimated; three-quarter-time peak under-fitted [explicit, pp.171â€“173].
- **Education counterfactual (Â§7, Tables 5â€“7):** equalising male to female education has a **modest** participation/hours effect, concentrated in **men** (single males 30â€“45: participation +1.5 to >7pp; mean hours +0.5 to >4h); female labour supply barely moves; the effect runs **predominantly through opportunities, not preferences** (Table 7) [explicit, pp.175â€“179].

**Benchmarking value for me:** their `Ïƒâ‰ˆ0.26` wage-offer dispersion and the education/experience gradients are a plausibility yardstick for my ability sub-block; their finding that an education shock works mainly through the **opportunity** channel is a (behavioural, not welfare) precedent that the opportunity channel carries real weight â€” consistent with, but not evidence for, a material opportunity share in my **welfare** decomposition [analogy â€” do not present their behavioural result as a welfare-share result].

## 10. Estimators, theorems, or formal results

1. **FrÃ©chet max-utility result.** Statement [explicit, p.153]: under the Poisson offer process with intensity `g2(h)g1(w|h)Î»1(Ï…)` and `Î»1(Ï…)=q/Ï…Â²`, the maximum attainable utility `U_B` over region `B` is FrÃ©chet, `P(U_B<u)=exp(âˆ’Ïƒ_B/u)` with scale `Ïƒ_B = âˆ«âˆ« g2(t)g1(r|t) qÎ¨(r,t) dr dt`, location 0, shape Î±=1. Technique: number of offers above utility `u` is Poisson; `P(U_B<u)=P(N=0)`; integrate the inverse-square intensity (eq. 6â€“8). **Reusability:** background to my log-sum (the additive-Gumbel analogue); I do not reuse the FrÃ©chet form directly. Verdict: **maybe / conceptual** [analogy].
2. **Choice probability (eq. 15).** `Ï†(w,h)=Î¨(w,h)q g1(w)g2(h) / [Î¨(0,0)+âˆ«âˆ«Î¨(r,t)q g1(r)g2(t)dt dr]`; assumption `g1(w|h)=g1(w)` (wage-hours independence) for identification [explicit, p.156]. **Reusability: yes** â€” structural analogue of my per-row value plus log-sum; the wage-hours independence assumption is a modelling choice I should state explicitly if I adopt it.
3. **Sampled-set simulated likelihood (eq. 23/25).** With proposal `P(w,h)` and weight `P(0,0)/P(w,h)`; `q`/`Î³1` collapse to `qÌƒ=Î³1 q`, `gÌƒ2=g2/Î³1`, with `Î³1` from the integrate-to-one identity (eq. 24) [explicit, pp.160â€“162]. **Reusability: yes, directly** â€” this is the correction and normalisation my pipeline must implement; verdict **yes**.
4. **Couples likelihood (eq. 15â€³, Appendix A2).** Four-regime joint probability with independent per-partner offer processes and a joint `Î¨(w1,h1,w2,h2)` carrying a leisure-complementarity term [explicit, p.186]. **Reusability: yes** â€” template for my 901-alternative joint couples grid.

No numbered theorems are stated in the supplied pages; the formal content is the Poissonâ†’FrÃ©chet derivation and the likelihood algebra above [explicit].

## 11. Robustness and specification sensitivity

- **What they vary:** the specification table (Table 3) fixes which covariates enter each block; they do **not** report sensitivity to choice-set size `|D|`, number of draws, or number of optimiser starts in the supplied pages [verify / not established].
- **Acknowledged fragilities:** (i) `Î¨`/`g2` not separately non-parametrically identified â€” hours peaks attributable to preferences instead (p.157, n.17); (ii) including `w` and `h` separately in `f` may threaten identification (n.5); (iii) the model is **static**, **not an equilibrium/matching model**, frictions taken as given (Â§8 conclusion, p.179); (iv) sample is not representative of the working-age population (selection on labour-market availability), handled in the counterfactual by re-weighting to MIDAS education distributions (p.175).
- **For my stress-tests:** their honest `Î¨`/`g2` confound tells me exactly where my **access vs preference** boundary is weakest (hours peaks), and their absence of a choice-set-size/draw-count robustness report is a gap I should *not* replicate â€” my welfare-integration ESS gate and draw-growth stability gate are the discipline they lack [analogy].

## 12. What I can cite this paper for

- The **canonical RURO/latent-jobs estimation template** on EU-SILC + EUROMOD, with wage as a drawn job attribute and EUROMOD pricing every sampled alternative [explicit, pp.148â€“149, 162].
- The **sampling-of-alternatives (proposal/prior) correction** in a RURO context, McFadden-style, per-alternative `P(0,0)/P(w,h)` weight (eq. 20â€“25) [explicit, pp.160â€“162].
- The **`q`/`Î³1` non-separability** and its resolution by the hours-density normalisation identity (eq. 24) [explicit, pp.161â€“162].
- The **non-parametric identification argument** for separating wage offers, hours offers, and offer intensity from preferences, **and its explicit limit** (`Î¨`/`g2` not separately identified), plus the **unemployment-rate exclusion restriction** as a labour-demand shifter on `q` [explicit, pp.157â€“158].
- The **Boxâ€“Cox preference form** for consumption/leisure in RURO and its functional-form justification lineage (Dagsvikâ€“RÃ¸ine Hoff 2011; Dagsvik 2013) [explicit, p.158].
- The **couples unitary joint-choice likelihood** with assignable leisure and a complementarity term (Appendix A2) [explicit, p.186].
- The **behavioural** finding that an education counterfactual operates mainly through the **opportunity** channel rather than preferences â€” as a *behavioural* result on participation/hours [explicit, pp.178â€“179].
- **EUROMOD F5.5** as the gross-to-net engine for Belgian SILC alternatives, full social-assistance take-up assumed [explicit, p.162, p.164].

## 13. What I should NOT cite this paper for â€” [overclaim risks]

- **NOT** for any **welfare** measure, money-metric, equivalent income, EV/CV, or inclusive-value welfare statistic â€” the paper computes none [explicit by omission, Â§6/Â§6b above].
- **NOT** for an **inequality decomposition** of any kind, and **NOT** for a three-way access/ability/preference split. Its Table 7 is a **two-way, behavioural** (participation/hours) counterfactual toggle, not a welfare-inequality Shapley decomposition. Citing it as a decomposition precedent would be an overclaim [explicit, Â§7 above].
- **NOT** for WÂ¹â€“Wâ¶ or any compensation/responsibility (Ind-y / Ind-A) reading â€” these concepts are absent; do not map the paper onto the family.
- **NOT** for occupation or sector/industry opportunity content â€” the model has **no** occupation or industry channel; do not let "job offers" be read as occupation-specific offers. (No sector/industry conflation exists *in the source* to flag, but I must not import one.)
- **Random vs deterministic framing:** this paper is genuinely **random-opportunity** (Poisson offer arrivals, FrÃ©chet max); my design treats opportunities as **deterministic** and uses RURO only as estimation machinery. Do not present their Poisson/FrÃ©chet stochastic-offer apparatus as if it were my deterministic-feasible-set object [explicit, pp.151â€“155].
- **Elasticity magnitudes** are Belgian 2007 offer-distribution-shift elasticities of a particular conceptual type (whole-distribution shift, not an exogenous wage change) â€” do not quote them as standard Marshallian/Hicksian micro elasticities; the authors explicitly warn against that reading [explicit, pp.174â€“175].
- **Theory-paper boundary:** nothing here touches the Haydarâ€“Maniquet axiomatic paper; this is an empirical-estimation source only. Do not let any normative reading leak from my theory paper onto this citation, and do not read this paper as a theory contribution.

## 14. Direct quotes worth citing

Short verbatim excerpts with page numbers (transcribe-verify before final use):

1. "These type of models â€¦ try to understand individual heterogeneity in choice behaviour as a combined effect of differences in preferences and opportunities." (p.145) [explicit]
2. "Job offers are considered as packages of wages, labour time regimes, and a number of other attributes." (p.147) [explicit]
3. "The utility function Î¨(w,h) and the distribution of offered labour time regimes g2(h) are however not separately nonâ€“parametrically identified." (p.157) [explicit]
4. "More specifically, a group specific unemployment rate is added as an explanatory variable for q. We assume that this variable does not affect individual preferences, but â€¦ has some relation with labour demand." (p.157) [explicit]
5. "We conclude that the already small change in labour market participation due to expected changes in education level, run predominantly through the channel of opportunities rather than through preferences." (pp.178â€“179) [explicit]
6. "The model is essentially static. And it does not provide a complete equilibrium framework. It is not a matching model â€¦" (p.179) [explicit]
7. "In our implementation, we do not specify a functional form for the disposable income function f(w,h;x_f). For each draw (w,h) â€¦ disposable income â€¦ is instead calculated on the basis of the existing Belgian tax rules, as implemented in â€¦ euromod." (p.162) [explicit]

## 15. Open questions and risks for my draft

- **The `Î¨`/`g2` non-identification is inherited.** I use the same Boxâ€“Cox preferences and an hours-availability access channel; their candid statement that hours peaks are not separately identified from preferences is the sharpest known threat to my **access-vs-preference** boundary. My draft must address it head-on (functional-form justification + whatever exclusion variation I have) rather than let a referee discover it [explicit, p.157].
- **External instrument gap.** Their identification leans on a type-specific unemployment-rate exclusion restriction on `q`; I have none at baseline. The risk is that my access channel is identified only by functional form + synthetic recovery. The regionÃ—year continuous covariate merge is the natural analogue to consider, but it is not yet in the baseline [analogy].
- **No welfare bridge in the literature template.** The closest estimation cousin to my paper stops *before* welfare; there is no off-the-shelf precedent here for forming the ex-ante inclusive value as a welfare object, inverting to a money metric, or decomposing it. My welfare-and-decomposition layer is genuinely the novel contribution relative to this template, but it also means I cannot lean on this paper for welfare-side validation [explicit by omission].
- **Proposal individualisation.** Their proposal is common-within-gender; mine is partly individualised (wage/occupation). Their setup does not test the well-conditioning of importance sampling under partial individualisation, so it offers no reassurance on my ESS concern; that remains mine to validate [analogy].
- **Numerical implementation undocumented in the supplied pages.** Optimiser, starting values, multistart, and choice-set-size/draw-count robustness are not reported [verify]; I should not assume their pipeline was multistart-validated.

## 16. TL;DR for retrieval

CapÃ©auâ€“Decosterâ€“Dekkers (IJM 2016) is the canonical worked **RURO/latent-jobs estimation** on Belgian EU-SILC 2007 with **EUROMOD** pricing every sampled (wage, hours) alternative â€” supplying my structural template for the **ability** channel (lognormal wage offers `g1(w)` in education and potential experience, dispersion Ïƒ) and the **access** channel (hours-peak density `g2(h)`, offer intensity `q` with an external unemployment-rate exclusion restriction), the McFadden **proposal/prior correction** (`P(0,0)/P(w,h)`), and the `q`/`Î³1` non-separability normalisation. It computes **no welfare object and no inequality decomposition** â€” its only channel attribution is a two-way *behavioural* (participation/hours) education counterfactual (Table 7) â€” so it informs my **preference/ability/access estimation and identification** blocks but is **incompatible** as a source for WÂ¹â€“Wâ¶, money-metric welfare, or my three-way Shapleyâ€“Shorrocks split, and its **genuinely random** Poisson/FrÃ©chet opportunity framing is exactly what my deterministic-feasible-set design replaces.
# Dagsvik, Jia, Kornstad & Thoresen 2014 â€” Theoretical and Practical Arguments for Modeling Labor Supply as a Choice among Latent Jobs

> **Extraction note.** This is a **survey / methodological-arguments** paper, not
> an empirical estimation paper. Its empirical figures are borrowed from Dagsvik
> & Jia (2012a). The primary technical derivations of the latent-jobs model live
> in **Dagsvik & StrÃ¸m (2006)** and **Dagsvik & Jia (2012a)**, to which this paper
> repeatedly defers; cite those for the machinery, this one for the *argument and
> interpretation*. Throughout I flag **[explicit]** (stated in this source),
> **[analogy]** (derived by mapping to the JMP), and **[not established]** (absent
> from this source). Pages cited from the running headers in the supplied PDF;
> ambiguous locations marked **[verify]**.

---

## 0. Metadata

- **BibTeX key:** `dagsvik_jia_kornstad_thoresen_2014`
- **Authors:** John K. Dagsvik (Statistics Norway and Ragnar Frisch Centre for Economic Research); Zhiyang Jia, Tom Kornstad, Thor O. Thoresen (Statistics Norway).
- **Year:** 2014 (Â© 2013).
- **Outlet:** *Journal of Economic Surveys*, Vol. 28, No. 1, pp. 134â€“151.
- **DOI:** 10.1111/joes.12003 [explicit, p.134].
- **PDF:** `Dagsvik_et_al__-_2014_-_THEORETICAL_AND_PRACTICAL_ARGUMENTS_FOR_MODELING_LABOR_SUPPLY_AS_A_CHOICE_AMONG_LATENT_JOBS.pdf`
- **Tier:** T1A (as filed). Qualifier: it is the *programmatic statement* of the latent-jobs research program rather than its technical core.
- **JMP block(s) it serves:** **model-foundation / motivation**; **estimation** (the latent-jobs likelihood form); **identification** (the preference-vs-opportunity separation result); **opportunity-mechanism â€” access** (hours availability $g(h)$ and total job availability $\theta$). It does **not** serve the **welfare** or **decomposition** blocks (no welfare measure, no inequality index, no decomposition is computed), and it speaks to **ability** only obliquely (a separately estimated qualifications-based wage equation, not an opportunity-density channel).

---

## 1. One-paragraph relevance to my JMP

This is the canonical theoretical justification for the object at the centre of my structural layer: it shows that the *ad hoc* part-time/full-time dummies of the conventional van Soest discrete-choice model can be re-read as an **explicit, structural opportunity term** $\log(\theta g(h))$ inside the choice index, i.e. that my opportunity-density terms ($\log h$, $\log\text{market}$) have a demand-side foundation rather than being a fitting device [explicit, pp.139â€“141]. It speaks directly to my **access** channel (the hours-opportunity distribution $g(h)$ and the total-job-availability scalar $\theta$, the latter linkable to the unemployment rate) and supplies the foundational **identification** result I must defend: preferences and the opportunity distribution are separable only up to an additive function of hours unless one imposes functional form (Boxâ€“Cox) or uses desired-hours data [explicit, p.143]. It does **not** separate **ability** from **access** within the opportunity object, computes **no** welfare measure, and contains **no** decomposition â€” so it anchors my estimation and identification prose, not my welfare or decomposition prose.

---

## 2. Data and setting

- This paper is a survey; it has no estimation dataset of its own. The empirical illustrations are **lifted from Dagsvik & Jia (2012a)**: **Norwegian married couples**, base year **1997**, Labour Force Survey data, with out-of-sample validation against 2006 LFS data and 2003 income-tax-return data [explicit, pp.144â€“145].
- **Sample unit in the illustration:** married couples (a joint decision unit) [explicit, p.144]. This matches my couples unit in spirit, but the figures are illustrative, not re-estimated here.
- **Key variables in the illustration:** annual hours of work discretised into eight intervals with positive-hours medians **260, 780, 1040, 1560, 1960, 2340, 2600** [explicit, p.144]; household disposable income (Figure 3) [explicit, p.146 [verify]].
- **Budget-set construction:** $C=f(hw,I)$, where $f(\cdot)$ maps gross income to after-tax household income and "can in principle capture all details of the tax and benefit system" [explicit, p.139, eq. (4)]. This is the same role my EUROMOD disposable-income map plays [analogy].
- **Transport to my France pooled 2015â€“2017 EUROMOD cross-section:** the *model* transports cleanly (static, discrete, tax-benefit budget). The *identification and validation strategy does not transport directly*: the paper's out-of-sample assessment exploits a **tax reform** (2006) and a second data source, and one of its two identification routes requires **desired/preferred-hours data** (Euwals & van Soest 1999; Bloemen 2008) [explicit, p.143]. I have **no panel, no desired-hours instrument, and no exploited reform**; I rely instead on functional form plus **synthetic recovery** (which this paper does not use). Features named here that I do **not** have: a tax-reform natural experiment for out-of-sample validation; desired-hours data; job-specific wage data of the Dagsvikâ€“Jia (2012a) "general case."

---

## 3. Model and objects (object-by-object map to mine)

- **Choice set = my latent-jobs set?** **Yes, conceptually [explicit].** The agent chooses among *jobs* $z=1,2,\dots$ (with $z=0$ the non-market alternative), each job carrying fixed job-specific hours $H(z)$ and non-pecuniary attributes; observed hours and income are those of the chosen job [explicit, pp.139â€“140, eq. (8)]. The choice sets $\{B(h)\}$ (available jobs with hours $h$) are latent to the researcher [explicit, p.140]. This is exactly my latent-jobs framing.
- **Deterministic utility = my preference utility $v$?** **Yes [explicit].** $U(C,h,z)=v(C,h)+\varepsilon(z)$ with $\varepsilon(z)$ iid Gumbel; $v(C,h)$ is the systematic preference term [explicit, p.139, eq. (8)]. The recommended functional form is **generalized Boxâ€“Cox in consumption and leisure with an interaction term** (eq. (15)) [explicit, p.143] â€” the same family as my preference block.
- **Explicit opportunity / availability mechanism analogous to my $g$?** **Yes, but only over hours and total count [explicit].** The number of available jobs at hours $h$ is $m(h)$; with $\theta=\sum_x m(x)$ and $g(h)=m(h)/\theta$, the term $\theta g(h)$ is the **opportunity measure** and $g(h)$ the **opportunity distribution** [explicit, p.141]. It enters the choice index additively as $\log(\theta g(h))$ (eq. (14)) [explicit, p.141].
  - **hours channel:** present, as $g(h)$ [explicit].
  - **market / participation channel:** present, as $\theta$ (total job availability; depends on education and a constant; linkable to the unemployment rate) and the single non-market alternative $m(0)=1$ [explicit, pp.140â€“141, 143; footnote 12 p.148].
  - **wage (ability) channel:** **not in the opportunity density of this exposition.** The baseline assumes the wage "only depends on individual qualifications and does not vary across jobs" [explicit, p.139]; wages are predicted from a **separately estimated wage equation** [explicit, p.144]. Job-specific wages are deferred to the cited Dagsvik & Jia (2012a) "more general case" [explicit, p.139].
  - **occupation channel:** **absent in the baseline** ("the jobs are latent and thus job characteristics do not appear") [explicit, p.144]. The cited Dagsvik & StrÃ¸m (2006) extension classifies jobs into **two observable sectors (public and private)** [explicit, p.144].
- **Budget map = my EUROMOD disposable income?** Functionally yes (eq. (4)); their $f$ is my EUROMOD map [analogy].
- **Does any job attribute enter BOTH utility and the opportunity mechanism?** **No [explicit].** Hours enter utility via $v(C,h)$ and availability via $g(h)$, but these are distinct objects whose **non-separability is the paper's central identification caveat** (Â§8), not a deliberate double-entry. They do not place wage or occupation in both blocks; in fact the baseline keeps occupation out of both. No identification-driven double-entry is asserted.

**Differences to record.** (i) Their opportunity object is **one-dimensional over hours** (plus the scalar $\theta$); my $g$ additionally carries a **wage/ability** sub-block and an **occupation** access sub-block, which are beyond this paper [explicit vs. JMP]. (ii) They use a **fixed finite hours grid $D$ with multiplicities $m(h)$**, not a **sampled** alternative set; consequently there is **no sampling-of-alternatives correction** in their likelihood (see Â§4b). (iii) Their "sector" (public/private) is an **institutional** partition â€” it is *neither* my occupation (`loc4`/ISCO) *nor* my industry (`lindi`/NACE); do not map it onto either.

---

## 4. Estimation method

- **Likelihood / estimator:** multinomial-logit-type choice probabilities derived from the iid-Gumbel RUM, with representative utilities $\{\psi(h)\}$ **weighted by job frequencies $\{m(h)\}$** (eqs. (10)â€“(11)) and re-expressed as $\exp(\psi(h)+\log(\theta g(h)))$ in the denominator-normalised form (eq. (14)) [explicit, pp.140â€“141]. Maximum likelihood, with the wage equation, choice probabilities, and opportunity measure specified jointly [explicit, p.144]. No GMM, no simulated argmax in the exposition.
- **Choice-set construction:** **fixed discrete grid** of hours points $D$ (the illustration uses eight intervals). Discretisation is argued to be inessential and arbitrarily refinable [explicit, pp.139, 144].
- **Proposal / sampling density:** **none** â€” the grid is fixed, not sampled (see Â§4b).
- **Prior/proposal correction ($-\log\pi$ subtracted from the choice index)?** **Not established / not present.** The additive term inside the index is the **structural** $\log(\theta g(h))$, not a nuisance sampling correction. It is always well defined for $g(h)>0$ [analogy]; the question of an importance-sampling prior does not arise here.
- **Normalisation / scale:** the summability constraint $\sum_h g(h)=1$ need **not** be imposed at estimation because $\theta g(h)$ enters jointly and the normalisation can be applied post-estimation [explicit, p.143]. Fixed cost can be folded into $\theta$ as $\theta\exp(c)$ (Cogan 1981) [explicit, p.141].
- **What pins preferences apart from the opportunity mechanism:** functional-form restrictions (Boxâ€“Cox, eq. (15)) â€” see Â§8. Without them the two are confounded up to an additive $d(h)$ [explicit, p.143].
- **Numerical method / starting values / multistart:** not discussed in this survey [not established]. (Boxâ€“Cox estimation difficulties are flagged â€” Â§11.)
- **Verdict â€” reusable for my RURO/JAX pipeline?** **Partly â€” as the structural template, not as a runnable recipe.** Reuse: the $\exp(\text{utility}+\log\text{opportunity})$ index structure (eq. (14)) is exactly my per-alternative value's structural backbone, **minus** my $-\log\pi$ correction (which my pipeline needs because I *sample* alternatives, whereas they use a fixed grid). Do **not** reuse: their fixed-grid construction in place of my sampled set; and there is no estimation code or numerical protocol to reuse here (it is in the cited companions).

## 4b. Proposal / sampling-of-alternatives correction  [extract even if brief]

**Not present in this paper.** Alternatives are a **fixed finite grid** of hours points with structural multiplicities $m(h)$; there is no random sampling of alternatives and therefore no McFadden-style sampling correction and no per-alternative log-prior [explicit, pp.139â€“141]. The additive log-term $\log(\theta g(h))$ that appears inside the choice index (eq. (14)) is a **structural opportunity weight** (the object of interest), **not** a proposal/prior correction â€” this is the single most important place a careless reader could conflate their model with my pipeline. Mapping to my design: their $\log(\theta g(h))$ is the analogue of my **structural** $[\log h + \log w + \log\text{market}]$ block, **not** of my $-\log\pi(j;x_i)$. My $-\log\pi$ exists only because I integrate over *sampled* draws; it has no counterpart here. Relation to my proposal-individualisation concern (wage/occupation individualised; hours/employment common): **not addressed** â€” the question is meaningless for a fixed grid [not established].

## 5. Opportunity mechanism  [MOST IMPORTANT â€” split by channel]

The mechanism is a **deterministic density over hours plus a total-availability scalar**, derived from latent job multiplicities. Formally: $B(h)$ is the set of available jobs with hours $h$; $m(h)=|B(h)|$; $m(0)=1$; $\theta=\sum_{x\in D} m(x)$; $g(h)=m(h)/\theta$; the **opportunity measure** is $\theta g(h)$ [explicit, pp.140â€“141]. The $\{m(h)\}$ are **sufficient statistics** for the latent choice sets under the iid-Gumbel assumption [explicit, p.141]. Equilibrium foundation: $\theta$ can be derived from a two-sided matching model (Dagsvik 2000; Dagsvik & Jia 2012b), but the paper uses a **reduced-form** representation [explicit, p.142] â€” as do I [analogy].

Mapping to my three sub-objects:

- **access (hours / market / region / year / occupation offers).**
  - *Hours availability:* **explicit and central** â€” $g(h)$. The standard empirical specification is **$g(h)$ uniform apart from peaks at part-time and full-time hours** [explicit, p.143], implemented as $\log(\theta g(h))$ **linear in length of schooling plus part-time and full-time dummies** [explicit, p.144]. This is the demand-side reinterpretation of van Soest's hours dummies â€” the foundation for treating my hours-availability terms as structural access rather than fitted taste.
  - *Market / participation:* **explicit** â€” $\theta$ (total job availability), allowed to depend on education and a constant, and linkable to the unemployment rate and business-cycle variation [explicit, pp.141, 143; footnote 12, p.148]. The non-market alternative is the single $z=0$ with $m(0)=1$.
  - *Region / year:* **not modelled** in this paper [not established]. (My access sub-block's regional, urbanisation, and year shifters are beyond it.)
  - *Occupation offers:* **not in the baseline** [explicit, p.144]. The cited two-sector (public/private) extension is institutional, not occupational.
- **ability (wage technology: returns to education/experience, residual productivity).** **Present but outside the opportunity density.** Wages depend on individual **qualifications** through a separately estimated wage equation, with random effects giving a **mixed multinomial logit** that also relaxes IIA (McFadden & Train 2000; used by Dagsvik & StrÃ¸m 2006, Dagsvik & Jia 2012a, Kornstad & Thoresen 2007) [explicit, pp.142, 144]. This is the closest object to my **ability** sub-block, but the paper does **not** fold it into $g$ as a job-availability channel, and does **not** separate ability from access *within* opportunity [explicit + not established]. My ability-in-$g$ design is therefore an **extension beyond** this source.
- **occupation as availability vs. something else.** In the baseline, occupation is **absent** (jobs latent, characteristics suppressed) [explicit, p.144]. In the cited extension it is an **observable sector (public/private)** entering as an additional discrete dimension [explicit, p.144]. **Flag:** their "sector" is an institutional split; it must **not** be mapped to my occupation-as-access (`loc4`, ISCO-type) nor to my reserved industry object (`lindi`, NACE). The paper does **not** conflate occupation with industry â€” it simply does not use either; the conflation risk is on the *reader's* side, not the source's.

**Functional form:** $g(h)$ piecewise-constant with PT/FT peaks; $\log(\theta g(h))$ linear in schooling and PT/FT dummies [explicit, pp.143â€“144]. **Deterministic** in the baseline ("So far we treat the terms $\{m(h)\}$ as deterministic") [explicit, p.140]; the paper *also* offers a **stochastic-choice-set** interpretation (Dagsvik 1994; Dagsvik & StrÃ¸m 2006; Dagsvik & Jia 2006; Dickensâ€“Lundberg) that accommodates unobserved heterogeneity in opportunities [explicit, pp.141â€“142] â€” which I do **not** adopt (my opportunities are deterministic). 

**Cost to my decomposition if the mechanism were omitted:** the source itself states the payoff â€” without an explicit $\log(\theta g(h))$, the PT/FT peaks would have to be absorbed into $v(C,h)+\gamma(h)$ as taste, making the model non-structural and policy simulation uninterpretable [explicit, pp.138â€“139]. That is precisely my motivation for putting access in $g$ rather than letting it masquerade as preference; this paper is the cleanest citation for that argument.

## 6. Welfare object â€” and its place on my $W^1$â€“$W^6$ map

**The paper computes no welfare measure. [explicit / not established]** It motivates structural modelling by noting that counterfactual policy effects "are at the core of discussions on welfare effects of policy changes" [explicit, p.136] and cites Chetty (2009) on sufficient statistics for welfare analysis [explicit, footnote 3, p.148], but it constructs **no** money-metric welfare, **no** equivalent income, **no** compensating/equivalent variation, and **no** inclusive-value welfare object. The only distributional output is a **descriptive** predicted disposable-income distribution for model assessment (Figure 3) [explicit, p.146 [verify]].

**Placement on my $W^1$â€“$W^6$ map:** **N/A.** The source does **not** contain $W^1$â€“$W^6$, does not use Independence-of-$y$ / Independence-of-$A$, and takes no compensationâ€“responsibility stance. Do not attribute any welfare-measure family to it. **Verdict: incompatible as a welfare source** (it is upstream of welfare â€” it supplies the structural utility/opportunity primitives the welfare layer consumes, nothing more).

## 6b. Inclusive value and money-metric inversion  [extract if used]

**Not established as a welfare construction.** The **log-sum denominator** appears in the choice probabilities (eqs. (10)â€“(14)) [explicit], and the expectation over the Gumbel shocks is taken **analytically** (this is what yields the closed-form MNL form) [explicit, by construction]. But the paper never elevates the log-sum to an **inclusive-value welfare** object and never performs a **money-metric inversion** (no one-dimensional solve to a money figure, no EV/CV). So: *analytic-in-shocks* â€” **yes, shared** [explicit, structurally]; *inclusive value as welfare core* â€” **not in this paper** [not established]; *inversion to money* â€” **absent** [not established]. My analytic-in-shocks, importance-sampling inversion shares only the analytic-expectation step with this source.

## 7. Inequality / decomposition content  [three-way where relevant]

**None. [explicit / not established]** No inequality index (no Gini/MLD/Theil/Atkinson), no decomposition rule (no Shapley/Shorrocks/factor/subgroup/RIF), no counterfactual equalisation. The disposable-income *distribution* in Figure 3 is a goodness-of-fit display, not an inequality analysis [explicit, p.146 [verify]]. **Verdict: not reusable for my three-way access/ability/preference Shapleyâ€“Shorrocks split.** The paper is silent on decomposition entirely; it is neither two-way nor three-way. To connect it to my decomposition would require building the entire welfare-and-decomposition layer *on top of* its structural model â€” which is exactly my contribution, not theirs.

## 8. Identification and the separation of preferences from opportunities  [STRICT]

This is the paper's most load-bearing contribution for me.

- **The confounding result [explicit, p.143].** For positive $h$, the choice index contains $\psi(h)+\log g(h)=v(f(hw,I),h)+\log g(h)$. Assuming the offered wage does **not** depend on hours and parameters are constant across the population, Dagsvik & Jia (2012a) show $v(C,h)$ is identified **only up to an additive term $d(h)$ depending on hours** â€” i.e. **preferences and the opportunity distribution are non-parametrically separable only up to an additive function of $h$.**
- **What restores full identification [explicit, p.143].** Either (i) **functional-form assumptions** â€” the Boxâ€“Cox form (eq. (15)), justified on invariance-principle grounds (Dagsvik & RÃ¸ine Hoff 2011; Dagsvik 2012), under which the model is identified; or (ii) **data on desired/preferred hours** (Euwals & van Soest 1999; Bloemen 2008).
- **Policy-simulation escape clause [explicit, p.143].** For counterfactuals that only change the budget $f$, one need **not** separate the hours-utility term from $g(h)$, because neither depends on $f$. (This does *not* help me: my decomposition *requires* the separation, since I equalise channels.)
- **Ability vs. access within opportunity:** **not addressed [not established].** The paper's identification argument is **preference vs. (hours) opportunity** only. It offers **no** argument separating a wage/ability sub-block from an access sub-block inside $g$. My three-way cut's ability/access boundary therefore cannot be supported by this paper; it rests on my own functional-form-plus-channel-assignment, and is exactly the part a "your decomposition is mechanical" referee will press.
- **Transport to my France pooled cross-section.** The functional-form route (i) **transports** â€” it is precisely my strategy (Boxâ€“Cox preferences). The desired-hours route (ii) does **not** â€” I have no desired-hours data. The paper's *assessment* standard is **out-of-sample prediction across a tax reform**, **not synthetic recovery** [explicit, pp.144â€“145]; so this paper does **not** license my synthetic-recovery certification â€” I must cite it for the *identification logic* (separation is parametric, not nonparametric) and source the recovery-as-evidence standard elsewhere. Honest net statement: **Dagsvik et al. establishes that preference/opportunity separation in latent-jobs models is inherently parametric and defensible on functional-form grounds; it does not, and cannot, certify the finer ability/access separation my decomposition needs.**

## 9. Key results and magnitudes

The paper reports **no estimated parameters of its own**; magnitudes are illustrative or borrowed.

- **Wage elasticities (borrowed from Dagsvik & Jia 2012a):** "of moderate magnitude, with married females more responsive than males," broadly in line with the literature; **no numerical values given here** [explicit, p.146]. The discrete-choice literature (including theirs) typically reports **gross** (pre-tax) wage elasticities, unlike the Hausman-type post-tax convention [explicit, p.146].
- **Illustrative logit elasticity arithmetic [explicit, p.147]:** for $P(w,X)=1/(1+\exp(-\alpha\log w - X\beta))$, the participation wage elasticity is $(1-P)\alpha$; at $P=0.6$ it is $0.4\alpha$, at $P=0.8$ it is $0.2\alpha$. This is a pedagogical point that **nonlinear models yield sample-dependent elasticities**, not an estimate.
- **Out-of-sample fit (Norway):** the 2006 tax reform cut the top marginal rate from **55.3% to 47.8%** [explicit, p.144]; the model's predicted **female** hours distribution for 2006 tracks the actual better than the 1997 baseline, while **male** responses are not well reproduced [explicit, pp.144â€“145]; the 2003 predicted disposable-income distribution matches the data closely [explicit, p.145].
- **Benchmarking value for me:** "females more responsive than males, both moderate" is a sanity band for my own elasticities **if** I compute them (currently deferred); there are **no opportunity-share or welfare-spread magnitudes** here to benchmark my decomposition against.

## 10. Estimators, theorems, or formal results

No numbered theorems. The reusable formal objects are the choice-probability derivations and the functional form.

1. **Latent-jobs choice probability (eq. (14)) [explicit, p.141].**
   $$\varphi(h)=\frac{\exp\!\big(\psi(h)+\log(\theta g(h))\big)}{\exp(\psi(0))+\sum_{x\in D}\exp\!\big(\psi(x)+\log(\theta g(x))\big)}.$$
   - Assumptions: iid Gumbel shocks $\varepsilon(z)$; $v(C,h)+\varepsilon(z)$ utility; fixed-hours jobs; $m(h)$ deterministic (baseline).
   - Technique: McFadden RUM â†’ MNL; sum over $z\in B(h)$ collapses the job-level probability (eq. (9)) into the hours-level probability via the multiplicity $m(h)$; $\{m(h)\}$ are sufficient statistics for the latent sets.
   - **Reusability: yes** â€” this *is* the structural form of my per-alternative value, minus the $-\log\pi$ sampling correction my pipeline adds.
2. **Boxâ€“Cox systematic utility (eq. (15)) [explicit, p.143].**
   $$v(C,h)=\gamma\frac{C^{\alpha}-1}{\alpha}+\delta\frac{(M-h)^{\beta}-1}{\beta}+\mu\frac{(C^{\alpha}-1)\big((M-h)^{\beta}-1\big)}{\alpha\beta}.$$
   - Assumptions: $\alpha<1,\beta<1,\gamma>0,\delta>0$, $\mu$ constrained â†’ strict concavity; $M$ = maximum feasible hours.
   - Technique: derived from qualitative-measurement / invariance axioms (Dagsvik & RÃ¸ine Hoff 2011; Dagsvik 2012); under it the model is identified.
   - **Reusability: yes** â€” same preference family as my utility block (consumption, leisure, interaction). Note my baseline carries demographic taste-shifters and gender that this generic form does not write out.
3. **Identification-up-to-$d(h)$ result [explicit, p.143].** Statement and assumptions as in Â§8. **Reusability: yes, as a cited identification primitive** for the preference/opportunity separation; **no** for ability/access separation.

## 11. Robustness and specification sensitivity

- **Boxâ€“Cox vs. quadratic [explicit, p.143]:** Boxâ€“Cox yields roughly the same fit as quadratic; quadratic can fail to be increasing in leisure; Boxâ€“Cox is harder to estimate (nonlinear in parameters). **Mastrogiacomo et al. (2011)** report estimation difficulties; **Blundell & Shepard (2012)** obtained an unacceptable estimate of one Boxâ€“Cox parameter. â†’ A direct warning for my own Boxâ€“Cox estimation; relevant to my pinned/at-bound parameters.
- **Number of discrete alternatives [explicit, pp.139, 144]:** discretisation is argued inessential and arbitrarily refinable; the discrete setting may even be the "true" one. â†’ Supports my fixed-resolution grids as defensible, not a mere approximation.
- **IIA relaxation [explicit, pp.142]:** nested MNL, random effects, or a random-effects wage equation (mixed MNL) relax IIA without ad hoc terms. â†’ Optionality for my robustness, though my baseline does not need it.
- **Elasticities sample-dependent in nonlinear models [explicit, pp.146â€“147].** â†’ Caution for any elasticity reporting I add.
- **Model assessment = out-of-sample prediction [explicit, pp.144â€“145].** Their stress test is predicting a different year / a reform, **not** synthetic recovery. â†’ My recovery-based certification is a *different* (and, for my no-reform setting, more available) standard; cite this for the limits of in-sample fit, not for recovery.

## 12. What I can cite this paper for

- That the conventional discrete-choice (van Soest) model's PT/FT **dummies can be reinterpreted as a structural opportunity term** $\log(\theta g(h))$ arising from demand-side job availability â€” the foundation for treating my access terms as structural rather than as fitted taste [pp.138â€“141].
- The **definitions** of the opportunity measure $\theta g(h)$ and opportunity distribution $g(h)$, with $\theta$ as total job availability (education-dependent, unemployment-linked) [pp.140â€“141].
- The **identification result** that preferences and the opportunity distribution separate only up to an additive $d(h)$ absent functional-form or desired-hours information, hence that **the separation is parametric** [p.143].
- That **Boxâ€“Cox** preferences are the invariance-justified, identification-securing functional form for this class of models [p.143].
- That the latent-jobs model **rationalises hours peaks structurally** and thereby keeps counterfactual simulation interpretable, where dummy-augmented conventional models do not [pp.138â€“139].
- That a **reduced-form** opportunity measure has an **equilibrium (two-sided matching)** foundation [p.142].
- General methodological cautions: Boxâ€“Cox estimation fragility; nonlinear elasticity sample-dependence; discretisation as inessential [pp.143, 146â€“147].

## 13. What I should NOT cite this paper for  [overclaim risks]

- **Any welfare measure.** It computes none; do **not** cite it for money-metric welfare, equivalent income, EV/CV, or inclusive-value welfare. **It does not contain $W^1$â€“$W^6$** or any compensationâ€“responsibility / Independence-of-$y$ / Independence-of-$A$ framing.
- **Any decomposition.** No inequality index, no Shapley/Shorrocks, no opportunity-vs-preference split â€” and certainly no **three-way access/ability/preference** split. Citing it for a decomposition (even two-way) would be an overclaim.
- **Ability/access separation within opportunity.** Its identification logic is preference-vs-(hours-)opportunity only. Do not read it as licensing my ability/access cut.
- **Occupation/sector language.** Its only occupational object is a cited **public/private institutional sector** extension. Do **not** present this as my **occupation-as-access** (`loc4`/ISCO), and do **not** let it drift into **industry** (`lindi`/NACE) language. The paper does not conflate the two; I must not introduce the conflation.
- **Random vs. deterministic opportunities.** The paper offers a **stochastic-choice-set** interpretation alongside the deterministic baseline. Map only the **deterministic** reading to my design; do not import the random-choice-set framing.
- **Synthetic-recovery certification.** Its assessment standard is out-of-sample prediction, not parameter recovery. Do not cite it as precedent for my recovery gate.
- **Theory-paper boundary.** This is empirical-methods literature; it has no bearing on the companion Haydarâ€“Maniquet axiomatic paper. Do not let any of its content migrate into the theory paper's territory, and do not read the JMP as a theory contribution because it cites this.

## 14. Direct quotes worth citing

To respect copyright I reproduce one short verbatim phrase and give page-anchored pointers for the rest (pull exact wording directly from the PDF at these locations):

- p.141, defining the central object (verbatim): "We shall call Î¸g(h) the opportunity measure and g(h) the opportunity distribution."
- p.141 [pointer]: the sentence stating that $\log g(h)+\log\theta$ in eq. (14) is an explicit representation of demand-side choice restrictions, no longer an ad hoc addition.
- p.143 [pointer]: the sentence stating preferences and the opportunity distribution can be separated only up to an additive term depending on $h$.
- p.143 [pointer]: the sentence that full identification requires functional-form assumptions (or desired-hours data).
- p.144 [pointer]: the sentence stating that in this version jobs are latent and job characteristics do not appear, with the public/private two-sector extension referenced to Dagsvik & StrÃ¸m (2006).
- p.140 [pointer]: the sentence treating $\{m(h)\}$ as deterministic ("So far we treat the terms $\{m(h)\}$ as deterministic").

## 15. Open questions and risks for my draft

- **The parametric-separation risk is inherited, not solved.** The paper is candid that separation rests on functional form; my decomposition inherits this, and the referee point ("the access/preference split is a functional-form artefact") is *not* answered by citing Dagsvik â€” it is *named* by it. My synthetic-recovery evidence is the load-bearing answer, and this paper does not supply it.
- **Ability/access has no identification anchor here.** My finer cut needs its own defence (channel assignment as an explicit normative-cum-functional assumption); I cannot lean on this source for it.
- **Validation-standard mismatch.** Their out-of-sample/reform standard is unavailable to me (no exploited reform, no panel); I must justify recovery-based certification on its own terms.
- **No welfare/decomposition scaffolding to borrow.** Everything downstream of the structural model â€” the inclusive-value welfare inversion, the $-\log\pi$ welfare integrator, the Shapley split â€” is mine to build; this paper ends exactly where my contribution begins.
- **Wage/ability modelling choice.** They keep wages in a separate qualifications equation (job-invariant in the baseline). My decision to carry wage returns *inside* $g$ as an ability channel is a deliberate departure I should flag against this baseline, citing Dagsvik & Jia (2012a)'s job-specific-wage general case as the closer precedent.

## 16. TL;DR for retrieval

Dagsvikâ€“Jiaâ€“Kornstadâ€“Thoresen (2014) is the programmatic survey that reinterprets van Soest's ad hoc hours dummies as a **structural opportunity term** $\log(\theta g(h))$ â€” supplying the foundation and citation for my **access** channel (hours availability $g(h)$, total job availability $\theta$) and for the **preference-vs-opportunity identification** result (separable only up to an additive $d(h)$ absent Boxâ€“Cox functional form or desired-hours data). It treats **ability** only as a separate qualifications-based wage equation (not an opportunity-density channel), keeps occupation latent (with a cited public/private *sector* extension that is neither my ISCO occupation nor NACE industry), and contains **no welfare measure, no $W^1$â€“$W^6$, and no decomposition** â€” it is strictly upstream of my welfare/decomposition layers and informs only my estimation and identification prose.
# Dagsvik & Jia 2016 â€” Labor Supply as a Choice Among Latent Jobs: Unobserved Heterogeneity and Identification

> Source of truth: the attached JSTOR PDF (J. Appl. Econ. 31(3): 487â€“506). The companion
> `.md` was used only for navigation. Page numbers refer to the journal pagination (487â€“506).
> Tags used below: **[explicit]** = stated in the paper; **[analogy]** = derived by mapping
> to my design, not asserted by the paper; **[not-established]** = the paper does not do this;
> **[verify]** = could not be confirmed from the provided PDF body (e.g. supplementary-appendix
> material).

---

## 0. Metadata

- **BibTeX key:** `dagsvik_jia_2016_latent_jobs`
- **Authors:** John K. Dagsvik (Statistics Norway; Frisch Centre); Zhiyang Jia (Statistics Norway).
- **Year:** 2016 (published online 6 January 2015; received 1 Oct 2012, revised 23 Sep 2014). [explicit, p.487]
- **Outlet:** *Journal of Applied Econometrics*, Vol. 31, No. 3, pp. 487â€“506. [explicit, p.487]
- **DOI / URL:** DOI 10.1002/jae.2428; JSTOR stable URL `https://www.jstor.org/stable/10.2307/26609622`. [explicit, p.487]
- **PDF filename:** `Dagsvik_and_Jia_-_2016_-_Labor_Supply_as_a_Choice_Among_Latent_Jobs...pdf`
- **Tier:** **T1A** (core â€” the canonical identification statement of the RURO/latent-jobs framework my estimation layer instantiates).
- **JMP blocks served:** **identification** (primary); **estimation**; **opportunity-mechanism (access + ability)**; **motivation**. It does **not** serve welfare, decomposition, or normative-interpretation directly.

---

## 1. One-paragraph relevance to my JMP

This is the foundational identification paper for the exact structural object my estimation layer instantiates: a choice probability that factorises into a deterministic preference utility $v(C,h)$ and an *opportunity measure* $\theta\,g_1(h)\,g_2(w\mid h)$ over latent jobs. [explicit, pp.489â€“490] It is the paper that establishes â€” formally, on cross-section data â€” *when* preferences can be separated from the opportunity mechanism, which is precisely the separation my access/ability/preference decomposition presupposes; without that separation the decomposition is mechanical, and this paper is my primary defence on that point. [explicit, Â§3, pp.492â€“494] It speaks directly to **two of my three channels**: the wage sub-block $g_2(w\mid h)$ and its individual-ability random effect $\eta$ map to my **ability** channel, and the hours/availability objects $g_1(h)$ and $\theta$ map to my **access** channel. [explicit for the objects, pp.489â€“491; channel-naming is [analogy]] It does **not** compute welfare, an inclusive-value welfare core, or any inequality decomposition, and it contains nothing resembling my $W^1$â€“$W^6$ family; it is upstream machinery, not a welfare or decomposition source. [not-established]

---

## 2. Data and setting

- **Country / year:** Norway, single cross-section, **Norwegian Labor Survey 1997**. [explicit, p.495]
- **Dataset / unit:** Married/cohabiting **couples**; the labour-supply model is a **joint** couple decision. [explicit, pp.487, 495]
- **Sample size:** Table I reports household counts by employment configuration â€” both spouses working **2,254**; only husband working **256**; only wife working **5** (no "neither working" row is shown in the table). [explicit, p.495] Total over the listed cells $\approx 2{,}515$ couples; whether a non-working-couple cell exists is [verify] (not shown in the provided body).
- **Key variables:** age, length of schooling (education), potential experience ($=$ age $-$ schooling $-7$), non-labour income, gross hourly wage rate, weekly hours of work, number of children (0â€“6 and 7â€“18). [explicit, Table I, p.495]
- **Budget-set construction:** disposable income via a net-of-tax function $C=f(hw,I)$, with $I$ non-labour income; $f$ is stated to be able in principle to capture the full tax/benefit system. [explicit, p.489]
- **Transport to my France pooled 2015â€“2017 EUROMOD cross-section:** *Partial.* The structural form transports cleanly (cross-section, discrete latent-jobs couples, parametric Boxâ€“Cox utility, opportunity density). What I have that they do not: an explicit microsimulated budget (EUROMOD `ils_dispy`) rather than an estimated net-of-tax function; pooled multiple waves (they have one year). What they have/use that bears on me: a **three-stage wage-equation estimation** to handle measurement error in hours ("division bias"), because they observe weekly hours only and infer the wage by division. [explicit, pp.495â€“496] **Features I do NOT have, named explicitly:** no panel, no administrative match, no external opportunity instrument, no vacancy/offer data â€” and the paper itself states that even panel or independent cross-sections do not, in general, solve the identification problem. [explicit, p.492]

---

## 3. Model and objects (object-by-object map to mine)

| Their object | Mine | Match? | Note |
|---|---|---|---|
| Latent job "packages" $(H(z),W(z),\text{attributes})$, worker-specific unobserved choice set | latent-jobs set $\mathcal C_i$ | **Yes** [explicit, pp.487â€“489] | Theirs is conceptually infinite (Poisson-scattered); mine is a finite sampled grid (singles 101, couples 901). |
| Deterministic utility $v(C,h)$, Boxâ€“Cox | preference utility $v_i(c,\ell)$, Boxâ€“Cox | **Yes** [explicit, eq.(8), p.493] | Both Boxâ€“Cox in consumption and leisure; globally concave. Theirs is over $C$ and $(1-h/M)$. |
| Opportunity measure $\theta\,g_1(h)\,g_2(w\mid h)$ | opportunity density $g(j;x_i)$ | **Yes** [explicit, p.489] | This is the central shared object; see Â§5. |
| $g_1(h)$ â€” offered-hours density | **access** (hours availability) | **Yes** [explicit] | Their $g_1$ is uniform with peaks at PT/FT. |
| $g_2(w\mid h)$, wage equation, random effect $\eta$ | **ability** (wage technology + residual $\sigma$) | **Yes** [explicit eq.(4),(9); channel name [analogy]] | $\eta$ is explicitly called individual *ability* (p.494). |
| $\theta$ â€” job-availability scalar (ratio of market to non-market opportunities) | **market/participation** availability term ($\log\text{market}$) | **Partial** [explicit p.489; mapping [analogy]] | $\theta$ also absorbs psychic cost of working ($\theta<1$). |
| Market vs non-market opportunities ($z>0$ / $z<0$) | market/participation channel | **Yes** [explicit, p.488] | The participation margin is a market-vs-non-market split. |
| Budget $C=f(hw,I)$ | EUROMOD `ils_dispy` | **Analogous** [explicit] | Their estimated net-of-tax function â†” my microsimulated income. |
| **Occupation / sector** | my `loc4` access object | **Absent in the estimated model** | See flag below. |

**Flag â€” occupation/sector.** The estimated empirical model contains **no occupation and no sector variable.** [explicit] The paper uses "sector" to mean *labour-market sector* (e.g. public health care, teaching) and invokes it only as informal *explanation* for gendered hours peaks, plus a footnote that a sector-specific model (as in Dagsvik & StrÃ¸m 2006) *could* yield explicit sector-specific opportunity measures. [explicit, p.497 fn.9; p.501] Two consequences for me: (i) this paper is **not** a precedent for an occupation-as-access layer being estimated â€” it is a precedent only for the *idea* that sector/occupation belongs in the opportunity measure if added; (ii) their "sector" language is closer to industry than to my ISCO-type `loc4` task categories, so I must not cite it as support for `loc4`-as-occupation, and must keep my `loc4`/`lindi` discipline intact when citing.

**Flag â€” does any attribute enter BOTH utility and opportunity?** **No.** [explicit] The wage and hours enter the opportunity measure $g_2(w\mid h)g_1(h)$ and enter utility only through $C=f(hw,I)$ and through $h$; the wage technology / ability is purely in the opportunity side, never in $v$. Crucially, **non-labour income $I$ enters only through consumption and does not affect the opportunity measure** â€” this exclusion is the load-bearing identification device (Assumption 3 / Theorem 2). [explicit, pp.492â€“493] This is consistent with my design (occupation and the wage return live in $g$ only, never in $v$).

---

## 4. Estimation method

- **Likelihood / estimator:** maximum likelihood on the closed-form choice probabilities (2a,b)/(3a,b). [explicit, p.496]
- **Choice-set construction:** a **fixed grid** of eight feasible annual hours per spouse â€” $\{0,\,208,\,624,\,1040,\,1456,\,1950,\,2340,\,2600\}$ â€” with the offered-wage dimension handled by **integration/summation** over the wage density, not by a sampled-alternative draw. [explicit, p.495] This is *full enumeration over a small grid*, **not** McFadden sampling-of-alternatives.
- **Proposal / sampling density:** **none** â€” there is no importance-sampling proposal because alternatives are enumerated; see Â§4b.
- **Prior/proposal correction ($-\log\pi$):** **absent**, by construction (no sampling). [explicit by absence] The opportunity density $g$ enters the likelihood as a *structural weight* on each enumerated alternative, not as a nuisance correction. This is the key contrast with my pipeline (see Â§4b).
- **Normalisation / scale:** $C_0$ is a known subsistence-consumption constant; $\theta$ enters multiplicatively on $v$, so it also soaks up the psychic cost of working (rationalising $\theta<1$). [explicit, pp.489â€“490] $\delta(h)$ / $g_1(h)$ separation is left unidentified for pure tax/wage simulation (kept fixed); see Â§8.
- **Division-bias handling (their numerical method of substance):** a **three-stage procedure** (after Dagsvik & StrÃ¸m 2004, 2006): (1) reduced-form participation probability; (2) wage-rate equations estimated with a selectivity correction using stage-1 results; (3) ML on the labour-supply model with stage-2 predicted wages inserted and the wage-equation errors integrated out. [explicit, p.496] Selection bias in the wage equations is reported negligible. [explicit, p.496]
- **Starting values / multistart:** not described in the provided body. [verify]
- **What pins preferences apart from opportunity:** the exclusion restriction on $I$, a parametric functional form (Boxâ€“Cox), and a normalisation on the offered-hours density (two hours points with equal $g_1$). [explicit, Assumptions 3, 5, 6; Theorem 4, p.493] â€” see Â§8.
- **Verdict â€” reusable for my RURO/JAX pipeline?** **Yes, structurally â€” with one decisive difference.** The likelihood object (utility $\times$ opportunity density, normalised over alternatives) is exactly mine. *Difference:* they **enumerate** a small grid and **integrate** the wage; I **sample** alternatives and therefore must carry the $-\log\pi$ correction that they do not need. Reuse the *factorisation and the role of $g$ as a structural weight*; do **not** import their estimation as evidence that a sampling correction is unnecessary â€” that is an artefact of enumeration. Their three-stage wage procedure is an alternative to my single-stage approach worth citing as a measurement-error precedent, not adopting.

---

## 4b. Proposal / sampling-of-alternatives correction  [extract even if brief]

**The paper has no sampling-of-alternatives step and therefore no McFadden-style proposal correction.** [explicit by construction] Alternatives are the eight fixed hours points; the offered-wage distribution is integrated analytically/numerically. The object that *plays the role* of a per-alternative weight is the **structural opportunity density** $\theta g_1(h)g_2(w\mid h)$ itself â€” but this is a structural primitive, not a nuisance proposal to be divided out. [explicit, pp.489â€“490]

Mapping to my concerns:
- **My $-\log\pi$** is a sampling nuisance correction; **their $g$-terms** ($\log g_1+\log g_2+\log\theta$) are the *structural* analogues of my $\log h_{ij}+\log w_{ij}+\log\text{market}_{ij}$. The clean lesson: when I sample, I must *both* keep the structural $g$-logs *and* subtract $\log\pi$; this paper isolates the structural logs in their pure (un-sampled) form, which is useful for verifying that my structural terms are specified correctly independent of the sampling correction. [analogy]
- **Proposal individualisation.** They consider $g_2(w\mid h;\eta)$ depending on individual covariates and a random effect $\eta$ (i.e. the wage channel is individual-specific), while keeping $g_1(h)$ common across observationally identical agents on the stated ground that hours restrictions are institutionally (union/negotiation) determined and not individual. [explicit, pp.490â€“491] This is a near-exact precedent for my proposal-individualisation split â€” **wage individualised, hours/employment common** â€” and I can cite it for that design choice. [explicit for their structural choice; my proposal-instrument analogy is [analogy]]

---

## 5. Opportunity mechanism  [MOST IMPORTANT â€” split by channel]

**Form.** The available jobs are a realisation of a **Poisson process** of taste shifters $\{\varepsilon(z)\}$ scattered on $(0,\infty)$ with non-homogeneous intensity $\propto \varepsilon^{-2}$ (market intensity scaled by $\theta$, non-market by $1$), with offered $(H(z),W(z))$ drawn independently on $D\times(0,\infty)$ according to $g_1(h)g_2(w\mid h)$. [explicit, Assumption 2, p.489] Dagsvik (1994) showed this $\varepsilon^{-2}$ intensity is the form required for the resulting job choice to satisfy IIA. [explicit, pp.489â€“490] The realised choice probability collapses to the closed form in Theorem 1 (eq. 2a,b): for $h>0$,
$$
\varphi(h,w\mid I)\;=\;\frac{v\big(f(hw,I),h\big)\,\theta\,g_1(h)\,g_2(w\mid h)}{v\big(f(0,I),0\big)\;+\;\theta\sum_{r\in D}\int_0^\infty v\big(f(ry,I),r\big)\,g_1(r)\,g_2(y\mid r)\,dy},
$$
with $\varphi(0,0\mid I)$ the no-work probability (numerator $v(f(0,I),0)$). [explicit, eq.(2a,b), p.490] When wages carry an individual random effect $\eta$, the probability is the same expression with $\theta(\eta)g_2(w\mid h;\eta)$ and an expectation $E_\eta[\cdot]$ taken over $\eta$, which **breaks IIA**. [explicit, eq.(3a,b), p.491]

**Channel map (the core of why this paper matters to me):**

- **ACCESS** = $g_1(h)$ and $\theta$.
  - $g_1(h)$ is the probability that a job with hours $h$ is available; empirically specified **uniform with peaks at part-time (1040 h/yr) and full-time (1950 h/yr)**, motivated as institutional hours regulation. [explicit, pp.489, 495] The paper notes this is *formally equivalent* to van Soest-style PT/FT dummies but with a structural (opportunity) rather than preference interpretation. [explicit, p.495]
  - $\theta$ ("job availability") is the ratio of available market to non-market opportunities; $\log\theta$ is specified **linear in length of schooling**; estimated $\theta<1$ for both genders; $\theta_F$ increases with schooling, $\theta_M$ not significant. [explicit, pp.489, 495, 497]
  - **What they do NOT have in access that I have:** region, urbanisation, year, and occupation offer shifters. Their access channel is hours-availability $+$ a schooling-shifted scalar $\theta$ only. [explicit by absence]
- **ABILITY** = the wage technology $g_2(w\mid h)$ and its random effect.
  - Offered log-wage equation $\log W(z)=\alpha+\psi(H(z))+\eta+\xi(z)$ [eq.(4)], with $\alpha$ a function of schooling, experience, experience$^2$, and a marriage dummy. [explicit, eq.(4) p.491; spec p.496]
  - The random effect $\eta$ (Model 2) is **explicitly interpreted as individual ability** affecting the opportunity measure: "$a+Xb+\eta$ â€¦ represent[s] the effect of observed and unobserved individual ability." [explicit, p.494]
  - $\xi(z)$ (Model 1) is *across-job* wage variation for a given agent. The two models are the two "extreme" stances: Model 1 = wage varies across jobs only ($\eta=0$); Model 2 = each agent faces one wage that varies across agents ($\xi=0$). [explicit, p.496]
  - This is a direct precedent for my ability sub-block (returns to education/experience $+$ residual dispersion $\sigma$). My $\sigma$ corresponds to their wage-equation residual variance (var of $\xi$ in M1, var of $\eta$ in M2). [explicit for theirs; correspondence [analogy]]
- **MARKET/PARTICIPATION** = the market-vs-non-market opportunity split and $\theta$. [explicit, pp.488â€“490]
- **OCCUPATION** = **not modelled** in the estimated opportunity mechanism; only referenced as a possible sector-specific extension. [explicit, p.497 fn.9] **No sector/industry conflation to flag in their estimation** because they estimate no such variable; but note their *informal* "sector" usage means industry-flavoured labour-market sectors, not my ISCO `loc4`.

**Does it vary with circumstances?** Yes, but narrowly: $\theta$ varies with schooling, and $g_2$ varies with schooling/experience and (in M2) with individual ability $\eta$; $g_1(h)$ is deliberately held common across observationally identical agents (institutional hours). [explicit, pp.490â€“491, 495]

**Cost of the omissions for my decomposition.** Because their access channel lacks region/urbanisation/year/occupation, their estimated "opportunity" is thinner than mine; their paper cannot, and does not, decompose welfare by access vs ability. I should cite it for the *existence and identification* of the access (hours, $\theta$) and ability (wage-$\eta$) sub-objects, not for any quantification of an access/ability split.

---

## 6. Welfare object â€” and its place on my $W^1$â€“$W^6$ map

**The paper computes no welfare object.** [not-established] It produces choice probabilities, expected hours ("labour supply curves"), wage elasticities, and a policy simulation of a change in the hours-opportunity distribution. There is **no money-metric welfare, no equivalent income, no compensating/equivalent variation, no inclusive-value welfare core, and no reference price/preference/bundle/set** in the sense my welfare layer requires. [not-established]

- It does **not** place anywhere on my $W^1$â€“$W^6$ family; **do not cite this paper as containing or supporting any $W^k$ measure.** Its closest relative â€” welfare effects of tax reforms â€” appears only in a *cited* reference (Aaberge, Dagsvik & StrÃ¸m 1995), not in this paper. [explicit, references p.502]
- The one welfare-adjacent operation is the **policy simulation** (Â§4.3, Appendix B): changing $g_1$ by removing the part-time peak and raising the full-time peak with $\theta_F$ fixed, then recomputing the realised labour-supply distribution. [explicit, pp.500â€“501, 505â€“506] This is a *behavioural* counterfactual on the opportunity density, not a welfare evaluation. It is, however, a clean precedent for the kind of access-shift counterfactual my decomposition equalises. [analogy]
- **Verdict:** **incompatible as a welfare source**; usable only as the structural-estimation foundation on which a welfare layer (mine) is later built. The welfare construction is entirely my (and the equivalent-income literature's) addition.

---

## 6b. Inclusive value and money-metric inversion  [extract if used]

**Not used.** [not-established] The paper does not use the log-sum / inclusive value as a welfare core and performs no money-metric inversion. The expectation over the extreme-value-type taste shifters is handled *analytically* in deriving the closed-form choice probabilities (Theorem 1), and the unobserved wage effect $\eta$ is integrated out (by simulation/numerical integration over $g_\eta$). [explicit, pp.490â€“491] So there is an analytic-in-taste-shocks derivation I can point to as the antecedent of my analytic-in-shocks log-sum â€” but the paper stops at choice probabilities and expected hours; it never forms a welfare inclusive value or inverts utility to money. My analytic-in-shocks importance-sampling inversion is my own construction, consistent in spirit but not present here.

---

## 7. Inequality / decomposition content  [three-way where relevant]

**None.** [not-established] No inequality index (Gini/MLD/Theil/Atkinson), no decomposition (Shapley/Shorrocks/factor/subgroup/RIF), no counterfactual equalisation of a distribution. The closest object is the *behavioural* hours-distribution simulation (Â§7-adjacent), which equalises nothing in a welfare sense. **It cannot be cited as a precedent for my three-way access/ability/preference Shapleyâ€“Shorrocks split.** To be extended to my decomposition it would need: (i) a welfare object built on top (the inclusive-value money metric); (ii) an inequality index over households; (iii) a Shapley equalisation protocol over the estimated $g$/$v$ blocks. All three are absent.

---

## 8. Identification and the separation of preferences from opportunities  [STRICT â€” the backbone]

This is the paper's central contribution and my primary identification citation. The problem is stated exactly as mine: observed behaviour reflects **both** preferences $v(C,h)$ **and** latent choice constraints (the opportunity measure $\theta g_1 g_2$), so standard multinomial/mixed-logit identification does **not** apply. [explicit, pp.492, 501] The results, in order:

- **Non-parametric ratio is identified, the split is not (Theorem 1 corollary).** $\varphi(h,w\mid I)/\varphi(0,0\mid I)=v(f(hw,I),h)\,\theta g_1(h)g_2(w\mid h)/v(f(0,I),0)$ is observable, but $v$ and $\theta g_1 g_2$ are not separately recoverable from it. [explicit, eq.(7), p.492]
- **Exclusion restriction (Assumption 3).** $v(C,h)$ is smooth and $I$ enters **only through consumption**, not the opportunity measure â€” i.e. non-labour income shifts $C$ while holding hours and wage fixed. [explicit, pp.492â€“493] This is the key economic exclusion; my analogue is that EUROMOD non-labour income enters only $c$, not $g$.
- **Theorem 2 (non-identification under exclusion alone).** Even with Assumption 3, the model is **non-parametrically unidentified**: $v(C,h)=\zeta(C)^{r}\lambda^{*}(C,h)\,\delta(h)$ with $\zeta,\lambda^{*}$ identified but $r$ an unknown constant and $\delta(h)$ an unknown function of hours. [explicit, p.493]
- **Theorem 3 (Assumption 4: offered wages âŸ‚ offered hours).** The offered-hours distribution is identified and $v(C,h)=\lambda(C,h)\delta(h)$ with $\lambda$ identified, **$\delta(h)$ still not**. For pure tax/wage counterfactuals one need not separate $\delta(h)$ from $g_1(h)$ as long as $g_1$ is held fixed. [explicit, pp.493] â€” *Important caveat for me: this "don't need to separate" licence applies to behavioural tax simulation, NOT to a welfare decomposition that attributes inequality to access vs preference; my object requires the separation their tax-simulation can dodge.*
- **Theorem 4 (full identification via functional form).** Under Assumptions 1â€“3, 5, 6 â€” a generalized **Boxâ€“Cox** $\log v$ (eq.8) plus a normalisation that two distinct hours points share the same offered-hours probability, $g_1(h_1)=g_1(h_2)$ â€” model (2a,b) is **identified**. [explicit, p.493] **This is parametric identification: the separation is bought with functional form + a normalisation, not with an instrument or panel.**
- **Theorem 5 (identification with a wage random effect / ability).** With unobserved wage heterogeneity (model 3a,b), identification needs an **exogenous covariate $X$ that affects the opportunity density / offered wage but not preferences** (Assumption 7: $\log W(z)=Xb+a+\eta+\xi(z)$, with $\theta$ constant or $\theta(a+Xb+\eta)$). Then $v$ is identified up to a multiplicative $h$-term, $\theta(\cdot)$ up to a constant, and the conditional offered-wage distribution is identified; adding Boxâ€“Cox (Assumption 6) gives full identification. [explicit, pp.494]

**Transport to my France pooled cross-section (honest assessment).**
- Their cross-section + Boxâ€“Cox + exclusion-of-$I$ + hours-normalisation route (**Theorem 4**) transports directly to me: I too rely on parametric Boxâ€“Cox and on non-labour income entering only consumption. My certification by **synthetic recovery** is the right standard precisely because identification here is *parametric*, not design-based â€” recovery on simulated data is the test of whether the functional-form identification actually bites at my sample size. [analogy; consistent with project state Â§3.6/Â§8]
- Their random-wage-effect route (**Theorem 5**) requires an **exogenous wage/opportunity shifter $X$ excluded from preferences**. My ability sub-block uses education and experience as the wage technology; for the Theorem-5 logic to support separating my ability channel, those must be credibly excluded from $v$ â€” which is exactly my design (education/experience are in $g$, not $v$). But I have **no external instrument** beyond functional form, and the paper is explicit that **panel or repeated cross-sections do not in general rescue identification** (only changes in the opportunity measure, not its level, become non-parametrically identifiable under fixed preferences). [explicit, p.492] So I cannot lean on my pooling of 2015â€“2017 as an identification gain; it is a precision/clustering matter, not an identification one.
- **Referee defence ("your decomposition is mechanical").** Cite Theorems 2â€“5 to establish that (a) the separation is a *known hard problem*, (b) it is *achievable* under stated parametric assumptions I satisfy, and (c) the honest standard is recovery under those assumptions â€” which is why I certify by synthetic recovery rather than in-sample fit. **Do not soften:** the identification is parametric and rests on the exclusion of $I$ from $g$, the exclusion of the wage shifter from $v$, the Boxâ€“Cox form, and an offered-hours normalisation.

---

## 9. Key results and magnitudes

All from the Norway 1997 married-couples sample; "M2" = their maintained Model 2 (individual wage heterogeneity).

- **Model selection.** Log-likelihood values $\approx 5309$ (M1) and $5243$ (M2) [sign reported as printed; magnitude is the likelihood-function value â€” [verify] sign]. McFadden $\rho^2 = 0.49$ (M1), $0.50$ (M2). [explicit, p.497]
- **Andrews $\chi^2$ goodness-of-fit (5 d.f., 6 cells):** M1 $=57.6$ (fails), M2 $=10.4$ (passes; 5% critical $=11.07$). M2 selected as maintained model. [explicit, pp.497â€“498]
- **Wage elasticities (aggregated, M2; Table II, p.499):**
  - Own-wage elasticity of the **probability of working, married women** $=0.333$ (text rounds to $0.33$); a 5% female wage rise raises the female participation share by $\approx 1.5\%$. [explicit, pp.499, 502/p.14 text]
  - Probability of working, **married men**: very small, $\approx 0.007$ (own), $0.010$ (men's wage). [explicit, Table II]
  - **Unconditional hours elasticity, women** $=0.618$ (M2, own-wage); **men** $\approx 0.022$ (own) to $0.080$ (men's wage). [explicit, Table II]
  - Cross-wage elasticity for women is **negative** and smaller than own-wage. Both-spouses-wage elasticity of female participation $=0.205$ (M2). [explicit, Table II; p.499]
- **Opportunity findings.** $\theta<1$ for both genders (interpreted as fewer interesting available jobs than non-market opportunities, and/or psychic cost of work). $\theta_F$ rises with schooling; $\theta_M$ insignificant. Number of children significantly raises women's marginal utility of leisure, not men's. [explicit, p.497]
- **Policy simulation.** Removing the female part-time peak and raising the full-time peak (with $\theta_F$ fixed) shifts women from PT to FT by roughly equal magnitudes; men's labour supply barely changes. [explicit, pp.500â€“501]
- **Benchmark value for me:** female participation own-wage elasticity $\approx 0.33$ and unconditional hours elasticity $\approx 0.6$, with near-zero male responses, are the order-of-magnitude sanity checks for my France estimates; large divergence would flag a specification problem. [analogy]

---

## 10. Estimators, theorems, or formal results

For each, statement (paraphrased; LaTeX for the math), assumptions, technique, reusability verdict.

- **Theorem 1 (closed-form choice probability).** Under Assumptions 1â€“2, the joint density of $(h,w)$ is the ratio in Â§5 (eq. 2a,b). Assumptions: separable random utility $U=v(C,h)\varepsilon(z)$; Poisson-scattered taste shifters with $\varepsilon^{-2}$ intensity; offered $(H,W)\sim g_1g_2$ independent of shifters. Technique: max-stable / extreme-value process algebra (Dagsvik 1994); the $\varepsilon^{-2}$ form yields IIA. **Reusable:** yes â€” this *is* my per-alternative structural weight, modulo my sampling correction. [explicit, p.490]
- **Theorem 2 (non-identification under exclusion).** $v(C,h)=\zeta(C)^{r}\lambda^{*}(C,h)\delta(h)$; $r,\delta(h)$ unidentified. Assumptions 1â€“3. Technique: log-differentiate the observable ratio in $I$, integrate over $C$ (Appendix A). **Reusable:** as the *negative* result I cite to justify parametric identification. [explicit, p.493]
- **Theorem 3 (partial identification under wageâŸ‚hours).** Offered-hours distribution identified; $v=\lambda\delta$, $\delta(h)$ unidentified. Assumptions 1â€“4. **Reusable:** yes, to delimit what is/ isn't free without functional form. [explicit, p.493]
- **Theorem 4 (parametric full identification).** Boxâ€“Cox $\log v$ (eq.8) $+$ $g_1(h_1)=g_1(h_2)$ $\Rightarrow$ model (2a,b) identified. Assumptions 1â€“3, 5, 6. **Reusable:** **yes â€” this is my identification citation.** [explicit, p.493]
- **Theorem 5 (identification with wage random effect).** With Assumption 7 (exogenous wage shifter $X$ excluded from preferences) $+$ moment bound (Assumption 8): $v$ identified up to an $h$-term, $\theta(\cdot)$ up to a constant, conditional offered-wage distribution identified; with Boxâ€“Cox, full identification. **Reusable:** yes for justifying the separability of my ability channel, conditional on excluding the wage shifter from $v$. [explicit, p.494]
- **Boxâ€“Cox utility (eq. 8).** $\log v(C,h)=\gamma_1\frac{C^{\alpha}-1}{\alpha}+\gamma_2\frac{(1-h/M)^{\beta}-1}{\beta}+\gamma_3\frac{(C^{\alpha}-1)}{\alpha}\frac{((1-h/M)^{\beta}-1)}{\beta}$ [explicit form, p.493; exact constant arrangement [verify] against the printed OCR]. Globally concave; justified by invariance principles (Dagsvik & StrÃ¸m 2006; Dagsvik & RÃ¸ine Hoff 2011). **Reusable:** yes â€” same family as my preference block.

---

## 11. Robustness and specification sensitivity

- **Wage-heterogeneity stance (their main robustness axis).** They estimate the two "extreme" cases â€” across-job wage variation (M1) vs individual wage heterogeneity / ability (M2) â€” and select M2 on fit. [explicit, pp.496â€“498] *Lesson for me:* the ability-vs-job-residual decomposition of wage variance is a real specification fork; my $\sigma$ inherits this ambiguity, and the M1/M2 contrast is the precedent for treating it as a robustness choice rather than a settled object. The authors decline to separate inter- vs intra-individual wage effects ($\xi+\eta$), judging it to hinge too much on functional form â€” directly relevant to how hard I can push the ability/access boundary. [explicit, p.496 fn.8]
- **Hours grid / cell aggregation.** Thin joint-hours cells force them to aggregate to six cells for goodness-of-fit; the eight-point grid is fixed. [explicit, p.497] *Lesson:* my 901/101 grids are far finer; their thin-cell problem is a caution about over-disaggregating couples.
- **Measurement error / division bias.** The negative observed wageâ€“hours correlation ($-0.22$ women, $-0.17$ men) is a measurement artefact handled by the three-stage procedure. [explicit, pp.495â€“496] *Lesson:* a stress test I should run if I ever construct wages by division; with EUROMOD income I sidestep it but should note it.
- **What they do NOT stress-test:** number of draws (no simulation draws â€” analytic), number of starts, alternative opportunity-set definitions, reference states (no welfare). [not-established] So this paper gives me *no* guidance on effective-sample-size or draw-growth stability â€” those concerns are specific to my importance-sampling layer and unaddressed here.

---

## 12. What I can cite this paper for

- The **RURO/latent-jobs factorisation** of labour supply into preference utility $\times$ opportunity measure, and the closed-form choice probability (Theorem 1). [explicit]
- The **formal identification problem** of separating preferences from the opportunity mechanism on cross-section data, and its resolution under exclusion + Boxâ€“Cox + an offered-hours normalisation (Theorems 2â€“5). This is my primary identification citation. [explicit]
- The terms **"opportunity measure"** ($\theta g_1 g_2$) and **"opportunity density"** ($g_1 g_2$), and $\theta$ as a **job-availability** scalar. [explicit, p.489]
- The design choice that the **wage channel is individualised while the hours channel is institutional/common** across observationally identical agents. [explicit, pp.490â€“491]
- The interpretation of a **wage random effect as individual ability** entering the opportunity measure (support for my ability channel). [explicit, p.494]
- That **non-labour income enters only consumption, not the opportunity measure** (the exclusion restriction). [explicit, pp.492â€“493]
- A **joint couples** latent-jobs labour-supply application as precedent. [explicit]
- Benchmark **female participation/hours elasticities** ($\approx 0.33$ / $\approx 0.6$) with negligible male responses. [explicit, Table II]
- That conventional discrete-choice (van Soest) **PT/FT preference dummies are formally equivalent to peaks in the opportunity density**, with the latter carrying a structural rationale. [explicit, p.495]

---

## 13. What I should NOT cite this paper for  [overclaim risks]

- **No welfare object.** Do not attribute any money-metric welfare, equivalent income, EV/CV, or inclusive-value welfare core to this paper. [not-established]
- **No $W^1$â€“$W^6$.** The compensationâ€“responsibility family is *not* here; it comes from the companion theory and the equivalent-income literature. [not-established]
- **No decomposition.** Do not cite for any inequality index or Shapley/Shorrocks split â€” and especially not for a three-way access/ability/preference decomposition. Its only "decomposition" of opportunity is conceptual, not an inequality decomposition. [not-established]
- **Two-way framing, not three-way.** Where the paper distinguishes sources it is *preferences vs opportunity (constraints)* â€” a **two-way** cut. My three-way access/ability/preference vocabulary is *my* refinement; when citing, say the paper separates preferences from the opportunity mechanism, and note that the access/ability sub-split is my extension. [explicit that it is two-way]
- **Occupation/sector.** Do not cite as support for an estimated occupation-as-access layer; the estimated model has no occupation and no sector. Their informal "sector" (health care, public sector) is industry-flavoured, not my ISCO `loc4`; do not let it license `loc4`/`lindi` slippage. [explicit by absence]
- **Random vs deterministic opportunities.** The paper treats opportunity sets as genuinely **stochastic** (Poisson-scattered, the "RO" is substantive). My design treats opportunities as **deterministic feasible sets** with "RO" as estimation machinery only. Do not import their random-opportunities interpretation as if it were mine. [explicit, Assumption 2]
- **Sampling correction.** Do not cite their enumeration-based estimation as evidence that a $-\log\pi$ proposal correction is dispensable; that is specific to fixed-grid enumeration. [explicit by construction]
- **Theory-paper boundary.** This is a Dagsvikâ€“Jia empirical/identification paper; it is unrelated to the Haydarâ€“Maniquet axiomatic theory paper. Never route any axiom, characterisation, or proof of the $W$-family through this citation, and never read this paper as a theory contribution to my JMP. [boundary]

---

## 14. Direct quotes worth citing

Short verbatim phrases for my own annotation (each kept brief; page numbers as printed):

- p.489 â€” "The parameter Î¸ is clearly a measure of job availability".
- p.489 â€” "the opportunity measure" / "the opportunity density" (their naming of $\theta g_1 g_2$ and $g_1 g_2$).
- p.492 â€” identification "arises from the fact that observed labor supply behavior is a result of both preferences â€¦ and latent job choice constraints".
- p.492 â€” on panel/cross-section data: "hard to see how this would help to solve the identification problem".
- p.494 â€” the wage intercept term is meant to "represent the effect of observed and unobserved individual ability".

(If a longer block is needed for a direct quotation in the draft, pull it from the PDF at the cited page rather than expanding these.)

---

## 15. Open questions and risks for my draft

- **Parametric identification is the whole game.** The paper makes unmistakable that the preference/opportunity separation is *not* design-identified on a cross-section; it is bought with Boxâ€“Cox + exclusions + a normalisation. My access/ability/preference decomposition inherits this â€” I must state plainly that the decomposition's credibility rests on those parametric assumptions and on synthetic recovery, not on an instrument I do not have. Risk: a referee reads the decomposition as data-identified; pre-empt it.
- **Ability vs across-job residual ($\eta$ vs $\xi$).** The authors refuse to separate inter- from intra-individual wage variation as "not theoretically sound" given the information. My ability channel ($\sigma$, returns to education/experience) sits on exactly this fault line; pushing the ability/access boundary too hard repeats the move they declined. Treat the ability/access re-allocation as a *named robustness* (project state Â§6.3), not a headline.
- **Hours channel as institutional/common.** Their justification for common $g_1(h)$ (union/negotiation-set hours) supports my "hours/employment common in the proposal" choice â€” but it also implies access heterogeneity I *do* model (region, occupation, year) is a stronger claim than theirs; I should be ready to defend that those access shifters are identified, given the paper warns even $g_1$'s level is delicate.
- **No guidance on integration error.** The paper is analytic/enumeration-based and says nothing about importance-sampling effective sample size or draw-growth stability â€” the live blockers in my singles welfare integral. This paper cannot reassure on that; it is orthogonal.
- **"Sector" temptation.** The paper's sector talk is a standing temptation to conflate occupation and industry. Discipline: cite only for the *idea* that occupation/sector belongs in $g$ if added, never as an estimated precedent, and keep `loc4` â‰  `lindi`.

---

## 16. TL;DR for retrieval

Dagsvik & Jia (2016, *JAE*) is the canonical identification paper for the latent-jobs/RURO factorisation â€” preference utility $v(C,h)$ times an opportunity measure $\theta g_1(h)g_2(w\mid h)$ â€” proving that on cross-section data preferences and opportunities are non-parametrically unseparable (Thms 2â€“3) but identified under a Boxâ€“Cox utility plus an offered-hours normalisation and the exclusion of non-labour income from the opportunity measure (Thms 4â€“5), with a wage random effect interpreted as individual **ability** entering $g$ (my ability channel) and $g_1(h)/\theta$ supplying my **access** channel. It is my primary **identification** and **opportunity-mechanism** citation and a benchmark for elasticities (female participation $\approx 0.33$), but it computes **no welfare, no inclusive-value money metric, and no decomposition**, contains nothing of the $W^1$â€“$W^6$ family, uses a **two-way** preference/opportunity cut and **genuinely stochastic** opportunity sets, and must never be read through the Haydarâ€“Maniquet theory boundary.
# Dagsvik & KarlstrÃ¶m 2005 â€” Compensating Variation and Hicksian Choice Probabilities in Random Utility Models that are Nonlinear in Income

## 0. Metadata
- **BibTeX key:** DagsvikKarlstrom2005 [verify exact key against project .bib]
- **Authors:** John K. Dagsvik (Statistics Norway and the Frisch Centre, Oslo); Anders KarlstrÃ¶m (Royal Institute of Technology, Stockholm).
- **Year:** 2005 (first version received August 2001; final version accepted February 2004).
- **Outlet:** *The Review of Economic Studies*, Vol. 72, No. 1 (Jan. 2005), pp. 57â€“76.
- **DOI/URL:** JSTOR stable URL https://www.jstor.org/stable/3700684 [no DOI printed on the supplied PDF â€” verify].
- **PDF filename:** `Dagsvik_KarlstrÃ¶m_2005_Compensating_Variation_and_Hicksian_Choice_Probabilities_in_Random_Utility.pdf`
- **Tier:** T1A.
- **JMP block(s) served:** welfare (primary); estimation / numerical-implementation of the welfare integrator (secondary, via the analytic-in-shocks expenditure-function machinery); normative-interpretation (only weakly â€” it supplies the *technique* for CV/EV in nonlinear-in-income RUMs, not a responsibility taxonomy). **Not** an opportunity-mechanism, identification, decomposition, or data-infrastructure source.

---

## 1. One-paragraph relevance to my JMP
This is the methodological backbone for converting a discrete-choice random-utility model that is **nonlinear in income** into a money-metric welfare figure â€” exactly my situation, since my Boxâ€“Cox utility $v_i(c,\ell)$ is nonlinear in consumption and the standard log-sum/linear-in-income CV shortcut therefore does **not** apply (explicit-in-source, p. 58: "when the utility function is nonlinear in income, no analogue to the log-sum approach exists"). The paper defines a random *expenditure function* $Y_B(\mathbf{w},u)=\min_{k\in B} Y_k(w_k,u-\varepsilon_k)$ and shows that money-metric welfare reduces to a **one-dimensional** problem in income for each alternative, then aggregated â€” which is precisely the structure of my money-metric inversion of attained utility $V_i$ to an equivalent income $\Omega_i$. It speaks to **all** my welfare measures uniformly (the inversion technique is measure-agnostic), but it is silent on the access/ability/preference channel cut: it has no opportunity mechanism, no inequality object, and no decomposition. Its contribution to my paper is *apparatus*, not *content*: the expenditure-function/Hicksian-choice-probability toolkit, the GEV closed forms (Corollary 5 / Examples), and the explicit warning that the linear-in-income log-sum welfare formula is invalid in my setting.

---

## 2. Data and setting
**N/A â€” this is a pure theory/methods paper.** There is no dataset, no country, no sample unit, and no estimation sample. The "setting" (their Â§2, p. 59) is an abstract consumer facing a feasible set $B\subseteq S=\{1,\dots,M\}$ of alternatives, each with attributes $w_j$ (including a price/user-cost component) and income $y$.

- **Transports to my France pooled 2015â€“2017 EUROMOD cross-section?** The *machinery* transports fully (it is data-free and holds for any GEV/MNL discrete-choice model nonlinear in income). The *application* does not transport, because there is nothing to transport â€” the paper provides formulae, not estimates.
- **Features I do NOT have that the paper presumes / exploits:** the paper is built around a **two-period price/attribute change** $(\mathbf{w}^0,y^0)\to(\mathbf{w},y^1)$ with the error terms $\{\varepsilon_j\}$ held fixed across the two regimes (explicit, p. 58). My JMP is a **single-cross-section level** welfare exercise, not a before/after reform-CV exercise; I have no policy counterfactual and (under the v5 design) no second regime. So the paper's headline objects (the *distribution* of CV across a policy change, compensated transition probabilities $i\to j$) are richer than what my baseline needs â€” I use the static expenditure-function/inversion core, not the two-period CV-distribution apparatus. This is a derived-by-analogy mapping, not explicit-in-source.

---

## 3. Model and objects (map object-by-object to mine)
Utility of alternative $j$: $U_j = v_j(w_j,y)+\varepsilon_j$ (eq. (1), p. 59), with $v_j(\cdot)$ continuous, decreasing in price, strictly increasing in income, possibly $j$-dependent; $\{\varepsilon_j\}$ have a joint CDF $F^B$ with continuous density (explicit-in-source).

- **Their choice set $B$ = my latent-jobs set $\mathcal{C}_i$?** **Derived-by-analogy.** Both are finite alternative sets entering a max-utility discrete choice. But their $B$ is a *given* feasible subset of a universal $S$; they treat $B$ as exogenous and do **not** model how $B$ is formed. My latent-jobs set is generated by an estimated opportunity density $g$. So the *object* maps, but the *mechanism that produces it* is absent here.
- **Their deterministic utility $v_j(w_j,y)$ = my preference utility $v$?** **Partially, explicit-in-source.** Their $v_j$ is the systematic utility nonlinear in income; my $v_i(c,\ell)$ is the analogous block. Caveat: their $v_j$ can absorb non-pecuniary attributes $a_j$ and a $j$-index, which in some of their examples plays a role analogous to an alternative-specific value. In my architecture those alternative-specific terms would live in the **opportunity density $g$**, not in $v$. So I must **not** import their "$v_j$ carries everything alternative-specific" convention â€” that would conflate my preference block with my access/ability blocks.
- **Explicit opportunity/availability mechanism analogous to my $g$?** **No â€” not-established / absent.** There is no density over alternatives representing feasibility, no offer probabilities, no participation restriction. $B$ is exogenously given. Consequently there is **no** separation of hours / wage(ability) / market / occupation channels. This is the central limitation for my purposes: the paper is about welfare *given* the choice set, not about the choice set's heterogeneity.
- **Their budget map = my EUROMOD disposable income?** **Derived-by-analogy only.** They use an abstract price/user-cost $w_{1j}$ entering $v_j(w_j,y)=\psi_j(y-w_{1j},w_{2j})$ (footnote 3, p. 58; Corollary 1, p. 63). My disposable-income map is the EUROMOD tax-benefit function $c_{ij}$. The paper's "price" abstraction subsumes my $c_{ij}$ as a special case but is not derived for a tax-benefit budget specifically.
- **Does any attribute enter BOTH utility and an opportunity mechanism?** **N/A â€” there is no opportunity mechanism**, so the double-entry flag cannot fire. (No identification justification is offered because the question does not arise in their framework.)

---

## 4. Estimation method
**Largely N/A â€” the paper is not an estimation paper.** It derives welfare formulae taking the random-utility model as already specified/estimated. There is no likelihood, no estimator, no choice-set-construction-by-sampling, no proposal density, and no prior/proposal correction in the paper.

- **Likelihood/estimator:** none.
- **Choice-set construction (fixed grid vs sampled alternatives; grid size):** they assume a **fixed, finite** feasible set $B=\{1,\dots,m\}$; no sampling of alternatives (explicit-in-source, Â§2).
- **Proposal/sampling density; prior/proposal correction; is $\log(\text{prior})$ subtracted from the choice index?** **Not present.** Because the set is fixed and exogenous, there is no McFadden-style sampling-of-alternatives correction anywhere in the paper. This is an important *negative* finding: the paper does **not** speak to my mandatory $-\log\pi(j)$ correction, and I must not cite it for that. (See Â§4b and Â§13.)
- **Normalisation/scale:** in the i.i. extreme-value specialisation (Â§7, p. 70) the standard MNL scale applies; the type-III EV with scale $\tau$ is noted in the Remark on p. 60 ($\tau U_j = v_j+\varepsilon_j$, $P(\varepsilon_j\le x)=\exp(-e^{-x})$).
- **Numerical method / starting values / multistart:** none â€” the contribution is *analytic* formulae plus, where closed forms are unavailable, a single one-dimensional (or low-dimensional) integral.
- **What pins down preferences vs the opportunity mechanism:** N/A â€” no opportunity mechanism, no estimation, so nothing is "pinned down" in the estimation sense.

**Verdict (reusable for my RURO/JAX pipeline?):** **Yes, for the welfare layer only â€” not for estimation.** The reusable step is the **expenditure-function inversion** $u=V_B(\mathbf{w},Y_B(\mathbf{w},u))$ (eq. (7), p. 60) computed alternative-by-alternative as a one-dimensional solve $Y_k(w_k,u-\varepsilon_k)$ (eq. (9), p. 61), and the analytic-in-shocks expectation in the GEV/MNL case (Corollary 5, eq. (20), p. 70). These map directly onto my "ex-ante attained utility $V_i$, then invert to money" core (welfare spec v5 Â§1.1). The estimation, sampling, and proposal-correction parts of my pipeline get **nothing** from this paper.

---

## 4b. Proposal / sampling-of-alternatives correction  [extract even if brief]
**Not-established / absent in the source.** The paper does not sample alternatives and does not carry any per-alternative log-prior. There is no covariate-dependent proposal mean, no occupation-conditioned draw, and no common-vs-individualised proposal distinction â€” because the feasible set is taken as a fixed exogenous primitive. 

Relation to my importance-sampling welfare integrator: the paper is **complementary but silent**. It establishes that, in the GEV/MNL case, the welfare expectation over the extreme-value shocks is **closed-form / analytic** (Corollary 5, p. 70), which is exactly the property my v5 integrator relies on ("analytic in the extreme-value shocks; no FrÃ©chet draws and no simulated argmax"). But the *separate* question of correcting for how the *alternatives themselves* are sampled (my $-\log\pi(j;x_i)$, partly individualised in wage and occupation, common in hours and employment) is **outside this paper's scope**. Do not attribute any proposal-correction result to Dagsvikâ€“KarlstrÃ¶m; cite McFadden's sampling-of-alternatives literature for that instead.

---

## 5. Opportunity mechanism  [MOST IMPORTANT â€” be exhaustive; split by channel]
**N/A â€” there is no explicit opportunity mechanism in this paper.** The feasible set $B$ is an exogenous, fixed, finite subset of the universal set $S$ (explicit-in-source, Â§2, p. 59). Availability of jobs, hours, wages, and occupations is **not** modelled as a density, as offer probabilities, or as a reservation-wage/participation restriction. The set does **not** vary with observable circumstances (region, education, demographic type, local labour market) â€” there are no covariates in the model at all beyond the alternative attributes $w_j$ and income $y$.

Mapping to my three sub-objects:
- **access** (hours / market-participation / region / year / occupation offers): **absent.**
- **ability** (wage technology â€” returns to education/experience, residual productivity): **absent.**
- **occupation as availability vs something else:** **absent**, hence no sector/industry conflation risk to flag (the paper never discusses occupation or industry).

One adjacency worth recording, but as **derived-by-analogy, not as an opportunity mechanism.** The paper shows how to handle a **changing choice set** across the two periods: removing an alternative is implemented by sending its price to infinity so $v_j\to-\infty$ (Remark, p. 67; Examples 2â€“3, pp. 71â€“72), and adding an alternative is the symmetric case (Example 2, eq. (24)â€“(26)). This is a *technical device for set changes under a policy*, not a model of *heterogeneous feasible sets across agents*. It could in principle be borrowed to represent "this job type is not in household $i$'s set" â€” but that is my $g$'s job, and the paper offers no estimation or probabilistic content for it.

**Cost of the omission for my decomposition:** because the paper has no opportunity mechanism, it cannot, on its own, support any access/ability/preference attribution. It supplies the welfare *evaluator* that sits *downstream* of my $g$; it does not supply $g$ and must not be cited as if it does.

---

## 6. Welfare object â€” and its place on my $W^1$â€“$W^6$ map
**Does the paper compute welfare? Yes â€” it derives the apparatus for compensating variation (CV) and equivalent variation (EV) in discrete choice.**

- **Money-metric? Equivalent income? CV/EV? Expected (log-sum) utility?** The welfare object is **compensating variation**, defined implicitly by $\max_j(v_j(w_j^0,y^0)+\varepsilon_j)=\max_j(v_j(w_j,y^1-\mathrm{cv})+\varepsilon_j)$ (p. 58), with $\mathrm{cv}=y^1-Y_B(\mathbf{w},V_B(\mathbf{w}^0,y^0))$ (p. 65). They emphasise (p. 73) that the EV derivation is "completely analogous." It is money-metric in the CV/EV sense. It is **not** an equivalent-income-with-reference-preference object of the King/Fleurbaeyâ€“Maniquet type; there is no reference preference and no responsibility taxonomy.
- **Universal vs constrained feasible set?** Defined over the agent's feasible set $B$ (which may differ across the two periods via the set-change device). It is a constrained-set object in the weak sense that $B$ can be any subset, but there is no normative reading of the set as "opportunity."
- **Reference price/preference/bundle/set:** the reference is the **initial utility level** $V_B(\mathbf{w}^0,y^0)$; welfare is measured relative to the agent's *own* utility at the initial attributes/income, holding the realised $\{\varepsilon_j\}$ fixed across regimes (explicit, p. 58). The reference is a *utility level under own preferences*, not an external reference preference.
- **Discrete-choice subtleties handled:** this is the paper's core strength. It handles (i) **log-sum aggregation** where utility is linear in income (acknowledged as the standard case, p. 58) and supplies the **replacement** when it is nonlinear; (ii) **selection / switching** â€” the chosen alternative can differ before vs after the change, which is precisely the analytic difficulty the random expenditure function resolves (p. 58, p. 64); (iii) **Hicksian vs Marshallian** â€” it defines *Hicksian (compensated) choice probabilities* $P^h_B(j,\mathbf{w},u)=P(J_B(\mathbf{w},Y_B(\mathbf{w},u))=j)$ (Definition 1, p. 62) and proves a discrete-choice **Shephard's-Lemma** analogue (Corollary 1, p. 63); (iv) **integration over unobserved heterogeneity** â€” only a one-dimensional integral is needed given $F^B$ (Theorem 2, p. 62); random coefficients handled in Â§5 (p. 68); (v) **ex-ante vs ex-post** â€” the framework is **ex-ante** in the sense that it integrates over $\{\varepsilon_j\}$ to produce *distributions* and *expectations* of CV (e.g. the mean-CV formula (20), p. 70), while also delivering the joint distribution with the realised initial/current choice.

**Locate on my $W^1$â€“$W^6$ map:** **Not on the map.** The paper's CV/EV is a **policy-change** welfare measure on a single preference with the *initial own-utility level* as reference. My $W^1$â€“$W^6$ are *level* equivalent-income measures distinguished by Independence-of-$\mathbf{y}$ / Independence-of-$A$ stances on responsibility. The paper has neither Ind-$\mathbf{y}$ nor Ind-$A$ content and does **not** correspond to any single $W^k$. The honest mapping is: Dagsvikâ€“KarlstrÃ¶m supply the **computational engine** (expenditure-function inversion, analytic-in-shocks expectation) that any of my $W^k$ inversions can be built on; they do **not** supply, and must not be cited for, the family or its normative readings (those are the companion Haydarâ€“Maniquet theory paper's content, imported as cited primitives).

**Verdict:** **Adaptable (engine), incompatible (object).** Directly usable as the nonlinear-in-income inversion/expectation machinery; incompatible as a normative welfare object or as my $W^k$ family.

---

## 6b. Inclusive value and money-metric inversion  [extract if the paper uses a log-sum or an EV/CV]
- **Does it use the inclusive value (log-sum)?** **Yes, but conditionally and as a contrast.** The paper states the log-sum is the right welfare core **only when utility is linear in income** (p. 58, p. 64: Roy's-identity duality "only when utility is linear in income"). Its whole point is the case where the log-sum **fails**. In the i.i.d. EV / MNL specialisation it nonetheless recovers closed-form expressions: Example 4 (p. 72) gives the linear-in-income case mean expenditure $EY_B(\mathbf{w},V_B(\mathbf{w}^0,y^0))=y^0+\frac1\gamma\log(\sum_k e^{-\gamma w_k^0+a_k^0})-\frac1\gamma\log(\sum_k e^{-\gamma w_k+a_k})$ (eq. (29)), i.e. a log-sum difference â€” confirming the standard formula as the linear special case.
- **Is welfare obtained by inverting an own-utility map to a money figure (1-D solve)?** **Yes â€” explicit-in-source and central.** $Y_k(w_k,u-\varepsilon_k)$ is defined by $v_k(w_k,Y_k(w_k,u-\varepsilon_k))+\varepsilon_k=u$ (eq. (9), p. 61); since $v_k$ is strictly increasing in income this is a **unique one-dimensional solve**, and $Y_B=\min_{k\in B} Y_k$ (eq. (10)). This is *exactly* my "invert attained utility to an equivalent income" step, done per-alternative then aggregated by the min. This is the single most directly reusable result in the paper.
- **Is the expectation over the extreme-value shocks taken analytically (no draws) or by simulation?** **Analytically, in the GEV/MNL case** â€” Corollary 5 (p. 70) and Example 1 (p. 70â€“71) give closed forms; eq. (20) gives mean expenditure as a one-dimensional integral with **no shock simulation**. The paper explicitly argues (citing McFadden 2001, Conclusion p. 73) that this analytic method "is to be preferred to using simulations." This **directly corroborates** my v5 decision to integrate $\varepsilon$ analytically (the log-sum is the closed-form expectation over $\varepsilon$) and to avoid FrÃ©chet draws / simulated argmax in the welfare layer.

Relation to my analytic-in-shocks, importance-sampling inversion: **strong, explicit-in-source for the analytic-in-$\varepsilon$ half; silent for the importance-sampling-over-alternatives half.** Dagsvikâ€“KarlstrÃ¶m justify the analytic expectation over shocks; they do **not** address sampling/weighting over a large alternative set (my IS over draws with weight $\hat g/\pi$), because their set is small and fixed.

---

## 7. Inequality / decomposition content  [three-way where relevant]
**N/A â€” there is no inequality index and no decomposition in this paper.** It computes individual-level (and population-mean, via Hammond 1990's weighted-population-mean welfare, mentioned p. 59) CV/EV objects, not a Gini/MLD/Theil/Atkinson index, and performs no factor/Shapley/Shorrocks/subgroup/RIF decomposition.

- **Counterfactual construction:** the only counterfactual is the **two-period attribute/price change** with $\{\varepsilon_j\}$ held fixed (p. 58). Nothing is "equalised," "neutralised," or "zeroed out" in the inequality-of-opportunity sense. The set-change device (price $\to\infty$) zeroes out an *alternative*, not a *circumstance*.
- **Order/path-independence/exhaustiveness:** N/A (no decomposition).

**Verdict (reusable for my three-way access/ability/preference Shapleyâ€“Shorrocks split anchored on $W^3$/$W^5$/$W^1$?):** **No.** The paper contributes **upstream** of the decomposition â€” it produces the money-metric welfare *values* that a Shapley decomposition would then operate on â€” but it supplies **zero** decomposition content. It is neither two-way nor three-way; it is non-decompositional. To reach my three-way split, everything in the decomposition layer must come from elsewhere (Shorrocks 2013; the IOp/Shapley literature); this paper is cited only for how the welfare numbers feeding the decomposition are computed.

---

## 8. Identification and the separation of preferences from opportunities  [STRICT]
**N/A for identification â€” the paper is not an identification paper.** It assumes the random-utility model (the systematic $v_j$ and the error CDF $F^B$) is **already known/specified**; it does not ask what identifies tastes vs constraints, and it has no opportunity side to separate from preferences. There is no exclusion restriction, no choice-set variation used for identification, no panel, no external opportunity shifter, and no synthetic-recovery argument.

The one assumption that bears on identification *of welfare effects* (not of the model) is the **fixed-$\varepsilon$ assumption**: the random terms are unchanged across the two regimes (p. 58). The paper is candid that this is "reasonable if the error terms characterize tastes" but "less reasonable if $\{\varepsilon_k\}$ also include unmeasured attributes of alternatives, which may be altered by policy" (p. 58) â€” citing Heckmanâ€“HonorÃ© (1990), McFadden (1999b), Carneiroâ€“Hansenâ€“Heckman (2001). 

**Transport to my France pooled cross-section (no panel, no external instrument):** the welfare *machinery* transports (it needs only $\hat\theta$ and the set, both of which I have). The fixed-$\varepsilon$ assumption is **not a binding concern for my baseline** because my v5 welfare object is a **single-cross-section level** computation, not a two-period reform-CV â€” there is no "after" regime in which $\varepsilon$ could change. If I ever add an EV/CV reform exercise (welfare spec v5 Â§1.1 lists EV/CV as secondary D3 objects for AC/JJT comparability), then the fixed-$\varepsilon$ caveat becomes live and I should cite this paper's discussion of it. This does **not** defend me against the "your decomposition is mechanical" referee â€” that defence rests on $g$'s identification and synthetic recovery, on which this paper is silent.

---

## 9. Key results and magnitudes
**No empirical magnitudes** â€” there are no elasticities, participation/hours effects, welfare-effect sizes, opportunity shares, or decomposition shares, because there is no data. The "results" are analytic formulae. The substantive deliverables, with units where they exist:

- **Distribution of the random expenditure function** (Theorem 1, eq. (12), p. 61): $P(Y_B(\mathbf{w},u)\le y)=1-F^B(u-v_1(w_1,y),\dots,u-v_m(w_m,y))$ â€” a CDF over the money metric.
- **Hicksian (compensated) choice probabilities** as a **one-dimensional integral** (Theorem 2, p. 62).
- **Discrete-choice Shephard's Lemma** (Corollary 1, p. 63): $\partial EY_B(\mathbf{w},u)/\partial w_{1j}=P^h_B(j,\mathbf{w},u)$ â€” the price-derivative of aggregate expenditure equals the fractional compensated demand (= Hicksian choice probability).
- **Closed-form mean expenditure / mean CV in the MNL case** (Corollary 5, eq. (20), p. 70) and nested-logit examples (Example 1, eqs. (22)â€“(23), p. 71).
- **Consistency check:** Example 4 (pp. 72â€“73) verifies that the general machinery reproduces the familiar linear-in-income log-sum mean-CV formula (eq. (29)) as a special case.

**Benchmarking value for my plausibility checks:** **low/indirect.** Because there are no numbers, the paper cannot tell me whether my opportunity share or welfare spread is plausible. Its benchmarking role is purely *formal* â€” it tells me the *correct closed form* my MNL welfare integrator should reduce to in the linear-in-income limit, which is a useful **unit-test target** (if I linearise $v$ in $c$, my integrator should reproduce eq. (29)).

---

## 10. Estimators, theorems, or formal results
For each, statement (in LaTeX, near-verbatim), assumptions, technique, reusability verdict.

**Theorem 1 (random expenditure function; p. 61).** $Y_B(\mathbf{w},u)$ is uniquely defined by (8), continuous in $(\mathbf{w},u)$, increasing in prices, strictly increasing in $u$; and
$$P(Y_B(\mathbf{w},u)\le y)=1-F^B\big(u-v_1(w_1,y),\dots,u-v_m(w_m,y)\big),\quad u\in\mathbb{R},\,y>0.$$
- *Assumptions:* $v_k$ continuous, decreasing in price, strictly increasing in income; $F^B$ has continuous density; $B$ finite.
- *Technique:* (i) per-alternative inverse $Y_k(w_k,u-\varepsilon_k)$ from monotonicity in income; (ii) expenditure = $\min_k Y_k$; (iii) translate the min-event into the utility-domain event and read off $F^B$.
- *Verdict:* **Yes â€” directly reusable.** This is the distributional backbone of my money-metric inversion.

**Theorem 2 (Hicksian choice probabilities; p. 62).**
$$P^h_B(j,\mathbf{w},u)=\int_0^\infty F^B_j\big(u-v_1(w_1,y),\dots,u-v_m(w_m,y)\big)\,v_j(w_j,dy),\quad u\in\mathbb{R}.$$
- *Assumptions:* as Theorem 1, plus differentiability of $F^B$ in component $j$.
- *Technique:* change of variable $u_j=v_j(w_j,y_j)$ introduces the Jacobian $v_j(w_j,dy)$; only a 1-D integral remains.
- *Verdict:* **Maybe â€” secondary.** Useful if I report compensated transition/choice probabilities; not needed for the level-welfare headline.

**Corollary 1 (discrete-choice Shephard's Lemma; p. 63).** With $v_j(w_j,y)=\psi_j(y-w_{1j},w_{2j})$ and finite expected expenditures,
$$\frac{\partial EY_B(\mathbf{w},u)}{\partial w_{1j}}=P^h_B(j,\mathbf{w},u).$$
- *Technique:* differentiate the mean-expenditure integral under the integral sign; use $\partial v_j/\partial w_{1j}=-\partial v_j/\partial y$.
- *Verdict:* **Maybe.** Conceptually important (it is the "aggregate/probabilistic Shephard's Lemma," p. 64); a useful sanity/derivative check, not a core computation for me.

**Theorems 3â€“4 and Corollaries 2â€“4 (two-period CV distribution and compensated transitions; pp. 64â€“69).** Joint distribution of $\big(Y_B(\mathbf{w},V_B(\mathbf{w}^0,y^0)),\,J_B(\mathbf{w}^0,y^0),\,J^*_B(\mathbf{w}^0,y^0,\mathbf{w})\big)$, with $\mathrm{cv}=y^1-Y_B(\mathbf{w},V_B(\mathbf{w}^0,y^0))$; the GEV specialisation (Corollary 3) needs **no integration**.
- *Verdict:* **No / deferred.** These power a *reform-CV* analysis (transitions $i\to j$ induced by a policy at fixed utility). My baseline is a level exercise; relevant only if I add the D3 EV/CV reform cross-check.

**Corollary 5 (i.i.d. EV / MNL specialisation; p. 70).** For $0<y<y_i(\mathbf{w}^0,y^0,w_i)$,
$$P\big(Y_B(\mathbf{w},V_B(\mathbf{w}^0,y^0))>y,\,J_B(\mathbf{w}^0,y^0)=i\big)=\frac{\exp(v_i(w_i^0,y^0))}{\sum_{k\in B}\exp\big(\max(v_k(w_k,y),v_k(w_k^0,y^0))\big)},$$
with the mean-expenditure integral (20).
- *Verdict:* **Yes â€” high value.** This is the MNL case I am in; the analytic-in-$\varepsilon$ closed form is the template for my welfare integrator and a unit-test target.

**Lemma 1 (moment identity; p. 63):** $\int_0^\infty x^\alpha\,dH(x)=\alpha\int_0^\infty x^{\alpha-1}(1-H(x))\,dx$. Utility: turns the expenditure CDF into expected expenditure/moments. *Verdict:* **Maybe** â€” handy if I compute welfare moments directly from the CDF.

---

## 11. Robustness and specification sensitivity
**N/A in the empirical sense** (no estimation to stress-test). The paper's "specification sensitivity" is *model-class* generality:
- It works for any $F^B$ with continuous density; specialises cleanly to **GEV** (Â§6, p. 68), **nested logit** (Example 1), **MNL** (Â§7), and **random-coefficient / mixed MNL** (Â§5, p. 68, where Theorem 3 holds conditional on $\beta$ then integrate over $f(\beta)$).
- The **choice-set-change** robustness (adding/removing alternatives via $\pm\infty$ prices; Examples 2â€“3) shows the formulae survive set changes â€” informative for my "is this job type in the set?" representation, but again as a *device*, not an estimated mechanism.

**What this tells my recovery/stability and robustness sections:** mainly a **numerical-correctness** message â€” in the GEV class the welfare expectation is closed-form (Corollary 3 "no integration is needed"), so where my integrator uses simulation I should be able to cross-check against the analytic GEV expression and treat divergence as a bug, not noise. It does **not** speak to effective-sample-size, draw counts, or circumstance partitions (my actual stress tests), because it has no sampling step.

---

## 12. What I can cite this paper for
Specific, attributable claims:
1. That in random-utility discrete choice **nonlinear in income**, the linear-in-income log-sum welfare formula does **not** apply, and a distinct expenditure-function approach is required (p. 58, p. 64). *(Use this to justify why I cannot use the naive log-sum CV in my Boxâ€“Cox setting.)*
2. The existence and uniqueness of a **random expenditure function** $Y_B(\mathbf{w},u)=\min_{k\in B}Y_k(w_k,u-\varepsilon_k)$, obtained by a **one-dimensional inversion per alternative** (eqs. (8)â€“(10), Theorem 1). *(Use to ground my "invert attained utility to equivalent income" step.)*
3. That in the **GEV/MNL** class the distribution and **mean of CV are available in closed form / by a one-dimensional integral, with the expectation over the extreme-value shocks taken analytically** (Corollaries 3â€“5; eq. (20)). *(Use to justify my analytic-in-$\varepsilon$ integrator and as a unit-test target.)*
4. The **discrete-choice (aggregate/probabilistic) Shephard's Lemma** (Corollary 1). *(Cite if I use the price-derivativeâ€“Hicksian-probability link.)*
5. That **EV is derived analogously to CV** in this framework (Conclusion, p. 73). *(Cite for the D3 EV/CV cross-check.)*
6. The methodological stance â€” following McFadden (2001) â€” that the **analytic expenditure-function method is preferable to simulation** for welfare in nonlinear-in-income RUMs (Conclusion, p. 73). *(Cite to defend the analytic design choice.)*

---

## 13. What I should NOT cite this paper for  [overclaim risks]
- **Not** for any **opportunity mechanism / feasible-set heterogeneity**: the set is exogenous and fixed; the paper has no $g$, no access/ability split, no offer probabilities. Do not present it as supporting my opportunity layer.
- **Not** for the **sampling-of-alternatives / proposal-prior correction** ($-\log\pi(j)$): absent here; cite McFadden's sampling literature instead.
- **Not** for any **inequality index or decomposition** (two-way *or* three-way): the paper is non-decompositional. Do not let it stand in for Shorrocks/Shapley content.
- **Not** for the **$W^1$â€“$W^6$ family or any Independence-of-$\mathbf{y}$/Independence-of-$A$ responsibility reading**: the paper has no responsibility taxonomy and no reference-preference equivalent income. Those are the **companion Haydarâ€“Maniquet theory paper's** content, imported by the JMP as cited primitives â€” **never attribute the family, the axioms, or the normative classification to Dagsvikâ€“KarlstrÃ¶m, and never read this paper as a theory contribution to my JMP.**
- **Boundary flags that apply:** (i) **two-way vs three-way** â€” N/A but worse: it is *non*-decompositional, so do not cite for decomposition at all; (ii) **ex-post/universal-set vs my constrained ex-ante object** â€” the paper's CV is a two-period reform object at fixed initial own-utility, **not** my single-cross-section level equivalent income; do not equate them; (iii) **"sectoral"/industry vs occupation-as-access** â€” N/A (paper never mentions occupation or industry), so no conflation to import; (iv) **random- vs deterministic-opportunity** â€” the paper's randomness is in *tastes* ($\varepsilon_j$), not in *opportunities*; it makes no claim that opportunities are random, consistent with my deterministic-opportunity framing, but it also makes no claim that they are deterministic â€” it simply has no opportunity object. Do not cite it either way on the opportunity-randomness question.

---

## 14. Direct quotes worth citing
(Short, exact, with page numbers. Reworded paraphrases preferred elsewhere; these are the few places exact wording matters.)
1. p. 58: "when the utility function is nonlinear in income, no analogue to the log-sum approach exists." *(The licence for using the expenditure-function method.)*
2. p. 62 (Definition 1): Hicksian choice probabilities $P^h_B(j,\mathbf{w},u)\equiv P(J_B(\mathbf{w},Y_B(\mathbf{w},u))=j)$ â€” "the probability of choosing $j\in B$ given that the utility level is given and equal to $u$."
3. p. 64: the Marshallian duality (Roy's identity) route "follow[s] from the mean indirect utility function â€¦ only when utility is linear in income." *(Sharp statement of the boundary of the standard method.)*
4. p. 73 (Conclusion): an "aggregate version of Shephard's Lemma holds under rather general conditions," and, citing McFadden (2001), the method "is to be preferred to using simulations."
5. p. 58: the fixed-error assumption "seems reasonable if the error terms characterize tastes [but] is less reasonable if $\{\varepsilon_k\}$ also include unmeasured attributes of alternatives, which may be altered by policy." *(The honest caveat to cite if I add a reform-CV exercise.)*

[All five verified against the supplied PDF text; if quoting in the draft, re-verify exact wording against the published typesetting, as the supplied scan has OCR noise.]

---

## 15. Open questions and risks for my draft
1. **Marginal vs total welfare.** The paper's CV is a *change* object (two-period). My headline is a *level* object (equivalent income of an attained situation). I must be explicit that I borrow the **inversion/expectation engine**, not the reform-CV object, so a referee does not read my levels as their CV. (Risk: object-mismatch overclaim â€” flagged in Â§13.)
2. **Fixed-$\varepsilon$ across regimes.** Live only if I add the D3 EV/CV reform cross-check; then their caveat (errors = tastes vs unmeasured alternative attributes) bears directly on whether my reform-CV is interpretable. Note in the robustness section if D3 is run.
3. **Large alternative sets.** Their closed forms assume a small fixed $B$ and exploit GEV structure with no sampling. My $\mathcal{C}_i$ is large (901 joint / 101 single) and I integrate by importance sampling over draws. Their analytic-in-$\varepsilon$ result justifies the *shock* integration but **not** the *alternative-set* sampling/weighting â€” the variance/ESS behaviour of my IS integrator (welfare spec v5 Â§6 gate) is **not** addressed by this paper and remains my own burden.
4. **Unit-test opportunity.** Their linear-in-income consistency check (Example 4, eq. (29)) is a concrete target: a linearised version of my integrator should reproduce the log-sum mean-CV. Worth building as a regression test for the welfare core.
5. **Numerical integration error.** The paper's claim that the GEV case needs "no integration" (Corollary 3) is a reminder that wherever I *do* integrate numerically, an analytic GEV cross-check should exist; absence of one is a code-smell.

---

## 16. TL;DR for retrieval
Dagsvik & KarlstrÃ¶m (2005, *REStud*) is the **welfare-engine** reference for discrete-choice random-utility models **nonlinear in income**: it builds a random expenditure function via per-alternative one-dimensional inversion of own utility ($Y_B=\min_k Y_k$), derives Hicksian/compensated choice probabilities and a discrete-choice Shephard's Lemma, and gives closed-form, **analytic-in-shocks** CV/EV distributions and means in the GEV/MNL class â€” directly grounding my money-metric inversion of attained utility $V_i$ to equivalent income and corroborating my analytic-$\varepsilon$ integrator. It speaks to **all** my welfare measures uniformly through the *evaluation* engine but to **none** of the access/ability/preference *channels*, because it has **no opportunity mechanism, no inequality/decomposition object, no proposal correction, and no $W^1$â€“$W^6$ family** (those are upstream/elsewhere and, for the family, the companion theory paper). Cite it for the nonlinear-in-income inversion and the closed-form MNL CV/EV; never cite it for opportunity, decomposition, or the responsibility taxonomy.
# Jacquet, Jia & Thoresen 2026 â€” How Much Does Responsibility Matter in Fairness Measurement?

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
- **Authors:** Laurence Jacquet (CY Cergy Paris UniversitÃ© and THEMA); Zhiyang Jia (Research Department, Statistics Norway); Thor O. Thoresen (Research Department, Statistics Norway; Norwegian Fiscal Studies, Department of Economics, University of Oslo).
- **Year / outlet:** 2026, CESifo Working Papers No. 12418, January 2026.
- **DOI/URL:** SSRN `https://ssrn.com/abstract=6112587`. No journal DOI yet (working paper).
- **PDF filename:** `Jacquet_et_al_2026_How_Much_Does_Responsibility_Matter_in_Fairness_Measurement.pdf`.
- **JEL:** H31, I31, J22, C25. **Keywords:** money metric utility, fairness, tax reform, structural labor supply model.
- **Tier:** T1A (core; this is the single closest cousin of the JMP â€” same estimator family, same money-metric apparatus, overlapping author set with the companion theory paper, and Maniquet appears in the acknowledgements).
- **JMP block(s) served:** estimation; welfare; normative-interpretation; opportunity-mechanism (**access only**); motivation. **Not** decomposition (no inequality decomposition is performed); **not** ability (no structural wage technology); **not** data-infrastructure for France (Norwegian register/survey merge).

**Boundary note carried from the start.** Maniquet is thanked in the acknowledgements; this paper is **not** the companion Haydarâ€“Maniquet theory paper and must never be cited as such. It is also not the JMP. It is the empirical paper whose method the JMP most directly extends and differentiates from.

---

## 1. One-paragraph relevance to my JMP

This is the empirical template the JMP is built against and must out-position: it estimates the same **latent-jobs / "job choice" model** (Dagsvik 1994; Dagsvik and Jia 2016) on a cross-section of couples, and it produces **money-metric** welfare figures by inverting the household's own utility to money (McFadden 1999 simulation). It speaks directly to the **preference** channel (its Boxâ€“Cox utility block = my $v$) and to the **access** channel (its $\log Q(h)$ hours-availability term and the education-scaled job-availability measure $\theta_F$ = my hours/access sub-block of $g$). It does **not** instantiate my **ability** channel â€” wages are taken as observed data, not modelled as a structural wage technology â€” and it performs **no inequality decomposition**: it compares two welfare-*change* measures (standard CV vs. a preference-neutralised CVcirc, with a Conditional-Equality cross-check) and reads off *where on the income distribution* they diverge. For my purposes its single most load-bearing contribution is the **reference-preference neutralisation device** (set taste-shifters to sample medians; impose a common error term) and the demonstration that, in a Norwegian reform, neutralising preference heterogeneity barely moves the welfare distribution except at the very top. It is the paper I cite for the estimator and the money-metric inversion, and the paper I must explicitly distinguish from on four axes: **level vs. change**, **two-measure comparison vs. Shapley decomposition**, **preference-neutralising reference vs. preference-respecting equivalent income**, and **bundled circumstances vs. an access/ability split**.

---

## 2. Data and setting

- **Country / unit:** Norway; **married couples** (with or without children), treated as **unitary** (harmonised joint decision over both spouses' labour supply, common budget). **Explicit-in-source.**
- **Year / dataset:** Cross-section, **2015**. Built by merging, on personal identification numbers, the **Labour Force Survey** (Statistics Norway 2024) and the **Income and Wealth Statistics of Households** (Statistics Norway 2019). The LFS supplies actual and formal working time for main/secondary jobs plus background variables including demographic characteristics and **occupation**; conditional on participation, respondents self-classify as self-employed or employee. **Explicit-in-source.**
- **Sample size:** **1,594 couples** (Table C2). **Explicit-in-source.** Summary statistics in Table C1.
- **Sample restrictions:** couples excluded if one adult has self-employment income > NOK 115,000 (2015 prices); excluded if weekly hours > 80 or wage outside NOK [70, 600] (2015 prices). A person "works" if â‰¥ 1 hour/week. Hours = formal hours in main + second job. Nominal hourly wage = labour income / total annual hours. **Explicit-in-source.**
- **Budget-set construction:** disposable income obtained via the **LOTTE** family of tax-benefit microsimulation models (Jia et al. 2024); piecewise-linear, possibly non-convex budget sets. **Explicit-in-source.**

**Transport to my setting.** Partial. Same broad object (couples, cross-section, microsimulated nonlinear budget), so the *estimator and welfare apparatus transport cleanly*. But the **data infrastructure does not transport**: this is an admin/survey **register merge with personal IDs**, not EUROMOD on EU-SILC. **Features I do not have that they rely on:** (i) a clean **employee/self-employed** self-report (they exclude high self-employment couples on it); (ii) **occupation in the data** as a usable background variable (they have it but, note Â§3, do **not** use it in the model); (iii) precise formal-vs-actual hours from an LFS. They have **no panel, no external opportunity instrument** either â€” so on the identification axis they are in the same cross-sectional boat as my France pooled 2015â€“2017 EUROMOD sample (Â§8).

---

## 3. Model and objects (mapped object-by-object to mine)

| My object | Theirs | Match? |
|---|---|---|
| Latent-jobs choice set $\mathcal C_i$ | Latent jobs $z=1,2,\dots$ market, $z=-1,-2,\dots$ non-market; set $B(h)$ of jobs at hours $h$, size $Q(h)$ unobserved | **Same family** (explicit). Theirs is a fixed discrete **hours grid** (56 couple alternatives), not sampled draws. |
| Preference utility $v$ (Boxâ€“Cox over $c,\ell$, demographic shifters, gender) | $u(C,h_F,h_M)$, Boxâ€“Cox in consumption and leisure with leisure shifters (age, children) and a leisure interaction $\alpha_{15}$ (Eq. 4.10) | **Direct match** (explicit). Their taste-shifters = my demographic shifters. |
| Opportunity density $g$ | $\log Q_F(h_F) + \log Q_M(h_M)$ in the indirect utility (Eq. 4.3); $Q(h)=\theta\,g(h)$, $g$ the **opportunity density of hours**; $\theta$ = relative size of the job set vs. non-work | **Partial match.** Theirs is an **access/hours** density only. |
| **access** sub-block (hours/employment/region/year/occupation) | hours-availability density $g(h)$ (uniform off-peak, with **part-time and full-time peaks**) + $\theta_F$ scaled by **education**: $\log\theta_F = \gamma_{F1}+\gamma_{F2}S$ (Eq. 4.5); $\theta_M$ normalised to 1 (males â‰ˆ all employed) | **access match** (explicit). No region/year/occupation in their access block. |
| **ability** sub-block (structural wage technology: returns to education/experience, residual $\sigma$) | **Absent.** Wages are **observed data** (income/hours), entering only the budget map $C=f(\cdot)$. A reference wage appears only in the **unimplemented** CVpref (Appendix D.2) | **No match.** This is my channel, not theirs (see Â§5, Â§13). |
| occupation as access (`loc4`) | Occupation is **in the data but not in the model** â€” not in utility, not in $g$, not in the wage | **No match.** They neither use occupation nor conflate it with industry. **Not-established** that occupation does anything structural here. |
| EUROMOD disposable income $c_{ij}$ | LOTTE disposable income $C=f(h_Fw_F,h_Mw_M,I)$ | **Functional match**, different microsimulator. |

**Does any attribute enter BOTH utility and the opportunity mechanism?** **No** (explicit). Hours enter both *as an argument* ($u$ depends on $h$; $g$ is a density over $h$), but this is the standard latent-jobs separation â€” preferences value the hours, the opportunity density governs their **availability** â€” not a double-loading of a covariate. Wage enters only the budget; occupation enters nothing. No identification-by-double-entry issue arises, and none is claimed.

**Key structural reading.** Their indirect utility (Eq. 4.3) cleanly splits into a **preference part** $u(\cdot)+\eta$ and a **circumstance part** $\log Q_F+\log Q_M$. In my vocabulary the circumstance part is **access only**; their "circumstances" therefore equal my **access**, *not* my access + ability, because the wage (my ability locus) is not inside their $g$. This is the single most important mapping fact in the paper for me.

---

## 4. Estimation method

- **Estimator:** Maximum Likelihood in a **conditional logit**, choice probability Eq. 4.4. Log-likelihood Eq. 4.11: $\sum_i \log\varphi(h_{iF},h_{iM}\mid w_{iF},w_{iM},I_i)$. **Explicit.**
- **Choice set:** **fixed discrete grid** â€” 56 couple alternatives = **7 male Ã— 8 female** options (males have 7 because there is no data support for a male non-market alternative). **Not** sampled alternatives. **Explicit.**
- **Proposal / sampling density:** **none** â€” there is no sampling-of-alternatives step (see Â§4b). **Explicit.**
- **What pins preferences vs. opportunities apart:** functional form + the observed **bunching at part-time/full-time hours peaks** (which identifies the opportunity density's shape) + the joint hours density $\varphi$; $\theta_F$ identified off **education** variation (Eq. 4.5); $\theta_M$ normalised to 1; $Q_F(0)=Q_M(0)=1$ normalisation. They defer to **Dagsvik and Jia (2016)** for the formal cross-sectional identification conditions. **Explicit.**
- **Numerics / starts / multistart:** not described in detail `[verify â€” no multistart or starting-value protocol stated in the main text]`.
- **Fit:** $N=1{,}594$; log-likelihood $-3070.9$; McFadden's $\rho^2=0.52$ (Table C2). **Explicit.**

**Verdict: reusable for my RURO/JAX pipeline? Partly.** The **likelihood and the indirect-utility decomposition (Eq. 4.3â€“4.4) are directly reusable** as the conceptual backbone (my model is the same family). **Not reusable as-is:** their *estimation* uses a small fixed grid with no proposal correction; my pipeline uses **sampled alternatives with a per-row $-\log\pi$ correction** at 901 (couples) / 101 (singles) resolution. Their grid approach is the older Dagsvikâ€“Jia implementation; my sampling-plus-correction is the scaling step they do not take. Reuse the model, not the choice-set machinery.

---

## 4b. Proposal / sampling-of-alternatives correction

**Not present in estimation.** Estimation is over a **complete fixed grid** of 56 alternatives, so there is no McFadden-style sampling correction and no $-\log\pi$ term in the likelihood. The structural analogue of an "opportunity weight" is the **estimated** $\log Q(h)=\log\theta + \log g(h)$ term, but this is a *model primitive jointly estimated with preferences*, **not** a sampling instrument to be divided out. **Explicit / derived-by-analogy.**

**On the welfare side, simulation enters but not as a proposal.** CV is computed by **drawing Gumbel error terms** $\{\eta_i^k(h)\}$ and solving Eq. (D.1) numerically per draw (McFadden 1999). These are **shock draws over a common grid**, not importance draws over an individualised proposal. There is therefore **no individualised proposal** here at all â€” neither wage-conditioned nor occupation-conditioned â€” because wages are fixed data and occupation is unused. **Explicit.**

**Relation to my proposal-individualisation concern.** Direct contrast, useful for my Â§5.3 audit: my proposal is **partly individualised** (wage mean $\mu_i=X_ib+\delta_{\text{occ}}[\text{loc4}_i]$ and occupation stratum condition on $x_i$; hours/employment common). JJT have **no proposal individualisation** because their two high-dispersion channels (wage, occupation) are simply not stochastic in their model. So they cannot illuminate the well-conditioning of importance sampling â€” they don't importance-sample â€” but they **do** confirm that the *welfare* expectation, when shocks are simulated, requires a per-draw one-dimensional solve. My analytic-in-shocks log-sum (Â§6b) is the efficiency improvement over exactly their D.1 simulation.

---

## 5. Opportunity mechanism  [most important â€” split by channel]

The mechanism is a **density over hours alternatives**, scaled by an aggregate availability measure. Explicitly (Eq. 4.3â€“4.5, Appendix B):

- The latent jobs $z$ at hours $h$ form a set $B(h)$ of unobserved size $Q(h)$. Taking the max over $B(h)$ of i.i.d. Gumbel taste shocks (Appendix B derivation) yields an indirect utility shifted by $\log Q(h)$ â€” i.e. **more available jobs at $h$ â‡’ higher choice value at $h$**. This is the entire opportunity channel.
- $Q(h)=\theta\, g(h)$ with $g(h)$ the **opportunity density of hours** (share of available jobs at $h$) and $\theta$ the **size of the market opportunity set relative to non-work**. Normalisations: $Q(0)=1$.
- $g(h)$ is **uniform for nonstandard hours with a part-time peak and a full-time peak**, matching the observed hours distribution. **Explicit.**

**Mapping to my three sub-objects.**
- **access (hours / participation / job availability):** **YES, this is the whole mechanism.** Hours availability via $g(h)$ with the two peaks; aggregate participation/availability via $\theta$. Females: $\log\theta_F=\gamma_{F1}+\gamma_{F2}S$ â€” **job availability rises with education** (their interpretation). Males: $\theta_M$ **not identified**, normalised to 1 (near-universal male employment). **Explicit.**
- **ability (wage technology):** **ABSENT from the mechanism.** Wages are observed and enter only the budget. There is **no** structural return to education/experience inside $g$, and **no** residual productivity dispersion $\sigma$. The closest object is the **reference wage** $\bar w$ of the **CVpref** alternative (Appendix D.2), where they explicitly reason that "abilities predominantly result from circumstances beyond the individual's control" and so a common reference wage neutralises ability-driven inequality â€” **but CVpref is defined and then left for future research, not implemented.** So ability exists here only as an *unexecuted* neutralisation, not as an estimated channel. **Explicit (that it is deferred).**
- **occupation:** treated as **nothing** â€” observed in data, absent from the model. **No** sector/industry conflation to flag, because occupation is simply unused.

**Functional form:** opportunity density piecewise-uniform with two estimated peak parameters per gender (Table C2: male full-time 2.8936, female full-time 1.5027, male part-time âˆ’0.1512, female part-time âˆ’0.0451), plus $\theta_F=\exp(\gamma_{F1}+\gamma_{F2}S)$ with $\gamma_{F1}=-2.9199$ and $\gamma_{F2}=0.1653$ (SE 0.389 â€” **the educationâ†’availability slope is statistically insignificant**; flag this, Â§9).

**What the omission of an ability channel costs my access/ability/preference decomposition.** A great deal, and this is exactly why my paper exists. By folding all of "circumstances" into **hours/job availability** and treating wages as data, JJT **cannot separate access from ability** â€” they have only a two-way preference/circumstance cut where "circumstance" = access. My added structural wage technology (occupation-conditioned wage draws, returns to education/experience, $\sigma$) is what lets the **ability** dimension exist as a distinct, estimable channel. Cite JJT as the paper that *bundles* the opportunity side; position my ability/access split as the resolution of that bundling.

---

## 6. Welfare object â€” and its place on my $W^1$â€“$W^6$ map

**What they compute.** Three objects, all **welfare *changes* of a tax reform**, not welfare levels:
1. **CV** â€” standard compensating variation: the income that equates max utility before and after the reform under the household's **own** preferences (Eq. 4.12; McFadden 1999). Money-metric, **own-preference-respecting**, defined over the **constrained** latent-job set (it carries the $\log Q$ terms â€” Eq. 4.12 explicitly includes $\log Q_{iF}+\log Q_{iM}$). CV is **stochastic** in the $\eta$ draws.
2. **CVcirc** â€” circumstance-CV: identical computation but with the **deterministic utility $\bar u$ and the random term $\bar\eta$ set to common reference values** (taste-shifters â€” gender, age, children â€” at sample medians; $\alpha_1$â€“$\alpha_4$ common), so "households differ only in circumstances" (Eq. 4.13, Appendix D.2). **Preference heterogeneity is neutralised.**
3. **$\Delta$CE** â€” change in the **Conditional Equality** criterion (Fleurbaey 2008): max **reference-preference** utility on a **hypothetical linear equivalent budget** (slope = wage, lump-sum tax $T$ as intercept), Eq. 3.2â€“3.3, following Carpantier and Sapata (2016); $\Delta\text{CE}=\text{CE}_1-\text{CE}_0$. Reference preferences again at medians.

**Discrete-choice subtleties handled:** CV is the **conditional indirect utility of the most-preferred job within the latent set** (so it is a *constrained-choice* CV); the $\eta$ terms are held fixed pre/post (the standard McFadden assumption), and because the pre- and post-maxima need not fall on the same alternative, CV does **not** collapse to a closed form and is obtained by simulation. **Ex-post element:** for CE they "do not exploit information about actual choices" â€” they draw shocks and assume the household picks the utility-maximising alternative â€” so the CE construction is itself an **ex-ante-by-simulation** object over the grid, though it conditions the equivalent budget on the household's own wage. **Explicit.**

**Locating the paper on my $W^1$â€“$W^6$ map.** Handle with care; the correspondence is **partial and derived-by-analogy**, and the level/change mismatch means *none of these is literally a $W^k$*.
- **Standard CV** respects own preferences **and** own circumstances (own wage, own $Q$) â€” "own everything." Its *stance* is closest to my **Full-Responsibility** corner ($W^2/W^3$): nothing is neutralised. **Derived-by-analogy**, with the caveat that it is a *change* and that all my $W^k$ read attained $V_i$ whereas CV reads a utility *difference*.
- **CVcirc / CE** neutralise **preferences** (set to a reference), leaving circumstances individual. This does **not** map to any single $W^k$, because my family holds **preferences as the responsibility object across all six** and varies *which circumstance dimension* (Ind-$y$ / pay vs. Ind-$A$ / set) is compensated. CVcirc varies the *preference* axis, which my menu does **not** traverse. The honest statement: **CVcirc/CE belong to the reference-preference / Conditional-Equality tradition, which is a different normative device from my preference-respecting equivalent-income family.** My $W^k$ use the household's **own** indifference map; CVcirc/CE substitute a **common reference** map. (`JMP_welfare_spec_v5.md` Â§1.1 is explicit that my $W^k$ invert the *own*-utility map "never by a closed-form shortcut that would bypass the household's preferences" â€” the exact opposite design choice from CVcirc.)
- **CVpref** (their unimplemented dual, Appendix D.2) neutralises **circumstances** instead (reference wage $\bar w$, reference opportunity $\bar Q$). *This* is the object whose **stance** is nearest my compensation corner / my $W^5$ (compensate the set; with reference wage, also compensate pay). But it is **not-established empirically** â€” defined, deferred, never computed.

**Verdict:** the **estimator and the CV inversion are directly adaptable**; the **CVcirc/CE objects are conceptually adjacent but normatively distinct** from my family (reference-preference vs. preference-respecting) and are **changes not levels**; treat them as the *contrast case*, not as instances of $W^1$â€“$W^6$.

---

## 6b. Inclusive value and money-metric inversion

- **Inclusive value:** Yes, partially and analytically â€” the $\log Q(h)$ terms in Eq. 4.3 are precisely the **expected-maximum (log-sum) over the latent jobs at a given hours point**, derived in Appendix B from the Gumbel max. So the inclusive value *within* an hours cell is closed-form. **Explicit.**
- **But welfare is obtained by simulation, not by a closed-form log-sum.** Because CV is **nonlinear in income**, no closed form exists (they cite Dagsvik and KarlstrÃ¶m 2005 for the distribution/moments); they **draw $K$ Gumbel vectors and solve a one-dimensional equation per draw** (Eq. D.1), then average. **Explicit.**
- **Money-metric inversion:** Yes â€” CV is a **one-dimensional solve** that equates pre- and post-reform maximised utility under own preferences (Eq. D.1); CE solves for the lump-sum tax $T$ (Eq. 3.2). Both are own-/reference-utility inversions to a money figure, **not** closed-form shortcuts that bypass preferences. **Explicit.**
- **Expectation over shocks: by simulation**, not analytic. **Explicit.**

**Relation to my integrator.** This is the cleanest single point of methodological differentiation. My welfare layer takes the **expectation over the extreme-value shocks analytically** (the ex-ante inclusive value is the closed-form expected maximum; `JMP_welfare_spec_v5.md` Â§1.1: "the welfare layer requires no shock draws and no simulated argmax"), and inverts by a one-dimensional bracketing root-solve on the **importance-sampled** log-sum. JJT do the inversion by **per-draw simulation over a fixed grid**. Same money-metric inversion logic; **my analytic-in-shocks + importance-sampling step is the efficiency and the ex-ante-access improvement over their D.1 simulation.** Cite D.1 as the simulation baseline I improve on.

---

## 7. Inequality / decomposition content  [three-way where relevant]

**There is no inequality index and no decomposition in this paper.** No Gini/MLD/Theil/Atkinson; no Shapley, Shorrocks, factor-component, subgroup, RIF, or Owen-grouped decomposition. **Explicit (by absence).**

What they do instead:
- Report **means and standard deviations** of the three welfare-change measures (Table 1): the SD is the only dispersion object, used informally to say preference-neutralisation "slightly reduces the spread" (5,458 â†’ 5,188 NOK under CV â†’ CVcirc).
- Report a **rank-transition matrix** across quintiles, CV vs. CVcirc (Table 2): 71â€“93% stay in the same quintile.
- Plot welfare effects **by income decile** (Figures 4â€“5) and identify the decile where CV and CVcirc diverge.

The conceptual cut is **two-way** and, in the source's own words, **preference vs. circumstance** â€” and it is operationalised as a **comparison of two measures**, not as an additive attribution. The "amount that responsibility matters" is *defined* as the gap between CV and CVcirc, not as a component share.

**Verdict: not reusable as a decomposition method.** To serve my **three-way access / ability / preference Shapleyâ€“Shorrocks** split (anchored on $W^3$ for total source-composition and the $W^5$/$W^1$ duals for the access/ability faces) it would need three extensions, each substantial: **(i)** move the object from welfare **change** to welfare **level**; **(ii)** replace the two-measure gap with a genuine **order-independent additive decomposition** of an inequality index; **(iii)** **split circumstances into access and ability**, which their model cannot do because ability (wages) is not a modelled channel. The paper is the *motivation* for a decomposition ("how much does responsibility/preference matter") executed by a cruder instrument; my decomposition is the instrument it lacks.

---

## 8. Identification and the separation of preferences from opportunities  [strict]

**What separates tastes from constraints.** The split rests entirely on **functional form + distributional assumptions + the shape of the observed hours distribution**:
- Preferences enter through the Boxâ€“Cox $u(\cdot)$ and its taste-shifters; constraints enter **only** through $\log Q(h)$. The two are separately identified because the opportunity density is pinned to the **bunching at part-time and full-time peaks** (a feature preferences alone, on a smooth Boxâ€“Cox, would not generate), while the smooth trade-off identifies tastes.
- $\theta_F$'s level and education slope are identified off cross-sectional **education** variation (Eq. 4.5); $\theta_M$ is **conceded non-identified** and normalised (a candid admission worth citing).
- They defer the formal conditions to **Dagsvik and Jia (2016)**: latent-jobs identification from **cross-sectional micro data** under the Gumbel/Luce structure. **Explicit.**

**Can they separate ability from access?** **No.** Within "circumstance" there is only access (hours/job availability); wages are data, so there is no ability sub-model to identify. The would-be ability neutralisation (CVpref reference wage) is deferred. **Explicit / not-established.**

**Transport to my France pooled cross-section.** **Yes, and this is the backbone of my identification defence.** JJT identify the preference/opportunity separation **without a panel and without an external instrument** â€” exactly my constraint â€” relying on parametric/functional-form identification plus the observed hours distribution. This is precisely the structure my baseline uses, and my baseline is additionally **certified by synthetic recovery** rather than in-sample fit. So I can write: *the separation of preferences from opportunities in a cross-section is established practice in this literature (Dagsvikâ€“Jia 2016; Jacquetâ€“Jiaâ€“Thoresen 2026); my contribution is (a) to push it to a three-way access/ability/preference split by adding a structural wage channel, and (b) to discipline the resulting specification by a synthetic-recovery gate rather than in-sample fit.* This is also my answer to the "your decomposition is mechanical" referee: the *same* parametric identification underwrites a published, peer-relevant CV/CVcirc exercise; what is new in mine is the channel split and the recovery certification, not the act of separating tastes from constraints in a cross-section. **Do not soften: the identification is parametric, and I should own that rather than overclaim nonparametric content.**

---

## 9. Key results and magnitudes

- **Average welfare effects (Table 1):** CV = **NOK 18,384** (SD 5,458); CVcirc = **NOK 18,677** (SD 5,188); $\Delta$CE = **0.356** (SD 0.108, different unit/scale). Neutralising preferences **raises** the mean slightly and **lowers** the SD by ~5%. **Explicit.**
- **Rank stability (Table 2):** 71â€“93% of households stay in the same income quintile across CV vs. CVcirc; bottom and top quintiles most stable (84.9% and 92.5%). **Explicit.**
- **Across the distribution (Figure 4):** CV and CVcirc track each other up through decile 9 (~NOK 25,000 gain at decile 9, where disposable income â‰ˆ NOK 1 million), then **drop in decile 10**; **decile 10 is the only group where the two diverge significantly.** **Explicit.**
- **Mechanism:** under CVcirc, women who initially had stronger leisure preferences are assigned **lower returns to leisure**, so **female labour supply rises across the distribution**; male labour supply is unchanged except in the top decile, where it **falls**. The top-decile welfare divergence is driven by **women's** re-optimised labour supply, where pre-reform female hours were low. **Explicit.**
- **$\Delta$CE robustness (Figure 5):** $\Delta$CE closely mirrors CVcirc across deciles 1â€“9; mild divergence at the top (smaller gains), interpreted as methodological noise. **Explicit.**
- **Estimation (Table C2):** $N=1{,}594$; logL $-3070.9$; $\rho^2=0.52$; consumption exponent $\alpha_1=0.6694$; female leisure exponent $\alpha_3=-1.1490$; male leisure exponent $\alpha_4=0.2309$ (SE 0.308 â€” **imprecise**); leisure interaction $\alpha_{15}=1.2111$ (SE 0.863 â€” **imprecise**); $\gamma_{F2}=0.1653$ (SE 0.389 â€” **educationâ†’availability insignificant**). **Explicit.**

**Benchmark for my plausibility checks.** The headline economic message â€” **neutralising preference heterogeneity barely changes the welfare distribution except at the very top** â€” is a (weak, change-based, single-reform, Norway) prior that the **preference channel contributes modestly** to welfare-effect dispersion, with action concentrated among high-income women's labour supply. If my France **level** decomposition returns a small preference component and a larger opportunity component overall, JJT is consistent corroboration; but it is a *change* in a different country, so it bounds plausibility only loosely. Their ~5% SD reduction from full preference-neutralisation is the closest single number to compare against my preference component â€” note that mine should be **larger in principle** because I decompose a *level* and split out *access*, but do not assert this until computed.

---

## 10. Estimators, theorems, or formal results

No theorems. Key formal objects (LaTeX near-verbatim; **explicit**), with reuse verdicts:

1. **Indirect utility with opportunity terms (Eq. 4.3):**
$$V(h_F,h_M,I)=u\big(f(h_Fw_F,h_Mw_M,I),h_F,h_M\big)+\log Q_F(h_F)+\log Q_M(h_M)+\eta_{h_F,h_M}.$$
*Technique:* max of i.i.d. Gumbel over $B(h)$ â‡’ a $\log Q$ shift, $\eta$ retains Gumbel (Appendix B). **Reuse: yes** â€” this is my model's core identity.

2. **Choice probability (Eq. 4.4):**
$$\varphi(h_F,h_M)=\frac{Q_F(h_F)Q_M(h_M)\exp\big(u(f(\cdot),h_F,h_M)\big)}{\sum_{x,y}Q_F(x)Q_M(y)\exp\big(u(f(\cdot),x,y)\big)}.$$
**Reuse: yes** as the likelihood kernel; my version replaces the full-grid sum with a sampled-alternatives sum plus $-\log\pi$.

3. **Opportunity scaling (Eq. 4.5):** $\log\theta_F=\gamma_{F1}+\gamma_{F2}S$. **Reuse: maybe** â€” an education-as-access shifter; relevant to my Â§6.3 "education-as-access" deferred robustness cut, but note its insignificance here.

4. **Boxâ€“Cox utility (Eq. 4.10)** in $(C-C_0)$ and leisure $L_F,L_M$ with a leisure interaction $\alpha_{15}$ and demographic shifters in $\beta_F,\beta_M$. **Reuse: yes** as a specification template (my preference block is the same family).

5. **CV definition (Eq. 4.12)** and **CVcirc (Eq. 4.13):** constrained-choice CV with $\log Q$ terms; CVcirc replaces $u_i,\eta_i$ by common $\bar u,\bar\eta$. **Reuse: yes as templates**, but for *changes*; my levels need the reference-package inversion, not a pre/post-reform difference.

6. **CE (Eq. 3.2â€“3.3):** lump-sum tax $T_i$ implicitly defined by $u(c_i,h_i;\gamma_i)=\max_h\{u(c,h;\gamma_i)\mid c\le w_ih-T_i\}$; then $\text{CE}_i=\max_h\{\bar u(c,h;\bar\gamma)\mid c\le w_ih-T_i\}$. **Reuse: maybe** â€” relevant to my secondary "ex-post chosen-alternative CE" cross-check (`JMP_welfare_spec_v5.md` D3), but their CE uses reference preferences whereas my correction-free CE cross-check is own-preference.

7. **CV simulation (Eq. D.1)** â€” per-draw one-dimensional solve over $\eta$. **Reuse: as the contrast** my analytic-in-shocks integrator replaces (Â§6b).

**Discrepancy to flag (`[verify]`).** The subsistence consumption $C_0$ is stated as **NOK 64,000** in the Â§4.2.3 text but **57,000** in Table C2; $L_0=5{,}110$ hours is consistent across both. Treat $C_0$ as `[verify]` before quoting a number.

---

## 11. Robustness and specification sensitivity

- **Reference-value sensitivity:** medians of taste-shifters replaced by **10th/90th-percentile** values â€” results "remain robust." **Explicit.** (Directly relevant to my reference-state robustness in the decomposition.)
- **CV aggregation:** two routes â€” per-individual mean across draws (their choice) vs. pooling all draws across observationally identical groups; they use the former. **Explicit.**
- **Choice-set size:** fixed at 56; **not varied.** No effective-sample-size / draw-count study (because estimation is not simulation-based). **Number of welfare draws $K$ not stated `[verify]`.**
- **Ability/access boundary:** **not stress-tested** â€” there is no ability channel; the CVpref reference-wage neutralisation that would probe it is **deferred to future research.** **Explicit.**

**What this tells me to stress-test.** (i) My reference-state choice (their 10th/90th-percentile check is the template I should replicate across measures). (ii) My **draw-count / ESS stability** â€” JJT give me *no* guidance here (they don't importance-sample), which underscores that my Â§6 welfare-integration gate and the ESS diagnostic are genuinely my own contribution, not borrowed. (iii) The **ability/access boundary** is exactly the axis they could not test; my education-as-access vs. ability re-allocation (`JMP_project_state_v1.md` Â§6.3) is the test they flagged-by-omission.

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
- Money-metric utility's "revival" in the fair-allocation literature, with their cite chain (Fleurbaey 2008; Fleurbaey and Maniquet 2011, 2018; Bosmansâ€“Decancqâ€“Ooghe 2018; Schleeâ€“Khan 2022) as a ready-made positioning paragraph.

---

## 13. What I should NOT cite this paper for  [overclaim risks]

- **Not** a three-way decomposition. It is a **two-measure comparison** along a **preference / circumstance** axis, and not even a formal additive decomposition. Never imply it decomposes inequality into access/ability/preference shares.
- **Not** a welfare **level** object. Everything here is a **welfare *change*** (CV of a tax reform). Do not present CV/CVcirc/$\Delta$CE as instances of my level equivalent-income family, and do not read their "spread reduction" as a level inequality result.
- **Not** an **access/ability** split. "Circumstance" here = **access (hours/job availability) only**; wages are data, ability is unmodelled, CVpref is deferred. Do not attribute a separate ability channel to this paper.
- **Not** an **occupation-as-access** result. Occupation is in the data but **unused** in the model. Do not cite for `loc4`/occupation opportunity, and do not say they "use occupation."
- **No industry/sector** content at all â€” so there is no sector/occupation conflation to inherit, but equally nothing to cite on industry.
- **Reference-preference â‰  preference-respecting.** CVcirc/CE substitute a **common reference** indifference map; my $W^1$â€“$W^6$ use the household's **own** map. Do not equate CVcirc with a preference-respecting equivalent income, and do not claim this paper computes my family.
- **Random-vs-deterministic:** the latent jobs are **latent** (count $Q(h)$ unobserved) but the opportunity sizes are **deterministic parameters**; the randomness is in the **taste shocks** $\eta$. This is **consistent** with my deterministic-opportunities stance â€” so cite it to *support* that framing, but do **not** describe their opportunities as "random."
- **Theory-paper boundary:** Maniquet is acknowledged, but this paper proves no axioms and characterises no welfare family. Never attribute the Haydarâ€“Maniquet axioms/characterisation to it, and never read it (or my JMP) as a theory contribution.
- **McFadden (1999)** is used here for **welfare simulation**, not for **sampling-of-alternatives in estimation**. Do not cite it via this paper as a sampling correction.

---

## 14. Direct quotes worth citing

Deliberately minimal; verify each against the PDF before use. Page numbers are the printed paper pages.

- On the model's central virtue (p. 1): the job choice model holds features that *"mirror the distinction between preferences and circumstances."*
- On the definition of when responsibility matters (p. 1): *"Responsibility matters whenever the two metrics display different values."*
- On the structural split of indirect utility (p. 10): the opportunity part *"represents the labor market opportunities facing the household."*
- On the headline empirical result (p. 19, summarising): preferences may *"not matter so much in fairness measurement, except at the very top."*

(If more quotation is needed, pull it directly from the PDF rather than from this file â€” I am keeping verbatim text minimal here on purpose.)

---

## 15. Open questions and risks for my draft

- **Simulation vs. analytic integration error.** Their CV is simulated over $K$ Gumbel draws with no stated $K$ or convergence diagnostic (`[verify]`). My analytic-in-shocks + ESS-gated importance sampling is the disciplined alternative â€” but it means *I* carry the burden of demonstrating integration adequacy (the Â§6 three-part gate), since this literature offers no off-the-shelf standard. Frame my ESS diagnostic as filling that gap.
- **Normative basis of the reference.** "Median preferences as the responsibility reference" is asserted, not derived; their 10th/90th-percentile robustness is reassuring but does not address *why* the median. My family-of-measures design sidesteps this by reporting a *spectrum* rather than committing to one reference â€” a defensible positioning move against the "arbitrary reference" critique.
- **Bundled circumstances.** Their inability to separate access from ability is the gap my paper fills, but it also warns me: **is the structural wage technology separately identified from preferences in a cross-section?** JJT avoid the question by not modelling wages; I cannot. This is the sharpest identification risk for my ability channel and must be defended (synthetic recovery of the wage block, not in-sample fit â€” consistent with my certification discipline).
- **External validity of "responsibility matters only at the top."** Reform-specific and Norway-specific (individual taxation, dual income tax). My France level decomposition need not replicate it; do not anchor expectations to it.
- **Change vs. level confusion is a live referee risk.** Because JJT is my nearest neighbour and is a *change* paper, a reader may assume my decomposition is also reform-based. The intro must state the level/change distinction early and explicitly.

---

## 16. TL;DR for retrieval

Jacquetâ€“Jiaâ€“Thoresen (2026) estimate the **same latent-jobs "job choice" model** (Dagsvikâ€“Jia) on 1,594 Norwegian couples and compute **money-metric welfare *changes*** of a bracket-tax reform â€” standard CV vs. a **preference-neutralised CVcirc** (taste-shifters at medians) plus a Conditional-Equality cross-check â€” finding preferences barely move the welfare distribution except in the top decile. For my JMP it is the **estimator-and-inversion template** and the source of the **reference-preference device**, speaking to my **preference** and **access** channels but offering **no ability channel** (wages are data; CVpref is deferred) and **no inequality decomposition** (a two-measure comparison, not a Shapley split). It is the paper I cite for cross-sectional preference/opportunity identification and money-metric CV, and the paper I must distinguish from on **level-vs-change**, **decomposition-vs-comparison**, **preference-respecting-vs-reference-preference**, and **access/ability split vs. bundled circumstance**.
# Sastre & Trannoy 2002 â€” Shapley Inequality Decomposition by Factor Components: Some Methodological Issues

> **Filename note.** This file is saved under the path requested
> (`.../T1A/Capeau_et_al_2015_RURO.md`), but the attached source PDF is **Sastre
> & Trannoy (2002)**, not Capeau et al. (2015). The summary below is of the
> actual attached paper. The filename should be corrected to
> `Sastre_Trannoy_2002_Shapley_decomposition.md`; the Capeau RURO paper must be
> summarised separately from its own PDF. Nothing about RURO / latent jobs is in
> this source.

---

## 0. Metadata

- **BibTeX key:** SastreTrannoy2002 [verify exact key against your .bib]
- **Authors:** Mercedes Sastre; Alain Trannoy
- **Year:** 2002
- **Outlet:** *Journal of Economics / Zeitschrift fÃ¼r NationalÃ¶konomie*, Supplement 9, pp. 51â€“89 (Springer-Verlag)
- **DOI/URL:** [verify â€” not printed on the supplied scan]
- **PDF filename:** `Sastre_Trannoy_2002_Shapley_inequality_decomposition_by_factor_components.pdf`
- **Tier:** T1A
- **JMP block(s) served:** **decomposition** (primary); secondarily **normative-interpretation** (only via the source-tree/hierarchy discussion) and **data-infrastructure** (income-source taxonomy). It does **not** serve estimation, identification, opportunity-mechanism, or welfare.

---

## 1. One-paragraph relevance to my JMP

This is a methodology paper on the **Shapley decomposition of inequality by factor components** â€” the exact decomposition family my headline three-way {access, ability, preference} Shapleyâ€“Shorrocks split belongs to. It does not touch labour supply, RURO, or welfare; its value is that it documents, on real data, the **pathologies** my decomposition must survive a referee on: the choice between *zero* and *equalised* elimination conventions, the **non-independence of contributions from the level of aggregation/clustering**, and the consequent need for a **nested (hierarchical) Shapley** structure with an economically meaningful tree. Because my three channels are themselves aggregates of finer structural sub-blocks (e.g. access = hours + market/participation + region + year + occupation offers; ability = returns to education + experience + residual dispersion $\sigma$), the paper's central warning â€” that the contribution assigned to a factor depends on how its siblings are grouped â€” bears directly on whether my "access share" is well-defined or an artifact of how I bundle sub-channels. It speaks to no single $W^k$; it is measure-agnostic decomposition machinery.

---

## 2. Data and setting

- **Country/years:** United Kingdom (1995 Family Expenditure Survey) and United States (1994 March Current Population Survey), drawn from the Luxembourg Income Study database.
- **Sample unit:** the household; the gross-income distribution is unweighted and not adjusted for family size, as is usual in source-decomposition studies.
- **Sample size:** [verify â€” not reported in the supplied pages].
- **Key variables:** household income disaggregated by source. The headline three-way partition is earnings (E, â‰ˆ72% of household income), capital income (C, 11.4%), and transfers (T, 16.8%). The appendix taxonomy splits these much finer (household-head wages, rest of wages, self-employment, cash property income, private pensions, social retirement, other replacement income, means-tested benefits, other benefits, private transfers, and direct taxes).
- **Budget-set construction:** N/A â€” this is an accounting decomposition of observed income sources, not a structural or behavioural model. There is no budget set, no choice set, no estimation.
- **Transport to my setting:** The *decomposition technique* transports fully to my France pooled 2015â€“2017 EUROMOD cross-section; the *data setting* does not and need not (different country, different vintage, pure income-accounting rather than structural welfare). **Features they have / use that I do not rely on here:** nothing they have is missing from my setting in a way that blocks reuse â€” the method is data-light. The relevant asymmetry runs the other way: my "sources" are **estimated structural channels** of a welfare object, not **observed additive income components**, so the additive-decomposition framing (Â§7) does not map one-to-one.

---

## 3. Model and objects (map object-by-object to mine)

There is **no structural model, no choice set, no utility, no opportunity mechanism, and no budget map** in this paper. It is an axiomatic/empirical study of a decomposition rule applied to an income matrix $X = [x_i^j]$ over individuals $i$ and sources $j$.

- Their choice set = my latent-jobs set? **N/A** (no choice set).
- Their deterministic utility = my preference utility $v$? **N/A** (no utility).
- Opportunity/availability mechanism analogous to my $g$ (hours / wage-ability / market / occupation)? **N/A** (none).
- Their budget map = my EUROMOD disposable income? **N/A**; their object is observed gross or net income by source.
- **Does any attribute enter both a "utility" and an "opportunity" block?** N/A â€” there are no such blocks. The analogous concern in *their* framework is whether a source enters two places in the **tree**; that is exactly the aggregation-dependence problem they study (Â§7 below), and it is the right analogy to flag for my own design, but it is **derived-by-analogy**, not explicit-in-source.

The only object that maps to mine is the **decomposition target**: their inequality index $I$ applied to a sum of components plays the role my Gini (or chosen index) applied to the welfare distribution $\Omega^k$ will play.

---

## 4. Estimation method

**N/A â€” there is no estimator, likelihood, choice-set sampling, or proposal density.** No starting values, no numerical optimisation, no normalisation. The "method" is the deterministic computation of Shapley factor contributions from an income-source matrix.

**Verdict: not reusable as an estimation method** (there is none). The *decomposition formulas* are reusable and are extracted in Â§10.

---

## 4b. Proposal / sampling-of-alternatives correction

**N/A.** There is no sampling of alternatives and no proposal/prior correction in this paper. The paper has nothing to say about my importance-sampling welfare integrator or proposal individualisation. (Flagging explicitly so this section is not mistakenly cross-referenced later: the source is silent here.)

---

## 5. Opportunity mechanism

**N/A â€” there is no opportunity mechanism, no feasibility/availability model, no offer probabilities, no reservation-wage or participation restriction, and no occupation object.** The paper does not model how anything is *available*; it decomposes the inequality of *realised* income by *accounting* source.

**Cost of this omission for my access/ability/preference decomposition:** none directly, because I do not look to this paper for an opportunity mechanism. The indirect lesson is structural, not substantive: the paper shows that even with *fully observed, additive* sources, attributing inequality to a "source" is non-unique once you allow regrouping â€” so my decomposition cannot inherit well-definedness from the structural model alone; it must additionally fix an elimination convention and a channel hierarchy (Â§7, Â§10). **No sector/industry conflation arises** because there is no occupation/sector object at all.

---

## 6. Welfare object â€” and its place on my $W^1$â€“$W^6$ map

**The paper computes no welfare object.** It decomposes inequality of **income** (gross and net), not of equivalent income or any preference-respecting money metric. There is:

- no equivalent income, no compensating/equivalent variation, no log-sum/inclusive value;
- no reference price, reference preference, reference bundle, or reference set;
- no discrete-choice subtleties, no ex-ante/ex-post distinction.

**Placement on my $W^1$â€“$W^6$ family: none.** The source does **not** contain $W^1$â€“$W^6$ or any Independence-of-$y$ / Independence-of-$A$ stance. Any attempt to locate it on the family map would be fabrication. The only contact point with my welfare layer is downstream: whatever $W^k$ distribution I produce, *this* paper governs how I may decompose its inequality by source/channel.

**Verdict: incompatible as a welfare source; directly usable as the decomposition rule applied to the welfare output.**

---

## 6b. Inclusive value and money-metric inversion

**N/A.** No inclusive value, no log-sum, no EV/CV, no money-metric inversion, no expectation over extreme-value shocks (analytic or simulated). The paper is silent on every item in this section. It cannot inform my analytic-in-shocks importance-sampling inversion.

---

## 7. Inequality / decomposition content  [MOST IMPORTANT for this paper]

This is the substantive core and the reason the paper is T1A for me.

**Inequality index.** Results are presented with the **Gini**; the authors state that results for other inequality indices exhibit the same pattern, so the conclusions do not depend on the choice of index. Note the cardinality caveat: the Shapley decomposition requires agreement not only with the ordinal meaning of an inequality index but also with its cardinal one.

**Decomposition rule.** Shapley factor-component decomposition (Shorrocks-1999 / Chantreuilâ€“Trannoy lineage), plus two hierarchical refinements: **Nested-Shapley** and **Owen**. Each elementary source's contribution is its expected marginal impact on overall inequality averaged over all possible sequences of source elimination.

**Counterfactual construction â€” the central design choice (what is zeroed vs equalised).** Two conventions for treating sources *not* in the evaluated subset:
- **Zero decomposition:** sources outside the subset are **removed/set to zero**.
- **Equalised decomposition:** inequality from sources outside the subset is **removed by replacing each excluded source with its mean** $\mu(x^j)$, i.e. equalised across individuals.
The treatment of an **equally distributed source** distinguishes them: under the zero rule its contribution is negative (an apparent equalising effect), whereas the equalised rule assigns it exactly zero impact, the latter matching Shorrocks's (1982) reasonable-property requirement.

**Headline empirical finding driving the recommendation.** The **zero rule is highly volatile to the level of aggregation; the equalised rule is far more stable.** Concretely: collapsing earnings+capital into a single "market income" makes the UK transfers contribution jump from 14.2% to 47.2% under the zero approach, while moving only from 4.6% to 5.5% under the equalised approach; finer partitions can even turn the zero-rule transfers contribution **negative**. Therefore the authors favour the equalised approach because zero contributions depend far more on the level of aggregation, a pattern invariant to the index or country.

**Order-independence / exhaustiveness / the key failure.** The Shapley contributions are exhaustive (sum to total inequality) and symmetric. But the rule does not satisfy independence of the aggregation level: a source's contribution depends on how the *other* sources are treated/clustered. This is the property most relevant to me. Two remedies impose a hierarchy:
- **Nested-Shapley** (Chantreuilâ€“Trannoy 1999): a two-stage between/within procedure on an exogenous, economically meaningful partition; it secures the *milder* requirement that a secondary factor's contribution is independent of the disaggregation of *other* primary factors (though still dependent on the treatment of the primary factor it belongs to).
- **Owen** value (Owen 1977): also satisfies the milder requirement, but the authors reject it as a default because it requires coalitions mixing elementary and aggregated sources whose economic meaning is doubtful, making Nested-Shapley more adequate.

**Tree-choice sensitivity.** With a fixed equalised Nested-Shapley rule, the **choice of income tree still matters**: across three economically defensible trees the contributions show moderate volatility, concentrated in the sources treated differently across structures (replacement income, redistributive transfers, property income), while the earnings contributions are barely affected, and the authors conclude it is impossible to escape that the choice of tree has a critical impact on the results. Net-income (post-tax) decompositions are additionally unstable: adding the tax stage can push transfers' contribution negative and market income's above 100%, and perturbs capital's contribution to a negative sign.

**Verdict for my three-way access/ability/preference Shapleyâ€“Shorrocks split (anchored on $W^3$/$W^5$/$W^1$):**
**Reusable as the governing methodology, with three concrete imports.**
1. **Adopt the equalised (not zero) elimination convention** for the headline. This is *explicit-in-source* as the more aggregation-robust choice and aligns with the Shorrocks zero-impact-of-an-equal-source property your spec already invokes. [The mapping of "equalise a source" to "equalise a structural channel" â€” i.e. neutralise the access/ability/preference channel to its population-reference state â€” is *derived-by-analogy*; your welfare spec's "equalisation" of a channel is conceptually the equalised convention, not the zero convention, and this paper is the citation for *why* that is the right default.]
2. **Treat the three channels as a fixed, economically motivated hierarchy and use Nested-Shapley if you ever report sub-channel contributions** (e.g. splitting access into hours/market/region/year/occupation, or ability into education/experience/$\sigma$). The paper's result is that a flat Shapley over many sub-channels will make your top-level "access share" depend on how finely you cut access â€” exactly the artifact your project-state already worries about for the couples preference-compression issue.
3. **Report tree/grouping sensitivity as a robustness object, not an afterthought** â€” the paper's own conclusion is that tree choice is consequential even under the stable rule.

**Two-way vs three-way note.** The paper is **factor-additive and flat-or-nested over income sources**, not organised as a two-way opportunity/preference cut. To reach my three channels I do not "extend" their two-way design (they have no such design); I instantiate their **general** k-factor rule with $k=3$ top-level channels and, optionally, a nested second level. The genuine gap is conceptual, stated in your own spec and *not* resolved here: their sources are **additive components of the target** ($\sum_j x^j = $ income), whereas my channels are **non-additive structural inputs** to a welfare object computed through a nonlinear inclusive value. The Shapley/Shorrocks machinery still applies (Shorrocks 1999 generalises beyond additive factors via the elimination/counterfactual formulation), but **the additive income-source intuition in this paper does not carry over literally**; cite it for the elimination-convention and aggregation-dependence lessons, not for an additive-share interpretation.

---

## 8. Identification and the separation of preferences from opportunities  [STRICT]

**N/A for behavioural identification â€” there is nothing to identify.** The paper estimates no preferences and no constraints; there is no panel, exclusion restriction, choice-set variation, or external instrument, because there is no behavioural model. It therefore says **nothing** about separating tastes from constraints, or ability from access.

**Honest transport statement:** This paper provides **no identification support** for my preference-vs-opportunity or ability-vs-access separation. That separation rests entirely on my structural model (functional form, the $g$/$v$ split, synthetic-recovery certification) and **not** on this source. The "your decomposition is mechanical" referee is met **only partly** here: this paper helps me defend the *decomposition step* (convention choice, aggregation robustness, exhaustiveness) but it **cannot** defend the *upstream structural separation* â€” and it is important not to overclaim that it does. The one transferable caution it raises against the mechanical-decomposition charge is endogeneity of the components: the authors quote Gottschalk and Smeeding (1997) that source decompositions can be misinterpreted because they do not distinguish endogenous from exogenous factors, and concede their own sources are not mutually exogenous. For me this is a *warning*, not a *solution*: my channels are model-constructed and interdependent, so the Shapley contributions are descriptive accounting under a fixed convention, not causal shares.

---

## 9. Key results and magnitudes

Benchmarks usable to sanity-check the *stability behaviour* (not the substance) of my own decomposition. UK 1995, Gini, household non-adjusted, three-source partition (E/C/T):
- Equalised Shapley relative contributions: earnings 83.6%, capital 11.8%, transfers 4.6%.
- Zero Shapley relative contributions: earnings 24.9%, capital 60.9%, transfers 14.2%.
The gap between the two conventions for the *same data and partition* is the headline magnitude: it is large, which is the whole point. US 1994 shows the zero rule can even make the earnings contribution negative.
- Aggregation sensitivity (UK transfers): zero rule 14.2% â†’ 47.2% when earnings+capital are merged; equalised rule 4.6% â†’ 5.5% for the same regrouping.
- Tree sensitivity (UK replacement income): âˆ’1.8% when treated as factor-linked income vs 3.8% when merged with the rest of transfers; private pension contribution ranges roughly 4.9%â€“7.6% across trees.

**What this benchmarks for me:** not a plausible opportunity share (different object entirely), but the *expected order of magnitude of convention/grouping-induced movement* â€” i.e. how much my access share could move purely from how I bundle sub-channels or which elimination rule I pick. The lesson is that **convention choice can move a contribution by tens of percentage points**, so my reported shares must be paired with a fixed, pre-registered convention and a grouping-robustness panel.

---

## 10. Estimators, theorems, or formal results

(Statements transcribed in LaTeX; equation numbers are the paper's.)

**(R1) Shapley value, marginalist form (eq. 2.1):**
$$Sh_i(N,v)=\sum_{S\subseteq N,\, i\in S}\frac{(s-1)!(n-s)!}{n!}\big[v(S)-v(S\setminus\{i\})\big].$$
- *Assumptions:* TU cooperative game; all orderings equally likely.
- *Technique:* expected marginal contribution averaged over all coalition orderings.
- *Reusability:* **yes** â€” this is the engine your Shapleyâ€“Shorrocks split already uses.

**(R2) Zero-income Shapley source contribution (eq. 3.3):**
$$Sh_j(K,X,I)=\sum_{S\subseteq K,\, j\in S}\frac{(s-1)!(k-s)!}{k!}\big[I(y(S))-I(y(S-\{j\}))\big],$$
with $y(S)=\big[\sum_{j\in S}x^j\big]$ (excluded sources removed).
- *Reusability:* **no for the headline** â€” this is the volatile zero convention the paper recommends against. Useful only as the disfavoured comparator.

**(R3) Equalised-income Shapley source contribution (eq. 3.4):**
$$Sh^e_j(K,X,I)=\sum_{S\subseteq K,\, j\in S}\frac{(s-1)!(k-s)!}{k!}\big[I(y^e(S))-I(y^e(S-\{j\}))\big],$$
with $y^e(S)=\big[\sum_{j\in S}x^j+\sum_{j\notin S}\mu(x^j)\big]$ (excluded sources set to their means).
- *Reusability:* **yes â€” adopt as the headline convention** (channel held at its population reference rather than zeroed). [The translation from "set excluded source to its mean" to "equalise an excluded structural channel to its reference state" is *derived-by-analogy*; cite R3 for the convention, implement the channel-equalisation in your own welfare/decomposition code.]

**(R4) Nested-Shapley contribution (eqs. 4.2â€“4.3):** two-stage between/within procedure on a partition $\mathcal P_K$, with the within-stage contribution of elementary source $j$ in aggregate $S_l$ equal to its equalised-Shapley contribution inside $S_l$ plus an equal split of the residual $\frac{1}{s_l}\big[NSh^e_{S_l}-I(y^e(S_l))\big]$.
- *Reusability:* **maybe â€” adopt only if reporting sub-channel contributions.** It secures independence from the disaggregation of *sibling* aggregates and keeps coalitions economically interpretable. Caveat: contributions remain dependent on the treatment of the *parent* channel, and the authors note Nested-Shapley is **not invariant to adding an initial tree stage** (net-income result).

**(R5) Owen value, equalised (eq. 4.6):** alternative hierarchical value mixing elementary and aggregate coalitions.
- *Reusability:* **no (default)** â€” rejected by the authors for relying on doubtfully-meaningful mixed coalitions; keep as a robustness comparator at most.

No probabilistic limit theorems, consistency proofs, or standard-error results are stated; the paper is finite-sample/accounting and **does not provide inference**. Your cluster-robust bootstrap on `idorighh` is *your* contribution, not this paper's.

---

## 11. Robustness and specification sensitivity

What they vary and what breaks â€” directly informs my robustness section:
- **Elimination convention (zero vs equalised):** breaks the zero rule (high aggregation-volatility, sign flips). **Stress-test:** report both; headline on equalised.
- **Level of aggregation / clustering of sibling sources:** breaks flat Shapley (the independence-of-aggregation failure). **Stress-test:** Nested-Shapley + a grouping panel showing your top-level access/ability/preference shares under at least two defensible sub-channel groupings.
- **Choice of hierarchy/tree:** moderate but non-negligible movement, concentrated in the regrouped sources. **Stress-test:** report channel shares under alternative trees (e.g. education-as-access vs education-as-ability â€” which is already your named ability/access re-allocation robustness).
- **Gross vs net (adding taxes as a stage):** destabilises Nested-Shapley (negative/over-100% contributions). **Relevance to me:** my welfare object is post-tax-benefit by construction (EUROMOD `ils_dispy`); I am not decomposing pre- vs post-tax income, so this specific pathology is less directly threatening â€” but it is a sharp reminder that **adding a coarse top-level split can destabilise everything below it**, which matters for how I place the singles/couples and year levels in any nested tree.
- **Inequality index:** robust â€” same patterns across indices (their claim).

**For my effective-sample-size / draw-count concerns:** this paper is silent (no simulation). Those gates come from your welfare-integration spec, not here.

---

## 12. What I can cite this paper for

- The **distinction between zero and equalised elimination conventions** in Shapley factor-component decomposition, and the **empirical case for preferring the equalised convention** on aggregation-robustness grounds.
- The **non-independence of Shapley contributions from the level of aggregation/clustering** of sibling factors â€” the core motivation for imposing a channel hierarchy.
- **Nested-Shapley** as the preferred hierarchical refinement over **Owen**, on the grounds of economically meaningful coalitions.
- The **sensitivity of decomposition results to the choice of hierarchy/tree**, justifying a tree-robustness panel.
- The **zero-impact-of-an-equally-distributed-source** property (equalised rule) as the principled treatment, linking to Shorrocks (1982).
- The endogeneity caution (Gottschalkâ€“Smeeding) that source decompositions are descriptive, not causal.

---

## 13. What I should NOT cite this paper for  [overclaim risks]

- **Not** a source for any opportunity mechanism, latent-jobs/RURO structure, choice set, proposal correction, or identification of preferences vs constraints â€” it has none of these.
- **Not** a welfare paper: it computes **no** money-metric/equivalent income and contains **no** $W^1$â€“$W^6$ family and **no** Independence-of-$y$/Independence-of-$A$ stance. Do not map it onto my measure menu.
- **Not** a two-way opportunity/preference decomposition that I "extend" to three-way; it is a flat/nested **k-factor income-source** decomposition. Frame my three channels as an instantiation of the general rule, not an extension of their cut.
- **Do not transfer the additive income-source interpretation literally** to my non-additive structural channels; the share-equals-source-weight intuition (their Â§4.1 ratio interpretation) does not hold for a nonlinear welfare object.
- **Not** an inference source â€” no standard errors, no bootstrap; do not attribute my cluster-robust CIs to it.
- **Sector/industry:** there is no occupation/sector object here, so there is no `loc4`/`lindi` content to (mis)cite; do not invent one.
- **Random vs deterministic opportunities:** the paper is silent; do not enlist it on either side.
- **Theory-paper boundary:** this paper is unrelated to the Haydarâ€“Maniquet axiomatic paper; do not let its "axiomatic properties of decomposition rules" language bleed into claims about the companion characterisation of $W^1$â€“$W^6$. Trannoy's separate body of social-choice work is **not** this paper.

---

## 14. Direct quotes worth citing

Short verbatim phrases with page numbers (page numbers are the printed journal pages on the scan):

1. p. 54 â€” the aggregation-level failure: "it does not satisfy the principle of independence of the aggregation level."
2. p. 54 â€” the two conventions: "zero income decomposition" vs "equalized income inequality decomposition."
3. p. 62 â€” the empirical verdict: zero contributions are "much more dependent on the level of aggregation than the equalized ones."
4. p. 70 â€” on Owen: its mixed coalitions "have a doubtful economic meaning."
5. p. 74 â€” tree choice: "the choice of a tree has a critical impact on the decomposition results."
6. p. 75 â€” mechanical application "may give odd results."

[All quotes kept under 15 words; verify exact wording/page against the PDF before pasting into the draft.]

---

## 15. Open questions and risks for my draft

- **Convention pre-registration.** I must fix the elimination convention (equalised) *before* reporting numbers, or invite the charge that I chose the convention that flattered the access share. This paper is the citation that makes equalised the defensible default â€” use it pre-emptively.
- **Channel hierarchy is a design decision, not a neutral one.** If I ever disaggregate access or ability, my top-level shares move with the grouping. I need a declared tree and a Nested-Shapley implementation, plus a robustness panel â€” otherwise the access share is not well-defined. This intersects directly with the project-state worry that pinned couples-preference parameters mechanically compress the couples preference component and inflate the couples opportunity share; the paper supplies the general reason that aggregation/treatment choices distort shares.
- **Additivity gap unresolved.** The paper's clean additive-source setting does not match my nonlinear welfare object; I must verify (in my own decomposition memo) that the Shorrocks elimination formulation â€” not the additive-share intuition â€” is what I am invoking, and state the exhaustiveness gate ($\sum$ components $= I(\Omega^k)$) as my own check, since the paper guarantees exhaustiveness only for its additive construction.
- **Descriptive, not causal.** The endogeneity caution means my shares are accounting under a convention; I should not phrase them as causal opportunity effects. Keep the normative reading (compensation-relevance) tied to the welfare measure stance, not to the decomposition arithmetic.
- **Inference is mine to supply.** No SEs here; my per-component cluster-robust bootstrap CIs (tight for opportunity, wide for preference, per the project state) are an addition this literature does not cover.

---

## 16. TL;DR for retrieval

Sastre & Trannoy (2002) is the **decomposition-methodology** anchor (no RURO, no welfare, no opportunity mechanism): it establishes the **equalised** elimination convention as more aggregation-robust than the **zero** convention, documents that flat Shapley contributions **depend on how sibling factors are clustered**, and recommends **Nested-Shapley over Owen** with a declared economic tree. For my JMP it governs the **decomposition step only** â€” convention choice, channel-hierarchy robustness, and the exhaustiveness/aggregation-dependence caveats around my three-way {access, ability, preference} Shapleyâ€“Shorrocks split â€” and explicitly does **not** inform any single $W^k$, the opportunity mechanism, or the preference-vs-opportunity identification.
# Shorrocks 1982 â€” Inequality Decomposition by Factor Components

## 0. Metadata
- **BibTeX key (suggested):** `shorrocks1982decomposition`
- **Author:** A. F. Shorrocks (London School of Economics; Queen's University)
- **Year:** 1982
- **Outlet:** *Econometrica*, Vol. 50, No. 1 (January 1982), pp. 193â€“211
- **URL:** JSTOR stable URL `https://www.jstor.org/stable/1912537` (explicit on PDF). DOI `10.2307/1912537` [verify â€” not printed on PDF]
- **PDF filename:** `Shorrocks_1982_Inequality_Decomposition_by_Factor_Components.pdf`
- **Tier:** T1A
- **JMP block(s) served:** **decomposition** (primary); **normative-interpretation** (the two "contribution" readings of Â§5, which formalise the counterfactual-neutralisation idea); **motivation** (foundational citation for additive factor decomposition). It does **not** serve estimation, identification, welfare, or opportunity-mechanism (access/ability) â€” the paper contains no choice model, no welfare object, and no opportunity structure.

## 1. One-paragraph relevance to my JMP
This is the foundational reference for **additive decomposition of an inequality index into the contributions of distinct components**, and it supplies the axiomatic backbone for the claim that a decomposition can be made *unique* and *index-independent*. It speaks to **Exercise B (the source decomposition)** rather than to any single channel: it is about *how* to allocate inequality to components, not about *which* components (access / ability / preference) are the right ones. Its central cautionary result â€” that without the right symmetry axioms the proportional contribution of a component can be driven to *any* value in $(-\infty,\infty)$ (the three-person example, eq. 30) â€” is precisely the "your decomposition is mechanical / arbitrary" referee threat my Â§8 must pre-empt, and it is the reason my decomposition must be pinned by exhaustiveness/order-independence axioms (Shapleyâ€“Shorrocks) rather than by a "natural" formula. **Crucial boundary:** the rule Shorrocks derives (cov$(Y^k,Y)/\sigma^2(Y)$) applies to **additive income sources** $Y=\sum_k Y^k$; my access/ability/preference channels are **not** additive money components but counterfactual neutralisations of structural blocks, so the cov-rule does **not** transport directly â€” the Shapley-value machinery (Shorrocks 2013) is the correct tool, and this 1982 paper is the additive special case / conceptual ancestor.

## 2. Data and setting
**N/A â€” no data, no empirical application, no country/year.** This is a purely methodological/theoretical paper in the theory of inequality measurement. Populations appear only as abstract income vectors $Y=(Y_1,\dots,Y_n)$ and as illustrative hypotheticals (notably a three-person population in the eq. 30 example). Income "sources" are abstract factor components $Y^k$ (the running examples named are earnings, investment income, and transfer payments). There is **no** budget-set construction, **no** microdata, **no** panel, **no** instrument, **no** vacancy/offer data. Nothing here transports as *setting* to my France pooled 2015â€“2017 EUROMOD cross-section; what transports is the **decomposition theory**, which is setting-free.

## 3. Model and objects (map object-by-object to mine)
There is **no structural/behavioural model** to map â€” no choice set, no deterministic utility $v$, no opportunity density $g$, no budget map. The single object is a partition of total income into factor components and an inequality index $I(Y)$.
- **Their factor components $Y^k$** vs **my channels:** their $Y^k$ are *additive* sub-vectors summing to total income, $Y=\sum_k Y^k$ (the decomposition is defined for "disjoint and exhaustive components of income," explicit-in-source, Â§3). My {access, ability, preference} are **not** additive income sub-vectors; they are structural blocks of the model whose effect on welfare inequality is isolated by *equalisation/neutralisation counterfactuals*, not by summing money pieces. **This is the single most important object-level mismatch** and the basis for several boundary flags below.
- **Their total $Y$** vs **my welfare vector $\Omega^k$:** their decomposed aggregate is the *income* distribution; my decomposed aggregate is a *money-metric equivalent-income* distribution $\Omega^k$ computed from attained utility $V_i$. Shorrocks's aggregate is observed income; mine is a constructed welfare object â€” so even the thing being decomposed differs in kind.
- **Opportunity / availability mechanism:** none. (Detailed in Â§5 below.)
- **Budget map = my EUROMOD disposable income?** No budget map at all.
- **Job attribute entering BOTH utility and opportunity?** N/A â€” no utility and no opportunity object exist here, so the double-counting flag does not arise. The analogue concern in *this* paper is whether components are disjoint and exhaustive (they are required to be).

## 4. Estimation method
**N/A.** No likelihood, no estimator, no choice-set construction, no numerical optimisation, no starting values. The paper derives decomposition *rules* (closed-form allocations of an index to components), not estimates. **Verdict: not reusable as an estimation method** (there is none); reusable only as the *decomposition* layer (see Â§7, Â§10).

## 4b. Proposal / sampling-of-alternatives correction
**N/A.** No alternatives are sampled; no proposal density; no $\log(\text{prior})$ correction. The paper has no choice-theoretic content whatsoever. Nothing here bears on my importance-sampling welfare integrator or my proposal-individualisation concern.

## 5. Opportunity mechanism  [MOST IMPORTANT â€” here: explicitly absent]
**There is no opportunity mechanism, by construction.** The paper takes the *realised* distributions of factor incomes $\{Y^k\}$ as given primitives and asks only how to allocate the inequality of their sum. There is no feasibility, no availability, no offer probability, no reservation wage, no participation restriction, and no dependence on circumstances (region, education, demographic type, local labour market).
- **access:** not modelled.
- **ability:** not modelled.
- **occupation as availability:** not modelled; no occupation object, hence **no risk of occupation/industry conflation** in this source.

Shorrocks himself flags the cost of this omission in his own terms (Â§5, concluding remarks, explicit-in-source): factor decomposition examines each component *separately* and **neglects feedback effects** on other sources (his example: a tax decomposition identifies the contribution of taxes to post-tax inequality but ignores taxes' effect on the *pre-tax* distribution). He states that evaluating such indirect effects would require specifying behavioural relationships, which factor decompositions deliberately avoid â€” and he calls this "both the strength and weakness" of the approach.

**What this omission costs my access/ability/preference decomposition (derived-by-analogy):** because Shorrocks's rule is purely statistical and behaviour-free, applying an *additive-component* logic to my channels would silently assume the channels are non-interacting additive money pieces with no general-equilibrium/behavioural feedback. My channels are behaviourally entangled (neutralising access changes attained utility and hence the chosen bundle, which is exactly a "feedback effect" Shorrocks excludes). This is the formal reason my decomposition needs the Shapley counterfactual construction (which handles interactions by symmetric averaging over orderings) rather than the 1982 covariance rule.

## 6. Welfare object â€” and its place on my $W^1$â€“$W^6$ map
**The paper computes no welfare object.** No money-metric, no equivalent income, no compensating/equivalent variation, no log-sum/inclusive value. It operates entirely on income distributions and inequality indices. There is **no** reference price, reference preference, reference bundle, or reference set, and no ex-ante/ex-post distinction (there is no choice and no uncertainty).

**Place on my $W^1$â€“$W^6$ map: none â€” do not claim this source contains $W^1$â€“$W^6$ or any Independence-of-$\mathbf{y}$ / Independence-of-$A$ stance.** It is index-and-component theory upstream of the welfare object. The one genuine point of contact is conceptual and lives in Â§5: Shorrocks's two interpretations of "the contribution of factor $k$" (below, Â§7) formalise the *neutralisation counterfactual* that my decomposition uses to isolate a channel â€” but this is a decomposition-construction idea, not a welfare measure. **Verdict: incompatible as a welfare object; usable only at the decomposition layer.**

## 6b. Inclusive value and money-metric inversion
**N/A.** No inclusive value, no log-sum, no EV/CV, no money-metric inversion, no expectation over shocks (analytic or simulated). The paper has no discrete-choice or random-utility content.

## 7. Inequality / decomposition content  [CORE OF THIS PAPER]
This is the section the paper exists for. All of the following is **explicit-in-source**.

**Indices covered.** Variance $\sigma^2$; squared coefficient of variation $I_2$; Gini $G$; the Generalized Entropy family $I_c$ (eq. 19), including Theil $I_1$ and $I_0$; and â€” via the weak-consistency extension of Â§4 â€” the Atkinson family.

**Decomposition family and the "natural" rule.** For additive components $Y=\sum_k Y^k$, the *natural* decomposition assigns to factor $k$ its own variance plus **half** of every interaction (covariance) term involving it, giving the contribution
$$ S_k^*(\sigma^2) \;=\; \mathrm{cov}(Y^k,\,Y), \qquad s_k^*(\sigma^2)=\frac{\mathrm{cov}(Y^k,Y)}{\sigma^2(Y)} $$
(eqs. 3â€“4). The same proportional contributions arise for $I_2$ (eqs. 6â€“7); a separate "natural" rule (the pseudo-Gini, eqs. 10â€“11) is given for the Gini and a pseudo-Theil for $I_1$ (eqs. 20â€“21).

**The non-uniqueness warning (the load-bearing result for my defence).** Theorem 1 (eqs. 13â€“14) shows that any index written in the quasi-separable weighted-sum form $I(Y)=\sum_i a_i(Y)Y_i$ admits a contribution $S(Y^k,Y)=\sum_i a_i(Y)Y_i^k$ â€” but the weights $a_i(Y)$ are **not unique**. Corollary 1 (eq. 27) characterises the *entire family* of admissible rules via arbitrary functions $\lambda_j(Y)$, and eq. 28 shows the proportional contributions can be made to match those of *any other* index. The three-person illustration (eq. 30) is the punchline: by choosing $\lambda_1$ freely, the proportional contribution of a factor "can be made to give any value between plus and minus infinity" â€” i.e. an unaxiomatised decomposition is empirically meaningless.

**The uniqueness theorem.** Adding **Assumption 6 (Two-Factor Symmetry)** to Assumptions 1â€“5 yields **Theorem 3 (eq. 31): a unique rule for every inequality index**,
$$ s_k(I)\;=\;\frac{S(Y^k,Y)}{I(Y)}\;=\;\frac{\mathrm{cov}(Y^k,Y)}{\sigma^2(Y)} \quad\text{for all } Y\neq\mu e, $$
with two consequences stated explicitly: (i) the decomposition rule is unique, and (ii) the *proportional* contributions are **independent of the inequality index chosen** (they coincide with the natural decomposition of the variance / $I_2$).

**Weakly consistent decompositions (Â§4).** Replacing additive consistency (Assumption 4) with a weaker aggregator condition (Assumption 4â€²) and invoking AczÃ©l's theorem gives Theorem 4: there is a monotonic transform $f$ (unique up to scale) such that transformed contributions sum to the transformed index. This extends the framework to indices that are monotonic transforms of the quasi-separable form, **including the Atkinson family** ($f(y)=(1-y)^{1-\varepsilon}$). Under a non-additive aggregator the *proportional* contributions need no longer sum to one or be index-invariant.

**Counterfactual construction (the two interpretations, Â§5 â€” directly relevant to my channel neutralisation).** Shorrocks formalises "the contribution of factor $k$" two ways:
- **(A) "pure" contribution** â€” inequality if factor $k$ were the *only* source of differences: $C_k^A = I\!\big(Y^k+(\mu-\mu_k)e\big)$ (eq. 39): hold $Y^k$, give everyone the *mean* of every other source.
- **(B) "eliminated" contribution** â€” the fall in inequality if factor $k$ differences were *removed*: $C_k^B = I(Y) - I\!\big(Y-Y^k+\mu_k e\big)$ (eq. 40): replace each $Y_i^k$ by its mean.

For the variance, the unique rule sits exactly between them: $S(Y^k,Y)=\mathrm{cov}(Y^k,Y)=\tfrac12(C_k^A+C_k^B)$. **(A) zeroes out all other sources; (B) zeroes out the target source** â€” and (B) is the formal sibling of my "equalise this channel and read the inequality fall" counterfactual. Shorrocks notes (A) ignores interactions while (B) loads *all* of factor $k$'s interactions onto $k$, and that in general neither $C^A$ nor $C^B$ alone yields a *consistent* (summing) decomposition except when components are uncorrelated.

**Verdict for my three-way Shapleyâ€“Shorrocks split (anchored on $W^3$/$W^5$/$W^1$).** **Reusable as foundational principle, not as formula.** Three transfers, one non-transfer:
1. **Transfers:** the *consistency/exhaustiveness* requirement (Assumption 4) and the *index-independence* property (Theorem 3) are exactly the disciplines I want â€” they justify (a) requiring my Shapley components to sum to $I(\Omega^k)$ and (b) reporting across Gini/Theil/Atkinson without re-qualifying every number.
2. **Transfer:** interpretation (B) (eq. 40) is the additive-world version of my channel-equalisation counterfactual.
3. **Transfer (as warning):** the eq. 30 $(-\infty,\infty)$ result is the citation that *motivates* axiomatic pinning of any decomposition.
4. **Does NOT transfer:** the closed-form rule $\mathrm{cov}(Y^k,Y)/\sigma^2(Y)$ itself, because (i) my channels are **not** additive income components, and (ii) the asymmetry between (A) and (B) when components interact is exactly what the **Shapley average over all orderings** resolves â€” which is the 2013 development, **not** present in this 1982 paper.

**This paper is a $K$-factor additive (income-source) decomposition.** It is neither a two-way opportunity/preference split nor a three-way access/ability/preference split, and it is **not** a Shapley-value paper. Extending it to my three channels requires (a) reconceiving the "components" as structural-block neutralisations and (b) replacing the half-the-covariance interaction split with the Shapley symmetric-orderings average.

## 8. Identification and the separation of preferences from opportunities  [STRICT]
**N/A in the structural-econometric sense** â€” there is no estimation, no tastes-vs-constraints identification problem, and nothing here addresses separating *ability* from *access*. The paper's "identification" is purely about *which allocation rule* is pinned down by which axioms, an algebraic question.

**Why it nonetheless belongs in my identification/defence note (derived-by-analogy, state as such):** the eq. 30 result is the cleanest existing statement that a decomposition with too few axioms is *not identified as a number* â€” its proportional contribution ranges over the whole real line. This is the formal precedent I cite when a referee charges that the access/ability/preference split is "mechanical" or "arbitrary": the answer is that the split is pinned by exhaustiveness + order-independence (Shapleyâ€“Shorrocks), exactly the kind of axiomatic discipline Shorrocks (1982) shows is *necessary* to obtain a unique, interpretable decomposition. **It does not, however, solve my structural identification** (preferences vs opportunities, or ability vs access) â€” that must come from functional form, the certified synthetic-recovery argument, and the opportunity-density structure, none of which this paper touches. Do not let this citation be read as identifying the *channels*; it only disciplines the *allocation* once channels are defined.

## 9. Key results and magnitudes
No empirical magnitudes (no data). The "results" are the theorems. The one quantitative illustration worth carrying is the **three-person example (eq. 30)**: with the Gini and a freely chosen $\lambda_1$, the proportional factor contribution spans the entire interval $(-\infty,\infty)$ â€” a qualitative "magnitude" that benchmarks *how badly* an unaxiomatised decomposition can behave, not any substantive share. Nothing here benchmarks the plausible size of my own opportunity share or welfare spread.

## 10. Estimators, theorems, or formal results
- **Theorem 1 (eqs. 13â€“14).** *Statement:* Assumptions 2â€“4 imply $S(Y^k,Y)=a(Y)\!\cdot\!Y^k=\sum_i a_i(Y)Y_i^k$ with $I(Y)=a(Y)\!\cdot\!Y$. *Assumptions:* continuity + symmetric treatment of factors (A2), independence of level of disaggregation (A3), consistent (additive) decomposition (A4). *Technique:* the additivity of A4 forces a Cauchy functional equation in the contribution map; its solution (AczÃ©l) is linear, i.e. a weighted sum of factor incomes. *Reusability:* **yes, as principle** â€” gives the quasi-separable contribution form and motivates the exhaustiveness requirement; not a formula I apply to non-additive channels.
- **Corollary 1 (eq. 27) + eq. 28.** *Statement:* the admissible decomposition rules form a large family indexed by arbitrary continuous $\lambda_j(Y)$; proportional contributions under one index can be reproduced under any other. *Technique:* characterise the solution space of the single linear restriction (14) via a basis of the homogeneous system (22)â€“(23). *Reusability:* **yes, as the non-uniqueness warning** (the motivation for axiomatic pinning).
- **Theorem 2 (eqs. 29).** *Statement:* population symmetry and the equal-factor normalisation (Assumption 5) constrain but do **not** uniquely pin the rule. *Reusability:* maybe â€” supports the claim that "reasonable but weak" axioms are insufficient; secondary.
- **Theorem 3 (eq. 31).** *Statement:* Assumptions 1â€“6 imply the **unique, index-independent** rule $s_k(I)=\mathrm{cov}(Y^k,Y)/\sigma^2(Y)$. *Assumptions:* A1â€“A5 plus **Two-Factor Symmetry (A6)**. *Technique:* A6 plus a permutation-matrix construction kills all free $\lambda_j$. *Reusability:* **yes, as principle** (index-independence justifies my across-index robustness reporting); **no, as formula** (covariance rule needs additive components).
- **Theorem 4 (eqs. 35â€“38).** *Statement:* under weak consistency (Assumption 4â€²) there is a monotonic $f$, unique up to scale, with transformed contributions summing to the transformed index; covers the Atkinson family. *Technique:* associativity of the aggregator $F$ + AczÃ©l's representation theorem. *Reusability:* **maybe** â€” relevant if I want to decompose an index (Atkinson) that is only a monotonic transform of a quasi-separable form; note proportional shares then lose index-invariance and additive summing.

## 11. Robustness and specification sensitivity
What the paper itself "stress-tests" is the **axiom set**: it shows step-by-step how adding axioms (A4 â†’ A5 â†’ A6, then the weakening A4 â†’ A4â€²) changes the admissible decomposition family from "the whole real line" to "unique." Two takeaways for my robustness section:
- **Index choice:** Theorem 3 says the *proportional* contributions are index-independent under A1â€“A6 â€” direct support for reporting my decomposition across **Gini / Theil / Atkinson** without expecting the *shares* to move for index-choice reasons alone (any movement I see is then attributable to the decomposition rule or the welfare measure, not the index). This is a useful internal consistency check.
- **Aggregation rule:** Â§4 warns that under a non-additive aggregator (e.g. multiplicative, $f=\log$), proportional shares need not sum to one â€” so if I ever decompose a non-additively-aggregable index I must report this explicitly. For my purposes the additive/exhaustive route (Shapley) is the safer default.
There is nothing here on choice-set size, number of draws, multistart, or opportunity-set definitions â€” those concerns are foreign to this paper.

## 12. What I can cite this paper for
- The **foundational principles of factor decomposition**: continuity, symmetric treatment of factors, independence of the level of disaggregation, and **consistency/exhaustiveness** (contributions sum to total inequality) â€” Assumptions 1â€“4.
- That a decomposition lacking sufficient symmetry axioms is **not pinned down** â€” the proportional contribution can take *any* value (eq. 30, three-person example). The motivation-for-axiomatics citation.
- That, with two-factor symmetry added, there is a **unique decomposition rule whose proportional contributions are independent of the inequality index** (Theorem 3, eq. 31) â€” support for cross-index robustness reporting.
- The **two formal readings of "a factor's contribution"** (the "only source" reading (A), eq. 39; the "eliminate the differences" reading (B), eq. 40) â€” the additive-world formalisation of channel-neutralisation counterfactuals.
- The honest statement that factor decompositions **neglect behavioural feedback between components** (Â§5, tax-incidence example) â€” useful when I caveat that my channel neutralisations are *accounting* counterfactuals, not general-equilibrium ones.
- The **weak-consistency extension to the Atkinson family** (Theorem 4), if I decompose an Atkinson index.

## 13. What I should NOT cite this paper for  [overclaim risks]
- **NOT a Shapley-value decomposition.** This 1982 paper is the *additive factor-component* rule (half-the-covariance interaction split); the Shapley-value / symmetric-orderings construction is **Shorrocks (2013)** (and the cooperative-game lineage), **not** here. Cite 2013 for the Shapley average, not 1982.
- **NOT a two-way *or* three-way opportunity/preference decomposition.** It decomposes by **additive income sources**, not by access / ability / preference. Do **not** describe its components as "opportunity vs preference."
- **NO welfare object.** It contains no money-metric, equivalent income, EV/CV, or inclusive value; do not present its $S(Y^k,Y)$ as a decomposition of *welfare* â€” my object is the inequality of $\Omega^k$, not of income.
- **Do NOT claim it contains $W^1$â€“$W^6$** or any Independence-of-$\mathbf{y}$ / Independence-of-$A$ stance â€” it has no responsibility/compensation content of any kind.
- **NO opportunity / access / occupation content**, hence no occupation-vs-industry issue arises; do not import any "sectoral"/availability language from it.
- **NO random-opportunity framing** (and none to "correct"); it is silent on opportunities entirely. Consistent with my deterministic-opportunities stance, but it makes no claim either way.
- The **cov$(Y^k,Y)/\sigma^2(Y)$ formula does not apply to my channels** â€” they are not additive money components. Citing the *formula* (rather than the *principle*) for a structural-block decomposition would be a misuse.
- **Theory-paper boundary:** this is an empirical-JMP citation for decomposition method; it has no bearing on, and must not be conflated with, the Haydarâ€“Maniquet axiomatic welfare-characterisation paper. Shorrocks's axioms are *inequality-decomposition* axioms, not the companion paper's *welfare-measure* axioms.

## 14. Direct quotes worth citing
To respect source copyright I keep verbatim quotation minimal and give precise locations so exact wording can be pulled from the PDF when drafting:
- On the central non-uniqueness danger, the three-person example concludes that a factor's proportional contribution can be made to take <em>any</em> value between plus and minus infinity (**p. 202, around eq. 30**) â€” the single most quotable line for the "decomposition needs axioms" point.
- On feedback effects being excluded, and this being "both the strength and weakness" of factor decomposition (**p. 210, final paragraph of Â§5**) â€” paraphrase or short exact pull when caveating accounting-vs-behavioural counterfactuals.
- On the index-independence payoff: that with Assumptions 1â€“6 no qualification by choice of index is needed (**p. 205, after Theorem 3**).
- Interpretations (A) and (B) of a factor's contribution (**p. 209, eqs. 39â€“40**) â€” cite by equation, no prose quote needed.

(*Verbatim strings deliberately not reproduced here; copy exact wording from the cited pages of the PDF for the manuscript.*)

## 15. Open questions and risks for my draft
- **Additivity is the hidden assumption.** Everything in this paper rests on $Y=\sum_k Y^k$. My channels are not additive money pieces, so I must be explicit in the draft that I borrow Shorrocks's *principles* (exhaustiveness, index-independence) while replacing his *construction* with the Shapley average â€” and cite 2013 for the latter. The risk is a referee conflating the two; pre-empt by stating the distinction once, clearly.
- **Interaction handling.** Shorrocks's (A)/(B) asymmetry under correlated components is exactly the path-dependence the Shapley average is designed to remove. My Â§8 should make the link: the eq. 30 indeterminacy and the (A)â‰ (B) gap are *the same problem*, and order-independence is the resolution. This strengthens the "not mechanical" defence.
- **Feedback / general equilibrium.** Shorrocks's own caveat (behavioural feedback ignored) applies to my channel neutralisations: equalising access changes attained utility and the chosen bundle. I should state that my decomposition is a *structural-accounting* counterfactual at the estimated $\hat\theta$, not a GE counterfactual, and that this is a deliberate, standard scope limit (citing Shorrocks's framing of strength-and-weakness).
- **Index choice for the headline.** Theorem 3's index-independence holds for *additive* components; under my non-additive Shapley split the index-invariance is not guaranteed by this theorem. I should *check empirically* that shares are stable across Gini/Theil/Atkinson rather than *assert* it from Shorrocks 1982 â€” and report the check.

## 16. TL;DR for retrieval
Foundational additive **factor-component** inequality decomposition: with continuity, symmetric factor treatment, disaggregation-independence, consistency, and **two-factor symmetry**, every inequality index has the **unique, index-independent** contribution rule $\mathrm{cov}(Y^k,Y)/\sigma^2(Y)$ (Theorem 3, eq. 31); without enough axioms the proportional contribution is **indeterminate** over $(-\infty,\infty)$ (eq. 30). Serves my **decomposition** block as the *principle* layer (exhaustiveness + index-independence + the (A)/(B) neutralisation readings, eqs. 39â€“40), **not** as a usable formula â€” my access/ability/preference channels are non-additive, so the Shapley-average construction (Shorrocks 2013) is required, and this paper carries **no welfare object, no opportunity mechanism, and no $W^1$â€“$W^6$ content**.
# Shorrocks 2013 â€” Decomposition Procedures for Distributional Analysis: A Unified Framework Based on the Shapley Value

## 0. Metadata
- **BibTeX key:** `Shorrocks2013` [verify exact key against your `.bib`]
- **Authors:** Anthony F. Shorrocks
- **Year:** 2013 (received 19 May 2011; accepted 26 May 2011; published online 7 January 2012; journal volume dated 2013)
- **Outlet:** *Journal of Economic Inequality*, vol. 11, no. 1, pp. 99â€“126
- **DOI/URL:** 10.1007/s10888-011-9214-z
- **PDF filename:** `Shorrocks_2013_Decomposition_procedures_for_distributional_analysis.pdf`
- **Tier:** T1A
- **JMP block(s) served:** decomposition (primary); methodological backbone of the three-way Shapleyâ€“Shorrocks split. It does *not* serve estimation, identification, opportunity-mechanism, welfare-object construction, data-infrastructure, or motivation directly â€” it is the attribution rule layered on top of whatever welfare object and channel partition the JMP supplies upstream.

## 1. One-paragraph relevance to my JMP
This is the foundational reference for the JMP's headline decomposition layer: it establishes the Shapley decomposition as the unique exact, symmetric, residual-free additive rule for attributing a distributional indicator $I = f(X_1,\dots,X_m)$ to its factors by averaging each factor's marginal contribution over all elimination orders. The JMP's three-way **access / ability / preference** Shapleyâ€“Shorrocks split *is* an instance of this rule with $m=3$ factors, where $I$ is the inequality of a money-metric welfare measure $\Omega^k$ and "removing" a factor means equalising the corresponding structural channel. The paper supplies the exhaustiveness/order-independence property that the welfare-spec Â§6 Shapley gate demands (components must sum exactly to $I(\Omega^k)$). It speaks to no single one of the three channels â€” it is channel-agnostic machinery â€” and it speaks to no specific welfare measure $W^1$â€“$W^6$; its bearing is entirely on *how the attribution is performed* once the channels and the indicator are defined upstream. The paper's most consequential warning for the JMP is its own Â§4 result that Shapley contributions are generally **not invariant to how factors are grouped** unless a separability condition holds, which directly governs whether the JMP may treat {access, ability} as a grouped "opportunity" primary factor.

## 2. Data and setting
N/A â€” the paper is **purely methodological**; it uses no microdata, no country, no sample, no estimation. Its illustrative applications (growthâ€“redistribution poverty change; subgroup poverty; subgroup inequality; source decomposition of inequality) are analytical, drawn from the prior decomposition literature (Dattâ€“Ravallion, Fosterâ€“Greerâ€“Thorbecke, Theil, Bourguignon, Shorrocks's own earlier work), not from a dataset. **Transport to my France pooled 2015â€“2017 EUROMOD cross-section:** the *rule* transports completely â€” it is dimensionless with respect to data and applies to any aggregate indicator $I=f(\cdot)$ â€” but the paper supplies no data-side guidance, no inference machinery beyond a remark that standard errors would "ideally" be computed by algorithm (Â§7), and no sample-design considerations. Features I have that the paper does not address: clustered/bootstrapped inference (the JMP's cluster-robust bootstrap on `idorighh` is mine to build; the paper only flags the desideratum), and the structural-model origin of the factors.

## 3. Model and objects (map object-by-object to mine)
The paper's "model" is the abstract structure $\langle K, F\rangle$: a factor index set $K=\{1,\dots,m\}$ and a set function $F(S)$ giving the value the indicator takes when factors outside $S$ have been "eliminated," with the normalisation $F(\varnothing)=0$ (explicit-in-source, Â§2). There is **no choice set, no utility function, no opportunity mechanism, no budget map** â€” none of my structural objects appear. The mapping to mine is therefore one of *interface*, not of shared primitives:
- My latent-jobs choice set / preference utility $v$ / opportunity density $g$ are all **upstream**; in this paper's terms they are inputs that determine the factor list $K$ and the elimination counterfactuals defining $F(S)$.
- My welfare measure's inequality $I(\Omega^k)$ is this paper's indicator $I=F(K)$.
- My three channels {access, ability, preference} are this paper's factors $X_1,X_2,X_3$.
- "Equalising channel $k$" (my counterfactual) is this paper's "eliminating factor $k$," i.e. moving from $F(S\cup\{k\})$ to $F(S)$.
No job attribute enters "both utility and the opportunity mechanism" *in this paper*, because the paper has neither â€” the double-counting flag is N/A here and must be policed in my structural spec, not here. **Critical caveat the paper forces onto my design:** the paper is explicit (Â§2, footnote 1) that when $F$ derives from an econometric model the normalisation $F(\varnothing)=0$ usually requires one factor to represent the unexplained residual, or $I$ to be renormalised to the "surplus due to the identified factors." My three-channel split must therefore confront whether equalising all three of {access, ability, preference} drives welfare inequality to exactly zero; if it does not, there is an implicit residual factor and the exhaustiveness gate must be interpreted against the renormalised surplus, not against raw $I(\Omega^k)$.

## 4. Estimation method
N/A as an estimator of structural parameters. The paper's "method" is the **construction of the attribution**, given $F$. The Shapley contribution is (explicit-in-source, Eq. 2.8â€“2.9)
$$
C^S_k(K,F) \;=\; \sum_{S\subseteq K\setminus\{k\}} \pi(|S|,|K\setminus\{k\}|)\,\Delta_k F(S)
\;=\; \mathbb{E}_{S\subseteq K\setminus\{k\}}\,\Delta_k F(S),
$$
with weights $\pi(s,m-1) = (m-1-s)!\,s!/m!$ and marginal effect $\Delta_k F(S) = F(S\cup\{k\}) - F(S)$. There is **no likelihood, no choice-set sampling, no proposal density, and no prior/proposal correction** in this paper â€” those belong to my estimation and welfare-integration layers and are *not* informed by Shorrocks. **Verdict: reusable for my decomposition layer â€” yes, directly.** With $m=3$ channels the rule requires evaluating $F$ on all $2^3=8$ subsets and forming the order-averaged marginals; the named step is "compute $I(\Omega^k)$ under each of the eight equalisation states and apply Eq. 2.9." The paper notes (Â§7, explicit-in-source) that for complex models the contributions will not have closed form and must be computed by algorithm, and that standard errors "ideally" be produced too â€” confirming my plan to compute the three-way split numerically with bootstrap CIs rather than analytically.

## 4b. Proposal / sampling-of-alternatives correction
N/A â€” the paper has no sampling of alternatives and no proposal/prior correction; these concepts do not appear and have no analogue in $\langle K, F\rangle$. My importance-sampling welfare integrator and the per-row `prior` correction are entirely outside this paper's scope and must be sourced from the discrete-choice / RURO literature, not here. Stated plainly so it is not silently imported: **Shorrocks 2013 contributes nothing to the proposal-individualisation question.**

## 5. Opportunity mechanism
N/A â€” **no explicit opportunity mechanism exists in this paper.** The paper models neither feasibility of jobs, nor offer probabilities, nor reservation wages, nor any density over alternatives; it does not vary anything with region, education, demographic type, or local labour market. "Opportunity" enters a Shapley decomposition *only if the analyst defines an opportunity factor upstream and specifies the counterfactual that removes it* â€” which is exactly the JMP's job, not Shorrocks's. Mapping to my three sub-objects:
- **access** (hours / participation / region / year / occupation offers): not modelled here; becomes a factor only by my construction.
- **ability** (wage technology; returns to education/experience; residual productivity): not modelled here; same.
- **occupation** (`loc4`): not modelled; the paper cannot and does not conflate occupation with industry/sector because it models neither â€” **no sector/industry language appears**, so there is no conflation to flag.
**What the omission costs my decomposition:** nothing at the rule level â€” the rule is built precisely to be agnostic about what the factors are. But the paper offers *no* help in (i) defining the access/ability/preference factors, (ii) defining their equalisation counterfactuals, or (iii) arguing those counterfactuals are economically meaningful. The paper itself is emphatic (Â§7 and throughout) that the rule is an attribution device, not a model, so the entire substantive opportunity content of the JMP is upstream of it.

## 6. Welfare object â€” and its place on my $W^1$â€“$W^6$ map
N/A as a welfare construction. The paper computes **no** welfare object â€” no money metric, no equivalent income, no EV/CV, no inclusive value, no reference price/preference/bundle/set. It is explicitly **normatively neutral about the choice of indicator** (derived-by-analogy from Â§2 and Â§7): the rule decomposes whatever aggregate distributional statistic the analyst supplies â€” a Fosterâ€“Greerâ€“Thorbecke poverty index, a Gini, a generalized-entropy/MLD index, a variance â€” without endorsing any. **Placement on my $W^1$â€“$W^6$ map:** none. The paper corresponds to no Independence-of-$y$ / Independence-of-$A$ stance, because it takes no stance on the welfare object at all; it sits one layer *above* the measure menu, as the operator that maps any chosen $\Omega^k$ to its factor contributions. **Verdict: the welfare object is not in this paper (incompatible-as-a-source-of-welfare-objects); the decomposition operator is directly usable on whichever $\Omega^k$ the welfare layer hands it.** Do **not** cite Shorrocks 2013 for anything about money-metric or equivalent-income welfare.

## 6b. Inclusive value and money-metric inversion
N/A â€” the paper uses no inclusive value, no log-sum, no EV/CV, and performs no money-metric inversion. There is no expectation over extreme-value shocks, analytic or simulated. My analytic-in-shocks, importance-sampling inversion is wholly outside this paper. (Stated to forestall overclaim: the "expectation" $\mathbb{E}_{S\subseteq K\setminus\{k\}}$ in Eq. 2.9 is an expectation over *factor-elimination subsets*, a combinatorial average â€” it is **not** an expectation over preference shocks or a log-sum and must never be conflated with my inclusive value $V_i$.)

## 7. Inequality / decomposition content  [the core of this paper]
**Indices the paper treats explicitly:** the Fosterâ€“Greerâ€“Thorbecke decomposable poverty family; the generalized-entropy class $E_c$ (including the mean logarithmic deviation $E_0$ and the Theil index $E_1$ as members); the Gini coefficient; the variance and squared coefficient of variation (for source decomposition). **Decomposition rule:** the **Shapley decomposition** (Eq. 2.8â€“2.9), defined as the expected marginal contribution of each factor over all $m!$ elimination orders; plus the two-stage **Owen** value (Eq. 4.6â€“4.8) for hierarchical/grouped factors. **Counterfactual construction:** a factor is "eliminated" by setting it to a neutralising value â€” e.g. growth eliminated by $G=0$, redistribution by $R=0$ (Â§3.1); between-group inequality eliminated by setting each relative subgroup mean $b_k=1$ (Â§5.1, with the explicit note in footnote 8 that $b_k=\beta>0$ is an alternative); a source eliminated either by zeroing it (the "levels" formulation $F(S)=I(\sum_{k\in S} y_k)$, Eq. 6.2) or by replacing it with its mean (the "differences" formulation $\tilde F(S)=I(\sum_{k\in S} y_k + \sum_{k\notin S}\mu_k e)$, Eq. 6.3). The Â§6 levels-vs-differences distinction is directly relevant to my equalisation design: equalising a channel to its mean (differences) vs zeroing it (levels) are different counterfactuals with different Shapley contributions, and an equally-distributed component contributes zero under the differences formulation but generally non-zero (and possibly negative) under levels.
**Properties established (explicit-in-source):** exact additivity $\sum_k C^S_k = F(K)$ (Eq. 2.7); symmetry/anonymity; order-independence (the average over all $m!$ paths is what removes path dependence, Â§2); and the characterisation (footnote 3, citing Young 1985) that Eq. 2.8 is the *only* symmetric and exact rule whose factor-$k$ contribution depends only on factor $k$'s own marginal-effect set.
**Verdict for my three-way access/ability/preference split: directly reusable.** With $m=3$ the rule is fully exhaustive and order-independent by construction, satisfying my Shapley exhaustiveness gate. The paper is not "two-way vs three-way" in any limiting sense â€” the rule is defined for arbitrary $m$ â€” so no extension is needed to go from its two-factor worked examples (growth/redistribution; within/between) to my three factors. The one genuine design decision the paper forces is **grouping**: if I ever report a two-level hierarchy (e.g. "opportunity = access + ability" as one primary factor, preference as the other), Â§4 warns that the within-opportunity split of access vs ability is sensitive to the grouping *unless* $F$ is separable over {access, ability} (Eq. 4.10), and that aggregation-consistency between the grouped "opportunity" contribution and the sum of its access+ability parts is guaranteed only via the **Owen two-stage** procedure (Prop. 2). This is exactly the welfare-spec concern that the {access, ability} bracket and the {preference} factor be reported jointly and not double-interpreted.

## 8. Identification and the separation of preferences from opportunities  [STRICT]
The paper offers **no identification content** in the structural sense and must not be read as supporting the separation of preferences from opportunities. It is explicit and repeated (Â§2, Â§7, and the concluding remarks) that the rule is an *attribution* device that operates **after** the analyst has (i) defined the factor list, (ii) defined the counterfactual that removes each factor, and (iii) chosen the indicator $I$ â€” all of which are "economic and normative, not mechanical." The credibility of any Shapley decomposition therefore rests entirely on those upstream choices, **not** on the rule. For my paper this is double-edged and must be stated honestly in the identification note: Shorrocks 2013 guarantees that *given* a credible access/ability/preference partition and credible equalisation counterfactuals, the attribution is exact, symmetric, and order-independent â€” but it provides **zero** defence against the "your decomposition is mechanical" referee, because that referee's target is precisely the upstream factor-and-counterfactual definitions that Shorrocks places outside his framework. The separation of preferences ($v$) from opportunities ($g$), and of ability from access *within* $g$, must be identified in my structural model (functional form, the wage-technology vs feasible-set distinction, synthetic-recovery certification) â€” Shorrocks contributes the exhaustiveness of the *split*, never the *identification* of the things being split. Do not soften this: a referee who concedes the Shapley rule still has every license to attack the channel definitions.

## 9. Key results and magnitudes
No empirical magnitudes â€” the paper reports **no elasticities, welfare effects, opportunity shares, or decomposition shares from data.** Its "results" are analytical equivalences (explicit-in-source): (i) for the growthâ€“redistribution poverty change, the Shapley contributions equal the Dattâ€“Ravallion components *averaged over base and final years*, eliminating their residual term $E$ (Â§3.1, Eq. 3.5â€“3.6); (ii) for a multivariate subgroup poverty decomposition with $n$ attributes, each factor receives exactly $1/n$ of its single-attribute contribution (Prop. 4, Eq. 4.21); (iii) for subgroup inequality with the generalized-entropy class, the Shapley split coincides with standard within/between practice **only** for the mean logarithmic deviation $E_0$, and differs for all other $E_c$ (Â§5.1, Eq. 5.10â€“5.11); (iv) for source decomposition, the Shapley split reproduces the "natural" covariance decomposition $C_k=\mathrm{cov}(y_k,y)$ **exactly for the variance** (Â§6, Eq. 6.10), partially for the squared coefficient of variation (Eq. 6.12), and not in closed form for other indices; (v) an equally-distributed income source receives a **negative** Shapley contribution under the levels formulation when the index is scale-invariant and strictly Schur-convex (Prop. 5). For benchmarking my own numbers: the only transferable quantitative lesson is the $1/n$ multivariate-attribution result and the $E_0$-only coincidence â€” both bear on which inequality index I choose, not on plausible magnitudes of an opportunity share.

## 10. Estimators, theorems, or formal results
For each formal result: statement (near-verbatim, LaTeX), assumptions, technique, reusability verdict.

- **Shapley decomposition rule (Eq. 2.8â€“2.9).** Statement: $C^S_k(K,F) = \sum_{S\subseteq K\setminus\{k\}} \frac{(m-1-|S|)!\,|S|!}{m!}\,\Delta_k F(S) = \mathbb{E}_{S\subseteq K\setminus\{k\}}\Delta_k F(S)$. Assumptions: $F:\{S\mid S\subseteq K\}\to\mathbb{R}$ with $F(\varnothing)=0$. Technique: (1) define order-specific marginal contributions; (2) average over all $m!$ elimination orders to remove path dependence; (3) collapse the average to a subset-weighted sum; (4) identify the weights with the Shapley value. **Reusable: yes** â€” this is the JMP's decomposition operator with $m=3$.
- **Exactness (Eq. 2.7).** Statement: $\sum_{k\in K} C^S_k = F(K) - F(\varnothing) = F(K)$. Assumption: $F(\varnothing)=0$. Technique: telescoping along any elimination path, preserved under averaging. **Reusable: yes** â€” this is the welfare-spec exhaustiveness gate ($\sum$ components $= I(\Omega^k)$).
- **Owen two-stage / hierarchical rule (Eq. 4.6â€“4.9).** Statement: allocate to primary factor $L$ its Shapley contribution in the aggregated model, then allocate $L$'s contribution among its constituents by an inner Shapley step; this is **always aggregation-consistent** (Eq. 4.9). Assumptions: a partition $A=\{L_j\}$ of $K$. Technique: nested Shapley averaging (outer over primary factors, inner over secondary). **Reusable: maybe** â€” only if I report a grouped "opportunity = access+ability" primary factor and need its parts to sum consistently; needed precisely when $F$ is **not** separable over the group.
- **Proposition 1â€“2 (separability).** Statement: if $F$ is separable over $L\subseteq K$ (Eq. 4.10: $\Delta_k F(S\cup T)=\Delta_k F(S)$ for $k\in L$), then grouping $L$ does not change contributions of factors outside $L$ (Prop. 1) and the Shapley and Owen decompositions **coincide** and are aggregation-consistent (Prop. 2). Technique: combinatorial lemmas (Appendix Lemmas 1â€“2). **Reusable: yes, as a diagnostic** â€” tells me whether my access/ability split can be reported either grouped or ungrouped without changing the numbers; if access and ability interact (non-separable), the grouped vs ungrouped reports will differ and Owen is required for consistency.
- **Proposition 3 (separable + sufficient).** Statement: if $F$ is separable over each primary factor and each is "sufficient," contributions reduce to $\frac{1}{|A|}M_k(K,F)$, the first-round marginal scaled by the number of primary factors. **Reusable: maybe** â€” gives the clean $1/n$ shortcut (Prop. 4) but its assumptions are unlikely to hold for an interacting structural welfare model; treat as a special-case sanity check, not the working case.
- **Proposition 5 (negative contribution of an equal component).** Statement: under scale-invariance and strict Schur-convexity, an income source distributed equally across the population gets a strictly negative Shapley contribution (levels formulation). **Reusable: as interpretation** â€” warns that a channel that compresses the welfare distribution can carry a negative contribution; relevant if a channel turns out equalising.

## 11. Robustness and specification sensitivity
The paper's own "robustness" content is methodological, and it maps cleanly onto my stress-tests. (1) **Index choice matters:** the Shapley split coincides with conventional within/between subgroup practice only for $E_0$ (MLD) among the entropy class, and with the natural covariance split only for the variance among source decompositions â€” so my reported decomposition shares can move with the inequality index even holding the channels fixed. *Implication:* report the three-way split for the Gini (welfare-spec baseline) but show at least one entropy index (MLD/Theil) as a robustness check, and expect the shares to shift. (2) **Counterfactual choice matters:** levels vs differences (Â§6), and the neutralising value used to "remove" a factor ($b_k=1$ vs $b_k=\beta$, footnote 8; zero vs mean for a source), change the contributions. *Implication:* my channel-equalisation counterfactual (equalise to mean? to a reference? to the access-/ability-equalised population distribution?) is a first-order specification choice that must be stated and stress-tested. (3) **Grouping matters** (Â§4): the access-vs-ability split inside a grouped "opportunity" factor is sensitive to grouping unless separability holds. The paper does **not** address number-of-draws, choice-set size, multistart, effective-sample-size, or circumstance partitions â€” those robustness axes are mine and get no guidance here.

## 12. What I can cite this paper for
- That the Shapley decomposition is the exact, symmetric, order-independent additive attribution rule for any indicator $I=f(X_1,\dots,X_m)$, computed as each factor's marginal contribution averaged over all elimination orders (Eq. 2.8â€“2.9, Eq. 2.7).
- That this rule unifies and, in benchmark cases, reproduces or improves upon the prior patchwork of poverty/inequality decomposition formulas (abstract; Â§7).
- That it eliminates the residual/interaction term required by ad hoc decompositions (the Dattâ€“Ravallion residual; the Gini interaction term) â€” Â§3.1, Â§5.2.
- That the Shapley split coincides with standard within/between practice **only** for the mean logarithmic deviation among entropy indices, and with the natural covariance decomposition **only** for the variance among source decompositions (Â§5.1, Â§6).
- That for grouped/hierarchical factors the **Owen** two-stage value delivers aggregation consistency, coinciding with Shapley under separability (Â§4, Prop. 2).
- That the rule is index- and model-agnostic and that its outputs depend on the analyst's upstream choice of factors, counterfactuals, and indicator (Â§2, Â§7) â€” useful as the honest caveat in my own decomposition section.
- That for complex models the contributions generally lack closed form and require algorithmic computation, ideally with standard errors (Â§7) â€” supports my numerical-plus-bootstrap implementation.

## 13. What I should NOT cite this paper for  [overclaim risks]
- **Not** a source for any welfare object: it computes no money-metric, equivalent-income, EV/CV, or inclusive-value welfare, and corresponds to **no** $W^1$â€“$W^6$ measure or Ind-$y$/Ind-$A$ stance. Do not attribute the welfare family or its normative readings to Shorrocks.
- **Not** an identification result: it does not identify or justify the separation of preferences from opportunities, or of ability from access. Citing it as support for the *credibility* of the access/ability/preference partition would be an overclaim â€” it explicitly places that work upstream and outside its scope.
- **Not** a structural or opportunity-mechanism paper: no choice set, no $g$, no offer probabilities. Do not read its set function $F(S)$ as a feasible-set or opportunity object.
- **Not** about occupation, industry, or sector â€” the paper models none of these; there is no `loc4`/`lindi` content and therefore no occupation-as-access claim to draw from it.
- **Boundary flags:** (a) two-way examples (growth/redistribution; within/between) are *illustrations*, not a limit â€” but do not cite a specific two-factor formula (e.g. Eq. 3.5) as if it were the three-way rule; cite the general Eq. 2.9 for the three-way split. (b) The combinatorial "expectation over subsets" in Eq. 2.9 must **never** be presented as an expectation over preference shocks or as my inclusive value. (c) "Random opportunities" framing is irrelevant here â€” the paper is deterministic set-function machinery; nothing in it bears on the deterministic-vs-random opportunities question.
- **Theory-paper boundary:** Shorrocks 2013 is decomposition methodology and belongs to the empirical JMP's decomposition layer. It is unrelated to the Haydarâ€“Maniquet axiomatic theory paper; do not let its "characterisation/axioms" language (which refers to characterisations of the Shapley *value*, not of welfare measures) be read as supporting the companion paper's measure characterisation, and do not read the JMP's use of it as a theory contribution.

## 14. Direct quotes worth citing
Short verbatim extracts with page numbers (each â‰¤ ~12 words; one per locus):
- p. 102: the objective is to assign contributions to each factor so that the total is the sum of factor contributions. [paraphrase-safe; verify exact wording if quoting]
- p. 103: the rule averages each factor's marginal impact over all elimination sequences. [paraphrase-safe; verify exact wording if quoting]
- p. 104: contributions "sum up to the amount" requiring explanation (exactness). [verify page/wording]
- p. 121 (Â§7): the procedure "can be applied to a wide range of problems which cannot be solved with existing techniques." [verify exact wording before quoting]

> **Note (honesty flag):** I have **not** lifted exact verbatim strings with certified page-precision from the PDF for Â§14; the loci above are paraphrase-safe pointers. Before any of these enters the draft as a quotation, open the PDF and confirm the exact words and page. Marked **[verify]**.

## 15. Open questions and risks for my draft
- **The $F(\varnothing)=0$ / residual problem (Â§2, fn 1).** If equalising all three channels does not drive welfare-measure inequality to exactly zero, there is an implicit residual factor and my exhaustiveness gate must be stated against the renormalised "surplus due to identified factors," not raw $I(\Omega^k)$. I must check this empirically and report it.
- **Counterfactual definition is a first-order choice the paper leaves to me.** Equalise each channel to its mean? to a reference distribution? The Shapley numbers depend on it; the welfare-spec's "what is equalised / held fixed / zeroed" must be pinned and stress-tested (cf. Â§6 levels-vs-differences).
- **Grouping / Owen decision (Â§4).** Whether to report "opportunity = access + ability" as a grouped primary factor, and if so whether to use Owen for aggregation consistency, hinges on separability of $F$ over {access, ability}. If access and ability interact in the welfare measure (plausible, since both enter $g$), grouped and ungrouped reports will differ â€” I must decide and disclose which I report.
- **Index sensitivity.** Shares may shift between Gini and entropy indices even with channels fixed; the robustness section must show this rather than report a single-index headline as if index-invariant.
- **Inference.** The paper flags but does not provide standard errors; the entire cluster-robust bootstrap apparatus is mine, and the welfare-spec's per-component CI asymmetry (tight opportunity, wide preference) is not something Shorrocks speaks to.

## 16. TL;DR for retrieval
Shorrocks 2013 is the canonical, data-free methodological source establishing the **Shapley decomposition** as the unique exact, symmetric, order-independent additive rule for attributing any distributional indicator to its factors, plus the **Owen** two-stage extension and separability conditions for grouped factors â€” it is the operator the JMP applies to its three-way **access / ability / preference** split of welfare-measure inequality, satisfying the exhaustiveness gate by construction. It supplies **no** welfare object, **no** opportunity mechanism, and **no** identification of the channels â€” all of which are upstream â€” so it must be cited for the *attribution machinery and its exactness/grouping properties only*, never for the credibility of the channel partition, the welfare family $W^1$â€“$W^6$, or anything structural. Its load-bearing warnings for my draft are the $F(\varnothing)=0$/residual normalisation, the counterfactual-definition dependence, the grouping/Owen sensitivity, and the index-dependence of the resulting shares.
