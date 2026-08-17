# JMP-M08 E2 Ruling — Parity Report v3 Documentary Correction

**Programme:** Goal 1 — Empirical JMP  
**Decision-maker:** Deputy Programme Director  
**Date:** 2026-08-06  
**Status:** Binding E2 disposition  
**Issue:** Second narrow-review REJECT after the permitted Rule-3 conversion  
**Classification:** Documentary claim-to-evidence defect only  
**Numerical gate:** Accepted as earned, subject to this documentary closure  
**New execution:** Prohibited

## 1. Decision

Authorize one exceptional, bounded documentary correction producing:

`docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v3.md`

Authorize one narrow re-verification of exactly the two residual R3 items.

On an `ACCEPT` verdict, the Goal 1 Manager may:

- accept report v3 as the parity-gate report of record;
- freeze the M08 Stage-A execution contract;
- continue the M08 critical path without further deputy contact.

No gate rerun, code change, EUROMOD execution, artifact regeneration, or general review cycle is authorized.

## 2. Basis

The narrow re-verification independently accepted:

- the T4 comparator correction;
- the witness non-finiteness treatment;
- the new attempt's earned numerical verdict;
- artifact binding and production geometry carried from the prior review.

Its sole remaining rejection concerns two numerical statements in report v2 that are not traceable to the new attempt's packet:

1. a projected-runtime statement;
2. a three-execution determinism statement.

The rejection is therefore evidence-integrity/documentation only. It does not reopen the production path or numerical parity result.

## 3. Exact authorized corrections

Report v2 remains immutable history.

### 3.1 Runtime statement

In §3, replace:

> “Projected and realised runtime was ~19 minutes for the complete grid…”

with a new-attempt-only statement:

> “Realised elapsed time for the complete grid was 19 minutes 20 seconds; no chunk was sampled, truncated, or deferred.”

The realised elapsed time must cite the attempt-of-record manifest's `started_utc` and `finished_utc`. The full-grid statement must cite the manifest's requested grid, full-run flag, and eight-chunk result.

Delete every statement about projected runtime, runtime-guard estimates, or an ex-ante cost decision from packet-only §§3–4.

Do not move the projection into a non-packet section. It is unnecessary to certification.

### 3.2 Determinism statement

Delete the fifth support item in §4.4 that claims:

- three independent executions establish determinism;
- each returned `0.0` against the same stored chunk;
- they therefore returned `0.0` against one another.

Replace it with:

> “The certification verdict rests solely on the attempt of record and its eight chunk JSONs. Earlier attempts are retained as code-lineage and procedural history only and do not provide numerical support for this verdict.”

The historical attempt table in §5 may remain, provided it is clearly lineage/history and not used to support the certified numerical result.

Do not cite the pre-fix comparator attempts as evidence of pairwise numerical equality or determinism.

### 3.3 Supersession and change declaration

Report v3 must state:

- it supersedes report v2;
- report v2 remains immutable history;
- only the two E2 documentary corrections in §§3.1–3.2 were made;
- the attempt of record, packet, code, comparator, tolerance, statistics, and verdict are unchanged.

## 4. Required correction outputs

Create:

1. `docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v3.md`
2. `docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v3_change_log.md`

The change log must contain:

- the exact old text;
- the exact new text;
- the source field for every retained numerical value;
- a diff summary confirming no other substantive change.

## 5. Narrow verification

Preferred reviewer:

- **Tool:** Codex
- **Model:** GPT-5.6 Codex
- **Mode:** read-only
- **Reasoning:** High

Permitted substitution if Codex quota is unavailable:

- **Tool:** ChatGPT Pro Thinking
- **Model:** GPT-5.6 Thinking
- **Reasoning:** High

The reviewer examines only:

- E2-1: projected-runtime claim removed and realised-runtime claim traced to the new manifest;
- E2-2: three-run determinism/pairwise-equality claim removed from the certification case;
- E2-3: prior attempts retained only as lineage/history;
- E2-4: no other substantive, numerical, gate, code, or interpretation change between v2 and v3.

The reviewer must not:

- rerun code;
- reopen T1–T6;
- reconsider the T4 fix;
- review general style;
- expand into software architecture;
- demand a new EUROMOD execution;
- introduce new certification requirements.

## 6. Verdict and return rule

### ACCEPT

On `ACCEPT`:

- create `docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v3_acceptance.md`;
- make report v3 the report of record;
- retain v1/v2 and all attempts as history;
- proceed to Stage-A freeze without deputy contact.

### REJECT

A `REJECT` is valid only if one of E2-1 through E2-4 fails.

Any valid REJECT returns to the deputy. The Goal 1 Manager may not authorize another correction.

An observation outside E2-1 through E2-4 is recorded as out of scope and does not block acceptance.

## 7. Repository and commit discipline

The documentary correction may be committed with the already accepted parity code and evidence only after the narrow verification accepts.

Recommended commit separation:

1. parity code/evidence/report-v3 checkpoint;
2. M08 contract freeze checkpoint, if repository discipline requires separation.

Do not mutate the accepted attempt directory.

## 8. Infrastructure note

The proposed merger of `Job_Market_paper` and MNL is deferred until after M08. No repository migration is authorized during the mission. The current split protects hash-pinned paths, accepted manifests, and the public-versus-restricted disclosure boundary.
