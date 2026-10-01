#!/usr/bin/env bash
# Copy the deck into the h1sort-website checkout (public copy: notes stripped, no control bar)
# and verify the static build.
#
#   .claude/skills/publish-to-site/sync.sh [--og]
#
#   --og   re-render og.jpg from the cover first (only needed when slide 01 changed)
#
# Does not branch, commit, or push; SKILL.md covers that.
set -euo pipefail

DECK_REPO="$(cd "$(dirname "$0")/../../.." && pwd)"
SITE_REPO="$(cd "${SITE_REPO:-$DECK_REPO/../h1sort-website}" && pwd)"
ROUTE="gbm-ai"
DEST="$SITE_REPO/public/$ROUTE"

[ -d "$SITE_REPO/.git" ] || { echo "site repo not found at $SITE_REPO (set SITE_REPO)"; exit 1; }

if [ "${1:-}" = "--og" ]; then
  node "$DECK_REPO/build/shot.mjs" "$DECK_REPO/ai-en-la-banca.html" --slides 1 --sizes 1200x630 --out "$DECK_REPO/build/shots/og"
  sips -s format jpeg -s formatOptions 82 "$DECK_REPO/build/shots/og/s01-1200x630.png" --out "$DECK_REPO/og.jpg" >/dev/null
fi

grep -q 'h1sort.com/gbm-ai' "$DECK_REPO/ai-en-la-banca.html" || { echo "deck is missing the h1sort.com/gbm-ai footer"; exit 1; }

mkdir -p "$DEST"
node "$DECK_REPO/.claude/skills/publish-to-site/public.mjs" "$DECK_REPO/ai-en-la-banca.html" "$DEST/index.html"
cp "$DECK_REPO/og.jpg" "$DEST/og.jpg"

(cd "$SITE_REPO" && npm run build >/dev/null)
cmp "$SITE_REPO/dist/$ROUTE/index.html" "$DEST/index.html"
if grep -q 'class="notes"' "$SITE_REPO/dist/$ROUTE/index.html"; then echo "presenter notes leaked into the build"; exit 1; fi
grep -q "h1sort.com/$ROUTE/" "$SITE_REPO/dist/sitemap-0.xml" || { echo "/$ROUTE/ missing from sitemap (astro.config.mjs customPages)"; exit 1; }

echo "synced: $(git -C "$DECK_REPO" rev-parse --short HEAD) -> $DEST"
git -C "$SITE_REPO" status --short -- public/$ROUTE
