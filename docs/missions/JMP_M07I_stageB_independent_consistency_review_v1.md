Verdict: PASS WITH REQUIRED CORRECTIONS
Correction count: 5

# JMP-M07I Stage B — Independent Consistency Review

## 1. Verdict

**PASS WITH REQUIRED CORRECTIONS**

The v2 identity set has successfully changed the paper-facing empirical baseline to **France 2016 single-adult households, P2a region-live specification, 1,555 households**. No document presents couples or pooled 2015–2017 estimates as the current application, and no surviving statement depreciates the singles application as obsolete or provisional. This satisfies the central empirical-identity ruling.

The review nevertheless identifies five narrow corrections. Two concern exact evidence wording, one concerns an incorrect attribution to the M08 handoff, one concerns the incomplete project-state verification, and one concerns the recorded scope of the literature-positioning residue.

## 2. Identity findings

### 2.1 Sole paper-facing application

All four v2 documents identify the current application consistently as France 2016 single-adult households under the P2a region-live specification, with 1,555 household observations:

* the abstract names this application directly;
* the core packet makes it the sole baseline and writing anchor;
* the extended abstract makes it the accepted empirical setting;
* the introduction skeleton requires the same formulation in the France-design paragraph.
  No couples-baseline, pooled-baseline, singles-fallback, or singles-obsolescence language survives in the four documents.

### 2.2 Couples and pooled-year references

The remaining references fall within the categories authorized by the deputy:

1. the staged extension to couples and pooled years;
2. the technically necessary explanation of eight pinned couples-leisure coordinates;
3. governance prohibitions against presenting couples or pooled years as delivered results.

The retained pinning statement is technically correct. The accepted parameter vector contains 47 coordinates; eight couples-leisure coordinates are pinned because the singles objective does not reference them, and two year-dummy coordinates are pinned because their covariates are identically zero in the 2016-only sample. These ten pins leave 37 free coordinates, of which two are at active upper bounds and 35 are interior.

### 2.3 Staged-extension formulation

The substance is consistent, but the wording is not identical across the documents.

The abstract reproduces the deputy-authorized sentence exactly:

> The empirical analysis first establishes the complete estimation–welfare–decomposition pipeline for France 2016 single-adult households; extension to couples and pooled years is subsequent work.

The extended abstract substitutes “these households,” adds “to” before pooled survey years, and adds a validation condition. The introduction uses a comma and “and” rather than the authorized semicolon construction. The core packet uses only the extension half and adds a validation condition. Because this audit specifically requires identical staged-extension framing, these variants require correction. The deputy ruling already supplies the controlling sentence.

## 3. Evidence findings

### 3.1 Numerical fidelity

The paper-facing numerical statements are faithful to the accepted inference section:

* 1,555 household observations and 1,555 clusters;
* finite-sample correction `1555/1520`;
* 47 coordinates, 10 pinned, 37 free, two active-bound, and 35 interior;
* robust Wald `37.45`, 10 degrees of freedom, and robust (p=4.7\mathrm{e}{-05}) for H0-A;
* robust Wald `29.21` and robust (p=6.5\mathrm{e}{-08}) for H0-G;
* robust (p=0.594) for H0-B and (p=0.847) for H0-C;
* `beta_E_gsur = -1.105` with the paper-facing robust interval `[-1.51, -0.70]`.

The 47/37/35 arithmetic is consistently and correctly stated. The documents also preserve the distinction between pinned coordinates and free coordinates at an active bound.

### 3.2 Strict non-rejection wording

The core packet and extended abstract correctly state that the NUTS-1 and urbanisation restrictions are **not rejected**. They do not convert non-rejection into evidence that the corresponding coordinates are zero.

The introduction skeleton also carries the necessary warning that failure to reject the remaining restrictions is not evidence of zero coefficients. No document uses “insignificant,” “irrelevant,” “absent,” or an equivalent substantive-zero formulation.

### 3.3 GSUR concentration statement

The accepted inference section authorizes the following bounded statement:

> At the resolution and specification studied, measured access heterogeneity is concentrated in one GSUR dimension rather than diffuse across broad NUTS-1 geography or the two urbanisation indicators.

The core packet and extended abstract preserve this qualifier. The abstract and introduction skeleton omit the opening limitation, “At the resolution and specification studied.” Their resulting formulation is materially stronger than the accepted sentence because it presents the concentration pattern without its resolution-and-specification boundary.

This is a written-claim defect, not a disagreement about the underlying test results.

### 3.4 Conditional active-set caveat

The core packet, extended abstract, and introduction skeleton correctly state that symmetric inference is conditional on the observed active set. They make no unconditional claim about active-set selection. The `NA` treatment of pinned and active-bound coordinates is also correctly described.

### 3.5 Responsibility and normative labels

No estimated component is relabelled as “responsibility,” “effort,” or a morally culpable component. The documents retain “opportunity-attributable” and “preference-related” terminology.

References to a responsibility-sensitive interpretation are explicitly framed as the paper’s adopted normative stance rather than a property established by the estimates. This is consistent with both the accepted inference section and appendix.

### 3.6 Welfare claims

No welfare level, welfare Gini, opportunity share, or decomposition magnitude is invented. All such quantities remain placeholders. The four-scenario W-4 sensitivity and the LOC4 sequencing are described as pre-registered designs rather than completed results. This is consistent with the accepted inference section, appendix, deputy ruling, and frozen M08 handoff.

## 4. Consistency findings

### 4.1 Cross-document empirical story

The four documents tell the same principal story:

* the application is France 2016 singles P2a;
* job opportunities operate through access and wage/ability channels;
* the headline decomposition is opportunity environment versus preferences;
* access versus ability is nested within the opportunity component;
* decomposition, rather than ranking or reform incidence, is the central paper object;
* microsimulation remains a supporting budget-mapping input;
* welfare and decomposition results have not yet been delivered.

There is no substantive baseline contradiction among the four documents.

### 4.2 Counterfactual-design attribution

A recurring statement does not survive comparison with the now-supplied M08 handoff.

The core packet, extended abstract, introduction skeleton, and addendum state or imply that the exact opportunity-equalization and preference-neutralization counterfactuals are “fixed by the frozen M08 welfare-input handoff.”

The handoff does not fix those counterfactual constructions. It freezes the accepted parameter and inference inputs, S-10 obligations, LOC4 sequencing, vigilance items, repository scope, and singles-only mission boundary. It states that the welfare mission will implement the JMP’s money-metric decomposition under its own charter, which was still to be issued by the deputy.

The present wording therefore attributes design content to a document that does not contain it. The counterfactual construction must instead be described as deferred to the M08 welfare mission charter or subsequently frozen welfare-design document.

### 4.3 Addendum change map

The addendum’s document-by-document change map accurately describes the main revisions. Its account of the 47-coordinate vector, pinning structure, identity reversal, welfare sequencing, and no-results boundary is consistent with the v2 documents.

The addendum is also correct that the project-state document was unavailable to Stage A and that its current supersession map is class-based rather than line-based. However, `JMP_project_state_latest.md` was not present in the supplied Stage B packet and was not located in the available File Library search. The reviewer therefore cannot verify whether the seven claim classes exhaust the actual stale passages in that document.

Under the charter’s requirement to identify exactly which parts of the project-state document are superseded, closure requires either:

* inspection and a line- or section-level mapping against the actual project-state file; or
* an explicit Goal 1 Manager ruling that the present class-level supersession is sufficient.

### 4.4 Literature-positioning residue

The addendum correctly identifies surviving couples-baseline language in the literature-positioning memo. The five named sections—§§1, 3, 5, 7, and 8—do contain such language. The memo describes the project as a France 2016 couples prototype, calls couples the actual or coherent baseline, and places singles after couples in the extension sequence.

The addendum’s inventory is nevertheless incomplete: §4 also ends by describing the concrete baseline as France 2016 couples. The residue should therefore be recorded as appearing in §§1, 3, 4, 5, 7, and 8.

Leaving that memo unrevised is permissible only if it remains quarantined as stale project history. Circulating it with the v2 identity documents would directly contradict the accepted empirical identity.

## 5. Contribution findings

The contribution has been preserved.

The four documents continue to define the main contribution as the integration of:

1. structurally estimated job opportunities;
2. money-metric welfare evaluated under constrained feasible sets;
3. an order-independent decomposition of welfare inequality.

The access-versus-ability split is added as a nested supporting decomposition, as required by the deputy, rather than promoted into a competing headline.

No contribution is weakened merely to accommodate the singles sample. The shift from couples to singles is presented as a change in the current empirical application, not a retreat from the structural or welfare question.

No material contribution inflation was found. The documents do not claim:

* completed welfare or decomposition magnitudes;
* clean nonparametric separation of preferences and opportunities;
* causal effects of location;
* policy conclusions from the regional battery;
* validation of LOC4;
* completed couples or pooled-year extensions.

The identification cautions remain proportionate. The contribution is described as disciplined structural measurement under maintained assumptions rather than settled identification of primitive heterogeneity.

## 6. Flagged-item adjudications

### 6.1 Title divergence

**Adjudication: permissible unresolved governance item; no Stage B correction required.**

The charter requires the provisional title to be retained unless a separate title decision is authorized. The core packet and extended abstract retain *Opportunity Constraints as a Driver of Welfare Inequality: A Latent-Jobs Structural Decomposition Approach*, while the alternative programme title remains recorded for Goal 1 Manager adjudication. This is a disclosed divergence, not an accidental inconsistency.
The title divergence does not block identity alignment provided the acceptance memo records which title remains provisional.

### 6.2 Four late-supplied binding inputs

**Inference appendix:** The deferral holds. No appendix-only numerical result was inserted into the identity documents. The W-4 and LOC4 descriptions used there are already carried by the accepted inference section and are consistent with the appendix.

**Goal Manager acceptance memo:** The deferral holds. The memo confirms acceptance of the inference section and appendix and identifies the singles/couples identity inconsistency that the deputy subsequently resolved. It introduces no conflicting paper-facing evidence.

**M08 welfare-input handoff:** The deferral does not fully hold. The documents correctly avoid inventing counterfactual formulas, but incorrectly say that their exact construction is fixed by the handoff. The handoff does not contain that construction. This requires correction.

**`JMP_project_state_latest.md`:** Not adjudicable from the supplied evidence. The class-level deferral is transparent, but the exact supersession boundary cannot be verified without the document or an explicit manager waiver.

### 6.3 Literature-positioning memo

**Adjudication: the residue exists and is materially contradictory.**

The five sections named by the author do contain couples-baseline language. There is also an additional couples-baseline statement in §4. The unrevised memo cannot be circulated as a current positioning document beside the v2 set. It must either be revised in a separate bounded task or clearly marked as superseded and excluded from current circulation.

## 7. Required corrections

1. **Standardize the staged-extension sentence.** In `JMP_core_packet_v2.md`, `JMP_extended_abstract_clean_v2.md`, and `JMP_intro_skeleton_v2.md`, use the deputy-authorized sentence verbatim:

   “The empirical analysis first establishes the complete estimation–welfare–decomposition pipeline for France 2016 single-adult households; extension to couples and pooled years is subsequent work.”

   Remove document-specific additions such as “conditional on successful validation” from this sentence. Any validation condition may be stated separately in governance text.

2. **Restore the exact bounded GSUR wording.** In `JMP_abstract_clean_v2.md` and the France-design paragraph of `JMP_intro_skeleton_v2.md`, prepend:

   “At the resolution and specification studied,”

   to the concentration statement. Retain the current non-rejection, no-substantive-label, and no-causal-claim cautions.

3. **Correct the M08 source attribution.** In the core packet, extended abstract, introduction skeleton, and identity addendum, remove statements that the exact opportunity-equalization and preference-neutralization counterfactuals are fixed by `JMP_M08_welfare_input_handoff_v1.md`. State instead that their exact construction is deferred to the M08 welfare mission charter or subsequently frozen welfare-design artifact. Do not describe the current handoff as containing formulas or reference specifications that it does not contain.

4. **Close the project-state supersession gate.** Before accepting the addendum as satisfying the charter, either:

   * inspect `JMP_project_state_latest.md` and add a section- or line-level supersession map; or
   * record an explicit Goal 1 Manager ruling that the seven claim classes in addendum §4 are accepted as sufficient despite the unavailable source document.

5. **Correct the positioning-memo residue inventory.** Amend addendum §6.4 from §§1, 3, 5, 7, and 8 to §§1, 3, 4, 5, 7, and 8. State explicitly in the acceptance record that `JMP_literature_positioning_memo_v2.md` is not current for empirical identity and must not accompany the v2 set unless revised.

## 8. Whether the v2 set may supersede v1

**Not yet in its present form.**

After corrections 1–3 and 5, the four v2 manuscript-identity documents may supersede their corresponding v1 documents for all paper-facing writing.

The identity addendum may control project-state interpretation only after correction 4 is satisfied by either direct mapping or an explicit manager waiver. Until then, it is a valid provisional class-level supersession notice but not a fully verified exact mapping under the charter.

The v1 files should remain immutable history. The literature-positioning memo should remain quarantined from current circulation until separately aligned.
