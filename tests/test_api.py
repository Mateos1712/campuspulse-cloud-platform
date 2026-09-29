from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_service_lifecycle_and_operational_endpoints() -> None:
    with TestClient(app) as lifecycle_client:
        root_response = lifecycle_client.get("/")
        assert root_response.status_code == 200
        assert root_response.json()["service"] == "campuspulse"

        readiness_response = lifecycle_client.get("/readyz")
        assert readiness_response.status_code == 200
        assert readiness_response.json() == {"status": "ready"}

        metrics_response = lifecycle_client.get("/metrics")
        assert metrics_response.status_code == 200
        assert "campuspulse_http_requests_total" in metrics_response.text


def test_health_endpoint() -> None:
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_summary_uses_only_synthetic_data() -> None:
    response = client.get("/api/v1/engagement/summary")
    assert response.status_code == 200
    payload = response.json()
    assert payload["source"] == "synthetic-demo-data"
    assert payload["active_students"] >= 0


def test_record_event() -> None:
    response = client.post(
        "/api/v1/engagement/events",
        json={
            "student_hash": "sha256-demo-student",
            "course_id": "CS-101",
            "event_type": "course_viewed",
        },
    )
    assert response.status_code == 202
    assert response.json()["event_type"] == "course_viewed"


def test_rejects_invalid_course_id() -> None:
    response = client.post(
        "/api/v1/engagement/events",
        json={
            "student_hash": "sha256-demo-student",
            "course_id": "bad value",
            "event_type": "login",
        },
    )
    assert response.status_code == 422
