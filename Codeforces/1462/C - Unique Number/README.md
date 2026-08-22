<h2><a href="https://codeforces.com/contest/1462/problem/C" target="_blank" rel="noopener noreferrer">1462C — Unique Number</a></h2>

| | |
|---|---|
| **Difficulty** | 900 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1462C](https://codeforces.com/contest/1462/problem/C) |

## Topics
`brute force` `greedy` `math`

---

## Problem Statement

<div class="header"><div class="title">C. Unique Number</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>You are given a positive number $$$x$$$. Find the smallest positive integer number that has the sum of digits equal to $$$x$$$ and all digits are <span class="tex-font-style-bf">distinct</span> (unique).</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains a single positive integer $$$t$$$ ($$$1 \le t \le 50$$$) — the number of test cases in the test. Then $$$t$$$ test cases follow.</p><p>Each test case consists of a single integer number $$$x$$$ ($$$1 \le x \le 50$$$).</p></div><div class="output-specification"><div class="section-title">Output</div><p>Output $$$t$$$ answers to the test cases:</p><ul> <li> if a positive integer number with the sum of digits equal to $$$x$$$ and all digits are different exists, print the smallest such number; </li><li> otherwise print <span class="tex-font-style-tt">-1</span>. </li></ul></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id006045220622004297" id="id0027897921689751126" class="input-output-copier">Copy</div></div><pre id="id006045220622004297">4
1
5
15
50
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id0025528852600575835" id="id0020207374931517863" class="input-output-copier">Copy</div></div><pre id="id0025528852600575835">1
5
69
-1
</pre></div></div></div>