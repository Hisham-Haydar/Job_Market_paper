# JMP_W1_stochastic_ability_set_bridge_v1.md — market-only random-set Measure 1: construction, compatibility and verdict

| Field | Value |
|---|---|
| Mission | JMP-W1-MARKET-SET-BRIDGE-1 (market-set construction author) |
| Date | 2026-09-12 |
| Controlling documents | `JMP_market_set_bridge_and_parallel_work_ruling_v1.md` §A–G; `JMP_BRIDGE1_amendment_v1.md` §A–I. **Where they differ, the amendment controls.** |
| Status | DESIGN / IDENTIFICATION MEMO. No execution, no calibration, no re-estimation, no pricing, no package change, no theory-paper change. |
| Output file | `JMP_W1_stochastic_ability_set_bridge_v1.md` |
| Version note | No `JMP_W1_stochastic_ability_set_bridge_v*.md` was supplied to this chat and none was reported by SRC-1/SRC-2. If the repository already contains a v1, **halt and re-issue this document as v2 without editing the existing file** (ruling, Outputs and restrictions). |
| Intended path | `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_v1.md` |

## 0. Authoritative inputs actually used

1. `JMP_market_set_bridge_and_parallel_work_ruling_v1.md` (sections A–G).
2. `JMP_BRIDGE1_amendment_v1.md` (sections A–I) — controlling.
3. `jobs_and_wellbeing.tex` via the SRC-1 quotation of its primitives and Measure 1 (extract §(a)), and `jobs_and_wellbeing_agent.md` for the theorem inventory. The `.md` copy is treated as the older labelled copy.
4. `JMP_bridge_source_extract_v1.md` (SRC-1/SRC-1-A), sections (a)–(h).
5. `JMP_bridge_source_extract_v2.md` (SRC-2), sections 1–6, superseding v1(f)/(g) on spec provenance.
6. `W1_latent_set_identification_note_v1.md` — Findings 1b, 2, 3, §2.3, §3.1, §4.1, §5.
7. `JMP_W1_BASELINE_F1_authorization_and_Cobs_ruling_v1.md`; `JMP_measure_map_acceptance_v1.md` (findings F1–F10, in particular **F6**); `baseline_f1_verification_v1.md`.
8. Dagsvik and Jia (2016), primary text: Assumption 2 (incl. footnote 2), Theorem 1 eq. (2a,b), Theorems 2–3, Assumption 7. Canonical transcription, pinned hash `9cbb7a56…` (PDF) / `29cf5975…` (markdown).
9. `JMP_positive_fit_diagnostics_memo_v2b_addendum.md` and addendum item A7, for POSFIT v2b status only.
10. Mission addendum items A1–A7.

Not used because not supplied and not indispensable: the R5 draft, the P/A/B/D operator code, the S12 node manifest (SRC-1 (e): does not exist under that name), the equivalence-scale note. None of the conclusions below depends on them; §12 lists what would change if they arrive.

---

## 1. VERDICT

**Amendment §I classification: D.**

> **D. NO — preserving the desired direct opportunity-set interpretation requires an augmented/re-estimated positive model.**

with a constructive fallback in class **C** that is recommended for immediate use (§11).

The reasoning is not "g alone is insufficient". It is sharper and it goes the other way:

> **Main finding (F-BRIDGE-1).** Under the set law that *exactly* reproduces the accepted S11 criterion, the realised market ability set is, almost surely, **the whole common market support** in job-attribute space. Literal market-only Measure 1 therefore takes the closed-form value
> $$W^{1,M}_i \;=\; C_i^{\rm obs}\exp\!\Big[\tfrac{L_i(j_i^{\rm obs})-L_i(h_{\min})}{\beta_c}\Big],\qquad h_{\min}=5,$$
> **deterministically, for every household**, and is invariant to every one of the 29 estimated opportunity parameters. It carries **zero opportunity content**. Its only remaining set input, $h_{\min}=5$, is `DEFAULT_H_MIN` in `continuous.py` — a proposal-support convention (addendum A3), not a data feature.

In the ruling §C taxonomy this splits into a clean dichotomy:

| Construction | Ruling §C class | Set-sensitive? |
|---|---|---|
| Literal min over the set law implied by the accepted likelihood | **1 — implied by the accepted model** | No: degenerate at the support floor |
| Any finite random-set law (iid-$n$, finite-$\Lambda$ Poisson, threshold set) | **4 — a changed positive model requiring new estimation** (usable as **3** if declared a sensitivity family) | Yes, but only through a primitive the likelihood cannot see |

The two classes do not overlap. There is no construction that is both implied by the accepted model and sensitive to the estimated opportunity structure. That is the demonstrated incompatibility, and per the ruling it is a valid scientific finding.

---

## 2. What enters systematic utility, and what follows (amendment §B)

### 2.1 Established from source

Addendum **A1**, corroborated by SRC-1 §(b)/(f)/(g), SRC-2 §1–2, the accepted measure map (§2.1, "Content of $L$": leisure only; coefficients carry age, age² and child shifters; **no wage or occupation term**), and `baseline_f1_verification_v1.md` (production dependency audit: the reachable call graph indexes only `beta_c`, the leisure intercept/age/age²/children coefficients, and leisure curvatures):

$$u_i(C,j)\;=\;\beta_c\,\mathcal B(C;\theta_c)\;+\;L_i(h_j),\qquad
L_i(h)=\beta_\ell(\mathbf x_i)\,\mathcal B\!\big(\tilde\ell(h);\theta_\ell\big),\quad \tilde\ell(h)=\tfrac{80-h}{10},$$

with $\theta_c=0$ exactly in both groups (SRC-2 §1), so $\mathcal B(C;0)=\log C$, and $\mathbf x_i=$ (age, age², and for women children). For couples the index is additive across spouses because `beta_ll` is **absent from the 47-coordinate list**, so the code path evaluates it as a hard `0.0` (SRC-1 §(b); addendum A2; latent-set note §1.2).

Everything else estimated — the five hours-band coefficients, the six log-normal wage coefficients incl. $\sigma$, the twelve market/region/urban/year coefficients, the six occupation coefficients — enters the **opportunity kernel** $g$, never $u$. SRC-2 §2(b) records the executed index verbatim:

$$V = u + \log_h + \log_w + \log_{\rm market} - \log_{\rm prior} \;=\; u + \log g - \log q .$$

**Amendment §A compliance, stated once and maintained throughout.** $V_i(j)$, $\varepsilon_{ij}$ and $g_i(j)$ are three separate objects. $\log g$ appears in the index because it is the **opportunity component of the behavioural choice law** (an importance-corrected offer intensity), **not** a preference or welfare-utility component. No monotone function of $g$ is inserted into $m_i(j)$ anywhere in this memo.

### 2.2 The consequence the amendment requires

Measure 1 pays every job in the reference set the same hypothetical amount $w$ (§3.1). Consumption is therefore held flat across reference jobs, and the only job attribute that can move $m_i(j)$ is whatever enters $u$ besides consumption. Under A1 that is **hours alone**. Hence:

> **F-BRIDGE-2.** Conditional on a realised ability set, two market jobs with the same hours have **identical** $m_i(j)$ however much they differ in wage, occupation, sector, region or year — even though every one of those attributes moves the behavioural choice law through $g$ and every one of them is estimated.

Is this an intended feature, a limitation, or evidence for a richer preference specification? All three, in a specific order, and the ordering matters:

1. **It is an intended feature of the positive specification, and it is load-bearing.** Addendum A1 states it exactly: the non-overlap of the $V$-block and the $g$-block **is** the exclusion restriction as coded; there is no other. This is the Dagsvik–Jia Assumption-7 device (observed wage covariates excluded from preferences and entering offered wages). Take wage or occupation into $u$ and the exclusion that identifies $g$ is gone.
2. **It is a limitation for market-only Measure 1 specifically**, and a severe one, because it collapses the job space to a single welfare-relevant coordinate (hours) before any set law is even discussed. The reference set can only matter through the hours it contains.
3. **It is evidence that a richer preference specification would eventually be required** — but it is *not* evidence that one can simply be added. Dagsvik–Jia Theorem 3 is explicit that under Assumptions 1–4 the hours-specific utility factor $\delta(h)$ is **not identified** even though the offered-hours distribution is. The current spec resolves that non-identification by fiat, setting $\delta(h)\equiv 1$ and attributing all hours structure (the pt1/pt2/f35/ft/lh bands) to $g$. A richer $u$ that reintroduced hours- or occupation-specific preference terms would re-open exactly the direction the primary source proves is unidentified.

**No amenity is added here, and nothing is re-estimated.** The point is recorded as a structural trade-off in this model class, not as a defect to patch.

---

## 3. Deterministic foundation (ruling §A)

### 3.1 Measure 1 and the minimum representation

The theory text (SRC-1 §(a), `jobs_and_wellbeing.tex:256–269`) defines

$$W(z,R,A;\mathbf y)=w \iff z\;I\;\max\nolimits_R\{B\},\qquad
(c',j')\in B \iff j'\in A \text{ and } c'=w .$$

Define $m_i(j)$ by $(m_i(j),j)\,I\,z_i^{\rm obs}$.

**Existence and uniqueness of $m_i(j)$.** $R$ is continuous and strictly monotonic in consumption (standing assumptions, `jobs_and_wellbeing_agent.md`), so for each $j$ the map $c\mapsto(c,j)$ crosses the indifference class of $z^{\rm obs}$ at most once; it does so at least once provided the indifference set is reached within $\mathbb R_+$. Under the accepted specification $u_i(c,j)=\beta_c\log c + L_i(h_j)$ with $\beta_c>0$, so $m_i(j)$ exists, is unique, and is strictly positive for every $j$ and every $C^{\rm obs}_i>0$:

$$\boxed{\,m_i(j)=C^{\rm obs}_i\exp\!\Big[\tfrac{L_i(j^{\rm obs}_i)-L_i(j)}{\beta_c}\Big]\,}$$

**Minimum representation.** Fix $w$. Since $u$ is strictly increasing in $c$, $\max_R B$ at pay $w$ is attained at the job maximising $L_i$ over $A$, and $u(w,\arg\max_A L_i)=u(z^{\rm obs})$ holds exactly at $w=\min_{j\in A}m_i(j)$. Hence

$$W^{1}_i(A)=\min_{j\in A}m_i(j),\qquad \text{equivalently}\qquad
W^1_i(A)=C^{\rm obs}_i\exp\!\Big[\tfrac{L_i(j^{\rm obs}_i)-\max_{j\in A}L_i(j)}{\beta_c}\Big].$$

**Infimum/supremum form.** When $A$ is infinite the maximum of $L_i$ over $A$ need not be attained. Everywhere below, $\min$ is read as $\inf$ and $\max$ as $\sup$; §4 shows this is not a technicality but the whole issue. Under the accepted specification $L_i$ is continuous, so $\inf_{j\in A}m_i(j)=\inf_{j\in\overline A}m_i(j)$ and the infimum over a dense subset of a set equals the infimum over that set.

**Positivity/domain conditions.** $C^{\rm obs}_i>0$ (verified: the consumption guard binds zero times, `baseline_f1_verification_v1.md`); $\beta_c>0$ (estimated 2.0387 singles / 2.1017 couples, SRC-2 §1); $A\neq\emptyset$ (§9.2); $z^{\rm obs}$ in the evaluation domain (§9.1).

### 3.2 The PI's example, reproduced

| Person | $A$ | $m(1)$ | $m(2)$ | $m(3)$ | $W=\min_{j\in A}m(j)$ |
|---|---|---:|---:|---:|---:|
| $i$ | $\{1,2\}$ | 100 | 120 | 40 | **100** |
| $k$ | $\{2,3\}$ | 50 | 70 | 60 | **60** |

Verified arithmetically (Appendix A, Toy 1). Two things the example is for. First, $m_i(3)=40$ is the smallest number in $i$'s row and is **irrelevant**, because job 3 is not in $i$'s set: the measure reads the set, not the job space. Second, the same job index carries different $m$ across people, because $m$ is defined by *that person's* indifference through *their* observed bundle.

**Anti-monotonicity.** $A\subseteq A'\Rightarrow W^1(A)\ge W^1(A')$: a minimum over a larger set is smaller. This is not a side remark. It says that under Measure 1, at a fixed observed bundle, **better opportunities lower measured well-being**. That is the responsibility content of the axiom pair (Responsibility For Equal Pay + Independence of $\mathbf y$, `thm:w1`) and it is the intended normative direction; but it must be stated in the paper, because the naive reading — "unequal job opportunities ⇒ unequal well-being, same sign" — is the opposite of what the measure does.

### 3.3 Why actual pay at unchosen reference jobs is not an input to $m_i(j)$

By construction $B$ prices **every** job in $A$ at the same $w$. The comparison is "your bundle versus the best job you could hold if all jobs paid alike", so the realised pay profile $\mathbf y$ never enters the right-hand side. This is exactly Independence of $\mathbf y$, one of the two axioms characterising $W^1$ (`thm:w1`). Empirically: $m_i(j)$ reads $h_j$ through $L_i$ and nothing else about $j$; the EUROMOD-priced disposable income $C_i(j)$ at an unchosen $j$ is never formed. Note the asymmetry preserved throughout: unchosen pay is irrelevant to $m$, but **not** to the behavioural conditioning likelihood (§6.3).

This also disposes of a possible confusion with $W^3$ (laissez-faire), which shifts the whole pay profile, and with $W^6$ (min of equal pay under Full Compensation). Only $W^1$ is in scope here.

### 3.4 The $h_{\min}$ reduction — GOAL 1 PRIOR: **VERIFIED**, with its scope stated

$L_i$ is strictly decreasing in hours iff $\beta_\ell(\mathbf x_i)>0$, because $\mathcal B(z;\theta)$ is strictly increasing in $z$ for every $\theta$ (derivative $z^{\theta-1}>0$) and $\tilde\ell$ is strictly decreasing in $h$. The latent-set note establishes $\beta_\ell(\mathbf x_i)>0$ **over the whole admissible covariate domain**, not merely in sample: $\beta_\ell$ is a quadratic in centred age with positive leading coefficient in all four blocks, with domain minima $7.81$ (sm), $5.87$ (sf), $3.98$ (cm), $12.59$ (cf), the last holding for any child count below 41.2 (Finding 1b; independently corroborated by the S12 premise audit `home_is_argmax_L: pass=true, n_fail=0` over $1{,}540\times2{,}048$ and $2{,}223\times2{,}048$ evaluations).

Therefore, **conditional on a realised nonempty market set $A^M_i$**:

$$\boxed{\;W^{1,M}_i(A)=C^{\rm obs}_i\exp\!\Big[\tfrac{L_i(j^{\rm obs}_i)-L_i\big(h_{\min}(A)\big)}{\beta_c}\Big],\qquad h_{\min}(A)=\inf\{h(j):j\in A\}.\;}$$

Scope, exactly as amendment §C requires:

- The reduction is **conditional on a realised set**. It is a statement about the welfare functional, not about anything observable.
- It depends on the sign of $\beta_{\ell 0}$ and must be re-verified whenever the preference block moves.
- **Couples.** With `beta_ll` $=0$ the minimand $L_m(h_m)+L_f(h_f)$ is additively separable, so *if* the household reference set is a Cartesian product $A_m\times A_f$, the household minimum is attained at $(h^m_{\min},h^f_{\min})$ and separates. What $\beta_{\ell\ell}=0$ buys is exactly that separability of the **objective**. What it does **not** buy: any statement about the set law (§9.3), and any licence to assume the reference set is a product. For a non-product $S\subseteq A_m\times A_f$, additive separability still gives $W^{1,M}(S)\ge W^{1,M}(A_m\times A_f)$, so the product assumption is a **signed** approximation (it under-states $W^{1,M}$), which is at least usable as a bound.
- $m$ is strictly **increasing** in $h$, so $\{j:m_i(j)\le w\}=\{j:h_j\le h_i(w)\}$ for the monotone household-specific transform $h_i(w)$ implied by $L_i$. Every distributional statement in §5 is therefore a statement about the law of $h_{\min}$ and nothing else.

The two objects the amendment insists on separating are kept separate from here on:

- **(1) conditional welfare given a realised set** — depends on $A$ only through $h_{\min}(A)$; established above;
- **(2) the posterior law $P(h_{\min}\mid j^{\rm obs},X_i)$** — treated in §6, where it is shown *not* to reduce to the marginal hours distribution.

### 3.5 Removal of home from the reference is not a change to behavioural availability

Dropping $o$ from the **welfare reference set** changes the argument of $W^1$ and nothing else. Non-employment remains an alternative in the behavioural model, remains in both estimation samples, and keeps its own proposal row (`non_employment_rows: log_prior: log(0.10)` for singles; the quadrant law for couples). The two operations are logically independent and are never performed jointly in this memo.

With $o$ in the reference, $L_i(o)>L_i(h)$ for all $h\ge5$ gives the latent-set note's Reading I: $W^1_i=m_i(o)$, i.e. exactly the verified Mapping-F baseline, and the set drops out. The whole bridge exists because Reading II — home excluded — was expected to restore set dependence. §4 shows it does not, for a reason that is not the one Reading II anticipated.

---

## 4. The set law implied by the accepted likelihood — mandatory gate (ruling §C; amendment §F; addendum A4)

### 4.1 The process that reproduces the executed criterion, exactly

Dagsvik–Jia Assumption 2 (primary source, pinned hash) places the taste shifters of available jobs on a **Poisson process on the taste axis** with intensity $\theta\varepsilon^{-2}$, the offered attribute combinations being independent of the taste shifters and distributed according to $g_1(h)g_2(w\mid h)$. Their footnote 2 gives the additive-utility equivalent used by the executed code: the corresponding intensity is $\theta e^{-\varepsilon}$ on $\varepsilon\in\mathbb R$. The paper is explicit that this intensity form is *necessary* for the choice of job to satisfy IIA — Dagsvik (1994)'s result, quoted in the Assumption 2 discussion.

So the candidate law is not an outside analogy (addendum A4 is confirmed). Written in this application's notation, and matching the latent-set note §4.1: the marked point process

$$\Pi_i=\{(j,\varepsilon)\}\ \text{on}\ \mathcal J\times\mathbb R,\qquad
\text{intensity}\quad \kappa_i\,\lambda_i(dj)\times e^{-\varepsilon}d\varepsilon,\qquad \lambda_i=g_i\,\nu,$$

with the home option carried at intensity $g_i(o)\equiv1$. Three exact consequences:

1. the induced utility process $\{u_i(j)+\varepsilon\}$ on $\mathbb R$ is Poisson with intensity $\Theta_ie^{-v}dv$, $\Theta_i=\kappa_i\int e^{u_i}d\lambda_i$;
2. its maximum is Gumbel with location $\log\Theta_i$;
3. $\Pr(\text{argmax}\in B)=\int_Be^{u_i}d\lambda_i\big/\int e^{u_i}d\lambda_i$ — **exactly the executed criterion**, of which $V=u+\log g-\log q$ under `jgroup_logsumexp` is the importance-sampled realisation, and the source of the $\kappa_i$-cancellation.

This is the unique construction in play that reproduces the accepted likelihood without approximation. Everything in §5 is an alternative to it, not a version of it.

### 4.2 The projection onto job space is a.s. everything

Fix any region $B\subseteq\mathcal J$ with $\lambda_i(B)>0$. The number of points of $\Pi_i$ with mark in $B$ is Poisson with mean

$$\kappa_i\,\lambda_i(B)\int_{\mathbb R}e^{-\varepsilon}d\varepsilon \;=\; +\infty ,$$

because the taste-axis intensity is not integrable at $\varepsilon\to-\infty$. Hence, almost surely, **every $g_i$-positive region of job space contains infinitely many available jobs**. The realised ability set, projected onto job-attribute space, is a.s. dense in $\operatorname{supp}(g_i)$; the number of *attractive* jobs is finite (points with $\varepsilon>t$ are Poisson with finite mean $\Theta_ie^{-t}$), but the number of jobs of any given type is not.

This is the same feature that makes the max Gumbel and the choice law logit. It is not an artefact of the application: it is what Assumption 2 says.

> **F-BRIDGE-3 (correction of record).** `W1_latent_set_identification_note_v1.md` uses two different set laws in two different sections. §4.1 uses the marked process on $\mathcal J\times\mathbb R$ above — correct, and the one that reproduces the criterion. §3.1 uses a Poisson process on $\mathcal J$ alone with *finite* intensity $\kappa_i\lambda_i(dj)$ and derives the survival family $\Pr(W^1>x)=e^{-\kappa_i\Lambda_i(x)}$. Those are different processes. Under §4.1's process, $\Lambda_i(x)=+\infty$ for every $x$ with $\lambda_i(\{m_i\le x\})>0$, so the survival function is a step, not an exponential family. The note's own §2.3 labels the finite-count reading "licensed only under an added hypothesis"; this memo establishes that the added hypothesis is **not** the model's, and §5.4 establishes that it is not observationally equivalent to it either. The note's Reading II conclusion — "$\kappa_i\to\infty$ gives the support infimum" — is right about the limit and wrong about the model being away from it: **the model is at the limit.**

### 4.3 The degeneracy theorem

Combining §3.4 and §4.2, for every household $i$ with $\beta_\ell(\mathbf x_i)>0$:

$$\inf_{j\in A^M_i}m_i(j)\;=\;\operatorname*{ess\,inf}_{j\in\operatorname{supp}(g_i)}m_i(j)\;=\;m_i(h_{\min})\quad\text{a.s.},\qquad
h_{\min}=\inf\{h:\ h\in\operatorname{supp} g^H_i\}.$$

The infimum is approached but not attained (§3.1), which is why the inf/sup reading is mandatory here.

**Is $h_{\min}$ common across households?** Yes, and by construction rather than by estimate. SRC-2 §4 establishes analytically that the structural hours-opportunity index on $[5,7.5]$ reduces to $\exp(\beta_E)$ — all band indicators are zero below 17.5 — which is strictly positive for any finite estimated $\beta_E$, for all four groups, **independent of the fitted values**; the wage component is a log-normal renormalised on $[2,590]$, positive throughout; the occupation component is a logit over four categories, positive throughout. So $\operatorname{supp}(g_i)$ is the same set $[5,70]\times[2,590]\times\{1,\dots,4\}$ for every household, and $m_i$ depends on $j$ only through $h$. Therefore

$$\boxed{\;W^{1,M}_i \;=\; C^{\rm obs}_i\exp\!\Big[\tfrac{L_i(j^{\rm obs}_i)-L_i(5)}{\beta_c}\Big]\quad\text{a.s., for every household.}\;}$$

**Corollaries.**

- **No opportunity content.** $W^{1,M}_i$ is invariant to all 29 shared opportunity parameters ($\beta_E$, the five hours-band coefficients, the twelve market/region/urban/year coefficients, the six occupation coefficients, the six wage coefficients incl. $\sigma$) and to $\kappa_i$. Every cross-household difference in $W^{1,M}$ comes from $(C^{\rm obs}_i,\,j^{\rm obs}_i,\,\beta_\ell(\mathbf x_i),\,\theta_\ell)$ — attainment and preferences.
- **It is a preference-driven rescaling of Mapping F.** $W^{1,M}_i/W^{1,F}_i=\exp\{[L_i(o)-L_i(5)]/\beta_c\}$, a household-specific constant $\ge1$ depending on the preference block only. Toy 5 (Appendix A), using S11 numerals transcribed from the latent-set note table and the verified $\beta_c$, evaluates this at the covariate-domain minimum of $\beta_\ell$: **1.0089** (single men), **1.0282** (single women), **1.0123** (couple, woman at 5h and man at home), **1.0292** (couple, both at 5h). It is increasing in $\beta_\ell$, so these are lower ends of the band.
- **Independent corroboration from an accepted record.** Measure-map acceptance finding **F6** reports, for couple 1485200, that *the market minimum is at (0,5)* — at the floor exactly — and that market Measure 6 / W1-F lies between **1.009 and 1.014** across the check households, consistent with the fork's 1–5% range. That is an independently computed confirmation of the location of the minimum and of the order of magnitude of the ratio derived here.
- **The remaining set input is a numerical convention.** $h_{\min}=5$ is `DEFAULT_H_MIN` in `alternatives/continuous.py`, a module-level default that bounds the Uniform$[5,70]$ hours **proposal** used for `log_q_hours`, overridable per call, asserted nowhere as a data feature or theoretical necessity (addendum A3; SRC-1 §(d),(h)). The welfare number moves if the draw floor moves. Per A3 this must be said in terms: **any welfare object whose value depends on the support floor inherits a numerical convention**, and $W^{1,M}$ does.

### 4.4 What this says about the theory-to-model bridge

The mismatch is structural and worth one sentence in the paper. In Haydar–Maniquet the ability set is a **set in job space**, and welfare reads which jobs are in it. In the RURO/Dagsvik class the opportunity object is a **density on (job type, taste) space**, and what differs across agents is not which job types exist but how the intensity is distributed over taste at each type. Projecting the second onto the first throws away exactly the dimension that carries the heterogeneity. The measure is not at fault and the model is not at fault; they are indexed on different spaces.

---

## 5. Random-set welfare distributions: the benchmark families (ruling §B)

These are **added assumptions**, not established properties of S11. They are set out because the ruling requires a constructive object, and because they are where any future set-sensitive design must live.

### 5.1 The common reduction

For any set law whose realisations are finite,

$$H_i(w)=\int \mathbb 1\{m_i(j)\le w\}\,f^M_i(dj)\;=\;G^{H}_i\big(h_i(w)\big),$$

where $f^M_i=g_i/\!\int_{\rm mkt}g_i\,d\nu$ is the normalised market composition, $G^H_i$ its hours marginal, and $h_i(\cdot)$ the monotone transform of §3.4. So $W^{1,M}_i$ is a deterministic increasing transform of $h_{\min}$, and **the entire random-set problem is the law of the minimum offered hours**. Wage and occupation composition enter only by changing nothing at all here — they affect neither $m$ nor $h_{\min}$. They return in §6, through the posterior.

### 5.2 iid-$n$ benchmark (ruling §B as written)

With $n\ge1$ independent market offers from $f^M_i$,

$$\Pr\big(W^{1,M}_i\le w\mid N_i=n\big)=1-\big(1-H_i(w)\big)^{n}.$$

### 5.3 Finite-Poisson counterpart, empty set, large-count limit

With $N_i\sim\text{Poisson}(\Lambda_i)$ and marks iid $f^M_i$ (equivalently a Poisson random measure on $\mathcal J$ with intensity $\Lambda_i f^M_i$), the void-probability formula gives directly

$$\Pr\big(W^{1,M}_i>w\big)=\exp\{-\Lambda_iH_i(w)\}\quad\text{on }\{A^M_i\neq\emptyset\},\qquad
\Pr\big(A^M_i=\emptyset\big)=e^{-\Lambda_i},$$

$$\Pr\big(W^{1,M}_i\le w\mid A^M_i\neq\emptyset\big)=\frac{1-e^{-\Lambda_iH_i(w)}}{1-e^{-\Lambda_i}} .$$

$\Lambda_i$ and $n$ are kept symbolic throughout, as instructed.

**Large-count limit.** $H_i(w)>0$ for every $w>m_i(h_{\min})$ because $g^H_i$ has positive density immediately above the floor (SRC-2 §4), so $\Pr(W^{1,M}_i>w)\to0$ and $W^{1,M}_i\to m_i(h_{\min})$ — the §4.3 value. Rate: if the offered-hours density just above the floor is $c_i$, then $\Lambda_i\,(h_{\min}-5)\Rightarrow\text{Exp}(c_i)$ and $\mathbb E[h_{\min}]-5\approx1/(\Lambda_ic_i)$. Toy 3 (Appendix A) evaluates $1/(\Lambda c)$ with $c=1/109.61$ per hour, the residual-band normalised density implied by the hours-integral already reported in the latent-set note §2.3. The dependence is first-order over any plausible range: $\Lambda=5$ gives $h_{\min}\approx27$h, $\Lambda=50$ gives $\approx7.2$h, $\Lambda=200$ gives $\approx5.6$h. **This is arithmetic on the formula, not a calibration and not a recommended value**; no finite $\Lambda$ is selected anywhere in this memo.

**Degenerate deterministic set law.** $\Lambda_i\to\infty$ is one route to degeneracy; $A^M_i\equiv\operatorname{supp}(g_i)$ with probability one is the other. Both give §4.3. The accepted model sits at both simultaneously.

**Relabelling and duplicate representation.** The law depends on $g_i$ only through the intensity measure $\Lambda_if^M_i=g_i\nu$. Splitting one job type into two copies carrying half the intensity each leaves the measure, hence the law, hence $W^{1,M}$, unchanged; and $\min$ is idempotent under duplication. The construction therefore respects the theory paper's maintained Job Duplication Invariance and is invariant to relabelling. (The related question of whether two offers with the same occupation and hours but different wage are one job or two is §5 of the latent-set note; it does not bite here, because $m$ is constant in the wage.)

### 5.4 Why the finite families are not the accepted model

Two independent arguments, both required by the ruling's "support this classification mathematically".

**(i) IIA.** The primary source states that the $\theta\varepsilon^{-2}$ (equivalently $\theta e^{-\varepsilon}$) intensity form is necessary for the job choice to satisfy IIA. The accepted criterion is a softmax with weights $e^{u}g$, i.e. IIA holds by construction. A mixture of logits over random finite sets is not a logit: the denominator $\sum_{k\in A}e^{u_k}$ is correlated with the inclusion indicators, so $\mathbb E_A[\,\cdot\,]$ does not factor.

**(ii) A three-alternative counter-example.** Toy 2 (Appendix A): home always present, two market jobs present independently with probabilities $\pi_1=0.55,\pi_2=0.30$, utilities $(0,\,0.5,\,2.0)$, iid Gumbel shocks. Exact mixture-of-logits choice probabilities are $(0.4929,\,0.2667,\,0.2404)$; the weighted softmax $e^{u_j}\pi_j/\sum_ke^{u_k}\pi_k$ gives $(0.2425,\,0.2199,\,0.5376)$. The gaps are $+0.25$, $+0.05$, $-0.30$ — an order-of-magnitude disagreement, not a numerical nicety, and signed: the random-set law under-weights the high-utility alternative because it is often absent from the set whose denominator it would otherwise dominate.

This is the mathematical content of the amendment's prohibition. **Never equate $g_i(j)$ with $\Pr(j\in A_i)$**: not as a modelling shortcut and not as an approximation, because reading $g$ as an inclusion probability changes the choice law by the amounts above, and the S11 estimates were obtained under the other one.

**The sharp form of the incompatibility.** Let $\Lambda$ index the finite family. As $\Lambda\to\infty$ the family converges to the accepted model — and the welfare object degenerates to §4.3. As $\Lambda$ falls into the range where $h_{\min}$ is economically informative (Toy 3: $\Lambda$ of order 10, not $10^3$), the choice law departs materially from the accepted one, so the S11 parameter vector is no longer the MLE of the model being used. **The region of the truncation parameter where the welfare object is informative is exactly the region where the positive model is misspecified relative to the accepted estimates.** That is the incompatibility, and it is why the verdict is D rather than B.

---

## 6. Conditioning on the observed choice (ruling §D; amendment §C part 2)

### 6.1 The conditional law

$$P_i(dA\mid \text{observed choice},X_i)\ \propto\ p_i(\text{observed choice}\mid A,X_i;\theta)\,P_i(dA\mid X_i),$$

with the continuous coordinates handled by the corresponding conditional density. Under the §4.1 process this has a closed form (latent-set note §4.1, adopted here): conditioning on the chosen package $y$ and on the attained maximum $M_i=v$, the remaining points form the **same Poisson process restricted to $\{u_i+\varepsilon<v\}$**, with the chosen point inserted at $(y,\,v-u_i(y))$; and $M_i$ is not observed, so the conditional law must be integrated over $M_i\mid y\sim\text{Gumbel}(\log\Theta_i)$, whose location contains $\kappa_i$.

Three points the ruling asks for explicitly.

- **Membership is not choice.** Conditioning on $j^{\rm obs}\in A$ is weaker than conditioning on $j^{\rm obs}$ having been *chosen*; the latter additionally excludes every configuration in which some other point beat it.
- **Adding the observed job to unconditional draws is not a proof of correct conditioning.** Unconditional draws place points above the attained utility with positive probability, and every such point contradicts the observation. The bias is one-sided and makes opportunity sets look better than the data say.
- **Behavioural shocks stay in the conditioning and out of the welfare ordering.** They are what makes $M_i$ random given $(u_i,\lambda_i)$. Excluding them from $R$ (deputy rule, used in §3.4) does not remove them from the selection mechanism.

### 6.2 Under the accepted law, the posterior does not rescue non-degeneracy

Restricting the marked process to $\{u_i+\varepsilon<v\}$ leaves the $\varepsilon\to-\infty$ divergence untouched: for any $g$-positive region $B$, the conditional expected number of points in $B$ is still infinite. So the posterior set is a.s. dense as well, and

$$P\big(h_{\min}\mid j^{\rm obs},X_i\big)=\delta_{\{5\}} .$$

The posterior law of $h_{\min}$ under the accepted model is a **point mass at the support floor**. Object (2) does not save object (1).

### 6.3 Under the finite benchmark, the posterior is *not* the marginal hours law — proved

Take the smallest non-trivial case: $A=\{j^{\rm obs}\}\cup\{J\}$ with one extra offer $J\sim f^M_i$, iid Gumbel shocks. Then

$$P\big(J\in dj\mid j^{\rm obs}\text{ chosen}\big)\ \propto\ f^M_i(dj)\cdot\sigma\!\big(u_i(z^{\rm obs})-u_i(j)\big),\qquad \sigma(t)=\tfrac{1}{1+e^{-t}} .$$

The posterior is the prior **tilted by a strictly decreasing function of the alternative's systematic utility**. Consequences, in the order the mission asks for them:

1. The tilt penalises attractive alternatives, so conditioning shifts the posterior **toward sets whose $h_{\min}$ is closer to $h^{\rm obs}$**. The Goal 1 lead's conjecture is confirmed in direction.
2. The strength of the shift depends on $u_i(j)=\beta_c\log C_i(j)+L_i(h_j)$, hence on the **consumption the alternative offers**, hence on the wage and occupation distribution — and on the taste-shock scale, which fixes the curvature of $\sigma$ ($\tau=1$ here).
3. Therefore two alternatives with **identical $m$** can carry **different posterior weight**. Toy 4 (Appendix A): at an illustrative observed bundle, a 10-hour job has $m=1133.35$ whatever it pays; the low-paid version gets posterior tilt $0.785$ and the well-paid version $0.394$ — a factor of two, at the same $m$.

> **F-BRIDGE-4.** $P(h_{\min}\mid j^{\rm obs},X_i)$ depends on the full joint law of hours, wages, occupation, systematic utility, $\varepsilon$ and opportunity density. It does **not** reduce to the marginal offered-hours distribution. Hence: wages and occupation affect market-only welfare **through the posterior set law, never through $m$**; and the $h_{\min}$ reduction simplifies the **welfare functional** without simplifying the **estimation or inference problem** at all. Both halves of that sentence are established, and the second is the one that matters for costing any future prototype.

### 6.4 The PI's expectation example, with $p$ defined

For person $i$ with $A\supseteq\{1,2\}$, $m(1)=100$, $m(3)=40$: if job 3 belongs to the realised set, $W=40$; otherwise $W=100$. Hence

$$\mathbb E[W\mid\text{information}]=40p+100(1-p)=100-60p .$$

**$p$ is the posterior inclusion probability $p=\Pr\big(3\in A_i\mid j^{\rm obs}_i,X_i\big)$.** It is not $g_i(3)$ — $g$ is an intensity per unit base measure and is not a probability at all (§5.4). It is not the prior inclusion probability either, which is itself a functional of the whole set law ($1-e^{-\Lambda_i f^M_i(\{3\})}$ in the Poisson benchmark). And it is not obtainable from the hours marginal, by §6.3: job 3 is a low-hours job, and how strongly the observation of $j^{\rm obs}$ argues against its presence depends on what job 3 pays. Under the accepted (dense) law $p=1$ and the expectation collapses to $40$; the example is informative only inside a finite family.

Finally, per ruling §D: unchosen jobs' pay **does** inform the conditioning likelihood, through $u_i(j)$ in the tilt, even though it does not enter $m_i(j)$ at fixed $z^{\rm obs}$ and fixed reference set. The two roles of the wage distribution are distinct and both real.

---

## 7. Identification of the random-set law (amendment §D)

Every primitive is classified into the amendment's seven categories. "Identified" always means: identified from the accepted S11 criterion under its maintained parametric form, not non-parametrically.

| # | Primitive | Class | Basis |
|---|---|---|---|
| 1 | Normalised **hours** composition $g^H_i$ (band coefficients $\beta_{h,\rm pt1/pt2/f35/ft/lh}$, $\beta_E$) | **IDENTIFIED UP TO NORMALISATION** | Identified only given $\delta(h)\equiv1$. Dagsvik–Jia Thm 3: under Assumptions 1–4 the offered-hours distribution is identified and $v(C,h)=\lambda(C,h)\delta(h)$ with $\delta(h)$ **not** identified. The spec sets $\delta\equiv1$ by excluding hours dummies from $u$ (A1). The normalisation is a choice, not a finding. |
| 2 | Normalised **wage** composition $g^W_i$ ($\beta_{w0},\beta_{w,\rm educL/H},\beta_{w,\rm pexp},\beta_{w,\rm pexp2},\sigma$) | **IDENTIFIED UP TO NORMALISATION** | Dagsvik–Jia Assumption 7 device: education and potential experience excluded from preferences, entering offered wages. Log-normal form plus the $[2,590]$ renormalisation are maintained. |
| 3 | **Occupation** composition ($\beta_{\rm occ\,2,3,4}^{m,f}$) | **IDENTIFIED UP TO NORMALISATION** | Identified only because occupation is excluded from $u$ by assumption (A1). Occupation-specific preference and occupation-specific availability are not separated by any data feature. |
| 4 | **Relative** market/home availability $\theta_i=e^{\beta_E+c_i}\!\int\!$(mark mass) | **IDENTIFIED** (relative to the home atom normalised to 1) | Addendum A5; latent-set note §2.3 ("a unit of $\nu$-mass in the market carries about 4.2% of the non-employment atom's intensity" at $c_i=0$). Caveat from the primary source: $\theta$ also absorbs psychological costs of working, so it is not a pure availability object and is not a vacancy count. |
| 5 | **Absolute** count/intensity scale $\kappa_i$ | **CANCELS FROM LIKELIHOOD** | Latent-set note Finding 2 with the code demonstration: `_center_proposal` literally applies $\kappa_i=\exp(-c_i\bar E_i)$ for numerical conditioning and leaves the likelihood exactly invariant. Under the §4.1 process the absolute scale is not merely unidentified: the total intensity is **infinite**, so no absolute count exists to identify. |
| 6 | Finite truncation $n$, $\Lambda$, $\varepsilon_0$ | **SENSITIVITY PARAMETER** — and **REQUIRES RE-ESTIMATION** if adopted as a model rather than declared as a family | §5.4. Not a parameter of the accepted model; introducing it changes the choice law by the amounts in Toy 2. |
| 7 | $\delta(h)$, hours-specific preference | **NOT IDENTIFIED** (normalised away) | Dagsvik–Jia Thm 3. Recorded here because it is precisely the welfare-relevant direction (§3.4). |
| 8 | Dependence of availability **across job regions** | **MAINTAINED ASSUMPTION** (Poisson independence), not identified | Nothing in a cross-section of single chosen jobs speaks to the joint occupancy of two regions of the latent space. |
| 9 | Dependence **across spouses** | **MAINTAINED ASSUMPTION** | The intensity factorises at code level ($\log g$ is a sum of per-spouse terms), but see §10.3: a factorising intensity on the space of *pairs* does not make the realised set a Cartesian product. |
| 10 | Taste-shock scale $\tau$ | **IDENTIFIED UP TO NORMALISATION** ($\tau=1$) | Standard logit scale normalisation; it fixes the curvature of the posterior tilt in §6.3, so it is not innocuous for any set-sensitive object. |
| 11 | Proposal $q$ (Uniform hours/wage, empirical occupation frequencies, singles `log(0.10)` non-employment row, couples quadrant law) | **CANCELS FROM LIKELIHOOD** (numerical) | SRC-2 §3. $q$ enters only as $-\log q$ and is an importance-sampling device. |
| 12 | Hours support floor/ceiling $[5,70]$, wage support $[2,590]$ | **MAINTAINED CONVENTION** | SRC-1 §(d),(h); addendum A3. Not estimated, not asserted as a data feature — and the welfare object of §4.3 depends on it. |

**Three naming collisions that must not be allowed to travel.**

- The couples proposal block's `quadrant_law: kappa: 0.2` (SRC-2 §3) is a **proposal-smoothing constant**, not an offer intensity and not the $\kappa_i$ of row 5.
- Node counts 101, 901, 2,048 are **quadrature counts**. A numerical integration node is never an offer, and no offer count can be read off them (ruling §C).
- The old W1-EA kernel masses (median $\int\hat g$ of 0.0773 singles / 147.96 couples) are **not set sizes and not offer counts** (latent-set note §2.3, "Not licensed").

**Is a one-parameter $n/\kappa/\Lambda$ family derivable?** Only conditionally, and the condition is the thing at issue:

> **F-BRIDGE-5.** *Given* the added finite-Poisson-on-job-space hypothesis, the welfare law **is** one-dimensional per household: by §5.1 it depends on the set law only through $(\Lambda_i,G^H_i)$, and $G^H_i$ is estimated, so $\Lambda_i$ is the single free primitive. This one-dimensionality is a genuine consequence of the $h_{\min}$ reduction and is derived, not assumed. But it is **conditional on a hypothesis that §5.4 shows is not the accepted model's**. The accepted model therefore does not deliver a one-parameter sensitivity family; a *declared* extension does. The amendment's instruction is satisfied in both directions: the derivation is given, and the family is not recommended as a model object.

**Unidentified absolute scale versus identified relative availability — kept apart.** Row 4 is identified and is a real empirical object: how much market intensity a household commands relative to its home option, with estimated structure in $\beta_E$, region, urban and year shifters, and estimated hours composition in the band coefficients (addendum A5). Row 5 is not identified and, under the accepted process, not even defined. The paper may say the first. It may not say the second, and it may not convert the first into the second.

---

## 8. Abundance versus desirability (amendment §A and §E)

### 8.1 The three objects, kept separate

$V_i(j)$ (systematic welfare-relevant utility), $\varepsilon_{ij}$ (behavioural taste shock), $g_i(j)$ (opportunity density) are distinct throughout. The executed index admits the algebraic form $u+\log g-\log q$; **$\log g$ is an opportunity component of the choice law, not a preference component**, and no monotone function of $g$ enters $m_i(j)$ anywhere. An abundant job may be systematically unpleasant: high observed choice frequency at a job type is consistent with high availability offsetting low desirability, and the model is built to express exactly that.

### 8.2 What actually separates low preference from low availability

Only two things, and neither is a data feature:

1. **The covariate non-overlap (addendum A1).** Education, potential experience and its square, occupation `loc4`, region, urban/rural, survey year and the hours-band indicators enter $g$; age, age² and children enter $V$. This is the exclusion restriction as coded, and there is no other. It is the Dagsvik–Jia Assumption-7 device for the wage block.
2. **Functional form.** $V$ is Box–Cox in leisure and consumption — smooth and monotone. $g$'s hours component is a piecewise-constant band index with fixed cut points ($\rm pt1=[17.5,21.5]$, $\rm pt2=[28.5,30.5]$, $\rm f35=[33.5,36.5]$, $\rm ft=[36.5,40.5]$, $\rm lh=[44.5,70]$, F35 reference); the wage component is log-normal.

For the **hours** dimension there is no exclusion restriction at all — the separation is pure functional form, and it is exactly the direction Dagsvik–Jia Theorem 3 proves is not identified. Cross-household variation in region, urban status and year identifies shifts in the *level* of market access; nothing identifies the *hours shape* of opportunity against an hours shape of preference.

### 8.3 Could omitted amenities be absorbed into $g$ or $\varepsilon$?

Yes, and the routing is predictable:

- an amenity correlated with **hours** (a fixed cost of working, a preference for standard full-time schedules, commuting) is absorbed by the band coefficients — the $\delta(h)$/$g_1(h)$ confound;
- an amenity correlated with **occupation or region** is absorbed by $\beta_{\rm occ}$ / $\beta_{E,\rm drgn}$, because those covariates appear only in $g$;
- a purely idiosyncratic amenity is absorbed by $\varepsilon$;
- only an amenity correlated with **age or children** would contaminate the preference block instead.

Since the welfare-relevant coordinate is hours (§2.2) and the welfare-relevant region is the low-hours tail (§3.4), the parts of $g$ that a set-sensitive market Measure 1 would lean on hardest are precisely the parts most exposed to absorbed preference structure. This is the substantive reason, independent of §4, to distrust any number produced by such a construction.

### 8.4 POSFIT v2b — diagnostic weight only

POSFIT v2b reports real choices being more predictable than the model's own self-simulated choices. That pattern is *consistent with* $\varepsilon$ carrying too much dispersion or systematic preferences being too sparse — which is what A1 would lead one to expect from a $V$ containing only leisure and consumption. Two limits on how far this can be pushed:

- addendum **A7**: all nine zero-probability cells are **unrepresented finite-panel regions, not structural zeros**, and log scores were floored at $p=10^{-12}$ for those rows. The comparison is therefore contaminated by the panel's finite support, in the direction of exaggerating the model's poor self-prediction.
- POSFIT verdicts remain open under the existing decision rules.

**It is suggestive diagnostic evidence and nothing is claimed to be proved by it.** In particular it is not offered as evidence for or against §4.3, which is an exact statement about the set law and does not depend on fit.

---

## 9. Threshold and effective sets (amendment §G) — diagnostic candidate only

$A_i(\tau)=\{j:g_i(j)\ge\tau\}$ assessed on the four grounds required.

**Normalisation dependence — fatal as written.** $g_i$ is identified only up to the household factor $\kappa_i$ (§7 row 5), and the executed code *actually applies* such a factor: `_center_proposal` subtracts the proposal-weighted within-set mean of $\log g^{\rm market}$, i.e. substitutes $\kappa_i=\exp(-c_i\bar E_i)$, for numerical conditioning. The value of $g_i(j)$ therefore differs between the centred and uncentred index while the likelihood is unchanged, so a fixed $\tau$ selects different sets in the two representations. $A_i(\tau)$ is not a well-defined object of the accepted model. It also depends on the base measure $\nu$: $g$ is a density, so a nonlinear reparameterisation of the job space moves the level sets.

**Discontinuity — and it lands exactly on the welfare-relevant region.** $g^H_i$ is piecewise constant with the cut points above, and all bands sit at or above 17.5 hours. Below 17.5 all indicators are zero, so $\log g^H\equiv\beta_E$ is **flat across the whole of $[5,17.5]$** (SRC-2 §4). Consequently, as $\tau$ rises past the residual level, the entire interval $[5,17.5]$ — which contains the floor and hence determines the welfare number — is deleted **at once**, and

$$h_{\min}\big(A_i(\tau)\big)\ \text{jumps from } 5 \ \text{to } 17.5\ \text{(and thereafter up the ladder } 28.5,\ 33.5,\ 36.5,\ 44.5).$$

$W^{1,M}$ is therefore a **step function of $\tau$ taking at most six values**, the ordering of deletions being governed by the estimated band coefficients. There is no interior $\tau$ at which the family varies smoothly.

*Named source discrepancy, not resolved here.* SRC-1 §(f) lists five hours-opportunity coefficients ($\beta_E$, pt1, pt2, ft, lh) with **F35 as the reference band**, i.e. carrying no coefficient; SRC-2 §4 quotes a block that also includes `working_f35 / beta_h_f35`. If F35 is the reference band then $[33.5,36.5]$ sits at the residual level and is deleted in the same step as $[5,17.5]$, which changes which rungs the ladder has. The **step-function conclusion and the $5\to17.5$ jump are unaffected either way**; only the upper rungs are. Flagged for the source pass, not resolved by this memo.

**$\tau$-sensitivity.** By the same fact, the entire spread of the family is realised at one critical $\tau$. A family whose output is a six-point ladder with one dominant jump cannot be presented as a continuous robustness curve.

**Is a cumulative-mass rule (90/95/99%) more scale invariant?** On the $\kappa$ dimension, yes: a retained-mass rule uses $f^M_i=g_i/\!\int g_i$, which is invariant to $\kappa_i$ and to the centering, and to linear changes of units. It does **not** fix the second problem and introduces a third: because the density is flat on $[5,17.5]$, a highest-density-region rule at a target mass of 90/95/99% will generically require cutting *inside* a constant-density region, where the rule provides no ordering at all. The tie-break is arbitrary and it is the tie-break that sets $h_{\min}$, hence the welfare number.

**Can either serve as a bound or robustness family?** Yes, in one direction only, and this is the usable part. $A_i(\tau)$ is decreasing in $\tau$, $W^{1,M}$ is anti-monotone in the set, so $\tau\mapsto W^{1,M}_i(A_i(\tau))$ is **monotone non-decreasing**, spanning from $m_i(5)$ at $\tau=0$ up the band ladder. It is therefore a legitimate *monotone sensitivity family with an interpretable index*, provided it is labelled as a truncation of the density and never as the household's ability set. **Not adopted as baseline** (amendment §G).

---

## 10. Nonworkers, empty sets, and couples (ruling §E; amendment §H)

### 10.1 The domain extension for observed nonworkers, named explicitly

The theory paper's notation convention is that when $W(z,R,A;\mathbf y)$ is measured, $z=(c,j)$ for some $j\in A$ (SRC-1 §(a), primitives, `jobs_and_wellbeing.tex:109–114`). Under a market-only reference set, an observed nonworker has $j^{\rm obs}=o\notin A^M$, so that convention fails.

**Named extension: off-set evaluation.** Extend $W^1$ to $Z\times\mathcal R\times2^{\mathcal J}$ with the requirement $j^{\rm obs}\in A$ dropped, retaining $A\neq\emptyset$. The object is well defined: $m_i(j)$ exists and is unique for every $j$ by continuity and strict monotonicity in consumption (§3.1), so $\min_{j\in A}m_i(j)$ is well defined whether or not $j^{\rm obs}\in A$.

What the extension does **not** carry: `thm:w1` characterises $W^1$ on the original domain. Extending the evaluation domain does not extend the characterisation, and this memo makes **no change to the theory paper**. Off-set evaluation is an empirical convention and requires Deputy/PI approval before it is used in any reported object. Do not silently discard nonworkers, do not condition the analysis on employment, and do not reinsert $o$ into the reference to avoid the issue (that is Mapping F, a different object).

### 10.2 Market-reference bounds that actually hold

Mapping F's tests are **not** carried over. Derived fresh, using only $L_i(o)>L_i(h)$ for all $h\ge5$ and $L_i$ strictly decreasing:

| Case | Bound | Attainment |
|---|---|---|
| Worker, $j^{\rm obs}\in A^M$ | $m_i(5)\ \le\ W^{1,M}_i\ \le\ C^{\rm obs}_i$ | upper bound with equality iff $h_{\min}(A)=h^{\rm obs}$; note **weak**, not strict as in F |
| Nonworker (off-set) | $C^{\rm obs}_i\ <\ m_i(5)\ \le\ W^{1,M}_i\ \le\ m_i(70)$ | strictly **above** $C^{\rm obs}$, never equal |
| All households | $W^{1,F}_i\ \le\ m_i(5)\ \le\ W^{1,M}_i$ | $W^{1,F}$ is the verified Mapping-F value |

Two consequences to state before anyone tabulates anything:

- F's nonworker test $W=C^{\rm obs}$ becomes a strict inequality **in the opposite direction**: a market-only reference values a nonworker's bundle *above* their observed consumption, because replicating their leisure at any market job requires compensation.
- Hence the market-only reading moves nonworkers **up** relative to workers, reversing the direction Mapping F imposes. Any inequality comparison between the two mappings is dominated by this, not by opportunity.

Both bounds are computable today from already-verified quantities ($C^{\rm obs}$, $L_i(j^{\rm obs})$, $\beta_c$, plus $L_i(5)$ and $L_i(70)$, which are the same closed form evaluated at two additional hours points).

### 10.3 The empty market set

$\Pr(A^M_i=\emptyset)=0$ under the accepted law (§4.2). It is strictly positive, $e^{-\Lambda_i}$, only under the finite benchmark of §5.3, where it must be handled.

**Proposed treatment (one, explicit, requiring approval).** On $\{A^M_i=\emptyset\}$, set

$$W^{1,M}_i=\sup_{j\in\mathcal J^{M}}m_i(j)=m_i(h_{\max}),\qquad h_{\max}=70 .$$

Rationale: $W^1$ is anti-monotone in the set (§3.2), so shrinking the market set raises the value, and the supremum over the market job space is the monotone-consistent limit as the set empties. The convention is finite, assigns neither zero nor infinity, discards no household, conditions on nothing, and does not reinsert $o$ into the reference. It repairs the $+\infty$ that the empty event otherwise produces (and that the latent-set note's Reading II carries at $\kappa\to0$).

**Normative and population consequences, stated:** a household with no market opportunity receives the **highest** market-reference value. That is the correct direction under anti-monotonicity, and it will look wrong in a table unless labelled. It also inherits $h_{\max}=70=$`DEFAULT_H_MAX`, a second numerical convention. The alternative — conditioning on nonemptiness — changes the population and is rejected here; $\Pr(A^M=\emptyset)$ should instead be reported by group alongside any such family. **This is a new convention and requires Deputy/PI approval.**

### 10.4 Couples

**Individual sets versus household combinations.** The package space is pairs $(j_m,j_f)$. Three candidate reference domains, nested by §3.4's additive separability:

$$\underbrace{W^{1,F}}_{\text{both at }o}\ \le\ \underbrace{W^{1}_{\ge1\,\rm market}}_{\text{one spouse at }o}\ \le\ \underbrace{W^{1}_{\rm both\,market}}_{\text{neither at }o}\ \le\ C^{\rm obs}\ \text{(two-worker households)} .$$

Allowing $o$ for **either** spouse puts that spouse at home in the minimising combination (home maximises $L$), so allowing it for both collapses the object back to Mapping F exactly. This is why the market-only restriction has to be stated at the level of combinations, not spouses: *"market-only" must not silently require both partners to work*, but admitting one-partner-at-home combinations is a substantive normative choice that moves the number, not a technicality. Measure-map finding **F6** records the record's market minimum for couple 1485200 at $(0,5)$ — the woman at 5 hours, the man at home — i.e. the $\ge1$-market reading.

**Joint availability.** The estimated intensity factorises across spouses: $\log g(j_m,j_f)$ is a sum of per-spouse hours/wage/occupation/market terms, so $g(j_m,j_f)=g_m(j_m)g_f(j_f)$ (code-level fact, SRC-1 §(b)). **This does not make the realised set a Cartesian product.** A Poisson process on the space of pairs with product intensity realises *pairs*, scattered independently; the set of realised pairs is not $A_m\times A_f$ for any marginal sets. A Cartesian-product reference is therefore an **additional assumption** about what combinations the household can reach, and it is signed: by §3.4 it under-states $W^{1,M}$ relative to any non-product subset. State it or avoid it; do not assume it silently. (Under the dense law of §4 the distinction evaporates, because every combination in the support is available.)

**$\beta_{\ell\ell}=0$: what it buys and what it does not.** It buys additive separability of the welfare minimand, hence the separation of the household minimum into two per-spouse minima *given a product reference set*, and hence the validity of the nesting above (latent-set note §1.2 notes the same load-bearing role for the argmax). It buys nothing about the set law, nothing about spouse dependence, and nothing about which combinations belong in the reference. It is also a **code-level constant given the certified spec**, not a parameter pinned by a bound (addendum A2): `couples_interaction_coef` is absent from the spec, so `beta_ll = P(interaction_name) if interaction_name else 0.0` evaluates the literal `0.0`.

### 10.5 The large-count limit and the 5-hour reference (amendment §H)

The three conditions, checked:

| Condition | Status |
|---|---|
| (1) every household has positive opportunity intensity arbitrarily close to the common market-hours floor | **HOLDS — by functional form, not by data.** On $[5,7.5]$ all band indicators are zero, so the structural hours index is $\beta_E\cdot\mathbb 1\{\text{working}\}$, and $\exp(\beta_E)>0$ for any finite estimate, for all four groups, independent of fitted values (SRC-2 §4). Per-household verification against microdata was explicitly not performed (SRC-1 §(h), SRC-2 open items). |
| (2) the relevant support is genuinely common | **HOLDS — by construction.** The support is the proposal's $[5,70]\times[2,590]\times\{1..4\}$, identical for every household. |
| (3) the required independence / point-process conditions | **MAINTAINED, NOT ESTABLISHED.** Poisson independence across job regions and across spouses is assumed, tested nowhere. |

So the common 5-hour reference **is** implied in the large-count limit — but conditions (1) and (2) hold because the hours support was imposed as a numerical convention (`DEFAULT_H_MIN`/`DEFAULT_H_MAX`, overridable per call, asserted nowhere as a data feature), and condition (3) is an assumption. Per addendum A3 the claim must therefore be stated as: **a common 5-hour reference is an artefact of the proposal support, not an economic finding about the French labour market.** It must not be presented as the latter.

---

## 11. What is learned, and how inequality could be evaluated (ruling §F)

### 11.1 Three distinct uncertainties, not to be merged

1. **Latent realised-set uncertainty** — which set this household actually faced, given the data. Governed by the posterior of §6.
2. **Ex-ante opportunity risk** — the prior spread of sets an observationally identical household might face. A different question, answered by $P_i(dA\mid X_i)$.
3. **Parameter-estimation uncertainty** — the S11/CR1 sampling distribution of $\hat\theta$. Orthogonal to both.

An expectation over any of them is a **summary and aggregation choice**. It is not an axiomatic theorem about lotteries, and the theory paper contains no result licensing $\mathbb E[W^1]$ as a welfare measure.

### 11.2 Retaining the full conditional law, and the three inequality objects

Retain $P(W^{1,M}_i\in\cdot\mid j^{\rm obs}_i,X_i)$ per household rather than collapsing it; every object below is then a functional of the collection $\{P_i\}$.

- **Inequality of household conditional means**: $I\big(\{\mathbb E[W_i\mid\text{data}_i]\}_i\big)$. Needs no cross-household coupling.
- **Expected inequality across joint realisations**: $\mathbb E\big[I(\{W_i\}_i)\big]$. **Requires the joint law across households** — a coupling assumption. Cross-household independence given covariates is the natural default, and it is substantive: regional or aggregate opportunity shocks would violate it, and the region/year shifters in $g$ are precisely covariates suggesting common components. Any future coalition counterfactual needs the same coupling, plus a stated rule for whether the realised $\varepsilon$-field is held fixed or redrawn (latent-set note §4.2, item 2).
- **Marginal mixture**: the distribution obtained by mixing each household's conditional law. For the variance the relation is exact,
 $\operatorname{Var}_{\rm marg}=\operatorname{Var}\big(\mathbb E[W_i\mid\cdot]\big)+\mathbb E\big[\operatorname{Var}(W_i\mid\cdot)\big]\ \ge\ \operatorname{Var}_{\rm cond}$,
 so the mixture always registers more dispersion than conditional means. For the Gini and Theil no such identity holds; the ordering must be computed, not asserted.

Under the accepted set law all three coincide, because the conditional law is degenerate (§4.3). Under the deterministic $\tau$-family of §9 they also coincide. They separate only inside a stochastic finite family — which is another way of seeing that the stochastic content and the model-compatibility problem are the same problem.

### 11.3 Weighting and equivalisation kept separate

All objects above are household EUR/month, unequivalised, with `dwt` weights — the frozen E2 convention (BASELINE-F1 authorisation §3; measure-map acceptance F9). Equivalisation is a separately documented post-transformation, and is being handled by E3-EQ. One useful invariance: dividing both $W^{1,M}_i$ and $C^{\rm obs}_i$ by a common scale $e_i$ leaves the **ratio** $W^{1,M}_i/C^{\rm obs}_i$ unchanged, so the bound family of §10.2 expressed in ratio form is equivalisation-invariant. Person- versus household-weighting is a third, independent choice and is not made here.

---

## 12. One recommendation (ruling §G)

**Do not take a stochastic market-only Measure 1 forward as the paper's opportunity object.** Take forward the **deterministic market-reference bracket**, in class C, explicitly labelled, with Mapping F remaining the primary verified benchmark until the Deputy/PI decides otherwise.

### 12.1 The construction

Report, per household, from closed form:

| Object | Definition | Status |
|---|---|---|
| $W^{1,F}_i$ | $C^{\rm obs}_i\exp\{[L_i(j^{\rm obs})-L_i(o)]/\beta_c\}$ | verified baseline, unchanged |
| $W^{1,M}_i$ | $C^{\rm obs}_i\exp\{[L_i(j^{\rm obs})-L_i(5)]/\beta_c\}$ | **the literal market-only Measure 1 under the accepted model** (§4.3); label: opportunity-free, floor-convention-dependent |
| upper bracket | $C^{\rm obs}_i$ (workers) / $m_i(70)$ (nonworkers, off-set) | §10.2 |
| $\tau$-ladder | $W^{1,M}_i$ evaluated at $h_{\min}\in\{5,17.5,28.5,33.5,36.5,44.5\}$ | §9; a **labelled monotone sensitivity family**, not an ability set |

Not a mean over sets, not a log-sum-exp, not the retired W1-EA integral. The minimum representation is preserved literally throughout.

### 12.2 Exact estimand

For each household $i$ in the accepted singles and couples estimation samples, at the observed attained bundle, in household EUR per month, unequivalised, with `dwt` weights, singles and couples reported separately and never pooled:

$$W^{1,M}_i=C^{\rm obs}_i\exp\!\Big[\frac{L_i(j^{\rm obs}_i)-L_i(h_{\min})}{\beta_c}\Big],\qquad h_{\min}=5\ \text{(declared convention)},$$

together with the bracket of §10.2 and the $\tau$-ladder. $C^{\rm obs}$ is the frozen E2 object: raw household EUROMOD-priced disposable consumption after the stored take-up rule, used as the engine's `c_norm`.

### 12.3 Identified versus additional primitives

- **Identified / already verified and sufficient for the recommendation:** $\beta_c$, the leisure block $(\beta_{\ell0},\beta_{\ell a},\beta_{\ell a^2},\beta_{\ell k},\theta_\ell)$, $C^{\rm obs}_i$, $h^{\rm obs}_i$. All are inputs to the already-verified BASELINE-F1 path.
- **Declared conventions, not primitives:** $h_{\min}=5$, $h_{\max}=70$, off-set evaluation for nonworkers, the couples reference domain, $\tau$ (or the retained-mass level).
- **Additional primitives required for a genuinely set-sensitive object, and not available:** a finite offer count/intensity $\Lambda_i$ (§7 row 6) and the joint dependence structure (rows 8–9). These cannot be calibrated from the accepted estimates and cannot be introduced without changing the choice law.

### 12.4 Coverage

Nonworkers: covered, under the named off-set extension, with the reversed bound (§10.2) reported explicitly. Couples: covered, with the reference domain declared among the three nested options of §10.4 and the one-partner-at-home option not silently excluded. Empty sets: probability zero under the accepted law; the §10.3 convention applies only if a finite family is ever authorised.

### 12.5 Implications for the existing estimates

**None to the estimates.** Nothing here re-estimates, re-prices, or revises S11. Every recommended object is a post-estimation closed-form transform of quantities already verified in `baseline_f1_verification_v1.md`.

The implications are to the **interpretation** of the empirical programme, and they are substantial:

1. The paper's main question — how much well-being inequality is attributable to unequal job opportunities — **cannot be answered through the reference set of Measure 1 on this empirical domain**, under either reading. Reading I (home in the reference) makes $A$ drop out because home dominates; Reading II (market-only) makes $A$ drop out because the realised set is the common support. The two mechanisms are different; the conclusion is the same.
2. Whatever opportunity content the JMP reports must therefore travel through **attainment** — through how the opportunity structure moves $j^{\rm obs}$ and $C^{\rm obs}$ under a counterfactual — not through the welfare reference. This is consistent with the standing learning that measures independent of the ability set cannot register opportunity inequality; the new content is that Measure 1, which is *not* independent of $A$ as an axiom, becomes **effectively** independent of it on this domain.
3. The anti-monotonicity of §3.2 must be stated in the paper whatever is decided, because it reverses the naive sign.

### 12.6 Numerical requirements

Closed form. No simulation, no quadrature, no draws, no posterior sampling, no new pricing. The computation is the verified BASELINE-F1 path with $L_i(o)$ replaced by $L_i(5)$ (and $L_i(70)$ for the nonworker upper bracket), i.e. the same `leisure_utility` evaluation at two additional hours points. Same restricted-environment discipline: household-level values stay outside Git, aggregates only in repository artifacts. The same pre-registered checks apply with the **bounds of §10.2 substituted for F's C1/C2** — in particular, C1 ($W=C^{\rm obs}$ for nonworkers) must be **replaced**, not reused, since it is false for this object.

### 12.7 The single Deputy/PI decision requested

> **Does the programme accept verdict D — that a set-sensitive market-only Measure 1 is not obtainable from the accepted positive model — and proceed with (i) Mapping F primary plus the §12.1 bracket as a labelled robustness annex; or does it instead authorise (ii) a scoped positive-model extension mission (finite-offer latent-set specification with re-estimation, or external offer/vacancy information to pin $\Lambda$) to obtain a literal set-sensitive Measure 1?**

Nothing else in this memo requires a decision. If (i), the next step is a bounded reporting card. If (ii), the next step is a feasibility charter, not an execution card, and the seminar timetable should not depend on it.

---

## 13. Evidence-status table (ruling, Outputs and restrictions)

| # | Statement | Status | Source |
|---|---|---|---|
| 1 | Measure 1 is $z\,I\max_R B$ with $B$ pricing every job in $A$ at a common $w$; the notation convention requires $j^{\rm obs}\in A$ | **PRIMARY SOURCE** | `jobs_and_wellbeing.tex:109–114, 256–269` via SRC-1 §(a) |
| 2 | `thm:w1`: Responsibility For Equal Pay + Independence of $\mathbf y$ $\Rightarrow W=W^1$ | **PRIMARY SOURCE** | `jobs_and_wellbeing.tex:544–553`; agent reference |
| 3 | Dagsvik–Jia Assumption 2 is an inhomogeneous Poisson offer process with taste intensity $\theta\varepsilon^{-2}$ (additively, $\theta e^{-\varepsilon}$, footnote 2); the intensity form is necessary for IIA; $\theta$ is a relative availability measure that also absorbs psychological costs of working and is not a vacancy count | **PRIMARY SOURCE** | Dagsvik–Jia (2016) Assumption 2 and discussion; Theorem 1 eq. (2a,b); pinned hashes |
| 4 | Dagsvik–Jia Theorem 3: offered-hours distribution identified, $\delta(h)$ not identified | **PRIMARY SOURCE** | Dagsvik–Jia (2016) Thm 3 |
| 5 | $V=u+\log_h+\log_w+\log_{\rm market}-\log_{\rm prior}=u+\log g-\log q$; per-household LL is the softmax $V_{\rm obs}-\mathrm{lse}$ | **INSPECTED CODE** | `engine_jax.py` module docstring 20–25, `index`/`neg_ll` 292–352; SRC-2 §2 |
| 6 | $u$ contains leisure (Box–Cox, age/age²/children shifters) and consumption only; no wage/occupation/sector/region term in any located spec | **INSPECTED CODE** | SRC-1 §(b),(f),(g); SRC-2 §1; measure-map §2.1; `baseline_f1_verification_v1.md` dependency audit |
| 7 | $\theta_c=0$ exactly both groups; $\beta_c$ estimated 2.0387 / 2.1017 | **INSPECTED CODE + CERTIFIED REPORT** | SRC-2 §1 |
| 8 | `beta_ll` absent from the certified coordinate list; code path evaluates hardcoded `0.0` | **INSPECTED CODE** | SRC-1 §(b); addendum A2 |
| 9 | `DEFAULT_H_MIN=5.0`, `DEFAULT_H_MAX=70.0` are module-level proposal defaults, overridable per call, asserted nowhere as data features | **INSPECTED CODE** | `continuous.py:38–41`, 370–371, 887; SRC-1 §(d),(h); addendum A3 |
| 10 | Structural hours index on $[5,7.5]$ is $\beta_E\cdot\mathbb 1\{\rm working\}$; positive mass near the floor for all four groups by functional form, independent of fitted values | **INSPECTED CODE, ANALYTICAL** | SRC-2 §4 |
| 11 | $\kappa_i$ cancels from the likelihood; `_center_proposal` applies such a substitution and leaves the LL invariant | **INSPECTED CODE + PRIOR DERIVATION** | latent-set note §2.2, Finding 2 |
| 12 | $\beta_\ell(\mathbf x_i)>0$ over the whole admissible covariate domain (all four blocks); $\arg\max_jL_i(j)=o$ passes on the whole S12 panel | **PRIOR DERIVATION + RECORD** | latent-set note Finding 1b and the S12 premise audit |
| 13 | Market minimum for couple 1485200 at $(0,5)$; market Measure 6 / W1-F between 1.009 and 1.014 across checks | **ACCEPTED RECORD** | measure-map acceptance F6 |
| 14 | $W^1(A)=\min_{j\in A}m_i(j)$, existence/uniqueness/positivity; $m$ increasing in $h$; anti-monotonicity in $A$ | **OWN DERIVATION** | §3.1–3.2 |
| 15 | The marked process $\kappa_i\lambda_i(dj)\times e^{-\varepsilon}d\varepsilon$ reproduces the executed criterion exactly and has infinite total intensity; its job-space projection is a.s. dense on $\operatorname{supp}g_i$ | **OWN DERIVATION** (on a primary-source assumption) | §4.1–4.2 |
| 16 | $W^{1,M}_i=m_i(5)$ a.s., invariant to all 29 opportunity parameters and to $\kappa_i$; $W^{1,M}/W^{1,F}=\exp\{[L_i(o)-L_i(5)]/\beta_c\}$ | **OWN DERIVATION**, corroborated by row 13 | §4.3 |
| 17 | A finite random-set law is not a weighted softmax (exact 3-alternative counter-example); the informative-$\Lambda$ region is the misspecified region | **OWN DERIVATION + TOY CHECK** | §5.4, Toy 2 |
| 18 | Posterior tilt $\propto\sigma(u^{\rm obs}-u(j))$; $P(h_{\min}\mid j^{\rm obs},X)$ depends on wages at equal $m$ | **OWN DERIVATION + TOY CHECK** | §6.3, Toy 4 |
| 19 | Under the accepted law the posterior set is also a.s. dense, so $P(h_{\min}\mid\cdot)=\delta_{\{5\}}$ | **OWN DERIVATION** | §6.2 |
| 20 | $\tau$-family: $h_{\min}$ is a step function jumping $5\to17.5$ at the residual level; at most six values | **OWN DERIVATION** (on row 10's band structure) | §9 |
| 21 | Couples nesting $W^{1,F}\le W^1_{\ge1{\rm mkt}}\le W^1_{\rm both\,mkt}$; product-set reference is an added, signed assumption | **OWN DERIVATION** | §10.4 |
| 22 | Poisson independence across job regions and across spouses | **MAINTAINED ASSUMPTION**, untested | §7 rows 8–9 |
| 23 | $\tau=1$ taste-shock scale; $\delta(h)\equiv1$; $g_i(o)\equiv1$ | **MAINTAINED NORMALISATIONS** | §7 rows 5, 7, 10 |
| 24 | Behavioural shocks excluded from the welfare ordering, retained in the conditioning | **MAINTAINED RULE** (Deputy) | §6.1 |
| 25 | Off-set evaluation for nonworkers; empty-set $\sup$ convention; couples reference domain | **UNRESOLVED — requires Deputy/PI approval** | §10.1, §10.3, §10.4 |
| 26 | Per-household positive opportunity mass near the floor, verified against microdata | **UNRESOLVED** — analytical only; never checked per household | SRC-1 §(h), SRC-2 open items |
| 27 | The pooled-spec covariate split quoted in SRC-1 §(f)/(g) versus the S11 specs of record | **UNRESOLVED (A6)** — see §14 | addendum A6; SRC-2 §1 |
| 28 | POSFIT v2b "real choices more predictable than self-simulated choices" | **SUGGESTIVE DIAGNOSTIC ONLY**, with the A7 flooring caveat; verdicts open | §8.4 |

---

## 14. Open items, dependence checks, escalations

**A6 — dependence on which spec is authoritative.** The addendum flags that SRC-1's covariate split was quoted from the pooled certified spec, whose `beta_c=1.0` fixed and estimated `theta_c_singles` contradict the verified S11 anchors. SRC-2 resolves the provenance: S11 ran off `estimation_spec_S8_corrected_floor5_v1.yaml` (singles) and `estimation_spec_couples_clean_r240_v1.yaml` (couples), with `beta_c` un-fixed in code by `build_target()` and, for couples, `theta_l_m` freely estimated. SRC-2 also records that both descendants inherit the `hours_opportunity` / `wage_opportunity` / `market_opportunity` / `occupation_opportunity` blocks **unchanged**, so the covariate split of A1 is unaffected by the provenance correction.

Dependence check, as required:

- **No conceptual conclusion in this memo depends on the numerical value of $\beta_c$.** §§2–11 use only $\beta_c>0$. The degeneracy theorem, the identification classification, the posterior result, the bounds and the couples nesting are all invariant to it.
- **Two arithmetic illustrations do use S11 numerals**: the ratio band in §4.3 (Toy 5) and the order-of-magnitude in §5.3 (Toy 3). Both are labelled illustrative. If the spec of record changes, those two numbers change and nothing else does.
- No conclusion depends on whether `theta_l_m` is pinned or free, only on $\mathcal B(\cdot;\theta)$ being increasing, which holds for every $\theta$.

**Escalations (targeted, not blocking this memo).**

1. **E-1.** Confirm whether `JMP_W1_stochastic_ability_set_bridge_v*.md` already exists in the repository. If so, this document must be re-issued as the next version and the existing one preserved.
2. **E-2.** The three conventions in evidence row 25 need Deputy/PI approval before any reported object uses them.
3. **E-3.** If a finite family is ever authorised, the per-household check that $g_i$ has positive mass in a neighbourhood of the floor (row 26) must be run in the restricted environment; the analytical argument is sufficient for the degeneracy theorem but not for a household-level family.

**Not escalated because not indispensable:** the S12 node manifest (does not exist as a named file, SRC-1 §(e)); the R5 draft and P/A/B/D operators (nothing here changes them); the equivalence-scale note (§11.3 gives the invariance that makes the bracket scale-free in ratio form).

---

## Appendix A — deterministic toy checks

Small analytic checks only, as permitted. No microdata, no simulation of the empirical model, no calibration. Reproducible from the numbers printed here.

**Toy 1 — PI example.** $i$: $A=\{1,2\}$, $m=(100,120,40)\Rightarrow W=100$. $k$: $A=\{2,3\}$, $m=(50,70,60)\Rightarrow W=60$. Ruling §D expectation: $40p+100(1-p)=100-60p$; at $p=0.25$, $85$.

**Toy 2 — a finite random set is not a weighted softmax.** Home always present; two market jobs present independently with $\pi=(0.55,0.30)$; $u=(0,0.5,2.0)$; iid Gumbel.

| alternative | $\mathbb E_A[\text{softmax}_A]$ | weighted softmax $e^{u_j}\pi_j/\sum_ke^{u_k}\pi_k$ | difference |
|---|---:|---:|---:|
| home | 0.492883 | 0.242512 | $+0.250372$ |
| job 1 | 0.266748 | 0.219909 | $+0.046840$ |
| job 2 | 0.240368 | 0.537580 | $-0.297211$ |

**Toy 3 — speed of degeneracy (illustrative arithmetic, NOT a calibration).** $\mathbb E[h_{\min}]-5\approx1/(\Lambda c)$ with $c=1/109.6096$ per hour (residual-band normalised density implied by the hours integral in the latent-set note §2.3):

| $\Lambda$ | 1 | 2 | 5 | 10 | 20 | 50 | 200 | 1000 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| $\mathbb E[h_{\min}]$ (h, capped at 70) | 70 | 59.8 | 26.9 | 16.0 | 10.5 | 7.2 | 5.5 | 5.1 |

**Toy 4 — the posterior tilt depends on the unchosen job's wage, not on $m$.** Illustrative household, $\beta_c=2.0387$, an illustrative leisure block ($\beta_\ell=6$, $\theta_\ell=-1$), observed $(C,h)=(1500,38)$. A 10-hour job has $m=1133.35$ **whatever it pays**. Posterior tilt $\sigma(u^{\rm obs}-u_j)$: low-paid version ($C_j=600$) $\to0.7853$; well-paid version ($C_j=1400$) $\to0.3939$.

**Toy 5 — $W^{1,M}/W^{1,F}$ at the covariate-domain minimum of $\beta_\ell$.** Numerals transcribed from the latent-set note §1.2 table ($\theta_\ell$ and $\min_a\beta_\ell$) and the verified $\beta_c$; normalised leisure $8$ at home, $7.5$ at $h=5$.

| block | $\theta_\ell$ | $\min\beta_\ell$ | $L(o)-L(5)$ | ratio |
|---|---:|---:|---:|---:|
| singles male | $-1.6263$ | 7.81447 | 0.018072 | **1.0089** |
| singles female | $-0.9274$ | 5.86714 | 0.056726 | **1.0282** |
| couple, woman at 5h / man at home | $-1.6863$ | 12.58681 | 0.025745 | **1.0123** |
| couple, both at 5h | — | — | 0.060565 | **1.0292** |

Ratios are increasing in $\beta_\ell$, so these are the low ends. Compare measure-map F6: 1.009–1.014 across the check households.

---

## 15. Output discipline

| Field | Content |
|---|---|
| **Mission ID** | JMP-W1-MARKET-SET-BRIDGE-1 |
| **Authoritative inputs** | Listed in §0, items 1–10. Controlling: `JMP_BRIDGE1_amendment_v1.md` over `JMP_market_set_bridge_and_parallel_work_ruling_v1.md` where they differ. |
| **Decisions made** | (1) Verdict **D**, with a class-C fallback recommended. (2) The $h_{\min}$ reduction is **verified**, scoped to conditional welfare given a realised set. (3) The posterior law of $h_{\min}$ is **proved not** to reduce to the marginal hours law under any finite family, and is **proved degenerate** under the accepted law. (4) No one-parameter $\Lambda$ family is recommended as a model object; it is derived only as a conditional consequence of an added hypothesis. (5) Threshold/effective sets are classed as a labelled monotone sensitivity family, not adopted as baseline. (6) Market-reference bounds derived fresh; F's C1/C2 tests **not** carried over. (7) Recommended construction: the deterministic market-reference bracket, Mapping F remaining primary. |
| **Unresolved decisions** | Off-set evaluation for observed nonworkers; the empty-set $\sup$ convention; the couples reference domain among the three nested options; whether to authorise a positive-model extension (the §12.7 decision). Plus evidence rows 25–27. |
| **Exact output filename** | `JMP_W1_stochastic_ability_set_bridge_v1.md` (re-issue as v2 if a v1 exists in the repository — escalation E-1) |
| **Next authorised action** | Independent conceptual review in a fresh Claude Project Fable 5.1 chat, high effort, thinking ON, per the ruling's review prompt, attaching this memo plus the inputs of §0. Output: `JMP_W1_stochastic_ability_set_bridge_review_v1.md`. Then return both to Goal 1 and on to the Deputy with the §12.7 decision. **No execution, no prototype, no calibration is authorised by this memo.** |
