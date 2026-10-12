"""HawkerFlow authorization checks (targeted DAST).

ZAP finds generic web flaws; it cannot know that stall 7 must not read stall 3's
orders. These tests do: they attack the deployed API the way a malicious diner
or hawker would and assert the platform refuses.

Every test is NON-DESTRUCTIVE: reads only, or writes aimed at IDs that do not
exist. A test passes when ANY layer stops the attack (the API Gateway JWT
authorizer or the service itself), which is the property that matters.

Run:
    API_BASE_URL=https://<api-id>.execute-api.ap-southeast-1.amazonaws.com \
    VICTIM_STALL_ID=1 pytest dast/authz -v --junitxml=reports/authz.xml

Path prefixes default to the ALB routes in PR2 and can be overridden:
ORDER_PATH, HAWKER_PATH, CUSTOMER_PATH, ANALYTICS_PATH.
"""

import base64
import json
import os
import uuid

import httpx
import pytest

BASE = os.environ.get("API_BASE_URL", "http://localhost:8080").rstrip("/")
ORDER = BASE + os.environ.get("ORDER_PATH", "/order")
HAWKER = BASE + os.environ.get("HAWKER_PATH", "/hawker")
CUSTOMER = BASE + os.environ.get("CUSTOMER_PATH", "/customer")
ANALYTICS = BASE + os.environ.get("ANALYTICS_PATH", "/analytics")

VICTIM_STALL = int(os.environ.get("VICTIM_STALL_ID", "1"))
# Far above any real order ID, so write attempts can never touch real data.
NONEXISTENT_ORDER_ID = 2_000_000_000
EVIL_ORIGIN = "https://evil.example"

DENIED = {401, 403}

client = httpx.Client(timeout=15, follow_redirects=False)


def forged_jwt(claims: dict) -> str:
    """A token with alg=none and no signature: anyone can mint this."""

    def b64(obj: dict) -> str:
        raw = json.dumps(obj, separators=(",", ":")).encode()
        return base64.urlsafe_b64encode(raw).rstrip(b"=").decode()

    return f"{b64({'alg': 'none', 'typ': 'JWT'})}.{b64(claims)}."


def explain(resp: httpx.Response) -> str:
    return f"{resp.request.method} {resp.request.url} -> {resp.status_code}: {resp.text[:200]}"


# ---------------------------------------------------------------- tenant isolation

def test_forged_x_stall_id_cannot_read_another_stalls_orders():
    """A hawker (or anyone) sets X-Stall-ID to a stall they do not own."""
    resp = client.get(
        f"{ORDER}/v1/order/stalls/{VICTIM_STALL}/orders",
        headers={"X-Stall-ID": str(VICTIM_STALL)},
    )
    assert resp.status_code in DENIED, explain(resp)


def test_unsigned_jwt_is_rejected():
    """A hand-made token with no signature claims to be the victim stall."""
    token = forged_jwt({"sub": str(uuid.uuid4()), "custom:stall_id": str(VICTIM_STALL)})
    resp = client.get(
        f"{ORDER}/v1/order/stalls/me/orders",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert resp.status_code in DENIED, explain(resp)


def test_analytics_needs_more_than_a_header():
    """Sales figures for any stall, identified only by a header the caller sets."""
    resp = client.get(
        f"{ANALYTICS}/v1/insights/stalls/{VICTIM_STALL}/summary",
        headers={"X-Stall-ID": str(VICTIM_STALL)},
    )
    assert resp.status_code in DENIED, explain(resp)


# ---------------------------------------------------------------- unauthenticated routes

def test_order_lookup_requires_authentication():
    """Order IDs are sequential integers, so an open lookup leaks every order."""
    resp = client.get(f"{ORDER}/v1/order/orders/1")
    assert resp.status_code in DENIED, explain(resp)


def test_order_status_update_requires_authentication():
    """Anonymous status change. A 404 here still means the handler ran."""
    resp = client.put(
        f"{ORDER}/v1/order/orders/update",
        json={"order_id": NONEXISTENT_ORDER_ID, "status": "CANCELLED"},
    )
    assert resp.status_code in DENIED, explain(resp)


def test_hawker_profile_lookup_requires_authentication():
    resp = client.get(f"{HAWKER}/v1/hawker/me/stall/{uuid.uuid4()}")
    assert resp.status_code in DENIED, explain(resp)


def test_customer_profile_lookup_requires_authentication():
    resp = client.get(f"{CUSTOMER}/v1/customer/user/{uuid.uuid4()}")
    assert resp.status_code in DENIED, explain(resp)


# ---------------------------------------------------------------- exposure / config

def test_queue_diagnostics_are_not_public():
    """/sqs/status reveals the worker's queue configuration."""
    resp = client.get(f"{ORDER}/v1/order/sqs/status")
    assert resp.status_code in DENIED | {404}, explain(resp)


@pytest.mark.parametrize("service", [ORDER, HAWKER, CUSTOMER])
def test_cors_does_not_trust_arbitrary_origins(service):
    """Any website must not be able to make credentialed calls to the API."""
    resp = client.options(
        f"{service}/health",
        headers={"Origin": EVIL_ORIGIN, "Access-Control-Request-Method": "GET"},
    )
    allow_origin = resp.headers.get("access-control-allow-origin")
    allow_creds = resp.headers.get("access-control-allow-credentials", "").lower() == "true"
    assert not (allow_origin == EVIL_ORIGIN and allow_creds), (
        f"{service} reflects {EVIL_ORIGIN} with credentials allowed"
    )
