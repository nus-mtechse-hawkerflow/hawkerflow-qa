# Scaling evidence summary

| Service | Tasks at start | Peak tasks | First scale-out (min after start) |
|---|---|---|---|
| analytics | 1 | 1 | no scale-out |
| customer | 1 | 1 | no scale-out |
| hawker | 1 | 1 | no scale-out |
| order | 1 | 1 | no scale-out |

- Peak requests per minute: 361
- Worst 1-min p95 target response time: 155 ms
- Peak order-queue backlog: 0 messages
- Oldest queued order: 0 s
- Peak RDS CPU: 7%
- Peak RDS connections: 4
