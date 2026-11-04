# 001 — Make the runaway bars visible and calm the chip and halo motion

- **Status**: DONE
- **Commit**: 146dbb3
- **Severity**: HIGH (bars), MEDIUM (halo, pop)
- **Category**: Performance / Accessibility / Physicality & origin, easing
- **Estimated scope**: 1 file (`docs/bfs-dfs-wave-and-thread.html`), about 10 changed lines (CSS + 3 JS lines)

All paths are relative to the repository root `~/dev/krafton-jungle/week02-03/`.
The page is published straight from `docs/` by GitHub Pages: a push changes the
live site. Do not push; the user decides that.

## Problem

Three defects in one page, all in its inline `<style>` and one small script.

**A. The runaway bars never appear (confirmed in the browser on 2026-10-08).**
The bar starts at `scaleX(0)` and nothing ever releases it. The script animates
`width` instead, so every bar stays zero wide. The user sees only the numbers.

```css
/* docs/bfs-dfs-wave-and-thread.html:239-242 — current */
.bar{
  height:13px;border-radius:3px;background:var(--dfs);opacity:.85;flex:none;
  transform:scaleX(0);transform-origin:left center;transition:transform .4s ease-out
}
```

```js
/* docs/bfs-dfs-wave-and-thread.html:1057 — current (row template) */
div.innerHTML=`<span class="t">${r.t}바퀴</span><span class="bar" style="width:0"></span><span class="n"></span>`;
/* :1065 — current (reset) */
rows.forEach(r=>{r.querySelector('.bar').style.width='0';r.querySelector('.n').textContent='';});
/* :1078 — current (each 260ms tick) */
rows[k].querySelector('.bar').style.width=(r.size/max*100*0.72)+'%';
```

**B. Under reduced motion the current-node halo flickers (code reading; verify in step 6).**
The halo loops forever. The page's reduced-motion rule shrinks the duration to
1ms but keeps `infinite`, so the ring restarts every millisecond and each frame
catches it at a random size and opacity.

```css
/* :205-206 — current */
.nd.cur .halo{opacity:1;animation:ring 1.4s ease-out infinite}
@keyframes ring{0%{transform:scale(1);opacity:.9}100%{transform:scale(1.62);opacity:0}}
/* :284-286 — current */
@media (prefers-reduced-motion:reduce){
  *{animation-duration:.001s !important;transition-duration:.001s !important}
}
```

**C. New chips pop from 60% size over 320ms.** Chips appear on every step of
the stepper, which the user clicks many times in a row. Nothing in the real
world grows from 60%; the entrance is too big and too slow for a repeated action.

```css
/* :160-161 — current */
.chip.fresh{animation:pop .32s ease-out}
@keyframes pop{from{transform:scale(.6);opacity:0}to{transform:scale(1);opacity:1}}
```

## Target

```css
/* :root (page token block, after the line `--mono:var(--font-code);`) */
--ease-out:cubic-bezier(0.23, 1, 0.32, 1);

/* A — bar: fixed slot, length by scaleX, finishes before the next 260ms tick */
.bar{
  width:72%;height:13px;border-radius:3px;background:var(--dfs);opacity:.85;flex:none;
  transform:scaleX(0);transform-origin:left center;transition:transform 240ms var(--ease-out)
}

/* B — reduced motion: play once, so the halo settles as a still ring */
@media (prefers-reduced-motion:reduce){
  *{animation-duration:.001s !important;animation-iteration-count:1 !important;transition-duration:.001s !important}
}

/* C — chip entrance */
.chip.fresh{animation:pop 200ms var(--ease-out)}
@keyframes pop{from{transform:scale(.94);opacity:0}to{transform:scale(1);opacity:1}}
```

```js
/* A — row template: no inline width */
div.innerHTML=`<span class="t">${r.t}바퀴</span><span class="bar"></span><span class="n"></span>`;
/* A — reset: drop the inline transform so the CSS scaleX(0) applies again */
rows.forEach(r=>{r.querySelector('.bar').style.transform='';r.querySelector('.n').textContent='';});
/* A — each tick: scale instead of width */
rows[k].querySelector('.bar').style.transform='scaleX('+(r.size/max)+')';
```

Why these values:
- `cubic-bezier(0.23, 1, 0.32, 1)` is the strong ease-out for UI entrances.
- 240ms keeps each bar's growth inside the script's 260ms tick, so bars never overlap in motion.
- `scale(.94)` + `opacity:0` is the "never from nothing" entrance (target range 0.9–0.97); 200ms suits a frequently repeated action.
- Under reduced motion the halo ends at its 100% keyframe, then falls back to the base rule `opacity:1` with no transform: a still ring that still marks the current node. Movement is gone; the state cue stays.

## Repo conventions to follow

- Page tokens live in the page's own `:root` block at `docs/bfs-dfs-wave-and-thread.html:10-23` (e.g. `--bfs:#12608E;`). Add `--ease-out` there, one token per line, same indentation.
- The CSS in this file is compact: one rule per line or a few short lines, no spaces after `:`. Match it.
- Shared colors and fonts come from `https://benjohnbill.github.io/assets/site.css`. Do not edit that file in this plan.

## Steps

1. In the `:root` block, add the line `  --ease-out:cubic-bezier(0.23, 1, 0.32, 1);` directly after `  --mono:var(--font-code);` (line 22). Do not add it to the dark-mode `:root` block at line 24.
2. Replace `.chip.fresh` and `@keyframes pop` (lines 160-161) with the two lines under "C" in Target.
3. Replace the `.bar{…}` rule (lines 239-242) with the rule under "A" in Target. Only two things change: `width:72%;` is added at the front, and the transition becomes `transform 240ms var(--ease-out)`.
4. In the runaway script, make the three JS edits under "A" in Target (lines 1057, 1065, 1078). Change nothing else in that script.
5. Replace the reduced-motion block (lines 284-286) with the block under "B" in Target.
6. Run the verification below, including the two observe-only checks (halo, Hanoi), and report what you saw.

## Boundaries

- Touch only `docs/bfs-dfs-wave-and-thread.html`. Not `docs/index.html`, not other pages, not `assets/site.css`.
- Do NOT change the `.nd.cur .halo` rule or the `ring` keyframes. The infinite halo is the current-node cue and stays.
- Do NOT touch the queue/stack mini demo (`fill()` near line 1021). Plan 002 owns it.
- Do NOT change the Hanoi section; only observe it (step 6).
- Do NOT change markup beyond the row template string in step 4.
- No new dependencies, no build step, no commit, no push.
- If any quoted "current" code does not match the file (drift since 146dbb3), STOP and report instead of improvising.

## Verification

- **Mechanical** (run from `docs/`):
  - `grep -c 'style.width' bfs-dfs-wave-and-thread.html` → `0`
  - `grep -c 'scale(.6)' bfs-dfs-wave-and-thread.html` → `0`
  - `grep -c 'animation-iteration-count:1' bfs-dfs-wave-and-thread.html` → `1`
  - `grep -c 'var(--ease-out)' bfs-dfs-wave-and-thread.html` → `2`
- **Serve locally**: `python3 -m http.server 8765 -d docs` from the repo root, then open `http://localhost:8765/bfs-dfs-wave-and-thread.html` in a browser on the Windows side (WSL forwards localhost). The user opens it; do not drive the user's browser.
- **Feel check — bars**: in "visited를 없애면", press 돌려 보기.
  - Twelve red bars grow from the left edge, one per tick, each settling before the next starts.
  - The last bar is the longest and reaches about 72% of the row.
  - The numbers now sit in one column after the full bar slot instead of trailing each bar end. That is expected.
  - Press 처음으로: every bar collapses to nothing; press 돌려 보기 again and it replays.
- **Feel check — chips**: step through the BFS/DFS stepper with 다음. Each new chip fades in from slightly smaller, short and quiet, with no visible "jump".
- **Observe only — halo under reduced motion**: in the page's DevTools console run
  `document.head.insertAdjacentHTML('beforeend','<style id="rm">*{animation-duration:.001s!important;animation-iteration-count:1!important;transition-duration:.001s!important}</style>')`
  then step the stepper. Expect a still ring around the current node, no flicker. Remove with `document.getElementById('rm').remove()`.
- **Observe only — Hanoi**: press the Hanoi start button. Report whether node colors fade (about 0.45s) or switch instantly. Do not fix either way; it decides whether a follow-up plan is needed.
- **Done when**: the four greps match, the bars are visible and replay after reset, and the user has looked at the bars and chips.
