# JMP-M05C W-4 Routing Memo v1

**Status:** Accepted Phase-5 statistical warning  
**Parameters:** `beta_l0_sm`, `beta_w_pexp2`  
**Current tier:** S-10 Tier 1

## 1. Interpretation

The robust 95% intervals for `beta_l0_sm` and `beta_w_pexp2` are near the
relevant parameter boundary.

This warning:

- is non-gating;
- does not invalidate the accepted estimate;
- does not reopen Phase 3;
- does not require immediate boundary-aware inference;
- must be visible in the inference appendix and later welfare/decomposition
  work.

## 2. Required manuscript treatment

The Phase-5 interpretation memo and inference appendix should state:

> Robust symmetric intervals for `beta_l0_sm` and `beta_w_pexp2` approach the
> relevant parameter boundary. These intervals are reported as local
> diagnostics and should not be read as unrestricted evidence beyond the
> admissible parameter region.

Do not elevate this warning into a headline result.

## 3. Required M07/M08 treatment

For each flagged coordinate:

1. record whether the welfare or decomposition functional has a material local
   loading;
2. report one targeted local sensitivity using an admissible perturbation;
3. distinguish a material effect from a negligible effect;
4. retain the accepted 35-dimensional conditional covariance as the baseline.

## 4. Tier-2 trigger

Boundary-aware or resampling inference becomes mandatory only when:

- a direct inferential claim is made about the flagged coordinate;
- the welfare/decomposition functional loads materially on it; or
- the paper makes an unconditional active-set claim.

Until then, Tier 1 disclosure and targeted sensitivity are sufficient.
