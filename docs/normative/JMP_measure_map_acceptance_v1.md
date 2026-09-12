# JMP_measure_map_acceptance_v1.md — Goal 1 acceptance of MEASURE-MAP-1R and BASELINE-F-1 unlock

| Field | Value |
|---|---|
| Mission | MEASURE-MAP-1R acceptance; BASELINE-F-1 unlock (Deputy R4; BASELINE_F1 ruling §2–§4) |
| Date | 2026-09-11 |
| Author | Goal 1 Manager (Claude project chat) |
| Status | ACCEPTANCE RECORD. MEASURE-MAP-1R is **ACCEPTED**. BASELINE-F-1 is **UNLOCKED** once GATE-1 step 2 passes (mechanical term-by-term confirmation, §2.2). |
| Intended path | `Job_Market_paper/docs/normative/JMP_measure_map_acceptance_v1.md` |

## 0. Inputs

- `Job_Market_paper/docs/normative/JMP_measure_map_v1.md`. This is the MEASURE-MAP-1R return. It was run on Codex (GPT-6 Astra) and was uncommitted at review; GATE-1 records its commit and SHA-256.
- BASELINE-F1-PREP provenance: `MNL/docs/corr/baseline_f1_provenance_v1.md`, branch `welfare/baseline-f1`, commit `838127e05c8f6ee97dd6088c6f754fa0709a1935`, SHA-256 `ab6e544f58e6921f4d79dc3cc183226a84755e14e192567e0922d24f3b91f938`. Goal 1 reviewed the PREP return summary; the document itself is cross-checked by GATE-1.
- BASELINE-F1-PREP-2: commit `686446802987069207d89f30ca84c7802e53fab4`; report `MNL/docs/corr/baseline_f1_prep2_report_v1.md`; 11 tests passing.
- REC-1-C: commits `8dcc476b6008d6926f8f46d99c32d26571976dfa` and `acf33c645f818463a4571e501d221b96a98fb1b2`. The fork record is citation-closed at r3 (158 of 158 numerals reproduced).
- Controlling rulings: Deputy R1–R6 (`JMP_W1_fork_ruling_v1.md`, Appendix A) and `JMP_W1_BASELINE_F1_authorization_and_Cobs_ruling_v1.md`.

## 1. Pre-registered acceptance criteria (MEASURE-MAP-1R card)

| Criterion | Result | Evidence in the map |
|---|---|---|
| (a) literal W1-F = (b) independent W4 inversion, to machine precision, for every checked household | PASS | §4. Differences b − a ≤ 1.4e-12 EUR/month; W4 utility residual 0 in all three checks. |
| Nonworker: (a) = C_obs | PASS | H-S2: ratio exactly 1. |
| Worker: (a) < C_obs | PASS | H-S1: 0.6304; H-C1: 0.4808. |
| Executed W1-EA classed DIFFERENT OBJECT | PASS | §2 and §7. |
| R4 vocabulary used throughout | PASS | §2, with all 13 columns. |
| Every ε, opportunity and proposal entry backed by a code line | PASS | Evidence ledger E1–E8. |
| No stored number called literal without a step-3 check | PASS | §4 and §5. |
| Valid file hashes | PASS | m08 SHA-256 now has 64 hex characters; the earlier 63-character digest is discarded. |

## 2. Unlock reconciliation (two independent traces: PREP versus MEASURE-MAP-1R)

### 2.1 Agreement on the consumption argument, parameters and call path

| Item | PREP provenance | MEASURE-MAP-1R | Agree |
|---|---|---|---|
| C_obs source | Accepted S10 observed row, `consumption_raw` = household-summed `ils_dispy_takeup` | Same: `consumption` = `consumption_raw`; engine argument `c_norm` = C_obs / c_scale | Yes |
| Units | EUR per month, household | EUR per household per month | Yes |
| Equivalisation | None | None before utility; S12 applied m_oecd only to outputs | Yes |
| Floor | Not applicable (loader guard binds 0 times) | No EUR 1 floor in the accepted estimation frame | Yes |
| Utility call path | `engine_jax.py:299–308` (singles), `514–530` (couples) | `engine_jax.py:303–308`, `519–530` | Yes (overlapping line ranges) |
| Parameter tables | S11 singles and couples | S11 singles and couples, with the certification memo named | Yes |
| β_c (singles, couples) | 2.038731824410903, 2.101720268206207 | Same | Yes |
| θ_c | Exactly 0 | 0 | Yes |
| Accepted N (singles, couples) | 1,540 and 2,223 | Frames hashed in Appendix B | Yes (GATE-1 pins the frame hashes) |
| Content of L | Sex-specific leisure (singles); joint male/female leisure (couples) | Leisure only; coefficients carry age, age² and child shifters; no wage or occupation term | Yes |

Numerical three-way agreement on the check households is reported below. All three routes are independent code paths.

| Household | PREP-2 production W / C_obs | MEASURE-MAP-1R W / C_obs | Engine oracle (PREP-2 O1) ΔL difference |
|---|---|---|---|
| Single H-S1 | 0.6304345043711471 | 0.6304345043711471 | −1.8e-15 |
| Couple H-C1 | 0.4808435094822485 | 0.4808435094822490 | 2.2e-15 |
| Nonworker H-S2 | 1.0 | 1.0 | 0 |

### 2.2 Term-by-term assignment of estimated parameters

Both traces independently state that L consists of leisure terms only, and that every other estimated term enters the opportunity density or the proposal. The numerical agreement above confirms the implementation of that assignment. It does not, by itself, confirm that the assignment is correct: a mis-assigned term would drop out of both routes equally.

A mechanical term-by-term comparison is therefore delegated to GATE-1 step 2, under a hard halt rule. It compares the PREP provenance classification table against the utility block at `engine_jax.py:303–308` and `519–530` and against the map's statement of L.

**BASELINE-F-1 unlocks only if that comparison shows no disagreement.** Any disagreement blocks the unlock and returns to the Deputy under BASELINE_F1 §3.

### 2.3 Deputy auto-unlock conditions (BASELINE_F1 §2)

- **E2 resolved by the audit: YES.** The frozen E2 contract is in the map's §4. It defines C_obs as raw household EUROMOD-priced disposable consumption after the stored take-up rule, in EUR per month, unequivalised; the engine uses it as `c_norm`. No ambiguous raw-versus-equivalised branch exists.
- **No literal-correspondence conflict remains: YES.** The literal objects are computed outside every executed path, and three independent routes agree.

No further Deputy round-trip is required.

## 3. Findings recorded from MEASURE-MAP-1R, with dispositions

| ID | Finding | Disposition |
|---|---|---|
| F1 | Every stored W1–W6 is a DIFFERENT OBJECT: each attained side is an inclusive value, never u(z_obs). Literal W1-F, W4 and market Measure 6 are NOT IMPLEMENTED in any stored lineage. | Recorded. The only reusable component is the home-reference primitive `R_single_node`, which PREP-2 confirmed is utility-only. |
| F2 | The m08 W4 wrapper (line 485) evaluates 1/θ_c without the log branch, so it fails at the accepted θ_c = 0. | BASELINE-F-1 does not use it. Historical defect; no repair. |
| F3 | The historical W1-EA path in `BasisArrays` uses `log_ghat` rather than `opp_hat`, so the base-proposal factor is absent. | Historical under R2. Any future revival of an ex-ante functional must address this first. No HFIX work. |
| F4 | At the check households, stored S12 W1-EA divided by literal W1-F is 1.91, 5.24 and 0.72. | Internal record only. This confirms that the retired object is not a small perturbation of W1-F. Not for presentation (R2, R6). |
| F5 | `welfare_identity_check_v1` verifies the production J/H identity under S8/R240 parameters with β_c = 1. It predates S11. | Not evidence for any literal distribution. Confirms MM-4 in the fork ruling record. |
| F6 | Couple H-C1: the market minimum is at (0,5), i.e. the woman works 5 hours and the man is at home. Market Measure 6 / W1-F is between 1.009 and 1.014 across the checks. | Consistent with fork §5 under S11 and with the fork's 1–5% range. Relevant to M-sensitivity only. |
| F7 | The 119 couples: not in baseline W1-F; present in the executed ex-ante objects; relevant to counterfactual choice sets. | R5 must specify the positive-consumption domain and the attainment operator. Carried into the R5 design. |
| F8 | The O-1 (R-85) disposable-income-for-pay substitution affects W2, W3 and W5 only. | No current ruling requires W2, W3 or W5. |
| F9 | S12 equivalised its outputs after computing W1. | BASELINE-F-1 stays in raw household EUR per month (E2). Any equivalised presentation would be a separately documented transformation and is not authorised now. Singles and couples are reported separately, with no pooled distribution. |
| F10 | MEASURE-MAP-1R and PREP were both run on Codex GPT-6 Astra, as separate returns with separate evidence ledgers. | Accepted as independent traces. Model independence is restored at verification, which runs on Claude Code. |

## 4. Gate file (written by GATE-1; never edited by hand)

The gate file is `gate/measure_map_accepted.json`, at the path and in the schema expected by the validator in `MNL/scripts/welfare/run_baseline_f1_full_sample.py`. The validator is read and not modified. The file carries:

- the mission identity (MEASURE-MAP-1R);
- the canonical document path, the 40-character commit, and the committed SHA-256 of `JMP_measure_map_v1.md`;
- the path, commit and SHA-256 of this acceptance record;
- the accepted estimation-frame hashes:
  - singles `641ceb0ed47b38111c4bac25deb9dd0d1f5942b931a694cd4cc1cec13d429128`;
  - couples `50b8289e97ceef16d767ce5799d9f0a712100c4db051444be630b1a56b34345d`.

It is written only after GATE-1 step 2 passes.

## 5. Next authorised actions

1. **GATE-1** (Claude Code): commit the map and this record; run the term-by-term comparison; write the gate file.
2. **BASELINE-F1-RUN** (Codex): run the full sample with pre-registered checks C1–C6. Aggregates only in Git.
3. **BASELINE-F1-VERIFY** (Claude Code, fresh): independent recomputation and verdict.
4. **R5**: Goal 1 drafts `JMP_counterfactual_attainment_design_v1.md`. This is authorised from this acceptance onward. No counterfactual execution.
5. After VERIFIED: the document update wave (Beamer, paper, HTML reports, A-to-Z notebook), issued as bounded modules per document stratum under R6.
