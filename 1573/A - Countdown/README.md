<h2><a href="https://codeforces.com/contest/1573/problem/A" target="_blank" rel="noopener noreferrer">1573A — Countdown</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1573A](https://codeforces.com/contest/1573/problem/A) |

## Topics
`greedy`

---

## Problem Statement

<div class="header"><div class="title">A. Countdown</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>You are given a digital clock with $$$n$$$ digits. Each digit shows an integer from $$$0$$$ to $$$9$$$, so the whole clock shows an integer from $$$0$$$ to $$$10^n-1$$$. The clock will show leading zeroes if the number is smaller than $$$10^{n-1}$$$.</p><p>You want the clock to show $$$0$$$ with as few operations as possible. In an operation, you can do one of the following: </p><ul> <li> decrease the number on the clock by $$$1$$$, or </li><li> swap two digits (you can choose which digits to swap, and they don't have to be adjacent). </li></ul><p>Your task is to determine the minimum number of operations needed to make the clock show $$$0$$$.</p></div><div class="input-specification"><div class="section-title">Input</div><p>Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^3$$$).</p><p>The first line of each test case contains a single integer $$$n$$$ ($$$1 \le n \le 100$$$) — number of digits on the clock.</p><p>The second line of each test case contains a string of $$$n$$$ digits $$$s_1, s_2, \ldots, s_n$$$ ($$$0 \le s_1, s_2, \ldots, s_n \le 9$$$) — the number on the clock.</p><p>Note: If the number is smaller than $$$10^{n-1}$$$ the clock will show leading zeroes.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, print one integer: the minimum number of operations needed to make the clock show $$$0$$$.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0025082994203270015" id="id0004900599538233108" class="input-output-copier">Copy</div></div><pre id="id0025082994203270015">7
3
007
4
1000
5
00000
3
103
4
2020
9
123456789
30
001678294039710047203946100020
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id008564881043697821" id="id008767691769323391" class="input-output-copier">Copy</div></div><pre id="id008564881043697821">7
2
0
5
6
53
115
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first example, it's optimal to just decrease the number $$$7$$$ times.</p><p>In the second example, we can first swap the first and last position and then decrease the number by $$$1$$$.</p><p>In the third example, the clock already shows $$$0$$$, so we don't have to perform any operations.</p></div>