---
name: publish-to-site
description: Publish or refresh the live copy of the "AI en la banca" deck at h1sort.com/gbm-ai by syncing ai-en-la-banca.html into the h1sort-website repo. Use after any edit to the deck, or when asked to mount, publish, deploy, refresh, or update the slides on the site.
---

# Publish the deck to h1sort.com/gbm-ai

**This repo (`gbm-ai-meetup`) is the source of truth.** `h1sort-website` only holds a generated public copy that is served live. Never edit the deck inside the site repo: fix it here, then sync.

```
gbm-ai-meetup/ai-en-la-banca.html  ──public.mjs──▶  h1sort-website/public/gbm-ai/index.html  ──▶  h1sort.com/gbm-ai/
gbm-ai-meetup/og.jpg               ──copy──▶  h1sort-website/public/gbm-ai/og.jpg
```

## Steps

1. **Deck repo is committed.** If the deck changed, rebuild it (`node build/assemble.mjs`), run the fit check (`node build/shot.mjs ai-en-la-banca.html --sizes 1920x1080,1280x720,390x844`), then commit and push `main`. The site copy should always match a pushed commit of this repo.
2. **Site repo on a fresh branch.** In `../h1sort-website`: `git checkout main && git pull`, then `git checkout -b chore/refresh-gbm-ai` (or `feat/...` for bigger changes). The site deploys via Workers Builds from `main`, so all changes go through a PR.
3. **Sync.** Run `.claude/skills/publish-to-site/sync.sh`, adding `--og` if slide 01 changed. It writes the public copy (`public.mjs`) and the cover image, runs `npm run build` in the site, checks that `dist/gbm-ai/index.html` matches and contains no notes, and confirms the route is in the sitemap.
4. **Smoke-test the real routing** (the Astro dev server doesn't match production):
   ```bash
   cd ../h1sort-website && npx wrangler dev --port 8799
   curl -sI localhost:8799/gbm-ai    # expect 307 -> /gbm-ai/
   curl -sI localhost:8799/gbm-ai/   # expect 200 text/html
   ```
   Open `localhost:8799/gbm-ai/?slide=5` in a browser: arrow keys advance, the footer shows `h1sort.com/gbm-ai`, there is no control bar in the bottom-right corner, and N, P and ? do nothing. Stop wrangler afterwards.
5. **Commit only the deck paths.** Use `git add public/gbm-ai` (plus `astro.config.mjs` / `public/llms.txt` if they changed). **Never `git add -A`**: the site has unrelated untracked local files (`.devin/`, `src/data/arena-text-models.json`). Commit with a message like `Refresh AI en la banca deck (gbm-ai-meetup <sha>)`, push, then open a PR with `gh pr create`.
6. **Any push deploys production, even before merging.** Workers Builds on h1sort-website currently deploys *every* branch push to production about 2.5 minutes later, not just `main` (seen 2026-10-01). Treat step 5's push as going live: run steps 3–4 first. Merge the PR so `main` matches what's live. To watch a deploy: `gh pr checks <n>` (the "Workers Builds" check) and `npx wrangler deployments list` in the site repo. Then confirm with `curl -s https://h1sort.com/gbm-ai/ | cmp - public/gbm-ai/index.html`.

## How it's mounted (and why)

- **The public copy differs from the local deck on purpose.** `public.mjs` strips every `<aside class="notes">` and adds `data-public` to `<html>`. The deck's own JS and CSS then hide the control bar (NOTAS · FUENTES · ? · ⛶) and ignore N, P and ?. The speaker presents from the **local** `ai-en-la-banca.html` in Chrome, which keeps notes and presenter mode. The public copy has no notes to show.

- **Static file, not an Astro page.** The deck is a self-contained HTML file (embedded fonts, its own JS and `?slide=` / `?presenter=1` URLs). Wrapping it in `Base.astro` like `/slides/fantastic-agents` would add the site's fonts, grain overlay, global CSS and assistant widget, and every refresh would mean re-porting it. Serving it from `public/` keeps refreshes to a scripted copy.
- **Sitemap:** `public/` files aren't Astro pages, so `/gbm-ai/` is listed under `customPages` in the site's `astro.config.mjs`.
- **`public/llms.txt`** has an entry for the deck. Update it if the slide count or framing changes.
- **Routing:** Cloudflare's static assets redirect `/gbm-ai` and `/gbm-ai/index.html` to `/gbm-ai/` (307), which fits the site's `trailingSlash: 'always'`. The worker only runs first for `/api/*` and `/p/*`, so it never sees this route. The survey QR links to `/p/UFRHASU9D4`, which is served by the same site.

## Where the footer and share metadata live

The footer URL, the cover-only URL, canonical/OG/Twitter meta and the favicon link are in `build/shell.html`. **`build/` is gitignored and local-only**: edit it there, re-run `node build/assemble.mjs`, and commit the regenerated `ai-en-la-banca.html`. The OG image (`og.jpg`, 1200×630, under 300 KB so WhatsApp shows the preview) is the cover rendered by `sync.sh --og`.

## Known gaps (accepted)

- **Notes are still in this public GitHub repo** (inside `ai-en-la-banca.html`). Only the live site copy is stripped.
- **The site's "no em dashes" copy rule** (h1sort-website `AGENTS.md`) isn't applied to the deck. The deck has its own editorial rules.

## Lessons log

Add a dated line here whenever a publish turns up something new.

- 2026-10-01 · First mount. All routes worked as expected under `wrangler dev` with no surprises. Added `customPages` to the sitemap and a `llms.txt` entry. Converted the OG image from an 805 KB PNG to a 96 KB JPEG.
- 2026-10-01 · Speaker asked that the live site not show the control bar or the notes. Added `public.mjs` (strips notes, sets `data-public`). The deck now has a public mode.
- 2026-10-01 · Merged PR #18 (`4b53757`), deployed 15:14:51Z (`ea469eb5`). Live `/gbm-ai/` is byte-identical to `main`. Both earlier PR-branch pushes had already deployed to production (15:07, 15:11), so the route was live before the merge.
