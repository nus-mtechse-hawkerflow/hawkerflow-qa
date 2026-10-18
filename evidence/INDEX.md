# HawkerFlow evidence

Downloaded from GitHub Actions by `fetch_evidence.sh` (re-run it after every test or release).

## loadtest

- [`loadtest/2026-10-17_1913Z_smoke_first-smoke-run_run39061510693`](loadtest/2026-10-17_1913Z_smoke_first-smoke-run_run39061510693/run.md) **success**: loadtest-smoke-1/k6-output.txt loadtest-smoke-1/k6-summary.json loadtest-smoke-1/metrics.csv loadtest-smoke-1/scaling.png loadtest-smoke-1/summary.md 
- [`loadtest/2026-10-17_1931Z_step_run-0-gateway-limit-50-req-s_run39062818294`](loadtest/2026-10-17_1931Z_step_run-0-gateway-limit-50-req-s_run39062818294/run.md) **failure**: loadtest-step-2/k6-output.txt loadtest-step-2/k6-summary.json loadtest-step-2/metrics.csv loadtest-step-2/scaling.png loadtest-step-2/summary.md loadtest-step-2/usl.md loadtest-step-2/usl.png 
- [`loadtest/2026-10-18_0935Z_step_run-1-gateway-500-max-order-5-hawker-3_run39115915961`](loadtest/2026-10-18_0935Z_step_run-1-gateway-500-max-order-5-hawker-3_run39115915961/run.md) **failure**: loadtest-step-3/k6-output.txt loadtest-step-3/k6-summary.json loadtest-step-3/metrics.csv loadtest-step-3/scaling.png loadtest-step-3/summary.md loadtest-step-3/usl.md loadtest-step-3/usl.png 

## dast

- [`dast/2026-10-17_local-authz-tests`](dast/2026-10-17_local-authz-tests/run.md) : authz.xml 

## cd

- [`cd/diner-ui/2026-10-17_1847Z_run39059623995`](cd/diner-ui/2026-10-17_1847Z_run39059623995/run.md) **success**: no artifacts
- [`cd/hawker-ui/2026-10-17_1852Z_run39059988328`](cd/hawker-ui/2026-10-17_1852Z_run39059988328/run.md) **success**: no artifacts
- [`cd/hawkerflow-service-analytics/2026-10-17_1505Z_run39043563420`](cd/hawkerflow-service-analytics/2026-10-17_1505Z_run39043563420/run.md) **failure**: pip-audit/pip-audit.json test-reports/coverage.xml test-reports/junit.xml 
- [`cd/hawkerflow-service-analytics/2026-10-17_1713Z_run39052840750`](cd/hawkerflow-service-analytics/2026-10-17_1713Z_run39052840750/run.md) **success**: pip-audit/pip-audit.json sbom/sbom.cdx.json test-reports/coverage.xml test-reports/junit.xml zap-report/openapi-get.json zap-report/rules.tsv zap-report/zap-report.html zap-report/zap-report.json zap-report/zap-report.md 
- [`cd/hawkerflow-service-customer/2026-10-17_1814Z_run39057215732`](cd/hawkerflow-service-customer/2026-10-17_1814Z_run39057215732/run.md) **success**: pip-audit/pip-audit.json sbom/sbom.cdx.json test-reports/coverage.xml test-reports/junit.xml zap-report/openapi-get.json zap-report/rules.tsv zap-report/zap-report.html zap-report/zap-report.json zap-report/zap-report.md 
- [`cd/hawkerflow-service-hawker/2026-10-17_1823Z_run39057866638`](cd/hawkerflow-service-hawker/2026-10-17_1823Z_run39057866638/run.md) **success**: pip-audit/pip-audit.json sbom/sbom.cdx.json test-reports/coverage.xml test-reports/junit.xml zap-report/openapi-get.json zap-report/rules.tsv zap-report/zap-report.html zap-report/zap-report.json zap-report/zap-report.md 
- [`cd/hawkerflow-service-order/2026-10-17_1801Z_run39056319869`](cd/hawkerflow-service-order/2026-10-17_1801Z_run39056319869/run.md) **success**: pip-audit/pip-audit.json sbom/sbom.cdx.json test-reports/coverage.xml test-reports/junit.xml zap-report/openapi-get.json zap-report/rules.tsv zap-report/zap-report.html zap-report/zap-report.json zap-report/zap-report.md 
