# Scaling evidence summary

| Service | Tasks at start | Peak tasks | Load start → first scale-out (min) | CPU > 60% → first scale-out (min) |
|---|---|---|---|---|
| analytics | 1 | 1 | no scale-out | – |
| customer | 1 | 1 | no scale-out | – |
| hawker | 1 | 3 | 6 | 6 |
| order | 1 | 5 | 6 | 6 |

Times are at CloudWatch's 1-minute resolution. A scale-out without a prior CPU breach was triggered by another target (hawker: requests per task; order: queue backlog per task).

- Peak requests per minute: 19,607
- Worst 1-min p95 target response time: 14,820 ms
- Peak order-queue backlog: 738 messages
- Oldest queued order: 72 s
- Peak RDS CPU: 45%
- Peak RDS connections: 15
