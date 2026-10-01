#!/usr/bin/env bash
# Slide-12 live demo: run the agent under pdb, paused right before the harness
# executes the model's tool request.
#
#   demo/run.sh ["pregunta"]
#
# At the (Pdb) prompt:  p call   -> the model's request (nothing has run yet)
#                       n        -> the handler runs
#                       n        -> OBSERVATION > prints
#                       q        -> quit   (or: cl, y, c  -> let the agent finish)
set -euo pipefail
cd "$(dirname "$0")/.."

ls demo/data/*.parquet >/dev/null 2>&1 || { echo "faltan los datos: python3 demo/download_data.py"; exit 1; }
line=$(grep -n "# HARNESS EXECUTES" demo/agent.py | cut -d: -f1)
question="${1:-¿Cuántos viajes hay en el dataset de taxis?}"

exec uv run --quiet --with langchain-anthropic --with langchain-core --with duckdb \
  python -m pdb -c "b $PWD/demo/agent.py:${line}" -c c demo/agent.py "$question"
