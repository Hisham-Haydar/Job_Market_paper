#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Build the R6 seminar deck with the existing beamer toolchain.

Same environment handling as build_deck_v4.py (Git's perl for latexmk, and
MiKTeX's Poppler pdftotext ahead of Git's bbox-less build).  It does NOT run
the v4 macro/figure generators: those regenerate S8/R240 artefacts that R6
excludes.  It runs the R6 generators and the R6 gates instead.

The full build log is written to build/JMP_seminar_deck_r6_build_log.txt.
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUILD = HERE / "build"
JOBS = {"deck": "JMP_seminar_deck_r6",
        "rehearsal": "JMP_seminar_deck_r6_rehearsal"}
LOG = BUILD / "JMP_seminar_deck_r6_build_log.txt"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("variant", choices=["all", *JOBS], default="all", nargs="?")
    p.add_argument("--no-verify", action="store_true")
    p.add_argument("--reuse-assets", action="store_true",
                   help="Compile presentation edits using existing numerical macros and figures")
    a = p.parse_args()

    env = os.environ.copy()
    env["PYTHONPATH"] = str(BUILD / "python_deps") + os.pathsep + env.get("PYTHONPATH", "")
    env["MPLCONFIGDIR"] = str(BUILD / "matplotlib")
    env["PYTHONIOENCODING"] = "utf-8"
    if os.name == "nt":
        poppler = Path(os.path.expanduser(
            r"~\AppData\Local\Programs\MiKTeX\miktex\bin\x64"))
        head = [str(poppler)] if (poppler / "pdftotext.exe").is_file() else []
        env["PATH"] = os.pathsep.join(
            head + [r"C:\Program Files\Git\usr\bin", env["PATH"]])

    BUILD.mkdir(exist_ok=True)
    lines: list[str] = ["R6 seminar deck build log",
                        "started %s" % datetime.now(timezone.utc).isoformat(),
                        "authority: JMP_W1_fork_ruling_v1.md Appendix A (R6); "
                        "JMP_W1_BASELINE_F1_authorization_and_Cobs_ruling_v1.md s5",
                        ""]

    def run(args, capture=True):
        lines.append("$ " + " ".join(str(x) for x in args))
        # Windows resolves the executable against the PARENT's PATH, not the
        # child env=, so latexmk/pdftotext must be resolved here explicitly.
        args = list(args)
        exe = shutil.which(args[0], path=env["PATH"])
        if exe is None:
            LOG.write_text("\n".join(lines), encoding="utf-8")
            raise SystemExit("FAILED: %r not found on the build PATH" % args[0])
        args[0] = exe
        r = subprocess.run(args, cwd=HERE, env=env,
                           capture_output=capture, text=True,
                           encoding="utf-8", errors="replace")
        if capture and r.stdout:
            lines.extend("  " + ln for ln in r.stdout.rstrip().splitlines())
        if capture and r.stderr:
            lines.extend("  ! " + ln for ln in r.stderr.rstrip().splitlines())
        lines.append("  exit %d" % r.returncode)
        lines.append("")
        if r.returncode != 0:
            LOG.write_text("\n".join(lines), encoding="utf-8")
            raise SystemExit("FAILED: %s (exit %d); log at %s"
                             % (args[0], r.returncode, LOG))
        return r

    if not a.reuse_assets:
        run([sys.executable, "make_deck_numbers_r6.py"])
        run([sys.executable, "make_slide_figures_r6.py"])

    jobs = list(JOBS.values()) if a.variant == "all" else [JOBS[a.variant]]
    for job in jobs:
        print("Building " + job, flush=True)
        run(["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error",
             "-outdir=build", job + ".tex"])
        run(["pdftotext", "-layout", "build/" + job + ".pdf",
             "build/" + job + "_text.txt"])
        log = (BUILD / (job + ".log")).read_text(encoding="utf-8", errors="replace")
        over, under = log.count("Overfull"), log.count("Underfull")
        pages = log.count("Output written")
        msg = "  %s: overfull=%d underfull=%d" % (job, over, under)
        print(msg, flush=True)
        lines.append(msg + " (output-written markers: %d)" % pages)
        lines.append("")

    if not a.no_verify:
        run([sys.executable, "verify_deck_r6.py"])

    lines.append("finished %s" % datetime.now(timezone.utc).isoformat())
    LOG.write_text("\n".join(lines), encoding="utf-8")
    print("build log: %s" % LOG)
    return 0


if __name__ == "__main__":
    sys.exit(main())
