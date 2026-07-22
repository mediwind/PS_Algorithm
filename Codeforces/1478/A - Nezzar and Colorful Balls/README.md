<h2><a href="https://codeforces.com/contest/1478/problem/A" target="_blank" rel="noopener noreferrer">1478A — Nezzar and Colorful Balls</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1478A](https://codeforces.com/contest/1478/problem/A) |

## Topics
`brute force` `greedy`

---

## Problem Statement

<div class="header"><div class="title">A. Nezzar and Colorful Balls</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>512 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>Nezzar has $$$n$$$ balls, numbered with integers $$$1, 2, \ldots, n$$$. Numbers $$$a_1, a_2, \ldots, a_n$$$ are written on them, respectively. Numbers on those balls form a non-decreasing sequence, which means that $$$a_i \leq a_{i+1}$$$ for all $$$1 \leq i  \lt  n$$$.</p><p>Nezzar wants to color the balls using the minimum number of colors, such that the following holds.</p><ul> <li> For any color, numbers on balls will form a <span class="tex-font-style-bf">strictly increasing sequence</span> if he keeps balls with this chosen color and discards all other balls. </li></ul> <p>Note that a sequence with the length at most $$$1$$$ is considered as a strictly increasing sequence.</p><p>Please help Nezzar determine the minimum number of colors.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains a single integer $$$t$$$ ($$$1 \le t \le 100$$$) — the number of testcases. </p><p>The first line of each test case contains a single integer $$$n$$$ ($$$1 \le n \le 100$$$).</p><p>The second line of each test case contains $$$n$$$ integers $$$a_1,a_2,\ldots,a_n$$$ ($$$1 \le a_i \le n$$$). It is guaranteed that $$$a_1 \leq a_2 \leq \ldots \leq a_n$$$.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, output the minimum number of colors Nezzar can use.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0012668646401529027" id="id0019444750896567198" class="input-output-copier">Copy</div></div><pre id="id0012668646401529027">5
6
1 1 1 2 3 4
5
1 1 2 2 3
4
2 2 2 2
3
1 2 3
1
1
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id0012259759830909445" id="id007956702337413026" class="input-output-copier">Copy</div></div><pre id="id0012259759830909445">3
2
4
1
1
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>Let's match each color with some numbers. Then:</p><p>In the first test case, one optimal color assignment is $$$[1,2,3,3,2,1]$$$.</p><p>In the second test case, one optimal color assignment is $$$[1,2,1,2,1]$$$.</p></div>