<h2><a href="https://codeforces.com/contest/1613/problem/A" target="_blank" rel="noopener noreferrer">1613A — Long Comparison</a></h2>

| | |
|---|---|
| **Difficulty** | 900 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1613A](https://codeforces.com/contest/1613/problem/A) |

## Topics
`implementation` `math`

---

## Problem Statement

<div class="header"><div class="title">A. Long Comparison</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>Monocarp wrote down two numbers on a whiteboard. Both numbers follow a specific format: a positive integer $$$x$$$ with $$$p$$$ zeros appended to its end.</p><p>Now Monocarp asks you to compare these two numbers. Can you help him?</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains a single integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of testcases.</p><p>The first line of each testcase contains two integers $$$x_1$$$ and $$$p_1$$$ ($$$1 \le x_1 \le 10^6; 0 \le p_1 \le 10^6$$$) — the description of the first number.</p><p>The second line of each testcase contains two integers $$$x_2$$$ and $$$p_2$$$ ($$$1 \le x_2 \le 10^6; 0 \le p_2 \le 10^6$$$) — the description of the second number.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each testcase print the result of the comparison of the given two numbers. If the first number is smaller than the second one, print '<'. If the first number is greater than the second one, print '>'. If they are equal, print '='.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0008605394277450751" id="id008466647711311222" class="input-output-copier">Copy</div></div><pre id="id0008605394277450751">5
2 1
19 0
10 2
100 1
1999 0
2 3
1 0
1 0
99 0
1 2
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id005303224372034809" id="id008217488470160784" class="input-output-copier">Copy</div></div><pre id="id005303224372034809">>
=
<
=
<
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>The comparisons in the example are: $$$20  \gt  19$$$, $$$1000 = 1000$$$, $$$1999  \lt  2000$$$, $$$1 = 1$$$, $$$99  \lt  100$$$.</p></div>