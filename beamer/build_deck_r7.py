"""Generate, compile and verify the versioned R7 seminar deck."""
from pathlib import Path
import importlib.util
import subprocess
import sys


HERE = Path(__file__).resolve().parent
for script in ("prepare_deck_v7.py", "make_deck_numbers_r7.py",
               "make_slide_figures_r7.py"):
    subprocess.run([sys.executable, str(HERE / script)], cwd=HERE, check=True)

spec = importlib.util.spec_from_file_location("deck_builder_r6_base",
                                              HERE / "build_deck_r6.py")
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
base.JOBS = {"deck": "JMP_seminar_deck_r7",
             "rehearsal": "JMP_seminar_deck_r7_rehearsal"}
base.LOG = HERE / "build/JMP_seminar_deck_r7_build_log.txt"
old_argv = sys.argv
try:
    sys.argv = ["build_deck_r7.py", "all", "--reuse-assets", "--no-verify"]
    result = base.main()
finally:
    sys.argv = old_argv
subprocess.run([sys.executable, str(HERE / "verify_deck_r7.py")],
               cwd=HERE, check=True)
raise SystemExit(result)
