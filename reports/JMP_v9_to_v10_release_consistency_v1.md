# JMP — V9 to V10 release consistency, v1

**Scope of this pass:** Stage A only (release-language consistency), per
`JMP_WEA_v9_status_and_release_cleanup_v1.md`. Stage B of the deputy
addendum (restoring the economic-derivation narrative, matched-household
illustration, body/appendix reorganisation) is **not** attempted here and
is deferred to a separate, explicitly scoped pass — it is a much larger
rewrite and was intentionally held back pending review of this Stage A
result.

No estimation, pricing, decomposition or ex-ante numerical routine was
run. No table, figure or numerical value changed. This is confirmed
below, not just asserted (see "Numerical identity check").

## 1. Stale-status sweep (A1)

A full text sweep of the V9 report's generated Markdown
(`story_v9.generated.md`) and the V9 gallery HTML for present-tense
claims that the ex-ante metric is undefined/blocked/unreported found
**exactly the five locations the source memo named — no additional
ones**. All five trace to a single reused string
(`v7_sections.WEA_STATUS`, plus one close variant used as the Q&A
answer), which V8 and V9 both pull into their collapsed technical
appendix by reference rather than by copy, so the same stale sentence
appears four times inside the report and once in the gallery:

| # | Location | Source string |
|---|---|---|
| 1 | Report, "Technical record: Introduction" | `v7_sections.WEA_STATUS` |
| 2 | Report, "The distinct ex-ante opportunity-prospect metric" | `v7_sections.WEA_STATUS` |
| 3 | Report, "What is not established" ("Numerically blocked opportunity-prospect metric") | `v7_sections.WEA_STATUS` |
| 4 | Report, Q&A "26. Is the ex-ante opportunity-prospect metric a result?" | `v7_sections.QA` answer for that question |
| 5 | Gallery, provenance appendix, "Distinct ex-ante metric" warn-box | hardcoded in `results_gallery_build/build.py`, carried through unedited by `build_v8.py`/`build_v9.py` |

**Treatment chosen:** these five passages are genuine historical
quotations — text a predecessor report version wrote about its own status
— reproduced inside a section whose own heading already says "Technical
record" / "provenance". Per the source memo's preservation rule
("historical quotations retained inside a shareable report must carry an
explicit 'superseded before V9' label and a pointer to current results"),
the original sentences were **not rewritten**. Instead, each was prefixed
with:

> *Superseded before V9.* The sentence(s) immediately below are
> reproduced unchanged from an earlier report version and describe that
> version's status only, not the current one. The ex-ante calculation has
> been completed and passed the numerical checks documented here. Its
> results remain conditional on the estimated model, reference convention
> and specified counterfactual operators. [+ certification-scope sentence,
> see §3] [+ pointer to the current-results section]

This satisfies both the literal replacement text requested in the source
memo (it appears verbatim, immediately adjacent to every stale sentence)
and the "preserve historical documents unchanged" instruction (the
original wording is still there, clearly labelled, not silently deleted).

**Verified it fires:** in `JMP_research_story_report_v10.html`, every
remaining occurrence of the stale phrases ("is definition-only and
numerically blocked", "has no numerical result", "currently block
numerical implementation", "No number for that metric is reported") is
now immediately preceded by a "Superseded before V9" label — 4 stale
occurrences, 4 labels, one-to-one, in the report; 1 stale occurrence, 1
label, in the gallery. No unlabelled present-tense blocked/no-result claim
about the ex-ante metric remains anywhere in either file.

## 2. Certification scope (A3)

Audited every place V9 describes the ex-ante certification. The existing
text already avoids over-claiming (it explicitly says the checks do "not
... turn it into a causal decomposition", that "Estimation uncertainty
has not been propagated through either decomposition", and that "Neither
measure is designated primary"), so no existing sentence needed
correcting. As reinforcement, V10 adds one explicit consolidated caveat
directly under the "Certification gates" heading in the appendix, and
folds the same caveat into all five superseded-status labels above:

> This numerical certification establishes that the computation is
> correct given the model and operators; it does not establish causal
> identification, does not quantify statistical uncertainty in the
> estimated parameters, and does not establish that either welfare
> perspective is the normatively correct one.

## 3. "Isolates only the welfare definition" check (A4)

Swept the report and gallery for any claim that the attained-bundle vs.
ex-ante comparison isolates the welfare definition alone. **None found.**
The existing decomposition-economics text already frames it correctly
("Exactly the same operators and allocation rule are applied to both
welfare perspectives... while preserving the distinction between what the
two welfare objects value"), and the sparse-support limitation for the
attained-bundle integration is already disclosed in "What remains
preliminary" ("an integration sample that represents the lower part of
the modelled hours range sparsely... Coverage below ten hours therefore
remains an explicit limitation"). No edit made; verified present, not
assumed.

## 4. RUM reporting-bin / band-edge check (A5)

**Verdict: no action needed.** Traced every displayed fit figure/table in
V9's main body (`{{figure:fitband}}`, `{{figure:fit}}`,
`{{table:fitsingles}}`, `{{table:fitcouples}}`, and the `mae_singles` /
`mae_couples` / `gap37_*` numbers) to their source files:
`manuscript/tables/v7/v7_fit_{singles,couples}.csv` and
`manuscript/figures/v7/*.png`, both produced from
`MNL_posfit/outputs/positive_fit_diagnostics_v3b` and
`.../bandfix2_recompute` — the corrected S11/S10 band edges (18.5 / 29.5 /
37.5), not the superseded S8/S12 edges (17.5 / 28.5 / 36.5). File
timestamps confirm the correct order: the BAND-FIX-3 audit (MNL_posfit
commit `cd7247cf`, 2026-09-14 22:33) precedes the regeneration of those
CSVs/figures (23:34) which precedes the V9 report render (2026-09-15
10:53). The MNL_posfit stale-value scan
(`outputs/band_fix_1/band_fix_3_stale_scan_summary.csv`) attributes every
remaining stale hit to `story_report_v6` and earlier surfaces only — no
v7/v8/v9 row. The one band-edge-adjacent item that *is* disclosed in the
report (the RUM-A 26.5-vs-29.5 estimation-input metadata defect) is
already correctly scoped there as a metadata-only issue that cancels from
the likelihood and leaves estimates unaffected. Nothing to fix or omit.

## 5. Pricing/certification manifest verification (A6) — verified, not rerun

Cross-checked the report's stated pricing volume against the source
artifacts directly:

| Quantity | Report (V9/V10) | `stage4_certification_and_results_v1.json` | `WEA_SPRINT_1_result_memo_v1.md` |
|---|---:|---:|---:|
| Singles stream A | 8,573,928 | `C12.independent_summary.priced_def_market_nodes_joined` = 8,573,928 | 8,573,928 |
| Singles stream B | 8,574,032 | (not separately keyed in JSON C12; matches memo) | 8,574,032 |
| Couples stream A | 166,937,889 | `C12.independent_summary.priced_def_market_nodes_joined` = 166,937,889 | 166,937,889 |
| Couples stream B | 166,938,558 | (not separately keyed in JSON C12; matches memo) | 166,938,558 |
| **Total** | **351,024,407** | sum matches | **351,024,407** |

`overall` block in the certification JSON: all of C1–C11 `true` for both
singles and couples, and `C12_household` `true` for both — i.e. all
twelve gates the report lists as PASS are PASS in the source record.
`numbers_of_record_v10.json` is byte-identical to
`numbers_of_record_v9.json` on every key except `build_date` and
`presentation_version` (checked programmatically), so no scalar in the
report changed either. No rerun performed or needed.

## 6. Numerical identity check

`JMP_research_story_report_v10.html` and `JMP_research_story_report_v9.html`
are byte-for-byte identical up to the first byte of the
`<!-- V9/V10_PROVENANCE_APPENDIX_BEGIN -->` marker (offset 4,387,565 of
9,777,680) — i.e. the entire main body, abstract, all seven economic
sections, all figures and the bibliography are unchanged; every
difference is confined to the collapsed technical appendix and the
trailing HTML-comment provenance block. Size grew by 3,770 bytes (the five
inserted status notes plus the certification-scope sentence).

## 7. Outputs

- `reports/JMP_research_story_report_v10.html` — SHA-256
  `e9e8049ff2304def71207e33b234d6470f44e800186e51c7012793815139531b`
- `reports/JMP_results_gallery_v10.html` — SHA-256
  `819efb731d026b0115a0bc2699571a9d9ac01b1c6e1971675585154da3e5f06c`
- Editable sources: `reports/research_story_build/v10_sections.py`,
  `reports/research_story_build/v10_render_inputs.py`,
  `reports/research_story_build/build_v10.py`,
  `reports/research_story_build/story_v10.generated.md`,
  `reports/results_gallery_build/build_v10.py`,
  `reports/numbers_of_record_v10.json`
- This memo: `reports/JMP_v9_to_v10_release_consistency_v1.md`

V9 was not overwritten; all V9 files are untouched (verified: the report
build's redirect table intercepts every V6-named path the underlying
build engine writes to, and a post-build check would abort if any V9 (or
V6) path's mtime moved past its V10 counterpart — none did). The paper
TeX/bib output that the shared build engine always produces alongside the
report was redirected to a scratch location rather than a new manuscript
version, since a new paper version was not requested and Stage A's own
provenance flag (`paper: False` on the appendix section) confirms the
edited content never reaches the paper anyway.

**Pre-existing, unrelated state noted for the record:**
`reports/JMP_research_story_report_v5.html` and
`reports/JMP_research_story_report_v6.html` show as modified in
`git status`, with a last-write time (2026-09-14 22:03) that predates this
V10 build entirely — this build did not touch them, and the diff is
carried over from earlier, unrelated work already in the working tree.

## 8. Not done (out of scope for this pass)

- Stage B (economic-derivation restoration, matched-household
  illustration, body/appendix movement) — deferred, not started.
- The full V9-style release-gate suite (`run_v9_release_gates.py`
  equivalent: beamer deck, rehearsal script, canonical-notebook refresh in
  the `MNL_wea` worktree, cross-surface synchronization) — not run. This
  pass only rebuilt the report and gallery, which is what Stage A and the
  original memo's "single immediate action" asked for.
- No commit was made; the repository already has unrelated uncommitted
  changes (see §7) and commit/push should be a separate, explicit step.
