<h2><a href="https://codeforces.com/contest/1619/problem/B" target="_blank" rel="noopener noreferrer">1619B — Squares and Cubes</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1619B](https://codeforces.com/contest/1619/problem/B) |

## Topics
`implementation` `math`

---

## Problem Statement

<div class="header"><div class="title">B. Squares and Cubes</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>Polycarp likes squares and cubes of positive integers. Here is the beginning of the sequence of numbers he likes: $$$1$$$, $$$4$$$, $$$8$$$, $$$9$$$, ....</p><p>For a given number $$$n$$$, count the number of integers from $$$1$$$ to $$$n$$$ that Polycarp likes. In other words, find the number of such $$$x$$$ that $$$x$$$ is a square of a positive integer number or a cube of a positive integer number (or both a square and a cube simultaneously).</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains an integer $$$t$$$ ($$$1 \le t \le 20$$$) — the number of test cases.</p><p>Then $$$t$$$ lines contain the test cases, one per line. Each of the lines contains one integer $$$n$$$ ($$$1 \le n \le 10^9$$$).</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, print the answer you are looking for — the number of integers from $$$1$$$ to $$$n$$$ that Polycarp likes.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0023073511663682356" id="id005064874707707417" class="input-output-copier">Copy</div></div><pre id="id0023073511663682356">6
10
1
25
1000000000
999999999
500000000
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id005642206323559321" id="id002007517946724836" class="input-output-copier">Copy</div></div><pre id="id005642206323559321">4
1
6
32591
32590
23125
</pre></div></div></div>