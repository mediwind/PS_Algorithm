<h2><a href="https://codeforces.com/contest/1486/problem/A" target="_blank" rel="noopener noreferrer">1486A — Shifting Stacks</a></h2>

| | |
|---|---|
| **Difficulty** | 900 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1486A](https://codeforces.com/contest/1486/problem/A) |

## Topics
`greedy` `implementation`

---

## Problem Statement

<div class="header"><div class="title">A. Shifting Stacks</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>You have $$$n$$$ stacks of blocks. The $$$i$$$-th stack contains $$$h_i$$$ blocks and it's height is the number of blocks in it. In one move you can take a block from the $$$i$$$-th stack (if there is at least one block) and put it to the $$$i + 1$$$-th stack. Can you make the sequence of heights strictly increasing?</p><p>Note that the number of stacks always remains $$$n$$$: stacks don't disappear when they have $$$0$$$ blocks.</p></div><div class="input-specification"><div class="section-title">Input</div><p>First line contains a single integer $$$t$$$ $$$(1 \leq t \leq 10^4)$$$ — the number of test cases.</p><p>The first line of each test case contains a single integer $$$n$$$ $$$(1 \leq n \leq 100)$$$. The second line of each test case contains $$$n$$$ integers $$$h_i$$$ $$$(0 \leq h_i \leq 10^9)$$$ — starting heights of the stacks.</p><p>It's guaranteed that the sum of all $$$n$$$ does not exceed $$$10^4$$$.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case output <span class="tex-font-style-tt">YES</span> if you can make the sequence of heights strictly increasing and <span class="tex-font-style-tt">NO</span> otherwise.</p><p>You may print each letter in any case (for example, <span class="tex-font-style-tt">YES</span>, <span class="tex-font-style-tt">Yes</span>, <span class="tex-font-style-tt">yes</span>, <span class="tex-font-style-tt">yEs</span> will all be recognized as positive answer).</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id00200982137130862" id="id0034187871915653556" class="input-output-copier">Copy</div></div><pre id="id00200982137130862">6
2
1 2
2
1 0
3
4 4 4
2
0 0
3
0 1 0
4
1000000000 1000000000 1000000000 1000000000
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id007767778011959555" id="id003683201932684337" class="input-output-copier">Copy</div></div><pre id="id007767778011959555">YES
YES
YES
NO
NO
YES
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first test case there is no need to make any moves, the sequence of heights is already increasing.</p><p>In the second test case we need to move one block from the first stack to the second. Then the heights become $$$0$$$ $$$1$$$.</p><p>In the third test case we could move one block from the first stack to the second and then from the second to the third, which would make the heights $$$3$$$ $$$4$$$ $$$5$$$.</p><p>In the fourth test case we can't make a move, but the sequence is not increasing, so the answer is <span class="tex-font-style-tt">NO</span>.</p><p>In the fifth test case we can only make one move (from the second to the third stack), which would make the heights $$$0$$$ $$$0$$$ $$$1$$$. Both $$$0$$$ $$$1$$$ $$$0$$$ and $$$0$$$ $$$0$$$ $$$1$$$ are not increasing sequences, so the answer is <span class="tex-font-style-tt">NO</span>.</p></div>