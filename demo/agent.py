#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["anthropic"]
# ///
"""Agente de la diapositiva 12: Solicitud -> Validación -> Ejecución -> Observación.

    uv run demo/agent.py

Una sola herramienta, d1_query, que corre `wrangler d1 execute` contra la base de
encuestas de h1sort.com. El modelo solo propone SQL; esta aplicación lo valida con
el compilador de SQLite (solo lectura de las tablas de encuestas) antes de ejecutarlo.

Dentro de la conversación, `/sql <consulta>` manda una solicitud escrita por el
orador directo a la herramienta, sin pasar por el modelo.
"""
from __future__ import annotations

import json
import os
import sqlite3
import subprocess
import sys
import time
from pathlib import Path

import anthropic

MODEL = os.environ.get("MODEL_ID", "claude-opus-5-5")
EFFORT = os.environ.get("EFFORT", "medium")
DATABASE = "h1sort-chat"
SITE_REPO = Path(os.environ.get("H1SORT_SITE", Path(__file__).resolve().parents[2] / "h1sort-website"))
GROUP_CODE = "UFRHASU9D4"
ALLOWED_TABLES = {"poll_groups", "polls", "poll_options", "poll_votes"}
HIDDEN_COLUMNS = {"voter_hash"}  # un navegador, no una persona: nunca se proyecta

DIM, BOLD, RESET = "\033[2m", "\033[1m", "\033[0m"
COLOR = {"SOLICITUD": "\033[33m", "VALIDACIÓN": "\033[36m", "EJECUCIÓN": "\033[32m",
         "OBSERVACIÓN": "\033[32m", "RECHAZADA": "\033[31m", "MODELO": "\033[35m"}


def stage(name: str, text: str) -> None:
    print(f"{COLOR.get(name, '')}{BOLD}{name} ›{RESET} {text}", flush=True)


# ---------- ejecución: el CLI de wrangler ----------

def wrangler(sql: str, show: bool = False) -> list[dict]:
    started = time.monotonic()
    proc = subprocess.run(
        ["npx", "wrangler", "d1", "execute", DATABASE, "--remote", "--json", "--command", sql],
        cwd=SITE_REPO, capture_output=True, text=True, timeout=90,
    )
    try:
        payload = json.loads(proc.stdout)
    except ValueError:
        raise RuntimeError((proc.stderr or proc.stdout).strip()[-400:] or "wrangler no respondió")
    if isinstance(payload, dict) and "error" in payload:
        raise RuntimeError(str(payload["error"].get("text", payload["error"]))[:400])
    rows = payload[0]["results"]
    if show:
        stage("EJECUCIÓN", f"wrangler d1 execute {DATABASE} --remote · {len(rows)} filas · {time.monotonic() - started:.1f} s")
    return rows


# ---------- validación: el compilador de SQLite decide qué se puede leer ----------

def load_schema() -> tuple[sqlite3.Connection, dict[str, str]]:
    """Copia vacía del esquema real, solo para compilar (nunca contiene datos)."""
    con = sqlite3.connect(":memory:")
    ddl = {}
    for row in wrangler("SELECT name, sql FROM sqlite_master WHERE type = 'table' AND sql IS NOT NULL"):
        try:
            con.execute(row["sql"])
            ddl[row["name"]] = row["sql"]
        except sqlite3.Error:
            pass  # tablas internas de D1/SQLite
    con.set_authorizer(authorizer)
    return con, ddl


def authorizer(action, arg1, arg2, db, trigger):
    if action in (sqlite3.SQLITE_SELECT, sqlite3.SQLITE_RECURSIVE):
        return sqlite3.SQLITE_OK
    if action == sqlite3.SQLITE_FUNCTION and arg2 != "load_extension":
        return sqlite3.SQLITE_OK
    if action == sqlite3.SQLITE_READ and arg1 in ALLOWED_TABLES:
        return sqlite3.SQLITE_OK
    return sqlite3.SQLITE_DENY


def validate(sql: str) -> str | None:
    """None si la consulta es de solo lectura sobre las tablas permitidas; si no, el motivo."""
    try:
        SCHEMA.execute("EXPLAIN " + sql)
    except sqlite3.ProgrammingError:
        return "una sola sentencia por solicitud"
    except sqlite3.DatabaseError as exc:
        if "prohibited" in str(exc):  # "access to messages.content is prohibited"
            return "tabla no permitida: " + str(exc).split("access to ")[1].split(".")[0]
        if "not authorized" in str(exc):
            return "solo se permite leer " + ", ".join(sorted(ALLOWED_TABLES))
        return str(exc)
    return None


# ---------- la herramienta ----------

def d1_query(sql: str) -> str:
    motivo = validate(sql)                            # VALIDACIÓN
    if motivo:
        stage("RECHAZADA", motivo)
        return f"rechazada por la aplicación: {motivo}"
    stage("VALIDACIÓN", "ok · solo lectura")
    try:
        rows = wrangler(sql, show=True)               # EJECUCIÓN
    except RuntimeError as exc:
        return f"error ejecutando SQL: {exc}"
    return render(rows)                               # OBSERVACIÓN


def render(rows: list[dict], limit: int = 40) -> str:
    if not rows:
        return "(sin filas)"
    cols = list(rows[0])
    lines = [" | ".join(cols)]
    for row in rows[:limit]:
        lines.append(" | ".join("‹oculto›" if c in HIDDEN_COLUMNS else str(row[c]) for c in cols))
    if len(rows) > limit:
        lines.append(f"... ({len(rows) - limit} filas más)")
    return "\n".join(lines)


TOOLS = [{
    "name": "d1_query",
    "description": "Ejecuta una sentencia SQL (SQLite) en la base D1 de encuestas de h1sort.com usando el CLI de wrangler y devuelve las filas.",
    "input_schema": {
        "type": "object",
        "properties": {"sql": {"type": "string", "description": "Una sola sentencia SQL."}},
        "required": ["sql"],
        "additionalProperties": False,
    },
}]


def system_prompt(ddl: dict[str, str]) -> str:
    tables = "\n\n".join(ddl[t] for t in sorted(ALLOWED_TABLES))
    return (
        "Eres un agente de datos que responde preguntas sobre la encuesta de la charla "
        f"«AI en la banca» (grupo con poll_groups.code = '{GROUP_CODE}') usando la herramienta d1_query.\n"
        "Cada voter_hash es un navegador, no una persona; nunca lo muestres. "
        "Una respuesta faltante no es un «No». No inventes números.\n"
        "Responde en español, breve, con una tabla compacta con numeradores y denominadores.\n\n"
        f"Tablas de la encuesta:\n{tables}"
    )


def ask(client: anthropic.Anthropic, messages: list, system: str) -> None:
    for _ in range(12):
        response = client.beta.messages.create(
            model=MODEL,
            max_tokens=16000,
            system=system,
            tools=TOOLS,
            messages=messages,
            output_config={"effort": EFFORT},
            betas=["server-side-fallback-2026-06-01"],
            fallbacks=[{"model": "claude-opus-4-8"}],
        )
        messages.append({"role": "assistant", "content": response.content})
        for block in response.content:
            if block.type == "text" and block.text.strip():
                stage("MODELO", block.text.strip())
        if response.stop_reason == "refusal":
            stage("MODELO", "(el modelo declinó responder)")
            return
        calls = [b for b in response.content if b.type == "tool_use"]
        if not calls:
            return
        results = []
        for call in calls:
            stage("SOLICITUD", f"{call.name}\n{DIM}{call.input.get('sql', '').strip()}{RESET}")
            output = d1_query(call.input.get("sql", ""))
            stage("OBSERVACIÓN", "\n" + "\n".join(output.splitlines()[:12]))
            results.append({"type": "tool_result", "tool_use_id": call.id, "content": output})
        messages.append({"role": "user", "content": results})
    stage("MODELO", "(se acabaron los turnos del loop)")


def load_api_key() -> None:
    """ANTHROPIC_API_KEY del entorno o de ../h1sort-website/.dev.vars. Nunca se imprime."""
    if os.environ.get("ANTHROPIC_API_KEY"):
        return
    dev_vars = SITE_REPO / ".dev.vars"
    if dev_vars.is_file():
        for line in dev_vars.read_text().splitlines():
            if line.strip().startswith("ANTHROPIC_API_KEY="):
                os.environ["ANTHROPIC_API_KEY"] = line.split("=", 1)[1].strip().strip("'\"")
                return


def main() -> None:
    global SCHEMA
    print(f"{DIM}cargando esquema de {DATABASE} vía wrangler…{RESET}", flush=True)
    SCHEMA, ddl = load_schema()
    load_api_key()
    client = anthropic.Anthropic()
    system = system_prompt(ddl)
    messages: list = []
    print(f"{DIM}modelo {MODEL} · effort {EFFORT} · /sql <consulta> la escribes tú · Ctrl-D para salir{RESET}\n")
    while True:
        try:
            text = input(f"{BOLD}tú › {RESET}").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if not text:
            continue
        if text.startswith("/sql "):
            sql = text[5:]
            stage("SOLICITUD", f"escrita por el orador\n{DIM}{sql}{RESET}")
            stage("OBSERVACIÓN", "\n" + d1_query(sql))
            continue
        messages.append({"role": "user", "content": text})
        ask(client, messages, system)
        print()


if __name__ == "__main__":
    main()
