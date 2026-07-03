<h2><a href="https://codeforces.com/contest/1620/problem/A" target="_blank" rel="noopener noreferrer">1620A — Equal or Not Equal</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1620A](https://codeforces.com/contest/1620/problem/A) |

## Topics
`constructive algorithms` `dsu` `implementation`

---

## Problem Statement

<div class="header"><div class="title">A. Equal or Not Equal</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>You had $$$n$$$ positive integers $$$a_1, a_2, \dots, a_n$$$ arranged <span class="tex-font-style-it">in a circle</span>. For each pair of neighboring numbers ($$$a_1$$$ and $$$a_2$$$, $$$a_2$$$ and $$$a_3$$$, ..., $$$a_{n - 1}$$$ and $$$a_n$$$, and $$$a_n$$$ and $$$a_1$$$), you wrote down: are the numbers in the pair equal or not.</p><p>Unfortunately, you've lost a piece of paper with the array $$$a$$$. Moreover, you are afraid that even information about equality of neighboring elements may be inconsistent. So, you are wondering: is there any array $$$a$$$ which is consistent with information you have about equality or non-equality of corresponding pairs?</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains a single integer $$$t$$$ ($$$1 \le t \le 1000$$$) — the number of test cases. Next $$$t$$$ cases follow.</p><p>The first and only line of each test case contains a non-empty string $$$s$$$ consisting of characters <span class="tex-font-style-tt">E</span> and/or <span class="tex-font-style-tt">N</span>. The length of $$$s$$$ is equal to the size of array $$$n$$$ and $$$2 \le n \le 50$$$. For each $$$i$$$ from $$$1$$$ to $$$n$$$: </p><ul> <li> if $$$s_i =$$$ <span class="tex-font-style-tt">E</span> then $$$a_i$$$ is equal to $$$a_{i + 1}$$$ ($$$a_n = a_1$$$ for $$$i = n$$$); </li><li> if $$$s_i =$$$ <span class="tex-font-style-tt">N</span> then $$$a_i$$$ is not equal to $$$a_{i + 1}$$$ ($$$a_n \neq a_1$$$ for $$$i = n$$$). </li></ul></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, print <span class="tex-font-style-tt">YES</span> if it's possible to choose array $$$a$$$ that are consistent with information from $$$s$$$ you know. Otherwise, print <span class="tex-font-style-tt">NO</span>.</p><p>It can be proved, that if there exists some array $$$a$$$, then there exists an array $$$a$$$ of positive integers with values less or equal to $$$10^9$$$.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id006578872813916392" id="id0021927172803652206" class="input-output-copier">Copy</div></div><pre id="id006578872813916392">4
EEE
EN
ENNEENE
NENN
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id0019342212282753513" id="id006194893544804485" class="input-output-copier">Copy</div></div><pre id="id0019342212282753513">YES
NO
YES
YES
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first test case, you can choose, for example, $$$a_1 = a_2 = a_3 = 5$$$.</p><p>In the second test case, there is no array $$$a$$$, since, according to $$$s_1$$$, $$$a_1$$$ is equal to $$$a_2$$$, but, according to $$$s_2$$$, $$$a_2$$$ is not equal to $$$a_1$$$.</p><p>In the third test case, you can, for example, choose array $$$a = [20, 20, 4, 50, 50, 50, 20]$$$.</p><p>In the fourth test case, you can, for example, choose $$$a = [1, 3, 3, 7]$$$.</p></div>