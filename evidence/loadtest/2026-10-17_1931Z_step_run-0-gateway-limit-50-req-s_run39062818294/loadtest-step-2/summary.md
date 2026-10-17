# Scaling evidence summary

| Service | Tasks at start | Peak tasks | First scale-out (min after start) |
|---|---|---|---|
| analytics | 1 | 1 | no scale-out |
| customer | 1 | 1 | no scale-out |
| hawker | 1 | 2 | 15 |
| order | 1 | 2 | 10 |

- Peak requests per minute: 2,387
- Worst 1-min p95 target response time: 117 ms
- Peak order-queue backlog: 8 messages
- Oldest queued order: 2 s
- Peak RDS CPU: 12%
- Peak RDS connections: 8
