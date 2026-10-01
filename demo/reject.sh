#!/usr/bin/env bash
# Slide-12 refusal branch. The speaker types this request, not the model:
#
#   demo/reject.sh                      -> DROP TABLE trips (rejected)
#   demo/reject.sh "SELECT COUNT(*) FROM trips"
set -euo pipefail
cd "$(dirname "$0")/.."
PYTHONDONTWRITEBYTECODE=1 exec uv run --quiet --with duckdb python demo/tools.py "${1:-DROP TABLE trips}"
