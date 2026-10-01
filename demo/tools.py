"""Herramienta del agente de la diapositiva 12 (la importa agent.py).

duckdb_query: SQL de solo lectura sobre los viajes de taxi NYC ene-mar 2025
(demo/data/*.parquet, vista `trips`). Mismo mecanismo que la demo de apertura,
otro dataset: sin red, sin D1, sin afirmación bancaria.

Probar la rama de rechazo a mano (la solicitud la escribe el orador):
  uv run --with duckdb python demo/tools.py "DROP TABLE trips"
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TAXI_GLOB = str(HERE / "data" / "*.parquet")
KEY_FILES = (HERE / ".env", HERE.parents[1] / "h1sort-website" / ".dev.vars")


def load_anthropic_key() -> None:
    """Carga ANTHROPIC_API_KEY del entorno, demo/.env o ../h1sort-website/.dev.vars. Nunca la imprime."""
    if os.environ.get("ANTHROPIC_API_KEY"):
        return
    for path in KEY_FILES:
        if not path.is_file():
            continue
        for line in path.read_text().splitlines():
            line = line.strip()
            if line.startswith("ANTHROPIC_API_KEY="):
                value = line.split("=", 1)[1].strip().strip("'\"")
                if value:
                    os.environ["ANTHROPIC_API_KEY"] = value
                    return
    raise RuntimeError("falta ANTHROPIC_API_KEY (entorno, demo/.env o ../h1sort-website/.dev.vars)")


_FORBIDDEN = re.compile(r"\b(insert|update|delete|drop|alter|create|copy|attach|pragma|call|export)\b", re.I)


def duckdb_query(sql: str) -> str:
    """SQL de solo lectura sobre los viajes de taxi NYC ene-mar 2025 (vista `trips`)."""
    import duckdb

    if _FORBIDDEN.search(sql):
        return "error: solo se permiten consultas de lectura (SELECT) sobre `trips`"
    con = duckdb.connect(":memory:")
    con.execute(f"CREATE VIEW trips AS SELECT * FROM read_parquet('{TAXI_GLOB}')")
    try:
        con.execute(sql)
        rows = con.fetchall()
        cols = [d[0] for d in con.description]
    except Exception as exc:  # se lo devolvemos al modelo como observación, no lo tumbamos
        return f"error ejecutando SQL: {exc}"
    preview = "\n".join(str(r) for r in rows[:20])
    more = "" if len(rows) <= 20 else f"\n... ({len(rows) - 20} filas más)"
    return f"columnas: {cols}\n{preview}{more}"


def extract_text(content) -> str:
    """El SDK devuelve bloques (thinking + texto) cuando piensa; nos quedamos con el texto."""
    if isinstance(content, str):
        return content
    return "\n".join(b.get("text", "") for b in content if isinstance(b, dict) and b.get("type") == "text").strip()


if __name__ == "__main__":
    print(duckdb_query(sys.argv[1] if len(sys.argv) > 1 else "SELECT COUNT(*) FROM trips"))
