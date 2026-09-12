# JMP — Step 0 status (SRC-1)

Date: 2026-09-12
Author: Claude Code Sonnet 5 (mechanical repository/source extraction, read-only)
Scope: per `JMP_market_set_bridge_and_parallel_work_ruling_v1.md`, Step 0. Earlier chat-cited
hashes are stale; every path/hash/status below was read directly from the working trees on
2026-09-12. No writes performed outside this file and `JMP_bridge_source_extract_v1.md`.

## Current HEADs

| Repo | Path | HEAD | Last commit (subject / date) |
|---|---|---|---|
| Job_Market_paper | `C:\Users\hisham\Repo\Job_Market_paper` | `cafe0ba019d31f970b43f143c4366bfc329fd271` | "docs(seminar): rebuild the deck on R6 content; retire the W1-EA block" (2026-09-12 10:01:04 +0200) |
| MNL | `C:\Users\hisham\Repo\MNL` | `b5550af594797c699c24af97f92f5338a3de5203` | "Verify BASELINE-F1 independently" (2026-09-11 22:48:33 +0200) |
| MNL_posfit | `C:\Users\hisham\Repo\MNL_posfit` (a `git worktree` of MNL, branch `diagnostics/posfit-v2`) | `a2e80a82646b3325b913d4a4927b360b743a020b` | "diagnostics: add POSFIT support coverage v2b" (2026-09-12 10:45:53 +0200) |
| dclaborsupply-monorepo (standalone checkout) | `C:\Users\hisham\Repo\dclaborsupply-monorepo` | `94c25f24c2738e893823c29436b960c314971f33` | "docs(spec-reference): document the couples engine-ready contract and its validation rules" (2026-09-01 19:15:59 +0200) |
| dclaborsupply-monorepo (engine checkout **actually used inside MNL**, gitlink) | `C:\Users\hisham\Repo\MNL\dclaborsupply-monorepo` | `55bb0d0ea7a1ad2d683f8b2b2a9f7bfb3d5118df` | "feat: implement sampled multiset criterion A" (2026-09-08 19:34:52 +0200) |
| dclaborsupply-monorepo (engine submodule inside MNL_posfit worktree) | `C:\Users\hisham\Repo\MNL_posfit\dclaborsupply-monorepo` | **UNINITIALIZED — directory exists and is empty** | n/a |

**Flag:** the ruling's own text says "confirm evaluator `55bb0d0e`". Confirmed: `MNL`'s gitlink pins
`dclaborsupply-monorepo` at `55bb0d0e...`, which is **older** than the standalone
`dclaborsupply-monorepo` checkout's HEAD (`94c25f2...`, 2026-09-01 — note this standalone
checkout predates the `55bb0d0e` commit chronologically in these logs; it is a separately
managed clone, not the one MNL uses). All engine-code quotes in the source extract are taken
from `MNL/dclaborsupply-monorepo` at `55bb0d0e`, the version the ruling expects. The
`MNL_posfit` worktree's own `dclaborsupply-monorepo` submodule is **not checked out** — any
POSFIT-S12 code path that imports `dclaborsupply` from that worktree must be resolving the
package from an installed environment (e.g. a venv site-packages copy), not from that
in-tree submodule. This is a targeted escalation item, not resolved by this extraction.

## Status table

| Item | Path (exact, as found) | HEAD / commit | SHA-256 | Status |
|---|---|---|---|---|
| E3-EQ reporting | Not found. No `JMP_BASELINE_F1_equivalised_reporting_v1.md` exists yet anywhere under `Job_Market_paper` or `MNL`. | — | — | **NOT STARTED.** The E3-EQ workstream (equivalised reporting, ruling §"Parallel continuation — E3-EQ") has no output artifact yet. Related but distinct: an E3 *estimation* convergence exists at `MNL/outputs/p2a_singles2016/region_live_margqh_v1/e3_estimation_v2/attempts/...E3_CONVERGED_SINGLE_OPTIMUM` (2026-08-19) — this is the M08E E3 re-estimation, not E3-EQ equivalised reporting. Do not conflate. |
| E3-EQ verification | Not found. | — | — | **NOT STARTED** (depends on the memo above). |
| POSFIT-1R-S12 card, outputs, interim notice | `MNL_posfit/JMP_positive_fit_diagnostics_memo_v2b_addendum.md` (interim notice, v2b); `MNL_posfit/JMP_positive_fit_diagnostics_memo_v2.md` (parent v2 memo); outputs under `MNL_posfit/outputs/positive_fit_diagnostics_v2b/` and `.../v2/`; report `MNL_posfit/reports/JMP_positive_fit_diagnostics_v2b.html` | worktree HEAD `a2e80a82` | v2b addendum: `4002220a4c127404ff1169d7453354dc0aa7f1d250ba38d9bbc820b9fee8a2e4`; v2 memo: `c2dd032363e70de24fe31a2d3fff082c3e56aaa2ed44fbfe1dd3787619e8ba71` | **LIVE — current is v2b, matches the ruling's cited `a2e80a8`.** Confirmed by direct HEAD read of the `MNL_posfit` worktree, not a stale chat hash. |
| R5 draft | Not found as a standalone file. The dashboard names it explicitly: `JMP_counterfactual_attainment_design_v1.md`. | — | — | **NOT FOUND / NOT YET DRAFTED.** `Job_Market_paper/docs/Missions/JMP_current_state_dashboard_v1.md:39` states: "R5 (`JMP_counterfactual_attainment_design_v1.md`) is authorized to begin drafting from this acceptance onward; no counterfactual execution is authorized." No file of that name exists in either repo as of HEAD. The ruling's own text ("Preserve the existing R5 draft") presumes a draft exists; it does not — this is a discrepancy to flag upward, not resolve. |
| W1 latent-set identification note | `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | Job_Market_paper `cafe0ba0` | `8b02ff93b94a72327caa8d16476a3bf5c6176894162e0758f03562ee6329e226` | **LIVE.** Exact filename resolved: `W1_latent_set_identification_note_v1.md` (not the ruling's placeholder spelling), under `docs/normative/`. |
| JMP_W1_reference_domain_fork_v1.md + REC-1 corrections (r3) | `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | Job_Market_paper `cafe0ba0` | `00df1d8d5a5e42bf0186515311389f87370cbd06457251943286e3c91990474d` | **LIVE, REC-1 CLOSED.** REC-1 is not a separate file — it is a correction item tracked *inside* this memo and inside `JMP_W1_fork_ruling_v1.md`. Per the fork memo (lines ~17-21): the REC-1 reproduction script `docs/normative/scripts/fork_derived_numerals_v1.py` (sha `994c3dfaad7cbafd2f76871ac05629e0ee60947b5a00085f944a0bebe11d8e9c`) run against `docs/normative/fork_derived_numerals_v1.csv` (sha `2677356a555ec3eb65623227e3d26363925c2d11add1112c8db925213f77bf8e`) passes 158/158; "REC-1 / Deputy R3 item 2 is closed." |
| — companion ruling | `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | Job_Market_paper `cafe0ba0` | `7f5d26857d8a96174a9924848f65a02611944273d7775fdc52dc82364a818c05` | **LIVE.** Deputy FORK-1 implementation record; R3 items table (line ~61-67) shows item 2 (deterministic script) as the item REC-1 discharged. |
| JMP_measure_map_v1.md + JMP_measure_map_acceptance_v1.md | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md`; `Job_Market_paper/docs/normative/JMP_measure_map_acceptance_v1.md` | Job_Market_paper `cafe0ba0` | map: `6568ec53936c48fdafe4376714b6d2eaa8d37f30db040da25014773023534cc9`; acceptance: `45c45247246b9516945e4c196c60c0194f39f5dd0587d0de6e10524b5904bab3` | **LIVE, ACCEPTED** (title "MEASURE-MAP-1R ACCEPTED" per memory index; both files present and current at HEAD). Note a *separate*, differently-scoped `JMP_measure_mapping_memo_v1.md` also exists under `MNL/docs/jmp_methodology/` and inside two stale `.claude/worktrees/` copies in MNL — do not confuse the MNL methodology memo with the Job_Market_paper normative measure-map pair; they are different documents. |
| baseline_f1_verification_v1.md + the BASELINE_F1 ruling | `MNL/docs/corr/baseline_f1_verification_v1.md`; ruling at `Job_Market_paper/docs/normative/JMP_W1_BASELINE_F1_authorization_and_Cobs_ruling_v1.md` (byte-identical duplicate also sits at `Job_Market_paper/docs/JMP_W1_BASELINE_F1_authorization_and_Cobs_ruling_v1.md`) | MNL `b5550af5`; Job_Market_paper `cafe0ba0` | verification: `da7badf639f3d502d47b301558453d76501c9c44033ece3f17bde350bfd5e55f`; ruling (both copies, identical): `54dfd886e41d0a89c1056cbea5fa51e0a1294d3ca0813f938802bdc3dbd9ee0e` | **LIVE.** The verification memo states explicitly (line 22): "Units throughout are household EUR/month, **unequivalised**." This corroborates the "equivalence-scale e_i" NOT FOUND finding below. |
| ANY existing JMP_W1_stochastic_ability_set_bridge_v*.md | — | — | — | **NOT FOUND.** No file matching `*stochastic_ability_set_bridge*` exists in `Job_Market_paper` or `MNL`. This is the deliverable the ruling's §PRIORITY authorizes; it has not yet been started. |
| Accepted equivalence-scale definition e_i | — | — | — | **NOT FOUND.** No formula, constant, or named function for a per-household equivalence scale `e_i` (OECD-modified, square-root, or otherwise) exists in `MNL/scripts/welfare/` (`welfare_core.py`, `baseline_f1.py`, `run_baseline_f1_full_sample.py`) or in `MNL/docs/corr/`. `baseline_f1_provenance_v1.md:75` explicitly distinguishes the wage/consumption normalization constant `c_scale` from equivalisation and states it is "not equivalisation." `baseline_f1_verification_v1.md` reports everything **unequivalised**. This matches the ruling's own uncertainty in the E3-EQ instructions ("Locate the existing accepted scale e_i; escalate only this workstream if missing/conflicting") — escalate: no accepted e_i exists yet. |
| Current HEADs of MNL, Job_Market_paper, MNL_posfit, engine checkout | see HEADs table above | — | — | Reported above. |

## One-line list of ruling items that could not be located

- E3-EQ reporting memo and its verification memo (`JMP_BASELINE_F1_equivalised_reporting_v1.md` / `..._verification_v1.md`) — not started, no file exists.
- R5 draft (`JMP_counterfactual_attainment_design_v1.md`, per the dashboard's own naming) — not started, no file exists, despite the ruling's phrasing presuming a draft is in progress.
- Any existing `JMP_W1_stochastic_ability_set_bridge_v*.md` — not started, no file exists (expected, since this ruling is what authorizes drafting it).
- An accepted equivalence-scale definition `e_i` — no such definition exists anywhere in the two repos; current baseline outputs are explicitly unequivalised.
- The `dclaborsupply-monorepo` submodule inside the `MNL_posfit` worktree is present as an empty, uninitialized directory — the actual code path POSFIT-S12 uses at runtime is not resolvable from that worktree's tree alone.
