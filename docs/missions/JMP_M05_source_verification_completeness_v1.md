## Task 2 — Completeness Review

I reviewed the three uploaded artifacts directly (parsed the CSV and JSON, cross-checked all three against each other and against the markdown report's own tables), then checked the full report against the 22-heading contract, the ledger's V-1–V-12 inventory, and the five binding corrections (C-1–C-5). One caveat stated up front: my checks below verify internal consistency of the three delivered files and their consistency with the governance documents. I have no independent channel to your local repositories — the git-state, hash, and timestamp claims are taken from the audit's self-report and your relay of its terminal output, not re-verified against `Job_Market_paper`/`MNL` directly.

---

# JMP-M05 Source-Verification Completeness Memo v1

**Mission:** JMP-M05 Stage A
**Reviewer:** JMP-M05 Task Manager
**Artifact under review:** `FR_P2a_region_live_phase5_source_verification_v1.md`, `phase5_parameter_map_v1.csv`, `phase5_source_inventory_v1.json`

## 1. Completeness verdict

**REPORT COMPLETE WITH NONBLOCKING GAPS.**

All structural requirements are met, all provenance items are established, all four blocking-class verification tasks (V-2, V-4, V-5, V-7) return fully resolved facts, and the three remaining `UNKNOWN` items are genuinely unrecoverable from any static source and are correctly classified as nonblocking. No halt condition fires. No follow-up is issuable because none of the open items can be closed through further static inspection (§13).

## 2. Artifacts reviewed

| Artifact | Format check | Cross-consistency check |
| --- | --- | --- |
| `FR_P2a_region_live_phase5_source_verification_v1.md` | 22/22 required headings present, in order, single final-verdict string | consistent with CSV and JSON on every shared fact |
| `phase5_parameter_map_v1.csv` | parses; 47 data rows + header | 35 `interior` + 10 `pinned` + 2 `active_bound` = 47; active-bound rows' `dist_to_ub`/`grad_free_negll` match report §6.2 and §8 exactly |
| `phase5_source_inventory_v1.json` | parses; all expected top-level keys present (`revisions`, `bundles`, `sources`, `likelihood_contract`, `cluster_contract`, `numerical_environment`, `open_unknowns`) | revisions, cluster contract, and numerical-environment blocks match report §3–5, §13–14, §17 verbatim |

## 3. Structural checks

- Three files, exactly as named in the CREATE EXACTLY block. ✓
- Exactly the 22 required headings, correctly ordered, no additions or omissions. ✓
- Exactly one final-verdict string used (`SOURCE CONTRACT COMPLETE WITH NONBLOCKING GAPS`), stated identically at §1 and as the closing line. ✓
- No dedicated "POST-AUDIT STATUS" heading inside the markdown file itself — this is a non-defect: the prompt places that requirement after FINAL VERDICT as a terminal chat-report item, not as one of the 22 file headings, and its content (three repository statuses, three created files, no-modification, no-commit) is fully covered by §2, §3, and §21 of the file plus your relayed return packet.
- CSV and JSON both parse without error and satisfy their declared row/column contracts. ✓

## 4. Repository-integrity checks

- MNL: no tracked change, exactly the three intended new files. ✓
- Nested `dclaborsupply`: clean, unchanged. ✓
- `Job_Market_paper`: unchanged; pre-audit and post-audit untracked-file sets are identical to the three files named in the Goal-1 Manager addendum, including the capital-`M` `docs/Missions/` casing artifact, which the report correctly identifies as a case-insensitive-filesystem non-anomaly. ✓
- No commit in any of the three repositories. ✓

## 5. Provenance checks

- `Job_Market_paper` HEAD `1d31d10a…` — matches the addendum exactly.
- Governance checkpoint `30fbe2da…` correctly identified as the *parent* of HEAD, with the one-commit gap explained as additive documentation only (ten files, 2,399 insertions, zero deletions/modifications). This reconciles the stage-A correction memo's anchor with the addendum's current-HEAD instruction without contradiction.
- MNL HEAD `982c5221…`, nested/gitlink `27756a06…` — both match the charter's binding revisions.
- V-1 descendancy: `982c5221…` confirmed a descendant of `fee60723…` via exactly one intervening commit (the checkpoint itself), ten changed files, all acceptance-memo/execution-report/bundle class — matches the ledger's expectation in §5.1 (G-A row) precisely.

## 6. Parameter-contract checks

- 47/37/35 vectors established **by name** from two independently agreeing committed sources (spec parser + Phase-4 manifest), not by position arithmetic — satisfies HM-MAP.
- Active-bound identity (`beta_l_age2_sm`, `beta_l_age2_sf` at free positions 2, 6) confirmed by name and by exact gradient-value match against `theta_estimated.csv`, closing V-3's provisional numeric guess.
- All ten pins classified by mechanism (eight unreferenced by the singles routing path, two multiplying an identically-zero year covariate) — this **overturns** the task plan's working assumption that `theta_l_f` is a normalisation candidate. That correction is source-grounded (routing-function inspection), not a methodological opinion, and is properly stated as a fact for Stage B to carry forward, not as a Stage-A decision.
- Note for the record, not a defect: the 1,555-household figure is the correct current-evidence count for the P2a 2016 region-live application. It should not be reconciled against older project-memory figures for pooled 2015–2017 singles — the canonical-state file already flags that pooling as stale context, and this audit's household count is independent confirmation of the *current* application, not a discrepancy needing resolution.

## 7. Likelihood-contract checks

- Call route and additive composition traced to exact line numbers in `run_p2a_regionlive_rebuild.py` and `engine_jax.py`, with the score hook (`per_group=True`) identified as already present in production code.
- V-4/C-1 finding: the task plan's `ln(101)` uniform-benchmark argument is shown to be unsupported by source (`V_obs` is one term inside its own log-sum-exp; no floor exists). This is exactly the treatment C-1 required — the `12.25` nats/household figure is left as a diagnostic clue, not elevated to a compositional proof, and the report explicitly instructs that the comparison be **dropped**, not restated. This satisfies the audit brief's interpretive restriction against inferring composition from average negLL.
- Objective scaling (`-jnp.sum(per)`, unweighted, no `dwt` read) — closes V-6/G-D cleanly.

## 8. Cluster-contract checks

- `idhh`/`idorighh`/`cluster_id` shown identical elementwise at loader group starts; 1,555 groups = 1,555 clusters = 1,555 additive terms; degeneracy (one term per cluster) established, giving algebraic identity to the household-level OPG sandwich **in this application only** — correctly scoped per C-3, with no claim extended to couples or pooled years.
- The package's existing `run_t3_cluster_count_check` default (`expected=9657`) is flagged as a P3a-pooled artifact that does not apply here — a useful inventory note that prevents a stale constant from leaking into Stage B.

## 9. Regional/access checks

- The ten-parameter block is explicitly and correctly described as the regional/urbanisation/GSUR access block only, with the opportunity index's occupation, hours-offer, and wage-density coordinates named as sitting outside it — satisfies C-2/C-5 exactly.
- `gsur` correctly reclassified as a continuous `(drgn1, educ3, sex)`-indexed rate rather than a region dummy, with omitted categories verified by direct count (`drgn1==1`, 245 HH; `drgru`, 395 HH). This sharpens task plan §9.2(1)'s conditional requirement rather than contradicting it.

## 10. Bread and environment checks

- Bundle hash recomputation matches for both Phase-3 and Phase-4 bundles; all seven Phase-4 members and thirteen runtime-input files rehash correctly.
- Two findings materially affect Stage B: `hessian_free.csv` is not bit-exact to `hessian_free.npy` (337/1,369 entries differ, ≤1.82e-12), and the persisted array is the **raw, unsymmetrised** `H`, not the `Hs` Phase 4 actually used downstream. Both are stated as facts with a named consequence ("Phase 5 must load the `.npy` and symmetrise on load against the recorded threshold") rather than as an inference-method choice — this stays inside the audit's mandate (V-10, bread provenance) and does not cross into the active-bound or finite-sample-correction decisions reserved for Stage B/C.
- x64 established from source at a named call site, ahead of every array creation on the accepted route — closes HM-X64 without needing the version-string unknowns below.

## 11. UNKNOWN register

| # | Item | Recoverable by further static inspection? |
| --- | --- | --- |
| 1 | JAX / jaxlib version at Phase-3/4 execution time | No — never logged in either manifest; today's interpreter value is not evidence of the historical one |
| 2 | Platform string / thread / XLA flags at execution time | No — same reason |
| 3 | SciPy version at Phase-3 execution time | No — same reason; also moot, since Phase 5 does not repeat the L-BFGS-B call |

All three are historical facts that were never written to any artifact; no repository inspection today can recover them, and re-execution to capture them is prohibited at this mission stage. This is why no follow-up is issued (§13).

## 12. Blocking classification

Per task plan §17 step 3's triage rule: a halt fires only if V-2, V-4, V-5, or V-7 returns `UNKNOWN`. None does — all four are fully resolved. The three open items above fall outside that blocking set (they sit under V-11, which was never load-bearing for the score-identity tolerance, since float64 is established independently from source). **No halt condition fires. No design-blocking gap remains.**

## 13. Follow-up used

**None.** The report is otherwise complete, and the only remaining omissions are execution-time environment facts that were never recorded and cannot be reconstructed by any static check available to the audit's read-only mandate. Issuing a follow-up against an unrecoverable historical fact would not close it; it is correctly left as a permanent, nonblocking `UNKNOWN` for the Phase-5 implementation charter to record going forward.

## 14. Recommendation to Goal 1 Manager

Accept the source report as delivered. In the acceptance memo, carry forward the five §20 findings as **verified inputs binding on the design memo**, not as open recommendations:

1. Drop the `ln(101)` comparison entirely; do not restate it in any form.
2. Assign no pin to a "normalisation" reporting category; report all ten as structurally inapplicable, and separately flag that the true normalisations (`beta_c`, couples `theta_c`, `theta_l_m`, removed `beta_ll`) sit outside the 47-vector and outside the pin-reporting convention altogether.
3. Treat `gsur` as a standalone continuous-rate access covariate, distinct from the seven-dummy NUTS-1 null and the two-dummy urbanisation null; the design memo's H0-A/B/C structure should reflect three separate constructs, not one ten-parameter block.
4. Name `hessian_free.npy` as the sole authoritative bread artifact.
5. Require symmetrisation on load against the recorded threshold before any bread/meat construction.

No manager decision (finite-sample correction, active-bound treatment, score-artifact format) is closed by this report, as required — it supplies verified facts (`N = G = 1,555`, degenerate clustering, strict KKT activity) that narrow those decisions without making them.

## 15. Immediate next action

Return this completeness memo together with the three source-audit files to the Goal 1 Manager chat, per `JMP_M05_stageA_correction_memo_v1.md` §6 step 6. Do not return to the deputy programme director. On Goal 1 Manager acceptance of the factual findings, Stage A closes (ledger §1) and Stage B — the inference design memo, delivered by a separate Opus author chat with thinking on, using `JMP_M05_inference_design_prompt_v1.md` plus this report and corrections C-1–C-5 as appended authoritative inputs — may be commissioned.