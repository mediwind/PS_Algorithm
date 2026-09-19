<h2><a href="https://codeforces.com/contest/1339/problem/A" target="_blank" rel="noopener noreferrer">1339A — Filling Diamonds</a></h2>

| | |
|---|---|
| **Difficulty** | 900 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1339A](https://codeforces.com/contest/1339/problem/A) |

## Topics
`brute force` `dp` `implementation` `math`

---

## Problem Statement

<div class="header"><div class="title">A. Filling Diamonds</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>You have integer $$$n$$$. Calculate how many ways are there to fully cover belt-like area of $$$4n-2$$$ triangles with diamond shapes. </p><p>Diamond shape consists of two triangles. You can move, rotate or flip the shape, but you cannot scale it. </p><p>$$$2$$$ coverings are different if some $$$2$$$ triangles are covered by the same diamond shape in one of them and by different diamond shapes in the other one.</p><p>Please look at pictures below for better understanding.</p><center> <img class="tex-graphics" src="https://espresso.codeforces.com/e0fea29aefdb21f54a0a87c19e1b6fa0aa7eefe7.png" style="max-width: 100.0%;max-height: 100.0%;"> On the left you can see the diamond shape you will use, and on the right you can see the area you want to fill.<p><img class="tex-graphics" src="https://espresso.codeforces.com/4a52d4205ad7630ef6dbd057d6c3fca8a820efa4.png" style="max-width: 100.0%;max-height: 100.0%;"> These are the figures of the area you want to fill for $$$n = 1, 2, 3, 4$$$. </p></center><p>You have to answer $$$t$$$ independent test cases.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains a single integer $$$t$$$ ($$$1 \le t \le 10^{4}$$$) — the number of test cases.</p><p>Each of the next $$$t$$$ lines contains a single integer $$$n$$$ ($$$1 \le n \le 10^{9}$$$).</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, print the number of ways to fully cover belt-like area of $$$4n-2$$$ triangles using diamond shape. It can be shown that under given constraints this number of ways doesn't exceed $$$10^{18}$$$.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id009734179883185037" id="id003285172279533424" class="input-output-copier">Copy</div></div><pre id="id009734179883185037">2
2
1
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id005257169773195229" id="id00951564403572632" class="input-output-copier">Copy</div></div><pre id="id005257169773195229">2
1
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first test case, there are the following $$$2$$$ ways to fill the area:</p><center> <img class="tex-graphics" src="https://espresso.codeforces.com/b172e94e9fd7027c24f4ebe2b9efecd6bb9837eb.png" style="max-width: 100.0%;max-height: 100.0%;"> </center><p>In the second test case, there is a unique way to fill the area:</p><center> <img class="tex-graphics" src="https://espresso.codeforces.com/540274c0723cb2c7a676bc5c963da672e107b608.png" style="max-width: 100.0%;max-height: 100.0%;"> </center></div>