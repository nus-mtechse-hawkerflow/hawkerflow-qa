# Scaling evidence summary

| Service | Tasks at start | Peak tasks | Load start → first scale-out (min) | CPU > 60% → first scale-out (min) |
|---|---|---|---|---|
| analytics | 2 | 2 | no scale-out | – |
| customer | 2 | 2 | no scale-out | – |
| hawker | 2 | 5 | 15 | 6 |
| order | 2 | 5 | 14 | 6 |

Times are at CloudWatch's 1-minute resolution. A scale-out without a prior CPU breach was triggered by another target (hawker: requests per task; order: queue backlog per task).

- Peak requests per minute: 16,861
- Worst 1-min p95 target response time: 12,722 ms
- Peak order-queue backlog: 971 messages
- Oldest queued order: 74 s
- Peak RDS CPU: 80%
- Peak RDS connections: 19
