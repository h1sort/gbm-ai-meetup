#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["langchain-anthropic>=0.3.0", "langchain-core>=0.3.0", "duckdb>=1.0.0"]
# ///
"""El loop de la diapositiva 12, en código:
GOAL -> MODEL -> TOOL REQUEST -> HARNESS EXECUTES -> OBSERVATION (y repite).

  demo/run.sh                       # en vivo: se pausa justo antes de ejecutar la solicitud
  uv run demo/agent.py "pregunta"   # corrida completa, sin pausa
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import tools  # noqa: E402  (duckdb_query y extract_text viven ahí)

from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from langchain_core.tools import tool

tools.load_anthropic_key()

# El mismo modelo con el que se ensayó la clase; MODEL_ID=claude-opus-5-5 para más profundidad.
MODEL_ID = os.environ.get("MODEL_ID", "claude-sonnet-5")


@tool
def duckdb_query(sql: str) -> str:
    """SQL de solo lectura sobre los viajes de taxi NYC (vista `trips`)."""
    return tools.duckdb_query(sql)


SYSTEM = (
    "Eres un agente de datos. Usa duckdb_query para consultar los viajes de taxi. "
    "No inventes números."
)


def run(goal: str) -> str:
    active = {"duckdb_query": duckdb_query}
    llm = ChatAnthropic(model=MODEL_ID, max_tokens=1024).bind_tools(list(active.values()))
    messages = [SystemMessage(SYSTEM), HumanMessage(goal)]
    print(f"GOAL > {goal}")
    for _ in range(6):
        response = llm.invoke(messages)  # MODEL piensa y decide
        messages.append(response)
        if not response.tool_calls:  # no pidió herramientas -> respuesta final
            answer = tools.extract_text(response.content)
            print(f"OBSERVATION FINAL > {answer}")
            return answer
        for call in response.tool_calls:  # TOOL REQUEST
            print(f"TOOL REQUEST > {call['name']}({call['args']})")
            result = active[call["name"]].invoke(call["args"])  # HARNESS EXECUTES
            print(f"OBSERVATION > {str(result)[:200]}")
            messages.append(ToolMessage(content=str(result), tool_call_id=call["id"]))
    return "(se acabaron los turnos del loop)"


if __name__ == "__main__":
    run(sys.argv[1] if len(sys.argv) > 1 else "¿Cuántos viajes hay en el dataset de taxis?")
