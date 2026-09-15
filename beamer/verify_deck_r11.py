"""Release checks for the R11 outcomes-versus-prospects deck."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path


HERE = Path(__file__).resolve().parent
source = (HERE / "JMP_seminar_deck_r11.tex").read_text(encoding="utf-8")
numbers = (HERE / "deck_numbers_r11.tex").read_text(encoding="utf-8")
pdf = HERE / "build/JMP_seminar_deck_r11.pdf"
rehearsal_pdf = HERE / "build/JMP_seminar_deck_r11_rehearsal.pdf"
text_path = HERE / "build/JMP_seminar_deck_r11_text.txt"
if pdf.is_file() and not text_path.is_file():
    subprocess.run(
        [str(Path.home() / "AppData/Local/Programs/MiKTeX/miktex/bin/x64/pdftotext.exe"),
         "-layout", str(pdf), str(text_path)],
        check=True,
    )
rendered = text_path.read_text(encoding="utf-8", errors="replace") if text_path.is_file() else ""
rendered_flat = " ".join(rendered.split())
frames_r9 = len(re.findall(r"\\begin\{frame\}",
                           (HERE / "JMP_seminar_deck_r9.tex").read_text(encoding="utf-8")))
frames_r11 = len(re.findall(r"\\begin\{frame\}", source))
exact_title = (
    "Unequal Job Opportunities and Well-Being Inequality: "
    "A Latent-Jobs Structural Decomposition"
)
checks = {
    "pdf_present": pdf.is_file() and pdf.stat().st_size > 100_000,
    "rehearsal_pdf_present": rehearsal_pdf.is_file() and rehearsal_pdf.stat().st_size > 100_000,
    "exact_title": rf"\title{{{exact_title}}}" in source,
    "two_additional_slides_ea_and_matched": frames_r11 == frames_r9 + 2,
    "two_perspective_slides": all(text in source for text in (
        "ATT: how well off is the household in the bundle it actually",
        "EA: how valuable is the distribution of job prospects the",
        "The welfare question changes which labour-market inequality matters.",
        "ATT: the attained bundle", "EA: the whole opportunity prospect",
        "couples: no reversal",
    )),
    "interpretation_sentence": "depends on whether welfare evaluates the realised outcome" in source,
    "d_status_sentence": ("equalises preferences, geographic/temporal job access and systematic "
                          "earning opportunities while holding household resources, needs and "
                          "composition fixed") in " ".join(source.split()),
    "no_haydar_maniquet_defence": not re.search(
        r"Haydar--Maniquet|measure one and measure four|companion theory paper with Francois Maniquet|Measure 1",
        source),
    "certified_values": all(macro in numbers for macro in (
        r"\newcommand{\AttOppSinglesRawRNine}{2.4}",
        r"\newcommand{\EAOppSinglesRawRNine}{14.8}",
        r"\newcommand{\EAOppCouplesRawRNine}{21.3}",
        r"\newcommand{\EAOppCouplesEqRNine}{7.9}",
        r"\newcommand{\MatchedAccessRatioREleven}{14.5}",
    )),
    "no_stale_exante_status": not re.search(
        r"ex-ante.*(?:blocked|not yet a numerical result|no numerical result)|"
        r"ex-ante metric is being reconstructed|no settled comparison",
        source + rendered, flags=re.I | re.S),
    "rendered_comparison": all(text in rendered_flat for text in (
        "The welfare question changes which labour-market inequality matters.",
        "21.3%", "7.9%", "Two matched men",
    )),
}
for name, ok in checks.items():
    print(("PASS" if ok else "FAIL") + ": " + name)
failed = [name for name, ok in checks.items() if not ok]
if failed:
    raise SystemExit("deck R11 failed: " + ", ".join(failed))
