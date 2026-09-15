"""Generate, compile and verify the R9 seminar and rehearsal decks."""
from __future__ import annotations

from pathlib import Path
import importlib.util
import subprocess
import sys


HERE = Path(__file__).resolve().parent
for script in ("make_deck_numbers_r9.py", "prepare_deck_v9.py"):
    subprocess.run([sys.executable, str(HERE / script)], cwd=HERE, check=True)

spec = importlib.util.spec_from_file_location("deck_builder_r6_base",
                                              HERE / "build_deck_r6.py")
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
base.JOBS = {
    "deck": "JMP_seminar_deck_r9",
    "rehearsal": "JMP_seminar_deck_r9_rehearsal",
}
base.LOG = HERE / "build/JMP_seminar_deck_r9_build_log.txt"
old_argv = sys.argv
try:
    sys.argv = ["build_deck_r9.py", "all", "--reuse-assets", "--no-verify"]
    result = base.main()
finally:
    sys.argv = old_argv
for rendered_text in (
    HERE / "build/JMP_seminar_deck_r9_text.txt",
    HERE / "build/JMP_seminar_deck_r9_rehearsal_text.txt",
):
    rendered_text.write_text(
        rendered_text.read_text(encoding="utf-8"),
        encoding="utf-8",
        newline="\n",
    )
subprocess.run([sys.executable, str(HERE / "verify_deck_r9.py")],
               cwd=HERE, check=True)
raise SystemExit(result)
