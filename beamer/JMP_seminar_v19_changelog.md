# Seminar deck changelog: V19 against V18

## What changed and what did not

V19 is the literature and presentation refinement.

**Unchanged:** V18, V17, V16 and r6. No number of the paper changed, no model was re-run, and no figure was regenerated.

**Sources:**
- **The paper's own numbers:** the V15 registry, through `make_deck_numbers_r6.py --v19`.
- **Literature numbers:** `beamer/literature_benchmarks_v19.json`. At every build, each item is re-checked against the literature corpus at `JMP_lit_collection/Markdowns`.

**Size:** 22 main frames (title plus 21 slides) and 38 backup frames (the appendix map plus 37 slides).

## 1. Tone

- **Scope once.** The scope is stated once, on "What is not claimed". The other main slides carry no hedges ("not causal", "preliminary", "point estimate", "not statistically established", "subject to", "cannot claim").
- **Removed from main slides:**

  | Removed | Where it went |
  |---|---|
  | Grey scope footers on the "How much" and channel slides | Scope slide and notes |
  | "current restricted P/A/B game" and "A = current local-access channel" labels on the 100% slide | Notes |
  | "not causal / structural associations" in selected-estimates and results notes | Scope slide, uncertainty backup |
  | The not-a-formal-test remark on Estimation | Benchmark comparison backup |

- **Qualifications kept in the deck:** in notes and on backups, in particular:
  - "Parameter uncertainty" — point estimates; not statistically established;
  - "Attained-bundle numerical design" — still being validated;
  - "Observational equivalence";
  - "Outside the current P-A-B decomposition".
- **One spoken line on ATT.** The notes of "How much is associated with opportunities?" contain the only line: *"The ATT calculation is the less numerically mature of the two and is a useful benchmark rather than the sole basis of the paper."*

## 2. D status

- **Residual label.** The 100% slide labels the last row **"Other / outside current P-A-B decomposition"**, footnoted **"Current decomposition equalises P, A and B only."** V18's longer "Not allocated is not a channel…" line is removed from the main slide. Nothing is labelled D anywhere, and no slide says or implies that adding a channel completes the decomposition.
- **What the residual contains, in backup.** "Outside the current P-A-B decomposition" (renamed from "What is not allocated") keeps the substance: resources, needs and composition held fixed; sex-specific and household-type-specific blocks retained; wage-draw luck and the common offer spread not equalised; location differences ≤ 0.10 against a 0.37 log-point spread. It no longer mentions a "fourth channel D". Its note explains that the operator must be fixed first.
- **Conclusion.** It reads "Next: extend the decomposition to household resources and needs." The note adds "after fixing the appropriate operator".

## 3. Literature: two new main slides

**Slide 4, "Inequality of opportunity".**
- **Top:** outcome inequality splits into circumstances versus responsibility-sensitive factors, with typical circumstances, typical outcomes and the typical question.
- **Benchmarks:** three verified values, large: Italy 19.5%, Brazil 10–37%, France 12.9%.
- **Footer:** one line only, "Different outcomes, circumstance sets and methods."

**Slide 5, "From circumstances to job opportunities".**
- **Layout:** two columns (Empirical EOp | This paper) across opportunity, outcome, structural objects and strategy.
- **Bottom line:** "An inequality-of-opportunity question with a structural opportunity object."

**Comparability.** The fuller discussion is in the slide-4 notes and in the backup "Inequality-of-opportunity benchmarks": lower-bound shares of earnings inequality from *observed* circumstances, versus this paper's share of welfare inequality from *estimated* latent opportunity components with resources and needs held fixed.

**Verified benchmarks.** Each was read in the corpus Markdown and against the original PDF page.

| Shown | Paper | Outcome | Country, data | Measure | Location |
|---|---|---|---|---|---|
| **19.5%** | Checchi & Peragine (2010), *Journal of Economic Inequality* 8: 429–450 | individual gross earnings | Italy, SHIW 1993–2000 (waves 1993, 1995, 1998, 2000) | mean log deviation; types by parental education | Table 4 and text, printed p. 445 (PDF p. 17) |
| **10–37%** | Bourguignon, Ferreira & Menéndez (2007), *Review of Income and Wealth* 53(4) | male hourly earnings | urban Brazil, PNAD 1996 | Theil index; five circumstances; range across cohorts | abstract (PDF p. 1); also PDF pp. 23 and 30 |
| **12.9%** | Brunori, Ferreira & Peragine (2013), IZA DP 7155 | post-tax individual earnings | France, EU-SILC 2005 | mean log deviation; parametric; five circumstances | Table 1 printed p. 23 (PDF p. 26): IEO-R 0.1288; Table 2 (PDF p. 27) |

**Verification notes.**
- **Italy, printed table.** The printed Table 4 row gives 19.5%. That percentage equals opportunity inequality divided by the "effort inequality" column rather than the adjacent total column. The paper's own text states the same 19.5% as "approximately one fifth of the overall inequality", so the paper's figure is shown as printed.
- **France, source of the value.** The value is shown as a percentage of the printed IEO-R ratio 0.1288. It is Brunori et al.'s report of Checchi, Peragine and Serlenga (2010); that primary study is not in the corpus.

**Requested but not shown:** none. All three preferred examples were verified, and no value was taken from memory.

## 4. Building blocks

- **Main slide "Building blocks".** It replaces "Literature and gap":
  - **Latent jobs:** Dagsvik & Jia; the Aaberge–Colombino tradition; Capéau, Decoster & Dekkers.
  - **Welfare:** Fleurbaey & Maniquet; Decoster & Haan; Jacquet, Jia & Thoresen.
  - **Decomposition:** Shorrocks · Shapley.
- **Backup "Literature".** It adds Aaberge, Colombino & Wennemo (2009) and Beffy, Blundell, Bozio, Laroque & Tô (2019), both verified in the corpus, alongside the wider references.

## 5. Identification

- **Main slide "How are preferences and opportunities separated?"** It presents the strategy in five rows:

  | Block | Source of separation |
  |---|---|
  | Preferences | smooth systematic utility over hours |
  | Access | local unemployment and geography, excluded from utility |
  | Hours opportunities | band structure |
  | Wage opportunities | education and experience shift the offer distributions |
  | Budgets | EUROMOD generates heterogeneous nonlinear consumption schedules |

  Bottom line: "These restrictions give different empirical variation to preferences and opportunities."
- **Backup "Observational equivalence".** It holds the deeper discussion.

## 6. Welfare

- **Framing.** The theory-figure slide is now "Welfare: attained outcomes versus job prospects".
- **Questions on the equation slides.**
  - ATT: *"What is the money equivalent of the attained bundle?"*
  - EA: *"What constant consumption over the household's own job environment is equivalent to its prospect?"*
- **Equations.** Kept unchanged.
- **Backup "The prospect reference".** It covers the moving own-opportunity reference and the weighted-mean representation M^EA = (∫ C^β_c ω dν)^{1/β_c}.
- **Wording deviation.** The backup calls this a "weighted generalised mean", not a "power mean", because the retired-token list bans the literal phrase "power mean" left over from the retired ex-ante record. The two terms mean the same thing.

## 7. Results (unqualified on the slides)

Values are unchanged from V18: prospect welfare, singles A + B 20.3% (access > earnings), couples 7.9% (earnings > access); attained-bundle welfare, singles 1.9%, couples 3.5% (earnings > access). The explicit percentage decomposition is kept.

## 8. Corrections

- **(a) Opportunity-density equation.** The backup "Opportunity density" now shows g_i(o) = 1 and g_i(j) = g^E_i g^H_i(h) g^Occ_i(k) g^W_i(w|k) for market jobs j ≠ o.
  - **Checked in the executed code.** In `dclaborsupply/likelihood/engine_jax.py`, `beta_E` enters as `beta_E · working`, and every access shifter carries `interaction: working` in both estimation specs. The non-employment row has log g = 0. The only other adjustment is a per-household centring constant, which cancels.
  - **Couples.** Each employed spouse's package carries its own factors.
  - **V15.** The V15 report's text uses the old form; that is a V15 issue, not changed here.
- **(b) Conventional-model wording.** The old claim is removed ("every difference in behaviour would have to be a difference in taste"). In its place, on the backup slide and in the notes: *"If availability heterogeneity is omitted, some of its effects can be absorbed by the estimated utility component."*
- **(c) Contribution wording.** "Levels rather than changes" is removed. On "Building blocks": *"The contribution is the structural equalisation of estimated preferences, access and earning opportunities followed by recomputation of money-metric welfare inequality."*
- **(d) Participation-convergence figure: nothing removed, pending separate verification.** The conflicting figure is V15's appendix `node_convergence_v3b.png`. It is not in the V18 or V19 deck. It conflicts with V15's corrected fit table ("Employment", model column).

  | Group | Figure at 2,048 nodes | Table | Figure − table |
  |---|---:|---:|---:|
  | Single men | 0.7613 | 0.8675 | −10.6 pp |
  | Single women | 0.8226 | 0.8665 | −4.4 pp |
  | Coupled men | 0.9013 | 0.9234 | −2.2 pp |
  | Coupled women | 0.8963 | 0.9047 | −0.8 pp |

  - **What is shared.** Both use the same parameters, households and weights.
  - **What differs:**
    - the figure integrates over the 2,048-node Sobol support;
    - the table uses 100 random draws plus an exact non-employment point.
  - **Not the cause.** The band fix and weighting do not explain the gap.
  - **Other fit evidence in the deck.** The deck's accuracy backup comes from the node support and matches the registry. The fit-by-margin figure matches the table. Both stay in the deck.
- **(e) Parameter identifiers.** The preference, employment-access, hours/occupation and wage-offer backup tables now show the estimation identifiers (e.g. `beta_E_gsur`). These are generated from the V15 gallery's own parameter names.

## 9. Backup

**New backup slides:**
- inequality-of-opportunity benchmarks (full citations and comparability);
- literature;
- observational equivalence;
- attained-bundle numerical design;
- the prospect reference;
- parameter uncertainty.

**Kept from V18 and extended:**
- identification restrictions (now linked from the new main slide);
- full fit diagnostics (extensive margin, fit by margin, thirty-seven-hour point);
- full parameter estimates (with identifiers);
- full decomposition tables;
- the rest of the V18 appendix.

**Navigation:** the appendix map lists every backup, and every backup has [Back] and [Appendix map]. Seventeen main slides carry corner buttons. The compiled PDF has 155 internal links, all resolving.

## Checks

`verify_deck_r6.py --deck v19` passes 36 of 36.

**Repointed from V18 (with adjustments):** all V18 checks, except that:
- the required statements follow the ruling's wording;
- the residual-label phrases changed;
- the welfare-slide title is a parameter;
- the substantive main-slide range is 19–21, because the ruling adds three main slides.

**New:**
- **G-V19-BENCHMARKS:** every literature number on a slide resolves to a corpus quote on the recorded page, recorded in the build.
- **G-V19-TONE:** no hedges on main slides except the scope slide; hedges retained in notes and backup; the maturity line exactly once.
- **G-V19-DLABEL:** residual label and footnote present; nothing labelled D; no "completes the decomposition".
- **G-V19-CORRECTIONS:** (a), (b), (c), (e) applied; (d) fit backups retained.

**Negative controls:** all nine fire. The seven V18 controls, plus:
- **NC-BENCHMARK-RECORD:** Italy changed to 21.5 in the record.
- **NC-BENCHMARK-SLIDE:** an unrecorded benchmark macro added to slide 4.

**Regression:** r6 19/19, V16 18/18, V17 23/23, V18 32/32.

**Rehearsal script:** `reports/rehearsal_pack_v1.md` is regenerated to V19 numbering and is identical to `reports/rehearsal_pack_v19.md`.

## V19-C2 corrections

Two small corrections. Nothing was recomputed and nothing restructured.

**1. Aggregation boundary (deck, edited in place).**
- **Slide 17 line.** Slide 17, "How much is associated with opportunities?", now carries one line under its label: "The two measures also differ in aggregation: the prospect measure inverts within each household; the attained-bundle measure averages inequality across simulated realisations."
- **Speaker notes.** The slide-17 notes add: the reversal is consistent with the two perspectives valuing different objects, but the aggregation difference is not controlled for, and separating the two is ongoing work.
- **New backup slide, "Backup: two aggregation orders".** It states both constructions:
  - attained bundle: I^att(S) = (1/R) sum_r G_w({M^att_{i,r}(T_S x_i)});
  - prospect: I^EA(S) = G_w({M^EA_i(T_S x_i)}).
- **Navigation.** The new backup is linked from a corner button on slide 17 and from the appendix map.
- **Tone ruling.** No other qualifier was added anywhere.
- **New check.** Both new statements are required on the rendered slides.

**2. Report V16.** V15 is unchanged. `reports/JMP_research_story_report_v16.html` corrects exactly four passages, via `reports/research_story_build/v16_sections.py`:
- **Opportunity-density equation.** It now reads g_i(j) = (g^E_i g^H_i(h) g^Occ_i(k) g^W_i(w|k))^{E_i(j)}, g_i(o) = 1.
- **Likelihood floor, two descriptions.** Both "one-euro floor" descriptions, in Section 2 and in the likelihood record, now say that non-positive simulated alternatives lie outside the choice domain and are excluded; no consumption floor is applied.
- **"Neither route" sentence.** It now says that this simulation is the executed preliminary decomposition, and names the two proposed final routes that are not executed.

`reports/check_v16_correction_scope.py` shows that the V16 Markdown equals V15 plus exactly these replacements. Registry entries and embedded images are identical, and a negative control fires.

**Checks.**
- **Deck (v19):** 36/36 pass, 9 negative controls fire, 159 internal PDF links (0 broken).
- **Deck regression:** r6 19/19, V16 18/18, V17 23/23, V18 32/32.
- **Report V16 release suite:** 14/14 pass. It covers the correction scope, figure captions, rendered language, ex-ante status, section titles, reader structure, number-to-source, offline render, cross-surface sync, the R11 deck, the V11 notebook, compilation and V9–V15 byte-preservation.
