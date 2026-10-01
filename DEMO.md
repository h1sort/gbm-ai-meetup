# Demo and survey handoff

## 1. Explicit opening decision

The speaker rejected live dashboard generation and approved this sequence:

**Original QR survey → manual COUNT(*) in Cloudflare → one live agent question requiring more elaborate SQL → thesis.**

Do not replace the existing questions with a shortened survey. Do not generate a report, dashboard, or ETL on stage.

The deck is a presentation, not a requirement to rebuild the poll application or embed an authenticated database client.

## 2. Existing public links

- [Class 1: AI 4 Data](https://h1sort.com/p/JFQES4AF97) — six choice questions; use this question set for the opening.
- [Class 2: AI 4 Data · Clase 2](https://h1sort.com/p/8P56ZUVE9Q) — confidence plus two free-text questions; context for later classification/Jev.
- [Management page](https://h1sort.com/polls/) — requires authentication. No password was supplied and no administrative changes were made.

The public links were inspected without submitting votes. They resolve to the site’s `/polls/?group=...` interface. Read-only browser requests observed these public definition endpoints:

- `https://h1sort.com/api/polls/public/groups/JFQES4AF97`
- `https://h1sort.com/api/polls/public/groups/8P56ZUVE9Q`

These return poll definitions/options, not a substitute for the participant-level answer relationships needed for the SQL cross-tab.

### Fresh GBM group is not yet prepared

The existing Class 1 group opened on September 22, 2026; Class 2 on September 25, 2026. They contain historical class context. A fresh GBM group with **identical questions** is recommended to avoid mixing populations and returning browsers being restricted to one vote per existing poll. This recommendation was not followed by an authorized creation request.

For the first deck iteration, an existing public URL may be used with an explicit presenter preparation note. Do not invent a GBM group code, pretend it exists, clear old votes, modify existing questions, or open/close voting without the speaker’s authorization.

## 3. Exact Class 1 questions and options

### Q1

**¿Usaste IA para una tarea de datos en los últimos 7 días?**

- Sí
- No

### Q2

**¿Has usado un agente conectado a una base de datos?**

- Sí
- No

### Q3

**¿Qué tanta confianza tienes revisando SQL generado por IA? (1 = ninguna confianza; 5 = mucha confianza)**

Options: `1`, `2`, `3`, `4`, `5`.

### Q4

**¿Qué tanta confianza tienes en un análisis generado por IA? (1 = ninguna confianza; 5 = mucha confianza)**

Options: `1`, `2`, `3`, `4`, `5`.

### Q5

**¿Cuál describe mejor tu trabajo principal?**

- Analítica / BI
- Ingeniería de datos
- Ciencia de datos / ML
- Desarrollo de software
- Liderazgo / gestión
- Estudiante / otro

### Q6

**Cuando una IA te entrega SQL, ¿cómo lo validas normalmente? Selecciona la comprobación más rigurosa que haces habitualmente.**

- No uso IA para generar SQL
- No lo valido
- Reviso el código
- Lo ejecuto y compruebo que el resultado parece razonable
- Lo comparo con un resultado conocido o pruebas

The first five were in the screenshots; Q6 was independently verified from the public group definition. Keep all six.

## 4. Exact Class 2 questions

The public voter flow currently presents confidence first, followed by the two text questions. The management screenshot displayed the text questions before confidence. Identify meaning from the question metadata, not screenshot order.

1. **¿Qué tanta confianza tienes en un análisis generado por IA? (1 = ninguna confianza; 5 = mucha confianza)** — options 1–5.
2. **¿Cuál es tu puesto actual, tal como aparecería en LinkedIn? (sin nombre ni empresa)** — free text, maximum 120 characters.
3. **Una tarea de datos que te gustaría automatizar primero.** — free text, maximum 280 characters.

Do not collect a second survey during the opening. These questions explain how free text can become structured columns in the Jev segment.

## 5. Manual count

The manual count should be easy to recognize as the traditional starting point. It counts **answer rows**, scoped to the relevant group/event, not all website votes and not verified people.

A prepared query can use the event group ID and one fixed UTC cutoff. Example shape, with placeholders that must be resolved from the verified schema:

```sql
SELECT COUNT(*) AS respuestas
FROM poll_votes
WHERE poll_id IN (
  SELECT id FROM polls WHERE group_id = 'EVENT_GROUP_ID'
)
AND created_at <= 'UTC_CUTOFF';
```

Do not project or execute these placeholder literals as a finished query. The point is the count, not live schema discovery or typing a long join.

Source schema expectations are documented in the prior Class 1 prompt and Class 2 data contract. Re-check the actual live schema before rehearsal; this handoff did not query the authenticated D1 database.

## 6. The live agent question

Preferred natural-language question:

> Por cada tipo de trabajo, ¿qué porcentaje usó IA para datos en los últimos siete días y qué porcentaje ha utilizado un agente conectado a una base de datos?

This joins **Q5 role**, **Q1 recent usage**, and **Q2 database-agent experience**.

Return a compact table with role, valid denominators, and percentages. A rigorous version uses:

| Trabajo | n con Q5 | Sí Q1 / n con Q5+Q1 | % Sí Q1 | Sí Q2 / n con Q5+Q2 | % Sí Q2 |
| --- | --- | --- | --- | --- | --- |

The projected live result can be simpler, but the underlying computation must preserve the two different denominators. Do not force a single “Respondientes” denominator if missing answers make it inaccurate.

### Suggested short staged prompt

```text
Con el grupo y el corte UTC acordados, responde:
Por cada tipo de trabajo, ¿qué porcentaje usó IA para datos en los últimos
siete días y qué porcentaje ha utilizado un agente conectado a una base de datos?
Cruza Q5 con Q1 y Q2 usando el identificador interno de navegador.
Usa un denominador de pares válidos para cada porcentaje; no conviertas faltantes en No.
Muestra el corte, SQL ejecutado y una tabla compacta con numeradores y denominadores.
No muestres identificadores ni respuestas individuales. Resume sin inferir causalidad o competencia.
```

Connection, schema inventory, group confirmation, tool permissions, and model selection happen **before** the stage prompt, not during the talk. Query generation and execution remain genuinely live.

### Real prior implementation context

Reference: [Class 1 poll prompts](file:///Users/Haro/Code/ai4data-class/demos/clase-01-poll-prompts.md).

That file documents:

- D1 database name `h1sort-chat`.
- Historical MCP server `cloudflare-bindings` and `d1_database_query` / database-list tools.
- Tables `poll_groups`, `polls`, `poll_options`, and `poll_votes`.
- Expected relationships: `polls.group_id`, `poll_options.poll_id`, `poll_votes.poll_id`, `poll_votes.option_id`.
- Internal pairing field `voter_hash`.
- Timestamp field `poll_votes.created_at` and a fixed UTC cutoff.

These are source-backed expectations, not a guarantee of the next harness’s tool schema. Discover available tools and verify the live schema before using them.

The database is shared with the website and also contains chats. Limit access technically to the required poll data. Do not inspect conversations, messages, authentication tables, or unrelated data. A prompt asking for SELECT-only access does not create read-only authorization.

## 7. Analytical semantics

- One answer row is one response to one question.
- A distinct `voter_hash` identifies an observable browser respondent, not a guaranteed unique human. Keep it internal and never project it.
- Scope all reads to the intended group and one consistent data cutoff.
- Resolve question IDs from metadata. Do not assume array position is stable or hard-code historical IDs into a fresh group.
- Join options to their owning questions, not only by an unconstrained label.
- Verify at most one answer per respondent/question; investigate violations rather than silently multiplying joined rows.
- Each role-specific Q1 percentage uses valid Q5+Q1 pairs; Q2 uses valid Q5+Q2 pairs.
- Missing answers are not No, zero, or evidence of abandonment while the poll is open.
- Zero denominator means undefined, not 0%.
- Preserve role categories with no responses where helpful, and label insufficient sample sizes.
- Q1 is recent usage; Q2 is ever-use experience. They are different behaviors/time windows, not a conversion funnel.
- Confidence is self-reported, not calibrated competence.
- “No uso IA para generar SQL” is not “fails to validate SQL.”
- Do not infer the size or readiness of the whole audience from respondents.
- Do not invent findings if the sample is small or empty.

The opening should not become a statistics lecture. Most of this belongs in rehearsal and notes; it also supplies the later semantic trust discussion.

## 8. Agent/tool demonstration

The required lesson is:

**Model-generated request → trusted application boundary → actual code execution or refusal → observation returned to the model.**

Show real requests and real runtime records. Do not ask the model to write a JSON reconstruction of the conversation and call it an authentic trace.

### Preferred staging strategy

Use one prepared environment for both demos. Inspect the opening’s actual SQL-tool request and implementation, then execute one narrow request live to expose the boundary. This avoids a new provider, installation, or dataset.

A tiny dedicated file-writing demonstration is another acceptable mechanism: show the typed request, actual write handler, pending/approved state, and resulting artifact. A request can exist while the file still does not. This is not permission to generate a report or dashboard.

The exact harness and final operation were not selected in the planning conversation. Choose the smallest authentic demonstration that makes proposal, policy, execution, and observation visible. Do not build an agent framework on stage.

### Determinism distinctions to teach

- Tool choice and arguments are model proposals; they can vary or be wrong.
- The model may generate SQL or program code without executing it itself.
- The runtime and downstream service authorize and execute operations.
- An AI-authored function remains normal software when executed, with normal tests and permissions.
- Tool implementations may include APIs or model calls; not every tool is a pure deterministic function.
- Explicit authorization/validation is not the same as guaranteed semantic correctness.
- A predictable computation on a fixed snapshot differs from querying changing live data.

If pausing/approval is shown, use a real execution gate or clearly label a conceptual illustration. Do not fake a denied/approved trace.

## 9. Jev illustration, not another live dependency

Use the second poll to explain text → predefined category → aggregate. A synthetic job title such as “gerente de analítica” can illustrate the type of input. Do not attach made-up measured probabilities or claim a label was produced by Jev unless it was actually queried and recorded.

The official interface is state plus typed questions. Outputs include typed values and probabilities; Choice and Score report confidence. Application code consumes those values and owns operational routing.

A valid class can be wrong. Domain calibration/evaluation is required. A single Jev call is not automatically an agent, and its bounded output does not make the judgment deterministic.

## 10. Rehearsal and fallback checklist

- Fresh-event survey decision and exact configured QR URL recorded.
- QR independently scanned/decoded; visible URL matches it.
- Survey group and questions verified; no historical responses presented as the current room.
- Authenticated Cloudflare and agent environment ready before the talk.
- Read-only/narrow tool permissions technically enforced.
- Quota, model availability, connectivity, and tool health checked.
- Group mapping and cutoff prepared; no secrets visible during tab switches.
- Manual count and agent analysis use matching scope/cutoff.
- Agent returns compact SQL/results rather than an unreadable transcript.
- Actual runtime trace/handler available for the later demonstration.
- No individual respondent key or free-text personal data projected.
- Rehearsal recording/snapshot available if latency or networking fails, visibly labeled as a recording or prior snapshot.
- Never manufacture live votes, errors, banking outcomes, or classifications.
- No poll writes, clearing, closing, or administrative changes without authorization.

The transcripts include quota problems, navigation issues, and connectivity interruptions. Do not repeat the provider-switching tour. Fallback should preserve the lesson while clearly disclosing that it is not current live execution.
