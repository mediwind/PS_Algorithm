<h2><a href="https://codeforces.com/contest/1473/problem/A" target="_blank" rel="noopener noreferrer">1473A — Replacing Elements</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1473A](https://codeforces.com/contest/1473/problem/A) |

## Topics
`greedy` `implementation` `math` `sortings`

---

## Problem Statement

<div class="header"><div class="title">A. Replacing Elements</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>You have an array $$$a_1, a_2, \dots, a_n$$$. All $$$a_i$$$ are positive integers.</p><p>In one step you can choose three distinct indices $$$i$$$, $$$j$$$, and $$$k$$$ ($$$i \neq j$$$; $$$i \neq k$$$; $$$j \neq k$$$) and assign the sum of $$$a_j$$$ and $$$a_k$$$ to $$$a_i$$$, i. e. make $$$a_i = a_j + a_k$$$.</p><p>Can you make all $$$a_i$$$ lower or equal to $$$d$$$ using the operation above any number of times (possibly, zero)?</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains a single integer $$$t$$$ ($$$1 \le t \le 2000$$$) — the number of test cases.</p><p>The first line of each test case contains two integers $$$n$$$ and $$$d$$$ ($$$3 \le n \le 100$$$; $$$1 \le d \le 100$$$) — the number of elements in the array $$$a$$$ and the value $$$d$$$.</p><p>The second line contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ ($$$1 \le a_i \le 100$$$) — the array $$$a$$$.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, print <span class="tex-font-style-tt">YES</span>, if it's possible to make all elements $$$a_i$$$ less or equal than $$$d$$$ using the operation above. Otherwise, print <span class="tex-font-style-tt">NO</span>.</p><p>You may print each letter in any case (for example, <span class="tex-font-style-tt">YES</span>, <span class="tex-font-style-tt">Yes</span>, <span class="tex-font-style-tt">yes</span>, <span class="tex-font-style-tt">yEs</span> will all be recognized as positive answer).</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id009517095396477876" id="id0020044666488504392" class="input-output-copier">Copy</div></div><pre id="id009517095396477876">3
5 3
2 3 2 5 4
3 4
2 4 4
5 4
2 1 5 3 6
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id0030980626417722534" id="id009206253655412193" class="input-output-copier">Copy</div></div><pre id="id0030980626417722534">NO
YES
YES
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first test case, we can prove that we can't make all $$$a_i \le 3$$$.</p><p>In the second test case, all $$$a_i$$$ are already less or equal than $$$d = 4$$$.</p><p>In the third test case, we can, for example, choose $$$i = 5$$$, $$$j = 1$$$, $$$k = 2$$$ and make $$$a_5 = a_1 + a_2 = 2 + 1 = 3$$$. Array $$$a$$$ will become $$$[2, 1, 5, 3, 3]$$$.</p><p>After that we can make $$$a_3 = a_5 + a_2 = 3 + 1 = 4$$$. Array will become $$$[2, 1, 4, 3, 3]$$$ and all elements are less or equal than $$$d = 4$$$.</p></div>