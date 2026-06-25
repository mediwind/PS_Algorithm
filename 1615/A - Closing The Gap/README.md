<h2><a href="https://codeforces.com/contest/1615/problem/A" target="_blank" rel="noopener noreferrer">1615A — Closing The Gap</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1615A](https://codeforces.com/contest/1615/problem/A) |

## Topics
`greedy` `math`

---

## Problem Statement

<div class="header"><div class="title">A. Closing The Gap</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>There are $$$n$$$ block towers in a row, where tower $$$i$$$ has a height of $$$a_i$$$. You're part of a building crew, and you want to make the buildings look as nice as possible. In a single day, you can perform the following operation:</p><ul> <li> Choose two indices $$$i$$$ and $$$j$$$ ($$$1 \leq i, j \leq n$$$; $$$i \neq j$$$), and move a block from tower $$$i$$$ to tower $$$j$$$. This essentially decreases $$$a_i$$$ by $$$1$$$ and increases $$$a_j$$$ by $$$1$$$. </li></ul><p>You think the ugliness of the buildings is the height difference between the tallest and shortest buildings. Formally, the ugliness is defined as $$$\max(a)-\min(a)$$$. </p><p>What's the minimum possible ugliness you can achieve, after any number of days?</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains one integer $$$t$$$ ($$$1 \leq t \leq 1000$$$) — the number of test cases. Then $$$t$$$ cases follow.</p><p>The first line of each test case contains one integer $$$n$$$ ($$$2 \leq n \leq 100$$$) — the number of buildings.</p><p>The second line of each test case contains $$$n$$$ space separated integers $$$a_1, a_2, \ldots, a_n$$$ ($$$1 \leq a_i \leq 10^7$$$) — the heights of the buildings.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, output a single integer — the minimum possible ugliness of the buildings.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0007305085326210548" id="id007807699748149932" class="input-output-copier">Copy</div></div><pre id="id0007305085326210548">3
3
10 10 10
4
3 2 1 2
5
1 2 3 1 5
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id006252352617998775" id="id006858776991036186" class="input-output-copier">Copy</div></div><pre id="id006252352617998775">0
0
1
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first test case, the ugliness is already $$$0$$$.</p><p>In the second test case, you should do one operation, with $$$i = 1$$$ and $$$j = 3$$$. The new heights will now be $$$[2, 2, 2, 2]$$$, with an ugliness of $$$0$$$.</p><p>In the third test case, you may do three operations: </p><ol> <li> with $$$i = 3$$$ and $$$j = 1$$$. The new array will now be $$$[2, 2, 2, 1, 5]$$$, </li><li> with $$$i = 5$$$ and $$$j = 4$$$. The new array will now be $$$[2, 2, 2, 2, 4]$$$, </li><li> with $$$i = 5$$$ and $$$j = 3$$$. The new array will now be $$$[2, 2, 3, 2, 3]$$$. </li></ol> The resulting ugliness is $$$1$$$. It can be proven that this is the minimum possible ugliness for this test.</div>