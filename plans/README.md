# Motion plans — `docs/bfs-dfs-wave-and-thread.html`

Written 2026-10-08 by an `improve-animations` audit of the study site (the site
index and the written pages it links; decks out of scope). Each plan is
self-contained: hand one file to an executor with no other context.

| # | Plan | Severity | Status |
|---|---|---|---|
| 001 | [Make the runaway bars visible and calm the chip and halo motion](001-bfs-dfs-motion-css.md) | HIGH | TODO |
| 002 | [Pop only the chip that was just pushed in the queue/stack mini demo](002-queue-stack-mini-fresh-chip.md) | HIGH | TODO |

## Order and dependencies

- The user runs each plan in its own session: 001 first, then 002.
- No hard dependency. Both edit the same file but different regions: 001 owns
  the CSS plus three lines of the runaway script; 002 owns the queue/stack mini
  script. 002's feel check looks best after 001 has softened the pop.
- Neither plan commits or pushes. `docs/` is published live by GitHub Pages
  (`SW-AI-W02-03`), so the push is the user's call after he has looked.

## Deferred (not planned yet)

- Site-wide motion tokens and the shared reduced-motion rule in
  `benjohnbill.github.io/assets/site.css`; hover-gating the index card arrow
  (`(hover:hover) and (pointer:fine)`). Low severity; plan only if asked.
- Hanoi node transitions: 001 step 6 observes whether `fill="var(--bfs)"`
  attribute changes actually fade. A follow-up plan only if they switch instantly.
- `week04/study/csapp-ch3/index.html` animates `width` (`.35s`), but the page
  is not on the shared base yet. Migrate it first, then audit its motion once.
