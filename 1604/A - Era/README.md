<h2><a href="https://codeforces.com/contest/1604/problem/A" target="_blank" rel="noopener noreferrer">1604A — Era</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1604A](https://codeforces.com/contest/1604/problem/A) |

## Topics
`greedy`

---

## Problem Statement

<div class="header"><div class="title">A. Era</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>Shohag has an integer sequence $$$a_1, a_2, \ldots, a_n$$$. He can perform the following operation any number of times (possibly, zero):</p><ul> <li> Select any positive integer $$$k$$$ (it can be different in different operations). </li><li> Choose any position in the sequence (possibly the beginning or end of the sequence, or in between any two elements) and insert $$$k$$$ into the sequence at this position. </li><li> This way, the sequence $$$a$$$ changes, and the next operation is performed on this changed sequence. </li></ul><p>For example, if $$$a=[3,3,4]$$$ and he selects $$$k = 2$$$, then after the operation he can obtain one of the sequences $$$[\underline{2},3,3,4]$$$, $$$[3,\underline{2},3,4]$$$, $$$[3,3,\underline{2},4]$$$, or $$$[3,3,4,\underline{2}]$$$.</p><p>Shohag wants this sequence to satisfy the following condition: for each $$$1 \le i \le |a|$$$, $$$a_i \le i$$$. Here, $$$|a|$$$ denotes the size of $$$a$$$.</p><p>Help him to find the minimum number of operations that he has to perform to achieve this goal. We can show that under the constraints of the problem it's always possible to achieve this goal in a finite number of operations.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains a single integer $$$t$$$ ($$$1 \le t \le 200$$$)  — the number of test cases.</p><p>The first line of each test case contains a single integer $$$n$$$ ($$$1 \le n \le 100$$$) — the initial length of the sequence.</p><p>The second line of each test case contains $$$n$$$ integers $$$a_1, a_2, \ldots, a_n$$$ ($$$1 \le a_i \le 10^9$$$) — the elements of the sequence.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, print a single integer  — the minimum number of operations needed to perform to achieve the goal mentioned in the statement.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0020433514274246967" id="id004069304595421078" class="input-output-copier">Copy</div></div><pre id="id0020433514274246967">4
3
1 3 4
5
1 2 5 7 4
1
1
3
69 6969 696969
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id006578541153794041" id="id009796236257608736" class="input-output-copier">Copy</div></div><pre id="id006578541153794041">1
3
0
696966
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first test case, we have to perform at least one operation, as $$$a_2=3 \gt 2$$$. We can perform the operation $$$[1, 3, 4] \rightarrow [1, \underline{2}, 3, 4]$$$ (the newly inserted element is underlined), now the condition is satisfied.</p><p>In the second test case, Shohag can perform the following operations:</p><p>$$$[1, 2, 5, 7, 4] \rightarrow [1, 2, \underline{3}, 5, 7, 4] \rightarrow [1, 2, 3, \underline{4}, 5, 7, 4] \rightarrow [1, 2, 3, 4, 5, \underline{3}, 7, 4]$$$.</p><p>In the third test case, the sequence already satisfies the condition.</p></div>