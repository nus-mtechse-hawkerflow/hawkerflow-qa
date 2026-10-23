# Brief: "Load Testing & Scaling" slides (HawkerFlow final presentation)

**For:** a slide-generation agent. Everything needed is in this file; do not invent numbers.
**Status:** final (run 2 results added, 23 Oct 2026).

---

## 1. Context

- **Presentation:** HawkerFlow, an NUS MTech SE project (food ordering for hawker centres). Final presentation on 24 Oct 2026, built in **PowerPoint**.
- **Deck order:**
  1. Overview + Project Conduct
  2. Logical Architecture
  3. Physical Architecture
  4. DevOps
  5. **Load Testing & Scaling (this section)**
  6. Demo
- **Time:** **~5 minutes, 5 slides**, about 1 minute each, about 650 spoken words in total.
- **Neighbouring sections:** DevOps is presented by someone else, just before; Demo follows. Don't explain CI/CD pipelines (DevOps covers them). Refer back to the Physical Architecture for components rather than re-explaining them.
- **Audience:** examiners and peers. Technical, but short on time. Plain words over jargon.

## 2. Output

- **Five 16:9 slides.** If the team's .pptx template is provided, use its layouts, fonts and colours; otherwise a clean, light, minimal style.
- **Speaker notes** on every slide (the script below; light edits for flow are fine, but keep every number exact).
- **One visual per slide** (figure, table or simple diagram) plus at most 3–4 short bullets. No paragraphs on slides.
- **Series colours** (match the figures): **order = #2a78d6** (blue), **hawker = #eb6834** (orange). Text in neutral dark grey/black, not series colours.
- **No new charts with two y-axes.** Use the provided figures as they are, or crop panels from them.

## 3. Figures (PNG, in the hawkerflow-qa repo)

| File | Shows | Use on |
|---|---|---|
| `evidence/figures/fig1_run0_vs_run1.png` | 2×2: requests reaching the services (top) and running tasks per service (bottom); left = run 0, right = run 1; held steps shaded and labelled 25/50/100/200 req/s | Slide 2 (crop **left column**, top panel at minimum), Slide 3 (crop **right column**) |
| `evidence/figures/fig2_order_bottleneck.png` | Run 1, order service: tasks, CPU vs 60% target, orders waiting in queue | Slide 4 |
| **`evidence/figures/slides/s2_run0_gateway_cap.png`** (1920×1080, large text) | Run 0: load offered by k6 (dashed, up to 200 req/s) vs load reaching the services (flat at ~37 req/s) | **Slide 2 (preferred)** |
| **`evidence/figures/slides/s3_run1_scaling.png`** (1920×1080) | Run 1: running tasks per service rising with the load steps (order 1 → 5, hawker 1 → 3) | **Slide 3 (preferred)** |
| **`evidence/figures/slides/s4_order_backlog_run1_vs_run2.png`** (1920×1080) | Orders waiting in queue and order tasks, run 1 (grey, before HA) vs run 2 (blue, HA): both queue at 100 req/s (peaks 738 / 971) | **Slide 4 (preferred)** |

The slide-sized figures are made for projection; use them in preference to the report figures above.

GitHub copies: `https://github.com/nus-mtechse-hawkerflow/hawkerflow-qa/tree/main/evidence/figures`

## 4. Key facts (the only numbers to use)

**Assumptions (seed-scale workload model; label them as assumptions):**
- ~**40 requests/s** at lunch peak
- **70%** browse stalls / **30%** place an order
- Targets: browse **p95 < 300 ms**; order placement **p95 < 500 ms**; order created (end-to-end) **p95 < 10 s**; errors **< 1%**. p95 = 95% of requests were faster than this.

**Method:**
- k6 load generator run from GitHub Actions against the live API.
- Steps of **25 → 50 → 100 → 200 requests/s**, each held 7 minutes (5 in run 0).
- Measured: k6 (what users see) + CloudWatch (tasks, CPU, order queue, database).
- Path: k6 → API Gateway → load balancer → ECS services (order, hawker) → PostgreSQL. Orders go API Gateway → **SQS queue** → order worker.

**Run 0 (17 Oct), API Gateway limited to 50 req/s:**
- The limit applied to the **whole API**.
- **19%** of requests rejected at 50 req/s; 54% at 100; **76%** at 200.
- Requests reaching the services stayed **flat at ~2,200/min** while offered load doubled.
- Fix: gateway limit **50 → 500 req/s**; max tasks **order 3 → 5, hawker 2 → 3**.

**Run 1 (18 Oct), after the fix:**

| Load (req/s) | Achieved | Rejected | Order created p95 | Browse p95 | Order placement p95 | Tasks |
|---|---|---|---|---|---|---|
| **25** | 26 | 0 | **1.0 s** | 236 ms | 239 ms | order 1, hawker 1 |
| **50** | 50 | 0 | **1.0 s** | 242 ms | 237 ms | order 2, hawker 2 |
| 100 | 97 | 0 | 52 s | 250 ms | 238 ms | order 4, hawker 3 |
| 200 | 189 | 0 | 1.1 s | 14.3 s | 237 ms | order 5 (max), hawker 3 (max) |

- **All targets met at 25 and 50 req/s.** No requests rejected at any step.
- **Scaling:** order **1 → 5** tasks, hawker **1 → 3**, each ~**6 minutes** after its CPU passed the 60% scaling target.
- **100 req/s:** order scaled too slowly; **738 orders queued** (oldest 72 s), orders took up to **52 s** to be created; the queue fully cleared once order reached 4–5 tasks. **Order placement stayed ~0.24 s throughout** (the queue design works: diners are accepted immediately).
- **Why scaling was slow:** the scaling alarm needs ~3 minutes of high CPU; a new task takes 1–2 minutes to start; CPU can't exceed 100%, so the first scale-up was too small (2 → 4 tasks, then 4 → 5 later).
- **200 req/s:** hawker hit its **maximum of 3 tasks**; browsing slowed to **14 s**.
- **Database not a bottleneck:** peak **45% CPU, 15 connections**.

**Capacity:**
- Within targets up to **50 req/s = 1.25× the peak**.
- Run 1 (before HA): throughput sustained to ~190 req/s (4.7×). **Run 2 (HA): 200 req/s = 5× the peak fully served**, with slower responses above 50–100 req/s. Use the run 2 figure on slides.

**High availability (added by the team after run 1):** min **2 tasks per service across 2 availability zones**, **Multi-AZ database**.

**Run 2 (23 Oct), same test with HA (min 2 tasks across 2 AZs, Multi-AZ database; hawker max raised to 5 by the team):**

| Load (req/s) | Achieved | Rejected | Order created p95 | Browse p95 | Order placement p95 | Tasks |
|---|---|---|---|---|---|---|
| **25** | 26 | 0 | **0.94 s** | 231 ms | 223 ms | order 2, hawker 2 (no scaling needed) |
| **50** | 50 | 0 | **0.95 s** | 231 ms | 221 ms | order 2, hawker 2 (no scaling needed) |
| 100 | 98 | 0 | 55 s | 1.4 s | 221 ms | order 2 → 5, hawker 2 → 3 |
| 200 | **200** | 0 | 1.2 s | **2.0 s** | 220 ms | order 5, hawker 5 |

- **Targets met at 25 and 50 with no scaling at all**: the two starting tasks per service covered the peak.
- **The 100 req/s queue still built up** (peak **971**, oldest 74 s, up to 55 s to create an order). Starting with 2 tasks doesn't cover a sudden doubling; order still had to scale out, which takes minutes. Placing an order stayed ~0.22 s.
- **200 req/s fully served** (200 of 200; browse p95 **2.0 s** vs 14.3 s in run 1), because hawker could now reach 5 tasks.
- **Database is the next bottleneck:** peak **80% CPU** at 200 req/s (45% in run 1), 19 connections.
- Scaling: order and hawker each scaled out ~6 min after CPU passed the target.

## 5. Slides

### Slide 1: Load testing & scaling: goal and approach
**On slide:**
- Goal: handle the lunch peak and scale automatically
- Assumptions: ~40 req/s at peak · 70% browse / 30% order · targets: p95 < 300 ms browse, < 500 ms order placement, orders created < 10 s, errors < 1%
- Test: k6 from GitHub Actions, steps 25 → 50 → 100 → 200 req/s

**Visual:** a simple **staircase** of the four steps, annotated: 25 "below peak", 50 "just above peak", 100 "2.5×", 200 "5×: find the limit". A small one-line path underneath: *k6 → API Gateway → ECS (order, hawker) → database; orders via SQS queue*.

**Notes:** "Our goal was to show the platform handles the lunch peak and scales automatically. We assumed about 40 requests per second at peak for our seed centre, with 70% of users browsing and 30% ordering, and set response-time targets based on the 95th percentile, so 19 of 20 requests must be faster than the target. We ran k6 from GitHub Actions against the live system, raising the load in steps from 25 to 200 requests per second, each held for 7 minutes so auto-scaling has time to react, and measured both what users see and what the servers do."

### Slide 2: Run 0: the first bottleneck wasn't our code
**On slide:**
- API Gateway limit: 50 req/s for the whole API
- **19% rejected even at the peak** (50 req/s)
- Fix: limit → 500 req/s, more tasks allowed

**Visual:** Figure 1, **left column** (run 0), at least the top panel: the flat line. Optional callout: "flat at ~2,200/min".

**Notes:** "Our first run found a bottleneck before our code. API Gateway was limited to 50 requests per second for the whole API. Because each order also polls for its status, even our lunch peak went over it: 19% of requests were rejected at 50 requests per second. You can see the requests reaching our services stay flat while the offered load keeps doubling. We raised the limit to 500 and allowed more tasks per service, then measured again."

### Slide 3: Run 1: requirement met, and the system scales
**On slide:**
- **All targets met at 25 and 50 req/s**
- Tasks scale automatically: order 1 → 5, hawker 1 → 3
- No requests rejected at any load

**Visual:** Figure 1, **right column** (run 1), plus a compact table: rows 25 / 50 / 100 / 200, columns *Order created p95*, *Browse p95*, *Tasks*. Highlight rows 25 and 50 as "within targets"; grey out 100 and 200 as "beyond peak".

**Notes:** "With the gateway out of the way, the lunch-peak steps met every target: orders were created in about one second, with no errors. As load increased, ECS added tasks automatically: the order service grew from one to five tasks and the hawker service from one to three, each about six minutes after CPU passed its target. Nothing was rejected at any load level."

### Slide 4: Beyond the peak: the queue absorbs overload
**On slide:**
- 100 req/s: order scaled slowly → **738 orders queued**, up to 52 s to create
- **Order placement stayed ~0.24 s**: diners never waited to be accepted
- Why slow: ~3 min alarm + 1–2 min task start; CPU capped at 100% → first step too small
- Re-tested with HA (2 tasks from the start): **queue still builds** (peak 971): starting headroom doesn't cover a sudden doubling

**Visual:** `slides/s4_order_backlog_run1_vs_run2.png` (queue and order tasks, run 1 grey vs run 2 blue). Fallback: Figure 2.

**Notes:** "At 100 requests per second, two and a half times the peak, the order service couldn't scale fast enough: the scaling alarm needs about three minutes of high CPU, new tasks take one to two minutes to start, and because CPU can't go above 100%, the first scale-up was too small. Orders queued up, 738 at the peak, and took up to 52 seconds to be created. But placing an order stayed at about a quarter of a second throughout. That's our queue design working: diners are accepted immediately, and processing catches up once capacity arrives. We re-ran the test after the team enabled high availability, with two tasks per service from the start. The peak needed no scaling at all, but at 100 requests per second the queue still built up, because a sudden doubling needs four to five order tasks, and adding them still takes minutes. So the fix is faster scaling, not just a higher minimum."

### Slide 5: Capacity, lessons, next steps
**On slide:** three big numbers:
- **1.25×** peak within all targets (50 req/s)
- **5×** peak served (200 req/s, with HA)
- **~6 min** to scale out

**Lessons:** check configuration before testing · measure before tuning · scaling takes minutes, so keep headroom
**Next:** bigger order tasks or an earlier CPU trigger · database is the next limit (80% CPU at 200 req/s) · client poll back-off · HA (2 tasks × 2 AZs, Multi-AZ database) now in place

**Notes:** "In summary: we meet all targets at 1.25 times our expected peak, and with high availability the system served the full 200 requests per second, five times the peak, with slower responses above it. Three lessons: check configuration before testing (our first bottleneck was a setting); measure before tuning (our scaling targets were defaults until the data told us where they fail); and scaling takes minutes, so headroom matters for sudden rushes. Next, we'd give the order service bigger tasks or an earlier trigger, raise the hawker limit, and have the app poll less aggressively. At 200 requests per second the database reached 80% CPU, so it's the next limit to watch. Now let's see the system in action."

## 6. Rules

- **Use only the numbers above.** If something seems missing, leave a visible placeholder rather than estimating.
- **Label the workload model as assumptions.**
- Keep **USL**, k6 internals, "virtual users", CloudWatch metric names and Terraform out of the slides; they're Q&A material.
- **Latency on slides is client-side p95** (includes ~220 ms of network from the US-based test runner). Don't add server-side numbers to slides; the presenter covers that in Q&A.
- **Runs 0 and 1 are from before HA was enabled; run 2 is the HA test.** Always attribute each number to its run (slides 2–3: runs 0/1; slide 4: run 1 vs 2; slide 5: "5× peak served" is run 2).
- Consistent names: "order service", "hawker service", "API Gateway", "SQS queue", "requests/s" (or "req/s").

## 7. Presenter Q&A notes (not for slides)

- **Why 40 req/s?** A seed-scale assumption from the proposal; we tested to 5× so the conclusion doesn't depend on it being exact.
- **Why p95?** Averages hide slow requests; p95 shows what 1 in 20 users experience.
- **240 ms seems slow.** ~220 ms is network from the US test runner to Singapore; servers answered in 6–10 ms at the peak.
- **Why was scaling slow?** Target-tracking alarms need 3 one-minute datapoints; Fargate tasks take 1–2 min; CPU capped at 100% under-sizes the step. The queue-backlog policy fired only after the backlog peaked (metric delay).
- **Database limits?** 15 connections used of ~80–110; with more tasks, the per-service connection pools should shrink.
- **Scale-in?** Deliberately slow: extra tasks ran ~33 min after the load stopped.
- **USL fit?** Run 1's was weak (R² 0.57). Run 2's is good (R² 0.998): predicted peak ~240 req/s (≈6× the peak), consistent with the database reaching 80% CPU at 200 req/s.
- **Did HA help?** Yes at the peak (no scaling needed at 25/50) and at 200 req/s (fully served, with hawker able to reach 5 tasks). No for the sudden jump to 100 (the queue still built up; scaling speed is the limit).
- **Database at 80%?** At 200 req/s, more browse traffic reached it (hawker 5 tasks), the stall list is bigger (5 stalls), and Multi-AZ adds synchronous replication. Next steps: watch CPU credits (burstable instance), shrink connection pools, or a larger instance.
