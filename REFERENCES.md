# Sources, paths, and provenance

## 1. Primary context requested by the speaker

### Class transcripts

Read these as prior delivery/context, not as verified final copy for every claim:

1. [Class 1 transcript](file:///Users/Haro/Code/ai4data-class/slides/clase-01-transcript.md)
   - Absolute path: `/Users/Haro/Code/ai4data-class/slides/clase-01-transcript.md`
   - QR-created dataset, manual count, live agent SQL, cheap-analysis thesis, historical phases, context/tools/evals, and the original tool/file demonstration.
   - Stored as one very long line. A line-limited reader may silently omit most of it; ensure the full content is actually inspected if needed.
2. [Class 2 transcript](file:///Users/Haro/Code/ai4data-class/slides/clase-02-transcript.md)
   - Absolute path: `/Users/Haro/Code/ai4data-class/slides/clase-02-transcript.md`
   - OLTP/OLAP, analytical infrastructure, ETL, free-text survey, classification, and early Jev discussion.
   - Lines 1597–1798 recap the eras and context/tools/evals. Lines 6190–7069 discuss classification and Jev.
   - Do not import the long database benchmark/ETL sequence into the GBM talk.
3. [Class 3 transcript](file:///Users/Haro/Code/ai4data-class/slides/clase-03-transcript.md)
   - Absolute path: `/Users/Haro/Code/ai4data-class/slides/clase-03-transcript.md`
   - Timestamped. Agent definition, model request/harness execution, semantic trap, stale-data trap, classification, and evaluations.
   - Lines 943–1047: definition and the request/execution/observation loop.
   - Lines 1664–1706: cash-tip recording and unsupported interpretation.
   - Lines 1754–1844: contextual correction; do not equate a reference prompt with the entire governed semantic layer.
   - Lines 2327–2389: stale data and the importance of the cutoff.
   - Lines 2477–2539: context, tools, freshness, and evaluations.

All three transcripts were read in the originating session. They contain automatic-transcription errors and some broad spontaneous claims. Do not preserve misspelled model names, speculative facts, unsafe “YOLO” permission advice, or model-alignment-as-security claims merely because the speaker said them live.

### Prior class decks

Verified local files:

- [Class 1 HTML](file:///Users/Haro/Code/ai4data-class/slides/clase-01.html)
- [Class 2 HTML](file:///Users/Haro/Code/ai4data-class/slides/clase-02.html)
- [Class 3 HTML](file:///Users/Haro/Code/ai4data-class/slides/clase-03.html)

Use as optional content context. The main visual reference for the new deck is Fantastic Agents, not these class decks.

## 2. Post-AI Data Stack

Primary article, requested by the speaker and read in full:

[Ian Macomber — The Shape and Feel of the Post-AI Data Stack](https://www.iandmacomber.com/blog/post-ai-data-stack/)

The article is dated August 30, 2026 and describes four approximate phases:

- Pre-modern stack around 2013: data moats, difficult semi-structured web/event analysis, and scale/workload constraints.
- Cloud warehouse adoption around 2016: broader analytical scope.
- Modern Data Stack around 2020: managed ETL plus Reverse ETL; reporter to operator.
- Post-AI around 2026: analysis becomes cheap; company-wide consistency/consensus and reusable expert judgment become scarce.

Important sections:

- **Pre-Modern Data Stack:** use the practical-question framing rather than retelling the author’s Wayfair anecdote as the speaker’s personal banking history.
- **Modern Data Stack:** ETL expands what teams see; Reverse ETL expands what they do.
- **Agent-Readable Artifacts:** expose meaning, queries, filters, owners, and provenance to agents.
- **Agent-Operable Tools:** capabilities must be usable by agents without depending on UI click automation.
- **Agent-Agnostic Context:** shared knowledge should survive changing models and interfaces.
- **Agent-Testable Consensus / Compounding Improvements:** compare outputs and traces; preserve corrections as shared context and regression cases.
- **Beyond SQL:** structure unstructured meaning for reusable analysis instead of reprocessing everything for every question.
- **The Job Today:** encode judgment so future analyses do not depend on the expert being in the room.

Do not repeat “infinite storage/compute,” “assume models are never wrong,” or consensus-as-proof literally. The new talk should be accurate about practical scale, model errors, and validated reference evidence.

## 3. Production-agent framework from the prior meetup

### Primary presenter notes

[Fantastic Agents presenter notes](file:///Users/Haro/Code/langchain-meetup/PRESENTER_NOTES.md)

Absolute path: `/Users/Haro/Code/langchain-meetup/PRESENTER_NOTES.md`.

This is the key source for banking architecture, not just a design reference:

- Lines 9–27: argument in one minute; local discretion, deterministic permissions/invariants/consequences.
- Lines 132–180: agent definition; the model proposes, the harness executes or refuses.
- Lines 184–222: authority gradient, not a maturity ladder; authority versus autonomy.
- Lines 295–403: authorized retrieval, trusted identity, budgets, evidence, and shape-versus-truth.
- Lines 488–581: tool access versus user permission versus execution approval; governed execution, receipts, idempotency, and reconciliation.
- Lines 688–726: **may versus must**, prompt request versus workflow invariant.
- Lines 730–882: consequential assessment, required evidence join, bounded inner agent, policy route, durable state, and measured calibration.
- Lines 947–997: pause/review/resume and checkpoint-versus-idempotency nuance.
- Lines 1005–1100: synthesis and least-freedom architecture selection.
- Lines 1171–1275: recurring contrasts, claims to avoid, and concise answers.

Original taxonomy: **Know / Do / Decide** through fictional Sourcehound, Keypaw, and Caseweaver specimens. The GBM talk adapts the engineering to **Ask / Execute / Judge**. Do not import the animal names or field-guide narrative.

### Visual reference

[Fantastic Agents HTML](file:///Users/Haro/Code/langchain-meetup/fantastic-agents.html)

Absolute path: `/Users/Haro/Code/langchain-meetup/fantastic-agents.html`.

Inspected characteristics: atmosphere, display typography, original SVGs, animated path tracing, cover choreography, varied but consistent slide families, full-viewport diagrams, and navigation. It has 23 main slides; **that is not the GBM slide-count requirement**.

Useful source locations:

- Early CSS: visual system, atmosphere, reveals, and cover composition.
- Around lines 1074–1122: representative retrieval architecture diagram.
- Around lines 1278–1324: action architecture.
- Around lines 1389–1404: may versus must.
- Around lines 1538–1593: assessment workflow.
- Around lines 2166–2394: navigation, atmospheric behavior, static mode, and motion handling.

Reference-repo instructions:

[LangChain meetup AGENTS.md](file:///Users/Haro/Code/langchain-meetup/AGENTS.md).

Its `masterclass-ai-tools.html` is explicitly immutable/reference-only with employer-asset and copying restrictions. It is not a required source for this task; leave it untouched.

## 4. Exact agent definition

[Simon Willison — Agents, September 18, 2025](https://simonwillison.net/2025/Sep/18/agents/)

Exact quotation:

> An LLM agent runs tools in a loop to achieve a goal.

The URL and exact quotation are recorded in the prior class’s [sources.md](file:///Users/Haro/Code/ai4data-class/demos/clase-03/sources.md), lines 124–133, and consistently used in the meetup notes.

Use as an operational definition, not a philosophical claim that all software agency must meet it.

## 5. Jev — primary sources checked

- [TypeSafe — Introducing System One Models & Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)
- [TypeSafe documentation](https://docs.typesafe.ai/)
- [Documentation index](https://docs.typesafe.ai/llms.txt)

The official introduction and documentation landing page were read in this session. The index is a documented discovery entry point for subsequent exploration.

Verified source-level framing:

- TypeSafe describes Jev as its first System One model and an early-access offering in the introduction.
- State plus typed questions returns values/probabilities for software to consume.
- Choice picks from predefined options; Score evaluates an ordered rubric; Noul represents a yes/no-style probabilistic judgment.
- Choice and Score return confidence in the documented interface.
- Application code composes and routes outcomes.

Speed, cost, intelligence, and calibration statements are vendor claims unless independently measured on the relevant task. Type constraints do not prove the selected answer is semantically correct. Do not copy “can’t hallucinate” as “cannot make an incorrect banking judgment.” No numerical performance claim is necessary for this talk.

## 6. Survey and demo implementation references

Public links:

- [Class 1 survey](https://h1sort.com/p/JFQES4AF97)
- [Class 2 survey](https://h1sort.com/p/8P56ZUVE9Q)
- [Password-protected management](https://h1sort.com/polls/)

The two public group definitions were inspected through the browser without voting or changing state. Exact questions are in DEMO.md.

Helpful verified local files:

- [Class 1 poll prompts](file:///Users/Haro/Code/ai4data-class/demos/clase-01-poll-prompts.md) — read in full; schema expectations, scoped read-only guidance, respondent/browser distinction, fixed UTC cutoffs, and analytical denominator rules. **Use this instead of reconstructing the opening from an imperfect transcript.**
- [Class 2 data contract](file:///Users/Haro/Code/ai4data-class/demos/clase-02/data-contract.md) — read; raw response fields and curated analytical contracts. Its historical counts are not current/event findings.
- [Class 3 demo prompts](file:///Users/Haro/Code/ai4data-class/demos/clase-03-prompts.md) — read; replay and semantic/freshness examples. Do not blindly execute its write/setup steps or inherit its historical paid-service workflow.
- [Class 3 sources](file:///Users/Haro/Code/ai4data-class/demos/clase-03/sources.md) — read; exact definition attribution and source verification caveats.

Additional paths were verified to exist but were not all inspected in detail:

- `/Users/Haro/Code/ai4data-class/demos/clase-03/agent/agent.py`
- `/Users/Haro/Code/ai4data-class/demos/clase-03/agent/tools.py`
- `/Users/Haro/Code/ai4data-class/demos/clase-03/evals/cases.py`
- `/Users/Haro/Code/ai4data-class/demos/clase-03/evals/run_evals.py`
- `/Users/Haro/Code/ai4data-class/demos/clase-03/trap1-tips/README.md`
- `/Users/Haro/Code/ai4data-class/demos/clase-03/trap1-tips/despues/AGENTS.md`
- `/Users/Haro/Code/ai4data-class/demos/clase-02/pipeline/06_jev.py`
- `/Users/Haro/Code/ai4data-class/demos/clase-02/notebooks/03_llm_jev.ipynb`
- `/Users/Haro/Code/ai4data-class/slides/assets/clase-03/agent-loop.svg`
- `/Users/Haro/Code/ai4data-class/slides/assets/clase-03/harness.svg`

Use notebook-aware readers for `.ipynb` files. Read surrounding instructions before executing anything. These are context, not dependencies that the new deck must import.

## 7. Invitation and screenshots

The invitation specifies GBM AI Experience / AI & Finance, AI/agents/quantitative models in finance, the 30-minute talk, regulated environments, common implementation issues, emerging solutions, Post-AI Data Stack, Jev, and the panel described in STORY.md.

Images were pasted into this conversation. Their temporary local paths are listed for provenance, not as durable required assets:

- Invitation: `/var/folders/cq/bk3jgkp10mj0n6k8h9ytmc3r0000gp/T/devin-pasted-images/1790819937245928000-99927-0-pasted.png`
- Q1/Q2 screenshot: `/var/folders/cq/bk3jgkp10mj0n6k8h9ytmc3r0000gp/T/devin-pasted-images/1790820640033742000-99927-1-pasted.png`
- Q3/Q4 screenshot: `/var/folders/cq/bk3jgkp10mj0n6k8h9ytmc3r0000gp/T/devin-pasted-images/1790820640039632000-99927-2-pasted.png`
- Q5 screenshot: `/var/folders/cq/bk3jgkp10mj0n6k8h9ytmc3r0000gp/T/devin-pasted-images/1790820640042848000-99927-3-pasted.png`
- Class 2 management screenshot: `/var/folders/cq/bk3jgkp10mj0n6k8h9ytmc3r0000gp/T/devin-pasted-images/1790820640044185000-99927-4-pasted.png`

The speaker explicitly said the screenshots were additional context. Do not make them the main deck visuals, reproduce management controls, or present their displayed counts as results of the new event. Temporary files may not survive a different session; the canonical wording and invitation summary are preserved in these Markdown documents.

## 8. Contact and language

Speaker’s public site: [h1sort.com](https://h1sort.com/).

Public identity used in prior delivery: Carlos Aro, “Charlie”; AI Engineer. Prefer concise identity/contact over a long employer biography. Do not invent social-profile URLs or add unprovided branding.

Main projected language: Spanish. Keep exact English technical names/definition where useful; explain them in Spanish nearby.

## 9. Source precedence and accuracy

1. Explicit decisions recorded in this handoff.
2. Exact current survey metadata and verified demo semantics.
3. Primary articles/docs and the prior meetup’s careful production framing.
4. Transcripts as evidence of delivery and speaker voice, not authority for every factual assertion.
5. Optional prior screenshots, illustrative figures, or rehearsals—always labeled with their real provenance.

Do not conflate the old class surveys with GBM attendees, source claims with independently measured performance, or representative architectures with actual employer systems.
