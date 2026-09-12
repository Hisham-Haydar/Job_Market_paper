# Beamer build entry point.
#
# No Makefile existed in this repository before the R6 rebuild; the build was
# driven directly by the Python builders below.  This file wraps them so the
# deck has a single documented entry point, and changes nothing about how
# either deck is produced.
#
#   make r6         the 17 September seminar deck (R6 content) + rehearsal
#   make r6-deck    the projection build only
#   make verify-r6  the R6 gates, without recompiling
#   make v41        the historical v4.1 deck (W1-EA content; NOT for seminar)
#
# The v4.1 deck is retained only as a historical artifact under ruling R2.
# It must not be presented: its welfare block states retired W1-EA magnitudes.

PYTHON ?= python

.PHONY: all r6 r6-deck r6-rehearsal verify-r6 numbers-r6 figures-r6 v41 clean-r6

all: r6

r6:
	$(PYTHON) build_deck_r6.py all

r6-deck:
	$(PYTHON) build_deck_r6.py deck

r6-rehearsal:
	$(PYTHON) build_deck_r6.py rehearsal

numbers-r6:
	$(PYTHON) make_deck_numbers_r6.py

figures-r6:
	$(PYTHON) make_slide_figures_r6.py

verify-r6:
	$(PYTHON) verify_deck_r6.py

# Historical only.  Guarded so it is never run by accident.
v41:
	@echo "The v4.1 deck carries retired W1-EA content (ruling R2)."
	@echo "It is preserved as a historical artifact and is not the seminar deck."
	@echo "To build it anyway, run: $(PYTHON) build_deck_v4.py all"

clean-r6:
	$(PYTHON) -c "import pathlib,glob; [pathlib.Path(p).unlink() for p in glob.glob('build/JMP_seminar_deck_r6*') ]"
