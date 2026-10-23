# Scalability: per-step results and USL fit

Achieved X counts successful browse and checkout requests (useful work). Gateway calls include order polls and every status. R is the load balancer's mean response time (server side) unless marked client.

| Offered (req/s) | Achieved X (req/s) | Orders/s | Gateway calls/s | 429s | Errors (all) | R (ms) | N | p95 browse (ms) | p95 enqueue (ms) | Order end-to-end p95 (ms) | In fit |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 25 | 26.0 | 8.0 | 34.0 | 0 | 0.0% | 12 | 0.31 | 231 | 223 | 940 | yes |
| 50 | 50.0 | 15.0 | 65.0 | 0 | 0.0% | 15 | 0.75 | 231 | 221 | 949 | yes |
| 100 | 97.5 | 26.0 | 224.6 | 0 | 0.1% | 1880 | 183.20 | 1,380 | 221 | 55,366 | yes |
| 200 | 199.8 | 60.0 | 259.8 | 0 | 0.0% | 240 | 47.89 | 1,982 | 220 | 1,151 | yes |

**USL fit** on 4 plateaus: σ (contention) = 0.075, κ (coherency) = 0.0003, R² = 0.998 (relative to X₀ = 26.0 req/s at N₀ = 0.31).

- Predicted peak: **239 req/s** at concurrency N ≈ 16.7; beyond that, throughput falls (retrograde scaling).
- Headroom over the 40 req/s workload model: **6.0×** (highest measured: 200 req/s = 5.0×).

Caveat: k6 offers load at a fixed arrival rate (open model) while the USL is defined for concurrency; N is the concurrency each plateau actually ran at (Little's law).
