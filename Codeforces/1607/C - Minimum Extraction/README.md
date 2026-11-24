<h2><a href="https://codeforces.com/contest/1607/problem/C" target="_blank" rel="noopener noreferrer">1607C — Minimum Extraction</a></h2>

| | |
|---|---|
| **Difficulty** | 1000 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1607C](https://codeforces.com/contest/1607/problem/C) |

## Topics
`brute force` `sortings`

---

## Problem Statement

<div class="header"><div class="title">C. Minimum Extraction</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>Yelisey has an array $$$a$$$ of $$$n$$$ integers.</p><p>If $$$a$$$ has length strictly greater than $$$1$$$, then Yelisei can apply an operation called <span class="tex-font-style-it">minimum extraction</span> to it: </p><ol> <li> First, Yelisei finds the minimal number $$$m$$$ in the array. If there are several identical minima, Yelisey can choose any of them. </li><li> Then the selected minimal element is removed from the array. After that, $$$m$$$ is subtracted from each remaining element. </li></ol><p>Thus, after each operation, the length of the array is reduced by $$$1$$$.</p><p>For example, if $$$a = [1, 6, -4, -2, -4]$$$, then the minimum element in it is $$$a_3 = -4$$$, which means that after this operation the array will be equal to $$$a=[1 {- (-4)}, 6 {- (-4)}, -2 {- (-4)}, -4 {- (-4)}] = [5, 10, 2, 0]$$$.</p><p>Since Yelisey likes big numbers, he wants the numbers in the array $$$a$$$ to be as big as possible.</p><p>Formally speaking, he wants to make the <span class="tex-font-style-bf">minimum</span> of the numbers in array $$$a$$$ to be <span class="tex-font-style-bf">maximal possible</span> (i.e. he want to maximize a minimum). To do this, Yelisey can apply the <span class="tex-font-style-it">minimum extraction</span> operation to the array as many times as he wants (possibly, zero). Note that the operation cannot be applied to an array of length $$$1$$$.</p><p>Help him find what maximal value can the minimal element of the array have after applying several (possibly, zero) <span class="tex-font-style-it">minimum extraction</span> operations to the array.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains an integer $$$t$$$ ($$$1 \leq t \leq 10^4$$$) — the number of test cases.</p><p>The next $$$2t$$$ lines contain descriptions of the test cases.</p><p>In the description of each test case, the first line contains an integer $$$n$$$ ($$$1 \leq n \leq 2 \cdot 10^5$$$) — the original length of the array $$$a$$$. The second line of the description lists $$$n$$$ space-separated integers $$$a_i$$$ ($$$-10^9 \leq a_i \leq 10^9$$$) — elements of the array $$$a$$$.</p><p>It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2 \cdot 10^5$$$.</p></div><div class="output-specification"><div class="section-title">Output</div><p>Print $$$t$$$ lines, each of them containing the answer to the corresponding test case. The answer to the test case is a single integer — the maximal possible minimum in $$$a$$$, which can be obtained by several applications of the described operation to it.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id001979228429721004" id="id005398177279380748" class="input-output-copier">Copy</div></div><pre id="id001979228429721004">8
1
10
2
0 0
3
-1 2 0
4
2 10 1 7
2
2 3
5
3 2 -4 -2 0
2
-1 1
1
-2
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id0014306454774168975" id="id0028722394832002496" class="input-output-copier">Copy</div></div><pre id="id0014306454774168975">10
0
2
5
2
2
2
-2
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first example test case, the original length of the array $$$n = 1$$$. Therefore <span class="tex-font-style-it">minimum extraction</span> cannot be applied to it. Thus, the array remains unchanged and the answer is $$$a_1 = 10$$$.</p><p>In the second set of input data, the array will always consist only of zeros.</p><p>In the third set, the array will be changing as follows: $$$[\color{blue}{-1}, 2, 0] \to [3, \color{blue}{1}] \to [\color{blue}{2}]$$$. The minimum elements are highlighted with $$$\color{blue}{\text{blue}}$$$. The maximal one is $$$2$$$.</p><p>In the fourth set, the array will be modified as $$$[2, 10, \color{blue}{1}, 7] \to [\color{blue}{1}, 9, 6] \to [8, \color{blue}{5}] \to [\color{blue}{3}]$$$. Similarly, the maximum of the minimum elements is $$$5$$$.</p></div>