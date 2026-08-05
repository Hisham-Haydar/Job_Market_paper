# JMP-M07 Stage C — Independent Economics Review

## Cover note for the Goal 1 Manager

**Verdict:** PASS WITH REQUIRED CORRECTIONS  
**Correction count:** 10 narrow written-claim corrections

## 1. Verdict

**PASS WITH REQUIRED CORRECTIONS**

The core empirical reporting is substantially sound. The 47-row parameter table is complete, remains in the reporting-map order, and matches the authoritative CSV for parameter status, estimates, model-based standard errors, robust standard errors, robust confidence intervals, and literal `NA` treatment. The central hypothesis-test structure is also present: H0-A is limited to the named regional/urbanisation/GSUR block; H0-B and H0-C are reported as non-rejections in the tables; and H0-G carries the rejection concentrated in the GSUR coordinate.

The drafts do not require any reopening of estimation, inference, or software certification. The required corrections concern written claims only: undeclared numerical rendering, over-interpretation of H0-B/H0-C, broad precision characterisations, unsupported singleton-cluster reasoning, technically over-strong KKT language, an incomplete S-10 output list in the main section, an inaccurate baseline/LOC4 wage-density description, the R-55c source-route treatment, and incomplete self-limitations.

## 2. Claim-to-evidence findings

### 2.1 Findings that pass

1. **The 47-row parameter table passes the source audit.** All 47 rows in `FR_P2a_empirical_inference_v1.md`, lines 158–240, match `FR_P2a_phase5_parameter_reporting_map_v1.csv`. This includes:
   - original parameter order;
   - panel assignment;
   - interior / active-bound / pinned status;
   - active-bound side;
   - estimates;
   - model-based and robust standard errors;
   - robust confidence intervals;
   - literal `NA` fields;
   - the special rendering of `beta_l0_m` as `0.000001`;
   - the half-away-from-zero rendering of `beta_occ_4_f` as `0.855`.

2. **The core paper-facing regional-test numbers pass.** The following values reproduce the charter/extraction-memo renderings:
   - H0-A: robust Wald `37.45`, robust p-value `4.7e-05`;
   - H0-G: robust Wald `29.21`, robust p-value `6.5e-08`;
   - `beta_E_gsur = -1.105`;
   - robust interval `[-1.51, -0.70]`;
   - H0-B robust p-value `0.594`;
   - H0-C robust p-value `0.847`.

3. **The full-precision appendix table is correct except for the specifically adjudicated H0-G route issue.** H0-A, H0-B, H0-C, and the H0-G Wald/model-based entries match the extraction memo exactly.

4. **The dimension counts and reporting statuses trace correctly.** The drafts correctly report 47 total coordinates, 10 pinned coordinates, 37 free coordinates, 2 active-bound coordinates, and 35 interior coordinates.

5. **The W-4 bounds and full-precision intervals trace correctly in Appendix A.6.** The two flagged coordinates, bounds, and endpoints match the extraction memo.

6. **No paper-facing claim relies on an item explicitly marked `UNAVAILABLE` except where the drafts themselves introduce unsupported assumptions.** The unavailable omitted/reference categories, parameter-level z/p statistics, and numerical S-10 perturbations are not reported as results.

### 2.2 Findings requiring correction

1. **Undeclared rounding occurs outside the stated rendering convention.**
   - Main §5.1 reports `1.4566e-13` rather than the extraction-memo value `1.4566126083082054e-13`.
   - Main Table 1 rounds several model-based and robust Wald/p entries without stating a Table-1 rendering rule. The drafting note governs estimates, standard errors, and confidence-interval endpoints, not Wald statistics or p-values.
   - Main §5.5 reports the `beta_w_pexp2` interval as `[-0.1014, 0.0754]`, which is neither the declared three-decimal rendering nor a verbatim full-precision source value.

2. **Appendix Table A.2 is labelled “full precision” but gives H0-G robust p as `6.5e-08`.** This is an accepted paper-facing rendering, not a full-precision rendering. The dual sixteenth-digit source routes must be disclosed without treating either as a substantive correction.

3. **The main drafting note overstates source fidelity.** It says every non-*Reading* statement is a direct rendering of an accepted artifact. The KKT explanation, singleton-cluster interpretation, and LOC4 wage-density description contain theoretical or design interpretations not stated in the extraction memo or reporting map.

## 3. Interpretation findings

### 3.1 Regional-access interpretation

The drafts correctly frame the regional/urbanisation/GSUR battery as **one channel** of the opportunity environment rather than a test of the whole opportunity mechanism. The hours-access and occupation-access blocks are explicitly excluded from H0-A.

The required H0 structure is also visible:
- H0-A rejects the named ten-coordinate block;
- H0-B fails to reject the seven NUTS-1 coordinates;
- H0-C fails to reject the two urbanisation coordinates;
- H0-G rejects the GSUR coordinate.

The canonical bounded interpretation is reproduced exactly:

> At the resolution and specification studied, measured access heterogeneity is concentrated in one GSUR dimension rather than diffuse across broad NUTS-1 geography or the two urbanisation indicators.

However, surrounding prose exceeds that bounded statement:

1. “Jointly indistinguishable from zero” and “add nothing” convert failures to reject into zero-effect conclusions.
2. The statement that broad geography and urbanisation “are not the dimensions along which measured access differs” is stronger than the tests license.
3. The claim that the parsimonious specification is “not leaving a measured regional signal on the table” is not established by testing only the included NUTS-1 and urbanisation coordinates.
4. The conclusion that external regional covariates are merely optional is a project-sequencing decision, not an empirical implication of H0-B/H0-C.
5. “The sub-blocks are not orthogonal by construction” is not documented in the extraction memo or reporting map.

### 3.2 Parameter interpretation

Several numerical summaries are accurate, but their umbrella characterisations are too broad:

1. “The access side is the precise side of the model” ignores the imprecise NUTS-1 and urbanisation estimates.
2. “The wage-density location parameters are equally sharp” is false as a block-level description: `beta_w_educL` and `beta_w_pexp2` have robust intervals containing zero.
3. “Large” is scale-dependent and is not benchmarked.
4. Sign interpretations for hours and education shifters should remain coefficient-sign statements until the omitted/reference categories—listed as unavailable—are supplied.
5. The claim that a model without an explicit opportunity term “would have to absorb” the observed occupation pattern into tastes is not established by a reported model comparison.
6. The broad “sharp access / soft preference” asymmetry is not the reason for S-10. S-10 is routed by W-4 for two specific near-boundary intervals, one preference coordinate and one wage-density coordinate.

## 4. Overclaim findings

### 4.1 Findings that pass

1. The drafts explicitly reject causal interpretation of the regional battery.
2. They draw no policy-effect conclusion from the Wald tests.
3. They do not label the preference-related decomposition component as responsibility.
4. They make no unconditional active-set claim; the 35-dimensional covariance is repeatedly described as conditional on the observed active set.
5. They do not report unestimated welfare, decomposition, or LOC4 results.

### 4.2 Findings requiring correction

1. “How access inequality should be modelled” is too prescriptive for this single static specification and test battery.
2. “Not leaving a measured regional signal on the table” amounts to an unsupported specification-adequacy claim.
3. “Would have to absorb into tastes” overstates what the estimated model alone identifies.
4. Appendix A.9 does not expressly limit the interpretation of failures to reject H0-B/H0-C and does not state that the battery cannot rule out omitted regional dimensions or validate the parsimonious specification against richer covariates.

## 5. Bound/W-4/S-10 findings

### 5.1 W-4 and S-10 findings that pass

1. W-4 is correctly classified as Tier 1, non-gating, visible, and non-headline.
2. The two flagged coordinates are correct.
3. The required manuscript disclosure is reproduced faithfully.
4. The four scenarios are correct:
   - accepted baseline;
   - `beta_l0_sm` perturbed alone;
   - `beta_w_pexp2` perturbed alone;
   - both perturbed jointly.
5. The perturbation rule is faithful.
6. No re-estimation is allowed.
7. The material-loading thresholds are faithful.
8. The three exact Tier-2 triggers are stated in Appendix A.6:
   - direct inference on a flagged coordinate;
   - material welfare/decomposition loading;
   - an unconditional active-set claim.
9. The interpretation limits are faithful.

### 5.2 KKT/NA finding

The `NA` convention is substantively correct, but the theoretical explanation is over-strong.

An active constraint does **not**, by itself, establish a strictly non-zero KKT multiplier; that requires an additional strict-complementarity condition. The numerical multipliers are expressly listed as unavailable. Likewise, the constrained estimator’s asymptotic law should not be described categorically as “censored at the constraint.” The defensible claim is narrower: the usual unconstrained, symmetric normal approximation need not apply in the constrained direction, so ordinary two-sided Wald inference is not reported.

### 5.3 S-10 output-list finding

Main §5.5 presents its scenario-output list as exhaustive but omits two outputs required by the binding S-10 specification:
- the chosen headline inequality index, if different from the welfare Gini;
- numerical convergence and invariance diagnostics.

Appendix A.7 includes both. The main section must either include them or make clear that its list is abbreviated and cross-refer to the complete appendix list.

## 6. LOC4 finding

The **Path-B ruling is rendered at the correct strength**:

- the certified model is the baseline for the first welfare/decomposition prototype;
- LOC4 does not block that prototype;
- the four-density LOC4 exercise is mandatory before preferred quantitative decomposition magnitudes are frozen and before final paper-facing quantitative decomposition claims.

This is neither stronger nor weaker than the ruling.

Two associated descriptions are not faithful:

1. The drafts state that the baseline wage-density location is shifted by occupation. The authoritative reporting map contains education and potential-experience location terms plus a common dispersion parameter; the occupation coefficients reported in Table 2 are opportunity-access coefficients, not wage-density location coefficients.
2. The drafts describe LOC4 as asking specifically whether occupation-specific **dispersion**, as distinct from occupation mean shifts “already in the model,” matters. The ruling requires the LOC4 mission to document whether mean and/or dispersion changes are introduced. It does not define the robustness as dispersion-only, and the asserted existing occupation mean shifts are not supported by the reporting map.

## 7. Consistency findings

### 7.1 Findings that pass

1. Main Table 2 and the reporting CSV agree in every row and numerical field.
2. Main Table 1 and Appendix Table A.2 agree on test verdicts.
3. Main and appendix agree on the 47/37/35/10/2 arithmetic.
4. Main and appendix agree on the flagged W-4 coordinates and bounds.
5. Main and appendix agree on Tier-1 status, no re-estimation, four S-10 scenarios, and LOC4 Path-B sequencing.
6. The main source-notes map correctly identifies the extraction memo, reporting map, W-4/S-10 specification, and LOC4 ruling for the mechanical claims it covers.

### 7.2 Findings requiring correction

1. Main §5.5 uses a four-decimal W-4 interval while Table 2 and Appendix A.11 prescribe three-decimal table rendering.
2. Appendix Table A.2 calls itself full precision but uses the paper-facing H0-G p-value.
3. Main §5.5 omits two required S-10 outputs that Appendix A.7 includes.
4. Appendix A.10 says sample information beyond the count is not stated, while the main section and Appendix A.3 assert one labour-market-relevant adult and one likelihood term per household.
5. The main drafting note’s source-fidelity claim is inconsistent with its own untraced interpretive assertions.
6. The main and appendix repeat the same unsupported occupation-shift/dispersion-only LOC4 description.

## 8. Ruling adjudications

### R-55b — precision through robust confidence intervals only

**UPHELD ON THE MERITS.**

The reporting map contains the robust confidence intervals needed for paper-facing precision statements, while parameter-level z-statistics and p-values remain in accepted artifacts but are not carried into the reporting map. Reporting precision through robust confidence intervals avoids introducing an additional source route and does not suppress any required parameter estimate, standard error, or interval. The drafts comply in the parameter table. The broad prose characterisations still require narrowing to what those intervals actually show.

### R-55c — H0-G sixteenth-digit dual rendering

**UPHELD ON THE MERITS.**

The two values,
`6.500461827702641e-08` and `6.500461827702638e-08`,
differ only in the sixteenth significant digit and arise from two accepted source routes within the extraction memo. They imply the same paper-facing rendering and the same verdict. This is a source-route note, not an extraction-memo error requiring correction.

The current Appendix A.5 sentence referring an extraction-memo correction to the Goal 1 Manager conflicts with R-55c and must be removed. A full-precision appendix table should use the table-route value and note the claim-route value; the paper-facing prose may retain `6.5e-08`.

## 9. Required corrections

1. **Regularise numerical rendering.** Add an explicit Table-1 rendering convention or reproduce the full-precision values; replace `1.4566e-13` with the source value or an authorised rendering; and render the `beta_w_pexp2` W-4 interval consistently at three decimals or full precision.

2. **Restore strict H0-B/H0-C language.** Replace “indistinguishable from zero,” “add nothing,” and the corresponding absence claims with “fail to reject”; retain the canonical bounded GSUR-concentration sentence.

3. **Delete or source the extra regional-specification conclusions.** Remove the claims that the included tests show no regional signal is left on the table, that richer external covariates are empirically optional, and that sub-block non-orthogonality is established, unless a separate accepted source is supplied.

4. **Narrow the Table-2 reading.** Identify only the exact subsets whose robust intervals exclude zero; remove block-wide “precise side/equally sharp” characterisations, unbenchmarked “large” language, and the untested “would absorb into tastes” model-comparison claim. State that S-10 is motivated by W-4, not by a general access-versus-preference precision asymmetry.

5. **Source-bound the singleton-cluster interpretation.** Either supply an accepted model/data source for one relevant adult, one likelihood term, and cluster size one, or qualify/remove those statements. Remove the unsupported claim that singleton clustering explains why robust and model-based results are close. Align Appendix A.10 accordingly.

6. **Correct the KKT explanation in both drafts.** Do not assert a non-zero multiplier or a categorically censored sampling distribution from active-bound status alone. State only that the unconstrained symmetric normal/Wald approximation is not licensed in the constrained direction and that inference is conditional on the observed active set.

7. **Complete the main S-10 output list.** Add the headline inequality index if different and numerical convergence/invariance diagnostics, or identify the main-section list as abbreviated and point explicitly to the exhaustive Appendix A.7 list.

8. **Correct the baseline and LOC4 wage-density description in both drafts.** Remove unsupported occupation location shifts from the certified baseline and do not characterise LOC4 as dispersion-only. Use the ruling’s mean-and/or-dispersion formulation and preserve the no-double-counting requirement.

9. **Implement R-55c.** Remove the request to correct the extraction memo. In a table labelled full precision, use the accepted table-route H0-G value and record the claim-route value as a harmless source-route discrepancy; retain `6.5e-08` in paper-facing prose.

10. **Expand Appendix A.9 and remove internal drafting artefacts before circulation.** Add that failure to reject is not evidence of zero effects and that the battery does not rule out omitted regional dimensions or validate the parsimonious specification against richer covariates. Remove mission/path metadata and drafting notes from the circulated manuscript, or revise the source-fidelity note so it does not misclassify theoretical and design interpretations as direct artifact renderings.

## 10. Unflagged assumptions

The drafts currently make or resolve the following assumptions without flagging them as assumptions:

1. The P2a label implies exactly one labour-market-relevant adult and exactly one likelihood term per household.
2. Household clustering therefore has cluster size one and cannot address within-household dependence.
3. Singleton clusters explain the closeness of model-based and robust results.
4. The H0-A sub-blocks are non-orthogonal “by construction.”
5. Failure to reject NUTS-1 and urbanisation restrictions means those dimensions do not carry measured access heterogeneity.
6. The included regional battery establishes that no relevant regional signal is omitted.
7. A conventional model without explicit opportunity terms would necessarily absorb the occupation-access pattern into tastes.
8. The wage-density block is uniformly sharp and the high-education coefficient is “large” without a scale or comparison benchmark.
9. The broad access/preference precision contrast is what motivates S-10.
10. Active-bound status implies a strictly non-zero KKT multiplier and a censored estimator distribution.
11. The certified wage-density baseline contains occupation-specific location shifts.
12. LOC4 is exclusively a dispersion robustness rather than a pre-registered wage-density variant whose mean and/or dispersion changes must be documented.
13. The score-aggregate deviation alone “demonstrably” establishes that bread and meat are derivatives of the same objective.
14. The finite-sample correction cannot matter for any conclusion, rather than the narrower sourced statement that the reported verdicts are stable.
