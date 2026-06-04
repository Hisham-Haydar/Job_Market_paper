# Dagsvik & Jia 2016 — Labor Supply as a Choice Among Latent Jobs: Unobserved Heterogeneity and Identification

> Source of truth: the attached JSTOR PDF (J. Appl. Econ. 31(3): 487–506). The companion
> `.md` was used only for navigation. Page numbers refer to the journal pagination (487–506).
> Tags used below: **[explicit]** = stated in the paper; **[analogy]** = derived by mapping
> to my design, not asserted by the paper; **[not-established]** = the paper does not do this;
> **[verify]** = could not be confirmed from the provided PDF body (e.g. supplementary-appendix
> material).

---

## 0. Metadata

- **BibTeX key:** `dagsvik_jia_2016_latent_jobs`
- **Authors:** John K. Dagsvik (Statistics Norway; Frisch Centre); Zhiyang Jia (Statistics Norway).
- **Year:** 2016 (published online 6 January 2015; received 1 Oct 2012, revised 23 Sep 2014). [explicit, p.487]
- **Outlet:** *Journal of Applied Econometrics*, Vol. 31, No. 3, pp. 487–506. [explicit, p.487]
- **DOI / URL:** DOI 10.1002/jae.2428; JSTOR stable URL `https://www.jstor.org/stable/10.2307/26609622`. [explicit, p.487]
- **PDF filename:** `Dagsvik_and_Jia_-_2016_-_Labor_Supply_as_a_Choice_Among_Latent_Jobs...pdf`
- **Tier:** **T1A** (core — the canonical identification statement of the RURO/latent-jobs framework my estimation layer instantiates).
- **JMP blocks served:** **identification** (primary); **estimation**; **opportunity-mechanism (access + ability)**; **motivation**. It does **not** serve welfare, decomposition, or normative-interpretation directly.

---

## 1. One-paragraph relevance to my JMP

This is the foundational identification paper for the exact structural object my estimation layer instantiates: a choice probability that factorises into a deterministic preference utility $v(C,h)$ and an *opportunity measure* $\theta\,g_1(h)\,g_2(w\mid h)$ over latent jobs. [explicit, pp.489–490] It is the paper that establishes — formally, on cross-section data — *when* preferences can be separated from the opportunity mechanism, which is precisely the separation my access/ability/preference decomposition presupposes; without that separation the decomposition is mechanical, and this paper is my primary defence on that point. [explicit, §3, pp.492–494] It speaks directly to **two of my three channels**: the wage sub-block $g_2(w\mid h)$ and its individual-ability random effect $\eta$ map to my **ability** channel, and the hours/availability objects $g_1(h)$ and $\theta$ map to my **access** channel. [explicit for the objects, pp.489–491; channel-naming is [analogy]] It does **not** compute welfare, an inclusive-value welfare core, or any inequality decomposition, and it contains nothing resembling my $W^1$–$W^6$ family; it is upstream machinery, not a welfare or decomposition source. [not-established]

---

## 2. Data and setting

- **Country / year:** Norway, single cross-section, **Norwegian Labor Survey 1997**. [explicit, p.495]
- **Dataset / unit:** Married/cohabiting **couples**; the labour-supply model is a **joint** couple decision. [explicit, pp.487, 495]
- **Sample size:** Table I reports household counts by employment configuration — both spouses working **2,254**; only husband working **256**; only wife working **5** (no "neither working" row is shown in the table). [explicit, p.495] Total over the listed cells $\approx 2{,}515$ couples; whether a non-working-couple cell exists is [verify] (not shown in the provided body).
- **Key variables:** age, length of schooling (education), potential experience ($=$ age $-$ schooling $-7$), non-labour income, gross hourly wage rate, weekly hours of work, number of children (0–6 and 7–18). [explicit, Table I, p.495]
- **Budget-set construction:** disposable income via a net-of-tax function $C=f(hw,I)$, with $I$ non-labour income; $f$ is stated to be able in principle to capture the full tax/benefit system. [explicit, p.489]
- **Transport to my France pooled 2015–2017 EUROMOD cross-section:** *Partial.* The structural form transports cleanly (cross-section, discrete latent-jobs couples, parametric Box–Cox utility, opportunity density). What I have that they do not: an explicit microsimulated budget (EUROMOD `ils_dispy`) rather than an estimated net-of-tax function; pooled multiple waves (they have one year). What they have/use that bears on me: a **three-stage wage-equation estimation** to handle measurement error in hours ("division bias"), because they observe weekly hours only and infer the wage by division. [explicit, pp.495–496] **Features I do NOT have, named explicitly:** no panel, no administrative match, no external opportunity instrument, no vacancy/offer data — and the paper itself states that even panel or independent cross-sections do not, in general, solve the identification problem. [explicit, p.492]

---

## 3. Model and objects (object-by-object map to mine)

| Their object | Mine | Match? | Note |
|---|---|---|---|
| Latent job "packages" $(H(z),W(z),\text{attributes})$, worker-specific unobserved choice set | latent-jobs set $\mathcal C_i$ | **Yes** [explicit, pp.487–489] | Theirs is conceptually infinite (Poisson-scattered); mine is a finite sampled grid (singles 101, couples 901). |
| Deterministic utility $v(C,h)$, Box–Cox | preference utility $v_i(c,\ell)$, Box–Cox | **Yes** [explicit, eq.(8), p.493] | Both Box–Cox in consumption and leisure; globally concave. Theirs is over $C$ and $(1-h/M)$. |
| Opportunity measure $\theta\,g_1(h)\,g_2(w\mid h)$ | opportunity density $g(j;x_i)$ | **Yes** [explicit, p.489] | This is the central shared object; see §5. |
| $g_1(h)$ — offered-hours density | **access** (hours availability) | **Yes** [explicit] | Their $g_1$ is uniform with peaks at PT/FT. |
| $g_2(w\mid h)$, wage equation, random effect $\eta$ | **ability** (wage technology + residual $\sigma$) | **Yes** [explicit eq.(4),(9); channel name [analogy]] | $\eta$ is explicitly called individual *ability* (p.494). |
| $\theta$ — job-availability scalar (ratio of market to non-market opportunities) | **market/participation** availability term ($\log\text{market}$) | **Partial** [explicit p.489; mapping [analogy]] | $\theta$ also absorbs psychic cost of working ($\theta<1$). |
| Market vs non-market opportunities ($z>0$ / $z<0$) | market/participation channel | **Yes** [explicit, p.488] | The participation margin is a market-vs-non-market split. |
| Budget $C=f(hw,I)$ | EUROMOD `ils_dispy` | **Analogous** [explicit] | Their estimated net-of-tax function ↔ my microsimulated income. |
| **Occupation / sector** | my `loc4` access object | **Absent in the estimated model** | See flag below. |

**Flag — occupation/sector.** The estimated empirical model contains **no occupation and no sector variable.** [explicit] The paper uses "sector" to mean *labour-market sector* (e.g. public health care, teaching) and invokes it only as informal *explanation* for gendered hours peaks, plus a footnote that a sector-specific model (as in Dagsvik & Strøm 2006) *could* yield explicit sector-specific opportunity measures. [explicit, p.497 fn.9; p.501] Two consequences for me: (i) this paper is **not** a precedent for an occupation-as-access layer being estimated — it is a precedent only for the *idea* that sector/occupation belongs in the opportunity measure if added; (ii) their "sector" language is closer to industry than to my ISCO-type `loc4` task categories, so I must not cite it as support for `loc4`-as-occupation, and must keep my `loc4`/`lindi` discipline intact when citing.

**Flag — does any attribute enter BOTH utility and opportunity?** **No.** [explicit] The wage and hours enter the opportunity measure $g_2(w\mid h)g_1(h)$ and enter utility only through $C=f(hw,I)$ and through $h$; the wage technology / ability is purely in the opportunity side, never in $v$. Crucially, **non-labour income $I$ enters only through consumption and does not affect the opportunity measure** — this exclusion is the load-bearing identification device (Assumption 3 / Theorem 2). [explicit, pp.492–493] This is consistent with my design (occupation and the wage return live in $g$ only, never in $v$).

---

## 4. Estimation method

- **Likelihood / estimator:** maximum likelihood on the closed-form choice probabilities (2a,b)/(3a,b). [explicit, p.496]
- **Choice-set construction:** a **fixed grid** of eight feasible annual hours per spouse — $\{0,\,208,\,624,\,1040,\,1456,\,1950,\,2340,\,2600\}$ — with the offered-wage dimension handled by **integration/summation** over the wage density, not by a sampled-alternative draw. [explicit, p.495] This is *full enumeration over a small grid*, **not** McFadden sampling-of-alternatives.
- **Proposal / sampling density:** **none** — there is no importance-sampling proposal because alternatives are enumerated; see §4b.
- **Prior/proposal correction ($-\log\pi$):** **absent**, by construction (no sampling). [explicit by absence] The opportunity density $g$ enters the likelihood as a *structural weight* on each enumerated alternative, not as a nuisance correction. This is the key contrast with my pipeline (see §4b).
- **Normalisation / scale:** $C_0$ is a known subsistence-consumption constant; $\theta$ enters multiplicatively on $v$, so it also soaks up the psychic cost of working (rationalising $\theta<1$). [explicit, pp.489–490] $\delta(h)$ / $g_1(h)$ separation is left unidentified for pure tax/wage simulation (kept fixed); see §8.
- **Division-bias handling (their numerical method of substance):** a **three-stage procedure** (after Dagsvik & Strøm 2004, 2006): (1) reduced-form participation probability; (2) wage-rate equations estimated with a selectivity correction using stage-1 results; (3) ML on the labour-supply model with stage-2 predicted wages inserted and the wage-equation errors integrated out. [explicit, p.496] Selection bias in the wage equations is reported negligible. [explicit, p.496]
- **Starting values / multistart:** not described in the provided body. [verify]
- **What pins preferences apart from opportunity:** the exclusion restriction on $I$, a parametric functional form (Box–Cox), and a normalisation on the offered-hours density (two hours points with equal $g_1$). [explicit, Assumptions 3, 5, 6; Theorem 4, p.493] — see §8.
- **Verdict — reusable for my RURO/JAX pipeline?** **Yes, structurally — with one decisive difference.** The likelihood object (utility $\times$ opportunity density, normalised over alternatives) is exactly mine. *Difference:* they **enumerate** a small grid and **integrate** the wage; I **sample** alternatives and therefore must carry the $-\log\pi$ correction that they do not need. Reuse the *factorisation and the role of $g$ as a structural weight*; do **not** import their estimation as evidence that a sampling correction is unnecessary — that is an artefact of enumeration. Their three-stage wage procedure is an alternative to my single-stage approach worth citing as a measurement-error precedent, not adopting.

---

## 4b. Proposal / sampling-of-alternatives correction  [extract even if brief]

**The paper has no sampling-of-alternatives step and therefore no McFadden-style proposal correction.** [explicit by construction] Alternatives are the eight fixed hours points; the offered-wage distribution is integrated analytically/numerically. The object that *plays the role* of a per-alternative weight is the **structural opportunity density** $\theta g_1(h)g_2(w\mid h)$ itself — but this is a structural primitive, not a nuisance proposal to be divided out. [explicit, pp.489–490]

Mapping to my concerns:
- **My $-\log\pi$** is a sampling nuisance correction; **their $g$-terms** ($\log g_1+\log g_2+\log\theta$) are the *structural* analogues of my $\log h_{ij}+\log w_{ij}+\log\text{market}_{ij}$. The clean lesson: when I sample, I must *both* keep the structural $g$-logs *and* subtract $\log\pi$; this paper isolates the structural logs in their pure (un-sampled) form, which is useful for verifying that my structural terms are specified correctly independent of the sampling correction. [analogy]
- **Proposal individualisation.** They consider $g_2(w\mid h;\eta)$ depending on individual covariates and a random effect $\eta$ (i.e. the wage channel is individual-specific), while keeping $g_1(h)$ common across observationally identical agents on the stated ground that hours restrictions are institutionally (union/negotiation) determined and not individual. [explicit, pp.490–491] This is a near-exact precedent for my proposal-individualisation split — **wage individualised, hours/employment common** — and I can cite it for that design choice. [explicit for their structural choice; my proposal-instrument analogy is [analogy]]

---

## 5. Opportunity mechanism  [MOST IMPORTANT — split by channel]

**Form.** The available jobs are a realisation of a **Poisson process** of taste shifters $\{\varepsilon(z)\}$ scattered on $(0,\infty)$ with non-homogeneous intensity $\propto \varepsilon^{-2}$ (market intensity scaled by $\theta$, non-market by $1$), with offered $(H(z),W(z))$ drawn independently on $D\times(0,\infty)$ according to $g_1(h)g_2(w\mid h)$. [explicit, Assumption 2, p.489] Dagsvik (1994) showed this $\varepsilon^{-2}$ intensity is the form required for the resulting job choice to satisfy IIA. [explicit, pp.489–490] The realised choice probability collapses to the closed form in Theorem 1 (eq. 2a,b): for $h>0$,
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
  - The random effect $\eta$ (Model 2) is **explicitly interpreted as individual ability** affecting the opportunity measure: "$a+Xb+\eta$ … represent[s] the effect of observed and unobserved individual ability." [explicit, p.494]
  - $\xi(z)$ (Model 1) is *across-job* wage variation for a given agent. The two models are the two "extreme" stances: Model 1 = wage varies across jobs only ($\eta=0$); Model 2 = each agent faces one wage that varies across agents ($\xi=0$). [explicit, p.496]
  - This is a direct precedent for my ability sub-block (returns to education/experience $+$ residual dispersion $\sigma$). My $\sigma$ corresponds to their wage-equation residual variance (var of $\xi$ in M1, var of $\eta$ in M2). [explicit for theirs; correspondence [analogy]]
- **MARKET/PARTICIPATION** = the market-vs-non-market opportunity split and $\theta$. [explicit, pp.488–490]
- **OCCUPATION** = **not modelled** in the estimated opportunity mechanism; only referenced as a possible sector-specific extension. [explicit, p.497 fn.9] **No sector/industry conflation to flag in their estimation** because they estimate no such variable; but note their *informal* "sector" usage means industry-flavoured labour-market sectors, not my ISCO `loc4`.

**Does it vary with circumstances?** Yes, but narrowly: $\theta$ varies with schooling, and $g_2$ varies with schooling/experience and (in M2) with individual ability $\eta$; $g_1(h)$ is deliberately held common across observationally identical agents (institutional hours). [explicit, pp.490–491, 495]

**Cost of the omissions for my decomposition.** Because their access channel lacks region/urbanisation/year/occupation, their estimated "opportunity" is thinner than mine; their paper cannot, and does not, decompose welfare by access vs ability. I should cite it for the *existence and identification* of the access (hours, $\theta$) and ability (wage-$\eta$) sub-objects, not for any quantification of an access/ability split.

---

## 6. Welfare object — and its place on my $W^1$–$W^6$ map

**The paper computes no welfare object.** [not-established] It produces choice probabilities, expected hours ("labour supply curves"), wage elasticities, and a policy simulation of a change in the hours-opportunity distribution. There is **no money-metric welfare, no equivalent income, no compensating/equivalent variation, no inclusive-value welfare core, and no reference price/preference/bundle/set** in the sense my welfare layer requires. [not-established]

- It does **not** place anywhere on my $W^1$–$W^6$ family; **do not cite this paper as containing or supporting any $W^k$ measure.** Its closest relative — welfare effects of tax reforms — appears only in a *cited* reference (Aaberge, Dagsvik & Strøm 1995), not in this paper. [explicit, references p.502]
- The one welfare-adjacent operation is the **policy simulation** (§4.3, Appendix B): changing $g_1$ by removing the part-time peak and raising the full-time peak with $\theta_F$ fixed, then recomputing the realised labour-supply distribution. [explicit, pp.500–501, 505–506] This is a *behavioural* counterfactual on the opportunity density, not a welfare evaluation. It is, however, a clean precedent for the kind of access-shift counterfactual my decomposition equalises. [analogy]
- **Verdict:** **incompatible as a welfare source**; usable only as the structural-estimation foundation on which a welfare layer (mine) is later built. The welfare construction is entirely my (and the equivalent-income literature's) addition.

---

## 6b. Inclusive value and money-metric inversion  [extract if used]

**Not used.** [not-established] The paper does not use the log-sum / inclusive value as a welfare core and performs no money-metric inversion. The expectation over the extreme-value-type taste shifters is handled *analytically* in deriving the closed-form choice probabilities (Theorem 1), and the unobserved wage effect $\eta$ is integrated out (by simulation/numerical integration over $g_\eta$). [explicit, pp.490–491] So there is an analytic-in-taste-shocks derivation I can point to as the antecedent of my analytic-in-shocks log-sum — but the paper stops at choice probabilities and expected hours; it never forms a welfare inclusive value or inverts utility to money. My analytic-in-shocks importance-sampling inversion is my own construction, consistent in spirit but not present here.

---

## 7. Inequality / decomposition content  [three-way where relevant]

**None.** [not-established] No inequality index (Gini/MLD/Theil/Atkinson), no decomposition (Shapley/Shorrocks/factor/subgroup/RIF), no counterfactual equalisation of a distribution. The closest object is the *behavioural* hours-distribution simulation (§7-adjacent), which equalises nothing in a welfare sense. **It cannot be cited as a precedent for my three-way access/ability/preference Shapley–Shorrocks split.** To be extended to my decomposition it would need: (i) a welfare object built on top (the inclusive-value money metric); (ii) an inequality index over households; (iii) a Shapley equalisation protocol over the estimated $g$/$v$ blocks. All three are absent.

---

## 8. Identification and the separation of preferences from opportunities  [STRICT — the backbone]

This is the paper's central contribution and my primary identification citation. The problem is stated exactly as mine: observed behaviour reflects **both** preferences $v(C,h)$ **and** latent choice constraints (the opportunity measure $\theta g_1 g_2$), so standard multinomial/mixed-logit identification does **not** apply. [explicit, pp.492, 501] The results, in order:

- **Non-parametric ratio is identified, the split is not (Theorem 1 corollary).** $\varphi(h,w\mid I)/\varphi(0,0\mid I)=v(f(hw,I),h)\,\theta g_1(h)g_2(w\mid h)/v(f(0,I),0)$ is observable, but $v$ and $\theta g_1 g_2$ are not separately recoverable from it. [explicit, eq.(7), p.492]
- **Exclusion restriction (Assumption 3).** $v(C,h)$ is smooth and $I$ enters **only through consumption**, not the opportunity measure — i.e. non-labour income shifts $C$ while holding hours and wage fixed. [explicit, pp.492–493] This is the key economic exclusion; my analogue is that EUROMOD non-labour income enters only $c$, not $g$.
- **Theorem 2 (non-identification under exclusion alone).** Even with Assumption 3, the model is **non-parametrically unidentified**: $v(C,h)=\zeta(C)^{r}\lambda^{*}(C,h)\,\delta(h)$ with $\zeta,\lambda^{*}$ identified but $r$ an unknown constant and $\delta(h)$ an unknown function of hours. [explicit, p.493]
- **Theorem 3 (Assumption 4: offered wages ⟂ offered hours).** The offered-hours distribution is identified and $v(C,h)=\lambda(C,h)\delta(h)$ with $\lambda$ identified, **$\delta(h)$ still not**. For pure tax/wage counterfactuals one need not separate $\delta(h)$ from $g_1(h)$ as long as $g_1$ is held fixed. [explicit, pp.493] — *Important caveat for me: this "don't need to separate" licence applies to behavioural tax simulation, NOT to a welfare decomposition that attributes inequality to access vs preference; my object requires the separation their tax-simulation can dodge.*
- **Theorem 4 (full identification via functional form).** Under Assumptions 1–3, 5, 6 — a generalized **Box–Cox** $\log v$ (eq.8) plus a normalisation that two distinct hours points share the same offered-hours probability, $g_1(h_1)=g_1(h_2)$ — model (2a,b) is **identified**. [explicit, p.493] **This is parametric identification: the separation is bought with functional form + a normalisation, not with an instrument or panel.**
- **Theorem 5 (identification with a wage random effect / ability).** With unobserved wage heterogeneity (model 3a,b), identification needs an **exogenous covariate $X$ that affects the opportunity density / offered wage but not preferences** (Assumption 7: $\log W(z)=Xb+a+\eta+\xi(z)$, with $\theta$ constant or $\theta(a+Xb+\eta)$). Then $v$ is identified up to a multiplicative $h$-term, $\theta(\cdot)$ up to a constant, and the conditional offered-wage distribution is identified; adding Box–Cox (Assumption 6) gives full identification. [explicit, pp.494]

**Transport to my France pooled cross-section (honest assessment).**
- Their cross-section + Box–Cox + exclusion-of-$I$ + hours-normalisation route (**Theorem 4**) transports directly to me: I too rely on parametric Box–Cox and on non-labour income entering only consumption. My certification by **synthetic recovery** is the right standard precisely because identification here is *parametric*, not design-based — recovery on simulated data is the test of whether the functional-form identification actually bites at my sample size. [analogy; consistent with project state §3.6/§8]
- Their random-wage-effect route (**Theorem 5**) requires an **exogenous wage/opportunity shifter $X$ excluded from preferences**. My ability sub-block uses education and experience as the wage technology; for the Theorem-5 logic to support separating my ability channel, those must be credibly excluded from $v$ — which is exactly my design (education/experience are in $g$, not $v$). But I have **no external instrument** beyond functional form, and the paper is explicit that **panel or repeated cross-sections do not in general rescue identification** (only changes in the opportunity measure, not its level, become non-parametrically identifiable under fixed preferences). [explicit, p.492] So I cannot lean on my pooling of 2015–2017 as an identification gain; it is a precision/clustering matter, not an identification one.
- **Referee defence ("your decomposition is mechanical").** Cite Theorems 2–5 to establish that (a) the separation is a *known hard problem*, (b) it is *achievable* under stated parametric assumptions I satisfy, and (c) the honest standard is recovery under those assumptions — which is why I certify by synthetic recovery rather than in-sample fit. **Do not soften:** the identification is parametric and rests on the exclusion of $I$ from $g$, the exclusion of the wage shifter from $v$, the Box–Cox form, and an offered-hours normalisation.

---

## 9. Key results and magnitudes

All from the Norway 1997 married-couples sample; "M2" = their maintained Model 2 (individual wage heterogeneity).

- **Model selection.** Log-likelihood values $\approx 5309$ (M1) and $5243$ (M2) [sign reported as printed; magnitude is the likelihood-function value — [verify] sign]. McFadden $\rho^2 = 0.49$ (M1), $0.50$ (M2). [explicit, p.497]
- **Andrews $\chi^2$ goodness-of-fit (5 d.f., 6 cells):** M1 $=57.6$ (fails), M2 $=10.4$ (passes; 5% critical $=11.07$). M2 selected as maintained model. [explicit, pp.497–498]
- **Wage elasticities (aggregated, M2; Table II, p.499):**
  - Own-wage elasticity of the **probability of working, married women** $=0.333$ (text rounds to $0.33$); a 5% female wage rise raises the female participation share by $\approx 1.5\%$. [explicit, pp.499, 502/p.14 text]
  - Probability of working, **married men**: very small, $\approx 0.007$ (own), $0.010$ (men's wage). [explicit, Table II]
  - **Unconditional hours elasticity, women** $=0.618$ (M2, own-wage); **men** $\approx 0.022$ (own) to $0.080$ (men's wage). [explicit, Table II]
  - Cross-wage elasticity for women is **negative** and smaller than own-wage. Both-spouses-wage elasticity of female participation $=0.205$ (M2). [explicit, Table II; p.499]
- **Opportunity findings.** $\theta<1$ for both genders (interpreted as fewer interesting available jobs than non-market opportunities, and/or psychic cost of work). $\theta_F$ rises with schooling; $\theta_M$ insignificant. Number of children significantly raises women's marginal utility of leisure, not men's. [explicit, p.497]
- **Policy simulation.** Removing the female part-time peak and raising the full-time peak (with $\theta_F$ fixed) shifts women from PT to FT by roughly equal magnitudes; men's labour supply barely changes. [explicit, pp.500–501]
- **Benchmark value for me:** female participation own-wage elasticity $\approx 0.33$ and unconditional hours elasticity $\approx 0.6$, with near-zero male responses, are the order-of-magnitude sanity checks for my France estimates; large divergence would flag a specification problem. [analogy]

---

## 10. Estimators, theorems, or formal results

For each, statement (paraphrased; LaTeX for the math), assumptions, technique, reusability verdict.

- **Theorem 1 (closed-form choice probability).** Under Assumptions 1–2, the joint density of $(h,w)$ is the ratio in §5 (eq. 2a,b). Assumptions: separable random utility $U=v(C,h)\varepsilon(z)$; Poisson-scattered taste shifters with $\varepsilon^{-2}$ intensity; offered $(H,W)\sim g_1g_2$ independent of shifters. Technique: max-stable / extreme-value process algebra (Dagsvik 1994); the $\varepsilon^{-2}$ form yields IIA. **Reusable:** yes — this *is* my per-alternative structural weight, modulo my sampling correction. [explicit, p.490]
- **Theorem 2 (non-identification under exclusion).** $v(C,h)=\zeta(C)^{r}\lambda^{*}(C,h)\delta(h)$; $r,\delta(h)$ unidentified. Assumptions 1–3. Technique: log-differentiate the observable ratio in $I$, integrate over $C$ (Appendix A). **Reusable:** as the *negative* result I cite to justify parametric identification. [explicit, p.493]
- **Theorem 3 (partial identification under wage⟂hours).** Offered-hours distribution identified; $v=\lambda\delta$, $\delta(h)$ unidentified. Assumptions 1–4. **Reusable:** yes, to delimit what is/ isn't free without functional form. [explicit, p.493]
- **Theorem 4 (parametric full identification).** Box–Cox $\log v$ (eq.8) $+$ $g_1(h_1)=g_1(h_2)$ $\Rightarrow$ model (2a,b) identified. Assumptions 1–3, 5, 6. **Reusable:** **yes — this is my identification citation.** [explicit, p.493]
- **Theorem 5 (identification with wage random effect).** With Assumption 7 (exogenous wage shifter $X$ excluded from preferences) $+$ moment bound (Assumption 8): $v$ identified up to an $h$-term, $\theta(\cdot)$ up to a constant, conditional offered-wage distribution identified; with Box–Cox, full identification. **Reusable:** yes for justifying the separability of my ability channel, conditional on excluding the wage shifter from $v$. [explicit, p.494]
- **Box–Cox utility (eq. 8).** $\log v(C,h)=\gamma_1\frac{C^{\alpha}-1}{\alpha}+\gamma_2\frac{(1-h/M)^{\beta}-1}{\beta}+\gamma_3\frac{(C^{\alpha}-1)}{\alpha}\frac{((1-h/M)^{\beta}-1)}{\beta}$ [explicit form, p.493; exact constant arrangement [verify] against the printed OCR]. Globally concave; justified by invariance principles (Dagsvik & Strøm 2006; Dagsvik & Røine Hoff 2011). **Reusable:** yes — same family as my preference block.

---

## 11. Robustness and specification sensitivity

- **Wage-heterogeneity stance (their main robustness axis).** They estimate the two "extreme" cases — across-job wage variation (M1) vs individual wage heterogeneity / ability (M2) — and select M2 on fit. [explicit, pp.496–498] *Lesson for me:* the ability-vs-job-residual decomposition of wage variance is a real specification fork; my $\sigma$ inherits this ambiguity, and the M1/M2 contrast is the precedent for treating it as a robustness choice rather than a settled object. The authors decline to separate inter- vs intra-individual wage effects ($\xi+\eta$), judging it to hinge too much on functional form — directly relevant to how hard I can push the ability/access boundary. [explicit, p.496 fn.8]
- **Hours grid / cell aggregation.** Thin joint-hours cells force them to aggregate to six cells for goodness-of-fit; the eight-point grid is fixed. [explicit, p.497] *Lesson:* my 901/101 grids are far finer; their thin-cell problem is a caution about over-disaggregating couples.
- **Measurement error / division bias.** The negative observed wage–hours correlation ($-0.22$ women, $-0.17$ men) is a measurement artefact handled by the three-stage procedure. [explicit, pp.495–496] *Lesson:* a stress test I should run if I ever construct wages by division; with EUROMOD income I sidestep it but should note it.
- **What they do NOT stress-test:** number of draws (no simulation draws — analytic), number of starts, alternative opportunity-set definitions, reference states (no welfare). [not-established] So this paper gives me *no* guidance on effective-sample-size or draw-growth stability — those concerns are specific to my importance-sampling layer and unaddressed here.

---

## 12. What I can cite this paper for

- The **RURO/latent-jobs factorisation** of labour supply into preference utility $\times$ opportunity measure, and the closed-form choice probability (Theorem 1). [explicit]
- The **formal identification problem** of separating preferences from the opportunity mechanism on cross-section data, and its resolution under exclusion + Box–Cox + an offered-hours normalisation (Theorems 2–5). This is my primary identification citation. [explicit]
- The terms **"opportunity measure"** ($\theta g_1 g_2$) and **"opportunity density"** ($g_1 g_2$), and $\theta$ as a **job-availability** scalar. [explicit, p.489]
- The design choice that the **wage channel is individualised while the hours channel is institutional/common** across observationally identical agents. [explicit, pp.490–491]
- The interpretation of a **wage random effect as individual ability** entering the opportunity measure (support for my ability channel). [explicit, p.494]
- That **non-labour income enters only consumption, not the opportunity measure** (the exclusion restriction). [explicit, pp.492–493]
- A **joint couples** latent-jobs labour-supply application as precedent. [explicit]
- Benchmark **female participation/hours elasticities** ($\approx 0.33$ / $\approx 0.6$) with negligible male responses. [explicit, Table II]
- That conventional discrete-choice (van Soest) **PT/FT preference dummies are formally equivalent to peaks in the opportunity density**, with the latter carrying a structural rationale. [explicit, p.495]

---

## 13. What I should NOT cite this paper for  [overclaim risks]

- **No welfare object.** Do not attribute any money-metric welfare, equivalent income, EV/CV, or inclusive-value welfare core to this paper. [not-established]
- **No $W^1$–$W^6$.** The compensation–responsibility family is *not* here; it comes from the companion theory and the equivalent-income literature. [not-established]
- **No decomposition.** Do not cite for any inequality index or Shapley/Shorrocks split — and especially not for a three-way access/ability/preference decomposition. Its only "decomposition" of opportunity is conceptual, not an inequality decomposition. [not-established]
- **Two-way framing, not three-way.** Where the paper distinguishes sources it is *preferences vs opportunity (constraints)* — a **two-way** cut. My three-way access/ability/preference vocabulary is *my* refinement; when citing, say the paper separates preferences from the opportunity mechanism, and note that the access/ability sub-split is my extension. [explicit that it is two-way]
- **Occupation/sector.** Do not cite as support for an estimated occupation-as-access layer; the estimated model has no occupation and no sector. Their informal "sector" (health care, public sector) is industry-flavoured, not my ISCO `loc4`; do not let it license `loc4`/`lindi` slippage. [explicit by absence]
- **Random vs deterministic opportunities.** The paper treats opportunity sets as genuinely **stochastic** (Poisson-scattered, the "RO" is substantive). My design treats opportunities as **deterministic feasible sets** with "RO" as estimation machinery only. Do not import their random-opportunities interpretation as if it were mine. [explicit, Assumption 2]
- **Sampling correction.** Do not cite their enumeration-based estimation as evidence that a $-\log\pi$ proposal correction is dispensable; that is specific to fixed-grid enumeration. [explicit by construction]
- **Theory-paper boundary.** This is a Dagsvik–Jia empirical/identification paper; it is unrelated to the Haydar–Maniquet axiomatic theory paper. Never route any axiom, characterisation, or proof of the $W$-family through this citation, and never read this paper as a theory contribution to my JMP. [boundary]

---

## 14. Direct quotes worth citing

Short verbatim phrases for my own annotation (each kept brief; page numbers as printed):

- p.489 — "The parameter θ is clearly a measure of job availability".
- p.489 — "the opportunity measure" / "the opportunity density" (their naming of $\theta g_1 g_2$ and $g_1 g_2$).
- p.492 — identification "arises from the fact that observed labor supply behavior is a result of both preferences … and latent job choice constraints".
- p.492 — on panel/cross-section data: "hard to see how this would help to solve the identification problem".
- p.494 — the wage intercept term is meant to "represent the effect of observed and unobserved individual ability".

(If a longer block is needed for a direct quotation in the draft, pull it from the PDF at the cited page rather than expanding these.)

---

## 15. Open questions and risks for my draft

- **Parametric identification is the whole game.** The paper makes unmistakable that the preference/opportunity separation is *not* design-identified on a cross-section; it is bought with Box–Cox + exclusions + a normalisation. My access/ability/preference decomposition inherits this — I must state plainly that the decomposition's credibility rests on those parametric assumptions and on synthetic recovery, not on an instrument I do not have. Risk: a referee reads the decomposition as data-identified; pre-empt it.
- **Ability vs across-job residual ($\eta$ vs $\xi$).** The authors refuse to separate inter- from intra-individual wage variation as "not theoretically sound" given the information. My ability channel ($\sigma$, returns to education/experience) sits on exactly this fault line; pushing the ability/access boundary too hard repeats the move they declined. Treat the ability/access re-allocation as a *named robustness* (project state §6.3), not a headline.
- **Hours channel as institutional/common.** Their justification for common $g_1(h)$ (union/negotiation-set hours) supports my "hours/employment common in the proposal" choice — but it also implies access heterogeneity I *do* model (region, occupation, year) is a stronger claim than theirs; I should be ready to defend that those access shifters are identified, given the paper warns even $g_1$'s level is delicate.
- **No guidance on integration error.** The paper is analytic/enumeration-based and says nothing about importance-sampling effective sample size or draw-growth stability — the live blockers in my singles welfare integral. This paper cannot reassure on that; it is orthogonal.
- **"Sector" temptation.** The paper's sector talk is a standing temptation to conflate occupation and industry. Discipline: cite only for the *idea* that occupation/sector belongs in $g$ if added, never as an estimated precedent, and keep `loc4` ≠ `lindi`.

---

## 16. TL;DR for retrieval

Dagsvik & Jia (2016, *JAE*) is the canonical identification paper for the latent-jobs/RURO factorisation — preference utility $v(C,h)$ times an opportunity measure $\theta g_1(h)g_2(w\mid h)$ — proving that on cross-section data preferences and opportunities are non-parametrically unseparable (Thms 2–3) but identified under a Box–Cox utility plus an offered-hours normalisation and the exclusion of non-labour income from the opportunity measure (Thms 4–5), with a wage random effect interpreted as individual **ability** entering $g$ (my ability channel) and $g_1(h)/\theta$ supplying my **access** channel. It is my primary **identification** and **opportunity-mechanism** citation and a benchmark for elasticities (female participation $\approx 0.33$), but it computes **no welfare, no inclusive-value money metric, and no decomposition**, contains nothing of the $W^1$–$W^6$ family, uses a **two-way** preference/opportunity cut and **genuinely stochastic** opportunity sets, and must never be read through the Haydar–Maniquet theory boundary.
