# Consistency gate v1

**Verdict: FAIL.** The values that are actually tied to a numbers-of-record key agree with that key, but the requested cross-artifact gate does not close. There is one direct model-notation conflict, one incorrect Shapley chart label, material coverage gaps for states/decomposition uncertainty and the couples limitation, incomplete reference labels, and many forbidden/internal-phrase hits.

Audit date: 2026-09-07. This was a read-only audit of the named inputs. No audited input was edited.

## Scope and method

- Registry: `reports/numbers_of_record_v1.json` (203 entries). Every entry has `value`, `source`, `basis`, and `reference`.
- Paper: `manuscript/JMP_working_paper_for_seminar_v2.md`.
- HTML: `reports/JMP_research_story_report_v1.html`. The parsed `NOR-DATA` object is exactly equal to the external registry across all 203 entries. `AUX-DATA` was also read. All 573 `.n` spans resolve to an existing `NOR-DATA` or `AUX-DATA` key; none resolves to `MISSING`. The rendered values below were reconstructed with the page's own `fmt` rules, so both the embedded values and the displayed precision were checked.
- Notebook artifact: executed outputs and Markdown in `MNL/experiments/JMP_SEMINAR_SPRINT/JMP_research_lab.ipynb`, with its declared coverage in `runs/research_lab/CELL_MAP_v1.md`.
- Deck: `beamer/build/JMP_seminar_deck_v1_text.txt`.

Input SHA-256 values at audit time:

| input | SHA-256 |
|---|---|
| registry | `7A707D8580F6E82BC1EF0A16977C6A7C0613F91F5CDBFE3D44FC779058E8F74F` |
| paper | `E8353A3884186AFBAD55CB8DC407A767DC8578EEFFB2EDF42074D8304A42AE88` |
| HTML | `2C7352FDA7C1DC52910F267D2B9609959678F609FA0EB3CEF9B70402D19B7D2F` |
| notebook | `DD80D596B89BA49FFDC0660A7482308F01E6A84386BA52AAA99D061F47601325` |
| cell map | `4658E65D69C13EFA9A256D781781497463054BD630FEB9F887A0A58B9F244D17` |
| deck text | `A46BE4C68CD5CA5ED15AF745D7B9FC0CFC0A9C9C54BB11BD9FA65CC5F50371C4` |

“Not stated” below is not treated as a contradictory value unless the requested rule requires the statement everywhere. It is nevertheless shown so that coverage is explicit. Rounding is treated as numerically consistent, but it does not satisfy a request for the full recorded objective.

## Item-by-item gate

| item | paper | HTML | notebook | deck | registry | verdict |
|---|---|---|---|---|---|---|
| Raw-frame households | 11,459, lines 1012–1014 and 1027 | 11,459, line 113, §3, `n_households_raw_frame` span | Not printed | Not stated | `n_households_raw_frame = 11459` (line 1048) | PASS where stated; incomplete coverage |
| Singles households | 1,555, lines 1043–1054 | 1,555, line 113, §3 | Executed output 1,555, lines 364 and 547 | 1,555, line 210 | `n_households_singles = 1555` (line 1055) | PASS |
| Couples households / CR1 clusters | 2,275, lines 1044–1045, 2674, 2724 | 2,275, line 113, §3 | Not printed under the executed singles controls | 2,275, line 628 | `n_households_couples = 2275`; `n_couples_clusters = 2275` (lines 1041 and 1034) | PASS where stated; incomplete notebook coverage |
| Alternatives per household | 101 = observed + 100 draws, lines 1052–1054 | 101, lines 113/157, §§3–4 and §7 | Executed output 101, lines 365 and 548 | Observed + 100 draws, lines 191–192 (101 implicit) | `n_alternatives = 101` (line 1027) | PASS |
| Priced singles rows | 157,055, lines 1052–1054 | 157,055, line 113, §3 | Executed output 157,055, line 366 | 157,055, line 204 | `n_priced_rows_singles = 157055` (line 1090) | PASS |
| Active parameters | 41, lines 1076–1080 and Appendix A.1 | 41, line 157, §7 | Executed output 41, lines 486 and 598 | 41, line 186 | `n_params_active = 41` (line 1062) | PASS |
| Interior / active-bound parameters | 39 / 2, lines 1080–1082 and Appendix A.4 | 39 / 2, line 157, §7 | Executed output 39 / 2, lines 599–600 | Not stated | `n_params_interior = 39`; `n_params_at_bound = 2` (lines 1076 and 1069) | PASS where stated |
| 51-coordinate representation is provenance-only and confined to allowed sites | Correct meaning in Appendix A.4, but `51` and/or `S8` also occur outside A.4 (Appendix A.3 and self-check); see hit ledger | One rendered 51 is in a provenance box, but another is in §22 Q31; embedded `NOR-DATA` also contains 140 `S8` and seven standalone `51` hits | Many `S8`/`51` hits in Markdown, code, outputs, and metadata; cell map repeats both | Neither appears | `n_params_provenance = 51` (line 1083), explicitly provenance | **FAIL** |
| Final singles negLL | Exact 18022.764617170084, line 3486 | Embedded value exact; rendered as 18022.7646 in §7 because the span uses `f4` | Exact executed output, lines 488–489 and 546 | Not stated | `negll_singles_final = 18022.764617170084` (line 1111) | Numeric PASS; HTML display is rounded |
| Final couples negLL | 43,493.342239 (rounded), line 2722 | Embedded value exact; rendered as 43493.3422 in §11 (`f4`) | Exact executed output 43493.342239066726, lines 1669 and 1675 | Not stated | `negll_couples_final = 43493.342239066726` (line 1104) | **FAIL exact-display coverage** |
| Model equations, symbols, and factor names | Four opportunity factors: `g^E`, `g^H`, `g^Occ`, `g^W`, lines 687–733 | Five terms in assembled index: `g^E`, `g^H`, `g^Acc`, `g^Occ`, `g^W`, lines 127–154, §6 | Markdown uses `g^E`, `g^H`, `g^W`, and collapsed `g^{market}`, physical lines 789–790 | Four factors `gE`, `gH`, `gOcc`, `gW`, lines 178–180 | No equation/symbol key | **FAIL** |
| W1 statement | Uniform pay on own reachable set; pay differences neutralized; set differences remain, lines 765–784 | All three clauses are present in §13, physical line 166 | Only names W1/common RQMC support; no uniform-pay, neutralization, or set-retention statement, lines 673–679 and 789–795 | Uniform pay/own reachable set, lines 66 and 422–424; does not explicitly say pay differences are neutralized and set differences remain | No semantic W1 key | **FAIL coverage** |
| Four singles states, raw, both references, RQMC | All points and half-widths agree, lines 1982–1990 | Female-raw points only; no male arm or state bands | Female-raw points only, executed lines 699–702; cell map line 17 declares that limited coverage | Female-raw points rounded, lines 444–445; no bands or male arm | All eight point keys and all eight `__rqmc_band` keys exist | PASS values; **FAIL requested coverage** |
| Four singles states, equivalized, both references, RQMC | Female-primary points reappear at lines 2893–2896; I00 and its band appear for both references at 2052–2053; remaining states/bands are not fully displayed | Only female I00 is rendered; no complete equivalized state grid or bands | Not printed | Not stated | All eight point keys and all eight `__rqmc_band` keys exist | **FAIL requested coverage** |
| Singles decomposition, raw/equivalized, both references, RQMC | Table 7.1, lines 2039–2055, agrees for all five contribution points, shares, and contribution half-widths | Female raw/equivalized points and shares are rendered; male points/bands and all contribution RQMC bands are not rendered | Female-raw contribution points only, executed lines 703–707; no shares/bands/other arms | Selected rounded female-reference shares, lines 489, 493–520 and 743–749; no complete grid/bands | Point/share keys and contribution `__rqmc_band` keys exist; no registry keys exist for the RQMC bands on the shares printed in paper Table 7.1 | PASS values; **FAIL requested coverage and registry coverage** |
| CR1 functional intervals | Appendix F prints female-primary/raw headline contributions and shares, lines 3988–4002; only I00 among the four states | Renders eight female-primary/raw headline CR1 keys in §§15/19; state CR1 keys are unused | Runs CR1 parameter inference, but does not print any functional CR1 interval | Only environment-share interval [89.1, 95.8], lines 489–490 | Fifteen female-primary/raw CR1 keys exist; no male-reference or equivalized CR1 keys exist | **FAIL requested coverage and registry coverage** |
| Couples states/decomposition | States on both bases and raw/equivalized component points, lines 2810–2830; component bands are incomplete | Selected equivalized state/component points only; no couples RQMC bands rendered | Only raw I1111 executed, line 1670 | Not stated | State points/bands exist on both bases; component points/bands exist only equivalized | **FAIL coverage** |
| Shapley 93.7/6.3 versus one-factor 77/+10 | Correct and explicit, lines 2099–2109 | Correct and explicit in §14 and §22 Q13–Q14, physical lines 166 and 176 | States Shapley identities but prints neither comparison nor distinction, lines 673–679 | 77 versus rounded 94 is distinguished at lines 451–452, but the preference +10 leg is omitted and Shapley plots are labelled as shares “removed” at lines 505 and 619–626 | `C_env_female_raw_share`, `C_pref_female_raw_share`, `equalization_env_only`, `equalization_pref_only` | **FAIL** |
| Reference labels: female primary; male structural zero; never averaged | Correct, e.g. lines 1987–1988, 2219–2243 | Correct in §§15, 19 and Q28, physical lines 166/176 | Says only “female-reference raw-basis”; no male structural-zero label or never-averaged rule, line 679 | Says “female reference” / “male reference”; omits primary, structural-zero, sensitivity, and never averaged, lines 485–490 | Basis strings on female/male state and contribution keys; `beta_l_nkids_male_status` supplies the structural-zero status | **FAIL** |
| Couples `beta_ll` absent, welfare 0, limitation | Correct and explicitly a limitation, lines 2687–2719 and 3247–3257 | Correct and explicitly a limitation in §§11/20 and Q21, physical lines 157/166/176 | Exact absence/value/form are printed at lines 1671–1673, but the notebook never calls the omission a limitation | Not stated; “preference share is not robustly identified” at lines 612–613 is not the `beta_ll` contract | `beta_ll_status`; `beta_ll_welfare_effective_value`; `beta_ll_cross_leisure_form` | **FAIL** |
| RURO/RUM: 6.3 vs 6.4; −24.2%; three destinations; +0.428 → −1.991 | Complete and correct, lines 1864–1934 | Complete and key-rendered in §18 and Q19, physical lines 166/176 | Not stated | 6.3→6.4 and rounded −24% at lines 519–520; rounded gap at 547; only the needs destination is named, not all three | Exact `rum_*` keys listed under discrepancies | **FAIL coverage** |
| Geography: 87.6% of access; 13.05% of I00; not causal | Complete and guarded, lines 2474–2499 and 2627–2631 | Complete and guarded in §17/Q17–Q18, physical lines 166/176 | Not stated | 13% and “not causal” at lines 592/609; 87.6% is absent | `geo_share_of_C_acc_raw`; `geo_share_of_I00_raw` | **FAIL coverage** |
| Sex subgroup: 19.6 vs 9.8 | 19.58 vs 9.79, lines 2612–2624 | 19.6 vs 9.8 in §17/Q16, physical lines 166/176 | Not stated | 19.6 vs 9.8, lines 600–604 | `subgroup_men_acc_share_raw`; `subgroup_women_acc_share_raw` | PASS values; incomplete notebook coverage |
| Obsolete/internal phrase scan | 34 hits | Reader-visible, post-render, and embedded-data hits; detailed below | 40 notebook hits + 5 cell-map hits | No hits | Registry excluded from the requested four-artifact prose grep | **FAIL** |

## Registry values for the state and decomposition audit

All state and contribution point/band keys below come from `tables/headline_decomposition_v1.csv`. The artifact displays are rounded versions of these values where present.

### Four singles states

| basis / reference | I00 point; RQMC band | I10 point; RQMC band | I01 point; RQMC band | I11 point; RQMC band |
|---|---|---|---|---|
| raw / female | `0.1342765561540117`; `[0.1323395837115014, 0.1362135285965221]` | `0.1483159928025005`; `[0.1467823742438407, 0.1498496113611603]` | `0.030968007072983`; `[0.0300573196720756, 0.0318786944738903]` | `0`; `[-6.762487618736419e-31, 6.762487618736419e-31]` |
| raw / male structural zero | `0.1342765561540117`; `[0.1323395837115014, 0.1362135285965221]` | `0.1359975812428928`; `[0.1336570174111281, 0.1383381450746575]` | `0.030968007072983`; `[0.0300573196720756, 0.0318786944738903]` | `-2.0352478302954915e-31`; `[-9.660254247518414e-31, 5.589758586927431e-31]` |
| equivalized / female | `0.1651054368471445`; `[0.1630913900801445, 0.1671194836141445]` | `0.1697155540038542`; `[0.1683314464361179, 0.1710996615715905]` | `0.030968007072983`; `[0.0300573196720756, 0.0318786944738903]` | `0`; `[-6.762487618736419e-31, 6.762487618736419e-31]` |
| equivalized / male structural zero | `0.1651054368471445`; `[0.1630913900801445, 0.1671194836141445]` | `0.1598397247236699`; `[0.1577603587168635, 0.1619190907304764]` | `0.030968007072983`; `[0.0300573196720756, 0.0318786944738903]` | `-2.0352478302954915e-31`; `[-9.660254247518414e-31, 5.589758586927431e-31]` |

Exact keys are `state_I{00,10,01,11}_{female,male}_{raw,equivalized}` and the corresponding exact `__rqmc_band` keys. The brace notation here abbreviates the displayed grid; it is not a literal registry key.

### Five singles contributions

Each cell is `point; RQMC band; share of I00`. The share has a point key but no share-band key in the registry.

| basis / reference | preferences | environment | job access | earning opportunities | endowments and needs |
|---|---|---|---|---|---|
| raw / female | `0.0084642852122471`; `[0.0075503278692388, 0.0093782425552553]`; `0.0630362101522682` | `0.1258122709417646`; `[0.124489477663436, 0.1271350642200932]`; `0.936963789847732` | `0.0200042817777703`; `[0.0187145549060242, 0.0212940086495163]`; `0.1489782159353708` | `0.0276822539770213`; `[0.0251600552395777, 0.0302044527144649]`; `0.2061585042832832` | `0.0781257351869729`; `[0.0766684440931391, 0.0795830262808067]`; `0.5818270696290777` |
| raw / male structural zero | `0.0146234909920509`; `[0.0139159306208809, 0.015331051363221]`; `0.1089057644230776` | `0.1196530651619608`; `[0.117890666013225, 0.1214154643106965]`; `0.8910942355769224` | `0.0182272212727959`; `[0.0170335918094355, 0.0194208507361563]`; `0.1357438840767543` | `0.0299474782444308`; `[0.0269234280394479, 0.0329715284494137]`; `0.2230283461401992` | `0.0714783656447339`; `[0.0700117598169577, 0.0729449714725102]`; `0.5323220053599687` |
| equivalized / female | `0.0131789449581366`; `[0.0123466940846208, 0.0140111958316523]`; `0.0798213869258452` | `0.1519264918890079`; `[0.1506558778819214, 0.1531971058960944]`; `0.9201786130741548` | `0.0159820855595331`; `[0.0149792984909266, 0.0169848726281397]`; `0.0967992687868267` | `0.0268136915715943`; `[0.0244368757425815, 0.029190507400607]`; `0.1624034440272162` | `0.1091307147578803`; `[0.1081069343269357, 0.1101544951888249]`; `0.6609759002601117` |
| equivalized / male structural zero | `0.0181168595982287`; `[0.0174678879804773, 0.0187658312159802]`; `0.1097290310009685` | `0.1469885772489157`; `[0.1453600258394945, 0.148617128658337]`; `0.8902709689990315` | `0.014262569872177`; `[0.0133737130759095, 0.0151514266684445]`; `0.0863846166700216` | `0.0288126537674288`; `[0.0259786256106405, 0.0316466819242171]`; `0.1745106297989672` | `0.1039133536093099`; `[0.1028273329595843, 0.1049993742590354]`; `0.6293757225300425` |

Exact key stems are `C_pref`, `C_env`, `C_acc`, `C_earn`, and `C_needs`, followed by `_{female,male}_{raw,equivalized}`; point shares add `_share`, and contribution bands add `__rqmc_band`.

### CR1 intervals actually present in the registry

All are female-primary/raw only and come from `tables/parameter_uncertainty_v1.csv`. This is the complete registry set; there are no male-reference or equivalized CR1 keys.

| exact registry key | interval |
|---|---|
| `I00_female_raw__cr1_interval` | `[0.1265054798962954, 0.1476004552022276]` |
| `I10_female_raw__cr1_interval` | `[0.1380949179360541, 0.1600459967144833]` |
| `I01_female_raw__cr1_interval` | `[0.0211053865838387, 0.044749799528547]` |
| `I11_female_raw__cr1_interval` | `[-2.3146699305643366e-31, 0]` |
| `C_pref_female_raw__cr1_interval` | `[0.005805322656376, 0.0144945261868043]` |
| `C_env_female_raw__cr1_interval` | `[0.1176117869956335, 0.1380149226185865]` |
| `C_acc_female_raw__cr1_interval` | `[0.015737693459865, 0.0284598783354103]` |
| `C_earn_female_raw__cr1_interval` | `[0.0209690499448844, 0.0378875433712228]` |
| `C_needs_female_raw__cr1_interval` | `[0.0719569420804525, 0.0821697126931477]` |
| `s_pref_female_raw__cr1_interval` | `[0.0422382635475491, 0.1088977103864352]` |
| `s_env_female_raw__cr1_interval` | `[0.8911022896135646, 0.9577617364524508]` |
| `C_geo_female_raw__cr1_interval` | `[0.01300698485765, 0.0260968300193562]` |
| `C_geo_over_I00_female_raw__cr1_interval` | `[0.0955627823280031, 0.1824441683885542]` |
| `C_oth_female_raw__cr1_interval` | `[0.0004047187309422, 0.006209818595329]` |
| `C_oth_over_I00_female_raw__cr1_interval` | `[0.0029474483125079, 0.0453360093764786]` |

## Discrepancies

1. **The model factors do not use the same symbols or factor names.** Paper lines 687–733 and deck lines 178–180 use four factors, with local-market access inside `g^E`: `g^E g^H g^Occ g^W`. HTML §6, physical lines 127–154, separates `g^Acc` and therefore assembles five terms. Notebook Markdown physical lines 789–790 uses `g^{market}` and does not name `g^Acc` or `g^Occ` separately. Registry key: **none**; the registry has no equation/symbol contract.

2. **The notebook and deck do not carry the complete W1 statement.** Paper lines 765–784 and HTML §13 (physical line 166) say uniform pay over the household's own reachable set, pay differences within the set are neutralized, and set differences remain. Notebook Markdown lines 673–679/789–795 only names W1 and its support. Deck lines 66 and 422–424 gives uniform pay over the reachable/own set but omits the latter two explicit clauses. Registry key: **none**; the registry has no W1 semantic key. The forbidden phrase `reference leisure` also appears in paper line 3870, although it refers to the alternative couples measure rather than W1.

3. **The requested state/decomposition uncertainty grid is not represented end to end.** Paper Table 7.1 (lines 2039–2055) is the broadest contribution display, but the complete four-state grid with bands is raw-only (lines 1982–1990), and CR1 state intervals other than I00 are not printed. HTML renders only five of 32 singles state point/band keys and 32 of 65 five-channel point/share/band keys; it uses eight of the 15 CR1 keys. Notebook cell 9 deliberately prints only the nine female-reference/raw point keys (cell-map line 17; notebook outputs 699–707). Deck gives selected rounded values without the grid. Exact registry keys are the state and contribution keys tabulated above. The registry itself has no share-RQMC keys and no male/equivalized CR1 keys.

4. **The deck mislabels Shapley attributions as quantities “removed.”** Lines 493–505 display the 58/21/15 Shapley channel shares, but line 505 labels the axis `share of measured welfare inequality removed (%)`; the couples comparison repeats `share ... removed (%)` at lines 619–626. This conflicts with paper lines 2099–2109 and HTML §22 Q14, both of which explicitly prohibit saying that a Shapley share removes a percentage. The deck correctly distinguishes environment-only 77% from rounded Shapley 94% at lines 451–452, but omits the preferences-only +10 leg. Registry keys: `C_needs_female_raw_share`, `C_earn_female_raw_share`, `C_acc_female_raw_share`, `C_env_female_raw_share`, `C_pref_female_raw_share`, `equalization_env_only`, `equalization_pref_only`.

5. **Reference labels are incomplete in notebook and deck.** Notebook line 679 says only female-reference/raw and supplies no male-reference convention or never-averaged rule. Deck lines 485–490 say `female reference` and `male reference`, not female primary and male structural-zero sensitivity, and never say the arms are not averaged. Paper lines 2219–2243 and HTML §§15/19/Q28 are correct. Registry keys: `state_I10_male_raw`, `state_I10_male_equivalized`, `C_pref_male_raw`, `C_pref_male_equivalized`, and `beta_l_nkids_male_status` (the last records the structural zero).

6. **The couples cross-leisure omission is not described as a limitation everywhere.** Notebook lines 12–15 and executed lines 1671–1673 correctly record absence, effective zero, and form, but never call this a limitation. The deck does not state the contract at all. Paper lines 2687–2719/3247–3257 and HTML §§11/20/Q21 do. Registry keys: `beta_ll_status`, `beta_ll_welfare_effective_value`, `beta_ll_cross_leisure_form`.

7. **The RUM/RURO comparison is incomplete in two artifacts.** Notebook contains none of the requested comparison. Deck lines 519–520 show 6.3→6.4 and rounded 24%, and line 547 shows rounded +0.43→−1.99, but the deck omits two of the three destinations and does not give −24.2%. Paper lines 1864–1934 and HTML §18/Q19 are complete. Registry keys: `rum_share_pref_RURO_raw`, `rum_share_pref_RUMB_raw`, `rum_inequality_drop_raw`, `rum_omitted_share_leaves_measured_total`, `rum_omitted_share_relabelled_as_needs`, `rum_omitted_share_relabelled_as_preferences`, `rum_leisure_gap_final`, `rum_leisure_gap_benchmark`.

8. **The geographic statement is incomplete in notebook and deck.** Notebook has no geographic result. Deck lines 592 and 609 round 13.05% to 13% and state `not causal`, but never show 87.6% of job access. Paper lines 2474–2499 and HTML §17/Q17–Q18 are complete. Registry keys: `geo_share_of_C_acc_raw`, `geo_share_of_I00_raw` (with `geo_share_of_I00_raw__band`).

9. **The sex-subgroup result is absent from the notebook.** Paper lines 2612–2624, HTML §17/Q16, and deck lines 600–604 agree after rounding on 19.6% for men versus 9.8% for women. Registry keys: `subgroup_men_acc_share_raw`, `subgroup_women_acc_share_raw`.

10. **Full negLL precision is not displayed consistently.** Notebook outputs and registry carry both full values. Paper carries the singles value exactly at line 3486 but rounds couples at line 2722; HTML embeds both exact values but renders both with four decimals; deck states neither. Registry keys: `negll_singles_final`, `negll_couples_final`.

11. **The raw couples contribution grid is not registry-backed.** Paper lines 2827–2830 display raw and equivalized couples component points. The registry has exact `couples_C_A_equivalized`, `couples_C_B_equivalized`, `couples_C_D_equivalized`, `couples_C_E_equivalized`, and `couples_C_P_equivalized` point/band keys, but no corresponding raw component keys. Therefore the raw row cannot be checked against the named registry. The couples state point/band keys do cover both bases.

## Obsolete/internal phrase hit ledger

The search was case-insensitive. `51` was counted only as a standalone integer/coordinate token, not as the decimal tail in values such as 35.51 or 51.23. Locations are `line:column`. The registry itself was not one of the requested four prose artifacts and is not included in this ledger.

### Paper — 34 hits

| term | every location | classification |
|---|---|---|
| `ruling` | `15:15`, `4162:146`, `4412:104` | forbidden/internal |
| `PROVISIONAL` | `31:18`, `35:62`, `166:48`, `622:43`, `2126:34`, `2547:9`, `3308:30` | forbidden |
| `PENDING` | `35:74`, `166:60`, `2126:46`, `2547:21`, `3308:42` | forbidden |
| `deputy` | `72:2`, `4162:114` | forbidden/internal |
| `S8` | `3474:60`, `3483:38`, `3584:16`, `4147:247`, `4240:71`, `4242:149` | all outside Appendix A.4; forbidden by the location rule |
| `LOC4` | `3475:38`, `3535:31`, `3584:33` | forbidden/internal |
| standalone `51` | `3588:50`, `3610:25`, `3621:51`, `4147:103`, `4193:118` | `3610:25` and `3621:51` are permitted in Appendix A.4; the other three are outside it |
| `reference leisure` | `3870:59` | forbidden phrase; occurs in Appendix D.3 |
| `bootstrap` | `3958:17`, `4086:739` | literal hits, both in the correct negated phrase “not a bootstrap”; still hits under the requested grep |

No paper hits: `removes 93.7`, `beta_ll estimated`, `C_P`.

### HTML

Reader-visible source text has five hits, all on the minified body line 166:

| term | exact reader-visible location | classification |
|---|---|---|
| `PROVISIONAL` | line 166, §16 “Splitting it further: the current status,” three occurrences; §16 “Why the channel is as large as it is,” one occurrence | forbidden |
| `PENDING` | line 166, §16 “Splitting it further: the current status,” one occurrence | forbidden |

Post-render, standalone `51` appears twice: line `157:533358`, §7 “The two boundary-active coefficients,” inside `.box.prov` (permitted); and line `176:43305`, §22 Q31, outside a provenance box (forbidden).

The minified embedded data are non-prose but were also searched, because the audit expressly required reading them:

| block | term | every source location | classification |
|---|---|---|---|
| `NOR-DATA` | `S8` | line 178, 140 occurrences | embedded registry metadata; outside a rendered provenance box, so the literal raw-file location rule fails |
| `NOR-DATA` | `LOC4` | `178:21644` | embedded registry metadata; forbidden/internal hit |
| `NOR-DATA` | `C_P` | `178:26361`, `178:26417`, `178:26685`, `178:26770`, `178:26948`, `178:27003`, `178:27128` | embedded couples key/reference metadata; forbidden/internal hit |
| `NOR-DATA` | standalone `51` | `178:39331`, `178:40130`, `178:40152`, `178:40421`, `178:41495`, `178:41554`, `178:41700` | embedded provenance metadata, but not a rendered provenance box |
| `AUX-DATA` | all searched terms | none | — |

No reader-visible or embedded HTML hits: `removes 93.7`, `reference leisure`, `beta_ll estimated`, `bootstrap`, `ruling`, `deputy`. No reader-visible `S8`, `LOC4`, or `C_P` hit occurs before considering the embedded data.

### Notebook — 40 hits

| term | every location |
|---|---|
| `bootstrap` | `59:9`, `87:8`, `266:14` |
| standalone `51` | `64:30`, `64:58`, `67:136`, `144:23`, `145:23`, `146:19`, `154:34`, `190:27`, `196:32`, `199:54`, `211:34`, `211:65`, `215:30`, `215:61`, `388:27`, `396:54`, `487:30`, `496:9`, `496:33`, `498:11`, `498:25`, `498:46`, `499:44`, `501:62`, `505:20`, `508:48`, `1712:235`, `1748:62`, `1785:30` |
| `S8` | `390:96`, `1609:39`, `1676:22` |
| `LOC4` | `423:55`, `458:55`, `1568:39` |
| `C_P` | `676:6`, `724:16` |

All are outside the only allowed S8/51 sites (HTML provenance boxes and paper Appendix A.4). No notebook hits: `removes 93.7`, `reference leisure`, `beta_ll estimated`, `PENDING`, `PROVISIONAL`, `ruling`, `deputy`.

### Cell map — 5 hits

| term | every location |
|---|---|
| `bootstrap` | `10:7` |
| standalone `51` | `10:158`, `13:42` |
| `S8` | `13:16` |
| `C_P` | `17:94` |

No cell-map hits for the other searched terms.

### Deck — zero hits

No searched obsolete/internal phrase occurs in the deck text layer.

## Bottom line

There is no evidence that a key-bound numeric span was populated from the wrong registry value: the embedded registry matches the external registry, every HTML span resolves, and the notebook's executed final gate reports exact equality for every key it prints (physical lines 1732–1733). The overall consistency gate still **fails** because semantic notation, presentation labels, required limitations/reference conventions, uncertainty coverage, and phrase/location discipline are not consistent across the four artifacts.
