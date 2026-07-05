<h2><a href="https://codeforces.com/contest/1546/problem/A" target="_blank" rel="noopener noreferrer">1546A — AquaMoon and Two Arrays</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1546A](https://codeforces.com/contest/1546/problem/A) |

## Topics
`brute force` `greedy`

---

## Problem Statement

<div class="header"><div class="title">A. AquaMoon and Two Arrays</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>AquaMoon and Cirno are playing an interesting game with arrays. Cirno has prepared two arrays $$$a$$$ and $$$b$$$, both consist of $$$n$$$ non-negative integers. AquaMoon can perform the following operation an arbitrary number of times (possibly zero):</p><ul> <li> She chooses two indices $$$i$$$ and $$$j$$$ ($$$1 \le i, j \le n$$$), then decreases the $$$i$$$-th element of array $$$a$$$ by $$$1$$$, and increases the $$$j$$$-th element of array $$$a$$$ by $$$1$$$. The resulting values at $$$i$$$-th and $$$j$$$-th index of array $$$a$$$ are $$$a_i - 1$$$ and $$$a_j + 1$$$, respectively. Each element of array $$$a$$$ <span class="tex-font-style-bf">must be non-negative after each operation</span>. If $$$i = j$$$ this operation doesn't change the array $$$a$$$. </li></ul><p>AquaMoon wants to make some operations to make arrays $$$a$$$ and $$$b$$$ equal. Two arrays $$$a$$$ and $$$b$$$ are considered equal if and only if $$$a_i = b_i$$$ for all $$$1 \leq i \leq n$$$.</p><p>Help AquaMoon to find a sequence of operations that will solve her problem or find, that it is impossible to make arrays $$$a$$$ and $$$b$$$ equal.</p><p>Please note, that you <span class="tex-font-style-bf">don't have to minimize</span> the number of operations.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The input consists of multiple test cases. The first line contains a single integer $$$t$$$ ($$$1 \leq t \leq 100$$$) — the number of test cases.</p><p>The first line of each test case contains a single integer $$$n$$$ ($$$1 \leq n \leq 100$$$).</p><p>The second line of each test case contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ ($$$0 \leq a_i \leq 100$$$). <span class="tex-font-style-bf">The sum of all $$$a_i$$$ does not exceed $$$100$$$.</span></p><p>The third line of each test case contains $$$n$$$ integers $$$b_1, b_2, \dots, b_n$$$ ($$$0 \leq b_i \leq 100$$$). <span class="tex-font-style-bf">The sum of all $$$b_i$$$ does not exceed $$$100$$$.</span></p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case print "<span class="tex-font-style-tt">-1</span>" on the only line if it is impossible to make two arrays equal with some sequence of operations.</p><p>Otherwise, print an integer $$$m$$$ ($$$0 \leq m \leq 100$$$) in the first line — the number of operations. Then print $$$m$$$ lines, each line consists of two integers $$$i$$$ and $$$j$$$ — the indices you choose for the operation.</p><p>It can be proven that if it is possible to make two arrays equal with some sequence of operations, there exists a sequence with $$$m \leq 100$$$.</p><p>If there are multiple possible solutions, you can print any.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id003129452998864095" id="id0085892884576148" class="input-output-copier">Copy</div></div><pre id="id003129452998864095">4
4
1 2 3 4
3 1 2 4
2
1 3
2 1
1
0
0
5
4 3 2 1 0
0 1 2 3 4
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id005596615097014114" id="id006985789540067152" class="input-output-copier">Copy</div></div><pre id="id005596615097014114">2
2 1
3 1
-1
0
6
1 4
1 4
1 5
1 5
2 5
2 5
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first example, we do the following operations:</p><ul> <li> $$$i = 2$$$, $$$j = 1$$$: $$$[1, 2, 3, 4] \rightarrow [2, 1, 3, 4]$$$; </li><li> $$$i = 3$$$, $$$j = 1$$$: $$$[2, 1, 3, 4] \rightarrow [3, 1, 2, 4]$$$; </li></ul><p>In the second example, it's impossible to make two arrays equal.</p></div>