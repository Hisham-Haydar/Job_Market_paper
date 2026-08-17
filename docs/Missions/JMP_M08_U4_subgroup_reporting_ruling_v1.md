# JMP-M08 U4 Subgroup Reporting Ruling v1

**Programme:** Goal 1 — Empirical JMP  
**Decision-maker:** Deputy Programme Director  
**Date:** 2026-08-05  
**Status:** Binding amendment to the M08 execution contract  
**Issue:** The governing documents required pre-registered subgroup summaries but no accepted subgroup list existed.

## 1. Decision

The following subgroup dimensions are now pre-registered for the France 2016 P2a singles welfare prototype:

1. **Sex**
   - single male;
   - single female.

2. **Education**
   - the three categories of the accepted `educ3` coding;
   - labels must be taken from the accepted data/specification documentation;
   - no relabelling or regrouping is permitted after welfare results are observed.

3. **Broad region**
   - all accepted NUTS-1 design categories represented by the `drgn1` reference category and `drgn2`–`drgn8`;
   - paper-facing labels must come from accepted data documentation;
   - absent accepted labels, report the design-category codes only.

These are descriptive reporting cuts. They do not change the access/ability/preference factor definitions, the equalisation operators, or the Shapley game.

## 2. Rejected or deferred subgroup dimensions

### Age

Age bands are **not** included in the mandatory M08 subgroup list.

Reason: the accepted model uses age terms, but the searched control artifacts do not define an accepted categorical age-band scheme. Creating bands now under the description “as structured in the accepted model” would misstate the model and originate an unrecorded design choice.

An age-gradient or age-band appendix may be proposed later, before execution and with a separately frozen rule, but it is not required for M08 acceptance and may not be selected after seeing welfare outcomes.

### Occupation

Occupation-based reporting groups are excluded from the baseline subgroup list.

Reason: occupation is an estimated access channel and the first mandatory LOC4 robustness dimension. Excluding occupation from baseline subgroup reporting avoids confusing descriptive stratification with the structural attribution exercise and avoids pre-empting the LOC4 robustness.

### Other dimensions

Children, marital-status variants, industry, external regional covariates, and ad hoc intersectional cells are not part of M08 baseline subgroup reporting.

## 3. Required subgroup statistics

Use the same weighting convention as the headline welfare and inequality calculations. Also report the unweighted household count.

### 3.1 Baseline welfare-family reporting

For each active welfare measure \(W^1,\ldots,W^6\), report by:

- sex;
- education.

Required statistics:

- unweighted household count;
- weighted mean money-metric welfare;
- weighted median money-metric welfare;
- weighted welfare Gini.

Region-by-measure tables for all six measures are not mandatory.

### 3.2 Primary decomposition measure

For the primary \(W^3\) baseline, report by:

- sex;
- education;
- broad region.

Required statistics:

- unweighted household count;
- weighted mean;
- weighted median;
- weighted 10th percentile;
- weighted 90th percentile;
- weighted welfare Gini.

No subgroup-level Shapley decomposition is required in M08. The decomposition remains a population-level structural attribution unless a later mission explicitly authorizes subgroup Shapley games.

### 3.3 S-10 four-scenario reporting

For each of the four S-10 scenarios, report the §3.2 statistics for \(W^3\) by:

- sex;
- education;
- broad region.

The purpose is to detect whether local sensitivity is concentrated in a particular observed subgroup. The pre-registered population-level materiality thresholds remain the formal Tier-2 trigger. Subgroup movements are reported continuously and discussed as diagnostics; they do not create an additional unstated trigger.

## 4. Cell and disclosure treatment

- No regrouping may be chosen after welfare outputs are observed.
- Report cell counts with every subgroup table.
- A cell with fewer than 30 unweighted households is not shown in paper-facing tables. It remains in restricted validation output and is marked `SUPPRESSED_LT30`.
- Suppressed cells are not merged post hoc.
- This suppression rule is a reporting/disclosure rule, not a change in the structural sample or decomposition.

## 5. Required contract amendment

Before Stage-D welfare execution, the Goal 1 Manager must insert this ruling verbatim or by exact cross-reference into:

`docs/missions/JMP_M08_singles_welfare_execution_contract_v1.md`

The contract must identify:

- the accepted source for `educ3` labels;
- the accepted source for region labels;
- the headline weighting convention;
- the implementation path for weighted quantiles and Gini;
- the output tables/files carrying the subgroup summaries.

If any label or weighting convention is absent, use code categories and the already accepted headline weighting convention. Do not invent substantive labels or a new weighting scheme.

## 6. Status

This ruling closes U4. It does not block parity diagnosis or correction. It blocks only the welfare reporting freeze until incorporated into the execution contract.
