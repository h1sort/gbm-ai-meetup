# Canonical story — AI en la banca: el hoy y el mañana

## 1. The arc is already defined

Do not treat the talk as three compressed classes followed by a compressed LangChain meetup. It is one investigation:

**We can build analysis cheaply → our reach has expanded over time → here is how an agent actually executes → different banking consequences demand different controls.**

The audience’s survey is the recurring thread. First they see an analytical answer; later they understand the machinery and the requirements needed to trust and use it.

### Governing thesis

> Producir análisis es cada vez más barato. Lo difícil es conservar su significado y controlar qué hacemos con él.

A related formulation, especially for the close:

> El análisis se abarató. El criterio institucional debe convertirse en infraestructura.

“Cheap” means the reduced friction and marginal cost of producing queries, analytical artifacts, and plausible answers. It does **not** mean zero infrastructure cost, free inference at arbitrary scale, or trivial production engineering.

### Three audience takeaways

1. AI expands what we can build and investigate, not just how quickly we type SQL.
2. The model proposes; the application executes—or refuses.
3. Asking, executing, and judging are different engineering problems because their consequences and delegated authority differ.

### The professional role

Do not reduce the data professional’s future to checking a flood of generated queries. The higher-leverage role is to encode definitions, domain knowledge, permissions, evidence requirements, and lessons from failures into infrastructure that improves every future analysis, agent, and employee.

## 2. Event and scope

The invitation describes a roughly 30-minute talk for professionals and leaders in AI, banking, and finance. It expects agent definitions, use in regulated environments, common implementation problems and emerging solutions, with a look at the Post-AI Data Stack and Jev.

The speaker will also participate in the panel **“Del modelo al mundo real, ¿cómo transformar las finanzas con inteligencia artificial?”**, scheduled in the invitation for 6:30–7:00 p.m. Do not invent a date or a start time for the talk.

Title: **AI en la banca: el hoy y el mañana**.

Suggested, not locked, subtitle: **Del análisis barato al criterio convertido en infraestructura**.

## 3. Timing budget

| Time | Section | Purpose |
| --- | --- | --- |
| 0:00–5:00 | QR, manual count, agent SQL, thesis | Demonstrate cheap analysis with data created in the room |
| 5:00–9:00 | Historical expansion | Explain the constraints each era removed |
| 9:00–15:00 | Agent definition and tool demonstration | Expose proposal, execution, and the runtime boundary |
| 15:00–26:00 | Ask / Execute / Judge, including Jev | Connect meaning, authority, evidence, and controls to banking |
| 26:00–28:00 | Today, tomorrow, closing | Institutional judgment becomes reusable infrastructure |
| 28:00–30:00 | Buffer or questions | Protect the demos and ending |

Do not narrate every diagram arrow, read every code line, or tour vendors. Historical years are approximate adoption phases, not invention dates.

## 4. Opening — counting is easy; answering takes work

### What happens

1. Show a QR for the original six-question Class 1 survey.
2. Let the audience answer while briefly setting the context.
3. Switch to Cloudflare and manually execute a simple count scoped to this event/group.
4. Ask the agent a question that requires joining answers and calculating role-specific percentages.
5. Show authentic generated SQL and executed results.
6. State the thesis, without pretending speed proved validity.

Preferred agent question:

> Por cada tipo de trabajo, ¿qué porcentaje usó IA para datos en los últimos siete días y qué porcentaje ha utilizado un agente conectado a una base de datos?

The analysis combines Q5, Q1, and Q2. DEMO.md specifies the correct units, denominators, scope, and cutoff.

### Suggested speaker beats

> Vamos a trabajar con datos que estamos creando aquí, no con un dataset preparado para que la demostración salga bien.

After the manual count:

> Ya contamos respuestas. Pero todavía no sabemos quién está en la sala ni cómo está usando IA.

After the agent result:

> Yo escribí un conteo. El agente construyó y ejecutó el análisis que respondía una pregunta de negocio. Eso es lo que se abarató.

Then introduce—not exhaust—the trust problem:

> Todavía falta saber si relacionó correctamente las respuestas y qué denominador utilizó. Una respuesta rápida no resuelve esas preguntas por sí sola.

The live demonstration is not a dashboard build, report-generation exercise, or ETL tutorial. The website already displays poll results; that is not the artifact being generated live.

### Transition to history

> Hoy podemos formular esa pregunta y obtener el análisis casi inmediatamente. No siempre pudimos hacerlo. Cada generación del stack eliminó una limitación distinta.

## 5. History — expanding reach, not replacing databases

This section adapts Ian Macomber’s “The Shape and Feel of the Post-AI Data Stack.” Its strongest organizing idea is expanded analytical/operational reach, not a vendor timeline.

Use one fictional banking question across the eras:

> ¿En qué punto perdemos a los clientes entre iniciar una solicitud y fondear una cuenta?

Treat this as investigating a journey and its observed patterns—not automatically proving why customers behave as they do.

### ~2013: the question fit the business, not the stack

Projected thesis:

> La pregunta cabía en el negocio, no en el stack.

Suggested delivery:

> Pensemos en una pregunta razonable de negocio. Queremos entender qué ocurre entre iniciar una solicitud y fondear una cuenta.
>
> Las solicitudes están en un sistema. Los movimientos, en otro. Los eventos de la aplicación quizá no están disponibles para análisis. Cruzar esa información requiere extracciones, coordinación y recursos que pueden competir con la operación.
>
> No nos faltaban preguntas. Nos faltaba una forma práctica de reunir la evidencia para responderlas.
>
> La infraestructura decidía qué preguntas podíamos permitirnos hacer.

The three constraints:

- **Fragmentación:** relevant evidence lives in separate systems.
- **Forma:** semi-structured events and other data are difficult to access through the available analytical tooling.
- **Escala y recursos:** large investigations are costly or contend with other workloads.

Do not make the DBA an antagonist. Do not claim distributed databases, warehouses, or big-data systems did not exist. “Impractical or costly in this representative environment” is stronger and more accurate than “impossible everywhere in 2013.”

### ~2016: observe more of the business

Projected thesis:

> Podemos observar más del negocio.

Cloud analytical infrastructure makes it practical to combine more sources, analyze larger histories, and better isolate analytical resources from other workloads.

> Ahora podemos reconstruir una parte mucho más completa del recorrido: solicitud, actividad y primer fondeo.

This is a change in scope, not simply a database relocation.

Plant the semantic problem:

> Tener los datos juntos no significa que ya acordamos qué significan.

Avoid “infinite compute/storage,” automatic single truth, or claims that every cloud warehouse has identical internals. Do not portray Snowflake as inventing cloud warehouses with all other vendors following it.

### ~2020: from observing to operating

Projected thesis:

> De observar a operar.

Managed ingestion reduces the friction of adding a source. Transformations make analytical data reusable. Reverse ETL carries modeled results back into operational systems.

> El análisis ya no termina necesariamente en una presentación. Una segmentación puede actualizar un CRM o alimentar un proceso operativo.

A memorable adaptation of Macomber:

> ETL amplió lo que podíamos ver. Reverse ETL amplió lo que podíamos hacer.

This is essential: it bridges the history to Execute. Data professionals could create operational consequences before agents arrived.

### ~2026: answers become abundant; judgment remains scarce

Projected thesis:

> La respuesta abunda. El criterio sigue siendo escaso.

Return to the live opening:

> Hace unos minutos formulamos una pregunta, y un agente construyó el análisis. Cada persona de una organización puede hacer lo mismo, desde su propia interfaz.
>
> Ahora el problema no es únicamente producir respuestas. Es conseguir que esas respuestas conserven las definiciones y el conocimiento del negocio.

The new professional leverage:

> Convertir el criterio de los expertos en infraestructura que otros puedan utilizar sin tener al experto presente.

Historical spine:

**Alcance limitado → visión más completa → capacidad de operar → criterio reutilizable.**

The Post-AI Data Stack does not abolish warehouses, ETL, modeling, or governance. It makes expert context, agent-operable capabilities, readable evidence, and feedback/evaluation infrastructure more valuable.

### Transition to agents

> Hasta ahora vimos lo que el agente produjo. ¿Qué tuvimos que construir para que pudiera hacerlo?

## 6. Agents — expose the execution boundary

Use Simon Willison’s exact operational definition:

> An LLM agent runs tools in a loop to achieve a goal.

Explain objective, model, tool request, runtime execution, observation, another turn, and stopping condition. A fixed retrieval pipeline or a single model call is not automatically an agent under this definition.

The critical pause is between request and execution:

> Que el modelo solicite una acción no significa que esa acción ya ocurrió.

> El modelo propone la siguiente acción. La aplicación decide si puede ejecutarla.

### What the live tool demonstration proves

The opening shows capability; this demonstration shows mechanism. Show an authentic request, the actual handler/function, application execution or refusal, and the returned observation. A paused write can illustrate that a request exists before any artifact is created.

Do not ask the model to reconstruct its own raw conversation and present that as a faithful trace. Instrument or inspect the actual runtime.

### Two different uses of AI

- AI helps write the program.
- AI participates in the running program.

> Que un agente haya escrito una función no convierte esa función en un modelo de lenguaje. Cuando se ejecuta, sigue siendo software, con sus pruebas, permisos y límites.

### Determinism: be precise

The model-generated plan, selected tool, arguments, SQL/code, and interpretation can vary and can be wrong. Application code can explicitly enforce authorization, validation, dispatch, budgets, and process preconditions.

A tool may depend on changing data, an external API, randomness, or another model. Do not equate “implemented in code” with identical results forever or proven correctness. A stable computation over the same snapshot is different from a changing live system.

> La selección puede ser probabilística. Las condiciones para autorizar y ejecutar deben estar explícitas en el sistema.

> Una propuesta puede ser probabilística. Un permiso no debería depender de que el modelo obedezca.

Prompts guide behavior. Applications and authoritative downstream services enforce permissions and invariants.

### Transition to banking

> El mismo modelo puede responder una pregunta, proponer una acción o contribuir a un juicio. La inteligencia puede ser la misma. Las consecuencias no.

## 7. Banking — Ask / Execute / Judge

These are authority archetypes, not maturity levels, mutually exclusive product categories, or mandatory sequential steps. A system may combine all three. Classify by its highest-consequence delegated freedom, not its safest frequent operation. Autonomy duration is not the same as operational authority.

### Ask — trust the answer

Primary analytical illustration:

> ¿Cuántos clientes activos tenemos?

Different definitions, periods, exclusions, or grains can produce different answers from SQL that executes successfully.

Teach shared definitions, authorized evidence, data cutoff, provenance, and evaluations against validated references.

> El warehouse reúne los datos. La capa semántica conserva su significado.

A policy-investigation variant can emphasize authorized retrieval before context, current versions, citations, bounded investigation, and abstention. Do not fully teach two separate architectures in the same short section.

Post-AI infrastructure should be visible here:

- Agent-readable artifacts: meaning and provenance, not screenshots alone.
- Agent-operable tools: narrowly usable capabilities rather than UI-only workflows.
- Shared, interface-agnostic context: definitions survive changing models and interfaces.
- Testable consistency and retained corrections: a discovered error becomes a regression case and shared fix.

Evaluation question:

> Con la misma definición, permisos y fecha de corte, ¿cambia la respuesta al cambiar de interfaz o modelo?

Agreement is not proof of truth. Compare against a validated reference and required evidence. Do not adopt Macomber’s “assume models are never wrong” literally; context ambiguity is one failure mode, not the only one.

### Execute — trust the action

Representative request:

> Perdí mi tarjeta. ¿Puedes bloquearla?

The model interprets and proposes a narrow operation. The application and downstream service establish trusted identity, entitlement, valid target/parameters, and approval proportional to risk. Execution returns a receipt/outcome.

Characteristic failure:

> La operación correcta sobre la tarjeta equivocada, o dos ejecuciones porque la primera terminó con un timeout.

Teach the execution contract: identity, authorization, exact intended effect, idempotency, audit, and reconciliation after an uncertain outcome. Approval does not grant authority the user lacks. Not every read or reversible operation requires human approval.

> Una respuesta equivocada y una acción equivocada son problemas distintos.

### Judge — defend the assessment

Define Judge as applying bounded judgment to evidence and producing an assessment a governed process can use—not an autonomous final verdict. It is also not necessarily the same thing as an LLM-as-judge evaluation grader.

Working illustration: synthetic fraud-alert investigation. Existing quantitative risk scores may be part of the evidence; do not imply the LLM replaces validated fraud or credit models.

The process:

1. Deterministic scope/triage establishes permissions and required evidence.
2. Collect authorized evidence with provenance.
3. Require completeness, or take an explicit safe-failure route.
4. A bounded local agent investigates the case and recommends.
5. Policy owns routing and review requirements.
6. Persist evidence, assessment, route, and reviewer decisions as appropriate.

The pivotal contrast:

> Un prompt puede pedir una condición. Un workflow puede convertirla en un requisito.

> Puedes decidir qué evidencia adicional inspeccionar. No puedes decidir que la evidencia obligatoria dejó de ser obligatoria.

> Agencia local. Invariantes globales.

A graph is not inherently an agent or universally safe. The agent is the bounded model/tool loop within the process. Explicit workflow topology earns its complexity when mandatory order, persistence, recovery, or review are requirements.

A checkpoint preserves execution state; it does not by itself prevent duplicate external effects. Routing thresholds require held-out/domain evaluation, not a model’s self-reported feeling of confidence.

## 8. Jev — bounded judgments with a software-oriented interface

Place Jev inside Judge, not as a disconnected product announcement or a third live dependency.

> No siempre necesitamos que la IA escriba una respuesta. A veces necesitamos que evalúe una condición dentro de un programa.

Contrast flexible text/tool proposals with:

**State + predefined typed questions → typed values and probabilities → application policy.**

Jev’s official docs describe Choice, Score, and Noul primitives. Its specialized interface can reduce output-shape problems and improve the economics of bounded tasks. Do not promise task correctness or transfer vendor calibration claims to a banking dataset without evaluating them.

The second poll supplies a low-stakes illustration: free-text job titles become predefined categories, then ordinary SQL aggregates the resulting column. This does not require surveying the room again.

Three boundaries:

- A valid label is not necessarily the correct label.
- A Jev API call is not, by itself, an agent.
- Typed/probabilistic output does not make the judgment deterministic or replace policy.

> Restringir las respuestas posibles elimina una clase de errores. No elimina el error de juicio.

Avoid unverified latency/cost multipliers, “the first classifier ever,” “zero semantic errors,” and “production-ready for this bank.” System One is TypeSafe’s category terminology, not a reason to rewrite the history of classification.

## 9. Today, tomorrow, and the close

**Today:** assisted analysis, bounded evidence investigation, and narrow governed capabilities.

**Tomorrow:** more institutional definitions, judgments, and corrections become reusable infrastructure. Model interfaces and orchestration can change while consequential execution remains governed.

Suggested close:

> El futuro de la IA en la banca no es solamente un modelo más inteligente. Es una institución capaz de convertir su criterio en sistemas: qué significa una métrica, qué evidencia exige un juicio y quién puede autorizar una acción.
>
> El análisis se abarató. Nuestro trabajo es que su significado y sus consecuencias no se pierdan.

Do not add a new topic after this ending.

Panel bridge, if useful later:

> ¿Qué debe construir una institución alrededor de un modelo para que sus capacidades se conviertan en un producto financiero confiable?

## 10. Deliberate cuts and emergency pacing

Do not include transformer internals, model-training history, installation instructions, vendor tours, live warehouse setup, the OLTP/OLAP benchmark, or live ETL construction. These belonged to the classes, not this talk.

The taxi-tip example is optional backup context: valid execution can still yield an unsupported interpretation when cash tips are unobserved. Prefer the active-customer banking example in the main deck. If the taxi example is used, verify TLC’s recording definition and avoid implying tips alone measure service quality or that every zero means missing data.

If behind schedule:

- Compress historical narration, but preserve fragmentation and the 2020 operational transition.
- Reduce architecture inventories; retain the model/runtime boundary and mandatory-evidence join.
- Keep Jev brief rather than introducing a live API call.
- Preserve the final synthesis and closing line.

The talk should be optimistic about expanded capability. Controls enable useful delegation; they are not the entire product story or a lecture about why agents should never act.
