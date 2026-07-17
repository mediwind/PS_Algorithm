<h2><a href="https://codeforces.com/contest/1454/problem/A" target="_blank" rel="noopener noreferrer">1454A — Special Permutation</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1454A](https://codeforces.com/contest/1454/problem/A) |

## Topics
`constructive algorithms` `probabilities`

---

## Problem Statement

<div class="header"><div class="title">A. Special Permutation</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>You are given one integer $$$n$$$ ($$$n  \gt  1$$$).</p><p>Recall that a permutation of length $$$n$$$ is an array consisting of $$$n$$$ distinct integers from $$$1$$$ to $$$n$$$ in arbitrary order. For example, $$$[2, 3, 1, 5, 4]$$$ is a permutation of length $$$5$$$, but $$$[1, 2, 2]$$$ is not a permutation ($$$2$$$ appears twice in the array) and $$$[1, 3, 4]$$$ is also not a permutation ($$$n = 3$$$ but there is $$$4$$$ in the array).</p><p>Your task is to find a permutation $$$p$$$ of length $$$n$$$ that there is no index $$$i$$$ ($$$1 \le i \le n$$$) such that $$$p_i = i$$$ (so, for all $$$i$$$ from $$$1$$$ to $$$n$$$ the condition $$$p_i \ne i$$$ should be satisfied).</p><p>You have to answer $$$t$$$ independent test cases.</p><p>If there are several answers, you can print any. It can be proven that the answer exists for each $$$n  \gt  1$$$.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line of the input contains one integer $$$t$$$ ($$$1 \le t \le 100$$$) — the number of test cases. Then $$$t$$$ test cases follow.</p><p>The only line of the test case contains one integer $$$n$$$ ($$$2 \le n \le 100$$$) — the length of the permutation you have to find.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, print $$$n$$$ distinct integers $$$p_1, p_2, \ldots, p_n$$$ — a permutation that there is no index $$$i$$$ ($$$1 \le i \le n$$$) such that $$$p_i = i$$$ (so, for all $$$i$$$ from $$$1$$$ to $$$n$$$ the condition $$$p_i \ne i$$$ should be satisfied).</p><p>If there are several answers, you can print any. It can be proven that the answer exists for each $$$n  \gt  1$$$.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id007646986276236125" id="id00039672480201824234" class="input-output-copier">Copy</div></div><pre id="id007646986276236125">2
2
5
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id0029729856312167413" id="id0037294253963712043" class="input-output-copier">Copy</div></div><pre id="id0029729856312167413">2 1
2 1 5 3 4
</pre></div></div></div>