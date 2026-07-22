# JMP Open Decisions — Cross-Repository — v1

Read-only. Date: 2026-07-22. Companion to `JMP_cross_repo_manager_handoff_v1.md`.

Decisions are grouped by priority horizon. "Central now" items block the immediate critical path.
This document proposes and sequences decisions; it does not make them, does not change the active
baseline, and does not authorise welfare.

---

## A. Central now (block the critical path)

**A1. Production rebuild of the FR-2016 singles P2a region-live fit — the single next gate.**
Rebuild the region-live fit (negLL 19053.4655) through the reusable `dclaborsupply` package/exports
path, not a notebook, and emit the full committed artifact bundle: engine-ready `_v2` provenance,
theta CSV, estimation JSON, optimizer status, gradient, **PD Hessian with eigenvalues / rank /
condition number**, cluster-robust SE (idorighh), post-estimation report, a committed producing
script, and a verified cold-reload anchor at 19053.4655.
*Why central:* region-live currently exists only as a notebook cell + a propagated artifact set from
a **missing** script, has **no** strict diagnostics, and its numbers already flow into committed
welfare outputs. Decision: **authorise the rebuild gate; do not promote until it passes.**

**A2. Region × urbanisation joint-identification decision.**
Region-dead showed five near-zero eigenvalues loading on the region block (a flat direction under the
zero-stub wiring bug). The rebuild (A1) must show whether reviving region/urb/gsur lifts that flat
direction (PD Hessian, finite condition number, full rank on the 10 regional params) or whether the
region block remains weakly/under-identified. Decision to make **after** A1: keep all 10 regional
params, or reduce/regularise the region block.

**A3. Documentation-repair authorisation (parallel to A1).**
Approve the staleness-audit repairs (rewrite Job_Market_paper `CLAUDE.md`/`README.md`/`JMP.md`;
MNL `RURO_ACTIVE_RESULTS_REGISTRY.md`/`README.md`; repair `P2A_MASTER_RECORD.md`, the
`p2a_fit_provenance.json` theta pointer, and the corrupted lines). *Why central:* these actively
mislead any AI/RAG reader about whether the model is estimated and what the baseline is. Low risk,
high clarity payoff. Decision: **authorise archival/rewrite per §8 of the staleness audit.**

**A4. Locate or reconstruct `propagate_regionlive.py`.**
The script that produced the committed region-live artifacts is absent from both repos (no git record).
Decision: **recover it or fold its logic into the A1 production rebuild** so region-live is reproducible.

## B. Useful later (after the region-live gate)

**B1. P2a welfare re-examination.** The P2a welfare/inequality outputs (Gini W1 0.176 / W4 0.261;
W4 median compensation 8505 EUR, +95% vs region-dead) were computed on the un-rebuilt region-live
theta. After A1, re-run and re-certify (or not) on the rebuilt theta. Do **not** treat current welfare
numbers as findings. Welfare readiness remains **undeclared**.

**B2. Baseline relationship of the singles-2016 track.** Decide the formal role of FR-2016 singles P2a
relative to the pooled 2015–2017 certified baseline: robustness slice, year-specific companion, or an
input to a singles-specific welfare exercise. It is **not** a replacement for the pooled baseline.

**B3. `gsplit` disposition.** The 49-param gender-split relaxation is rejected on synthetic ID
(tight-SE bias). Decide whether to (a) shelve it as a documented negative result, or (b) attempt a
less-aggressive split with a pre-registered synthetic re-gate before any real-data use.

**B4. Provenance-JSON standard.** The certified baseline has no standalone provenance JSON (provenance
lives in an execution-log markdown). Decide whether to emit a machine-readable provenance sidecar for
the baseline to match the P2a track's format.

## C. Deferred extensions

**C1. Welfare decomposition (Exercise B).** Shapley–Shorrocks access/ability/preference decomposition —
designed in `JMP_welfare_spec_v5.md`, not implemented. Deferred until welfare measurement (Exercise A)
is certified on a rebuilt baseline and the thin-ESS / EUROMOD reprice-parity blockers are cleared.

**C2. Full W¹–W⁶ family as headline.** Gated (per the welfare spec) behind an empirically observed
inequality spread across measures; deferred until welfare is certified.

**C3. Cross-country / cross-year generalisation.** The estimator is intended to be country/year/spec
agnostic (a publishable package). The DE-2017 pricing pilot is feasible but distinct from FR wiring.
Deferred until the FR singles track is settled.

**C4. `dclaborsupply` app hardening.** `france/gsur.py` is a placeholder stub; `loc_empirical` /
`vw_occupation` are parser-recognised but have no JAX implementation (must not be used structurally).
Promote these from stubs to tested implementations only when a downstream need is confirmed.

## D. Directions not worth pursuing now

**D1. Promoting region-live on the improved likelihood alone.** Explicitly out of scope — an improved
likelihood and a (currently absent) PD Hessian are not sufficient for promotion; the rebuild gate (A1)
is the only path.

**D2. Reviving the legacy GAMSPy/CONOPT, continuous-RURO or job-choice branches.** Superseded by the
certified JAX baseline; do not re-open. Keep archived for provenance only.

**D3. Editing `fr_singles_pipeline_v1.ipynb` to "add" region-live.** The region-live work belongs in a
production rebuild (A1), not in another notebook. Add only a header note that the pipeline notebook is
region-dead (staleness audit §8.9).

**D4. Country-ranking framing.** The contribution is explicitly not a country ranking; do not drift the
research question toward one.

**D5. Any welfare-readiness declaration.** Not now, under any of the above.

---

### Decision sequencing (one line)

**A3 + A4 immediately and in parallel → A1 (the gate) → A2 → B1/B2 → the deferred extensions.**
Nothing in B/C/D proceeds until A1 passes.
