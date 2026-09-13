<h2><a href="https://codeforces.com/contest/1401/problem/A" target="_blank" rel="noopener noreferrer">1401A — Distance and Axis</a></h2>

| | |
|---|---|
| **Difficulty** | 900 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1401A](https://codeforces.com/contest/1401/problem/A) |

## Topics
`constructive algorithms` `math`

---

## Problem Statement

<div class="header"><div class="title">A. Distance and Axis</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>We have a point $$$A$$$ with coordinate $$$x = n$$$ on $$$OX$$$-axis. We'd like to find an <span class="tex-font-style-it">integer point</span> $$$B$$$ (also on $$$OX$$$-axis), such that the <span class="tex-font-style-it">absolute difference</span> between the distance from $$$O$$$ to $$$B$$$ and the distance from $$$A$$$ to $$$B$$$ is equal to $$$k$$$.</p><center> <img class="tex-graphics" src="https://espresso.codeforces.com/67969afa374236d990021a6f450f73f7a21cbb28.png" style="zoom: 100.0%;max-width: 100.0%;max-height: 100.0%;"> <span class="tex-font-size-small">The description of the first test case.</span> </center><p>Since sometimes it's impossible to find such point $$$B$$$, we can, in one step, increase or decrease the coordinate of $$$A$$$ by $$$1$$$. What is the minimum number of steps we should do to make such point $$$B$$$ exist?</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains one integer $$$t$$$ ($$$1 \le t \le 6000$$$) — the number of test cases.</p><p>The only line of each test case contains two integers $$$n$$$ and $$$k$$$ ($$$0 \le n, k \le 10^6$$$) — the initial position of point $$$A$$$ and desirable absolute difference.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, print the minimum number of steps to make point $$$B$$$ exist.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id009996739325733207" id="id009628824928495524" class="input-output-copier">Copy</div></div><pre id="id009996739325733207">6
4 0
5 8
0 1000000
0 0
1 0
1000000 1000000
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id0021113866938400705" id="id00028149297871151724" class="input-output-copier">Copy</div></div><pre id="id0021113866938400705">0
3
1000000
0
1
0
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first test case (picture above), if we set the coordinate of $$$B$$$ as $$$2$$$ then the absolute difference will be equal to $$$|(2 - 0) - (4 - 2)| = 0$$$ and we don't have to move $$$A$$$. So the answer is $$$0$$$.</p><p>In the second test case, we can increase the coordinate of $$$A$$$ by $$$3$$$ and set the coordinate of $$$B$$$ as $$$0$$$ or $$$8$$$. The absolute difference will be equal to $$$|8 - 0| = 8$$$, so the answer is $$$3$$$.</p><center> <img class="tex-graphics" src="https://espresso.codeforces.com/1d1cb8c77a6097b153360ea35724f1924359c1cd.png" style="zoom: 100.0%;max-width: 100.0%;max-height: 100.0%;"> </center></div>