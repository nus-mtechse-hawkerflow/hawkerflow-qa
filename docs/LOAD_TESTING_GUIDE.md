# HawkerFlow load testing: concepts, setup and strategy

Written 18 Oct 2026. A reference for what we're testing, why, and how to read the results.

---

## 1. What we're trying to prove

Our proposal (`docs/PROPOSAL.md` in hawkerflow-service-order) promises **scalability**: *"a workload model (≈40 RPS burst at seed scale) proven by stepped k6 load tests (25/50/100 RPS) with auto-scaling evidence and a USL fit for headroom."*

So the load tests must show three things:

1. **The requirement is met:** at and around the lunch peak (~40 req/s), latency and errors stay within target.
2. **The system is elastic:** as load rises, ECS adds tasks; as it falls, it removes them.
3. **How much headroom there is:** where the system stops scaling (the "knee"), expressed as a multiple of the 40 req/s workload.

The proposal described Lambda + DynamoDB; we built **ECS Fargate + RDS**, so our scaling evidence is **ECS task count**, not Lambda concurrency.

---

## 2. The path a request takes

```
diner (k6)
   │
   ▼
API Gateway (public)        ← throttling: 429 if a route exceeds its rate limit
   │  VPC link
   ▼
Internal load balancer (ALB) ← routes /hawker/* → hawker tasks, /order/* → order tasks …
   │
   ▼
ECS Fargate tasks           ← auto-scaling adds/removes tasks
   │
   ▼
RDS PostgreSQL (db.t4g.micro)

Ordering goes a different way:
diner → API Gateway → SQS order queue → order service's worker → RDS
        (the diner gets "accepted" immediately; the order is created moments later)
```

Every layer can be the bottleneck. A load test is largely about **finding which layer limits first**.

---

## 3. Concepts

### 3.1 Tasks and auto-scaling
- A **task** is one running copy of a service (one container, 0.25 vCPU, 512 MB). Normally each service runs 1.
- **Auto-scaling (target tracking)** watches a metric and adds or removes tasks to keep it near a target.
- It is **slow on purpose**: CloudWatch reports once a minute, scale-out waits for ~3 consecutive minutes above target, and a new task takes 1–2 minutes to start. **Expect 3–5 minutes from overload to extra capacity.** Scale-in is slower still (3-minute cooldown) to avoid flip-flopping.

Our rules (Terraform PR #1, applied 17 Oct):

| Service | Tasks min–max | Adds a task when… |
|---|---|---|
| order | 1–3 | CPU > 60%, **or** > 50 queued orders per task |
| hawker | 1–2 | CPU > 60%, **or** > 1,500 requests/min per task (25 req/s) |
| customer | 1–2 | CPU > 60% |
| analytics | 1–1 | (never: max is 1) |

- **The maximums are low because of the database.** Each task can open up to 15 connections; db.t4g.micro allows ~80–110. 3+2+2 tasks ≈ 112 connections at most.
- **These targets are kit placeholders, not measured.** Tuning them from data is the point of section 6.
- While paused (`pause.sh`), min = max = 0, so scaling can't start tasks on a paused stack.

### 3.2 API Gateway throttling: the token bucket
- A bucket of tokens: **burst** is the bucket size; **rate** is how fast it refills. **Run 0 showed it limits the whole API combined** (~50 req/s across all routes), not each route separately as first assumed.
- Every request takes 1 token. Empty bucket → **`429 Too Many Requests`**, returned by the gateway; the request never reaches ECS.
- Idle → bucket full → a sudden spike up to the burst size passes. Sustained load above the rate drains it, and then only `rate` req/s pass; the rest get 429.
- Was **50 req/s, burst 100**. PR #2 raises it to **500 / 1000** (variables `api_throttling_rate_limit`, `api_throttling_burst_limit`).
- The throttle is a **protection control**, not a mistake. It should sit just above the capacity the services are proven to handle.
- Same idea elsewhere in AWS: EBS gp2 I/O credits, EC2/RDS T-family CPU credits.

### 3.3 Burstable database (CPU credits)
- Our RDS is **db.t4g.micro**, a T-family instance: it earns CPU credits when idle and spends them when busy.
- In long tests (`step` ~26 min, `soak` 33 min) it can run out of credits → CPU capped (slower queries) or billed extra (unlimited mode).
- If latency rises late in a test while ECS looks fine, check **RDS CPU** and `CPUCreditBalance`. The database may be the bottleneck.
- Fargate tasks don't burst: they always get their allotted CPU.

### 3.4 Offered load vs HTTP requests
- k6 uses an **open model**: it *starts* a fixed number of **user actions per second** ("offered load"), whether or not earlier ones have finished, like customers walking in.
- Each user action is:
  - **browse (70%)**: 1 request, `GET /hawker/v1/hawker/stalls`;
  - **checkout (30%)**: 1 `POST` to the order queue, then **polls** `GET …/queue/{ref}` every 0.5 s until the order exists.
- So **HTTP requests at the gateway = offered + polls**. Smoke run: **1 poll per order** → gateway sees ~1.3× offered. Polls may increase under heavy load.
- The polls aren't counted in "offered" because offered models **diners**; polls are a side effect of how the app works. Our **throughput** numbers likewise count only browse + order (useful work).
- **Not simulated:** the hawker POS (accepting/preparing orders), logins, the customer service, analytics. So only **hawker** and **order** are loaded; customer and analytics stay flat (expected).

### 3.5 Test profiles

| Profile | Shape | Question it answers |
|---|---|---|
| `smoke` | 5 req/s, 1.5 min | Does the whole chain work at all? (setup check, not a result) |
| `step` | 25 → 50 → 100 → 200, each held `HOLD` (default 7 min) | Where are the limits? Does scaling keep up? Gives the USL fit. SLOs apply only to steps ≤ 50 (design load); 100 and 200 are observation-only |
| `spike` | 20 → sudden 200 for 15 min → 20 for 10 min | Can it handle a lunch rush, and scale back in afterwards? (No end-to-end SLO: orders are meant to queue during a surge) |
| `soak` | 40 req/s for 30 min | Is it stable over time (leaks, connection build-up, CPU credits)? |

**Why the step values:** built around the 40 req/s workload model: 25 (below peak, baseline) · 50 (just above peak, where scaling should start) · 100 (2.5×, headroom; named in the proposal) · 200 (5×, stress, to find the knee). Doubling covers a wide range in few runs and gives the USL fit well-spread points.

**Why 7-minute holds:** run 0 measured ~5–6 minutes from a CPU breach to the new task serving. 5-minute holds ended just as scaling arrived; 7 minutes shows it settle.

### 3.6 Concurrency and Little's law
- **Concurrency N** = requests in flight at once. **Little's law:** N = X × R (throughput × response time).
- e.g. 50 req/s × 0.1 s = 5 requests in flight.
- `usl_fit.py` computes N for each plateau from the measured X and the **server** response time R (the load balancer's average), not k6's latency, which is mostly network.

### 3.7 Universal Scalability Law (USL)
Throughput doesn't grow linearly forever. The USL describes why:

    C(N) = N / (1 + σ(N − 1) + κ·N(N − 1))

- **σ (sigma), contention:** waiting for shared resources (DB connections, locks, a single worker). Causes a ceiling.
- **κ (kappa), coherency:** components having to coordinate with each other. Causes throughput to **fall** past a peak (retrograde).
- From the fit: **peak throughput** (if κ > 0) or **ceiling** (if only σ), and **headroom = peak ÷ 40 req/s**.
- Read with care: k6 runs an open model while the USL is defined for concurrency; we use Little's law to get N. If every step keeps up (no saturation), the fit says "near-linear, no ceiling yet". That just means "test higher".
- **Throttled plateaus (any 429) are excluded from the fit**: they measure the gateway, not the services.

### 3.8 Client latency vs server latency
- k6's latency includes the **network** from GitHub's runners (usually in the US) to Singapore: ~200 ms on top.
- Smoke: k6 p95 ≈ **250 ms**, load balancer p95 ≈ **12–155 ms**.
- **Use the load balancer's response time for server performance**; report k6's as client-observed. k6's p95 < 300 ms threshold may fail just from distance.

---

## 4. Current setup (as of 18 Oct)

| Item | Value |
|---|---|
| Where tests run | hawkerflow-qa → Actions → **Load test** (choose profile, hold, note) |
| Target API | `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com` |
| Orders go to | **Stall 2, "ZZ Load Test Stall (do not order)"** (`LOADTEST_STALL_IDS=2`); auto-cancel after 15 min |
| Workload mix | 70% browse, 30% checkout via the SQS queue path |
| k6 thresholds | browse p95 < 300 ms, enqueue p95 < 500 ms, errors < 1%, order end-to-end p95 < 10 s, 0 timed-out orders, 0 dropped iterations. `step`: only steps ≤ 50; `spike`: enqueue p95/errors, timed-out and dropped only |
| Per-step metrics | achieved req/s, **orders/s**, **gateway calls/s** (incl. polls), **429s**, server R, N, p95s, order end-to-end |
| Metrics collected | tasks, ECS CPU, ALB requests + p95, queue backlog + oldest age, RDS CPU + connections (`scaling.png`) |
| Per-step results + USL | `usl.md`, `usl.png` (step profile only) |
| Gateway limit | 50 req/s → **500** once PR #2 is applied |

---

## 5. What we've learned so far

**Smoke run (17 Oct, 5 req/s):**
- Whole chain works: 164 orders on stall 2, all created; 0 failed requests; all thresholds passed.
- Order end-to-end: avg 1.25 s, p95 1.45 s (target < 10 s).
- **1 poll per order** at low load → gateway sees ~1.3× offered.
- **CPU at 5 req/s: order ~17%, hawker ~7%.** Rough extrapolation: order may reach its 60% target around the 25–50 steps.
- Database idle: 7% CPU, 4 connections.
- k6 p95 ~250 ms vs load balancer p95 12–155 ms → network distance (3.8).

**Before the load tests:**
- **The gateway limit (50 req/s) would have cut off the 100/200 steps**: requests rejected before reaching ECS. Found by reading the Terraform before running.
- **The scaling targets were never measured**: kit placeholders.

**Run 0 (`step`, 5 m holds, gateway at 50), 17 Oct 19:31 UTC** ([evidence](../evidence/INDEX.md)):

| Offered | Achieved (successful) | Rejected at the gateway |
|---|---|---|
| 25 | 26 req/s | 0% |
| 50 | 40 req/s | 19% |
| 100 | 46 req/s | 54% |
| 200 | 48 req/s | 76% |

- **The gateway caps the whole API at ~50 req/s.** Load balancer requests flatten at ~2,200/min (~37 req/s) from the 50 step while offered load keeps doubling; plus ~13 order posts/s straight to SQS ≈ 50.
- **With the old limit, the platform couldn't reliably serve the proposal's own lunch peak** (~40 req/s + order polling): 19% rejected at the 50 step. Raising the limit (Terraform PR #2) is a capacity fix, not just a test convenience.
- **Auto-scaling worked under the cap:**
  - **order** exceeded its 60% CPU target already at the **25 step** (~67–70%) and scaled to 2 tasks at minute 10 (CPU then ~40%): CPU-driven. One order task saturates at ~7.5 orders/s plus polls.
  - **hawker** scaled to 2 at minute 15, triggered by requests per task (CPU peaked ~50%).
  - The order queue backlog stayed tiny (max 8, oldest 2 s), so the backlog rule never triggered.
- **Servers stayed healthy:** load balancer p95 ~12 ms (peaks 117 ms at scale-out, ~87 ms at the 200 step); RDS ≤ 12% CPU, ≤ 8 connections; 8,932 orders on stall 2, 0 timed out, end-to-end p95 1.07 s.
- **Ignore the USL fit for this run:** "peak 44 req/s" is the gateway's limit, not the services' capacity.

**Run 1 (`step`, 7 m holds, gateway 500, max order 5 / hawker 3), 18 Oct 09:35 UTC** ([evidence](../evidence/INDEX.md)):

| Step | Achieved / offered | 429s | Order end-to-end p95 | Browse p95 (k6) | Server R (ALB mean) | Tasks |
|---|---|---|---|---|---|---|
| 25 | 26 / 25 | 0 | 1.0 s | 236 ms | 6 ms | order 1, hawker 1 |
| 50 | 50 / 50 | 0 | 1.0 s | 242 ms | 10 ms | → order 2, hawker 2–3 |
| 100 | 97 / 100 | 0 | **52 s** | 250 ms | 1.5 s | → order 4–5, hawker 3 |
| 200 | 189 / 200 | 0 | 1.1 s | **14.3 s** | 2.9 s | order 5 (max), hawker 3 (max) |

- **Requirement met:** every SLO passed at 25 and 50 req/s (peak model ~40). The run is red only because of **5,814 dropped iterations at the 200 step** (k6 ran out of browse VUs when hawker slowed).
- **No 429s:** the gateway is out of the way.
- **Scaling worked:** hawker 1 → 3, order 1 → 5, each ~6 min after its CPU breach.
- **Bottleneck at 100: order scaled too slowly.** Order CPU sat at 100% on 2 tasks for ~4 min before tasks 3–5 arrived. Queue backlog peaked at 738 (oldest 72 s), end-to-end p95 52 s, and 410 orders exceeded the 60 s poll limit. Polls amplified the load (240 gateway calls/s for 97/s of useful work). The backlog drained fully once order reached 4–5 tasks.
- **Bottleneck at 200: hawker at its max of 3** (~90% CPU), browse p95 14 s.
- **The queue design held:** order *placement* p95 stayed ~237 ms at every step, even during the backlog. Diners are accepted instantly while order creation absorbs the surge and catches up.
- **Database not a bottleneck:** peak 45% CPU, 15 connections.
- **USL fit is weak (R² 0.57):** latency explodes once queues build, which the model handles poorly in an open-model test. Capacity statement instead: **SLOs met to ≥ 50 req/s (1.25× peak); throughput keeps up to ~190 req/s (4.7×) with degraded latency beyond ~50–100.**
- **Tuning candidates for run 2:** bigger order tasks (0.5 vCPU) and/or a lower order CPU target; hawker max 3 → 5; diner app poll backoff (app code); higher browse `maxVUs` in k6.

---

## 6. Strategy: measure → find the bottleneck → remove it → measure → tune → verify

| # | Run | Purpose | Status |
|---|---|---|---|
| 0 | `smoke` | Chain works | ✅ 17 Oct |
| 1 | **Run 0**: `step`, gateway 50 | Show the gateway is the bottleneck: 429s at 100/200, load balancer requests flatten while offered load rises; whatever scales below 50 | ✅ 17 Oct: gateway caps the API at ~50 req/s; order and hawker scaled to 2 |
| 2 | Apply PR #2 (gateway 500) | Remove the bottleneck | PR open |
| 3 | **Run 1**: `step`, gateway 500 | **Baseline**: the services' real behaviour, where latency rises, the knee, USL fit | ✅ 18 Oct: SLOs met at 25/50; order bottleneck at 100 (slow scale-out, queue backlog), hawker at max at 200 |
| 4 | **Tune** (Terraform PR + apply) | Set targets from run 1 (rules below) | – |
| 5 | **Run 2**: `step`, tuned | **Verify**: scaling starts before latency degrades | – |
| 6 | **`spike`**, tuned | Lunch-rush story: scale-out and scale-in | – |
| 7 | *(optional)* `soak` | Stability over 30 min | – |

### 6.1 How to read a `step` run
1. **`usl.md` table:** per step, *achieved vs offered* (keeping up?), orders/s, gateway calls/s, 429s (gateway) vs other errors (services), server R, p95, order end-to-end.
2. **`summary.md`:** scale-out time from load start and from the CPU breach (run 0: order 6 min from breach).
3. **`scaling.png`:** tasks over time vs load; CPU per service; ALB requests (flattening while offered load rises = something upstream is limiting); queue backlog; RDS CPU and connections.
4. **The knee:** the first step where achieved < offered, latency jumps, or errors appear.
5. **Validity:** `dropped_iterations` must be 0 (else k6 didn't offer the load), and for capacity runs there must be **no 429s** (else the gateway was still in the way).

### 6.2 Tuning rules (after run 1)

| Setting | Rule | Where |
|---|---|---|
| Hawker requests/task target (now 1,500/min) | **≈ ½ the per-task rate where browse p95 starts rising**, so it scales before slowing down | `autoscaling_hawker_requests_per_task` |
| Order backlog/task target (now 50) | **Acceptable queue wait (e.g. 30 s) ÷ measured seconds per order** | `autoscaling_order_backlog_per_task` |
| CPU target (now 60%) | Lower it if latency rises before 60% CPU | `autoscaling_cpu_target_percent` |
| Max tasks (now 3/2/2/1) | Lower, or cap the per-task DB pool, if RDS connections/CPU limit first | `autoscaling_limits` |
| Gateway limit (500) | Just above the capacity run 1 proves | `api_throttling_rate_limit` / `_burst_limit` |
| `HOLD` | Longer (7–10 m) if scaling hasn't settled before the next step | workflow input |
| Steps | Higher if no knee by 200; finer around the knee if it's early | `PROFILES` in `hawkerflow.js` |
| Poll interval | `POLL_INTERVAL_S=1` if polls dominate gateway traffic | k6 env |

All Terraform settings are in `hawkerflow-terraform/variables.tf`; changing them is a PR + `terraform apply`, and nothing restarts.

**If run 1 already shows scaling before latency rises,** the defaults fit: say so ("measured, confirmed adequate") and skip to `spike`.

### 6.3 Rules while testing
- **No releases (main → release merges) during a load test**: deploys restart tasks and distort the charts.
- **No Terraform apply during a load test.**
- Load tests only order from **stall 2**; never point them at stall 1 (the demo stall).
- After every run, download the results: `bash evidence/fetch_evidence.sh` (from this repo's root) saves them to [`evidence/`](../evidence/INDEX.md); commit and push them.

---

## 7. Where results are

| Place | What |
|---|---|
| Run page → **Summary** tab | `summary.md`, and for `step` the per-step table + USL fit |
| Run page → **Artifacts** → `loadtest-<profile>-<n>` | `scaling.png`, `summary.md`, `metrics.csv`, `k6-summary.json`, `k6-output.txt`, (`usl.md`, `usl.png`) |
| **[`evidence/`](../evidence/INDEX.md)** in this repo | All of the above per run, plus `run.md`; index in `evidence/INDEX.md` |

GitHub deletes artifacts after 90 days; the `evidence/` copy is the one to use for the report.

---

## 8. Glossary

| Term | Meaning |
|---|---|
| Offered load | User actions per second k6 starts (open model) |
| Achieved throughput (X) | Successful browse + order requests per second actually completed |
| p95 | 95th-percentile latency: 95% of requests were faster than this |
| Plateau | A held step at constant offered load |
| Knee | The load where throughput stops rising and latency jumps |
| Headroom | Peak throughput ÷ expected peak load (40 req/s) |
| Target tracking | Auto-scaling that keeps a metric near a target value |
| Token bucket | Rate-limiting model: burst = bucket size, rate = refill speed |
| 429 | "Too Many Requests": rejected by a rate limit |
| Little's law | N = X × R: requests in flight = throughput × response time |
| USL (σ, κ) | Scalability model: σ = contention, κ = coherency |
