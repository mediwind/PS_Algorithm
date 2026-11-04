<h2><a href="https://codeforces.com/contest/1238/problem/A" target="_blank" rel="noopener noreferrer">1238A — Prime Subtraction</a></h2>

| | |
|---|---|
| **Difficulty** | 900 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1238A](https://codeforces.com/contest/1238/problem/A) |

## Topics
`math` `number theory`

---

## Problem Statement

<div class="header"><div class="title">A. Prime Subtraction</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>You are given two integers $$$x$$$ and $$$y$$$ (it is guaranteed that $$$x  \gt  y$$$). You may choose any <span class="tex-font-style-it">prime</span> integer $$$p$$$ and subtract it any number of times from $$$x$$$. Is it possible to make $$$x$$$ equal to $$$y$$$?</p><p>Recall that a <span class="tex-font-style-it">prime</span> number is a positive integer that has exactly two positive divisors: $$$1$$$ and this integer itself. The sequence of prime numbers starts with $$$2$$$, $$$3$$$, $$$5$$$, $$$7$$$, $$$11$$$.</p><p>Your program should solve $$$t$$$ independent test cases.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains one integer $$$t$$$ ($$$1 \le t \le 1000$$$) — the number of test cases.</p><p>Then $$$t$$$ lines follow, each describing a test case. Each line contains two integers $$$x$$$ and $$$y$$$ ($$$1 \le y  \lt  x \le 10^{18}$$$).</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, print <span class="tex-font-style-tt">YES</span> if it is possible to choose a prime number $$$p$$$ and subtract it any number of times from $$$x$$$ so that $$$x$$$ becomes equal to $$$y$$$. Otherwise, print <span class="tex-font-style-tt">NO</span>.</p><p>You may print every letter in any case you want (so, for example, the strings <span class="tex-font-style-tt">yEs</span>, <span class="tex-font-style-tt">yes</span>, <span class="tex-font-style-tt">Yes</span>, and <span class="tex-font-style-tt">YES</span> will all be recognized as positive answer).</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0018514974199092427" id="id004970914670781844" class="input-output-copier">Copy</div></div><pre id="id0018514974199092427">4
100 98
42 32
1000000000000000000 1
41 40
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id007035010265022891" id="id007174539038908431" class="input-output-copier">Copy</div></div><pre id="id007035010265022891">YES
YES
YES
NO
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first test of the example you may choose $$$p = 2$$$ and subtract it once.</p><p>In the second test of the example you may choose $$$p = 5$$$ and subtract it twice. Note that you cannot choose $$$p = 7$$$, subtract it, then choose $$$p = 3$$$ and subtract it again.</p><p>In the third test of the example you may choose $$$p = 3$$$ and subtract it $$$333333333333333333$$$ times.</p></div>