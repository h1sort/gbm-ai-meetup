# GBM talk — implementation handoff

## Start here

Build a cinematic, light-theme HTML presentation for **“AI en la banca: el hoy y el mañana”**, a roughly 30-minute GBM AI & Finance talk. The narrative has already been discussed with the speaker. **Preserve the story arc; do not restart discovery or substitute a generic agents presentation.**

The speaker requested this Markdown handoff so another coding harness can implement the deck, potentially with a swarm. This handoff replaces implementation in the originating session: **no new deck, demo application, or deployment has been created yet.**

Project root: `/Users/Haro/Code/gbm-ai-meetup`.

### Read in this order

1. [STORY.md](STORY.md) — canonical argument, section timing, Spanish speaker beats, transitions, and claims to avoid.
2. [SLIDES.md](SLIDES.md) — proposed 18-slide production outline implementing that argument.
3. [DEMO.md](DEMO.md) — exact existing surveys, live opening, analysis semantics, tool demonstration, and rehearsal boundaries.
4. [DESIGN.md](DESIGN.md) — light cinematic direction, reference-deck characteristics, implementation requirements, and validation.
5. [REFERENCES.md](REFERENCES.md) — absolute local source paths, hyperlinks, provenance, and relevant excerpts.

If these documents appear to conflict, preserve explicit user decisions and the arc in STORY.md. The slide outline and aesthetic specifics are implementation defaults, not permission to change the central argument.

## The story in one paragraph

The audience creates a dataset through a QR survey. The speaker manually runs a simple `COUNT(*)` in Cloudflare, then asks an agent a question requiring substantially more elaborate SQL. This demonstrates that producing analysis has become cheap. Four historical phases explain how infrastructure expanded analytical reach: fragmented systems around 2013, cloud warehouses around 2016, the Modern Data Stack and operational activation around 2020, and the Post-AI Data Stack around 2026. The talk then defines an agent and exposes the distinction between a model-generated tool request and the real application code that authorizes and executes it. Banking applications are organized as **Ask / Execute / Judge**, with controls proportional to the delegated authority. Jev illustrates typed, bounded model judgments consumed by software. The closing reframes the opportunity: convert institutional expertise into reusable infrastructure so meaning and control survive cheap, abundant analysis.

> Producir análisis es cada vez más barato. Lo difícil es conservar su significado y controlar qué hacemos con él.

## Explicit decisions to preserve

- Title from the invitation: **AI en la banca: el hoy y el mañana**.
- Approximately 30 minutes; plan 28 minutes of material and 2 minutes of buffer.
- Spanish delivery and projected copy. Preserve the exact English Simon Willison definition with attribution.
- Open with the QR and **the original six-question Class 1 survey**, not a newly shortened survey.
- First demonstrate a manual count in Cloudflare, then live agent-generated and executed SQL for a cross-question analysis.
- **No dashboard generation, no report generation, and no live ETL construction.**
- Improve the 2013 history: focus on reasonable questions made impractical by fragmented data, shape, scale, and resource constraints; do not make the DBA the antagonist.
- Include the agent definition and a live tool demonstration exposing proposal versus execution.
- Banking framework: **Ask / Execute / Judge**, adapting the prior meetup’s Know / Do / Decide production patterns. The speaker explicitly prefers Judge to Decide.
- Include the Post-AI Data Stack and Jev, as requested in the invitation.
- Visual direction: cinematic like the prior `fantastic-agents.html`, **but in a light theme**.

## Working defaults, not separately confirmed user choices

Use these to proceed rather than blocking implementation:

- Mixed technical/business audience, inferred from the invitation’s professionals and leaders in AI, banking, and finance.
- Roughly 18 main slides. Optional sources and detailed technical material should not lengthen the timed talk.
- Primary banking illustrations: active-customer metric or policy investigation for Ask; missing-card freeze for Execute; synthetic fraud-alert investigation for Judge.
- Keep Jev as a compact conceptual/illustrative segment, not a third live API dependency.
- Fold semantic meaning, provenance, and evaluations into the Post-AI and Ask/Judge material instead of adding a separate lecture.
- Original ivory/ink visual system with restrained green and copper accents; exact palette and fonts remain design choices.
- Proposed deliverable filename: `ai-en-la-banca.html`.
- No browser text-editing feature was requested or selected. Prioritize presentation ergonomics and speaker notes instead.

## Outstanding event preparation

These do not prevent building the deck, but must remain visible:

1. The public survey links currently point to historical class groups. A fresh GBM group with identical questions is recommended but **has not been created or authorized in this session**. Clearly note the existing link’s status in presenter notes. Do not fabricate a new URL or silently alter the existing polls.
2. The exact agent harness and executable tool demonstration have not been locked. Keep staging simple and expose authentic runtime traces.
3. Live counts, query results, and any future demo recording must be measured during rehearsal or the event; never invent audience findings.
4. The proposed subtitle and synthetic banking example can be polished without changing the arc.

## Context and confidentiality

All banking cases and architecture diagrams are teaching composites, not the speaker’s employer’s systems. Say **“una arquitectura representativa”**, never “nuestra arquitectura.” Do not copy employer branding, internal screenshots, schemas, operational metrics, or anecdotes into this deck.

The original poll responses are real audience data. Use aggregates, not individual profiles. A browser identifier is not a verified person; do not expose join keys.

## Suggested swarm boundaries

One agent should own the final HTML and integration. Keep parallel work disjoint:

- **Story/editorial:** check Spanish projected copy and speaker notes against STORY.md; supply revisions without editing the final HTML concurrently.
- **Visual design:** develop original light-theme visual language and illustrations; work in clearly assigned assets or prototypes.
- **Architecture/demos:** verify diagram boundaries, poll-query semantics, Jev claims, and actual trace-display strategy; do not execute writes or modify live polls.
- **Integrator:** assemble the standalone deck, navigation, animations, notes, and assets.
- **QA:** independently inspect rendered slides, code validity, viewport fit, reduced motion, timing, QR behavior, and source accuracy.

Do not let separate agents independently reinvent each section’s visual grammar or narrative. Coordinate a single palette, typography, diagram notation, and timing budget. Avoid concurrent writes to the same HTML file.

## Definition of done

- The agreed arc is evident without reading speaker notes.
- A polished, original light-theme deck exists in this repo and opens locally.
- The QR resolves to the configured, real survey URL; historical/fresh-group status is explicit.
- The opening contains manual count and agent-SQL cues, not fake live outputs or a generated dashboard.
- Proposal versus execution is visibly taught, and mandatory controls are outside model discretion.
- Ask, Execute, and Judge have distinct consequences and controls.
- Jev is not represented as automatically correct, deterministic, or itself an agent.
- Keyboard/wheel/touch navigation, progress, deep links, and reduced motion work.
- Every slide fits its viewport; no accidental inner scrollbars, clipped labels, or unreadable diagrams.
- Spanish accents, attributions, links, code, and folios are checked.
- Source repos and reference decks remain unmodified. No credentials are embedded; no commit, push, or deployment without a separate request.

## Local tooling already checked

- Node: `v24.14.0`.
- uv: `0.10.9`.
- Use **uv for everything Python-related**. Do not use pip, pipx, poetry, or plain Python commands outside uv.
- `uv run --no-project --with qrcode==8.2 python ...` successfully generated an SVG QR for the existing Class 1 public link. The result was printed only; no QR asset was saved.
- No package manifest or test infrastructure existed in this repo when inspected. The only original tracked working file was `.gitignore`.

Final-deck validation should include `git diff --check`, parsing/checking embedded JavaScript with `node --check`, browser layout inspection, and real QR decoding/scanning. See DESIGN.md for the full checklist.
