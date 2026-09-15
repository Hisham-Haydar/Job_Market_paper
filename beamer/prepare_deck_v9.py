"""Create the R9 deck with one additional two-perspective welfare slide."""
from __future__ import annotations

from pathlib import Path


HERE = Path(__file__).resolve().parent
source = (HERE / "JMP_seminar_deck_r7.tex").read_text(encoding="utf-8")
source = source.replace(
    "% JMP_seminar_deck_r7.tex -- the 17 September seminar deck, R7 content.",
    "% JMP_seminar_deck_r9.tex -- V9 welfare-perspective update.",
    1,
)
source = source.replace(r"\input{deck_numbers_r7}", r"\input{deck_numbers_r9}")
source = source.replace("make_deck_numbers_r7.py", "make_deck_numbers_r9.py")
source = source.replace(
    r"\title{Unequal Job Opportunities and the Measurement of Welfare Inequality}",
    r"\title{Unequal Job Opportunities and Well-Being Inequality: A Latent-Jobs Structural Decomposition}",
    1,
)
source = source.replace(
    "% The distinct ex-ante opportunity-prospect metric is definition-only and\n"
    "% numerically blocked; no numerical result for it is present in this deck.",
    "% Certified ex-ante results are reported beside the attained-bundle results.\n"
    "% Neither welfare perspective is designated primary.",
    1,
)

stale = (
    "A separately defined ex-ante metric is being reconstructed for comparison. "
    "Historical ex-ante percentages are not current results and are not shown. "
    "The verified attained-bundle measure and its observed-bundle results remain "
    "the current welfare evidence; no settled comparison between the two metrics "
    "is available."
)
current = (
    "The certified ex-ante calculation is now reported as a separate perspective "
    "beside the attained-bundle measure. The two measures disagree about the "
    "dominant channel for single-adult households: earnings dominate the realised "
    "job, while access is about three times earnings for the whole prospect. "
    "Neither perspective is designated primary."
)
source = source.replace(stale, current)
stale_backup = (
    "A preliminary P/A/B decomposition has been computed for the attained-bundle "
    "money metric, holding resources, needs and composition fixed. It is a "
    "restricted counterfactual exercise, not a comprehensive share of inequality "
    "due to all opportunities. A separately defined ex-ante metric is being "
    "reconstructed for comparison; neither historical ex-ante percentages nor a "
    "settled cross-estimand conclusion are reported here."
)
current_backup = (
    "The attained-bundle and ex-ante decompositions apply the same restricted "
    "three-pathway game while holding resources, needs and composition fixed. "
    "The ex-ante calculation is numerically certified; the attained-bundle "
    "counterfactual remains preliminary. Neither is a comprehensive or causal "
    "share of inequality due to all opportunities."
)
source = source.replace(stale_backup, current_backup)

slide = r'''
% ============================================================ V9 COMPARISON
\begin{frame}
\headlineframe{The welfare perspective changes which opportunity channel dominates.}
\vspace{0.2em}
\begin{columns}[T,onlytextwidth]
\begin{column}{0.485\textwidth}
\begin{beamercolorbox}[rounded=true,sep=0.8em]{block body}
{\bfseries Attained bundle: the realised job}\par\smallskip
\decktable{\begin{tabular}{lcc}
\toprule
& raw & equivalised \\
\midrule
single adult & \AttOppSinglesRawRNine\% & \AttOppSinglesEqRNine\% \\
couple       & \AttOppCouplesRawRNine\% & \AttOppCouplesEqRNine\% \\
\bottomrule
\end{tabular}}
\smallskip
{\color{chearn}\bfseries Earning opportunities $>$ access}\\
in both populations and at both scales.
\end{beamercolorbox}
\end{column}
\begin{column}{0.485\textwidth}
\begin{beamercolorbox}[rounded=true,sep=0.8em]{block body}
{\bfseries Ex ante: the whole job prospect}\par\smallskip
\decktable{\begin{tabular}{lcc}
\toprule
& raw & equivalised \\
\midrule
single adult & \EAOppSinglesRawRNine\% & \EAOppSinglesEqRNine\% \\
couple       & \EAOppCouplesRawRNine\% & \EAOppCouplesEqRNine\% \\
\bottomrule
\end{tabular}}
\smallskip
{\color{chacc}\bfseries Singles: access $\simeq 3\times$ earnings;}\\
couples: earning opportunities $>$ access.
\end{beamercolorbox}
\end{column}
\end{columns}
\vfill
\caveat{Cells are access plus earning opportunities as a share of each
perspective's own baseline Gini. Neither perspective is designated primary.}
\note{This is the comparison to remember. The attained-bundle measure asks what
the realised job is worth; earning opportunities dominate because wages drive
disposable consumption at that job. The ex-ante measure asks what the whole job
prospect is worth; reachability therefore enters directly, and for single-adult
households access is \EAAccessRatioSinglesRawRNine{} times earnings before
equivalisation and \EAAccessRatioSinglesEqRNine{} times after it. For couples,
equivalisation is materially consequential: the ex-ante access-plus-earnings
share moves from \EAOppCouplesRawRNine{} to \EAOppCouplesEqRNine{} per cent and
the preference contribution turns negative. I make no directional preference
claim and do not designate either welfare perspective as primary. All cells
come from a restricted accounting that holds resources, needs and composition
fixed; they are not causal or total opportunity shares.}
\end{frame}
'''

marker = "% ================================================================ 7 ARCHITECTURE"
if source.count(marker) != 1:
    raise SystemExit("could not locate R9 comparison-slide insertion point")
source = source.replace(marker, slide + "\n" + marker, 1)
source = source.replace(
    "A preliminary restricted-operator decomposition is in the backup appendix.",
    "Both welfare perspectives and their restricted decompositions are reported.",
    1,
)

(HERE / "JMP_seminar_deck_r9.tex").write_text(source, encoding="utf-8", newline="\n")
(HERE / "JMP_seminar_deck_r9_rehearsal.tex").write_text(
    "% Second-screen rehearsal build of the R9 deck: same source, notes on the right.\n"
    "\\def\\RehearsalDeck{}\n\\input{JMP_seminar_deck_r9}\n",
    encoding="utf-8",
    newline="\n",
)
print("wrote JMP_seminar_deck_r9.tex and rehearsal driver")
