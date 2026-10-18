# Scalability: per-step results and USL fit

Achieved X counts successful browse and checkout requests (useful work). Gateway calls include order polls and every status. R is the load balancer's mean response time (server side) unless marked client.

| Offered (req/s) | Achieved X (req/s) | Orders/s | Gateway calls/s | 429s | Errors (all) | R (ms) | N | p95 browse (ms) | p95 enqueue (ms) | Order end-to-end p95 (ms) | In fit |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 25 | 26.0 | 8.0 | 34.0 | 0 | 0.0% | 6 | 0.17 | 236 | 239 | 968 | yes |
| 50 | 50.0 | 15.0 | 65.0 | 0 | 0.0% | 10 | 0.51 | 242 | 237 | 975 | yes |
| 100 | 97.2 | 26.2 | 239.6 | 0 | 0.0% | 1519 | 147.66 | 250 | 238 | 52,338 | yes |
| 200 | 189.2 | 60.0 | 249.5 | 0 | 0.1% | 2918 | 552.08 | 14,307 | 237 | 1,128 | yes |

**USL fit** on 4 plateaus: σ (contention) = 0.146, κ (coherency) = 0.0000, R² = 0.573 (relative to X₀ = 26.0 req/s at N₀ = 0.17).

- No retrograde region in the tested range (κ = 0). Contention alone caps throughput at about **178 req/s** (asymptote X₀/σ).
- Headroom over the 40 req/s workload model: **4.5×** (highest measured: 189 req/s = 4.7×).

Caveat: k6 offers load at a fixed arrival rate (open model) while the USL is defined for concurrency; N is the concurrency each plateau actually ran at (Little's law).
