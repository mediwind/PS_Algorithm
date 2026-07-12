<h2><a href="https://codeforces.com/contest/1566/problem/A" target="_blank" rel="noopener noreferrer">1566A — Median Maximization</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1566A](https://codeforces.com/contest/1566/problem/A) |

## Topics
`binary search` `greedy` `math`

---

## Problem Statement

<div class="header"><div class="title">A. Median Maximization</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>You are given two positive integers $$$n$$$ and $$$s$$$. Find the maximum possible median of an array of $$$n$$$ <span class="tex-font-style-bf">non-negative</span> integers (not necessarily distinct), such that the sum of its elements is equal to $$$s$$$.</p><p>A <span class="tex-font-style-bf">median</span> of an array of integers of length $$$m$$$ is the number standing on the $$$\lceil {\frac{m}{2}} \rceil$$$-th (rounding up) position in the non-decreasing ordering of its elements. Positions are numbered starting from $$$1$$$. For example, a median of the array $$$[20,40,20,50,50,30]$$$ is the $$$\lceil \frac{m}{2} \rceil$$$-th element of $$$[20,20,30,40,50,50]$$$, so it is $$$30$$$. There exist other definitions of the median, but in this problem we use the described definition.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The input consists of multiple test cases. The first line contains a single integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases. Description of the test cases follows.</p><p>Each test case contains a single line with two integers $$$n$$$ and $$$s$$$ ($$$1 \le n, s \le 10^9$$$) — the length of the array and the required sum of the elements.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case print a single integer — the maximum possible median.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id006797522844368843" id="id008725985768870468" class="input-output-copier">Copy</div></div><pre id="id006797522844368843">8
1 5
2 5
3 5
2 1
7 17
4 14
1 1000000000
1000000000 1
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id009878481908624597" id="id00711412470257708" class="input-output-copier">Copy</div></div><pre id="id009878481908624597">5
2
2
0
4
4
1000000000
0
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>Possible arrays for the first three test cases (in each array the median is underlined):</p><ul> <li> In the first test case $$$[\underline{5}]$$$ </li><li> In the second test case $$$[\underline{2}, 3]$$$ </li><li> In the third test case $$$[1, \underline{2}, 2]$$$ </li></ul></div>