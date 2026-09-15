"""Generate, compile and verify the V16 seminar deck (rebuilt from V15).

Numbers: make_deck_numbers_r6.py --v16 (V15 registry only).
Compile: the R6 builder's toolchain (latexmk + pdftotext), job names swapped.
Gates:   verify_deck_r6.py --deck v16, which also runs both negative controls.
Rehearsal pack: build_rehearsal_script_v16.py.
"""
from __future__ import annotations

import importlib.util
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
subprocess.run([sys.executable, str(HERE / "make_deck_numbers_r6.py"), "--v16"],
               cwd=HERE, check=True)
(HERE / "JMP_seminar_beamer_v16_rehearsal.tex").write_text(
    "% Second-screen rehearsal build of the V16 deck: same source, notes on the right.\n"
    "\\def\\RehearsalDeck{}\n\\input{JMP_seminar_beamer_v16}\n",
    encoding="utf-8", newline="\n")

spec = importlib.util.spec_from_file_location("deck_builder_r6_base", HERE / "build_deck_r6.py")
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
base.JOBS = {"deck": "JMP_seminar_beamer_v16",
             "rehearsal": "JMP_seminar_beamer_v16_rehearsal"}
base.LOG = HERE / "build/JMP_seminar_beamer_v16_build_log.txt"
old_argv = sys.argv
try:
    sys.argv = ["build_deck_v16.py", "all", "--reuse-assets", "--no-verify"]
    result = base.main()
finally:
    sys.argv = old_argv

env = dict(os.environ, PYTHONPATH=str(HERE / "build/python_deps"), PYTHONIOENCODING="utf-8")
subprocess.run([sys.executable, str(HERE / "verify_deck_r6.py"), "--deck", "v16"],
               cwd=HERE, check=True, env=env)
subprocess.run([sys.executable, str(HERE / "build_rehearsal_script_v16.py")],
               cwd=HERE, check=True, env=env)
raise SystemExit(result)
