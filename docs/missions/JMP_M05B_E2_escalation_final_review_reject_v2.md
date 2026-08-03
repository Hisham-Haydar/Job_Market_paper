# JMP-M05B E2 Escalation — Final Review REJECT v2

**Mission:** JMP-M05B — Phase-5 Inference Implementation and Certification
**From:** Goal 1 Manager — Empirical JMP  **To:** ChatGPT Deputy Programme Director
**Date:** 2026-08-02
**Halt trigger:** review v3 REJECT after the final authorized remediation cycle (deputy decision v1 §3: no third cycle exists; Goal-1 R-25 pre-registered E2 on any non-APPROVE)
**Target repository path:** `docs/missions/JMP_M05B_E2_escalation_final_review_reject_v2.md`

## 1. State at halt

Remediation cycle 2 implemented all ten review-v2 correction groups; the Goal-1 screen verified the fix signatures; review v3 (Codex, fresh session, read-only) verified the exact state precisely — correct inventory, no residue, nested clean at `27756a06…`, MNL base `983a2ecf…` — treated remediation report v2 as claims to test, and returned **REJECT: 15 of 51 gates fail**. Nothing has ever been committed; the full Phase-5 working set is preserved uncommitted; the test-42 fix remains logically separate and committable when authorized; no household-level score bytes have ever existed; the store is empty; the parser provably refuses this negative verdict (fail-closed re-confirmed).

## 2. Honest convergence analysis

Progress across rounds is real, not illusory: v1 (REJECT, 12 fixes) → v2 (APPROVE AFTER FIXES, 10 narrower fixes, 16 failed gates) → v3 (REJECT, 15 failed gates collapsing to 8 residual defects / 7 fix groups). Most v2 failures now pass — ancestry discovery, parameter-map binding and tamper refusal, T-12 member closure, publication atomicity, the optimizer guard. Statistical design and package boundary have passed in every round; no defect has ever touched design v4, D-1–D-8, or any constant.

The v3 failures sit one layer deeper each time: this round, the import-callable Python route (`_phase5_contract` + `_phase5_evaluate` with an in-memory config computes the full score without gates), a STOPPED-rename TOCTOU, absent post-evaluation reauthentication in the T-12 child, STOPPED-inventory truthfulness, one lifecycle-invalid guard test, and two documentation remnants. Each reviewer standard was defensible under §4 fix 1's "every process capable of computing the full score matrix" — but that criterion is unbounded so long as gating is applied surface-by-surface. The recurring authorization class will not converge under enumeration; it converges only structurally.

## 3. Requested deputy decisions

1. **Authorize one further bounded remediation with an architectural directive** (this is the deputy's to grant; the mission's own budget is spent): restructure so that full scoring is reachable **only inside one gated process entry** — review v3 fix 1's second branch — making every other route structurally incapable of producing scores (e.g., the scoring callable requires an unforgeable token constructible only inside the gated entry after all authorization/custody gates pass). Plus the six remaining narrow groups (STOPPED-rename revalidation; T-12-child post-evaluation reauthentication; truthful STOPPED inventory incl. directories/junctions/partials; behavioral integration tests for the new refusal classes; lifecycle-aware exact working-set assertions valid in all three states; stale v2 help text and the last comparator description corrected to R-23b-rev).
2. **Close the acceptance criterion in the same decision:** the follow-on review must begin from a pre-committed exhaustive enumeration of full-score-capable surfaces under the new architecture (expected: exactly one), so approval is a closed-form check, not an open search. If the reviewer finds any second surface, that is an automatic REJECT — otherwise the authorization class is settled by construction.
3. **Rule on reviewer continuity** for the follow-on review (same Codex role; fresh session; the enumeration requirement above bounds scope drift in both directions).
4. Alternatively: restructure or pause the mission. The Goal 1 Manager recommends option 1+2 — the defect class is real, the remedy is known, the statistical core has been stable throughout, and the marginal work is one architectural refactor plus six narrow items.

## 4. Repository state

MNL `983a2ecf…`: modified `.gitignore` + test-42 fix; untracked Phase-5 set + reviews v1/v2/v3 + five reports. `Job_Market_paper` `7195fc50…` clean (+ registered untracked mission instruments). Nested clean at gitlink. Both bundles rehash. No `complete/`; no Phase-5 output root; store empty. Retention warning and replication-ACL tension remain queued for the pre-real-run gate.
