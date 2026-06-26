<h2><a href="https://codeforces.com/contest/1514/problem/A" target="_blank" rel="noopener noreferrer">1514A — Perfectly Imperfect Array</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1514A](https://codeforces.com/contest/1514/problem/A) |

## Topics
`math` `number theory`

---

## Problem Statement

<div class="header"><div class="title">A. Perfectly Imperfect Array</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>Given an array $$$a$$$ of length $$$n$$$, tell us whether it has a non-empty subsequence such that the product of its elements is <span class="tex-font-style-bf">not</span> a perfect square.</p><p>A sequence $$$b$$$ is a subsequence of an array $$$a$$$ if $$$b$$$ can be obtained from $$$a$$$ by deleting some (possibly zero) elements.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains an integer $$$t$$$ ($$$1 \le t \le 100$$$) — the number of test cases. The description of the test cases follows.</p><p>The first line of each test case contains an integer $$$n$$$ ($$$1 \le n \le 100$$$) — the length of the array $$$a$$$.</p><p>The second line of each test case contains $$$n$$$ integers $$$a_1$$$, $$$a_2$$$, $$$\ldots$$$, $$$a_{n}$$$ ($$$1 \le a_i \le 10^4$$$) — the elements of the array $$$a$$$.</p></div><div class="output-specification"><div class="section-title">Output</div><p>If there's a subsequence of $$$a$$$ whose product isn't a perfect square, print "<span class="tex-font-style-tt">YES</span>". Otherwise, print "<span class="tex-font-style-tt">NO</span>".</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id008062083203923759" id="id001426910432692744" class="input-output-copier">Copy</div></div><pre id="id008062083203923759">2
3
1 5 4
2
100 10000
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id007298759099477196" id="id0015927751155263847" class="input-output-copier">Copy</div></div><pre id="id007298759099477196">YES
NO
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first example, the product of the whole array ($$$20$$$) isn't a perfect square.</p><p>In the second example, all subsequences have a perfect square product.</p></div>