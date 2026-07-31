# JMP-M05 Stage-B Author Addendum v1 — Binding

**Status:** Binding supplement to `docs/prompts/JMP_M05_inference_design_prompt_v1.md`. Paste immediately after the full committed prompt text. Where this addendum and the prompt conflict, this addendum governs; everywhere else the prompt governs unchanged.
**Issued by:** Goal 1 Manager — Empirical JMP, 2026-07-31, under `JMP_Goal1_manager_operating_contract_v1.md` and mission ledger v2 rulings R-1–R-5.
**Target repository path:** `docs/prompts/JMP_M05_stageB_author_addendum_v1.md` (Job_Market_paper; untracked until the next documentation checkpoint).

## 1. Authoritative-input extension

Insert into the prompt's AUTHORITATIVE ORDER, after item 5 (committed manager-acceptance memos and repository evidence) and before project memory:

5a. `FR_P2a_region_live_phase5_source_verification_v1.md` + `phase5_parameter_map_v1.csv` + `phase5_source_inventory_v1.json` (Stage-A audit, accepted by Goal 1 ruling R-1);
5b. `JMP_M05_source_verification_completeness_v1.md` (task-manager completeness review);
5c. `JMP_M05_mission_ledger_v2.md` §§3–5 (ratified findings, errata, rulings).

Every factual claim in the design memo about the likelihood, parameters, bounds, pins, clusters, weights, regional covariates, bread, or environment must cite the audit report section that verifies it, or be marked UNKNOWN.

## 2. ERR-1 — bound-direction correction (supersedes prompt text)

The prompt's BINDING ACCEPTED STATE sentence "two free parameters at their accepted lower bounds" is factually wrong and is superseded by the source-verified statement (audit §8):

- `beta_l_age2_sm` (free position 2) and `beta_l_age2_sf` (free position 6) sit at their accepted **upper** bound `1.0` (spec bounds `[-1.0, 1.0]`), `dist_ub = 0.0`;
- negLL free-gradient components `-0.8445544161794221` and `-1.4682021491125388`; KKT multipliers `0.8446` and `1.4682`, both strictly positive;
- strict activity: multipliers are 3–4 orders of magnitude above the interior maximum `1.0992597206183063e-4` (`beta_w_educH`, free position 33); the task plan §7.3 falsification criterion does not trigger;
- consistent with Phase-3 G-15 (bound hits exactly this pair) and G-16 (zero in-bounds violations at ε = 1e-9).

All boundary-inference reasoning in the memo (prompt requirement E) must use the upper-bound direction: the likelihood objective would fall further if these coordinates could rise past 1.0; the feasible cone points downward in these coordinates.

## 3. ERR-2 — structure and verdict ruling

The prompt's CREATE block governs: exactly its 23 headings, in order, and exactly its verdict set (`READY FOR MANAGER REVIEW` / `READY WITH OPEN DECISIONS` / `BLOCKED`). The task plan §14 heading list and verdict set are superseded on structure. The task plan §14 **properties** remain binding content requirements inside the prompt's structure:

- one recommended baseline per decision, with rejected alternatives named and rejection reasons given — no menus;
- every recommendation states its own pre-registered falsification criterion;
- every numerical claim traces to a verified source or is marked UNKNOWN;
- permitted and prohibited paper-facing claims stated explicitly (place in heading 20, Interpretation limits);
- implementation-mission handoff content supplied (place in headings 21–22) without writing the implementation charter itself.

## 4. Binding verified inputs (ratified findings; facts binding, decisions yours)

- **F-1 (audit §11).** `ln(101)` is not an objective bound. `l_g = V_obs − logsumexp_j(V_gj) ≤ 0` with no `−ln(101)` floor; every index term (`u`, `log_h`, `log_w`, `log_market`, `−log_prior`) is alternative-specific and enters inside the index. The household contribution is exactly ONE additive term; any derivation writing `l_g` as "choice term + wage-density term" is wrong for this model. Do not restate the `ln(101)` comparison in any form; rest nothing on average negLL.
- **F-2 (audit §9).** No pin is a normalisation: eight are unreferenced by the singles builder; two (`beta_E_y2015`, `beta_E_y2017`) multiply an identically-zero 2016 covariate. True normalisations (`beta_c = 1.0`, couples `theta_c = 0.0`, `theta_l_m = −0.8`, removed `beta_ll`) sit outside the 47-vector. A pin-reporting convention with a "normalisation" category would have no members; design requirement F accordingly.
- **F-3 (audit §15).** `gsur` is a continuous `(drgn1, educ3, sex)`-indexed rate (×10, `offer_only_vars`), not a region dummy. Verified references: NUTS-1 region 1 (`drgn1 == 1`, 245 households); rural (`drgru`, 395 households). Constraint: the prompt's requirement G of ONE ten-degree-of-freedom omnibus joint test stands; whether and how to layer sub-tests (gsur alone / seven NUTS-1 dummies / two urbanisation dummies) is your design decision under C-2/C-5 language discipline.
- **F-4 (audit §16).** `hessian_free.csv` is not bit-exact to `hessian_free.npy` (337/1,369 entries differ; ≤1.82e-12 abs). Authoritative bread: `hessian_free.npy` (float64, 37×37, C-contiguous, SHA-256 `e9ca080ecc7e40e43881b9422af0095f23ad2bfef3e84648d2031a33eb9e4061`). The fingerprint gates (requirement H) must bind to the `.npy`, not the CSV.
- **F-5 (audit §16).** The persisted Hessian is the raw unsymmetrised `H`; the `Hs` Phase 4 used for every downstream diagnostic is not persisted (`max |H − Hᵀ| = 1.8189894035458565e-12`). The design must mandate: load `hessian_free.npy`, symmetrise on load against the recorded threshold `2.3588019878151842e-4`, and gate on it — otherwise Phase 5 is not using the object Phase 4 accepted.
- **Scaling and weights (audit §12).** The objective is a verified UNWEIGHTED SUM over households (`-jnp.sum(per)`; `tot = nm + nf`); survey weight `dwt` exists in the stem but is never loaded or read. The frozen identity `Σ_g s_g = −∇negLL` therefore holds with matched scaling and no correction factor — state it as verified, not assumed.
- **Cluster contract (audit §13–14).** Exactly 1,555 additive terms; `cluster_id = idorighh = idhh` elementwise at loader group starts; one term per cluster ⇒ clustering is DEGENERATE and the household-cluster sandwich is algebraically identical to the household-level OPG sandwich in this application only. Use C-3 language: household-clustered and misspecification-robust, with the equivalence explained; no unconditional claims about couples or pooled years.
- **Correction-scalar inputs (audit §20).** `N = G = 1,555` is verified, not presumed; the 157,055 row count is definitively not a candidate for N. K remains yours to fix under requirement D/E.
- **Score route (audit §10, inventory JSON).** The production builder already exposes `per_group=True`, returning the `(n_groups,)` positive log-likelihood vector; `jax.jacrev` of that vector is the 1,555×37 score matrix. Design requirement A's efficient, non-row-Jacobian route should be specified around this existing hook.
- **Environment (audit §17, §19).** float64 is source-established (`_load_jax()` sets `jax_enable_x64` before any array creation). JAX/jaxlib versions, platform, threads/XLA flags, and SciPy version at Phase-3/4 execution time are PERMANENT UNKNOWNS — never recorded. The implementation-handoff content must mandate that Phase-5 execution logs interpreter, JAX/jaxlib, platform, and thread/XLA facts into its manifest.

## 5. Corrections C-1 to C-5 (in force, one line each)

C-1: the 12.25 nats/household figure is a diagnostic clue only; use only the verified composition. C-2: the ten-parameter joint test is the regional/urbanisation/GSUR access block only — never "no opportunity heterogeneity", never the complete opportunity-versus-preference test, never the decomposition share. C-3: cluster/OPG terminology conditional on the verified degenerate structure. C-4: the 35-dimensional conditional covariance is a working hypothesis requiring independent review; no symmetric Wald inference for the two bound parameters under the baseline. C-5: always distinguish regional/access-block inference, the full opportunity mechanism, and the later welfare decomposition.

## 6. Output handling

Produce the complete memo as one downloadable markdown file named exactly `FR_P2a_region_live_phase5_inference_design_v1.md`. The user saves it to `MNL/docs/France_case/P2a/`. It remains UNCOMMITTED before independent review and manager acceptance. Return the file plus a short cover note stating: the verdict; the three recommended manager-decision baselines (finite-sample correction, active-bound treatment, score artifact); and any open decisions — to the Goal 1 Manager chat only.

## 7. Standing prohibitions (unchanged from the prompt)

No implementation, no computation of scores/covariances/tests, no optimizer/gradient/Hessian/EUROMOD/notebook runs, no commits, no respecification of the accepted model, no welfare or decomposition content beyond the boundary statement, no couples/pooled-years/other-country broadening.
