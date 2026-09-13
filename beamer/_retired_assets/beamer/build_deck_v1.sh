#!/usr/bin/env bash
# Compatibility entry point: the three original variants, with v4 content gates.
set -euo pipefail
cd "$(dirname "$0")"
exec python build_deck_v4.py "${1:-all}"
