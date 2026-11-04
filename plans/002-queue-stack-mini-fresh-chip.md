# 002 — Pop only the chip that was just pushed in the queue/stack mini demo

- **Status**: DONE
- **Commit**: 146dbb3
- **Severity**: HIGH
- **Category**: Purpose & frequency
- **Estimated scope**: 1 file (`docs/bfs-dfs-wave-and-thread.html`), about 8 changed JS lines

All paths are relative to the repository root `~/dev/krafton-jungle/week02-03/`.
The page is published straight from `docs/` by GitHub Pages: a push changes the
live site. Do not push; the user decides that.

## Problem

The mini demo shows a queue and a stack side by side. Its point is *which value
just went in* and *which one comes out*. But every redraw gives every chip the
class `fresh`, so on each click all chips replay the pop animation at once. The
one new chip is lost in the movement, and on "꺼내기" chips that did not change
pop too. Confirmed in the browser on 2026-10-08: on the third push A, B and C
all popped.

```js
/* docs/bfs-dfs-wave-and-thread.html:1021-1036 — current */
  function fill(host,arr,cls){
    host.innerHTML='';host.classList.toggle('empty',arr.length===0);
    arr.forEach(v=>{const d=document.createElement('span');d.className='chip fresh '+cls;d.textContent=v;host.append(d);});
  }
  function draw(){
    fill(qBin,q,'q');fill(sBin,s,'q');
    bPush.disabled=n>=seq.length;
    bPop.disabled=q.length===0;
  }
  bPush.onclick=()=>{const v=seq[n++];q.push(v);s.push(v);
    qOut.textContent='넣음 → '+v; sOut.textContent='넣음 → '+v; draw();};
  bPop.onclick=()=>{const a=q.shift(),b=s.pop();
    qOut.innerHTML='꺼냄 ← <b>'+a+'</b>  (가장 먼저 넣은 것)';
    sOut.innerHTML='꺼냄 ← <b>'+b+'</b>  (가장 나중에 넣은 것)';draw();};
  bRes.onclick=()=>{n=0;q=[];s=[];qOut.innerHTML='&nbsp;';sOut.innerHTML='&nbsp;';draw();};
  draw();
```

## Target

A push appends the new value at the end of both arrays (`q.push`, `s.push`), so
the new chip is always the last one. Only that chip gets `fresh`, and only on a
push. Pop, reset and the first draw animate nothing.

```js
/* target */
  function fill(host,arr,cls,pushed){
    host.innerHTML='';host.classList.toggle('empty',arr.length===0);
    arr.forEach((v,idx)=>{const d=document.createElement('span');d.className='chip '+cls+(pushed&&idx===arr.length-1?' fresh':'');d.textContent=v;host.append(d);});
  }
  function draw(pushed){
    fill(qBin,q,'q',pushed);fill(sBin,s,'q',pushed);
    bPush.disabled=n>=seq.length;
    bPop.disabled=q.length===0;
  }
  bPush.onclick=()=>{const v=seq[n++];q.push(v);s.push(v);
    qOut.textContent='넣음 → '+v; sOut.textContent='넣음 → '+v; draw(true);};
```

`bPop.onclick`, `bRes.onclick` and the final `draw();` stay as they are: they
call `draw()` with no argument, so `pushed` is `undefined` and no chip gets
`fresh`.

## Repo conventions to follow

- The stepper in the same file already does this right: `chips()` at `docs/bfs-dfs-wave-and-thread.html:893-902` adds `fresh` only to the newly added last chip (`idx===list.length-1&&list.length>prev.length`). Imitate its intent; the mini demo is simpler, so the explicit `pushed` flag is enough.
- Compact one-line JS style, no semicolon-free rewrites, no new helpers.

## Steps

1. Replace the `fill` function (lines 1021-1024) with the target `fill`.
2. Replace the first line of `draw` (line 1026, `fill(qBin,q,'q');fill(sBin,s,'q');`) with `fill(qBin,q,'q',pushed);fill(sBin,s,'q',pushed);`, and change its signature from `function draw(){` to `function draw(pushed){`.
3. In `bPush.onclick` (line 1031), change the final `draw();` to `draw(true);`.
4. Leave everything else in this IIFE unchanged.

## Boundaries

- Touch only the queue/stack mini IIFE (`/* ---------- 큐/스택 미니 ---------- */`, about lines 1013-1037).
- Do NOT change the CSS (`.chip.fresh`, `@keyframes pop`). Plan 001 owns those values. The two plans are independent and may land in either order.
- Do NOT change the stepper's `chips()` function.
- No new dependencies, no build step, no commit, no push.
- If the quoted "current" code does not match the file (drift since 146dbb3), STOP and report instead of improvising.

## Verification

- **Mechanical** (from `docs/`):
  - `grep -c "chip fresh '" bfs-dfs-wave-and-thread.html` → `0` (the unconditional class is gone)
  - `grep -c 'draw(true)' bfs-dfs-wave-and-thread.html` → `1`
- **Serve locally**: `python3 -m http.server 8765 -d docs` from the repo root; the user opens `http://localhost:8765/bfs-dfs-wave-and-thread.html` on the Windows side. Do not drive the user's browser.
- **Feel check**: in the queue/stack mini demo,
  - Press "다음 값 넣기" three times slowly. Each time, only the newest chip (A, then B, then C) pops; the older chips sit still.
  - Press "꺼내기" once. Nothing pops; the queue loses its front chip, the stack loses its last chip.
  - Press reset. The bins empty with no animation.
  - Console check right after a push: `[...document.querySelectorAll('#qBin .chip.fresh')].length` → `1`.
- **Done when**: both greps match and the user has seen only the new chip pop.
