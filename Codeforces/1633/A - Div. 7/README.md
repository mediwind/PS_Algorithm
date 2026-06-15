<h2><a href="https://codeforces.com/contest/1633/problem/A" target="_blank" rel="noopener noreferrer">1633A — Div. 7</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1633A](https://codeforces.com/contest/1633/problem/A) |

## Topics
`brute force`

---

## Problem Statement

<div class="header"><div class="title">A. Div. 7</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>512 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>You are given an integer $$$n$$$. You have to change the minimum number of digits in it in such a way that the resulting number <span class="tex-font-style-bf">does not have any leading zeroes</span> and <span class="tex-font-style-bf">is divisible by $$$7$$$</span>.</p><p>If there are multiple ways to do it, print any of them. If the given number is already divisible by $$$7$$$, leave it unchanged.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains one integer $$$t$$$ ($$$1 \le t \le 990$$$) — the number of test cases.</p><p>Then the test cases follow, each test case consists of one line containing one integer $$$n$$$ ($$$10 \le n \le 999$$$).</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, print one integer without any leading zeroes — the result of your changes (i. e. the integer that is divisible by $$$7$$$ and can be obtained by changing the minimum possible number of digits in $$$n$$$).</p><p>If there are multiple ways to apply changes, print any resulting number. If the given number is already divisible by $$$7$$$, just print it.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0010395958333444622" id="id006373252694794305" class="input-output-copier">Copy</div></div><pre id="id0010395958333444622"><div class="test-example-line test-example-line-even test-example-line-0">3</div><div class="test-example-line test-example-line-odd test-example-line-1">42</div><div class="test-example-line test-example-line-even test-example-line-2">23</div><div class="test-example-line test-example-line-odd test-example-line-3">377</div></pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id00936623488007657" id="id0092305709440332" class="input-output-copier">Copy</div></div><pre id="id00936623488007657">42
28
777
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first test case of the example, $$$42$$$ is already divisible by $$$7$$$, so there's no need to change it.</p><p>In the second test case of the example, there are multiple answers — $$$28$$$, $$$21$$$ or $$$63$$$.</p><p>In the third test case of the example, other possible answers are $$$357$$$, $$$371$$$ and $$$378$$$. Note that you <span class="tex-font-style-bf">cannot</span> print $$$077$$$ or $$$77$$$.</p></div>