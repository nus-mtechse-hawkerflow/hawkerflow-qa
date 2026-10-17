# Scalability: per-step results and USL fit

Throughput counts successful browse and checkout requests only (order polls and errors excluded).

| Offered (req/s) | Achieved X (req/s) | Achieved / offered | Errors (all requests) | Mean R (ms) | Concurrency N | p95 browse (ms) | p95 enqueue (ms) | Order end-to-end p95 (ms) |
|---|---|---|---|---|---|---|---|---|
| 25 | 26.0 | 104% | 0.0% | 234 | 6.08 | 238 | 238 | 979 |
| 50 | 40.4 | 81% | 19.1% | 234 | 9.45 | 238 | 237 | 974 |
| 100 | 46.1 | 46% | 53.9% | 233 | 10.73 | 237 | 236 | 1,028 |
| 200 | 48.4 | 24% | 75.8% | 242 | 11.73 | 288 | 236 | 1,222 |

**USL fit:** σ (contention) = 0.000, κ (coherency) = 0.1271, R² = 0.600 (relative to the lowest plateau, X₀ = 26.0 req/s at N₀ = 6.08).

- Predicted peak: **44 req/s** at concurrency N ≈ 17.0; beyond that, throughput falls (retrograde scaling).
- Headroom over the 40 req/s workload model: **1.1×**.
- ⚠️ Concurrency varied less than 2× across plateaus, so the fit is weakly constrained.

⚠️ Some plateaus had more than 1% failed requests. If they are `429`s, API Gateway throttling (not the services) limited throughput at that step.

Caveat: k6 offers load at a fixed arrival rate (open model) while the USL is defined for concurrency; N here is the concurrency each plateau actually ran at (Little's law).
