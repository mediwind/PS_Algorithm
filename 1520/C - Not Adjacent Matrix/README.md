<h2><a href="https://codeforces.com/contest/1520/problem/C" target="_blank" rel="noopener noreferrer">1520C — Not Adjacent Matrix</a></h2>

| | |
|---|---|
| **Difficulty** | 1000 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1520C](https://codeforces.com/contest/1520/problem/C) |

## Topics
`constructive algorithms`

---

## Problem Statement

<div class="header"><div class="title">C. Not Adjacent Matrix</div><div class="time-limit"><div class="property-title">time limit per test</div>4 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>We will consider the numbers $$$a$$$ and $$$b$$$ as adjacent if they differ by exactly one, that is, $$$|a-b|=1$$$.</p><p>We will consider cells of a square matrix $$$n \times n$$$ as adjacent if they have a common side, that is, for cell $$$(r, c)$$$ cells $$$(r, c-1)$$$, $$$(r, c+1)$$$, $$$(r-1, c)$$$ and $$$(r+1, c)$$$ are adjacent to it.</p><p>For a given number $$$n$$$, construct a square matrix $$$n \times n$$$ such that: </p><ul> <li> Each integer from $$$1$$$ to $$$n^2$$$ occurs in this matrix exactly once; </li><li> If $$$(r_1, c_1)$$$ and $$$(r_2, c_2)$$$ are adjacent cells, then the numbers written in them <span class="tex-font-style-bf">must not be adjacent</span>. </li></ul></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains one integer $$$t$$$ ($$$1 \le t \le 100$$$). Then $$$t$$$ test cases follow.</p><p>Each test case is characterized by one integer $$$n$$$ ($$$1 \le n \le 100$$$).</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, output: </p><ul> <li> <span class="tex-font-style-tt">-1</span>, if the required matrix does not exist; </li><li> the required matrix, otherwise (any such matrix if many of them exist). </li></ul><p>The matrix should be outputted as $$$n$$$ lines, where each line contains $$$n$$$ integers.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id001868990367645269" id="id0010312054871276388" class="input-output-copier">Copy</div></div><pre id="id001868990367645269">3
1
2
3
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id006614107810763197" id="id0016818111434681682" class="input-output-copier">Copy</div></div><pre id="id006614107810763197">1
-1
2 9 7
4 6 3
1 8 5
</pre></div></div></div>