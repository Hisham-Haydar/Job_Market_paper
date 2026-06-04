# Capéau, Decoster & Dekkers 2016 — Estimating and Simulating with a Random Utility Random Opportunity Model of Job Choice: Presentation and Application to Belgium

> Source of truth: the attached PDF (*International Journal of Microsimulation* (2016) 9(2) 144–191). The journal masthead dates the article 2016; the project's working citation key uses 2015. Both are recorded; the **2016** outlet date is what the PDF prints. Pages cited below are the printed journal pages (144–191).
> Extraction discipline: claims are tagged **[explicit]** (stated in the PDF), **[analogy]** (derived by mapping to my JMP, not stated in the source), or **[not established]** (absent from the source). `[verify]` marks anything I could not confirm against the PDF text.

## 0. Metadata

- **BibTeX key:** `Capeau_et_al_2015_RURO` (project key; printed outlet year is 2016) [explicit: outlet year 2016]
- **Authors:** Bart Capéau (KU Leuven), André Decoster (KU Leuven), Gijs Dekkers (Federal Planning Bureau) [explicit, p.144]
- **Year:** 2016 (printed); 2015 (project key) [explicit / project convention]
- **Outlet:** *International Journal of Microsimulation*, 9(2), 144–191 [explicit, p.144]
- **DOI/URL:** [verify] — no DOI printed on the supplied pages; the IJM volume/issue/page string (9(2) 144–191) is the locator.
- **PDF filename:** `Capéau_et_al__-_2015_-_Estimating_and_Simulating_with_a_Random_Utility_Random_Opportunity_Model_of_Job_ChoicePresentation_a.pdf`
- **Tier:** T1A.
- **JMP blocks served:** estimation; identification; opportunity-mechanism (access **and** ability); data-infrastructure (EUROMOD/EU-SILC); motivation. It does **not** serve the welfare or decomposition blocks (the paper computes no welfare object and no inequality decomposition — §6, §7 below).

## 1. One-paragraph relevance to my JMP

This is the closest published methodological template for my structural layer: it is a worked RURO/latent-jobs estimation on EU-SILC processed through EUROMOD, the same data-and-microsimulation infrastructure I use, with the choice modelled as selection among job packages of (wage, hours) plus a non-market alternative, and with disposable income for every sampled alternative computed by EUROMOD rather than from a stored income column [explicit, pp.148–149, 162]. It speaks directly to all three of my channels: the wage-offer distribution `g1(w)` is my **ability** sub-block (returns to education and potential experience, lognormal dispersion `σ`); the hours-offer density `g2(h)` and the job-offer intensity `q(x_opp)` are my **access** sub-block (hours availability and market/participation intensity, with a group-specific unemployment-rate shifter on `q`); and the Box–Cox `Ψ`/`V` over consumption and leisure is my **preference** block [explicit, pp.158–159]. It is the canonical statement of the sampling-of-alternatives correction I must carry (the `P(0,0)/P(w,h)` proposal weight, eq. 23/25), and of the `q`/`γ1` non-separability normalisation [explicit, pp.161–162]. Its limits relative to my paper are equally informative: it is **two-side** (preferences vs opportunities), not three-way; it computes **no** welfare measure and **no** decomposition; it has **no occupation channel** (occupation/sector appear nowhere in the opportunity mechanism); and it frames opportunities as genuinely **random** (Poisson offer arrivals), which is exactly the framing my design removes.

## 2. Data and setting

- **Country / year:** Belgium, EU-SILC **2007** (collected 2007) [explicit, p.163].
- **Dataset:** Belgian EU-SILC; full dataset 6,348 households / 15,493 individuals, representative of Belgian private households (collective households/institutions excluded) [explicit, p.163].
- **Sample unit:** three separately estimated sub-samples — **couples** (different-sex reference person + partner), **single females**, **single males** [explicit, p.163].
- **Sample sizes:** **1,457 couple households, 571 single females, 449 single males** [explicit, pp.164–165, Table 1].
- **Selection:** reference person (and partner, for couples) aged 16–64 and available for the labour market; excluded if sick, in education, disabled, or (pre)retired; **self-employed excluded** (unreliable hours/income); mixed households where only one partner is available excluded; households with labour-market-age children still co-resident dropped [explicit, pp.163–164].
- **Key variables:** gross household labour income (sum of members' earnings); disposable income via EUROMOD (taxes and employee SSC deducted, social transfers added, full take-up of social assistance assumed) [explicit, p.164]; **potential experience** (age − 15 low-educ, age − 19 middle, age − 23 high; age excluded from the wage equation due to collinearity) [explicit, p.164]; education in three levels (low/middle/high); region (Brussels/Flanders/Wallonia); number/age-bands of children; gender [explicit, Tables 1, 3].
- **External data:** **type-specific unemployment rate** (by age × sex × education, Eurostat 2007) merged as a proxy for job availability and used as an exclusion restriction on `q` [explicit, pp.164–165, Table 2; p.157].
- **Budget-set construction:** disposable income `c = f(w,h;x_f)` is **not** given a functional form; for each drawn `(w,h)` it is computed from Belgian tax rules in **EUROMOD version F5.5** using SILC information on non-earned income and household characteristics [explicit, p.162; p.190 n.15].

**Transport to my France pooled 2015–2017 EUROMOD cross-section:** strong on infrastructure, partial on design. Same family of data (EU-SILC) and same microsimulator (EUROMOD) used to price every alternative — directly transportable [analogy]. Differences I must record: single cross-section (2007) vs my **pooled three-wave** design (no pooling/clustering issue arises for them); **no occupation variable** in their model vs my `loc4` access object; their identifying opportunity shifter is the **type-specific unemployment rate**, an external merge analogous to (but coarser than) the region×year continuous covariates I have considered. **Features they have that I do not / do differently:** an explicit **external opportunity instrument** (type-specific unemployment) entering `q` under an exclusion restriction [explicit, p.157] — I currently have **no external instrument**; they rely on a single cross-section and on functional-form/identification arguments rather than synthetic recovery. **Features I have that they lack:** an occupation access channel; a pooled multi-year sample; a welfare-and-decomposition layer.

## 3. Model and objects (object-by-object map to mine)

| Their object | Symbol / form | My object | Match? |
|---|---|---|---|
| Latent job set + non-market alternatives | jobs `j ∈ J`, non-market `i ∈ I`, `Z = I ∪ J` | latent-jobs set `C_i` | **Yes** [explicit, pp.148–149] |
| Systematic utility | `V(c, T−h; x_V)`, Box–Cox; induces `Ψ(w,h)` via `c=f(w,h;x_f)` | preference utility `v_i(c,ℓ)` | **Yes** (both Box–Cox in consumption & leisure) [explicit, pp.149–150, 158] |
| Random utility term | `ε(z)` enters **multiplicatively**, `U = V·ε`, with `U_B` Fréchet (α=1) | additive EV1 shock, log-sum inclusive value | **Functionally equivalent, different parameterisation** — their multiplicative-Fréchet form is the log-level of my additive-Gumbel form [analogy; the Fréchet/α=1 result is explicit, pp.152–155] |
| Hours-offer density | `g2(h)`, piecewise-uniform with peaks at half/three-quarter/full time | `log h` access term | **Yes — access** [explicit, p.159] |
| Wage-offer density | `g1(w)`, lognormal, mean depends on education + potential experience, dispersion `σ` | `log w` (ability) sub-block | **Yes — ability** [explicit, p.159] |
| Job-offer intensity | `q(x_opp) = exp(η_q' x_opp)`; relative intensity of market vs non-market | `log market` access term | **Yes — access/participation** [explicit, p.158] |
| Budget map | `c = f(w,h;x_f)` via EUROMOD | EUROMOD disposable income | **Yes** [explicit, p.162] |
| Occupation/sector channel | **none** | `loc4` occupation access | **Absent in source** [explicit by omission — Table 3, p.166] |
| Couples | unitary joint model, leisure assignable, leisure-complementarity term `β_{h1,h2}` | couples joint decision unit | **Yes** [explicit, p.158, Appendix A2 p.186] |

**Wage as a job attribute, not a fixed characteristic.** A defining feature, shared with my design: the wage is **part of the job offer**, drawn from `g1(w)`, not a fixed individual productivity endowment; the denominator of the choice probability therefore sums over `(w,h)` pairs, not over hours alone for a fixed wage (their eq. 15 vs eq. 16) [explicit, p.156; p.190 n.2].

**Does any attribute enter BOTH utility and the opportunity mechanism?** Examined directly via their specification table (Table 3, p.166): **education** enters preferences (`x_V`), job-offer intensity (`x_opp`), and the wage equation (`x_w`); **region** enters preferences and job-offer intensity; **gender** enters all blocks. So education and region appear in *both* the utility side and the opportunity side [explicit, Table 3]. The paper does **not** flag this as a problem and offers **no** dedicated identification defence of the double-entry beyond the general non-parametric identification argument and the unemployment-rate exclusion restriction on `q` (§8 below) [explicit by absence]. This is directly relevant to my own discipline of *not* putting occupation in both blocks at baseline: their precedent shows education/region double-entry is treatable when an external `q`-shifter and functional-form restrictions carry identification, but they do not isolate the cost of the double-entry [analogy].

## 4. Estimation method

- **Likelihood:** the choice probability of a job `(w,h)` is `φ(w,h) = Ψ(w,h)·q·g1(w)·g2(h) / [Ψ(0,0) + ∫∫ Ψ(r,t)·q·g1(r)·g2(t) dt dr]` (eq. 15), with `φ(0,0)` the non-market analogue (eq. 15′) [explicit, p.156]. Couples: a four-case likelihood (both work / only partner 1 / only partner 2 / neither), eq. 15″ in Appendix A2 [explicit, p.186].
- **Choice-set construction:** the offer sets `W`, `H` are unobserved, so a set `D` of `(w,h)` alternatives is **sampled from a prior `P(w,h)`**; the observed choice is always included [explicit, p.160]. Wages drawn lognormal `(m, ς)`; hours drawn uniform on `[H_min, H_max)`; the non-market alternative drawn with the observed inactivity rate `π0_obs` (males: `π0=.104, m=2.71, ς=.308`; females: `.246, 2.63, .297`) [explicit, p.162; p.191 n.14].
- **Proposal / prior correction:** **yes** — the simulated likelihood (eq. 23, reduced to eq. 25) carries the weight `P(0,0)/P(w,h)` on every non-base term, via Bayes' law from `P(D|(w,h))` (eq. 20–22) [explicit, pp.160–161]. This is the McFadden sampling-of-alternatives correction (they cite McFadden 1978, Ben-Akiva–Lerman 1985, Train 2009) [explicit, p.191 n.13]. **Always well defined here:** `P(0,0)=π0_obs>0` and `P(w,h)>0` on the lognormal×uniform support, so the ratio is finite [analogy — they do not state a degeneracy check].
- **Normalisation / scale:** `Ψ(0,0)` normalised (a utility-level normalisation) to identify `q` (eq. 19) [explicit, p.157]. Critical non-separability: the offer-intensity constant `exp(η_{q,0})` and the hours-density base level `γ1` enter the likelihood only as a product and **cannot be estimated separately**; `γ1` is pinned by the density's integrate-to-one identity (eq. 24), and `η_{q,0}` is then backed out (eq. 25 uses rescaled `g̃2 = g2/γ1`, `q̃ = γ1·q`) [explicit, pp.161–162].
- **Numerical method / starting values / multistart:** [verify] — the supplied pages state a maximum-simulated-likelihood construction but do **not** report the optimiser, starting values, or any multistart procedure. **[not established]** in the text provided.
- **What separates preferences from the opportunity mechanism:** the non-parametric identification argument (§8 below) plus the unemployment-rate exclusion restriction on `q` [explicit, p.157]. Note the honest caveat that `Ψ(w,h)` and `g2(h)` are **not** separately non-parametrically identified — the hours peaks could in principle be attributed to preferences instead (p.157, p.191 n.17).

**Verdict — reusable for my RURO/JAX pipeline?** **Yes, as the structural template.** Reusable steps: (i) the sampled-choice-set + `P(0,0)/P(w,h)` correction maps exactly onto my per-row `prior` column and `−log π` term; (ii) the EUROMOD-prices-every-alternative loop is my build pattern; (iii) the `q`/`γ1` non-separability is a normalisation I must replicate or consciously break. **Not reusable as-is:** their multiplicative-Fréchet algebra (I use additive-Gumbel/log-sum); their lack of occupation; their single-cross-section identification. **[verify]** their optimiser before citing any numerical-implementation detail.

## 4b. Proposal / sampling-of-alternatives correction

- **How alternatives are sampled:** from `P(w,h)` = lognormal in `w` × uniform in `h`, plus the non-market point mass at `π0_obs` (eq. 26) [explicit, p.162].
- **Is the proposal individualised?** **Partly, but less than mine.** The prior `P(w,h)` as written uses **common** lognormal parameters `(m, ς)` within gender (separate male/female values given) and a **common** inactivity probability `π0_obs` within gender [explicit, p.162, n.14] — i.e. individualised by gender only, *not* by household covariates. There is **no occupation-conditioned draw** (no occupation in the model). This contrasts with my proposal, whose wage mean is household-specific (`μ_i = X_i b + δ_occ[loc4_i]`) and whose occupation channel is gender×education-stratified [analogy — the contrast is to my own design, not stated in the source].
- **Is the correction McFadden-style?** **Yes** — Bayes'-law reweighting of sampled alternatives, citing McFadden (1978) and Ben-Akiva–Lerman (1985) [explicit, p.191 n.13].
- **Does each drawn alternative carry its own log-prior?** **Yes** — the `P(0,0)/P(w_i,h_i)` factor is per-alternative (eq. 20, 23) [explicit, pp.160–161].
- **Relation to my importance-sampling welfare integrator:** their estimation-stage correction is the exact analogue of my welfare-stage `−log π(j)` term; my concern that only wage/occupation are individualised while hours/employment are common is *more* acute in their setup, where the **entire** proposal is common-within-gender. Their design therefore does not test the well-conditioning question my proposal audit addresses; it is a precedent for the *form* of the correction, not for proposal individualisation [analogy].

## 5. Opportunity mechanism — [MOST IMPORTANT; split by channel]

The opportunity side is a **genuine stochastic offer process**: jobs and non-market activities arrive via **independent inhomogeneous spatial Poisson processes**, so the number of offers of any type with utility ≥ u is Poisson, and the max attainable utility over a region is Fréchet (location 0, shape α=1) [explicit, pp.151–155, Appendix A1 pp.184–185]. This is the literal "random opportunities" content my design deliberately drops. The intensity is `g2(h)·g1(w|h)·λ1(υ)` with `λ1(υ)=q/υ²` (and `λ0(υ)=1/υ²` for non-market), the inverse-square form guaranteeing IIA in the job-choice probabilities (Dagsvik 1994) [explicit, pp.151–154].

Mapping to my three sub-objects:

- **access — hours availability.** `g2(h)`: piecewise-uniform density over labour-time regimes with a baseline level `γ1` and **peaks** (estimated bumps `γ1·exp(γ_{k+1})`) around half time (18.5–20.5h), three-quarter time (29.5–30.5h), and full time (37.5–40.5h); `H_min=1h`, `H_max=70h` (p.162); the only covariate allowed to shift it is **gender** [explicit, p.159, Fig. 1]. Maps to my `log h` access term.
- **access — market/participation intensity.** `q(x_opp) = exp(η_q' x_opp)`: the relative intensity of suitable job offers vs non-market opportunities; covariates are a constant, region, education, gender, and the **group-specific unemployment rate** (the exclusion restriction) [explicit, pp.157–159, Table 3]. Reported normalised as `q/(1+q)` in figures (p.191 n.18). Maps to my `log market` access term.
- **ability — wage technology.** `g1(w;x_w)`: lognormal with mean a function of **education** and **potential experience** (quadratic) and dispersion `σ`; gender-specific [explicit, p.159, Table A3]. This is exactly my ability sub-block (returns to education + experience, residual dispersion `σ`). Estimated `σ ≈ 0.26` for both sexes; education and experience shift the offer distribution rightward, with a turning point in experience (≈37y males, ≈32y females) [explicit, pp.168, 188].
- **occupation.** **None.** Occupation/sector enters neither utility nor opportunities; there is no `loc4`-type object and no industry/NACE object anywhere in the model (Table 3, p.166) [explicit by omission]. **No sector/industry conflation risk arises** because neither concept is present.

**Does feasibility vary with circumstances?** Yes: by gender (all offer blocks), education and region (`q` and `g1`), potential experience (`g1`), and the external age×sex×education unemployment rate (`q`) [explicit, Table 3, pp.158–159].

**Functional forms (exact):**
- `ln q(x_opp) = η_q' x_opp` (log-linear) [explicit, p.158].
- `g1(w;x_w) = (1/(w·σ·√(2π)))·exp(−½((ln w − δ_{g1}' x_w)/σ)²)` (lognormal) [explicit, p.159].
- `g2(h)` piecewise-uniform with peak multipliers `exp(γ_{k+1})` (form on p.159).
- `λ1(υ)=q/υ²`, `λ0(υ)=1/υ²` (p.151, p.154).

**Cost to my decomposition if such a mechanism were absent:** they *have* the mechanism, so the relevant lesson is the converse — their honest statement that `Ψ(w,h)` and `g2(h)` are not separately non-parametrically identified (p.157) is precisely the preference/access confound my access component must survive; without the `q`-exclusion restriction the access channel would not be cleanly separated from preferences [explicit caveat, p.157].

## 6. Welfare object — and its place on my W¹–W⁶ map

**The paper computes NO welfare object.** There is no money-metric, no equivalent income, no equivalent/compensating variation, and no inclusive-value welfare statistic anywhere in the supplied text [explicit by exhaustive omission — the results sections are §5 estimation, §6 fit/elasticities, §7 an education counterfactual on participation/hours]. The "fit" exercise compares simulated vs observed disposable-income, wage, and hours **distributions** (Figs 6–11), and the counterfactual reports **participation rates and mean hours** (Tables 6–7), not welfare [explicit, pp.171–178].

**Place on my W¹–W⁶ map:** **N/A — the source contains none of W¹–W⁶ and makes no compensation/responsibility (Ind-y / Ind-A) distinction.** Any mapping would be invented. I must **not** cite this paper for welfare-measure content.

**Verdict:** incompatible as a welfare source; it is an *estimation and simulation* template only. The one bridge to my welfare layer is purely computational: the same `Ψ`, `g`, and proposal correction they estimate are the inputs my ex-ante inclusive value `V_i` is built from — but they never form that inclusive value as a welfare quantity.

## 6b. Inclusive value and money-metric inversion

- **Inclusive value as welfare core:** **No.** The Fréchet/log-sum structure is used to derive **choice probabilities** (the denominator of eq. 15), not as a welfare statistic [explicit, pp.155–156].
- **Money-metric inversion:** **N/A** — no money figure is recovered by inverting an own-utility map; no EV/CV is computed [explicit by omission].
- **Expectation over shocks analytic or simulated?** For **estimation**, the expectation is taken **analytically** — the Poisson/Fréchet algebra yields the closed-form choice probability with no shock draws (eqs. 13–15) [explicit, pp.155–156]. For **simulation/fit**, they *do* draw Fréchet shocks `ε(w_s,h_s)` per sampled alternative and take the simulated argmax (p.163) [explicit] — i.e. simulation is by drawn shocks, estimation is analytic. This is relevant to my design choice to keep the welfare expectation **analytic in the shocks** (closed-form log-sum): their estimation step is the precedent; their simulation step is the thing I avoid for welfare [analogy].

## 7. Inequality / decomposition content — [three-way where relevant]

**No inequality index and no decomposition of any kind.** No Gini/MLD/Theil/Atkinson; no Shapley/Shorrocks/factor/subgroup/RIF decomposition [explicit by omission].

The **only** "decomposition-flavoured" content is the **preferences-vs-opportunities channel attribution in Table 7** (p.178): they re-simulate the education counterfactual switching the education level *only in preferences* ("alt pref") vs *only in the opportunity blocks* ("alt opp"), and read off which channel drives the change in **participation and mean hours**. They conclude the education effect "run[s] predominantly through the channel of opportunities rather than through preferences" [explicit, pp.178–179]. This is a **two-way, behavioural (participation/hours), counterfactual-simulation** attribution — **not** a welfare-inequality decomposition, **not** Shapley, **not** order-independent, and it equalises nothing; it swaps a covariate's value between blocks.

**Verdict — reusable for my three-way access/ability/preference Shapley–Shorrocks split?** **No, not as a decomposition.** It is useful only as (a) a conceptual precedent that the preference/opportunity channels can be separately *toggled* once the structural model is estimated, and (b) a warning that their toggle is on **behaviour**, not on a **welfare** object, and is **two-way** (preference vs opportunity), not three-way. To reach my split it would need: a welfare object (absent), an inequality index (absent), the Shapley equalisation machinery (absent), and the ability/access subdivision *within* opportunities (they keep wage and hours/`q` separate in estimation but never separate them as inequality sources) [explicit by absence].

## 8. Identification and the separation of preferences from opportunities — [STRICT]

The identification argument (their §3.2, pp.157–158) is the backbone item for my identification note. Stated explicitly:

1. **Identify `Ψ(w,h)·g2(h)`:** take two observationally-equivalent groups working different hours `h1, h2` at the **same** wage `w`; the population ratio `φ(w,h1)/φ(w,h2) = [Ψ(w,h1)g2(h1)]/[Ψ(w,h2)g2(h2)]` (eq. 17); varying `w` traces out `Ψ(w,h)g2(h)` [explicit].
2. **Identify `g1(w)`:** take groups at the **same** hours `h`, different wages `w1,w2`; the ratio (eq. 18) isolates `g1(w1)/g1(w2)`, pinned to a density by `∫ g1 = 1` [explicit].
3. **Identify `q`:** compare workers vs non-workers in an observationally-equivalent group (eq. 19); with `Ψ(0,0)` normalised, `q` is identified [explicit].
4. **Exclusion restriction:** a **group-specific unemployment rate** is added to `q`, assumed to shift labour demand but **not** preferences — improving identification of `q` beyond the non-parametric argument [explicit, p.157].

**Honest non-identification caveat (critical to carry):** `Ψ(w,h)` and `g2(h)` are **NOT** separately non-parametrically identified; the observed hours peaks could be explained by preferences instead, and the resolution is a **functional-form justification** of Box–Cox preferences (citing Dagsvik–Røine Hoff 2011, Dagsvik 2013) [explicit, pp.157–158, p.191 n.17]. They also flag that including gross wage *and* hours separately in `f` (for the Belgian work bonus) may threaten non-parametric identification (p.190 n.5).

**Transport to my France pooled cross-section (no panel, no external instrument):** Their argument is **cross-sectional** (observationally-equivalent groups), so it transports in principle to a cross-section — good news for me [analogy]. But two of their load-bearing devices I currently lack: (i) the **external unemployment-rate exclusion restriction** on `q` — I have no external instrument at baseline, though region×year continuous covariates are the natural analogue I have considered; (ii) their reliance on the **functional-form justification** of Box–Cox to break the `Ψ`/`g2` confound — I share Box–Cox, so I inherit both the device and its fragility. My defence against the "your decomposition is mechanical" referee should note that **the preference/access confound is acknowledged in the founding RURO-estimation paper itself** and is resolved there by functional form + an exclusion restriction, not by data variation alone [explicit, pp.157–158]. My synthetic-recovery standard is a *stronger* discipline than their in-sample/functional-form argument; the source does not use synthetic recovery [explicit by absence — they report no recovery experiment].

## 9. Key results and magnitudes

All figures **[explicit]**, Belgium EU-SILC 2007, from the named tables.

- **Aggregate wage elasticities (Table 4, p.174):** shift each gender's wage-offer distribution right by 10% (add ln 1.1 to the location). Total elasticities: couple female **0.6445**, couple male (own, male shift) **0.3304**, single female **0.6877**, single male **0.4569**; **cross** (partner) elasticities negative (couple male under female shift **−0.1734**; couple female under male shift **−0.2014**). Intensive-margin and part-in/part-out components tabulated. They note these totals are "rather large" vs micro Marshallian estimates but argue they are conceptually macro-like (include the extensive margin) and that RURO frictions push them *down* relative to macro figures [explicit, pp.174–175].
- **Wage-offer dispersion:** `σ ≈ 0.264` (M), `0.261` (F) (Table A3, p.189) [explicit].
- **Wage-offer education/experience gradient:** high education `+0.260` (M), `+0.291` (F) on log wage; low education `−0.147` (M), `−0.095` (F); experience enters with a positive linear and negative quadratic term (turning points ≈37y M, ≈32y F) [explicit, pp.168, 189].
- **Offer intensity `q`:** education raises offer availability per se; for **males** a higher type-specific unemployment rate *raises* estimated suitable-offer intensity (coefficient `+0.338`, t≈1.50, not significant), partially offsetting education; for **females** the unemployment-rate coefficient is small/negative (`−0.072`) [explicit, pp.169–170, 189].
- **Fit (§6.1):** couples mean simulated consumption €3,070/m vs €3,143 observed; single-male consumption €1,585 fitted vs €1,588 observed; non-participation over-estimated; three-quarter-time peak under-fitted [explicit, pp.171–173].
- **Education counterfactual (§7, Tables 5–7):** equalising male to female education has a **modest** participation/hours effect, concentrated in **men** (single males 30–45: participation +1.5 to >7pp; mean hours +0.5 to >4h); female labour supply barely moves; the effect runs **predominantly through opportunities, not preferences** (Table 7) [explicit, pp.175–179].

**Benchmarking value for me:** their `σ≈0.26` wage-offer dispersion and the education/experience gradients are a plausibility yardstick for my ability sub-block; their finding that an education shock works mainly through the **opportunity** channel is a (behavioural, not welfare) precedent that the opportunity channel carries real weight — consistent with, but not evidence for, a material opportunity share in my **welfare** decomposition [analogy — do not present their behavioural result as a welfare-share result].

## 10. Estimators, theorems, or formal results

1. **Fréchet max-utility result.** Statement [explicit, p.153]: under the Poisson offer process with intensity `g2(h)g1(w|h)λ1(υ)` and `λ1(υ)=q/υ²`, the maximum attainable utility `U_B` over region `B` is Fréchet, `P(U_B<u)=exp(−σ_B/u)` with scale `σ_B = ∫∫ g2(t)g1(r|t) qΨ(r,t) dr dt`, location 0, shape α=1. Technique: number of offers above utility `u` is Poisson; `P(U_B<u)=P(N=0)`; integrate the inverse-square intensity (eq. 6–8). **Reusability:** background to my log-sum (the additive-Gumbel analogue); I do not reuse the Fréchet form directly. Verdict: **maybe / conceptual** [analogy].
2. **Choice probability (eq. 15).** `φ(w,h)=Ψ(w,h)q g1(w)g2(h) / [Ψ(0,0)+∫∫Ψ(r,t)q g1(r)g2(t)dt dr]`; assumption `g1(w|h)=g1(w)` (wage-hours independence) for identification [explicit, p.156]. **Reusability: yes** — structural analogue of my per-row value plus log-sum; the wage-hours independence assumption is a modelling choice I should state explicitly if I adopt it.
3. **Sampled-set simulated likelihood (eq. 23/25).** With proposal `P(w,h)` and weight `P(0,0)/P(w,h)`; `q`/`γ1` collapse to `q̃=γ1 q`, `g̃2=g2/γ1`, with `γ1` from the integrate-to-one identity (eq. 24) [explicit, pp.160–162]. **Reusability: yes, directly** — this is the correction and normalisation my pipeline must implement; verdict **yes**.
4. **Couples likelihood (eq. 15″, Appendix A2).** Four-regime joint probability with independent per-partner offer processes and a joint `Ψ(w1,h1,w2,h2)` carrying a leisure-complementarity term [explicit, p.186]. **Reusability: yes** — template for my 901-alternative joint couples grid.

No numbered theorems are stated in the supplied pages; the formal content is the Poisson→Fréchet derivation and the likelihood algebra above [explicit].

## 11. Robustness and specification sensitivity

- **What they vary:** the specification table (Table 3) fixes which covariates enter each block; they do **not** report sensitivity to choice-set size `|D|`, number of draws, or number of optimiser starts in the supplied pages [verify / not established].
- **Acknowledged fragilities:** (i) `Ψ`/`g2` not separately non-parametrically identified — hours peaks attributable to preferences instead (p.157, n.17); (ii) including `w` and `h` separately in `f` may threaten identification (n.5); (iii) the model is **static**, **not an equilibrium/matching model**, frictions taken as given (§8 conclusion, p.179); (iv) sample is not representative of the working-age population (selection on labour-market availability), handled in the counterfactual by re-weighting to MIDAS education distributions (p.175).
- **For my stress-tests:** their honest `Ψ`/`g2` confound tells me exactly where my **access vs preference** boundary is weakest (hours peaks), and their absence of a choice-set-size/draw-count robustness report is a gap I should *not* replicate — my welfare-integration ESS gate and draw-growth stability gate are the discipline they lack [analogy].

## 12. What I can cite this paper for

- The **canonical RURO/latent-jobs estimation template** on EU-SILC + EUROMOD, with wage as a drawn job attribute and EUROMOD pricing every sampled alternative [explicit, pp.148–149, 162].
- The **sampling-of-alternatives (proposal/prior) correction** in a RURO context, McFadden-style, per-alternative `P(0,0)/P(w,h)` weight (eq. 20–25) [explicit, pp.160–162].
- The **`q`/`γ1` non-separability** and its resolution by the hours-density normalisation identity (eq. 24) [explicit, pp.161–162].
- The **non-parametric identification argument** for separating wage offers, hours offers, and offer intensity from preferences, **and its explicit limit** (`Ψ`/`g2` not separately identified), plus the **unemployment-rate exclusion restriction** as a labour-demand shifter on `q` [explicit, pp.157–158].
- The **Box–Cox preference form** for consumption/leisure in RURO and its functional-form justification lineage (Dagsvik–Røine Hoff 2011; Dagsvik 2013) [explicit, p.158].
- The **couples unitary joint-choice likelihood** with assignable leisure and a complementarity term (Appendix A2) [explicit, p.186].
- The **behavioural** finding that an education counterfactual operates mainly through the **opportunity** channel rather than preferences — as a *behavioural* result on participation/hours [explicit, pp.178–179].
- **EUROMOD F5.5** as the gross-to-net engine for Belgian SILC alternatives, full social-assistance take-up assumed [explicit, p.162, p.164].

## 13. What I should NOT cite this paper for — [overclaim risks]

- **NOT** for any **welfare** measure, money-metric, equivalent income, EV/CV, or inclusive-value welfare statistic — the paper computes none [explicit by omission, §6/§6b above].
- **NOT** for an **inequality decomposition** of any kind, and **NOT** for a three-way access/ability/preference split. Its Table 7 is a **two-way, behavioural** (participation/hours) counterfactual toggle, not a welfare-inequality Shapley decomposition. Citing it as a decomposition precedent would be an overclaim [explicit, §7 above].
- **NOT** for W¹–W⁶ or any compensation/responsibility (Ind-y / Ind-A) reading — these concepts are absent; do not map the paper onto the family.
- **NOT** for occupation or sector/industry opportunity content — the model has **no** occupation or industry channel; do not let "job offers" be read as occupation-specific offers. (No sector/industry conflation exists *in the source* to flag, but I must not import one.)
- **Random vs deterministic framing:** this paper is genuinely **random-opportunity** (Poisson offer arrivals, Fréchet max); my design treats opportunities as **deterministic** and uses RURO only as estimation machinery. Do not present their Poisson/Fréchet stochastic-offer apparatus as if it were my deterministic-feasible-set object [explicit, pp.151–155].
- **Elasticity magnitudes** are Belgian 2007 offer-distribution-shift elasticities of a particular conceptual type (whole-distribution shift, not an exogenous wage change) — do not quote them as standard Marshallian/Hicksian micro elasticities; the authors explicitly warn against that reading [explicit, pp.174–175].
- **Theory-paper boundary:** nothing here touches the Haydar–Maniquet axiomatic paper; this is an empirical-estimation source only. Do not let any normative reading leak from my theory paper onto this citation, and do not read this paper as a theory contribution.

## 14. Direct quotes worth citing

Short verbatim excerpts with page numbers (transcribe-verify before final use):

1. "These type of models … try to understand individual heterogeneity in choice behaviour as a combined effect of differences in preferences and opportunities." (p.145) [explicit]
2. "Job offers are considered as packages of wages, labour time regimes, and a number of other attributes." (p.147) [explicit]
3. "The utility function Ψ(w,h) and the distribution of offered labour time regimes g2(h) are however not separately non–parametrically identified." (p.157) [explicit]
4. "More specifically, a group specific unemployment rate is added as an explanatory variable for q. We assume that this variable does not affect individual preferences, but … has some relation with labour demand." (p.157) [explicit]
5. "We conclude that the already small change in labour market participation due to expected changes in education level, run predominantly through the channel of opportunities rather than through preferences." (pp.178–179) [explicit]
6. "The model is essentially static. And it does not provide a complete equilibrium framework. It is not a matching model …" (p.179) [explicit]
7. "In our implementation, we do not specify a functional form for the disposable income function f(w,h;x_f). For each draw (w,h) … disposable income … is instead calculated on the basis of the existing Belgian tax rules, as implemented in … euromod." (p.162) [explicit]

## 15. Open questions and risks for my draft

- **The `Ψ`/`g2` non-identification is inherited.** I use the same Box–Cox preferences and an hours-availability access channel; their candid statement that hours peaks are not separately identified from preferences is the sharpest known threat to my **access-vs-preference** boundary. My draft must address it head-on (functional-form justification + whatever exclusion variation I have) rather than let a referee discover it [explicit, p.157].
- **External instrument gap.** Their identification leans on a type-specific unemployment-rate exclusion restriction on `q`; I have none at baseline. The risk is that my access channel is identified only by functional form + synthetic recovery. The region×year continuous covariate merge is the natural analogue to consider, but it is not yet in the baseline [analogy].
- **No welfare bridge in the literature template.** The closest estimation cousin to my paper stops *before* welfare; there is no off-the-shelf precedent here for forming the ex-ante inclusive value as a welfare object, inverting to a money metric, or decomposing it. My welfare-and-decomposition layer is genuinely the novel contribution relative to this template, but it also means I cannot lean on this paper for welfare-side validation [explicit by omission].
- **Proposal individualisation.** Their proposal is common-within-gender; mine is partly individualised (wage/occupation). Their setup does not test the well-conditioning of importance sampling under partial individualisation, so it offers no reassurance on my ESS concern; that remains mine to validate [analogy].
- **Numerical implementation undocumented in the supplied pages.** Optimiser, starting values, multistart, and choice-set-size/draw-count robustness are not reported [verify]; I should not assume their pipeline was multistart-validated.

## 16. TL;DR for retrieval

Capéau–Decoster–Dekkers (IJM 2016) is the canonical worked **RURO/latent-jobs estimation** on Belgian EU-SILC 2007 with **EUROMOD** pricing every sampled (wage, hours) alternative — supplying my structural template for the **ability** channel (lognormal wage offers `g1(w)` in education and potential experience, dispersion σ) and the **access** channel (hours-peak density `g2(h)`, offer intensity `q` with an external unemployment-rate exclusion restriction), the McFadden **proposal/prior correction** (`P(0,0)/P(w,h)`), and the `q`/`γ1` non-separability normalisation. It computes **no welfare object and no inequality decomposition** — its only channel attribution is a two-way *behavioural* (participation/hours) education counterfactual (Table 7) — so it informs my **preference/ability/access estimation and identification** blocks but is **incompatible** as a source for W¹–W⁶, money-metric welfare, or my three-way Shapley–Shorrocks split, and its **genuinely random** Poisson/Fréchet opportunity framing is exactly what my deterministic-feasible-set design replaces.
