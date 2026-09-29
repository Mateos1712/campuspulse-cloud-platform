import logging
import os
import time
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, Response, status
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest

from app.models import EngagementEvent, EngagementSummary
from app.service import EngagementService
from app.telemetry import ENGAGEMENT_EVENTS, HTTP_DURATION, HTTP_REQUESTS, IN_PROGRESS

logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
LOGGER = logging.getLogger("campuspulse")
SERVICE = EngagementService()


@asynccontextmanager
async def lifespan(_: FastAPI):
    LOGGER.info("service_started env=%s", os.getenv("APP_ENV", "local"))
    yield
    LOGGER.info("service_stopped")


app = FastAPI(
    title="CampusPulse API",
    version=os.getenv("APP_VERSION", "0.1.0"),
    description="Synthetic student-engagement service for a Cloud Engineer portfolio.",
    lifespan=lifespan,
)


@app.middleware("http")
async def observe_request(request: Request, call_next):
    path = request.url.path
    start = time.perf_counter()
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    IN_PROGRESS.inc()
    try:
        response = await call_next(request)
        status_code = response.status_code
        return response
    finally:
        duration = time.perf_counter() - start
        IN_PROGRESS.dec()
        HTTP_REQUESTS.labels(request.method, path, str(status_code)).inc()
        HTTP_DURATION.labels(request.method, path).observe(duration)


@app.get("/", tags=["service"])
def root() -> dict[str, str]:
    return {
        "service": "campuspulse",
        "environment": os.getenv("APP_ENV", "local"),
        "version": os.getenv("APP_VERSION", "0.1.0"),
    }


@app.get("/healthz", tags=["service"])
def health() -> dict[str, str]:
    return {"status": "healthy"}


@app.get("/readyz", tags=["service"])
def readiness() -> dict[str, str]:
    return {"status": "ready"}


@app.get("/metrics", include_in_schema=False)
def metrics() -> Response:
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)


@app.get("/api/v1/engagement/summary", response_model=EngagementSummary, tags=["engagement"])
def get_summary() -> EngagementSummary:
    return SERVICE.summary()


@app.post(
    "/api/v1/engagement/events",
    response_model=EngagementEvent,
    status_code=status.HTTP_202_ACCEPTED,
    tags=["engagement"],
)
def record_event(event: EngagementEvent) -> EngagementEvent:
    ENGAGEMENT_EVENTS.labels(event.event_type.value).inc()
    return SERVICE.record(event)

