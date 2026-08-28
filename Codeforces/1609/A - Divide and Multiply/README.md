<h2><a href="https://codeforces.com/contest/1609/problem/A" target="_blank" rel="noopener noreferrer">1609A — Divide and Multiply</a></h2>

| | |
|---|---|
| **Difficulty** | 900 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1609A](https://codeforces.com/contest/1609/problem/A) |

## Topics
`greedy` `implementation` `math` `number theory`

---

## Problem Statement

<div class="header"><div class="title">A. Divide and Multiply</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><center> <img class="tex-graphics" height="302px" src="https://espresso.codeforces.com/023c3fb86b9ac22b6cb1accb6de674bfa4b74a5e.png" style="max-width: 100.0%;max-height: 100.0%;" width="454px"> </center><p>William has array of $$$n$$$ numbers $$$a_1, a_2, \dots, a_n$$$. He can perform the following sequence of operations <span class="tex-font-style-bf">any number of times</span>: </p><ol> <li> Pick any two items from array $$$a_i$$$ and $$$a_j$$$, where $$$a_i$$$ must be a multiple of $$$2$$$ </li><li> $$$a_i = \frac{a_i}{2}$$$ </li><li> $$$a_j = a_j \cdot 2$$$ </li></ol><p>Help William find the maximal sum of array elements, which he can get by performing the sequence of operations described above.</p></div><div class="input-specification"><div class="section-title">Input</div><p>Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). Description of the test cases follows.</p><p>The first line of each test case contains an integer $$$n$$$ $$$(1 \le n \le 15)$$$, the number of elements in William's array.</p><p>The second line contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ $$$(1 \le a_i  \lt  16)$$$, the contents of William's array.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case output the maximal sum of array elements after performing an optimal sequence of operations.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id005933703367506183" id="id007153685805995389" class="input-output-copier">Copy</div></div><pre id="id005933703367506183">5
3
6 4 2
5
1 2 3 4 5
1
10
3
2 3 4
15
8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id002719252766659995" id="id009437752658484405" class="input-output-copier">Copy</div></div><pre id="id002719252766659995">50
46
10
26
35184372088846
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first example test case the optimal sequence would be: </p><ol> <li> Pick $$$i = 2$$$ and $$$j = 1$$$. After performing a sequence of operations $$$a_2 = \frac{4}{2} = 2$$$ and $$$a_1 = 6 \cdot 2 = 12$$$, making the array look as: [12, 2, 2]. </li><li> Pick $$$i = 2$$$ and $$$j = 1$$$. After performing a sequence of operations $$$a_2 = \frac{2}{2} = 1$$$ and $$$a_1 = 12 \cdot 2 = 24$$$, making the array look as: [24, 1, 2]. </li><li> Pick $$$i = 3$$$ and $$$j = 1$$$. After performing a sequence of operations $$$a_3 = \frac{2}{2} = 1$$$ and $$$a_1 = 24 \cdot 2 = 48$$$, making the array look as: [48, 1, 1]. </li></ol><p>The final answer $$$48 + 1 + 1 = 50$$$.</p><p>In the third example test case there is no way to change the sum of elements, so the answer is $$$10$$$.</p></div>