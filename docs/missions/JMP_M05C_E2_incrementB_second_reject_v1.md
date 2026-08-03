# JMP-M05C E2 Escalation — Increment B Second REJECT v1

**Mission:** JMP-M05C — Minimal Streaming Inference Implementation
**From:** Goal 1 Manager — Empirical JMP  **To:** ChatGPT Deputy Programme Director
**Date:** 2026-08-03
**Halt trigger:** standing rule 3 hard limit — second REJECT for the same increment (Review B v2), remediation and conversion budgets both spent.

## 1. State at halt

MNL HEAD `92e299de…` (Increment A committed), Increment-B working set frozen uncommitted: module, tests, report v1, refix report, reviews v1 and v2. Nested clean at `27756a06…`; attempts/ = 70; bundles rehash; Increment-A files untouched with tests green; no commit, no full-population run, no persistence event has ever occurred.

## 2. Review B v2 outcome — substantial partial closure

The six review-v1 adversarial examples all now reproduce as claimed and all twelve updated PROOFS pass. Fix-by-fix: **T-5 theta-byte authentication PASS** (one-byte flip fails exactly the right arm); **authoritative-gradient (R-37b) PASS** including the poisoned-CSV invariance construction; **PROOF corrections PASS**. Three FAIL as partial: **T-22** rejects all review-v1 forgeries but exposes a caller-overridable `active_names` parameter, so a forged name set can still satisfy the gate; **inference_grade (R-37a)** propagates on success paths but the serializers validate emptiness only after writing, so refusal does not leave the destination untouched; **serializer contracts** now refuse the review-v1 cases but `write_score_aggregate_summary(extra=...)` accepts arbitrary content — including a temporary 5×37 score block — and can overwrite protected payload fields. The reviewer classifies all three as required-contract defects, with residual 3 touching the no-row-persistence contract (PI disclosure determination), not merely gate hygiene. The numerical core is unchanged and sound; no economic or econometric element has failed in this or any prior review.

## 3. Requested deputy decision

**Option (a) — recommended: test-first closure.** Authorize one final Increment-B closure cycle in which the fix specification IS executable: the Review-B-v2 reviewer supplies its three probes as ready-to-run failing test functions (forged `active_names` call; refusal-leaves-no-file check; `extra=` score-block/field-overwrite probes); the implementer makes exactly those tests pass with no gate weakened, no schema or constant changed, and a mechanical hunk map; a decisive binary re-review verifies test provenance (unmodified probes) plus regression. This converts boundary-closure from open-ended instruction to closed-form target — the mechanism that ended the M05B spiral — and is plausibly one short cycle.

**Option (b) — calibration alternative for explicit decision:** accept Increment B with residuals 1–2 recorded as known limitations (rationale: all execution flows through the gated runner operated solely by the PI; the marginal scientific value of further hardening is zero), while residual 3 remains blocking in any variant, since an `extra=` channel that can persist score bytes contradicts the PI's EU-SILC disclosure determination directly. The Goal 1 Manager recommends (a) and notes the principal investigator's proportionality view should inform the choice.

## 4. Disclosure

Increment B consumed its standing-rule-3 conversion (first REJECT converted 2026-08-03, disclosed per the rule); Increment A previously closed via deputy-authorized refix. Whichever option is chosen, the remaining pipeline is unchanged: Increment C (runner/transaction/reproduction), Review C, final integrated review, one aggregate-only dry run, Goal-1 audit, deputy packet.
