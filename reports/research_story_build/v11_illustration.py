"""Matched-household opportunity illustration text for V11.

The numbers are bound to reports/v11_matched_households.json through registry
keys prefixed ``mh_`` (see v11_render_inputs.py), produced by
make_v11_matched_households.py.
"""
from __future__ import annotations

REPORT_BLOCK = r"""
## What unequal opportunity means in this model: two matched households

The equations above say that households differ in what they can reach. A pair
of estimation households makes that concrete. The pair is a teaching device:
it is not a causal comparison and it is not representative of the population.

**How the pair was chosen.** Among employed single adults, admissible pairs
share their sex, observed occupation group, model hours band and
observed-wage quintile—the things an income or employment table would show.
Among those {{n:mh_admissible_pairs}} pairs, only those whose estimated leisure
profiles are closest (at or below the tenth percentile of leisure-profile
distance) are retained, and the pair whose estimated opportunity densities
differ most is selected. The selected pair is therefore an extreme case under a
stated rule, not a typical one. Identifiers, exact observed values, ages,
regions and local labour-market values are withheld.

{{figure:matched}}

**Preferences are nearly identical.** Both households are men with estimated
leisure weights of {{n:mh_leisure_weight_a|.2f}} and
{{n:mh_leisure_weight_b|.2f}} and a common curvature; their leisure-value
curves in panel (a) overlap. Their leisure-profile distance is
{{n:mh_leisure_distance|.3f}}, against a selection cut-off of
{{n:mh_leisure_cut|.3f}}.

**Access differs by an order of magnitude.** Household A's employment mass is
{{n:mh_access_ratio|.1f}} times household B's. If both were indifferent between
all jobs and not working, employment would account for
{{n:mh_employment_share_a|.2f}} of A's opportunity mass and
{{n:mh_employment_share_b|.2f}} of B's (panel b). The gap comes from local
unemployment exposure and region—exactly the geographic/temporal access channel
equalised by $A$ in Section 4.

**Hours and occupation opportunities are the same by construction.** In the
preferred specification the hours density is common to all single adults and
occupation mass is common within sex (panels c and d). The illustration cannot
show differences the specification does not allow.

**Earning opportunities point the other way.** Household B's wage-offer
location is {{n:mh_wage_gap|.1f}} log points higher, with the same dispersion.
Its wage-offer distribution given employment therefore first-order
stochastically dominates household A's (panel e). Yet A faces more offers paying
at least $w$ at every wage below about {{n:mh_crossing_wage|.0f}} euros per hour,
which covers essentially all offer mass (panel f), because its access advantage
outweighs B's better wage location.

**What the pair teaches.** Two men who look alike in an income table and have
almost the same estimated tastes face different opportunity environments, and
neither environment is better on every margin. A has many more jobs; B's jobs
pay more. Whether A or B is better placed depends on how welfare weighs the
number of reachable jobs against what the realised job pays—the same question
that separates the two welfare perspectives in Section 3.
"""

APPENDIX_BLOCK = r"""
## Implementation record: matched-household illustration

The illustration is produced by `make_v11_matched_households.py`, which
evaluates the accepted single-adult leisure index and opportunity density for
every estimation household with the certified ex-ante evaluators. No
estimation, pricing, welfare or decomposition routine is called. Leisure-profile
distance is the maximum absolute gap between the two households' leisure-index
curves over 5–70 weekly hours, divided by its standard deviation among employed
single adults. Opportunity distance is the closed-form total-variation distance
between the two households' opportunity densities normalised to include
non-employment; the common hours factor cancels, and wage truncation, which
removes a negligible share of offer mass, is ignored in the distance only. The
selected pair's opportunity distance is {{n:mh_opportunity_distance|.2f}},
against an admissible-pair median of {{n:mh_opportunity_distance_median|.2f}}.
The source record `reports/v11_matched_households.json` stores only rounded model
quantities and the hashes of the parameter vector, estimation frame and
evaluator code; it contains no identifier or observed record value. An induced
consumption-prospect distribution is feasible from the existing priced
integration points but is not shown, because it would require reweighting those
points outside the certified calculation.
"""
