# Slide production brief

## Governing constraints

Read [STORY.md](STORY.md) first. This outline implements the established argument; it is not a new narrative proposal.

Target: **18 main slides, 28 minutes of prepared delivery, 2 minutes of buffer**. Slide count is a working default. Split only if necessary for legibility and preserve the timing; do not quietly grow this into a 40-slide tutorial.

For every slide, provide concise Spanish projected copy, a distinct visual claim, and presenter notes with purpose, timing, transition, and any demo/source caveat. Notes must not appear on the projected slide by default.

The website screenshots were supplied for context, not as required slide assets. Do not use screenshot counts as event findings or imitate an admin UI instead of designing the deck.

## Timing and slide map

| Slides | Section | Budget | Clock |
| --- | --- | --- | --- |
| 1–4 | Live opening and thesis | 5:00 | 0:00–5:00 |
| 5–8 | Four historical phases | 4:00 | 5:00–9:00 |
| 9–12 | Definition, runtime boundary, live tool demo | 6:00 | 9:00–15:00 |
| 13–17 | Ask / Execute / Judge and Jev | 11:00 | 15:00–26:00 |
| 18 | Synthesis and closing | 2:00 | 26:00–28:00 |
| — | Buffer or questions | 2:00 | 28:00–30:00 |

## 01 — AI en la banca: el hoy y el mañana

**Budget:** 0:20.

**Claim:** This is a talk about the changing economics of analysis and the institutional systems needed to use it.

**Projected copy:** Title; Carlos Aro / Charlie; GBM AI Experience / AI & Finance event context. Suggested subtitle: “Del análisis barato al criterio convertido en infraestructura.” Keep the subtitle subordinate; it is not locked.

**Visual:** A cinematic light-theme hero, generous typography, and an original abstraction of data passing through a meaningful boundary. Not a fantasy-creature remake or a generic stock-image banking skyline.

**Notes:** Introduce the public teaching framing briefly. Do not start with biography, a long agenda, or vendor logos.

## 02 — Los datos empiezan aquí

**Budget:** 2:00.

**Claim:** The room creates the dataset.

**Projected copy:** Large scannable QR, readable short public URL, “6 preguntas · aproximadamente 2 minutos.” Suggested supporting line: “Primero, conozcamos la sala.”

**Visual:** QR has real visual priority and a clean quiet zone. Pair with understated diagrammatic marks, not moving interference behind the code.

**Interaction:** Link opens the configured survey. No voting, admin login, or API credentials embedded in the presentation.

**Notes:** Default public link is the existing Class 1 survey, not an already-created GBM group. Preparation note must explicitly say to configure a fresh identical group if the speaker authorizes it. Do not read all six questions aloud. See DEMO.md for exact wording.

## 03 — Del conteo a una pregunta

**Budget:** 2:10.

**Claim:** The agent turns a business question into substantial SQL, beyond a simple manual count.

**Projected copy:** Two beats: “Yo: COUNT(*)” and “Agente: una pregunta de negocio.” Show the short question prominently:

> Por tipo de trabajo: ¿qué porcentaje usó IA recientemente y qué porcentaje ha usado un agente con una base de datos?

The full staged prompt lives in notes/copy support, not a dense projected block.

**Visual:** Simple count contrasted with linked role/usage/experience observations. This is a stage cue, not a fabricated result table.

**Demo:** Speaker switches to Cloudflare for the count, then to a prepared agent environment for genuine query generation and execution. The actual output stays in that environment; the deck need not connect directly to the database.

**Notes:** Count answer rows, not verified people. Use the event/group scope and one fixed UTC cutoff. Resolve relationships and denominators correctly. Return a compact aggregate table and actual SQL. Do not generate a dashboard or report.

## 04 — Producir análisis se abarató

**Budget:** 0:30.

**Claim:** Cheap production is not the same as validated meaning.

**Projected copy:** “Producir análisis se abarató.” Secondary line: “Acordar qué significa sigue requiriendo criterio.”

**Visual:** Large, restrained editorial statement with a subtle abundance motif. This should feel like the argument’s first landing, not another bullet slide.

**Notes:** “Yo escribí un conteo. El agente construyó y ejecutó el análisis.” Introduce join/denominator questions without immediately performing a full audit. Transition: each historical era removed a different constraint.

## 05 — ~2013: la pregunta cabía en el negocio, no en el stack

**Budget:** 1:00.

**Claim:** Fragmentation, data shape, and scale/resource contention constrain reasonable investigations.

**Projected copy:** Approximate year and headline. Three short labels: “Fragmentación · Forma · Escala.” The running question concerns the journey from application to first account funding.

**Visual:** A representative map with separate application, movement/payment, and app-event sources. Draw the reachable analytical boundary narrowly, with relevant evidence outside or costly to connect. Show isolation rather than a DBA blocking the path.

**Notes:** Narration is in STORY.md. Do not claim all analysis ran on one server everywhere, or that warehouses/distributed systems did not exist.

## 06 — ~2016: podemos observar más del negocio

**Budget:** 1:00.

**Claim:** Cloud analytical infrastructure expands accessible evidence and practical analytical scale.

**Projected copy:** “Podemos observar más del negocio.” Optional short labels: “Más fuentes · Más escala · Cargas mejor aisladas.”

**Visual:** Evolve the previous map with a shared analytical plane, more reachable sources, and an isolated analytical workload. Keep shapes/positions consistent so the audience perceives the expansion.

**Notes:** This is more than relocating a database. Say: “Tener los datos juntos no significa que ya acordamos qué significan.” Avoid infinite-resource claims and vendor invention chronology.

## 07 — ~2020: de observar a operar

**Budget:** 1:00.

**Claim:** Managed integration expands what data teams see; Reverse ETL expands what they do.

**Projected copy:** “ETL: lo que podemos ver.” / “Reverse ETL: lo que podemos hacer.”

**Visual:** Continue the same map, adding managed ingestion and a clear return path into a representative CRM/operational process. The outbound operational path must be unmistakable.

**Notes:** A segment can feed an operational process rather than end in a slide. This is the bridge to Execute. Do not call this merely “filters that get us to insights faster.”

## 08 — ~2026: la respuesta abunda; el criterio sigue siendo escaso

**Budget:** 1:00.

**Claim:** Many interfaces can produce analyses; shared judgment must survive them.

**Projected copy:** Headline and one short supporting phrase: “Criterio experto, convertido en infraestructura.”

**Visual:** Evolve the map with multiple human/agent interfaces, a harness, shared context, and a feedback loop. Show context as definitions/provenance, not just a giant database. Use selected labels, not an entire vendor ecosystem.

**Notes:** Cite Macomber unobtrusively. Warehouses, ETL, and modeling remain valuable. Shared context and correction loops make each future question start smarter. Transition into what makes the opening system an agent.

## 09 — Una definición útil de agente

**Budget:** 1:00.

**Claim:** Tools, iteration, and an objective make the operational definition concrete.

**Projected copy:** Exact quotation:

> An LLM agent runs tools in a loop to achieve a goal.

Attribution: Simon Willison. Small Spanish unpacking: “Objetivo · Herramientas · Bucle · Condición de salida.”

**Visual:** Quote-led composition with a restrained loop motif. Do not place a dense architecture behind the definition.

**Notes:** A fixed retrieval pipeline or single model call is not automatically an agent. No model-training or transformer detour.

## 10 — El modelo propone. La aplicación ejecuta.

**Budget:** 1:30.

**Claim:** Proposal and execution are separate, with a trusted runtime boundary.

**Projected copy:** Headline; diagram labels for model, tool request, application/runtime, observation, and stop/loop.

**Visual:** Model and application are distinct regions. Place permission/validation at the application boundary. Animate the request crossing only after the execution gate, with the observation returning. Include a clear refusal path.

**Notes:** Do not say the model itself runs database code or establishes identity. Scope, trusted identity, budgets, timeouts, and authorization belong around the loop. See DEMO.md for determinism nuance.

## 11 — Una solicitud todavía no es una acción

**Budget:** 2:30.

**Claim:** The live runtime turns—or refuses to turn—a proposed call into a real effect.

**Projected copy:** “Solicitud → Validación → Ejecución → Observación.” A discrete “Demo en vivo” cue.

**Visual:** Clean split between actual request and implementation, with a visibly pending execution boundary. Do not show invented logs as if captured from the session.

**Demo:** Expose the real request, actual handler, and real result. Reuse the opening environment/trace if practical. A small dedicated file-writing demonstration is an available staging option; no generated report/dashboard and no framework setup on stage.

**Notes:** The exact harness and operation are not locked. A paused request can show that the file/effect does not exist yet. Do not request a model-authored reconstruction of the raw conversation. Keep one authentic narrow tool call ready to make the demonstration genuinely live.

## 12 — Dos lugares distintos para la IA

**Budget:** 1:00.

**Claim:** AI-authored software and runtime model judgments are different things.

**Projected copy:** “IA que escribe el programa” versus “IA dentro del programa.” Landing line: “Una propuesta puede ser probabilística. Los permisos deben ser explícitos.”

**Visual:** Two clean lanes: generated artifact enters normal software validation/execution; runtime model requests pass through governed tools. Ordinary code should not be drawn as an LLM merely because an agent wrote it.

**Notes:** Tools may call external services or models. Do not equate all code with pure deterministic output or semantic correctness. Transition to identical model capability with different consequences.

## 13 — El mismo modelo. Distintas consecuencias.

**Budget:** 1:00.

**Claim:** Architecture follows delegated authority and consequence.

**Projected copy:** **Ask / Execute / Judge**. Spanish labels: “Consultar · Ejecutar · Juzgar.” Under each, one failure: “Respuesta equivocada · Acción equivocada · Juicio sin evidencia.”

**Visual:** A coherent three-part authority landscape. Avoid a maturity staircase suggesting Judge is the inevitable best endpoint.

**Notes:** These patterns can coexist. Judge means bounded assessment, not an unreviewed final verdict. Cases are fictional teaching composites.

## 14 — Ask: ¿cuántos clientes activos tenemos?

**Budget:** 2:30.

**Claim:** Successful SQL execution does not settle the meaning of a metric.

**Projected copy:** The question and a small set of requirements: “Definición · Permisos · Corte · Evidencia.” Landing line: “El warehouse reúne los datos. La capa semántica conserva su significado.”

**Visual:** An approved metric definition and date/scope feed a bounded analytical investigator through an authorized tool boundary. Include a small correction/evaluation return path. Contrast differing definitions without inventing measured banking totals.

**Notes:** Answer accuracy, evidence support, current definitions, authorization before context, and abstention. The policy-retrieval example is an alternative, not a second full architecture. Distinguish agreement from validated truth; evaluate against a reference.

## 15 — Execute: una petición cambia el mundo

**Budget:** 2:30.

**Claim:** A proposed operation must become a governed, recoverable execution.

**Projected copy:** “Perdí mi tarjeta. ¿Puedes bloquearla?” Short control labels: “Identidad · Autorización · Efecto exacto · Recibo.”

**Visual:** User request → bounded proposal → policy/validation → approval where required → execution → authoritative system/receipt. Include a concise audit/reconciliation rail, without building a giant service diagram.

**Notes:** Wrong customer and duplicate execution after timeout are characteristic risks. Explain idempotency and reconcile-before-retry in plain language. Approval is not authorization; not every operation needs human review. No real banking action is executed.

## 16 — Judge: agencia local, invariantes globales

**Budget:** 3:00.

**Claim:** Model discretion belongs inside a process that enforces required evidence and routing.

**Projected copy:** “Construir un caso, no dictar un veredicto.” Emphasize: “La evidencia obligatoria no es opcional.”

**Visual:** Synthetic fraud alert → scope → authorized evidence branches → mandatory completeness join → bounded assessment-agent loop → policy-controlled recommendation/review. Add a durable-state/provenance rail. Make the agent loop inside the workflow visible.

**Notes:** This includes the may-versus-must contrast; do not add another timed slide merely to repeat it. “Un prompt puede pedir una condición. Un workflow puede convertirla en un requisito.” Required evidence cannot be waived because the model feels confident. Policy routing, held-out calibration, and review preserve accountability.

## 17 — Jev: un juicio que el software puede consumir

**Budget:** 2:00.

**Claim:** Typed bounded model outputs fit ordinary software, without proving semantic correctness.

**Projected copy:** “Estado + preguntas tipadas → valores + probabilidades → código.” Landing line: “Una categoría válida no necesariamente es correcta.”

**Visual:** A small illustrative classification of a synthetic job-title string into predefined categories; then normal aggregation/routing. Label it illustrative, not a live or measured Jev result. Keep the surrounding application boundary visible.

**Notes:** The second survey provides context for text-to-column analysis. Jev is a component, not automatically an agent. Domain evaluation is required before probabilities drive a banking route. No live API dependency, unverifiable speed/cost multipliers, or blanket correctness guarantee.

## 18 — El criterio también se construye

**Budget:** 2:00.

**Claim:** The institutional opportunity is reusable expertise, not merely a smarter chat interface.

**Projected copy:** Three concise closing anchors: “Significado compartido · Ejecución gobernada · Juicio verificable.” Final line: “Que el significado y las consecuencias no se pierdan.” Contact: `h1sort.com`.

**Visual:** Return to the cover’s boundary/data motif, now visibly connected and governed. The ending should feel like a resolved visual story, not a checklist page.

**Notes:** Use the closing paragraph in STORY.md. Today: assisted analysis and narrow bounded capabilities. Tomorrow: reusable definitions, evidence rules, and corrections across interfaces. Stop cleanly; no new topic after the final line.

## Supporting material outside the timed deck

Keep references and rehearsal notes accessible without making them projected slides by default. Good options: a sources dialog, a notes mode, or clearly separated appendix content.

Optional backup material:

- Exact survey questions and full staged prompt.
- Query denominator/cutoff explanation.
- Taxi-tip semantic trap, if the speaker specifically wants it.
- Full authority/control comparison.
- Normal code versus agent loop versus explicit workflow decision guide.

Do not let appendices alter the main folio count or accidentally enter normal next-slide navigation unless clearly intended.

## Density and editorial acceptance

- One main claim per slide; maximum approximately 4–6 short bullets or two short paragraphs.
- A code panel should be about 8–10 legible lines, not a terminal dump.
- QR, definition, diagrams, and final takeaway deserve breathing room.
- Supporting notes contain the nuance; projected copy remains understandable at a glance.
- All historical years use approximation markers or a clear “fases aproximadas” qualification.
- Demonstration cues must not imply an illustrative image is the current live result.
- The Post-AI Data Stack and Jev are substantively integrated, not name-dropped at the end.
