<h2><a href="https://codeforces.com/contest/1476/problem/A" target="_blank" rel="noopener noreferrer">1476A — K-divisible Sum</a></h2>

| | |
|---|---|
| **Difficulty** | 1000 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1476A](https://codeforces.com/contest/1476/problem/A) |

## Topics
`binary search` `constructive algorithms` `greedy` `math`

---

## Problem Statement

<div class="header"><div class="title">A. K-divisible Sum</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>You are given two integers $$$n$$$ and $$$k$$$.</p><p>You should create an array of $$$n$$$ <span class="tex-font-style-bf">positive integers</span> $$$a_1, a_2, \dots, a_n$$$ such that the sum $$$(a_1 + a_2 + \dots + a_n)$$$ is divisible by $$$k$$$ and maximum element in $$$a$$$ is minimum possible.</p><p>What is the minimum possible maximum element in $$$a$$$?</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains a single integer $$$t$$$ ($$$1 \le t \le 1000$$$) — the number of test cases.</p><p>The first and only line of each test case contains two integers $$$n$$$ and $$$k$$$ ($$$1 \le n \le 10^9$$$; $$$1 \le k \le 10^9$$$).</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, print one integer — the minimum possible maximum element in array $$$a$$$ such that the sum $$$(a_1 + \dots + a_n)$$$ is divisible by $$$k$$$. </p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0020350250294480976" id="id006374938110316801" class="input-output-copier">Copy</div></div><pre id="id0020350250294480976">4
1 5
4 3
8 8
8 17
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id0014234506431977612" id="id0018790781389307099" class="input-output-copier">Copy</div></div><pre id="id0014234506431977612">5
2
1
3
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first test case $$$n = 1$$$, so the array consists of one element $$$a_1$$$ and if we make $$$a_1 = 5$$$ it will be divisible by $$$k = 5$$$ and the minimum possible.</p><p>In the second test case, we can create array $$$a = [1, 2, 1, 2]$$$. The sum is divisible by $$$k = 3$$$ and the maximum is equal to $$$2$$$.</p><p>In the third test case, we can create array $$$a = [1, 1, 1, 1, 1, 1, 1, 1]$$$. The sum is divisible by $$$k = 8$$$ and the maximum is equal to $$$1$$$.</p></div>