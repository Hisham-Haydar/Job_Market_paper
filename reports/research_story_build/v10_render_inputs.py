"""V10 report inputs: identical evidence to V9. No new numerical input.

Stage A (release-language consistency) adds no number, table or figure, so
V10 reuses V9's registry, tables and captions by reference rather than by
copy. See v10_sections.py for the only substantive change.
"""
from __future__ import annotations

from v9_render_inputs import (
    HERE, ROOT, PAPER, FIG, REG, TABLES, CAPTIONS, USED, DIAG_SHA256,
    resolve, val,
)
