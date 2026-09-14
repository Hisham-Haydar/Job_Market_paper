"""Regenerate the modular working-paper fit section from v7 render inputs."""
from pathlib import Path
import re

import pypandoc

from v7_render_inputs import FIG, ROOT, resolve
from v7_sections import RESULTS


fit = "## Fit" + RESULTS.split("## Fit", 1)[1].split(
    "## Within-sample equivalised results", 1)[0]
markdown = resolve(fit, "report")
latex = pypandoc.convert_text(
    markdown, "latex", format="markdown+raw_tex+tex_math_dollars",
    extra_args=["--wrap=none"]).replace("\r\n", "\n")
latex = latex.replace(r"\begin{figure}", r"\begin{figure}[H]")
latex = latex.replace(FIG.as_posix() + "/", "figures/v7/")
latex = latex.replace((ROOT / "manuscript/figures/v5").as_posix() + "/",
                      "figures/v5/")


def wrap_table(match):
    count = len(match[1])
    first = .155 if count == 7 else (.25 if count >= 4 else .42)
    total = .98 - .014 * count
    widths = [first] + [(total - first) / (count - 1)] * (count - 1)
    return (r"\begin{longtable}[]{@{}" + "".join(
        r">{\RaggedRight\arraybackslash}p{" + f"{width:.4f}" + r"\linewidth}"
        for width in widths) + r"@{}}")


latex = re.sub(r"\\begin\{longtable\}\[\]\{@\{\}([lrc]+)@\{\}\}",
               wrap_table, latex)
latex = latex.replace(
    r"\begin{longtable}",
    r"\Needspace*{12\baselineskip}\small\setlength{\tabcolsep}{3pt}\begin{longtable}")
target = ROOT / "manuscript/sections/05b_fit.tex"
target.write_text(latex + "\n", encoding="utf-8")
print("wrote " + str(target))
