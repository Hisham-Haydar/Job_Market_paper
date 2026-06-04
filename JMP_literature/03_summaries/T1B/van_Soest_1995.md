# van Soest 1995 — Structural Models of Family Labor Supply: A Discrete Choice Approach

> **FILE/SOURCE MISMATCH NOTE (not part of the template).** This summary was
> requested under the save name `Aaberge_Colombino_2013.md`, but the attached
> PDF is **van Soest (1995)**, not Aaberge & Colombino (2013). Per the
> instruction that *the attached PDF is the source of truth* and the rule
> *do not invent claims*, this document summarises van Soest (1995) and is named
> accordingly. If an Aaberge & Colombino (2013) summary is wanted, attach that
> PDF. **Suggested correct path:** `JMP_literature/03_summaries/T1B/van_Soest_1995.md`
> (tier reassessed below).

## 0. Metadata
- **BibTeX key:** `vanSoest1995` [verify against library convention]
- **Authors:** Arthur van Soest (Tilburg University)
- **Year:** 1995
- **Outlet:** *The Journal of Human Resources*, Vol. 30, No. 1 (Winter 1995), pp. 63–88
- **DOI/URL:** JSTOR stable URL `https://www.jstor.org/stable/146191` (printed on source); DOI [verify, not printed]
- **PDF filename:** `Van_Soest_-_1995_-_Structural_Models_of_Family_Labor_Supply_A_Discrete_Choice_Approach.pdf`
- **Tier:** Filed by the user under **T1A**. **My assessment: T1B** — it is the foundational *estimation*/data-infrastructure ancestor of the discrete-choice family-labour-supply approach, but it contains no opportunity density, no welfare object, and no decomposition, so it does not serve the JMP's defining (welfare/decomposition/opportunity-mechanism) blocks directly.
- **JMP block(s) served:** **estimation** (primary: the discrete-choice MNL labour-supply backbone, the joint-couple decision unit, simulated ML for unobserved wages); **data-infrastructure** (Heckman-corrected wage imputation feeding a discretised budget map); **identification** (secondary, as a *cautionary* baseline for separating preferences from availability); **access** channel (precursor only, by analogy — the "hours-restrictions" device). **Not** welfare, **not** decomposition, **not** ability-as-a-welfare-object, **not** normative-interpretation.

## 1. One-paragraph relevance to my JMP
van Soest (1995) is the canonical statement of the **discrete-choice structural labour-supply model**, which is the estimation skeleton my RURO/latent-jobs pipeline inherits: a finite choice set over (income, leisure) packages, type-I extreme-value shocks, and a multinomial-logit choice probability that sidesteps budget-set nonconvexities (explicit-in-source, pp. 67–69). It speaks to my **preference** channel directly (his translog $U$ is the analog of my Box–Cox utility block $v$) and to my **access** channel only by analogy: his ad hoc "hours-restrictions" alternative-specific constants are an early, *non-circumstance-varying* device for missing part-time jobs, which is precisely the homogeneity assumption my circumstance-dependent access density is built to relax (pp. 71–72). His simulated-ML integration over an unobserved-wage density (his "ability" technology, a Heckman-corrected wage equation) is the methodological ancestor of my importance-sampling integrator over the wage channel (pp. 70–71). The paper computes **no welfare object and no inequality decomposition**, so for those layers it is a methodological prerequisite, not a usable template.

## 2. Data and setting
- **Country/year:** Netherlands, 1987 (explicit, p. 73).
- **Dataset:** Socio Economic Panel (SEP), wave drawn October 1987 by CBS (explicit, p. 73).
- **Sample unit:** two-adult families (husband + wife, both aged 16–65); a **unitary family** decision unit (explicit, pp. 73–74).
- **Sample size:** 2,859 families after dropping missing values; composition — 13.0% neither spouse works, 3.1% only wife, 49.7% only husband, 34.1% both (explicit, pp. 73–74). (Table 5 uses 2,826 observations for simulations.)
- **Key variables:** number/age of children, spouses' ages, education levels, child benefits, other family income, before-tax hourly wages, weekly hours, employment dummies (Table 2, p. 75).
- **Budget-set construction:** after-tax family income $y_j$ as a function of the spouses' hours, inverting the Dutch 1987 tax/premium system (eleven brackets, marginal rates 0–70%) plus a stylised benefits floor at ~50% of the family poverty line; before-tax wage assumed independent of hours (explicit, pp. 66–67, 74). The transferable tax-free allowance creates the canonical joint-filing nonconvexity (explicit, p. 66).
- **Transport to my France pooled 2015–2017 EUROMOD cross-section:** the *architecture* transports cleanly (discrete choice, tax-benefit budget map, couples as joint unit). Features I have that van Soest does **not** use: EUROMOD-computed `ils_dispy` as the budget map (he hand-codes a stylised 1987 system); pooled multi-year cross-section. Features **he** has that bear on mine: a single cross-section (no panel) — same limitation as mine. Features **neither** of us has: panel, administrative match, external opportunity instrument, vacancy/offer data (explicit absence in source; he estimates the availability device from hours data alone, p. 72).

## 3. Model and objects (object-by-object map to mine)
- **Choice set vs my latent-jobs set:** His choice set is a **fixed, common, finite grid** of $(y_j, l_{mj}, l_{fj})$ packages — $m = m_{\text{ind}}^2$ points, with $m_{\text{ind}}=5$ (25 alts, $IL=12$) or $m_{\text{ind}}=6$ (36 alts, $IL=10$), time endowment $TE=80$ h/week (explicit, p. 67). This is a **universal hours grid, identical across families** — *not* a household-specific feasible-job set. This is the single most important difference from my latent-jobs construction.
- **Deterministic utility vs my preference $v$:** His direct **translog** utility $U(v)=v'Av+b'v$ with $v=(\log y,\log l_m,\log l_f)'$ (eq. 1, p. 68); demographic taste-shifters enter through $\beta_i,\alpha_{ij}$ (eq. 2, p. 68). This **maps to my preference utility $v$** (explicit functional-form analog; mine is Box–Cox, his is translog — both checkable for monotonicity/quasi-concavity).
- **Opportunity / availability mechanism analogous to my $g$:** **None as a density.** The only availability device is a set of **alternative-specific constants** $\gamma_m(l_{mj}),\gamma_f(l_{fj})$ on part-time alternatives (eqs. 13–14, p. 72), interpreted as drawbacks/scarcity of part-time jobs. This is **not** a density over alternatives, **not** household-specific, and **explicitly assumed homogeneous across the labour market** (p. 72). Mapping to my four $g$-channels: **hours** ↔ his $\gamma$ constants (crude, aggregate, deterministic — derived-by-analogy only); **wage (ability)** ↔ handled outside the index, via the wage equation feeding the budget map (see §4b, §5); **market/participation** ↔ not separately modelled (participation is just the $h=0$ alternative); **occupation** ↔ **absent entirely** (see §5, §13).
- **Budget map vs my EUROMOD disposable income:** His $y_j$ = hand-coded Dutch 1987 tax-benefit map; mine = EUROMOD `ils_dispy` (2016-real). Same role, different engine.
- **Attribute entering BOTH utility and availability?** **No** — wage/occupation do not enter his utility-plus-availability index twice; the $\gamma$ constants enter the index, the wage enters only the budget map. So no double-entry to flag here. (This is the cleanliness my baseline also targets: occupation in $g$ only.)

## 4. Estimation method
- **Likelihood/estimator:** Multinomial logit choice probabilities (eq. 6, p. 69) from i.i.d. type-I EV shocks added to each alternative's utility (eq. 5, p. 68); estimated by **(simulated) maximum likelihood** (explicit, pp. 69–71).
- **Choice-set construction:** **Fixed full grid** (25 or 36 alternatives), **not** sampled alternatives (explicit, p. 67). There is therefore **no** sampling-of-alternatives correction and **no** per-alternative log-prior (see §4b).
- **Proposal/sampling density and $\log(\text{prior})$ subtraction:** **N/A** — no alternatives are sampled; the "simulation" in the paper is over *unobserved wages and random preferences*, not over the choice set.
- **Normalisation/scale:** The common EV variance $\pi^2/6$ is the scale normalisation, chosen instead of normalising a utility parameter so that the normalised parameter's sign is known a priori (explicit, p. 69).
- **Numerical method / draws:** Approximate (simulated) ML; integrals over the unobserved-wage density and random-preference density approximated by $R$ Monte Carlo draws, $R=5$ and $R=10$ (eqs. 11–12, 18, pp. 71, 73). Consistency requires $R\to\infty$ with $\sqrt{n}/R\to 0$ (explicit, p. 71). No multistart procedure described [verify].
- **What pins preferences vs the availability device:** the translog functional form plus the assumption that the $\gamma$ constants are alternative-specific and homogeneous across the labour market (see §8).
- **Verdict — reusable for my RURO/JAX pipeline?** **Partly, yes.** The MNL log-sum core (eqs. 5–6) and the simulated-integration step (eqs. 11–12) are reusable in spirit (my JAX engine already does the analytic-in-shocks log-sum and importance-sampling integration). His **fixed-grid** choice set is **not** reusable — my pipeline uses sampled alternatives with a $-\log\pi$ correction, which his framework lacks by construction. **Name the step:** reuse the MNL probability form and the simulated-ML-over-wage-density idea; replace the fixed grid with my sampled-alternatives + proposal correction.

## 4b. Proposal / sampling-of-alternatives correction
**N/A in the strict sense.** van Soest uses a **fixed, exhaustive grid** of 25–36 alternatives, so there is no proposal distribution, no McFadden-style correction, and no per-alternative log-prior (explicit, p. 67). The integration he *does* perform is over the **unobserved before-tax wage density** $p(W_{bm},W_{bf}\mid Z_m,Z_f)$ (eqs. 10–12, pp. 70–71), with draws from the Heckman-estimated wage equations. **Relation to my work:** this wage-density integration is the closest analog to my **wage-channel importance sampling**, and his proposal is **partly individualised** in the same sense mine is — the wage draws condition on individual characteristics $Z$ (education, age, region, minimum wage), while there is no analogous individualisation of an hours/employment offer mechanism (he has none). So his design supports, by precedent, my "wage/occupation individualised; hours/employment common" individualisation pattern — though for him the hours dimension is a fixed grid, not a common offer density (derived-by-analogy, not explicit).

## 5. Opportunity mechanism  [MOST IMPORTANT — split by channel]
**There is no explicit opportunity density.** The choice set is a universal common grid; the only availability content is the ad hoc hours-restrictions device. By channel:

- **access (hours / participation / region / occupation offers):**
  - *Hours availability:* represented by **alternative-specific constants** $\gamma_{sk}$ ($s=m,f$; $k=1,2,3$) on part-time alternatives (eqs. 13–14, p. 72), motivated by the basic model's strong **over-prediction of part-time work** (Table 3, p. 78). All $\gamma_{sk}$ estimated significantly negative (explicit, p. 78). **Functional form:** additive constants on specific hours cells; **deterministic**, not a density. **Crucially, assumed homogeneous across the labour market** — they "do not depend on wage rates, education level, family composition" (explicit, p. 72), i.e. the relative scarcity of part-time jobs is assumed **uncorrelated with circumstances**.
  - *Participation/market:* not separately modelled; non-participation is simply the $h=0$ alternative within the same grid.
  - *Region:* enters only the *wage equation* (DWEST, regional unemployment rate), not an availability mechanism over the choice set (explicit, Table A1, p. 85).
  - *Occupation offers:* **absent** (see below).
- **ability (wage technology):** a **Heckman selection-corrected log-wage equation** estimated separately for males and females, with returns to **education dummies, age (log age, log age²), the legal minimum wage, and the regional unemployment rate**, plus residual dispersion $\sigma(\eta)$ and a selection correlation $\rho$ (explicit, Table A1, p. 85). This is the analog of my **ability** sub-block (returns to education/experience + residual productivity dispersion), **but** it is used only to *impute and integrate over unobserved wages in the budget map*, **not** as a channel in a welfare or decomposition object (derived-by-analogy for the mapping; the welfare/decomposition use is not-established because the paper has no such layer).
- **occupation:** **not present** in any form — no ISCO/task variable, no `loc4` analog, no industry/NACE variable. There is therefore **no occupation-as-access object and no sector/industry conflation risk** to flag in this source.

**Cost of the omission for my access/ability/preference decomposition (stated plainly):** because the choice set is common and the hours-restriction constants are homogeneous across circumstances, the model has, by construction, **no between-household variation in access** — exactly the object my paper exists to measure. Adopting his device unchanged would mechanically **zero out the access component** of my decomposition. His framework is a baseline to *depart from*, not a source for the access channel.

## 6. Welfare object — and its place on my $W^1$–$W^6$ map
**The paper computes no welfare object.** No money-metric income, no equivalent income, no compensating/equivalent variation, no inclusive-value-as-welfare. Its post-estimation objects are **behavioural**: expected hours, elasticities, and tax/benefit **policy simulations** reported in hours and participation rates (Tables 4–5, pp. 80, 83). Reference price/preference/bundle/set: **N/A** (no welfare reference is constructed). Discrete-choice welfare subtleties (log-sum aggregation, Hicksian vs Marshallian, ex-ante vs ex-post): **not addressed**, because no welfare is computed.

**Location on my $W^1$–$W^6$ map:** **none.** The source does **not** contain $W^1$–$W^6$ or any compensation–responsibility classification (explicitly absent). Any attempt to place it would be fabrication. **Verdict: incompatible as a welfare source** — it is upstream of the welfare layer.

## 6b. Inclusive value and money-metric inversion
- **Inclusive value as welfare core?** **No** (not-established). He never forms the log-sum as a welfare object.
- **Money-metric inversion (1-D solve)?** **No** (not-established).
- **Expectation over EV shocks — analytic or simulated?** For *choice probabilities and expected hours*, **analytic** — expected hours are a closed-form, continuously differentiable function of wages/income via the MNL probabilities (explicit, footnote 13, p. 80). Simulation in the paper is over *wages and random preferences*, not over the shocks.
- **Relation to my analytic-in-shocks, importance-sampling inversion:** his expected-hours object shares my **analytic-in-shocks** property, but he stops at *behaviour*; my contribution converts the same analytic log-sum into an **ex-ante money-metric** via a 1-D root-solve, which he does not do (derived-by-analogy for the analytic step; the inversion is mine, not his).

## 7. Inequality / decomposition content
**None.** No inequality index (Gini/MLD/Theil/Atkinson), no decomposition rule (Shapley/Shorrocks/RIF/subgroup), no counterfactual equalisation. **Verdict: not reusable for my three-way access/ability/preference Shapley–Shorrocks split**, and it is neither a two-way nor a three-way decomposition — it has **no** decomposition at all. To serve this layer it would have to be extended with the entire welfare *and* decomposition apparatus.

## 8. Identification and the separation of preferences from opportunities  [STRICT]
- **What separates tastes from the availability device:** (i) the **translog functional form** of $U$, which generates smooth indifference maps and cannot, by itself, reproduce the spikes/holes in the observed hours distribution; (ii) the **restriction that the $\gamma$ hours-restriction constants are alternative-specific and homogeneous across the labour market** — they are identified from the residual peaks (full-time mass) and troughs (part-time deficit) the smooth utility leaves unexplained (explicit reasoning, pp. 72, 78). So the preference/availability split rests on **functional form + a strong homogeneity restriction**, not on choice-set variation, a panel, or an external instrument.
- **ability vs access within the availability side:** the paper does **not** attempt this split; "ability" lives only in the wage equation and is not contrasted against an access object.
- **Transport to my France pooled cross-section (no panel, no external instrument):** the *mechanism of identification* transports — I, too, lack a panel/instrument and lean on functional form. **But the specific homogeneity restriction does not survive contact with my research question:** van Soest assumes availability is uncorrelated with circumstances; my access channel is defined by making availability **circumstance-dependent**. This is the cleanest statement of why his device cannot be borrowed and is, instead, the foil for my identification note.
- **Defence against the "your decomposition is mechanical" referee:** van Soest is useful here precisely as the *negative* example — it shows that a model which forces availability to be homogeneous will load all between-household variation onto preferences (his basic-vs-extended elasticity collapse is the symptom; see §9), which is the over-attribution my paper corrects. Do **not** soften this: his hours-restriction constants are *ad hoc* and discretization-dependent (his own characterisation, pp. 72, 83).
- **Synthetic-recovery / parametric identification:** the paper relies on in-sample fit and diagnostic tests (Andrews 1988 chi-square; LM/Wald/LR on the $\gamma$'s), **not** on synthetic recovery (explicit, pp. 76–78). My baseline's standard of evidence (synthetic recovery, not in-sample fit) is therefore *stricter* than his and should be flagged as a deliberate departure.

## 9. Key results and magnitudes
- **Aggregate own before-tax wage elasticities of labour supply:** **0.11 (males), 0.40 (females)** (abstract p. 63; policy-sim rows 4–5, Table 5, p. 83). Population: sample-average aggregate response to a 10% wage increase.
- **Average-family median own-wage elasticities** (Table 4, p. 80): basic model (Model I) $h_m=0.153$, $h_f=1.027$; with hours restrictions (Model II) $h_m=0.104$, $h_f=0.524$; with hours restrictions + wage prediction error (Model III, $R=10$) $h_m=0.076$, $h_f=0.472$. **Headline pattern:** adding the availability device **roughly halves the female own-wage elasticity** (explicit, pp. 81–83). Cross-wage elasticities small and negative; income elasticities very small.
- **Model fit:** the basic model **strongly over-predicts part-time work**; the $\gamma$ constants restore the marginal hours fit almost exactly (max marginal difference 0.29 pp), though a bivariate chi-square test still rejects (explicit, pp. 78–79).
- **Quasi-concavity:** violated at 0.8% (25 alts) / 6.3% (36 alts) of basic-model sample points, concentrated among high-income full-time-wife families; 99.9% concave under Model II (explicit, pp. 76, 78).
- **Wage-prediction-error and random-preference extensions:** small effects; $R=5$ vs $R=10$ "virtually identical"; random-preference standard deviations imprecise and not confirmed as important (explicit, p. 79).
- **Policy simulations** (Table 5, p. 83): abolishing the transferable tax-free allowance → female labour supply **+4.2%**, male **−0.7%** (net hours **+0.4%**); full individualisation of taxes+benefits → female labour supply **−7.1%**, two-earner households **−14.5%**.
- **Benchmark value for my work:** the **elasticity collapse when availability is added** is the directly relevant magnitude — it quantifies how much "preference responsiveness" in a no-availability model is actually availability, which is the over-attribution my decomposition targets.

## 10. Estimators, theorems, or formal results
This is an applied econometrics paper; it states estimators, not theorems.
1. **Discrete-choice (MNL) labour-supply estimator.** Statement: $\Pr[U_j>U_k\ \forall k\neq j]=\exp(U(y_j,l_{mj},l_{fj}))/\sum_{k}\exp(U(y_k,l_{mk},l_{fk}))$ (eq. 6, p. 69), with $U$ the translog (eq. 1) and i.i.d. EV(I) shocks (eq. 5). Assumptions: finite common choice set; i.i.d. type-I EV; IIA. Technique: ML on closed-form logit probabilities; budget-set shape is irrelevant to the probability (a stated advantage). **Reusability:** **yes** — this is the backbone my RURO factorisation generalises ($v$ + $\log g$ − $\log\pi$).
2. **Hours-restrictions extension.** Statement: $U_j=U(\cdot)+\gamma_m(l_{mj})+\gamma_f(l_{fj})+\varepsilon_j$ (eqs. 13–14, p. 72), $\gamma_{sk}$ alternative-specific, homogeneous across the market. **Reusability:** **no, as-is** — adopt only as the explicit foil; my access channel must make these circumstance-dependent.
3. **Simulated ML over unobserved wages.** Statement: $L=\int F_{\text{job}}(W_{bm},W_{bf},X)\,p(W_{bm},W_{bf})\,dW$ approximated by $L_R=\frac1R\sum_r F_{\text{job}}(W_{bmr},W_{bfr},X)$ (eqs. 10–12, pp. 70–71), draws from the Heckman wage equation; consistent as $R\to\infty$, $\sqrt n/R\to0$. **Reusability:** **yes** — methodological ancestor of my wage-channel importance sampling; my contribution is to fold this into an opportunity *density* rather than a budget-map nuisance integral.
4. **Random-preferences extension.** Statement: random normal coefficients on the leisure log-terms $\beta_2,\beta_3$ (eqs. 15–18, p. 73), integrated by simulation. **Reusability:** **maybe** — relevant only if I revisit unobserved preference heterogeneity beyond the EV shocks; the source finds it adds little.
No propositions, lemmas, or theorem numbers to report.

## 11. Robustness and specification sensitivity
- **Choice-set granularity:** $m_{\text{ind}}=5$ (25 alts) vs $6$ (36 alts) — most parameters similar, elasticity confidence intervals overlap; discretisation introduces rounding error and a modest quasi-concavity difference (explicit, pp. 76, 80). *Lesson for me:* alternative-count sensitivity is real but second-order; worth a recovery check across grid sizes.
- **Number of draws:** $R=5$ vs $10$ "virtually identical" (explicit, p. 79). *Lesson:* small $R$ can suffice — relevant to my effective-sample-size concern, though my singles ESS problem is about *importance-sampling* coverage, which his fixed-grid design does not face.
- **Discretisation-dependence of the availability device:** the $\gamma$ parameterisation depends on the chosen $IL$/$m_{\text{ind}}$, so results across discretisations "can no longer be compared" (explicit, p. 72). *Lesson/warning:* any hours-availability parameterisation I tie to a specific alternative grid inherits this fragility — argue for a circumstance-parameterised (not cell-specific) form.
- **What breaks:** elasticities fall sharply with each added realism layer; the author cautions that "misspecification is still present" and that true elasticities may be even smaller (explicit, p. 84).

## 12. What I can cite this paper for
- The **discrete-choice / multinomial-logit structural labour-supply model** as the foundational approach that handles nonlinear taxes and budget-set nonconvexities without coherency restrictions (pp. 67–69).
- The **unitary-couple joint-decision** treatment with a single family utility over (income, both leisures) (pp. 63, 68).
- The empirical fact that **standard models over-predict part-time work**, motivating an explicit treatment of **limited job/hours availability** (pp. 71–72, 78) — useful motivation for my access channel.
- That **adding availability constraints substantially lowers estimated wage elasticities** (pp. 81–84) — the over-attribution-to-preferences point.
- **Simulated ML** for integrating over **unobserved wages of non-workers** via a Heckman-corrected wage equation (pp. 70–71).

## 13. What I should NOT cite this paper for  [overclaim risks]
- **Not** an opportunity-density / RURO / latent-jobs paper — its availability device is **ad hoc alternative-specific constants**, not a household-specific feasible-set density. Do not attribute a latent-jobs opportunity mechanism to it.
- **Not** a source for **circumstance-varying access** — it explicitly assumes hours restrictions are **homogeneous across the labour market** (p. 72), the opposite of my access object.
- **Not** a welfare / equivalent-income paper — do **not** cite for money-metric well-being under different feasible sets; it computes no welfare object.
- **No inequality or decomposition** — do not read any "opportunity vs preference" (two-way) *or* access/ability/preference (three-way) split into it; it has none.
- **No occupation/sector** — it has no ISCO/`loc4` analog and no NACE/`lindi`; do not cite for occupation-as-access, and note there is no sector/industry conflation to inherit.
- **Random-opportunity vs deterministic framing** — irrelevant here; its randomness is in *shocks and unobserved wages*, not in opportunities. Do not import any "random opportunities" reading.
- **Theory-paper boundary** — nothing in this source bears on $W^1$–$W^6$ or the Haydar–Maniquet axioms/characterisation. Do not let it stand in for the theory paper, and do not read it as a theory contribution.
- **Intra-household** — it is a *unitary* family utility, explicitly setting aside collective/Pareto-efficient intra-household models (footnote 1, p. 64); do not cite for individual-within-couple welfare.

## 14. Direct quotes worth citing
*(short verbatim phrases, page-numbered, for retrieval indexing only)*
- "labor supply is treated as a discrete choice problem" (p. 64).
- "the lack of available part-time jobs" (p. 71).
- "hours restrictions are homogeneous across the labor market" (p. 72).
- "allowing for hours restrictions substantially reduces estimated own wage elasticities" (pp. 83–84).

## 15. Open questions and risks for my draft
- **The availability-homogeneity assumption is the crux.** van Soest's model demonstrates the failure mode my paper corrects (availability folded into a homogeneous constant), but it also shows how *little* identifying variation supports an availability device estimated from hours data alone (p. 72). Risk for my draft: a referee can ask whether my circumstance-dependent access is identified by more than functional form — I must point to my synthetic-recovery certification and the partly-individualised proposal, not to in-sample fit.
- **Discretisation-dependence (p. 72)** is a live warning for any hours-availability parameterisation tied to a specific alternative grid; argue for a circumstance-parameterised form and report grid-size recovery.
- **Elasticity attenuation under added realism (p. 84)** suggests my preference-component estimates (already wide per the project's standard-error asymmetry) will be sensitive to how richly access is modelled — relevant to the preference-component confidence-interval width in the decomposition.
- **No welfare/integration machinery here**, so this source offers no guidance on my binding open issue (singles importance-sampling coverage / EUROMOD reprice parity); that risk must be addressed from the welfare-spec and project-state lineage, not from van Soest.

## 16. TL;DR for retrieval
van Soest (1995) is the foundational **discrete-choice MNL family-labour-supply estimator** (translog utility = my **preference** block; fixed common hours grid; simulated ML over unobserved wages = ancestor of my wage/**ability**-channel integration), and it motivates an **access**-type device only through ad hoc, *circumstance-homogeneous* hours-restriction constants. It contains **no opportunity density, no occupation variable, no welfare object, and no decomposition**, so it serves my **estimation/data-infrastructure** blocks and stands as the explicit **foil** for my circumstance-dependent access channel — never as a source for welfare, the $W^1$–$W^6$ family, or the three-way Shapley–Shorrocks split.
