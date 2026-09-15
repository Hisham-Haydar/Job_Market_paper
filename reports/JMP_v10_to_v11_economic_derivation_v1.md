# JMP — V10 to V11 economic derivation release, v1

**Scope.** Stage B of the Goal 1 addendum, as corrected by the D-status /
two-perspective ruling. Expository only: no estimation, pricing, welfare
recomputation or decomposition recomputation. Every certified value is unchanged
(`numbers_of_record_v11.json` equals `numbers_of_record_v10.json` on every V10
key; the only new keys are source-bound `att_*` and `mh_*` entries). V9 and V10
are byte-preserved.

**Stage A commit (V10):** `0e69c5eacd3f79548285ddb325386e0d9ed1eac2`.

## 1. Structure of the V11 reader text

1. Why welfare inequality is not income inequality
2. How the latent-jobs model separates preferences from opportunities
3. From choices to well-being: outcomes versus prospects
4. From well-being to inequality: counterfactuals and the Shapley allocation
5. What the current results say
6. What remains preliminary
7. Appendix. Technical record and provenance (collapsed)

## 2. Equations restored to the main text

| | Equation | Why | Interpretation | Empirical use |
|---|---|---|---|---|
| A | $v_i(j)=L_i(j)+\beta_c\log(C_i(j)/\lambda_c)$ | Labour supply trades consumption against leisure; welfare needs the two separable because only consumption is in euros. | $L_i$ is the full non-consumption value (Box-Cox leisure, household-specific weight in age and, for women, children — a reduced-form time-constraint shifter); $\beta_c$ estimated; $\lambda_c$ a units convention. | Preference half of the choice law; the $L$/$\beta_c$ split turns utility gaps into proportional consumption adjustments in both welfare measures; its coefficients are pathway $P$. |
| B | $P_i(j)=e^{v_i(j)}g_i(j)/\int e^{v_i}g_i\,d\nu$ | A common-opportunity RUM must read every behavioural difference as taste. | A job is chosen often if valued or plentiful; choices reflect preferences and opportunity density; the common-opportunity model is the special case of equal $g_i$; only the shape of $g_i$ is estimated. | The estimated likelihood; the central distinction that lets reachability, not taste, explain part of behaviour. |
| C | $g_i(j)=g^E_i\,(g^H_i\,g^{Occ}_i\,g^W_i)^{E_i(j)}$ | "Opportunity" has several margins with different meaning; they must be separable to be equalised one at a time. | Access (local unemployment exposure, region, urbanisation, year), hours bands, occupation, log-normal wage offers; states which blocks vary across households; $A$ is the geographic/temporal channel, not all job opportunities. | Defines what the operators can change and how opportunities reach each welfare measure. |
| D | $M_i^{att}=C_i^{obs}\exp\{[L_i(j_i^{obs})-L_i(o)]/\beta_c\}$ | Utility is not an interpersonal monetary index; a common monetary reference is needed. ATT asks how well off the household is in the bundle it attains. | Non-employment reference; values the attained bundle; no direct opportunity-density term given that bundle; coincides with the staying-home equivalent on the current domain (stated as a verified property, not a theorem). | Computed per household; its counterfactual versions give the attained-bundle decomposition. |
| E | $J_i$, $H_i$, $M_i^{EA}=\lambda_c\exp\{(\log J_i-\log H_i)/\beta_c\}$ | EA asks how valuable the whole distribution of job prospects is; prospect quality may itself be welfare-relevant. | Four points: $J$ values actual prospects; $H$ is the own-opportunity flat-consumption reference; $M^{EA}$ is the equivalent constant consumption; opportunity composition enters directly. Shock reading ($\log J$ ≈ expected best reachable utility) and its normative caveat stated. | Integrated numerically per household over priced points; gives the ex-ante decomposition. |
| F | $M_i^{p,eq}=M_i^p/e_i$ | Welfare is household-level; cross-household comparison needs a needs convention. | Modified-OECD scale, normative not estimated; populations never pooled. | Substantively consequential: couples EA A+B moves 21.3% → 7.9% and the preference term turns negative. |
| G | $I^p(S)=\mathcal G(\{M_i^p(T_Sx_i)\})$ | A distribution alone cannot say which heterogeneity it reflects. | Each coalition equalises named pathways, fully recomputes welfare and inequality; $d_i$ fixed in every coalition. | Bridge from the model to the decomposition: 8 coalitions per perspective, type and scale. |
| H | $\phi_k^p=\sum_S \frac{|S|!(3-|S|-1)!}{3!}[v^p(S\cup k)-v^p(S)]$ | Pathways interact; one ordering is arbitrary. | Average marginal contribution over 3! orders; exact adding-up to $\Delta I^p$; signed; standard Shapley, no novelty claimed. | Keeps $\Delta I$ shares and baseline-Gini shares apart; same rule for both perspectives makes orderings comparable. |

## 3. Revised introduction (summary)

The logical chain now precedes all methodology: observed income inequality is
not necessarily welfare inequality (preferences, constraints, prospects differ);
observed choices do not identify preferences alone (choice frequencies reflect
opportunity density); therefore (1) a structural model separating preferences
from opportunities, (2) a money-metric mapping, (3) structural equalisation
counterfactuals, (4) an order-independent decomposition — each tied to the
section that supplies it. "Why this matters" states that income-based
distributional analysis can miss heterogeneity in labour-market prospects, that
the paper asks whether welfare inequality is associated with preferences,
geographic/temporal access or earning opportunities, and that it does **not**
show an opportunity policy beats redistribution. The introduction then gives
the two perspectives (ruling's framing sentence), the exact D-status sentence,
D as a planned extension, and the central result with the interpretation
sentence. Haydar–Maniquet defensive language is absent from all reader-facing
text; the literature paragraph now describes the factors with budget, needs and
composition held fixed.

## 4. Matched-household illustration — built

`make_v11_matched_households.py` evaluates the accepted singles leisure index and
opportunity density with the certified ex-ante evaluators (no estimation or
pricing). Rule: employed single adults, same sex / occupation group / hours band
/ observed-wage quintile (9,529 pairs); leisure-profile distance ≤ 10th
percentile; maximal opportunity total-variation distance.

Selected pair (two men): leisure weights 8.22 vs 8.17 (distance 0.019, cut
0.065); employment mass ratio 14.5 (opportunity employment share 0.75 vs 0.17);
wage-offer location 11.5 log points higher for B with common dispersion, so B's
wage-offer distribution first-order stochastically dominates A's, while A has
more offers paying at least $w$ for every wage below about €356/h (essentially
all offer mass). Hours density and occupation mass are identical by construction
in this specification, and this is stated. No dominance on every margin exists
and none is claimed. Record and figure contain no identifier, exact observed
value, age, region, local-unemployment value, urbanisation, year or weight.
Stated as not causal and not representative. The optional consumption-prospect
panel was not built (it would require reweighting priced points outside the
certified calculation).

## 5. Body-to-appendix movement log

| Moved to appendix | From |
|---|---|
| Sampled-set index $V_{ij}$, proposal $q_{ij}$, conditional probability with multiplicity $n_y$, $R=100$ / 101 rows, out-of-fold proposal, couples regime-first proposal, one-euro floor | Section 2 "Estimation" (replaced by "Estimation, in words") |
| Criterion values, terminal-path spread, Hessian eigenvalues, bound coordinate; five starts / two polishing contracts | Section 5 behavioural estimates opening paragraph; Section 2 estimation |
| Maintained-restriction parameter code names | Section 5 (replaced by a plain-words restriction sentence) |
| Leisure-scaling reparameterisation / re-estimation box and figure | Section 2 preferences |
| Raw labour-force-status join detail and table | Section 2 data (replaced by a one-sentence model mapping) |
| Tax-benefit accounting identity at machine precision | Section 2 household budget |
| Population-fit moment tables (singles, couples) | Section 5 predictive fit (figures and summary stay in body) |
| Matched-pair distance definitions and source hashes | new, appendix only |
| Integration design, pricing volume (351,024,407), reference-domain convention, C1–C12, sensitivities | already appendix (retained) |

## 6. Corrections found while building V11

- **Stage A missed two stale passages** in the inherited appendix: an editorial
  heading "Numerically blocked opportunity-prospect metric" that preceded its
  superseded label, and the V6 sentence "A separately defined ex-ante metric is
  being reconstructed for comparison". Both are now labelled "Superseded before
  V9" in V11 (wording kept verbatim). The committed V10 was not altered. The new
  Stage A gate (`check_v11_stage_a_status.py`) caught them; its negative control
  fires.
- **$T_A$ description.** Inherited text described the access operator as region,
  urbanisation and year; the operator code also equalises local unemployment
  exposure. V11's new sections say so. The inherited attained-bundle Shapley
  table's "economic content" cell still reads "Region, urban or rural location,
  and year" and is flagged for the next table pass.
- The couples/singles mechanism is labelled an untested reading, and the
  comparison is described as "not a pure comparison of welfare definitions".

## 7. Superseded-number confirmation

The reader gate scans the rendered main text and gallery for V4-era headline
and fit numbers (55.92, 49.16, 34.20, 35.72, 51.20, 8.23, 0.01304, 0.013595,
0.01523, 0.01385) and stale labels (S8, R240, floor5, Mapping F, W1_F,
own-set equal-consumption, Measure 1, Haydar–Maniquet): none found. V4 was used
only as a density benchmark; no V4 number, specification label or diagnostic
was reintroduced.

## 8. Gates (all PASS; `reports/v11_release_gate_summary.md`)

Illustration build; report, gallery, deck (0 overfull/underfull) and rehearsal
builds; notebook refresh and verification; rendered-text banned-term audit with
negative control; Stage A status check with negative control; 40 reader and
economic-derivation checks; 30 number-to-source checks; offline render; cross-
surface synchronisation; deck verification; Python compilation; V9/V10
byte-preservation.

## 9. Hashes

- `JMP_research_story_report_v11.html` — `24091eaebfb84d6707d9578347346266816c9fc19f987dfe5e356522991693f8`
- `JMP_results_gallery_v11.html` — `bed5be97340099edc17f339a672724d8aea3ed6a19c8a1999ed4c6457168d3f8`
- Full surface list: `reports/v11_surface_manifest.json`.
