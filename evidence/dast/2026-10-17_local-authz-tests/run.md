# Authorization tests (local run, before the AISS-06 fix)

- Run: local, from this Mac (not GitHub Actions), 17 Oct 2026
- Target: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com, VICTIM_STALL_ID=1
- Tests: `hawkerflow-qa/dast/authz/test_authz.py` (11 cases)
- Result: **8 failed, 3 passed**: the attacks succeeded (the expected "before" picture)

| Test | Result | Response |
|---|---|---|
| Forged X-Stall-ID reads stall 1's orders | FAILED (vulnerable) | 200 with stall 1's orders |
| Unsigned JWT (alg: none) accepted | FAILED (vulnerable) | 200 with stall 1's orders |
| Analytics by header only | FAILED | 503 "Analytics database is unavailable" |
| Order #1 readable without auth | FAILED (vulnerable) | 200 with order details |
| Order status change without auth | FAILED (vulnerable) | 404 "Order 2000000000 not found" (handler ran) |
| Hawker profile lookup without auth | FAILED | 500 Internal Server Error |
| Customer profile lookup without auth | FAILED | 200 (empty profile) |
| /sqs/status public | FAILED (vulnerable) | 200, reveals queue URL incl. AWS account ID |
| CORS evil origin + credentials (order, hawker, customer) | PASSED ×3 | API Gateway does not reflect the origin |

JUnit XML: `authz.xml`.
