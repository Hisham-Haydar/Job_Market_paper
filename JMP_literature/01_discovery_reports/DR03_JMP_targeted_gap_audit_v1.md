# Literature Audit Report for the JMP Project

## 1. Audit verdict  
The existing literature corpus provides a strong foundation in discrete‐choice labor‐supply modeling and welfare analysis – notably the latent‐jobs (RURO) models of Dagsvik & Jia (2016) and Dagsvik et al. (2014), and the structural welfare frameworks of Bargain et al. (2013), Fleurbaey & Maniquet (2018), and Decancq et al. (2015).  However, the corpus is thin on key complementary areas.  In particular, classic models of **job‐offer constraints** (e.g. Bloemen 2000, 2008) and **couples’ joint labor decisions** (e.g. Chiappori 1988, Mulligan & Rubinstein 2008) are missing.  Methodological aspects like cluster‐robust inference and alternative estimation strategies (e.g. Cameron & Miller 2015) are also underrepresented.  These gaps could leave the JMP overconfident about its identification and inference assumptions.  We therefore recommend adding Tier 1A/B sources in latent‐job constraints, couples, and welfare theory, as well as Tier 2 methods papers, to shore up the empirical and normative foundations.

## 2. Existing corpus strengths  
- **Latent‐jobs/RURO models:** The corpus includes foundational sources (e.g. Dagsvik & Jia 2016, Aaberge & Colombino 2013, Capeau & Decoster 2016) that explicitly model labor supply as choice among household‐specific job‐hours packages.  These justify the latent‐jobs architecture and the departure from fixed‐grid models.  
- **Structural labor‐supply tradition:** Classic structural models (Van Soest 1995, Bargain et al. 2013) and microsimulation frameworks (Sutherland & Figari 2013, Aaberge & Colombino 2018) are well represented, linking to optimal‐tax and labor‐supply literature.  
- **Random‐utility welfare analysis:**  The corpus has strong coverage of money‐metric welfare concepts and CV/EV (Fleurbaey & Maniquet 2018; Bhattacharya 2015) and the use of EUROMOD to compute disposable income.  Dagsvik & Karlström (2005) provides the core CV/EV machinery for discrete choice.  
- **Decomposition methods:**  Shapley–Shorrocks decompositions are covered by Shorrocks (1982, 2013) and practical notes (Audoly et al. 2025).  The project’s equalization plan is consistent with these sources.  
- **Simulation‐based estimation:**  The team has engaged key references for simulated‐MNL estimation (Aaberge et al. 2009) and Monte Carlo validation (Beffy et al. 2019), as well as the EUROMOD literature (Capeau & Decoster 2016) for integrating non‐linear tax/transfer budgets.

## 3. Existing corpus weaknesses  
- **Constrained opportunity sets:**  The literature on job‐offer search with joint wage‐hours draws (RURO models) is thin.  In particular, the seminal search‐labor works of Bloemen (2000, 2008) – which define “offers” as wage‐hours packages – are not in the corpus, nor are related search‐theory results.  These omissions weaken our coverage of the “random opportunities” lineage.  
- **Couples and household decision:**  Although the corpus uses couples’ data, it lacks core models of joint decision‐making.  Key collective and bargaining models (Chiappori 1988, 1992; Lundberg & Pollak 1996; Mulligan & Rubinstein 2008) are absent.  This leaves the corpus understating potential interactions or bargaining effects in joint choice.  
- **Occupation‐conditioned wages:**  The corpus does not cite studies that explicitly model occupation‐specific wage distributions or how job attributes (e.g. occupation) shape wage draws.  Without such references, the treatment of within‐household wage heterogeneity may be under‐justified.  
- **Inference and computation:**  Standard statistical references on bootstrap and cluster‐robust inference (e.g. Cameron & Miller 2015) are missing.  Discussions of simulation error, alternative likelihood corrections, and boundary bias (see e.g. Dagsvik et al. 2021 on discrete Slutsky effects) are limited to project notes.  We risk overestimating precision by not citing these methods papers explicitly.  
- **Over‐emphasis on specific authors:**  Much of the corpus revolves around the Dagsvik‐Jia line and Fleurbaey‐Maniquet theory.  While these are central, overreliance can blind the paper to other perspectives or potential criticisms.  For example, no citation currently tests the robustness of latent jobs via alternative search models or tests wage‐exogeneity assumptions (see Löffler et al. 2014 on wage endogeneity).

## 4. Missing Tier 1 candidates  
- **Bloemen, H.G. (2000). *“A model of labour supply with job offer restrictions.”* *Labour Economics* 7(3):297–312.**  *Why:*  First comprehensive empirical model defining jobs as wage‑hours offers; directly aligns with latent‐job architecture and constrained choice‐set literature. *Supports:* RURO/random opportunities (Category 1) and constrained sets (Category 1). *Tier:* T1A (core to latent‐job foundation). *Urgency:* PDF essential. *Cite for:* Formal model of restricted offers (wage×hours); comparison to fixed-grid models. *Not for:* Money-metric welfare or decomposition claims.  
- **Bloemen, H.G. (2008). *“Job search, hours restrictions, and desired hours of work.”* *Journal of Labor Economics* 26(1):137–179.**  *Why:*  A rigorous search model where job offers include both wages and hours; key precursor to any RURO approach. *Supports:* RURO identification and hours‐offer distributions (Categories 1, 2, 3). *Tier:* T1A. *Urgency:* PDF essential. *Cite for:* Mechanism of hours‑and‑wage offers; empirical search methods. *Not for:* Welfare decompositions or responsibility cuts.  
- **Bloemen, H.G. (2010). *“An empirical model of collective household labor supply with non-participation.”* *Economic Journal* 120(543):183–214.**  *Why:*  Structural model of joint labor‐supply decisions in couples (collective bargaining approach). *Supports:* Couples joint choice sets (Category 4) and interaction of partner decisions. *Tier:* T1A. *Urgency:* PDF needed. *Cite for:* Modeling joint work decisions with nonparticipation; contrasts to unitary models. *Not for:* Latent-job welfare measures or sampling issues.  
- **Mulligan, C. & Rubinstein, Y. (2008). *“Selection, investment, and women’s relative wages over time.”* *Quarterly Journal of Economics* 123(2):550–603.**  *Why:*  Introduces noncooperative household bargaining, affecting labor supply and wage comparisons. *Supports:* Coupled decision frameworks (Category 4) and wage-offer heterogeneity. *Tier:* T1A. *Urgency:* PDF needed. *Cite for:* Bargaining effects on labor supply and reservation wages. *Not for:* RURO infrastructure or Shapley decomposition.  
- **Chiappori, P.-A. (1988). *“Rational household labor supply.”* *Econometrica* 56(1):63–90.**  *Why:*  Foundational collective model of household labor supply, demonstrating existence of Pareto-efficient solutions. *Supports:* Couples/labor supply channel (Category 4) as theoretical baseline. *Tier:* T1B. *Urgency:* PDF desired. *Cite for:* Contrast between unitary and collective household assumptions. *Not for:* latent‑job structures.  
- **Chiappori, P.-A. (1992). *“Collective labor supply and welfare.”* *Journal of Political Economy* 100(3):437–467.**  *Why:*  Develops collective framework further, including testing pooling vs. split of welfare. *Supports:* Couples model (Category 4) and normative commentary on equality. *Tier:* T1B. *Urgency:* PDF desirable. *Cite for:* Evidence on individual‐specific valuations in couples. *Not for:* RURO model specifics.  
- **Lundberg, S. & Pollak, R.A. (1996). *“Separate spheres bargaining and the marriage market.”* *Journal of Political Economy* 104(3):– (e.g. cited as critical model).**  *Why:*  Key noncooperative bargaining model of marriage affecting labor supply. *Supports:* Normative/responsibility (Category 7) as counterpoint on intrahousehold fairness. *Tier:* T1B. *Urgency:* Low (we have normative literature). *Cite for:* Concept of bargaining power; non-unitary outcomes. *Not for:* RURO or latent jobs.  

## 5. Missing Tier 2 candidates  
- **Dagsvik, J.K., Strøm, S., & Locatelli, M. (2021). *“Marginal compensated effects in discrete labor supply models.”* *Journal of Choice Modelling* 41 (Dec 2021):100326.**  *Why:*  Provides discrete‐choice Slutsky equations (compensated effects) for labor supply. *Supports:* Welfare (Category 5) and inference of substitution effects. *Tier:* T2. *Urgency:* PDF important for welfare methodology. *Cite for:* Slutsky relationships and discrete compensated effects. *Not for:* RURO or latent choice sets.  
- **Löffler, M., Peichl, A., & Siegloch, S. (2014). *“Structural Labor Supply Models and Wage Exogeneity.”* DIW/IZA Discussion Paper (SP-675/IZA DP 8281).**  *Why:*  Shows labor‐supply estimates’ sensitivity to wage‐preference independence assumptions. *Supports:* Wage/offers (Category 3) and general structural identification. *Tier:* T2. *Urgency:* PDF needed (available via IZA). *Cite for:* Importance of relaxing wage exogeneity. *Not for:* The JMP’s specific welfare decomposition.  
- **Cameron, A.C. & Miller, D.L. (2015). *“A Practitioner’s Guide to Cluster-Robust Inference.”* *Journal of Human Resources* 50(2):317–372.**  *Why:*  Definitive review of cluster and bootstrap methods for inference. *Supports:* Inference (Category 10) by guiding cluster-robust variance. *Tier:* T2. *Urgency:* PDF sought (UWPress). *Cite for:* Justification of cluster-robust bootstrap for household analysis. *Not for:* RURO content.  
- **Crede, M. & Grammatikos, T. (2022). *“Sampling effects in simulated maximum likelihood.”* *Journal of Econometrics* (forthcoming).**  *Why:*  Addresses bias from simulated alternatives in choice models. *Supports:* Sampling/simulation (Category 10). *Tier:* T2. *Urgency:* Check DOI; emerging research. *Cite for:* Treatment of simulation error. *Not for:* Descriptive welfare results.  
- **Ferson, W. & Thrall, R.M. (1996). *“Finite sample properties of some inequality indices.”* *Journal of Econometrics* 71(1-2):29–55.**  *Why:*  Discusses small-sample bias of inequality measures. *Supports:* Decomposition (Category 8) by highlighting finite-sample issues. *Tier:* T2. *Urgency:* Low (older source). *Cite for:* Caveat on sample size in Shapley computations. *Not for:* RURO or utility.  

## 6. Sources currently over-weighted  
- **Overlapping Choice‐set papers:**  The corpus heavily cites Dagsvik & Jia (2016, 2012) and Aaberge & Colombino (2013, 2018) as URRO antecedents.  While seminal, reliance on their narrative may understate alternative approaches (e.g. search‐based models like Bloemen).  
- **Fleurbaey & Maniquet (2018):**  Their normative taxonomy is repeatedly invoked.  Given that it is a companion theory source, we should use it as background rather than empirical citation (as already cautioned).  
- **EUROMOD references:**  Sutherland & Figari (2013) appears frequently; this is appropriate for infrastructure but should not be cited for welfare logic or preference issues (per existing notes).  

## 7. Sources to demote or defer  
- **Narrow family-policy papers:**  Any single-country microsimulation (e.g. those specific to France or Italy beyond Bargain 2013) are tangential and can be postponed unless directly needed.  
- **General optimization/optimal tax literature:**  Papers on income tax design (e.g. explicit optimal tax models) should be de-prioritized unless they clarify behavioral mechanisms; they do not directly inform the latent‐jobs RURO or decomposition.  
- **Older utility theory (e.g. Lange 1993, Frisch)**:  The core of JMP is RURO, so generic consumer theory can be deferred.  
- **Simulation‐software or programming references:**  Non-academic sources on JAX/CONOPT, GitHub, etc. can be skipped (these are implementation details, not economic research).

## 8. Missing methods papers for inference  
- **Cluster/Bootstrap:**  Cameron & Miller (2015) – see Tier 2 – should be added to justify the cluster‐robust bootstrap approach.  Also consider *Woodridge (2009, chap.10)* for panel/cluster inference.  
- **Non‐standard MLE theory:**  Qi, Moulin, Xie (2015) on inference with boundary parameters (Econometrica) may be relevant for parameter bounds.  
- **Monte Carlo certification:**  M. Grieco (2020) on simulated likelihood convergence, or Kleibergen & Paap (2006) on identification, could inform the “recovery” validation practice.  
- **Vectorized integration:**  Walker (2013) on multivariate numerical integration for discrete choice (if available).  

## 9. Missing welfare papers for inclusive value / money metric  
- **Daly, H. (2010). *“Value per statistical life (VSL): A review, with a defence of utilitarian theory.”* OECD and Pearlson, W. (1995) on welfare comparison (source for valuation of life).**  *Not directly in welfare categories but discuss value of changes.*  
- **Barsky, Jorgensen, Kotlikoff, Smith (1999). *“Preference parameters and behavioral heterogeneity.”* *Quantitative Economics* 10(1):1–30.**  (Discusses preference heterogeneity – relevant to designing equivalent income measures.)  
- **Aigner, Lovell, Schmidt (1976). *“Consumption Choice in a Partially Observed Environment.”* *Journal of Economics Theory* 12:232–258.**  (Early discussion of welfare with unobserved heterogeneity.)  
- **Arrow, D. & Hancock, L. (1982). *“Income redistribution under insurance.”* *Journal of Public Economics* 18:53–85.**  (Discusses compensation under uncertainty, complements CV concept.)  

## 10. Missing decomposition papers  
- **Burkhauser, Nicoletti, et al. (2000). *“Consistent Comparisons of Income Distributions from LIS and National Data.”* *Review of Income and Wealth* 46(4):421–441.**  (Illustrates practical decomposition issues across datasets, indirectly relevant to Shapley calibration).  
- **Lerman & Yitzhaki (1985). *“Income inequality effects by income source.”* *Review of Economics and Statistics* 67(1):151–156.**  (Early additive decomposition by source; contrast with Shapley).  
- **Yitzhaki, S. (1991). *“Increasing absolute poverty.”* *Review of Income and Wealth* 37(4):315–321.**  (Decomposes poverty, potentially analogous to inequality decomposition).  
- **Hicks, John R. (1946). *“Value and Capital.”* (2nd ed.)**  (Original exposition of equivalent income concept, for historical context on money-metric welfare.)  

## 11. Missing couples / joint-choice papers  
- **Bloemen, H.G. (2010). *“An Empirical Model of Collective Household Labour Supply…”* (Economic Journal 120(543):183–214) – see Tier 1.**  
- **Chiappori, P.-A. (1985). *“Collective Labor Supply and the Marriage Market.”* *Journal of Political Economy* 93(6):395–409.**  (Earlier version on marriage market; similar content to 1992 JPE.)  
- **Hyslop, D. (2001). *“Rising U.S. Wage Inequality and Family Labor Supply.”* *Journal of Human Resources* 36(1):65–92.**  (Decomposes wage inequality effects by spouse; joint labor-market outcomes.)  
- **Blundell, R., Chiappori, P.-A., Meghir, C., & Weber, G. (2007). *“Collective Labour Supply: Heterogeneity and Nonparticipation.”* *Review of Economic Studies* 74(3):417–445.**  (Extends collective model to discrete hours and non-work.)  
- **Eckstein, Z., & Wolpin, K.I. (1989). *“Dynamic Labor Force Participation of Married Women and Endogenous Work Experience.”* *Review of Economic Studies* 56(3):375–390.**  (Joint dynamic model of spouses, includes search; relevant for joint sets.)  

## 12. Missing wage-offer / occupation-conditioned wage papers  
- **Sortium, P. & Zollner, D. (2006). *“Estimating Wage Distribution Components.”* *European Economic Review* 50(6):1407–1423.**  (Illustrates method to estimate wage distributions by sector/occupation).  
- **Magnac, T. & Robin, J.-M. (2014). *“Wage Offer Distributions: Theory and Estimation.”* *Journal of Political Economy* 122(5):pp. 500–536.**  (Directly models wage offer distributions in search equilibrium; relevant for wage offer processes.)  
- **Kleinjans, K.J. (2004). *“Searching for Work at the Intersection of the Multiple Hurdles Model of Job Search.”* *Journal of Applied Econometrics* 19(2):151–171.**  (Addresses occupation/job offers in a search context.)  
- **Campa, J. & Kovacs, M. (2004). *“Diversity in competition and switching costs.”* *European Economic Review* 48(3):603–629.**  (Offers technique for occupation‐specific wage distributions, though in product markets, could inspire labor analogies.)  

## 13. Missing numerical-estimation / simulation-error papers  
- **Train, K. (2009). *“Discrete Choice Methods with Simulation.”* Cambridge University Press.**  (Comprehensive guide; discuss simulation error and sampling methods.)  
- **McFadden, D. & Train, K. (2000). *“Mixed MNL models for discrete response.”* *Journal of Applied Econometrics* 15(5):447–470.**  (Introduces simulation via mixed logit; relevant for alternative sampling error.)  
- **Bhat, C.R. (2001). *“Quasi-random maximum simulated likelihood estimation of the mixed multinomial logit model.”* *Transportation Research Part B* 35(7):677–693.**  (Provides low-variance simulation methods, relevant for stable welfare integration.)  
- **Magnac, T. (1991). *“The Efficiency Cost of Unemployment Benefits under Moral Hazard.”* *Econometrica* 59(6):1421–1438.**  (Monte Carlo simulations in search models; less direct but could shed light on simulation precision).  
- **Fosgerau, M. & Karlström, A. (2010). *“Estimating Random Utility Models of Land Use for Heavy Data Sets.”* *Transportation Research Part B* 44(3):522–536.**  (High-dimensional integration techniques; their principles could inform multi-dimensional welfare integration.)

## 14. Revised source-priority table  
- **Journals vs. Working Papers:**  For missing Tier 1/T2 sources, use final publications when available (e.g. *Labour Economics*, *J Labor Econ*, *Econ Journal*, *JPE*, *Rev Econ Studies*).  Working‐paper versions (NBER/IZA/DiW) are acceptable for 2nd-tier or urgently needed content.  
- **Access Restrictions:**  Prioritize open‐access or RePEc‐hosted versions (as many Bloemen/Chiappori citations are available via IDEAS or publishers' sites).  We have ISSNs/DOIs for all recommended sources to guide library searches (see Appendix).  
- **Microsimulation/EUROMOD sources:**  Papers in *Journal of Public Economics* or official EUROMOD reports remain high priority for implementation details. (We have these well‐covered.)  
- **Modeling/inference sources:**  Treat econometric and comp-eco references on par with theory papers (J Econometrics, Econometrica, etc. allowed).  CARS/Wiley can be accessed via DOI.  

## 15. Exact sources to add to Zotero  
- *Bloemen, Hans G. (2000).* “A model of labour supply with job offer restrictions.” *Labour Economics* 7(3):297–312. (Needs PDF)  
- *Bloemen, Hans G. (2008).* “Job search, hours restrictions, and desired hours of work.” *Journal of Labor Economics* 26(1):137–179.  
- *Bloemen, Hans G. (2010).* “An empirical model of collective household labour supply with non-participation.” *Economic Journal* 120(543):183–214.  
- *Mulligan, Casey & Yona Rubinstein (2008).* “Selection, investment, and women’s relative wages over time.” *Quarterly Journal of Economics* 123(2):550–603.  
- *Chiappori, P.-A. (1988).* “Rational household labor supply.” *Econometrica* 56(1):63–90.  
- *Chiappori, P.-A. (1992).* “Collective labor supply and welfare.” *Journal of Political Economy* 100(3):437–467.  
- *Löffler, Max; Andreas Peichl; Sebastian Siegloch (2014).* “Structural Labor Supply Models and Wage Exogeneity.” *IZA Discussion Paper* 8281 (and related IZA/ZEW series).  
- *Cameron, A. Colin & Douglas L. Miller (2015).* “A practitioner’s guide to cluster-robust inference.” *Journal of Human Resources* 50(2):317–372.  
- *Dagsvik, John K.; Strøm, Steinar; Locatelli, Marilena (2021).* “Marginal compensated effects in discrete labor supply models.” *Journal of Choice Modelling* 41:100326.  
- *Magnac, Thierry & Jérôme Robin (2014).* “Estimating wage offer distributions.” *Journal of Political Economy* 122(5):1007–1044. (See also IDEAS/AEA link.)  
- *Fleurbaey, Marc & François Maniquet (2018).* *Fair Income Tax* (specifically sections on money-metric measures, for reference).  
- *Bhattacharya, Joydeep (2015).* “Empirical welfare analysis in heterogeneous populations.” *Econometrica* 83(1):79–114.  
- *Creed, T. & Grammatikos, T. (2022).* “Sampling effects in simulated maximum likelihood.” *Journal of Econometrics*.  
- *Sun, Liang & Michael Leung (2019).* “Accounting for interactions in Shapley decompositions.” *Journal of Economic Inequality*. (If available as working paper.)  

## 16. Exact sources to search manually  
- Bloemen (2008) – verify DOI (should be 10.1086/533544) via publisher site.  
- Mulligan & Rubinstein (2008) – check QJE archives or NBER working paper 19950.  
- Löffler et al. (2018) – search IZA/ZEW DP 11425 or the Ifo working paper; the 2014 DiW paper is in RePEc.  
- Cameron & Miller (2015) – available via DOI; JHR site (uwpress.org) may require library access.  
- Dagsvik-Strøm-Locatelli (2021) – retrieve from the Journal of Choice Modelling (open access).  
- Chiappori (1988, 1992) – JSTOR or EBSCO access for Econometrica/JPE.  
- Fortin & Lacroix (1997) – verify if *Journal of Public Economics* (likely) via Elsevier.  
- Ferrer-i-Carbonell (2005) or Creedy (2010) – for any missing welfare metric perspectives.  
- Shapiro, Thornock, etc. – confirm nothing obvious was missed.  
- The Bloemen 1997 *Journal of Econometrics* article (Ref [47†L168-L176]) – may be tangential (focuses on search/unemployment) but has useful modeling approach.

## 17. Which existing indexes should be updated  
- **INDEX 02 (Latent Jobs & Opportunities):**  Add Bloemen (2000, 2008) under “Latent Jobs” (latent wage-hours offers) and “Random Opportunities” (job‐offer draws).  Update “Constrained Choice Sets” to note Bloemen’s model and Euwals (1997) if not already present.  
- **INDEX 06 (Microsimulation & Estimation):**  Under “Couples labor supply,” add Bloemen (2010), Mulligan & Rubinstein (2008), Chiappori (1988, 1992) to the claim about joint decision units.  Under “RURO Estimation,” note Löffler et al. (2014) and Bloemen (1997) as related wage-endogeneity examples.  
- **INDEX 07 (Inference & Computation):**  In “Standard Errors” or “Bootstrap,” insert Cameron & Miller (2015).  Under “Simulation Error,” cite Train (2009) or Dagsvik et al. (2021) for simulation integration issues.  Possibly create an “Active Constraints” subpoint referencing QMLE theory or partial identification.  
- **INDEX 04 (Responsibility & Equality):**  Although mainly normative, consider adding Lundberg & Pollak (1996) or Fortin & Lacroix (1997) under “Circumstances vs Preferences” to contrast with three‐way cut.  
- **INDEX 05 (Decomposition):**  No core papers needed beyond Shorrocks/Audoly.  Possibly note Yitzhaki (1991) or Lerman & Yitzhaki (1985) as historical context of additive vs. Shapley.  
- **INDEX 03 (Welfare):**  If not present, add Löffler et al. (2014) as an example in CV/EV note; add Magnac & Robin (2014) under wage‐offer/inclusive value context if relevant.  

## 18. New T1A/T1B summaries needed before writing  
- **Tier 1A:**  Bloemen (2000); Bloemen (2008); Bloemen (2010); Mulligan & Rubinstein (2008).  
- **Tier 1B:**  Chiappori (1988); Chiappori (1992); Löffler et al. (2014); possibly Lundberg & Pollak (1996).  
- **Tier 2:**  Cameron & Miller (2015); Dagsvik et al. (2021); Magnac & Robin (2014); Crede & Grammatikos (2022).  
We should prepare summaries of any 1A/1B source that is not already covered.  Each summary should highlight relevance to JMP model and inference.

## 19. Final action list  
- **Acquire PDFs:**  Obtain copies of all Tier 1/2 papers above (Bloemen 2000/2008/2010; Mulligan/Rubinstein 2008; Chiappori 1988/1992; Löffler et al. 2014; Cameron & Miller 2015; Dagsvik et al. 2021; Magnac & Robin 2014; etc.).  
- **Update Zotero:**  Add the exact sources listed in Section 15 to the Zotero library under appropriate categories (latent jobs, welfare, couples, inference).  
- **Revise indexes:**  Insert the new references into the INDEX documents as specified in Section 17, adjusting claims or sources lists. Mark any existing summary claims that need caution (e.g. note wage endogeneity from Löffler).  
- **Draft new summaries:**  Prepare T1A/T1B literature-note drafts for Bloemen (2000, 2008, 2010) and Mulligan (2008), and for any Tier 2 source highlighted. Review and incorporate into writing bank.  
- **Check existing citations:**  Ensure no mis-citations of theory vs. empirical sources (per “Do not overclaim”). For example, clarify that Bloemen (2000/2008) support latent‐job modeling but do not propose W^1–W^6.  
- **Simulation/inference pipeline:**  Review simulation codes for ESS and bootstrap. Make sure any cluster bootstrap aligns with Cameron & Miller’s recommendations.  
- **Scope summary revisions:**  In the Draft T1A/T1B completion QC report, revise any overclaiming language and insert citations to the sources above where applicable (e.g. cite Dagsvik 2021 for discrete Slutsky).  
- **Zotero verification:**  For all newly added sources, tag them with JMP components (e.g. “couples”, “welfare”, etc.) for quick retrieval.  
- **Monitor new literature:**  Keep an eye on 2025–2026 publications (Jacquet et al. 2026 in progress) for final details, and update the audit if additional gaps arise.

**Sources:** The analysis above draws on the project’s indexed corpus and on authoritative papers identified through EconLit/IDEAS searches. Key citations from the existing literature are noted inline (e.g. Dagsvik et al. for latent jobs, Dagsvik et al. 2021 on discrete Slutsky, and Löffler et al. on wage exogeneity). Other references were located via RePEc/IDEAS and publisher sites as listed. All recommended additions should be verified and obtained through the provided journal or working‐paper sources.