from prometheus_client import Counter, Gauge, Histogram

HTTP_REQUESTS = Counter(
    "campuspulse_http_requests_total",
    "Total number of HTTP requests",
    ["method", "path", "status"],
)

HTTP_DURATION = Histogram(
    "campuspulse_http_request_duration_seconds",
    "HTTP request latency in seconds",
    ["method", "path"],
    buckets=(0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5),
)

IN_PROGRESS = Gauge(
    "campuspulse_http_requests_in_progress",
    "Current HTTP requests in progress",
)

ENGAGEMENT_EVENTS = Counter(
    "campuspulse_engagement_events_total",
    "Accepted synthetic engagement events",
    ["event_type"],
)

