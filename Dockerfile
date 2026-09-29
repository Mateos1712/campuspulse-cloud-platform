FROM python:3.12-slim AS builder

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /build
COPY pyproject.toml README.md ./
COPY app ./app
RUN python -m pip install --prefix=/install .

FROM builder AS test
RUN python -m pip install -e '.[dev]'
CMD ["pytest", "-q", "--cov=app", "--cov-report=term-missing"]

FROM python:3.12-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/home/app/.local/bin:${PATH}" \
    APP_ENV=production \
    APP_VERSION=0.1.0

RUN groupadd --gid 10001 app && useradd --uid 10001 --gid app --create-home app
COPY --from=builder /install /usr/local
WORKDIR /app
COPY --chown=app:app app ./app
USER 10001:10001
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
  CMD ["python", "-c", "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/healthz', timeout=2)"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
