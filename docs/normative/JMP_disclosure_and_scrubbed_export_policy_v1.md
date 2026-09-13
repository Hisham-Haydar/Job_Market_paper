# JMP disclosure and scrubbed-export policy v1

| Field | Value |
|---|---|
| Card | DISCLOSURE-POLICY-1 (Deputy SEMINAR-PACK-1 §4) |
| Date | 2026-09-13 |
| Scope | Both repositories: `MNL` and `Job_Market_paper` |
| Nature | Forward-looking POLICY only. Record-and-verify precursor: DISCLOSURE-LOG-1 (`MNL/docs/corr/JMP_identifier_exposure_log_v1.md`). No file redacted, deleted, or rewritten by this document. No history rewritten. No push. |
| Disclosure discipline | Zero raw household-identifier values appear anywhere in this document. All patterns below are SHAPES (character classes / digit-length ranges), never literal matched strings. |

---

## 1. What counts as an identifier here

An "identifier" in scope for this policy is any of the following, as established empirically by DISCLOSURE-LOG-1:

- A **bare numeric household or person id** held in a column, JSON key, or free-text value, under any of the observed name variants: `uid`, `idhh`, `idorighh`, `stacked_hh_uid`, `idperson`, `source_idhh`, `source_idorighh`, `hh_id`, `household_id`, `household_uids`, `uids`, `anchor_uid`, or any per-project synonym. Digit-length varies by id namespace and all bands are in scope: 7 digits (`idhh`/`idorighh`/`source_idhh` family), 9 digits (`idperson` family, confirmed empirically at 9 digits — narrower than earlier working assumptions of 10–11), and 12 digits (`uid`/`stacked_hh_uid` family). A conservative scanning pattern therefore spans the whole range, e.g. `\b\d{7,12}\b`, applied per length-band rather than as a single fixed width.
- The **`20000_<uid>` compound "pooled key"** (and its `[1-3]0000_`-prefixed relatives, keyed by `year_tag`): a fixed 5-digit literal prefix followed by an underscore and a 9–12 digit household id. The literal prefix must be checked for (`20000_`, or the `[1-3]0000_` family) — a generic `\d{4,6}_\d{9,12}` shape is **not** safe to scan for on its own, since it collides with unrelated attempt-directory timestamp/hash naming conventions used throughout both repositories.
- An **identifier value embedded directly in a filename** (observed shape: `anchor_<label>_uid<12-digit-id>_<suffix>.<ext>`). A filename carrying an id is itself a disclosure channel independent of file content.
- A **hardcoded anchor-id literal or list in Python source** (observed pattern: `_[A-Z_]*UID[A-Z_]*\s*=\s*\d{7,12}` for a single constant, or `_ANCHOR_UIDS\s*=\s*\[...\]` for a list literal).

**Forward guards check column/key NAMES, not values — this is a real blind spot, not a hypothetical one.** DISCLOSURE-LOG-1 read the actual guard code added in MNL commits `d4616071`/`5b577bb9` (`_assert_no_household_identifiers` / `_assert_no_household_identifiers_obj` in the 10 patched `scripts/welfare/fastlane/*.py` scripts): it refuses a write only when a DataFrame column name or JSON key (case-insensitive) is a member of the fixed set `{idhh, idorighh, idperson, source_idhh, stacked_hh_uid, household_uids, uids, uid, hh_id, household_id}`, and it exempts any destination path containing a component literally named `restricted`. It does not inspect the *contents* of any column at all. Consequently, a compound-key or bare-id value written under an unlisted or renamed column (e.g. `pooled_key`, `f4a_key`, `hh_ref`) would pass the guard silently. Two of the ten guarded scripts additionally refuse a filename containing a 9+ digit run, but this filename check exists in only those two scripts, not the other eight, and not outside the fastlane family at all. Anyone relying on this guard as a complete content-level control is relying on it for something it does not do.

---

## 2. Forward rule

**No identifier value, in any of the forms in §1, may appear in any newly committed artifact — source code, data output (parquet/CSV/JSON/log), filename, or log file — in either `MNL` or `Job_Market_paper`, going forward, from the date of this policy onward.** This applies regardless of whether the destination path, column name, or script is currently covered by an existing name-based guard. Where a script must legitimately handle raw household identifiers as *input* (reading restricted-store or EUROMOD source data), it must not write them back out to any git-tracked path; the guard's own `restricted`-path exemption is the sanctioned place for such intermediate values to live, and only there.

---

## 3. History

**Committed history is explicitly NOT rewritten by this policy or by DISCLOSURE-LOG-1.** No `git filter-repo`, `rebase`, force-push, or historical file deletion is authorized by this document. The reason is structural, not a matter of convenience: a registry of pinned-SHA citations exists across both repositories — the CLEAN-B hash-registry pattern used by rulings documents, gate files, and decision notes (e.g. `M6_RULINGS_SHA` in `MNL/scripts/loc4/run_loc4_stage2_comparison.py`, the HK01 inventory/disposition registers, `JMP_measure_map_v1.md`, `JMP_repo_inventory_v1.md`, and multiple execution-contract versions) — and these depend on stable, unrewritten commit history to remain valid provenance chains. Rewriting history to remove exposed commits would silently invalidate every one of those pinned citations.

**This is a provenance decision only. It does not discharge any institutional or data-use obligation.** Whatever compliance requirement applies to the underlying household microdata — IRB approval, a data-use agreement, an ethics-committee condition, or any other institutional rule — is a separate, unresolved matter. This document takes no position on whether that obligation has been met, and does not claim to satisfy it. Leaving history unrewritten for provenance reasons is not equivalent to, and must not be read as, a determination that the historical exposure is compliant or acceptable.

---

## 4. Shareable-export rule

Any export of this work intended for a party outside the immediate working environment (a co-author, a seminar audience, a journal, a public repository mirror, a cloud drive) must be built **only** from cleared aggregate or synthetic assets. Concretely, a shareable export must contain:

- **No household-level table.** Row-level data keyed by any identifier in §1's scope is excluded outright; only aggregate/summary statistics (counts, means, quantiles, Gini/Theil/Atkinson-type summaries, model coefficients) or fully synthetic illustrative data may travel.
- **No crosswalk file.** The identifier-to-label mapping (§5) never leaves the restricted store under any circumstances, including inside a "for reference only" export.
- **No identifying filename.** A filename containing an embedded id (per §1's filename pattern) is itself a disclosure and must be renamed or excluded before export — renaming the file does not require touching its content, but the original identifying name must not appear anywhere in the exported tree, including in manifests or file listings that reference it by its original name.
- **No `.git` directory.** A shareable export must never include a `.git` folder copied or zipped from either repository, since that carries the complete commit history — including every historical commit that DISCLOSURE-LOG-1 found to expose identifiers (which, per §3, is not being rewritten). Copying working-tree files without their `.git` history is the only safe export mechanism.

## 5. Restricted-store retention

The label-to-identifier crosswalk (the H-S1 / H-C1 / H-S2 scheme established by SANITISE-1, `Job_Market_paper/docs/normative/JMP_household_identifier_sanitisation_decision_v1.md`) lives outside git entirely, in the restricted store on `EUROMOD-STORAGE`, alongside the CLEAN-A cleanup quarantine:

- `C:/Users/hisham/MNL/EUROMOD-STORAGE/restricted/id_sanitisation_crosswalk_2026-09-12/household_id_crosswalk_v1.json` — the label-to-identifier mapping itself.
- `C:/Users/hisham/MNL/EUROMOD-STORAGE/restricted/id_sanitisation_crosswalk_2026-09-12/originals/` — byte-exact pre-sanitisation copies of files that were relabelled or removed from the forward tree (e.g. the full-sample `n4_fastlane.csv`, quarantined here before its removal from `Job_Market_paper`'s tracked tree).
- `C:/Users/hisham/MNL/EUROMOD-STORAGE/restricted/cleanup_quarantine_2026-09-12/` — the broader CLEAN-A quarantine of untracked, zero-history files.

**This mapping must never be committed to either repository, under any branch, at any time.** Regenerating derived evidence from restricted inputs (e.g. re-running the bridge fastlane pipeline) will write raw identifiers back into its output by construction; any such regeneration must re-apply the SANITISE-1 labels before the output is committed, and the forward rule in §2 applies to that regenerated output exactly as it does to anything else.

## 6. Escalation line

Whether the historical exposure documented in DISCLOSURE-LOG-1 requires institutional notification, remediation of already-pushed content, or any other compliance action is a decision for the **PI and the data steward**, not for an agent or a Claude Code session operating unilaterally. This document does not authorize, recommend, or perform any such remediation. Its scope is limited to (a) stating the forward rule in §2, (b) explaining why history is not being rewritten (§3), and (c) defining what a compliant shareable export looks like (§4–5). Any decision to rewrite history, request removal of already-pushed content from GitHub, or notify an oversight body must be escalated to and made by the PI/data steward, and is explicitly out of scope for this card.
