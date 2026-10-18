// HawkerFlow load test: the lunch-peak workload from PR1, against the deployed stack.
//
//   browse   (70%)  GET  /hawker/v1/hawker/stalls          - the public catalogue read
//   checkout (30%)  POST <ORDER_QUEUE_URL>                  - API Gateway -> SQS, as the diner app does
//                   GET  <ORDER_QUEUE_URL>/<order_ref>      - poll until the worker has created the order
//
// The checkout scenario measures two things separately:
//   http_req_duration{name:order_enqueue}  how fast the platform ACCEPTS an order (the diner's wait)
//   order_e2e_ms                           how long until the order EXISTS in PostgreSQL (queue + worker)
// Under a spike the first should stay flat while the second grows and then recovers
// as ECS adds Order tasks. That contrast is the scalability evidence.
//
// Usage:
//   k6 run loadtest/hawkerflow.js \
//     -e API_BASE_URL=https://<api-id>.execute-api.ap-southeast-1.amazonaws.com \
//     -e ORDER_QUEUE_URL=<same value as the diner app's ORDER_QUEUE_URL> \
//     -e PROFILE=step \
//     --summary-export=reports/summary.json
//
// PROFILE: smoke | step | spike | soak   (default smoke)
// HOLD:    plateau length for `step` (default 7m). Run 0 showed ~5-6 min from a scaling
//          threshold breach to a new task serving (~3 min alarm + launch + metric lag);
//          7 min lets each step show the new task settle.
// DESIGN_MAX_RPS: steps at or below this offered rate must meet the SLOs (default 50);
//          higher steps are observation-only (capacity testing: they may degrade).
// STALL_IDS: comma-separated stall IDs to order from (use dedicated load-test stalls)
// CHECKOUT_MODE: queue (default, production path) | direct (POST /v1/order/orders, local runs without SQS)

import http from 'k6/http';
import exec from 'k6/execution';
import { check, fail, sleep } from 'k6';
import { Counter, Trend } from 'k6/metrics';

const BASE = (__ENV.API_BASE_URL || 'http://localhost:8080').replace(/\/$/, '');
// HAWKER_URL / ORDER_URL override the whole service URL (services on separate hosts, local runs).
const HAWKER = (__ENV.HAWKER_URL || BASE + (__ENV.HAWKER_PATH || '/hawker')).replace(/\/$/, '');
const ORDER = (__ENV.ORDER_URL || BASE + (__ENV.ORDER_PATH || '/order')).replace(/\/$/, '');
const QUEUE_URL = (__ENV.ORDER_QUEUE_URL || `${ORDER}/v1/order/orders/queue`).replace(/\/$/, '');
const CHECKOUT_MODE = __ENV.CHECKOUT_MODE || 'queue';
const PROFILE = __ENV.PROFILE || 'smoke';
const HOLD = __ENV.HOLD || '7m';
const DESIGN_MAX_RPS = Number(__ENV.DESIGN_MAX_RPS || 50);
const POLL_INTERVAL_S = Number(__ENV.POLL_INTERVAL_S || 0.5);
const POLL_TIMEOUT_S = Number(__ENV.POLL_TIMEOUT_S || 60);
const BROWSE_SHARE = 0.7;

const orderE2E = new Trend('order_e2e_ms', true);
const ordersCreated = new Counter('orders_created');
const ordersTimedOut = new Counter('orders_timed_out');
// Requests rejected by a rate limit (API Gateway throttling), kept separate from service errors.
// 429 still counts as a failed request: it is not added to the expected statuses.
const throttled = new Counter('throttled_429');

// ---------------------------------------------------------------- load profiles
// Each profile is a list of [duration, total requests/s]; browse/checkout split 70/30.
const PROFILES = {
  smoke: [['30s', 5], ['1m', 5]],
  // Stepped: seed scale (~40 rps from PR1), then 2x, 4x, 8x. Each step holds long
  // enough for CloudWatch alarms (1-min datapoints) to trigger a scale-out.
  step: [
    ['1m', 25], [HOLD, 25],
    ['1m', 50], [HOLD, 50],
    ['1m', 100], [HOLD, 100],
    ['1m', 200], [HOLD, 200],
    ['2m', 0],
  ],
  // Lunch spike: quiet, sudden 10x surge, back to quiet. The 15-minute surge outlasts the
  // ~5-6 min scale-out so the recovery is visible; the 10-minute tail shows the queue
  // backlog draining and scale-in starting.
  spike: [['1m', 20], ['3m', 20], ['30s', 200], ['15m', 200], ['30s', 20], ['10m', 20], ['1m', 0]],
  // Soak: seed load for 30 minutes (memory leaks, connection-pool exhaustion).
  soak: [['2m', 40], ['30m', 40], ['1m', 0]],
};

if (!PROFILES[PROFILE]) fail(`Unknown PROFILE '${PROFILE}'. Use: ${Object.keys(PROFILES).join(', ')}`);

function stagesFor(share) {
  return PROFILES[PROFILE].map(([duration, rps]) => ({ duration, target: Math.max(0, Math.round(rps * share)) }));
}

function startRate(share) {
  return Math.max(1, Math.round(PROFILES[PROFILE][0][1] * share * 0.2));
}

// ---------------------------------------------------------------- plateaus (per-step results)
// A plateau is a stage that holds the previous stage's rate. Requests made during a
// plateau are tagged step:<rps> (ramps are tagged step:ramp), so the summary has
// per-step throughput and latency for usl_fit.py.
function seconds(duration) {
  let total = 0;
  for (const [, n, unit] of String(duration).matchAll(/(\d+(?:\.\d+)?)(h|m|s)/g)) {
    total += Number(n) * { h: 3600, m: 60, s: 1 }[unit];
  }
  return total;
}

const PLATEAUS = []; // [startS, endS, rps]
{
  let t = 0;
  let prev = null;
  for (const [duration, rps] of PROFILES[PROFILE]) {
    const d = seconds(duration);
    if (rps > 0 && rps === prev) PLATEAUS.push([t, t + d, rps]);
    t += d;
    prev = rps;
  }
}
const PLATEAU_RATES = [...new Set(PLATEAUS.map(([, , rps]) => rps))];

function currentStep() {
  const elapsedS = (Date.now() - exec.scenario.startTime) / 1000;
  const p = PLATEAUS.find(([start, end]) => elapsedS >= start && elapsedS < end);
  return p ? String(p[2]) : 'ramp';
}

// Thresholds that always pass, only so the summary export includes per-step sub-metrics.
function perStepSubmetrics() {
  const t = {};
  for (const rps of PLATEAU_RATES) {
    for (const name of ['stalls', 'order_enqueue']) {
      // Successful requests only, so throttled (429) responses don't count as throughput.
      t[`http_reqs{name:${name},step:${rps},expected_response:true}`] = ['count>=0'];
      t[`http_req_duration{name:${name},step:${rps},expected_response:true}`] = ['avg>=0'];
    }
    t[`http_req_failed{step:${rps}}`] = ['rate>=0'];
    t[`order_e2e_ms{step:${rps}}`] = ['avg>=0'];
    t[`http_reqs{step:${rps}}`] = ['count>=0']; // gateway calls incl. polls, all statuses
    t[`orders_created{step:${rps}}`] = ['count>=0'];
    t[`throttled_429{step:${rps}}`] = ['count>=0'];
  }
  return t;
}

// SLOs (PR1/PR2 section 4.1), scoped per profile. `abortOnFail: false` throughout so a
// breach is recorded and the run continues to show the whole curve.
function addThreshold(t, key, expr) {
  t[key] = [...(t[key] || []), expr];
}

function sloThresholds(tagSuffix, { e2e = true } = {}) {
  const s = tagSuffix ? `,${tagSuffix}` : '';
  const one = tagSuffix ? `{${tagSuffix}}` : '';
  const t = {
    [`http_req_duration{name:stalls${s}}`]: ['p(95)<300'],
    [`http_req_duration{name:order_enqueue${s}}`]: ['p(95)<500'],
    [`http_req_failed{name:stalls${s}}`]: ['rate<0.01'],
    [`http_req_failed{name:order_enqueue${s}}`]: ['rate<0.01'],
    [`orders_timed_out${one}`]: ['count<1'],
    [`checks${one}`]: ['rate>0.99'],
  };
  if (e2e) t[`order_e2e_ms${one}`] = ['p(95)<10000'];
  return t;
}

function buildThresholds() {
  const t = { dropped_iterations: ['count<1'] }; // k6 ran out of VUs => load not offered as configured
  if (PROFILE === 'step') {
    // Capacity test: only steps within design load must meet the SLOs; higher steps are
    // observation-only (their per-step sub-metrics still appear in the summary).
    for (const rps of PLATEAU_RATES.filter((r) => r <= DESIGN_MAX_RPS)) {
      for (const [k, v] of Object.entries(sloThresholds(`step:${rps}`))) v.forEach((e) => addThreshold(t, k, e));
    }
  } else if (PROFILE === 'spike') {
    // SQS exists so orders can queue during a surge: end-to-end time is expected to exceed
    // 10 s at 10x load. The claims are: diners are accepted fast, no order is lost.
    Object.assign(t, {
      'http_req_duration{name:order_enqueue}': ['p(95)<500'],
      'http_req_failed{name:order_enqueue}': ['rate<0.01'],
      orders_timed_out: ['count<1'],
    });
  } else {
    Object.assign(t, sloThresholds(''));
  }
  for (const [k, v] of Object.entries(perStepSubmetrics())) v.forEach((e) => addThreshold(t, k, e));
  return t;
}

export const options = {
  scenarios: {
    browse: {
      executor: 'ramping-arrival-rate',
      exec: 'browse',
      startRate: startRate(BROWSE_SHARE),
      timeUnit: '1s',
      stages: stagesFor(BROWSE_SHARE),
      preAllocatedVUs: 50,
      maxVUs: 600,
    },
    checkout: {
      executor: 'ramping-arrival-rate',
      exec: 'checkout',
      startRate: startRate(1 - BROWSE_SHARE),
      timeUnit: '1s',
      stages: stagesFor(1 - BROWSE_SHARE),
      // Each checkout iteration polls until the order exists, so it holds a VU longer.
      preAllocatedVUs: 100,
      maxVUs: 1500,
    },
  },
  thresholds: buildThresholds(),
  summaryTrendStats: ['avg', 'min', 'med', 'p(90)', 'p(95)', 'p(99)', 'max'],
  userAgent: 'hawkerflow-loadtest/1.0',
};

// ---------------------------------------------------------------- setup: real menu data
export function setup() {
  const res = http.get(`${HAWKER}/v1/hawker/stalls`, { tags: { name: 'stalls_setup' } });
  if (res.status !== 200) fail(`Cannot load stalls: ${res.status} ${res.body}`);

  const wanted = (__ENV.STALL_IDS || '')
    .split(',')
    .map((s) => s.trim())
    .filter(Boolean)
    .map(Number);

  const catalogue = [];
  for (const stall of res.json('stalls') || []) {
    const menu = (stall.stall_menu || []).map((m) => ({
      dish_id: m.f_menu_id,
      dish_name: m.f_menu_name,
      price: m.f_menu_price,
      stall_id: m.f_stall_id,
    }));
    const stallId = menu.length ? menu[0].stall_id : (stall.stall_owner || [{}])[0].f_stall_id;
    if (!menu.length || stallId === undefined) continue;
    if (wanted.length && !wanted.includes(stallId)) continue;
    catalogue.push({ stall_id: stallId, menu });
  }

  if (!catalogue.length) fail('No stalls with menu items to order from (check STALL_IDS).');
  console.log(`Ordering from ${catalogue.length} stall(s): ${catalogue.map((s) => s.stall_id).join(', ')}`);
  // Read by usl_fit.py from the k6 output: plateau start/end (s) and rate.
  console.log(`PLATEAUS: ${JSON.stringify(PLATEAUS)}`);
  return { catalogue };
}

// ---------------------------------------------------------------- helpers
function pick(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

function uuidv4() {
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, (c) => {
    const r = (Math.random() * 16) | 0;
    return (c === 'x' ? r : (r & 0x3) | 0x8).toString(16);
  });
}

// A basket of 1-2 stalls, 1-3 dishes each: the shape the diner app sends.
function basket(catalogue) {
  const stalls = [pick(catalogue)];
  if (catalogue.length > 1 && Math.random() < 0.3) {
    const other = pick(catalogue.filter((s) => s.stall_id !== stalls[0].stall_id));
    if (other) stalls.push(other);
  }

  let total = 0;
  const orders = stalls.map((s) => {
    const dishes = [];
    const n = 1 + Math.floor(Math.random() * 3);
    for (let i = 0; i < n; i++) {
      const m = pick(s.menu);
      const quantity = 1 + Math.floor(Math.random() * 2);
      dishes.push({ dish_id: m.dish_id, dish_name: m.dish_name, quantity, price: m.price });
      total += m.price * quantity;
    }
    return { stall_id: s.stall_id, dishes };
  });

  return { orders, total_price: Math.round(total * 100) / 100, dining_option: 'takeaway', takeaway_fee: 0 };
}

const JSON_HEADERS = { 'Content-Type': 'application/json' };

// ---------------------------------------------------------------- scenarios
// Read by usl_fit.py to line plateaus up with CloudWatch (server-side latency).
let startLogged = false;
function logScenarioStart() {
  if (startLogged || exec.vu.idInTest !== 1) return;
  startLogged = true;
  console.log(`SCENARIO_START: ${new Date(exec.scenario.startTime).toISOString()}`);
}

function countThrottle(res, name, step) {
  if (res.status === 429) throttled.add(1, { name, step });
}

export function browse() {
  logScenarioStart();
  const step = currentStep();
  const res = http.get(`${HAWKER}/v1/hawker/stalls`, { tags: { name: 'stalls', step } });
  countThrottle(res, 'stalls', step);
  check(res, {
    'stalls 200': (r) => r.status === 200,
    'stalls has data': (r) => r.status === 200 && Array.isArray(r.json('stalls')),
  }, { step });
}

export function checkout(data) {
  logScenarioStart();
  const payload = basket(data.catalogue);
  const step = currentStep();

  if (CHECKOUT_MODE === 'direct') {
    const res = http.post(`${ORDER}/v1/order/orders`, JSON.stringify(payload), {
      headers: JSON_HEADERS,
      tags: { name: 'order_enqueue', step },
    });
    countThrottle(res, 'order_enqueue', step);
    const ok = check(res, { 'order accepted': (r) => r.status === 200 }, { step });
    if (ok) {
      orderE2E.add(res.timings.duration, { step });
      ordersCreated.add(1, { step });
    }
    return;
  }

  // Production path: the same body the diner app posts to API Gateway.
  const orderRef = uuidv4();
  const started = Date.now();
  const res = http.post(
    QUEUE_URL,
    JSON.stringify({ event_type: 'ORDER_PLACED', order_ref: orderRef, data: payload }),
    { headers: JSON_HEADERS, tags: { name: 'order_enqueue', step } },
  );
  countThrottle(res, 'order_enqueue', step);
  if (!check(res, { 'order accepted by queue': (r) => r.status === 200 }, { step })) return;

  // Poll until the SQS worker has written the order (202 PENDING -> 200 CREATED).
  // Orders are counted against the step the checkout started in; polls against the
  // step they ran in (for gateway calls per step).
  const deadline = started + POLL_TIMEOUT_S * 1000;
  while (Date.now() < deadline) {
    sleep(POLL_INTERVAL_S);
    const pollStep = currentStep();
    const poll = http.get(`${QUEUE_URL}/${orderRef}`, { tags: { name: 'order_poll', step: pollStep } });
    if (poll.status === 200 && poll.json('status') === 'CREATED') {
      orderE2E.add(Date.now() - started, { step });
      ordersCreated.add(1, { step });
      check(poll, { 'order created': () => true }, { step });
      return;
    }
    if (poll.status === 429) {
      // Throttled poll: the order may already exist, so keep polling rather than
      // failing the order (that would drop its end-to-end time and inflate failures).
      countThrottle(poll, 'order_poll', pollStep);
      continue;
    }
    if (poll.status !== 202) {
      check(poll, { 'order poll ok': () => false }, { step });
      return;
    }
  }
  ordersTimedOut.add(1, { step });
  check(null, { 'order created': () => false }, { step });
}
