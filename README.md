# hawkerflow-qa

Platform-level security and performance testing for HawkerFlow.

| Workflow | Trigger | What it does |
|---|---|---|
| `DAST` | nightly 02:00 SGT, manual | authorization attacks (`dast/authz`) + ZAP API scan of each service |
| `Load test` | manual (pick `smoke`, `step`, `spike`, `soak`) | k6 against the deployed stack, then CloudWatch metrics → `scaling.png` + `summary.md` |

## Configuration

Repository variables: `API_BASE_URL`, `ORDER_QUEUE_URL`, `VICTIM_STALL_ID`,
`LOADTEST_STALL_IDS`, `ECS_CLUSTER`, `ECS_SERVICE_ORDER`, `ECS_SERVICE_HAWKER`,
`ECS_SERVICE_CUSTOMER`, `ECS_SERVICE_ANALYTICS`, `ALB_DIMENSION`,
`ORDER_QUEUE_NAME`, `RDS_INSTANCE`, optional `ZAP_FAIL`.

Repository secret: `AWS_METRICS_ROLE`, an OIDC role allowed only `cloudwatch:GetMetricData`.

## Running locally

```bash
# authorization checks
pip install -r dast/authz/requirements.txt
API_BASE_URL=https://<api>.execute-api.ap-southeast-1.amazonaws.com VICTIM_STALL_ID=1 pytest dast/authz -v

# load test
k6 run loadtest/hawkerflow.js -e API_BASE_URL=... -e ORDER_QUEUE_URL=... -e PROFILE=smoke

# charts from a saved run, no AWS needed
python loadtest/collect_metrics.py --from-csv reports/metrics.csv --out reports
```

The load test creates real orders. Point `LOADTEST_STALL_IDS` at dedicated test
stalls; unaccepted orders are expired by the Order service after 15 minutes.
