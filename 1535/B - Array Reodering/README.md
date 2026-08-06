<h2><a href="https://codeforces.com/contest/1535/problem/B" target="_blank" rel="noopener noreferrer">1535B — Array Reodering</a></h2>

| | |
|---|---|
| **Difficulty** | 900 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1535B](https://codeforces.com/contest/1535/problem/B) |

## Topics
`brute force` `greedy` `math` `number theory` `sortings`

---

## Problem Statement

<div class="header"><div class="title">B. Array Reodering</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>You are given an array $$$a$$$ consisting of $$$n$$$ integers.</p><p>Let's call a pair of indices $$$i$$$, $$$j$$$ <span class="tex-font-style-bf">good</span> if $$$1 \le i  \lt  j \le n$$$ and $$$\gcd(a_i, 2a_j)  \gt  1$$$ (where $$$\gcd(x, y)$$$ is the greatest common divisor of $$$x$$$ and $$$y$$$).</p><p>Find the maximum number of <span class="tex-font-style-bf">good</span> index pairs if you can reorder the array $$$a$$$ in an arbitrary way.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains a single integer $$$t$$$ ($$$1 \le t \le 1000$$$) — the number of test cases.</p><p>The first line of the test case contains a single integer $$$n$$$ ($$$2 \le n \le 2000$$$) — the number of elements in the array.</p><p>The second line of the test case contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ ($$$1 \le a_i \le 10^5$$$).</p><p>It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2000$$$.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, output a single integer — the maximum number of <span class="tex-font-style-bf">good</span> index pairs if you can reorder the array $$$a$$$ in an arbitrary way.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id000798517831061043" id="id0032695895391593277" class="input-output-copier">Copy</div></div><pre id="id000798517831061043">3
4
3 6 5 3
2
1 7
5
1 4 2 4 1
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id009405315105043829" id="id0011494678246527901" class="input-output-copier">Copy</div></div><pre id="id009405315105043829">4
0
9
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first example, the array elements can be rearranged as follows: $$$[6, 3, 5, 3]$$$.</p><p>In the third example, the array elements can be rearranged as follows: $$$[4, 4, 2, 1, 1]$$$.</p></div>