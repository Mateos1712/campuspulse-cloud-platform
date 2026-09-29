#!/usr/bin/env bash
set -Eeuo pipefail

base_url="${1:-http://localhost:8000}"
requests="${2:-100}"

for ((index = 1; index <= requests; index++)); do
  curl --silent --output /dev/null "${base_url}/api/v1/engagement/summary"
  if (( index % 10 == 0 )); then
    echo "Generated ${index}/${requests} requests"
  fi
done

