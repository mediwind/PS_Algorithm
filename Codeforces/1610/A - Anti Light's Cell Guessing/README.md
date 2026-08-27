<h2><a href="https://codeforces.com/contest/1610/problem/A" target="_blank" rel="noopener noreferrer">1610A — Anti Light's Cell Guessing</a></h2>

| | |
|---|---|
| **Difficulty** | 900 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1610A](https://codeforces.com/contest/1610/problem/A) |

## Topics
`math`

---

## Problem Statement

<div class="header"><div class="title">A. Anti Light's Cell Guessing</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>You are playing a game on a $$$n \times m$$$ grid, in which the computer has selected some cell $$$(x, y)$$$ of the grid, and you have to determine which one. </p><p>To do so, you will choose some $$$k$$$ and some $$$k$$$ cells $$$(x_1, y_1),\, (x_2, y_2), \ldots, (x_k, y_k)$$$, and give them to the computer. In response, you will get $$$k$$$ numbers $$$b_1,\, b_2, \ldots b_k$$$, where $$$b_i$$$ is the manhattan distance from $$$(x_i, y_i)$$$ to the hidden cell $$$(x, y)$$$ (so you know which distance corresponds to which of $$$k$$$ input cells). </p><p>After receiving these $$$b_1,\, b_2, \ldots, b_k$$$, you have to be able to determine the hidden cell. What is the smallest $$$k$$$ for which is it possible to always guess the hidden cell correctly, no matter what cell computer chooses?</p><p>As a reminder, the manhattan distance between cells $$$(a_1, b_1)$$$ and $$$(a_2, b_2)$$$ is equal to $$$|a_1-a_2|+|b_1-b_2|$$$.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line of the input contains a single integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases. The description of test cases follows. </p><p>The single line of each test case contains two integers $$$n$$$ and $$$m$$$ ($$$1 \le n, m \le 10^9$$$) — the number of rows and the number of columns in the grid.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case print a single integer — the minimum $$$k$$$ for that test case.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id001769759337404644" id="id009354207406209295" class="input-output-copier">Copy</div></div><pre id="id001769759337404644">2
2 3
3 1
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id00021559898359711283" id="id001742239906301285" class="input-output-copier">Copy</div></div><pre id="id00021559898359711283">2
1
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first test case, the smallest such $$$k$$$ is $$$2$$$, for which you can choose, for example, cells $$$(1, 1)$$$ and $$$(2, 1)$$$.</p><p>Note that you can't choose cells $$$(1, 1)$$$ and $$$(2, 3)$$$ for $$$k = 2$$$, as both cells $$$(1, 2)$$$ and $$$(2, 1)$$$ would give $$$b_1 = 1, b_2 = 2$$$, so we wouldn't be able to determine which cell is hidden if computer selects one of those.</p><p>In the second test case, you should choose $$$k = 1$$$, for it you can choose cell $$$(3, 1)$$$ or $$$(1, 1)$$$.</p></div>