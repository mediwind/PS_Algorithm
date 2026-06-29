<h2><a href="https://codeforces.com/contest/1562/problem/A" target="_blank" rel="noopener noreferrer">1562A — The Miracle and the Sleeper</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1562A](https://codeforces.com/contest/1562/problem/A) |

## Topics
`greedy` `math`

---

## Problem Statement

<div class="header"><div class="title">A. The Miracle and the Sleeper</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>You are given two integers $$$l$$$ and $$$r$$$, $$$l\le r$$$. Find the largest possible value of $$$a \bmod b$$$ over all pairs $$$(a, b)$$$ of integers for which $$$r\ge a \ge b \ge l$$$.</p><p>As a reminder, $$$a \bmod b$$$ is a remainder we get when dividing $$$a$$$ by $$$b$$$. For example, $$$26 \bmod 8 = 2$$$.</p></div><div class="input-specification"><div class="section-title">Input</div><p>Each test contains multiple test cases.</p><p>The first line contains one positive integer $$$t$$$ $$$(1\le t\le 10^4)$$$, denoting the number of test cases. Description of the test cases follows.</p><p>The only line of each test case contains two integers $$$l$$$, $$$r$$$ ($$$1\le l \le r \le 10^9$$$).</p></div><div class="output-specification"><div class="section-title">Output</div><p>For every test case, output the largest possible value of $$$a \bmod b$$$ over all pairs $$$(a, b)$$$ of integers for which $$$r\ge a \ge b \ge l$$$.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id007952950818410733" id="id009263919604750537" class="input-output-copier">Copy</div></div><pre id="id007952950818410733">4
1 1
999999999 1000000000
8 26
1 999999999
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id008839525281308108" id="id005376564802164618" class="input-output-copier">Copy</div></div><pre id="id008839525281308108">0
1
12
499999999
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first test case, the only allowed pair is $$$(a, b) = (1, 1)$$$, for which $$$a \bmod b = 1 \bmod 1 = 0$$$.</p><p>In the second test case, the optimal choice is pair $$$(a, b) = (1000000000, 999999999)$$$, for which $$$a \bmod b = 1$$$.</p></div>