#!/usr/bin/env node
// Make the live-site copy of the deck: strip presenter notes and switch on public mode
// (no control bar; N, P and ? are disabled). The local deck keeps everything.
//
//   node .claude/skills/publish-to-site/public.mjs <in.html> <out.html>
import { readFileSync, writeFileSync } from 'node:fs';

const [src, out] = process.argv.slice(2);
let html = readFileSync(src, 'utf8');

const slides = (html.match(/<section class="slide\b/g) || []).length;
let stripped = 0;
html = html.replace(/[ \t]*<aside class="notes">[\s\S]*?<\/aside>\n?/g, () => (stripped++, ''));
if (stripped !== slides) throw new Error(`stripped ${stripped} notes for ${slides} slides`);

const tag = '<html lang="es" class="no-js">';
if (!html.includes(tag)) throw new Error('unexpected <html> tag');
html = html.replace(tag, '<html lang="es" class="no-js" data-public>');

if (/class="notes"/.test(html)) throw new Error('notes left in public copy');
writeFileSync(out, html);
console.log(`public copy: ${stripped} notes stripped, ${(html.length / 1024).toFixed(0)} KB`);
