# JMP_W1_stochastic_ability_set_bridge_review_v1.md — independent conceptual review of the market-only random-set Measure 1 memo

| Field | Value |
|---|---|
| Mission | JMP-W1-MARKET-SET-BRIDGE-1 — independent conceptual review (ruling, "One independent conceptual review"; Goal 1 addendum R1–R10) |
| Reviewed document | `JMP_W1_stochastic_ability_set_bridge_v1.md`, dated 2026-09-12 |
| Date | 2026-09-12 (reissued the same day after the full input set was supplied; supersedes the first issue, which carried four "not supplied" flags) |
| Model used | Claude Fable 5.1, Claude Project chat, thinking on |
| Status | REVIEW. No execution, no calibration, no re-estimation, no literature search. Arithmetic limited to reproducing the memo's Appendix A toys. |
| Output file | `JMP_W1_stochastic_ability_set_bridge_review_v1.md` |

## 0. Authoritative inputs actually used

1. `JMP_market_set_bridge_and_parallel_work_ruling_v1.md` §A–G and review prompt; `JMP_BRIDGE1_amendment_v1.md` §A–I (controlling).
2. `Jobs_and_wellbeing.tex` (primitives 107–114, axioms 122–254, Measure 1 258–267, Results standing assumptions 358–375, `thm:imp1`, `thm:w1` 548–596); `jobs_and_wellbeing_agent.md` (standing assumptions, theorem inventory); `jobs_and_wellbeing.md` (older copy; Measure 1 text verbatim identical per SRC-1 §(a), used for nothing else).
3. Dagsvik and Jia (2016) markdown: Assumption 2 and footnote 2, Theorem 1 (2a,b), Theorems 2–3 and proofs, Assumption 7, Theorem 5.
4. `W1_latent_set_identification_note_v1.md` §0–§7.
5. `JMP_W1_reference_domain_fork_v1.md` §3.1–3.4, §4.2, Table 1; `JMP_W1_fork_ruling_v1.md` §1–§3 and Appendix A (Deputy R1–R6, verbatim).
6. `JMP_bridge_source_extract_v1.md` (SRC-1) §(a)–(h); `JMP_bridge_source_extract_v2.md` (SRC-2) §1–§4.
7. `JMP_W1_BASELINE_F1_authorization_and_Cobs_ruling_v1.md`; `JMP_measure_map_acceptance_v1.md` F1–F10, §2.1; `baseline_f1_verification_v1.md`.
8. `JMP_positive_fit_diagnostics_memo_v2b_addendum.md` — status line only.

Every input the ruling lists for the review is now in hand. No claim below rests on an unsupplied document.

---

## 1. Verdict

**The memo's principal verdict D is upheld as stated, under the maintained rule that behavioural taste shocks are excluded from the welfare ordering.** The deterministic reduction, the marked-process representation of the accepted likelihood, the degeneracy theorem, the identification classification, the conditioning results and the market-reference bounds are correct. The demonstrated incompatibility — that the region of any finite-count parameter where the market-set welfare object is informative is the region where the positive model departs from the accepted one — is a valid scientific finding.

Three things are corrected or added, in decreasing order of weight.

1. **The Goal 1 conjecture R5 is incorrect, and its correction changes the framing of the decision, not the verdict.** Admitting the taste shock into the welfare ordering does not collapse market-only Measure 1 to observed consumption. It yields a finite, non-degenerate, set-sensitive random object bounded above by $C^{\rm obs}$, whose conditional law depends on the unidentified common scale $\kappa_i$. The dichotomy is therefore "floor (shocks excluded) versus a class-B object needing a declared $\kappa$ family (shocks admitted)", not "floor versus $C^{\rm obs}$". Verdict D stands because the exclusion rule is in force (Deputy R5, Appendix A of the fork ruling; BASELINE-F1 authorization §2); the §12.7 decision should be reframed so the rule, not the positive model alone, is seen to close the set-sensitive route (§3, R5).
2. **The memo's headline findings restate results already on the record without citing them.** Deputy R1 (fork ruling, Appendix A) already states that at the dense-law endpoint M "has no household-specific direct access content and becomes the whole-market/universal-market reference object" and that finite-κ M "requires an additional unidentified intensity/set-size object"; the fork memo derives the closed form (M.4), the infinite-mass argument (§3.1), amendments N1–N2, and the M/F gap band (Table 1); the fork's central result was accepted by the Deputy subject to record items, and REC-1 is citation-closed (measure-map acceptance §0). F-BRIDGE-1 is the rigorous derivation of R1's statement; F-BRIDGE-3 is fork N2. This is a provenance gap, not a scientific error, but the memo lists neither the fork nor its ruling among its inputs although the ruling requires both (§3, R6 and R10).
3. **Two domain facts the memo treats as "by construction" need a declaration**: the theory's standing assumption that $\mathcal J$ is finite (the memo's dense infinite set is outside the characterised domain of `thm:w1`), and the household-specific gaps in the executed choice sets — the `choice_domain` mask, and the verification's finding that a finite neither-work atom "is not available in every accepted choice set" — which the likelihood cannot distinguish from unavailability (§3, R3 and R10).

**Classification (review prompt).**

| Object | Class |
|---|---|
| Literal set-sensitive market-only Measure 1 from the accepted model, shocks excluded from $R$ | **Needs a positive-model change** (D confirmed). |
| Same object with the match-value coordinate admitted into $R$ | **Needs one stated design decision** (a normative ruling amending Deputy R5's requirement that ε stay out of the welfare ranking) **plus a declared sensitivity primitive** ($\kappa_i$): class B, not D. Not recommended here; recorded so the decision is posed correctly. |
| The memo's recommended class-C bracket ($W^{1,F}$, $W^{1,M}=m_i(5)$, upper bracket, floor ladder) | **Ready for a bounded prototype once one stated decision is taken** (§12.7 branch (i) together with the conventions of evidence row 25), with the labelling corrections in §4. Its inputs are exactly the verified BASELINE-F1 path plus two additional hours points; the verification's dependency audit confirms nothing else can reach it. |

---

## 2. Review against the ruling's checklist

| Item | Finding |
|---|---|
| Deterministic reduction (§3) | Correct. Existence, uniqueness, positivity (verification: consumption-guard count zero in both samples), minimum representation, inf/sup reading, $h_{\min}$ reduction (Finding 1b reused correctly), anti-monotonicity, PI example (Toy 1 reproduced). One unnamed domain extension: the theory's finiteness of $\mathcal J$ (R10-1). |
| Distribution / void-probability formulas (§5) | Correct for the iid-$n$ and finite-Poisson benchmarks. Minor: the first display in §5.3 is the unconditional survival (the empty event counts as $W>w$), not a statement "on $\{A\neq\emptyset\}$"; the conditional formula that follows is right. Toy 3 reproduces, but the exponential-rate approximation is valid only when $1/(\Lambda c)\ll12.5$ h; the rows $\Lambda\le10$ lie outside its validity. |
| Conditioning on the observed choice (§6) | Correct. Follows note §4.1 and fork §3.4(b). The posterior tilt in §6.3 is proved for one extra offer; the general finite case has tilt $e^{u_y}/(e^{u_y}+\sum_{k\in A\setminus y}e^{u_k})$, decreasing in every $u_k$, so F-BRIDGE-4 holds generally. |
| Exact compatibility with the accepted likelihood (§4, §5.4) | Correct. The marked process reproduces the criterion exactly; finite laws do not (Toy 2 reproduced; fork §3.1 gives the same by Mecke/Jensen). Clarify in §4.1 that $\kappa_i$ multiplies the home atom too — the only reading under which it cancels (note §2.2). Soften "unique": the deterministic full-support reading is equally exact and gives the same welfare value (§5.3). |
| Identification of scale and set dependence (§7) | Correct. Row 4's caveat (θ absorbs psychological costs of working) is in the primary text. F-BRIDGE-5 is a correct conditional statement. The "29 shared opportunity parameters" is sourced (pooled-spec partition, SRC-1 §(g)), but the memo's own enumeration double-counts $\beta_E$ and the count hinges on the F35 question (R10-5). |
| Nonworkers and empty sets (§10.1–10.3) | Correct. Off-set evaluation named; bounds re-derived; empty set has probability zero under the accepted law; the $m_i(70)$ convention correctly flagged for approval. The verification sizes the reversal: 204 single and 50 couple nonworkers (6.7% of 3,763 households) satisfy $W=C^{\rm obs}$ exactly under F and would sit strictly above it under M. |
| Couples (§10.4–10.5) | Correct. Nesting holds by additive separability; product-set reference correctly identified as added and signed; F6's $(0,5)$ minimum agrees with fork ruling R3.1 and with Toy 5 (the woman's leisure loss 0.0257 < the man's 0.0348). Condition (2) of §10.5 needs the R3 qualification. |
| Separation from W1-EA and quadrature (§7, §12.1) | Correct and complete; consistent with Deputy R2 and measure-map F1/F3. |

---

## 3. Adjudication of the Goal 1 addendum R1–R10

### R1 — Non-integrability. **CORRECT.**
Assumption 2 places the market taste shifters on $(0,\infty)$ with intensity $\theta\varepsilon^{-2}$; $\int_0^\infty\varepsilon^{-2}d\varepsilon$ diverges at $0$. Footnote 2 gives the additive equivalent $\theta e^{-\varepsilon}$; with $\varepsilon'=\log\varepsilon$, $\theta\varepsilon^{-2}d\varepsilon=\theta e^{-\varepsilon'}d\varepsilon'$, diverging at $-\infty$. The paper states, citing Dagsvik (1994), that this form is necessary for IIA; the induced utility process is Poisson with intensity $\Theta e^{-v}$, whose maximum is Gumbel and whose argmax law is the logit. Truncating the taste axis below any finite level breaks the exact logit. One precision: Dagsvik's necessity result is about the exponential *form*; non-integrability is its consequence.

### R2 — Projection. **CORRECT UNDER STATED CONDITIONS.**
Assumption 2 states the offered $(H,W)$ combinations are independent of the taste shifters and distributed according to $g_1g_2$. Independent marking of a Poisson process with infinite mean, thinned to a region $B$ with $\lambda(B)>0$, gives a Poisson count with infinite mean. Fails if (i) the mark law depends on the taste coordinate (the random-effect extension keeps the product form conditional on $\eta$, so not here); (ii) the taste intensity has finite mass (any finite-count law); (iii) $\lambda(B)=0$ — with continuous hours a single job type is null, so the projected set is dense but contains no prescribed point; the inf/sup reading handles this.

### R3 — Common support. **CORRECT UNDER STATED CONDITIONS**, and the conditions are the substantive content.
The four opportunity blocks (SRC-1 §(f), SRC-2 §2–§4, note §2.1) are exp of a linear band index gated on `working`, constant at $\exp\beta_E$ on the residual region; a log-normal density renormalised on a fixed interval, positive throughout for every finite $(\mu_i,\sigma)$; exp of household covariates times `working`; a four-category logit. Each scales intensity; none can zero a region or move an endpoint. **The parameterisation can only scale intensity and never truncate support**; the support is the base measure's, i.e. the proposal's draw support, a module-level default (SRC-1 §(d),(h)). Confirmed.

Two qualifications the memo omits:

- **The executed frames carry household-specific gaps in job space.** `index()` returns $V$ only where `choice_domain` is true and $-\infty$ elsewhere (SRC-2 §2). The note §1.1 records 155 non-positive-consumption alternatives and 60 out-of-domain home atoms in the S10 frame; measure-map F7 records 119 couples whose NN bundle is outside the positive-consumption domain; and the BASELINE-F1 verification had to *construct* a same-consumption home row because "a finite neither-work atom is not available in every accepted choice set". Under exact log consumption an alternative with $C_i(j)\le0$ has $u=-\infty$ and contributes zero to $\int e^{u}d\lambda$ whether read as *unavailable* or as *available but never chosen*; the likelihood cannot distinguish the two (the same observational equivalence as Finding 1a / fork N1). "Common support by construction" therefore requires the declaration: **availability is the base-measure support; evaluability is separate; jobs with non-positive priced consumption are in the ability set.** Under the opposite declaration $h_{\min}$ is household-specific wherever the floor job is masked. This belongs in evidence row 25 and is the positive-consumption-domain question F7 assigns to R5.
- **The wage support quoted in §4.3 and §10.5 is the structural renormalisation interval $[2,590]$; the proposal draw support is $[2,170]$** (`DEFAULT_W_MAX = 170.0`, SRC-1 §(d); SRC-2 §3). Immaterial to $W^{1,M}$, but the sampled sets inherit the draw support, and the two intervals should be reconciled in a source pass.

Per-household positive mass near the floor was not checked against microdata (SRC-1 §(h), SRC-2 open items; memo row 26). The analytical argument suffices for the degeneracy theorem given the declaration above.

### R4 — Measure 1 reads support, not intensity. **CORRECT, and the mismatch is genuine — but it is created by the correspondence chosen, not by the two frameworks as such.**
Haydar–Maniquet's $A$ is a subset of $\mathcal J$; the RURO object is an intensity measure on $\mathcal J\times\mathbb R$; the memo's correspondence projects onto $\mathcal J$ and, by the Deputy rule, drops the taste coordinate from $R$. After that projection the only heterogeneity left in "which jobs exist" is support, which is common.

Fork §4.2 already anticipates the alternative ("a cut in the match-value dimension"): take Haydar–Maniquet's job to be the pair (type, match), let the ability set be the marked set $\{(j,\varepsilon_j)\}$, and let $R$ rank $(c,(j,\varepsilon))$ by $\beta_c\log c+L_i(h_j)+\varepsilon$. Nothing in the theory forbids this: $R$ is any continuous, consumption-monotone preference over $Z=\mathbb R_+\times\mathcal J$ and job identities are abstract (agent reference, standing assumptions). Under that correspondence the projection discards nothing and Measure 1 is set-sensitive (R5). The accurate statement is: **the frameworks are indexed on different spaces only after the match coordinate is assigned to "chance" rather than to "the job", and that assignment is a maintained Deputy rule (R5, Appendix A: ε "used only for behavioural choice and … excluded from the welfare ranking"), a normative choice, not a fact about either model.** The memo's paper sentence should say so.

### R5 — Goal 1 conjecture. **INCORRECT** as stated; the first step is right, the conclusion is wrong, and the correct conclusion matters.
Let $s_j:=L_i(h_j)+\varepsilon_{ij}$ be the flat-pay index. With ε in $R$, $m_i(j)=C^{\rm obs}\exp[(s_y-s_j)/\beta_c]$, decreasing in $\varepsilon_j$ (correct). Hence
$$W^{1,M}_i=C^{\rm obs}_i\exp\!\Big[\tfrac{s_y-\sup_{j\in A^M_i}s_j}{\beta_c}\Big].$$
The minimum is attained at the job maximising the **flat-pay** index $s$. The chosen job $y$ maximises the **actual-pay** index $v_j=s_j+\beta_c\log C_i(j)$. These coincide only in special cases. For a worker $y\in A^M$, so
$$W^{1,M}_i\le C^{\rm obs}_i,\qquad\text{with equality iff } y=\arg\max_{A^M}s,$$
generically strict, because higher-paid jobs are chosen over jobs with a higher flat-pay index. So "include ε ⇒ $W^{1,M}=C^{\rm obs}$ exactly for every worker" is false.

Under the accepted marked process $\{s_j\}$ restricted to the market is Poisson on $\mathbb R$ with intensity $\Theta^L_ie^{-s}$, $\Theta^L_i=\kappa_i\int_{\rm mkt}e^{L_i}g_i\,d\nu<\infty$, so $\sup_A s$ is a.s. finite, Gumbel$(\log\Theta^L_i)$ unconditionally, and the welfare object is **non-degenerate and set-sensitive** — through the hours composition of $g_i$ (via $\int e^{L_i}g_i\,d\nu$) and through $\kappa_i$. Conditional on the observation, with remaining points restricted to $\{v_j<v\}$ (note §4.1),
$$\Pr\big(\sup_{A^M\setminus y}s\le t\,\big|\,y,M_i=v\big)=\exp\Big\{-\kappa_i\!\int_{\rm mkt}\big[e^{L_i(j)-t}-e^{L_i(j)+\beta_c\log C_i(j)-v}\big]^+\lambda_i(dj)\Big\},$$
with $v\mid y\sim$ Gumbel$(\log\Theta_i)$, $\Theta_i$ containing $\kappa_i$. So the object depends on the unidentified scale exactly as the note's Reading II and fork §3.4(b) say. For a fixed job type the infinite mass at low ε is harmless here because welfare needs the *maximum* of $s$, which is finite — the precise sense in which R4 is right.

The same holds for Mapping F: with ε in $R$, $W^{1,F}=C^{\rm obs}\exp[(s_y-\max\{s_o,\sup_{A^M}s\})/\beta_c]$, no longer $m_i(o)$ (note §1.2 caveat). The verified BASELINE-F1 value, and the authorization's own dependency prohibition on ε (§2), therefore rest on the exclusion rule.

Effect on the verdict: **D unchanged in force**; the memo's "complete dichotomy" is **weakened** — the two branches are "floor" and "class-B object with a declared κ family", not "floor" and "$C^{\rm obs}$". The §12.7 decision should carry the third branch explicitly (§5).

### R6 — Correction of record (F-BRIDGE-3). **CORRECT**, and already on the record.
Verified against the note: §3.1 posits a Poisson process on $\mathcal J$ with finite intensity ("conditional on adding one") and derives $e^{-\kappa_i\Lambda_i(x)}$; §2.3 computes $\mathbb E[N^{\rm mkt}]=9.62/20.84$ under that reading; §4.1 uses the marked process on $\mathcal J\times\mathbb R$. Different processes; under §4.1's, $\Lambda_i(x)=\infty$ wherever $\lambda_i(\{m_i\le x\})>0$. Two additions:

- The note's §1.1 sentence that iid Gumbel marks make the market part "a Gumbel with location $\log\int e^{u}d\mu_i$" is itself a §4.1-process statement: a *finite* Poisson number of iid-Gumbel-marked points has maximum c.d.f. $\exp\{-\Lambda(1-\mathbb E_f[e^{-e^{u-t}}])\}$, not Gumbel. So Finding 1a's $e^{-1}$ claim rests on the §3.1 process; under the model's own process $o\in A_i$ a.s. This is fork amendment **N1**, which the memo should carry alongside F-BRIDGE-3.
- Fork amendment **N2** is verbatim the content of F-BRIDGE-3, and the fork's central result is Deputy-accepted (Appendix A, preamble) with REC-1 citation-closed. Attribute.

### R7 — Anti-monotonicity. **CORRECT** on the mathematics; **CORRECT UNDER STATED CONDITIONS** on the normative gloss.
$A\subseteq A'\Rightarrow\min_{A'}\le\min_A$. Confirmed against the .tex: Measure 1's $B$ prices every job in $A$ at the same $w$ (259–267); the paper's commentary (line 170) says Independence of $\mathbf y$ "leaves the possibility to hold individuals responsible for the set of jobs they are able to take". The paper states **no** direction axiom; `thm:w1` characterises $W^1$ without one (agent reference, dependency index). The decreasing direction is a consequence of the characterised measure, not a stated design intent, and the paper text should attribute it as such. The fork (line 540) records the same reading.

### R8 — The class-C fallback. (a) **Honestly labelled, with one label to add.** (b) **Yes.** (c) **A reference-domain sensitivity annex; not an answer to the main question, and the memo says so.**
(a) Add the label Deputy R1 and the fork already give: under the dense law $W^{1,M}$ **is Measure 6 on the market-job universe**, an Independence-of-$A$ object — what measure-map F6 calls "market Measure 6". "The literal market-only Measure 1 under the accepted model" is defensible but invites the reading the amendment forbids.
(b) Inputs are $\beta_c$, the leisure block, $C^{\rm obs}$, $h^{\rm obs}$ plus declared conventions; the verification's dependency audit shows the reachable BASELINE-F1 path indexes nothing else, and the bracket adds only $L_i(5)$ and $L_i(70)$. One precision: bands are deleted in order of their *coefficients*, not their hours, so $h_{\min}(A(\tau))$ visits a subsequence of $\{5,17.5,28.5,33.5,36.5,44.5\}$ determined by the estimated ordering; "at most six values" is right, "thereafter up the ladder" is not implied. Presenting the ladder as a floor menu (§12.1) avoids this and the normalisation problem together.
(c) By the memo's own theorem the bracket carries zero opportunity content. The memo's §12.5(2) — opportunity content must travel through attainment — is the operative recommendation and matches Deputy R5's design brief. I would not substitute a different fallback. The only literal-Measure-1 object with set sensitivity available without re-estimation is the ε-inclusive marked-set object of R5, class B, requiring a prior normative ruling; it should appear in the decision as an option, not as this review's recommendation.

### R9 — Toy checks. **CORRECT arithmetic; one "lower end" claim wrong; F6 consistency conditional.**
All five toys reproduce to printed precision (Toy 1: 85 at $p=0.25$; Toy 2: $(0.4929,0.2667,0.2404)$ vs $(0.2425,0.2199,0.5376)$; Toy 3 as tabled; Toy 4: $m=1133.35$, tilts $0.7853/0.3939$; Toy 5: $1.0089,1.0282,1.0123,1.0292$).
- The ratio is increasing in $\beta_\ell$, so the singles rows are lower ends over the admissible domain (children raise $\beta_\ell^{\rm sf}$). For couples' women the child term is $-0.30547k$ (note §1.2), so the $k=0$ row is **not** the domain minimum (about $1.0117$ at $k=2$). Relabel the couples rows "at $k=0$".
- Toy 5 uses the S11 curvature table ($-0.976/-1.686$). Fork ruling P1 records a second table (R240: $-1.0321/-1.8669$); the measure-map acceptance and the verification pin the S11 tables by hash, so the memo's choice is the accepted one. Say so; P1 affects M-sensitivity only.
- Consistency with F6 ($1.009$–$1.014$ across H-S1, H-C1, H-S2): the couple is consistent (fork Table 1: $1.012$–$1.013$). The two singles are consistent **only if both are men**: any single woman has ratio $\ge1.0282>1.014$ (fork: women $1.028$–$1.053$). The verification is aggregates-only and does not settle it. Goal 1 should confirm the sex flags from the accepted frame; if either is a woman, one of Finding 1b's female numerals or F6 is wrong. One-line check, not a blocker.

### R10 — Unsourced load-bearing assertions; ruling/amendment items not answered.
1. **Finite $\mathcal J$.** The theory's Results section, and the agent reference's standing assumptions, state that $\mathcal J$ and hence every $A$ is finite; `thm:w1` is proved under it (JDI applied $|\bar A\setminus A|$ times). The memo's "literal Measure 1" on an a.s. countably infinite dense set is outside the characterised domain. The memo names the inf/sup reading but not this extension, which the ruling requires. Record it next to off-set evaluation; the closed form is the limit of finite truncations, so nothing numerical changes.
2. **Fork and fork ruling not cited.** Ruling input 4 is absent from memo §0. F-BRIDGE-1 = Deputy R1 statement + fork (M.4); F-BRIDGE-3 = fork N2; the note-§1.1 correction = fork N1; the M/F band = fork Table 1. Attribute.
3. **Household-specific gaps in the executed frames** (R3).
4. **Wage draw support** $[2,170]$ vs renormalisation $[2,590]$ (R3).
5. **The F35 discrepancy is real and remains open**, and the memo was right to flag rather than resolve it. SRC-1 §(f)/(g) quote the pooled ancestor: five hours coefficients ($\beta_E$, pt1, pt2, ft, lh), "F35 remains reference", partition count 29. SRC-2 §4 lists `working_f35 / beta_h_f35` in the S11 spec while SRC-2 also asserts the block was inherited "unchanged" — internally inconsistent. The note §2.1 gives the residual reference width as 26.5 h, which equals $12.5+7+3+4$, i.e. F35 *excluded* from the residual (with F35 as reference the residual would be 29.5 h). So two of three sources indicate F35 carries a coefficient in the S11 spec. Source pass needed; the memo's step-function conclusion and the $5\to17.5$ jump are unaffected either way.
6. **"29 opportunity parameters"** is sourced (SRC-1 §(g), pooled-spec partition), but the memo's §4.3 enumeration ("β_E, the five hours-band coefficients, …") double-counts $\beta_E$ (it is one of the five) and sums to 30; if F35 carries a coefficient the true count is 30. Fix the enumeration; the invariance claim does not depend on it.
7. **§5.3 large-count rate** valid only where $1/(\Lambda c)$ stays inside the residual band; the small-$\Lambda$ rows of Toy 3 are outside validity.
8. **Evidence row 24** classes the shock-exclusion rule as "MAINTAINED RULE (Deputy)". Given R5 it is the rule on which verdict D rests, and it is a Deputy R5 design requirement and a BASELINE-F1 dependency prohibition, not merely a convention; the decision request should say so.
9. Amendment items answered: §A (three objects kept separate — throughout); §B (§2.2, Theorem 3 correctly sourced); §C (§3.4/§6); §D (§7, complete); §E (§8; POSFIT held to diagnostic weight with the A7 caveat); §F (honoured); §G (§9, with R8(b)); §H (§10.4–10.5, subject to R3); §I (D with C fallback). Ruling §B relabelling/duplication — §5.3, correct. Nothing in the ruling or amendment is left unanswered; the gaps are provenance and declaration.

---

## 4. Exact corrections requested before the memo goes to the Deputy

Material (change meaning):

- **M1** §1 and §12.7: replace the "complete dichotomy" framing. Shocks excluded from $R$ ⇒ $W^{1,M}=m_i(5)$ a.s. (D). Shocks admitted ⇒ $W^{1,M}=C^{\rm obs}\exp[(s_y-\sup_{A^M}s)/\beta_c]\le C^{\rm obs}$, a.s. finite, set-sensitive, conditional law depending on $\kappa_i$ (class B; needs a declared κ family and a prior amendment of Deputy R5's ε requirement). Add the third branch to §12.7.
- **M2** §4.3 and §10.5: add the availability declaration (base-measure support is the ability set; masked non-positive-consumption alternatives and absent home atoms are in $A$) to the conditions for common support; list it in evidence row 25, citing SRC-2 §2, note §1.1, F7, and the verification's constructed home row.
- **M3** §3.1 and §13: name the extension from finite $\mathcal J$ to the a.s. infinite dense set as a domain extension, with the finite-truncation limit as justification.
- **M4** §12.1: label $W^{1,M}=m_i(5)$ as Measure 6 on the market-job universe (Independence-of-$A$ object), per Deputy R1 and measure-map F6.

Precision (no change of verdict):

- **P1** §0: add the fork, the fork ruling (Deputy R1–R6) and SRC-1 as inputs; attribute F-BRIDGE-1 to R1 + (M.4), F-BRIDGE-3 to N2, the M/F band to fork Table 1; carry N1.
- **P2** §4.1: state that $\kappa_i$ multiplies the home atom; replace "the unique construction in play" by "the exact random-set reading; the deterministic full-support reading is equally exact and gives the same welfare value".
- **P3** §4.3 and §10.5: cite the proposal draw wage support $[2,170]$ (`DEFAULT_W_MAX`) and flag the $[2,590]$ reconciliation.
- **P4** §4.3 corollary: fix the enumeration (β_E is one of the five hours coefficients); note the count is 29 or 30 depending on R10-5.
- **P5** §5.3 and Toy 3: mark the first display as unconditional; restrict or label the rate table to $1/(\Lambda c)\ll12.5$ h.
- **P6** §9: replace "thereafter up the ladder 28.5, 33.5, 36.5, 44.5" by "thereafter to the lower endpoint of the surviving bands, in the order of their estimated coefficients"; record that the F35 question is open in the sources (R10-5), not resolved.
- **P7** Appendix A Toy 5: relabel the couples rows "$k=0$"; note the S11 table is the hash-pinned accepted one (P1 of the fork ruling); add the F6 consistency condition and the sex-flag check.
- **P8** §3.2 and §12.5(3): attribute anti-monotonicity as a consequence of the characterised measure, not a stated axiomatic intent.
- **P9** §10.2: cite the verification's nonworker counts (204 singles, 50 couples) to size the reversal, and note that C1's exact equality is verified under F, which is why it must be replaced rather than reused under M.

---

## 5. Decision framing for the Deputy/PI

The memo's decision is correctly posed in its two branches. It should be posed with a third, so the maintained rule is decided rather than inherited:

> (i) Accept D under the maintained shock-exclusion rule (Deputy R5; BASELINE-F1 §2); Mapping F primary; the §12.1 bracket as a labelled reference-domain annex (Measure 6 on the market universe); opportunity content routed through attainment (R5 design).
> (ii) Authorise a scoped positive-model extension mission (finite-offer specification with re-estimation, or external offer information) for a literal set-sensitive Measure 1 with shocks excluded.
> (iii) Amend the shock-exclusion requirement — decide whether match-specific taste is part of the job in Haydar–Maniquet's sense — and, if admitted, authorise a design (not execution) card for the ε-inclusive marked-set Measure 1 with a declared $\kappa_i$ sensitivity family (class B; no re-estimation; the note §7.1 grid made rigorous under the §4.1 conditional law). Note that (iii) also changes the verified Mapping-F object, which rests on the same rule.

This review does not recommend among them. It records that (iii) exists, that the memo's dichotomy did not, and that (i) is ready for a bounded prototype the moment it is chosen.

---

## 6. Output discipline

| Field | Content |
|---|---|
| **Mission ID** | JMP-W1-MARKET-SET-BRIDGE-1 — independent conceptual review |
| **Authoritative inputs** | §0 items 1–8; complete. Controlling: amendment over ruling; Deputy Appendix A over the fork ruling's §1. |
| **Decisions made** | (1) Verdict D upheld under the maintained shock-exclusion rule. (2) R5 ruled INCORRECT; corrected object derived (class B, κ-dependent, $\le C^{\rm obs}$). (3) R1, R2 (conditional), R3 (conditional on two declarations), R4 (genuine under the chosen correspondence), R6, R7 (mathematics), R9 (arithmetic) ruled CORRECT; R8 fallback accepted with a Measure-6 label. (4) Four material and nine precision corrections requested (§4). (5) Classification: bracket ready for a bounded prototype after one stated decision; literal set-sensitive object needs a positive-model change under the current rule, or a rule amendment plus a sensitivity primitive under the alternative. |
| **Unresolved decisions** | The §12.7 decision, now with branch (iii). Evidence-row-25 conventions plus the availability declaration and the finite-$\mathcal J$ extension. F35 coefficient status in the S11 spec (three sources disagree). Sex flags of H-S1 and H-S2. Wage draw-support reconciliation. |
| **Exact output filename** | `JMP_W1_stochastic_ability_set_bridge_review_v1.md` |
| **Next authorised action** | Return this review with the memo to Goal 1, then to the Deputy with the decision above. Goal 1 may ask the author for a memo v2 applying §4 before transmission, or transmit v1 with this review attached; either is within the ruling. No execution, prototype, calibration or re-estimation is authorised by this review. |
