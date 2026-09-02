# 3. Data and institutional setting

*Drafting note, to be stripped at final.* Status tags carry the same meaning as
in §2: **[ACCEPTED]** — on the record of an accepted run or a ratified ruling;
**[PROVISIONAL]** — computed and internally verified, but carrying an explicit
provisional label on its own artifacts; **[PENDING]** — designed or asserted but
not yet ruled or not yet on disk. Every numeral below is bound to a source in
the self-check table at the end of the section. Drafted under Goal-1 R-220.2;
that ruling is **not on disk** — the Goal-1 rulings register ends at R-218 — and
the authorization is therefore recorded here as **[PENDING]** rather than cited.

---

## 3.1 Data

The estimation data are France 2016 EU-SILC/SRCV household microdata, taken in
the form EUROMOD delivers them: the input file `FR_2016_a3`, covering **11,459
households**. This is authentic survey microdata, not the synthetic HHoT
training database that shares part of the EUROMOD French documentation.
**[ACCEPTED]**

The modelled population is the set of households whose labour-supply decision is
well defined and separable: one or two prime-age adults who are neither retired,
disabled, nor still in education, and with no other household member who is
themselves working or employable. Applying that definition in sequence removes
about 62% of the post-composition baseline, almost all of it at the first two
hurdles. Table 3.1 is the waterfall, reproduced from the production
sample-construction functions rather than typed. **[ACCEPTED]**

**Table 3.1 — Sample flow (households).**

| step | households | dropped | share of file total |
|---|---:|---:|---:|
| all households in the France 2016 input file | 11,459 | — | 100.0% |
| one- or two-adult households (composition screen) | 10,003 | 1,456 | 87.3% |
| every adult aged 20–60 | 5,793 | 4,210 | 50.6% |
| no adult still in education | 5,557 | 236 | 48.5% |
| no retirement or disability benefit | 4,973 | 584 | 43.4% |
| labour status in scope | 4,010 | 963 | 35.0% |
| no other employable or earning member | 3,887 | 123 | 33.9% |
| hours and wage within bounds | 3,830 | 57 | 33.4% |
| → single-adult households (modelled) | **1,555** | — | 13.6% |

The composition screen at the second row is a household-classification step, not
a behavioural one, and it is itemised separately: of the 1,456 households it
removes, **930** have three or more adults, **452** have two adults not mutually
linked as partners, **53** are two mutually linked adults of the same sex, and
**21** have no adult aged 20 or over. **[ACCEPTED]**

Of the 3,830 households that clear the whole funnel, **1,555 are single-adult
households** — the estimation sample of this paper — and **2,275 are
opposite-sex couple households**. The 1,555 single-adult households contain
2,236 persons: a single adult decider plus, in some households, children.
Restricting the estimated module to singles is a modelling choice rather than a
data limitation: a single adult's problem is one-dimensional in employment and
hours, while a couple requires a joint decision over two labour supplies and a
joint budget. **[ACCEPTED]**

The estimation frame pairs each household with 101 job packages — the observed
one and 100 drawn alternatives — giving **1,555 × 101 = 157,055 priced rows**.
All descriptive shares in this section are weighted by the survey weight `dwt`;
counts are unweighted. The sample represents a population of **4,547,080**.
**[ACCEPTED]**

**Table 3.2 — Composition of the 1,555 single-adult households.**

| dimension | category | households | unweighted share | weighted share |
|---|---|---:|---:|---:|
| sex | female | 841 | 54.1% | 52.1% |
| sex | male | 714 | 45.9% | 47.9% |
| education | low | 232 | 14.9% | 14.5% |
| education | mid | 692 | 44.5% | 43.1% |
| education | high (tertiary) | 631 | 40.6% | 42.4% |
| employment | employed | 1,348 | 86.7% | 87.1% |
| employment | non-employed | 207 | 13.3% | 12.9% |

The sample is majority female and highly educated, and 87% are employed. The
employment rate is high because the eligibility screen removes exactly the groups
with low attachment; it is the right denominator for this model, since the margin
being explained is the labour supply of people who could plausibly be working.
**[ACCEPTED]**

**The couples module.** The 2,275 opposite-sex couple households — 4,550
deciders — are built by the *same* certified production path: the same household
classifier, the same funnel function, the same feature builder, with the pooled
funnel asserted mechanically to reproduce the certified counts step for step.
What differs is that for a couple the age, education, labour-state and hours
screens must hold for **both** adults, which is why couple attrition is steeper.
This module is a parallel one throughout the paper: it is not promoted, and no
number computed on it is comparable to a singles number, because the frames
differ and likelihoods and information criteria therefore live on different
scales. **[PROVISIONAL]**

**The wage variable.** The production data carry **observed** hourly wages for
workers. The delivered variable `yivwg` satisfies the arithmetic identity
`yivwg = yem × (12/yemmy) / (lhw × 52/12)` on **100.0%** of FR_2015 and FR_2016
persons with observed hours and earnings, in every labour-status and
self-employment category, to machine precision; on the estimation frame the
model's `wage` equals `yivwg` bitwise on all **1,348** working chosen rows. It
is an observed wage, not a prediction. The one exception is small and named:
the **21** workers recorded with zero annual earnings, for whom no observed
hourly wage exists and the delivered value stands. This supersedes the earlier
premise carried in the design record; the dated provenance correction is the
2026-09-02 corrective append under Goal-1 **R-220 s10**
(`docs/Missions/JMP_M08_goal1_rulings_document_v4.md`), and the underlying audit
is `decision_note.md` §22. **[ACCEPTED]**

**One caveat on the observed-hours anchor.** Ten households (0.643% unweighted,
0.889% weighted) had weekly hours moved by the data-prep cap/floor before the
choice set was built, so their chosen node does not carry their observed earnings.
Three are projections onto the model's 70-hour support boundary; seven are an
unintended floor clip and are the subject of a proposed data correction plus one
re-estimation. Final positive-model selection is held pending that re-estimation
(`decision_note.md` §23). **[PROVISIONAL]**

---

## 3.2 Institutional setting

France's statutory working week is 35 hours, and the observed hours distribution
piles up on it: a single dominant spike at 35, a second cluster in the high
thirties, and very little mass between the modes (Figure 3.1, the paper's
motivating picture). Hours are chosen over a small number of *bands*, not on a
continuum; a specification treating hours as a smooth choice variable would have
to explain the gaps away. **[ACCEPTED]**

The model's hours-band factor is a categorical density over five bands. Because
only differences between bands are identified, one band's coefficient must be
normalised, and the specification normalises the band containing the statutory
week — precisely because it is the modal band. Every other hours coefficient in
§4 and §5 is therefore read *relative to a statutory full-time job*. The
35-hour mass is in the model as the yardstick, not excluded from it.
**[ACCEPTED]**

**Table 3.3 — The hours bands, with the corrected labels.**

| band | hours range | role in the offer density | workers |
|---|---|---|---:|
| statutory full-time (35 h reference) | 33.5 – 36.5 | reference — coefficient normalised to zero | 389 |
| short part-time | 17.5 – 21.5 | own estimated coefficient | 34 |
| long part-time | 28.5 – 30.5 | own estimated coefficient | 172 |
| above-statutory full time | 36.5 – 40.5 | own estimated coefficient | 436 |
| long hours (overtime) | 44.5 – 70.0 | own estimated coefficient | 296 |

*Worker counts are on the 1,327 employed households with positive recorded
earnings, over the audit's contiguous partition of the hours line, which closes
the gaps between the estimated bands: `(0, 17.5)`, `[17.5, 33.5)`, `[33.5,
36.5)`, `[36.5, 40.5]`, `(40.5, 70]`.*

Two labels are corrections carried into this draft. The band $[33.5, 36.5)$ is
**statutory full-time (35 h reference)**; the band immediately above it,
$[36.5, 40.5)$, is **above-statutory full time** — full-time work in excess of
the statutory week, not "full time" as against the 35-hour spike. Only the
labels change; the band edges are the ones the hours-mixture module carries and
are unchanged. **[ACCEPTED]**

Nothing in this section, and nothing in the specification, is an estimate of the
effect of the statutory week. The 35-hour coefficient the preferred
specification adds is a feature of the estimated offer density at the statutory
week — an institutionally motivated opportunity peak — and the paper does not
claim identification of a statutory effect anywhere. **[ACCEPTED]**

**Occupation.** Occupation enters as four task groups, collapsed from ISCO-08
one-digit codes by the production function. The map, the group names and the
ISCO titles are all read from source rather than typed.

**Table 3.4 — The occupation key (ISCO-08 → `loc4`).**

| `loc4` | task group | ISCO-08 major groups | share of employed (weighted) |
|---:|---|---|---:|
| 1 | routine manual | 6, 7, 8, 9 — skilled agricultural; craft and trades; plant and machine operators; elementary | 27.5% |
| 2 | nonroutine manual | 5 — service and sales workers | 15.4% |
| 3 | routine cognitive | 4 — clerks | 9.4% |
| 4 | nonroutine cognitive | 1, 2, 3 — senior officials and managers; professionals; technicians and associate professionals | 47.6% |

The four categories are a task grouping, not a skill ranking. Two conventions in
the map are worth stating: elementary occupations (ISCO 9) are collapsed with
the skilled manual groups rather than given their own category — the collapsing
function's `elementary_as_nonroutine_manual` switch is off in the certified
build — and armed forces (ISCO 0) map to an unknown-occupation sentinel rather
than to any of the four. No household in this estimation sample carries that
sentinel. Non-employed rows carry `loc4 = −1`. **[ACCEPTED]**

Occupation composition differs sharply by sex — group 1 employs 38% of men
against 18% of women, groups 2 and 3 are each roughly twice as common among
women, and group 4 is the largest group for both. Because the offer density is
allowed to depend on occupation separately by sex, this composition is
information rather than nuisance. **[ACCEPTED]**

**The wage-offer summary of record.** Over the 1,327 employed households with
positive recorded earnings (weighted population 3,892,446), the delivered hourly
wage has a weighted **mean of €15.47** and a weighted **median of €14.05**. Its
range on the estimation frame is €2.06 to €94.76, with weighted p01 €3.14 and
p99 €41.72. Wages are log-normal with a long right tail, which is the reason the
wage-ability block is specified as a log-normal density rather than a
deterministic wage. **[ACCEPTED]**

---

## 3.3 Geography

The finest household geography in the delivered data is **NUTS-2**: the variable
`drgn2`, **22** metropolitan régions (NUTS-2 2013, identical to NUTS-2 2016).
There is no commune, no département, no employment zone and no NUTS-3. Cell
sizes at NUTS-2 run from 3 to 245 households, median 53.5, with 5 cells below 30
households. The two sampling-unit variables in the file — `dsu01`, 567 primary
units, and `dsu02`, 236 secondary units — are unlabelled, have no published
territorial crosswalk and are overwhelmingly tiny; they are clustering
dimensions, never merge keys. The estimated access block itself keys on the
coarser `drgn1` (ZEAT, NUTS-1 2013, 8 zones, cell sizes 122–279), carrying seven
region dummies. **[ACCEPTED]**

Degree of urbanisation is a three-level coding derived from EU-SILC `db100`:
`drgur` 832 households, `drgmd` 328, `drgru` 395. The verified coding is that
**rural (`drgru`) is the reference category** — it is loaded but carries no
coefficient — and the access block carries two urbanisation dummies against it.
**[ACCEPTED]**

`gsur` is a *continuous* local labour-market rate, sourced from a
`(drgn1, educ3, sex)` lookup at opportunity year 2015, scaled by 10 and gated on
working: 47 unique household-level values, range `[0.053183, 0.225]`, mean
`0.09451`, constant within household. It is not a region dummy and has no
omitted category; it varies with region, education and sex jointly, and is
reported separately from the region dummies throughout. **[ACCEPTED]**

**The missing-region verification.** The EUROMOD French derivation contains a
recode that maps missing region to the capital région
(`replace drgn2 = 1 if drgn2 == .`, `DRD_FR_2016_a3_export.txt:178`), which
would contaminate any Île-de-France comparison. It was checked against the
EU-SILC household register and **it never fired**: the register carries
`N = 11,459` households, an exact match to the EUROMOD household universe with
difference `0`; `DB040` is observed at NUTS-2 across all **22** codes; the
`DB040_F == −1` count is **`0`**; the weighted missing-region share is
**0.0000%**; and the `DB040_F` domain observed over all 11,459 rows is exactly
`{1}` at weighted share `1.0`. There are **1,449** genuine Île-de-France
households in the register (weighted 5,141,585), and the 245 frame households
coded `drgn2 = 1` are all genuine. The record is an aggregate provenance record,
written with method `DERIVED_FROM_UNIVERSE_AGGREGATE_NOT_A_ROW_JOIN` — the
certified 1,555-household frame is a subset of the register on the same
`DB030 == idorighh` key space, and a subset of a set with no flagged members has
no flagged members. Status tokens `DB040_F_RECODE_NOT_USED` and
`FULL_SAMPLE_GENUINE_REGION_OBSERVED`, ratified at Goal-1 R-210. One standing
disclosure travels with the geography: Corse has three households, so no
Corse-specific statement is possible. **[ACCEPTED]**

---

## 3.4 EUROMOD

Consumption is not a survey variable in this model; it is priced. **EUROMOD is
deterministic**: given a household, a weekly hours figure and an hourly wage,
the tax–benefit system returns a disposable income by arithmetic, and the same
triple always returns the same euro figure. Nothing in the estimation simulates
a tax–benefit outcome. All of the randomness in the pipeline is in *which*
points get evaluated, never in what a point is worth. That is what makes a
counterfactual job package priceable at all: every one of the 157,055 rows
carries a disposable income the tax–benefit system actually delivers at that
package. **[ACCEPTED]**

The priced object is EUROMOD's `ils_dispy`, adjusted for benefit take-up.
Take-up traits are rebuilt deterministically from the priced observed node —
revealed-first rates, seeded Bernoulli, seed `20162016`, revealed rates 0.548
for non-workers and 0.265 for workers, realised shares 0.542 and 0.292 — and
enter through the mask
`ils_dispy_takeup = ils_dispy − bsa00_s · (1 − take)`. **[ACCEPTED]**

Take-up is the input weakness of the pipeline and is flagged rather than buried:
the rates are estimated on thin cells, and they enter consumption through the
take-up-adjusted disposable income the builder uses. The thinness is a named
open item for the couples module in particular. **[PROVISIONAL]**

The priced budget is the domain of the environment's budget/needs channel;
see §2.4 for how that channel enters the decomposition. No welfare quantity is
reported in this section. **[ACCEPTED]**

---

## Self-check

### (a) Numerals → source

| numeral (as used above) | source |
|---|---|
| `FR_2016_a3`; 11,459 households in the input file | `MNL/notebooks/france/fr_singles_results_discussion_v1.ipynb` §1, Table 1.1 |
| authentic microdata, not the synthetic HHoT training database | `MNL/experiments/JMP_PS1/decision_note.md` §22.1 |
| waterfall 11,459 → 10,003 → 5,793 → 5,557 → 4,973 → 4,010 → 3,887 → 3,830 → 1,555 (Table 3.1) | notebook Table 1.1 |
| composition screen itemisation 930 / 452 / 53 / 21 = 1,456 (Table 3.1 note) | notebook Table 1.1a |
| 2,275 couple households; 4,550 deciders; identical production screens | notebook §11(a), Table 11.1 |
| 1,555 households / 2,236 persons | `MNL/docs/France_case/P2a/FR_P2a_region_live_dry_run_report_v2.md` §8 |
| 101 alternatives; 157,055 priced rows; population represented 4,547,080 | notebook §1 (cell 6 stdout) |
| composition by sex / education / employment (Table 3.2) | notebook Table 1.2 |
| `yivwg` identity holds at 100.0% for FR_2015 and FR_2016, machine precision | `decision_note.md` §22.2 |
| `wage == yivwg` bitwise on all 1,348 working chosen rows | `decision_note.md` §22.4 |
| the 21 workers with `yem = 0` | `decision_note.md` §22.3 |
| dated correction of the wage premise, 2026-09-02 under Goal-1 R-218 | `decision_note.md` §22.1; `JMP/docs/Missions/JMP_M08_goal1_rulings_document_v4.md`, "Appended 2026-09-02 — R-210..R-218" |
| Figure 3.1 (the observed hours distribution with the band structure) | notebook Figure 2.2 (`fig2_2_hours_bands.png`) |
| hours-band edges and roles (Table 3.3) | notebook Table 2.1 |
| band worker counts 34 / 172 / 389 / 436 / 296 on n = 1,327 | `decision_note.md` §22.3, "hours band" rows |
| corrected labels "statutory full-time (35 h reference)" / "above-statutory full time" | notebook §2, "The band names used throughout" |
| occupation key, ISCO groups and weighted shares 27.5 / 15.4 / 9.4 / 47.6% (Table 3.4) | notebook Table 2.2 |
| `elementary_as_nonroutine_manual` off; ISCO 0 → sentinel, absent from the sample; `loc4 = −1` for non-employed | notebook §2 (cell 13 stdout, cell 14) |
| occupation shares by sex: 38% of men / 18% of women in group 1 | notebook §2, "Occupation composition differs sharply by sex" |
| wage mean €15.465, median €14.047, n = 1,327, weighted 3,892,446 | `MNL/experiments/JMP_PS1/runs/ps1laneB_wage/ps1laneB_step0_wage_comparison_v1.csv`, pooled row; `decision_note.md` §22.3 |
| `yivwg` range 2.063–94.760; weighted p01 3.137, p99 41.722 | `decision_note.md` §22.3, "Tail diagnostics" |
| geography inventory: `drgn2` 22 levels, min 3 / median 53.5 / max 245, 5 cells < 30; `drgn1` 8 levels, 122–279; `dsu01` 567; `dsu02` 236 | notebook Table 12.1 |
| NUTS-2 is the finest geography; nothing below it; sampling units are clustering dimensions | notebook §12(a) |
| urbanisation counts `drgur` 832 / `drgmd` 328 / `drgru` 395; rural is the reference and carries no coefficient | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_inference_design_v2.md` §"drgur, drgmd" |
| `gsur`: `(drgn1, educ3, sex)` at 2015, scale 10, `working`-gated, 47 values, `[0.053183, 0.225]`, mean 0.09450886, not a dummy | same, §"gsur" |
| register `N = 11,459`, difference 0; 22 `DB040` codes; `DB040_F == −1` count 0; weighted share 0.0000%; domain `{1}` at weighted share 1.0; 1,449 IDF households (weighted 5,141,585); 245 frame households at `drgn2 = 1` | rulings document v4, R-210 |
| recode site `DRD_FR_2016_a3_export.txt:178`; method `DERIVED_FROM_UNIVERSE_AGGREGATE_NOT_A_ROW_JOIN` | rulings document v4, R-210 |
| Corse: three households | notebook §12(a), closing caveat |
| EUROMOD determinism | notebook §4(a), "How the numbers are computed" |
| take-up: seed 20162016, revealed rates 0.548 (nw) / 0.265 (w), shares 0.542 / 0.292 | `FR_P2a_region_live_dry_run_report_v2.md` §8 |
| take-up mask `ils_dispy_takeup = ils_dispy − bsa00_s·(1−take)` | `MNL/docs/France_case/P2a/FR_P2a_region_live_production_rebuild_plan_v2.md` §step 2 |
| take-up rates estimated on thin cells (couples flag) | notebook §11(a) |

### (b) Claims → status

| claim / design element | status |
|---|---|
| France 2016 EU-SILC/SRCV via the EUROMOD input `FR_2016_a3`; 11,459 households | **[ACCEPTED]** |
| the eight-step eligibility waterfall and the 1,555-household singles sample | **[ACCEPTED]** |
| the composition screen itemisation | **[ACCEPTED]** |
| survey weighting by `dwt`; 4,547,080 represented | **[ACCEPTED]** |
| singles restriction as a modelling choice, not a data limitation | **[ACCEPTED]** |
| the 2,275-household couples frame as a parallel module, not comparable to singles | **[PROVISIONAL]** |
| the production data carry observed hourly wages for workers (`yivwg` identity) | **[ACCEPTED]** |
| 35-hour statutory week; the observed spike; hours chosen in bands | **[ACCEPTED]** |
| the reference band is a normalisation, not an omission | **[ACCEPTED]** |
| the corrected band labels | **[ACCEPTED]** |
| ISCO-08 → `loc4` four task groups; a grouping, not a skill ranking | **[ACCEPTED]** |
| the wage-offer summary of record | **[ACCEPTED]** |
| NUTS-2 (`drgn2`, 22 régions) as the finest household geography | **[ACCEPTED]** |
| rural (`drgru`) as the urbanisation reference | **[ACCEPTED]** |
| `gsur` as a continuous rate, reported separately from the region dummies | **[ACCEPTED]** |
| the `DB040_F` verification: zero missing-region recodes, aggregate provenance record | **[ACCEPTED]** (R-210) |
| Corse disclosure (three households) | **[ACCEPTED]** |
| EUROMOD as deterministic pricing; `ils_dispy`; the take-up mask | **[ACCEPTED]** |
| take-up thinness as a named input weakness | **[PROVISIONAL]** |
| the priced budget as the domain of the environment's budget/needs channel | **[ACCEPTED]** (forward reference only) |
| the Goal-1 R-220.2 drafting authorization | **[PENDING — not on disk; register ends at R-218]** |

### (c) Prohibitions observed in this section

No welfare number of any kind — no level, no inequality index, no component, no
share. No headline. No restatement of the superseded wage premise: the section
states the observed-wage fact and cites the dated correction, and does not
reproduce the withdrawn description or its provenance dispute. No causal
language on the 35-hour institution — no "effect of the 35-hour law", no claim
of identification of a statutory effect, and the 35-hour coefficient is named as
an institutionally motivated opportunity peak in the estimated offer density.
No comparison of a couples number to a singles number. No Corse-specific
statement. Exactly one forward reference, to §2.4.
