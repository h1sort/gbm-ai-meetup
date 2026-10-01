# Visual and implementation brief

## 1. Explicit visual request

The speaker asked for:

> Something cinematic like `/Users/Haro/Code/langchain-meetup/fantastic-agents.html`, but in a light theme.

Reference: [Fantastic Agents HTML](file:///Users/Haro/Code/langchain-meetup/fantastic-agents.html).

The request establishes the quality bar and light-theme direction. It does not ask for a creature deck recolor or an adaptation of employer-branded presentation code.

## 2. What to learn from the reference

The reference was inspected in source and opened in a browser. It has:

- Cinematic cover staging and intentional entrance pacing.
- Strong display typography with quieter supporting typography.
- Atmospheric depth rather than flat backgrounds.
- Original SVG illustration and diagrams.
- Animated strokes/pulses that trace meaningful paths.
- Repeated visual families that make architecture legible.
- Full-viewport composition, concise claims, and restrained reveals.
- Keyboard, wheel, and touch navigation; progress and slide folios.
- `?slide=N` deep links and a `?still=1` static/review mode.
- Reduced-motion handling.

Carry the craft and presentation ergonomics forward, not its specific creatures, Latin names, candlelight/brass field-guide setting, or fantasy framing.

## 3. Proposed original direction

**Light cinematic / institutional daylight.** This is a recommended design interpretation, not a user-approved exact preset.

- Ivory or warm off-white surfaces, with excellent projector contrast.
- Deep green/charcoal ink for text and diagram structure.
- Restrained copper/ochre accents for important boundaries and transitions.
- A limited green accent for evidence/authorized paths; a distinct warm accent for consequential execution or uncertainty.
- Editorial display typography with a clear sans-serif body and legible mono for code.
- Original abstractions of analytical reach, data paths, permission boundaries, and evidence convergence.
- Slow deliberate cover entrance and restrained section transitions.
- Evolving historical maps and trace animations whose movement explains the narrative.

Possible palette starting points, not fixed requirements:

| Role | Suggested color |
| --- | --- |
| Paper | `#f6f2e8` |
| Primary ink | `#17382f` |
| Evidence/authorized path | `#257a68` |
| Consequential-action accent | `#b75437` |
| Quiet warm accent | `#c5a053` |

Possible font pairing: Fraunces display, Manrope body, IBM Plex Mono technical. Inspect rendered Spanish typography before locking it. These fonts are not installed project dependencies by default; verify sources/licensing and loading behavior.

The poll site’s cream/ink/lime styling is context, not a requirement to copy its admin interface. The deck should feel like a composed talk, not a website screenshot gallery.

### Avoid

- Dark slides dominating a deck requested in a light theme.
- Generic purple gradients, blue SaaS-card layouts, excessive pills, or low-contrast pastel labels.
- A new arbitrary aesthetic on every slide.
- Stock banking skylines, robot mascots, fantasy creatures, franchise imagery, or decorative vendor-logo walls.
- Long continuous background animation that competes with diagrams or the QR.
- Huge architecture diagrams with 20 tiny components.
- Decorative motion that implies execution happened when only a request exists.

## 4. Visual grammar

Use consistent meaning across the deck:

- **Reachable boundary:** what can practically be inspected/used.
- **Model region:** flexible interpretation and proposed next steps.
- **Trusted application gate:** authorization, validation, and process requirements.
- **Solid path:** actual permitted execution or required control flow.
- **Return path:** observations or evaluation feedback.
- **Evidence join:** required completeness before assessment.
- **Operational rail:** provenance, audit, recovery, and persistent state.

Use labels and shape/line distinctions as well as color. A denied request and an approved request must be distinguishable without relying on red/green alone.

The four historical diagrams should evolve one map, rather than look like unrelated architecture inventories. The cover and close should share a motif, creating a resolved visual story.

## 5. Deliverable and engineering default

Suggested final filename: `ai-en-la-banca.html` in this repo.

Prefer a standalone HTML presentation with inline CSS/JavaScript and original inline SVG. Avoid unnecessary frontend frameworks or a build system in this currently empty repository. Do not install a library merely because it is familiar.

Aim for the deck itself to work offline. Live demos and the survey naturally require network access, but navigation, diagrams, and content should not depend on it. Embed fonts/assets where practical and legally permitted, or provide verified readable fallbacks. Do not leave runtime CDN dependencies or externally generated QR images as silent single points of failure.

Do not embed credentials, database clients with secrets, private admin sessions, or paid API keys. External links should be explicit user actions.

### Navigation

- Arrow keys, Space, Page Up/Down, Home, and End.
- Wheel and touch/swipe with sensible input throttling.
- Progress indication and consistent folios.
- Read-only deep-link review via `?slide=N`, with clearly documented numbering.
- A static mode such as `?still=1` for screenshots/review.
- Reduced-motion support with all meaningful content visible.
- Optional fullscreen and a compact help control.
- Presenter notes accessible but hidden from ordinary projected view.

If implementing notes/help dialogs, do not hijack keyboard input inside editable controls and do not let wheel handlers make notes impossible to read. Browser editing/export was not requested; do not make it a prerequisite.

### Viewport and density

- Each `.slide` fits exactly one viewport: `height: 100vh; height: 100dvh; overflow: hidden`.
- No inner slide scrolling in presentation mode.
- Use responsive `clamp()` typography and spacing.
- Content containers have bounded heights and correct `min-height: 0` behavior where necessary.
- Images and diagrams are constrained to available viewport space.
- Support shorter heights around 700, 600, and 500 pixels; narrow layouts should remain intentional.
- Do not hide essential statements merely to make a slide fit.
- One visual claim per slide; approximately 4–6 short bullets or two short paragraphs at most.
- Code panels about 8–10 legible lines; full prompts and nuances live in notes.
- Technical diagrams need genuinely legible labels on a projector.

## 6. Existing frontend-slides skill reference

The frontend-slides skill was invoked and these files were read:

- [Skill](file:///Users/Haro/.claude/skills/frontend-slides/SKILL.md)
- [Viewport base](file:///Users/Haro/.claude/skills/frontend-slides/viewport-base.css)
- [HTML architecture](file:///Users/Haro/.claude/skills/frontend-slides/html-template.md)
- [Animation patterns](file:///Users/Haro/.claude/skills/frontend-slides/animation-patterns.md)
- [Style presets](file:///Users/Haro/.claude/skills/frontend-slides/STYLE_PRESETS.md)

Use the actual source paths above if these are available in the next harness; do not assume a different skill directory. The user has already supplied purpose, narrative, duration, references, and light/cinematic preference. Do not repeat a generic discovery questionnaire as a blocker.

Local/global project rules take priority over generic skill examples. In particular, all Python work uses uv. Any new tool configuration belongs in `.devin/`, not `.claude/` or other harness-specific directories, unless explicitly requested.

## 7. Original reference constraints

Read [the LangChain repo’s AGENTS.md](file:///Users/Haro/Code/langchain-meetup/AGENTS.md) before exploring that repo.

`/Users/Haro/Code/langchain-meetup/masterclass-ai-tools.html` is an immutable reference-only artifact with explicit restrictions. It is **not needed for this task**. Do not edit, import, build from, or copy its wording, employer assets, proprietary fonts, NOVA/supernova motif, color system, animation code, or DOM/CSS implementation.

Do not modify `fantastic-agents.html` or any prior source repo while building the GBM deck. Use the current project for new work. Preserve its existing `.gitignore` unless a justified change is separately needed; do not casually overwrite it.

## 8. Validation checklist

### Static checks

- Run `git diff --check`.
- Validate HTML structure and unique IDs.
- Extract all embedded JavaScript and check it with Node (`node --check`); check browser console as well.
- Confirm main slide count, timing table, navigation targets, and folios agree.
- Check every link, QR target, asset path, and font-loading behavior.
- Independently scan/decode the QR; a visually plausible QR is not enough.
- Do not leak secrets or individual poll join keys in code, notes, or screenshots.

### Browser review

Render at least:

- Cover and closing.
- QR slide and live-demo cue.
- Historical diagram before/after expansion.
- Agent-loop diagram and request/execution boundary.
- Code/implementation split.
- Ask, Execute, and Judge architecture examples.
- Jev illustration.

Test at 1440×900 and 1280×720, plus a large projector-oriented viewport such as 1920×1080 and at least one narrow/mobile viewport. Also inspect short-height behavior. Measure content boxes, not just the absence of a body scrollbar; `overflow: hidden` can conceal clipping.

Check keyboard/wheel/touch navigation, first/last slide behavior, deep links, static mode, fullscreen/help/notes if present, reduced motion, and font/network failure behavior. Revisit earlier slides to ensure animations do not leave content hidden.

### Editorial and rehearsal

- Spanish accents and terminology correct.
- Exact agent quote attributed.
- Approximate historical years qualified.
- No fake audience results or unverified Jev metrics.
- Synthetic banking cases labeled as representative.
- Proposal, execution, authorization, approval, and final decision are distinct.
- Semantics, data cutoff, evidence completeness, and evaluation remain visible in the argument.
- The talk rehearses below the hard 30-minute limit.

### Temporary artifacts

Keep render outputs out of the final deliverable and Git unless requested. Chrome DevTools MCP in this environment rejected a screenshot path under `/tmp` because it was outside configured workspace roots. Use an allowed project-local temporary location if needed, then remove only files created for this task. Do not assume `/tmp` writes will work through that MCP.

No browser screenshots of a new deck were produced in the originating session because implementation was delegated before a deck existed.
