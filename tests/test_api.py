import pytest
from playwright.sync_api import APIRequestContext

BASE_URL = "https://jsonplaceholder.typicode.com"

# # ── GET Tests ─────────────────────────────────────────────

def test_get_all_posts(api_context):
    response = api_context.get(f"{BASE_URL}/posts")
    assert response.status == 200

def test_get_all_posts_returns_100(api_context):
    response = api_context.get(f"{BASE_URL}/posts")
    body = response.json()
    assert len(body) == 100

def test_get_single_post(api_context):
    response = api_context.get(f"{BASE_URL}/posts/1")
    assert response.status == 200

def test_get_single_post_has_correct_fields(api_context):
    response = api_context.get(f"{BASE_URL}/posts/1")
    body = response.json()
    assert "id" in body
    assert "title" in body
    assert "body" in body
    assert "userId" in body

def test_get_invalid_post_returns_404(api_context):
    response = api_context.get(f"{BASE_URL}/posts/9999")
    assert response.status == 404

# ── POST Tests ────────────────────────────────────────────

def test_create_post(api_context):
    payload = {
        "title": "SDET Portfolio Post",
        "body": "Testing POST endpoint",
        "userId": 1
    }
    response = api_context.post(f"{BASE_URL}/posts", data=payload)
    assert response.status == 201

def test_create_post_returns_id(api_context):
    payload = {
        "title": "SDET Portfolio Post",
        "body": "Testing POST endpoint",
        "userId": 1
    }
    response = api_context.post(f"{BASE_URL}/posts", data=payload)
    body = response.json()
    assert "id" in body

# ── Security Tests (OWASP basics) ─────────────────────────

def test_sql_injection_in_param(api_context):
    response = api_context.get(f"{BASE_URL}/posts?id=1' OR '1'='1")
    # should not crash the server
    assert response.status in [200, 400, 404]

def test_xss_payload_in_param(api_context):
    response = api_context.get(f"{BASE_URL}/posts?title=<script>alert(1)</script>")
    assert response.status in [200, 400, 404]
    body = response.text()
    assert "<script>" not in body

def test_missing_required_fields(api_context):
    response = api_context.post(f"{BASE_URL}/posts", data={})
    # server should handle gracefully
    assert response.status in [200, 201, 400, 422]