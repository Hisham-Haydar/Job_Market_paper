"""Create the R11 deck from R9: two welfare perspectives, D held fixed, matched pair."""
from __future__ import annotations

from pathlib import Path

HERE = Path(__file__).resolve().parent
source = (HERE / "JMP_seminar_deck_r9.tex").read_text(encoding="utf-8")


def swap(old: str, new: str) -> None:
    global source
    if source.count(old) != 1:
        raise SystemExit("R11 deck anchor not found exactly once: " + old[:80])
    source = source.replace(old, new, 1)


swap("% JMP_seminar_deck_r9.tex -- V9 welfare-perspective update.",
     "% JMP_seminar_deck_r11.tex -- V11 outcomes-versus-prospects update.")
source = source.replace(r"\input{deck_numbers_r9}", r"\input{deck_numbers_r11}")
source = source.replace("make_deck_numbers_r9.py", "make_deck_numbers_r11.py")
swap(r"\graphicspath{{figures/}{figures/slides/}{figures/r7/}}",
     r"\graphicspath{{figures/}{figures/slides/}{figures/r7/}{figures/r11/}}")

swap("Seminar of 17 September. The welfare results use the own-set\n"
     "equal-consumption measure. Both welfare perspectives and their restricted decompositions are reported.",
     "Seminar of 17 September. Well-being is measured from two perspectives:\n"
     "the attained bundle (ATT) and the ex-ante opportunity prospect (EA).")

swap(r"""  \item The own-set equal-consumption money metric; in this empirical
        specification its direct reference collapses to universally available
        non-employment.
  \item Observed-bundle welfare and resource inequality, reported separately
        for single-adult and couple households.""",
     r"""  \item Two money-metric welfare perspectives: the bundle a household
        attains (ATT) and the opportunity prospect it faces (EA).
  \item An exact Shapley decomposition over preferences, geographic/temporal
        access and earning opportunities, holding household resources, needs
        and composition fixed.""")
swap(r"\caveat{The computed preliminary restricted-operator decomposition is in the backup appendix.}",
     r"\caveat{The current decomposition equalises preferences, geographic/temporal job access and systematic earning opportunities while holding household resources, needs and composition fixed.}")
swap("The welfare measure is taken from\nthe companion theory paper with Francois Maniquet. ",
     "The welfare side asks two questions: how well off a household is in the\n"
     "bundle it attains, and how valuable the job prospect it faces is. ")

swap(r"\section{The welfare measure}",
     r"\section{From choices to well-being: outcomes versus prospects}")
swap(r"""\headlineframe{Haydar--Maniquet $\Wone$: the consumption at home that would
leave the household exactly as well off.}""",
     r"""\headlineframe{ATT: how well off is the household in the bundle it actually
attains?}""")
swap("The most likely question here is whether I have just proved that measure one\n"
     "and measure four are the same thing. I have not, and the ruling is explicit\n"
     "about it.",
     "The most likely question here is whether this coincidence is a general\n"
     "identity. It is not.")

ea_frame = r"""
\begin{frame}
\headlineframe{EA: how valuable is the distribution of job prospects the
household faces?}
\slideeq{$\displaystyle\begin{gathered}
  J_i=\int e^{L_i(j)}\Big(\tfrac{C_i(j)}{\lambda_c}\Big)^{\beta_c}\gopp_i(j)\,d\nu,
  \qquad
  H_i=\int e^{L_i(j)}\gopp_i(j)\,d\nu,
  \\[0.3em]
  W^{EA}_i=\lambda_c\exp\!\Big[\tfrac{\log J_i-\log H_i}{\beta_c}\Big]
  \end{gathered}$}
\vfill
\begin{itemize}\itemsep0.4em
  \item $J_i$: the actual prospect over the whole estimated opportunity environment.
  \item $H_i$: same jobs and availability, equal consumption across jobs.
  \item $W^{EA}_i$: the flat consumption that makes the two prospects equally valuable.
\end{itemize}
\vfill
\caveat{The two measures answer different welfare questions. ATT evaluates the
bundle eventually reached against a common non-employment reference; EA
evaluates the whole distribution of potential job outcomes against a reference
that keeps the opportunity environment and equalises consumption across jobs.}
\note{The second perspective values the prospect itself. Every job enters,
weighted by how available it is and how much the household values it; the
reference keeps exactly those jobs and preferences but pays every job the same.
A common rescaling of the opportunity density cancels, so what matters is how
opportunity weight is spread across jobs. Neither perspective corrects the
other. Under the extreme-value shocks, log J is the expected utility of the best
reachable job up to a constant, so the measure treats taste-shock variety as
welfare-relevant; that is a normative position, and I flag it. The ex-ante
calculation passed all its numerical checks; that certifies the computation,
not causal identification, parameter uncertainty or normative uniqueness.}
\end{frame}
"""
swap("% ================================================================ 6 BASELINE",
     ea_frame + "\n% ================================================================ 6 BASELINE")
swap(r"\section{Equivalised $\Wone$-F distribution (primary)}",
     r"\section{Attained-bundle distribution, equivalised}")

matched_frame = r"""
\begin{frame}
\headlineframe{Two matched men, almost identical tastes, different opportunity
environments.}
\begin{center}
\includegraphics[height=0.64\textheight]{fig_matched_households_v11.png}
\end{center}
\caveat{Same occupation group, hours band and wage quintile. A has
\MatchedAccessRatioREleven{} times B's employment mass; B's wage-offer location
is \MatchedWageGapREleven{} log points higher. A stated-rule teaching example:
not causal, not representative.}
\note{What does unequal opportunity mean in this model? These two single men
look alike in an income table and have nearly identical estimated leisure
profiles. Household A's employment share of opportunity mass is
\MatchedEmpShareAREleven{}, household B's \MatchedEmpShareBREleven{}. B's wage
offers are better: its offer distribution first-order stochastically dominates
A's. But A faces more offers paying at least any given wage over essentially all
offer mass. Hours and occupation opportunities are identical by construction in
this specification. Neither household is better placed on every margin, and
which one is better off depends on the welfare question, which is exactly where
the two perspectives come in.}
\end{frame}
"""
swap("% ================================================================ 5 W1",
     matched_frame + "\n% ================================================================ 5 W1")

swap(r"\headlineframe{The welfare perspective changes which opportunity channel dominates.}",
     r"\headlineframe{The welfare question changes which labour-market inequality matters.}")
swap(r"{\bfseries Attained bundle: the realised job}", r"{\bfseries ATT: the attained bundle}")
swap(r"{\bfseries Ex ante: the whole job prospect}", r"{\bfseries EA: the whole opportunity prospect}")
swap(r"""{\color{chacc}\bfseries Singles: access $\simeq 3\times$ earnings;}\\
couples: earning opportunities $>$ access.""",
     r"""{\color{chacc}\bfseries Singles: access $\simeq 3\times$ earnings;}\\
couples: no reversal, earnings $>$ access.""")
swap(r"""\caveat{Cells are access plus earning opportunities as a share of each
perspective's own baseline Gini. Neither perspective is designated primary.}""",
     r"""\caveat{The importance assigned to different labour-market inequalities
depends on whether welfare evaluates the realised outcome or the opportunity
prospect itself. Cells: access plus earning opportunities as a share of each
perspective's own baseline Gini, holding resources, needs and composition fixed.
Neither perspective is designated primary.}""")

swap(r"""\caveat{Household resources, needs and composition are held fixed. Personal
occupation access, hours-band access and node-level alternative
characteristics are not equalised by $A$.}""",
     r"""\caveat{Household resources, needs and composition are held fixed; adding them
as a fourth pathway $D$ is a planned extension, and $A+B+D$ would not be an
opportunity share. Personal occupation access and hours-band access are not
equalised by $A$.}""")

(HERE / "JMP_seminar_deck_r11.tex").write_text(source, encoding="utf-8", newline="\n")
(HERE / "JMP_seminar_deck_r11_rehearsal.tex").write_text(
    "% Second-screen rehearsal build of the R11 deck: same source, notes on the right.\n"
    "\\def\\RehearsalDeck{}\n\\input{JMP_seminar_deck_r11}\n",
    encoding="utf-8", newline="\n")
print("wrote JMP_seminar_deck_r11.tex and rehearsal driver")
