<h2><a href="https://codeforces.com/contest/1516/problem/A" target="_blank" rel="noopener noreferrer">1516A — Tit for Tat</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1516A](https://codeforces.com/contest/1516/problem/A) |

## Topics
`greedy`

---

## Problem Statement

<div class="header"><div class="title">A. Tit for Tat</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>Given an array $$$a$$$ of length $$$n$$$, you can do at most $$$k$$$ operations of the following type on it:</p><ul> <li> choose $$$2$$$ different elements in the array, add $$$1$$$ to the first, and subtract $$$1$$$ from the second. However, all the elements of $$$a$$$ have to remain non-negative after this operation. </li></ul><p>What is lexicographically the smallest array you can obtain?</p><p>An array $$$x$$$ is <a href="https://en.wikipedia.org/wiki/Lexicographical_order">lexicographically smaller</a> than an array $$$y$$$ if there exists an index $$$i$$$ such that $$$x_i \lt y_i$$$, and $$$x_j=y_j$$$ for all $$$1 \le j  \lt  i$$$. Less formally, at the first index $$$i$$$ in which they differ, $$$x_i \lt y_i$$$.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains an integer $$$t$$$ ($$$1 \le t \le 20$$$) – the number of test cases you need to solve.</p><p>The first line of each test case contains $$$2$$$ integers $$$n$$$ and $$$k$$$ ($$$2 \le n \le 100$$$, $$$1 \le k \le 10000$$$) — the number of elements in the array and the maximum number of operations you can make.</p><p>The second line contains $$$n$$$ space-separated integers $$$a_1$$$, $$$a_2$$$, $$$\ldots$$$, $$$a_{n}$$$ ($$$0 \le a_i \le 100$$$) — the elements of the array $$$a$$$.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, print the lexicographically smallest array you can obtain after at most $$$k$$$ operations.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0022893772917008204" id="id009612166882334683" class="input-output-copier">Copy</div></div><pre id="id0022893772917008204">2
3 1
3 1 4
2 10
1 0
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id008496724358105643" id="id008876836438344077" class="input-output-copier">Copy</div></div><pre id="id008496724358105643">2 1 5 
0 1 
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the second test case, we start by subtracting $$$1$$$ from the first element and adding $$$1$$$ to the second. Then, we can't get any lexicographically smaller arrays, because we can't make any of the elements negative.</p></div>