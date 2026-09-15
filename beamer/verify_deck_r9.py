"""Release checks for the R9 two-perspective deck."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path


HERE = Path(__file__).resolve().parent
source = (HERE / "JMP_seminar_deck_r9.tex").read_text(encoding="utf-8")
numbers = (HERE / "deck_numbers_r9.tex").read_text(encoding="utf-8")
pdf = HERE / "build/JMP_seminar_deck_r9.pdf"
rehearsal_pdf = HERE / "build/JMP_seminar_deck_r9_rehearsal.pdf"
text_path = HERE / "build/JMP_seminar_deck_r9_text.txt"
if pdf.is_file() and not text_path.is_file():
    subprocess.run(
        [str(Path.home() / "AppData/Local/Programs/MiKTeX/miktex/bin/x64/pdftotext.exe"),
         "-layout", str(pdf), str(text_path)],
        check=True,
    )
rendered = text_path.read_text(encoding="utf-8", errors="replace") if text_path.is_file() else ""
frames_r7 = len(re.findall(r"\\begin\{frame\}",
                           (HERE / "JMP_seminar_deck_r7.tex").read_text(encoding="utf-8")))
frames_r9 = len(re.findall(r"\\begin\{frame\}", source))
exact_title = (
    "Unequal Job Opportunities and Well-Being Inequality: "
    "A Latent-Jobs Structural Decomposition"
)
checks = {
    "pdf_present": pdf.is_file() and pdf.stat().st_size > 100_000,
    "rehearsal_pdf_present": rehearsal_pdf.is_file() and rehearsal_pdf.stat().st_size > 100_000,
    "exact_title": rf"\title{{{exact_title}}}" in source,
    "exactly_one_additional_slide": frames_r9 == frames_r7 + 1,
    "comparison_slide": all(text in source for text in (
        "The welfare perspective changes which opportunity channel dominates.",
        "Attained bundle: the realised job",
        "Ex ante: the whole job prospect",
        r"Singles: access $\simeq 3\times$ earnings",
        "Neither perspective is designated primary",
    )),
    "certified_values": all(macro in numbers for macro in (
        r"\newcommand{\AttOppSinglesRawRNine}{2.4}",
        r"\newcommand{\EAOppSinglesRawRNine}{14.8}",
        r"\newcommand{\EAOppCouplesRawRNine}{21.3}",
        r"\newcommand{\EAOppCouplesEqRNine}{7.9}",
    )),
    "no_stale_exante_status": not re.search(
        r"ex-ante.*(?:blocked|not yet a numerical result|no numerical result)|"
        r"ex-ante metric is being reconstructed|no settled comparison",
        source + rendered,
        flags=re.I | re.S,
    ),
    "rendered_comparison": all(text in rendered for text in (
        "The welfare perspective changes which opportunity channel dominates.",
        "21.3%", "7.9%", "access", "earnings",
    )),
}
for name, ok in checks.items():
    print(("PASS" if ok else "FAIL") + ": " + name)
failed = [name for name, ok in checks.items() if not ok]
if failed:
    raise SystemExit("deck R9 failed: " + ", ".join(failed))
