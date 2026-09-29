#!/usr/bin/env bash
set -Eeuo pipefail

base_url="${1:-http://localhost:8000}"

health_status="$(curl --silent --show-error --output /dev/null --write-out '%{http_code}' "${base_url}/healthz")"
summary_status="$(curl --silent --show-error --output /dev/null --write-out '%{http_code}' "${base_url}/api/v1/engagement/summary")"

if [[ "${health_status}" != "200" || "${summary_status}" != "200" ]]; then
  echo "Smoke test failed: health=${health_status} summary=${summary_status}" >&2
  exit 1
fi

echo "Smoke test passed for ${base_url}"

