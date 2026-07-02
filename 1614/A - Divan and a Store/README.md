<h2><a href="https://codeforces.com/contest/1614/problem/A" target="_blank" rel="noopener noreferrer">1614A — Divan and a Store</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1614A](https://codeforces.com/contest/1614/problem/A) |

## Topics
`brute force` `constructive algorithms` `greedy`

---

## Problem Statement

<div class="header"><div class="title">A. Divan and a Store</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>Businessman <span class="tex-font-style-it">Divan</span> loves chocolate! Today he came to a store to buy some chocolate. Like all businessmen, <span class="tex-font-style-it">Divan</span> knows the value of money, so he will not buy too expensive chocolate. At the same time, too cheap chocolate tastes bad, so he will not buy it as well.</p><p>The store he came to has $$$n$$$ different chocolate bars, and the price of the $$$i$$$-th chocolate bar is $$$a_i$$$ dollars. <span class="tex-font-style-it">Divan</span> considers a chocolate bar too expensive if it costs strictly more than $$$r$$$ dollars. Similarly, he considers a bar of chocolate to be too cheap if it costs strictly less than $$$l$$$ dollars. Divan will not buy too cheap or too expensive bars.</p><p><span class="tex-font-style-it">Divan</span> is not going to spend all his money on chocolate bars, so he will spend at most $$$k$$$ dollars on chocolates.</p><p>Please determine the maximum number of chocolate bars <span class="tex-font-style-it">Divan</span> can buy.</p></div><div class="input-specification"><div class="section-title">Input</div><p>Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 100$$$). Description of the test cases follows.</p><p>The description of each test case consists of two lines. The first line contains integers $$$n$$$, $$$l$$$, $$$r$$$, $$$k$$$ ($$$1 \le n \le 100$$$, $$$1 \le l \le r \le 10^9$$$, $$$1 \le k \le 10^9$$$) — the lowest acceptable price of a chocolate, the highest acceptable price of a chocolate and Divan's total budget, respectively.</p><p>The second line contains a sequence $$$a_1, a_2, \ldots, a_n$$$ ($$$1 \le a_i \le 10^9$$$) integers — the prices of chocolate bars in the store.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case print a single integer — the maximum number of chocolate bars <span class="tex-font-style-it">Divan</span> can buy.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id001630998013971886" id="id008446194555436475" class="input-output-copier">Copy</div></div><pre id="id001630998013971886">8
3 1 100 100
50 100 50
6 3 5 10
1 2 3 4 5 6
6 3 5 21
1 2 3 4 5 6
10 50 69 100
20 30 40 77 1 1 12 4 70 10000
3 50 80 30
20 60 70
10 2 7 100
2 2 2 2 2 7 7 7 7 7
4 1000000000 1000000000 1000000000
1000000000 1000000000 1000000000 1000000000
1 1 1 1
1
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id008896410750579185" id="id004820129350396516" class="input-output-copier">Copy</div></div><pre id="id008896410750579185">2
2
3
0
0
10
1
1
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first example <span class="tex-font-style-it">Divan</span> can buy chocolate bars $$$1$$$ and $$$3$$$ and spend $$$100$$$ dollars on them.</p><p>In the second example <span class="tex-font-style-it">Divan</span> can buy chocolate bars $$$3$$$ and $$$4$$$ and spend $$$7$$$ dollars on them.</p><p>In the third example <span class="tex-font-style-it">Divan</span> can buy chocolate bars $$$3$$$, $$$4$$$, and $$$5$$$ for $$$12$$$ dollars.</p><p>In the fourth example <span class="tex-font-style-it">Divan</span> cannot buy any chocolate bar because each of them is either too cheap or too expensive.</p><p>In the fifth example <span class="tex-font-style-it">Divan</span> cannot buy any chocolate bar because he considers the first bar too cheap, and has no budget for the second or third.</p><p>In the sixth example <span class="tex-font-style-it">Divan</span> can buy all the chocolate bars in the shop.</p></div>