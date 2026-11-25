<h2><a href="https://codeforces.com/contest/1473/problem/B" target="_blank" rel="noopener noreferrer">1473B — String LCM</a></h2>

| | |
|---|---|
| **Difficulty** | 1000 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1473B](https://codeforces.com/contest/1473/problem/B) |

## Topics
`brute force` `math` `number theory` `strings`

---

## Problem Statement

<div class="header"><div class="title">B. String LCM</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>Let's define a multiplication operation between a string $$$a$$$ and a positive integer $$$x$$$: $$$a \cdot x$$$ is the string that is a result of writing $$$x$$$ copies of $$$a$$$ one after another. For example, "<span class="tex-font-style-tt">abc</span>" $$$\cdot~2~=$$$ "<span class="tex-font-style-tt">abcabc</span>", "<span class="tex-font-style-tt">a</span>" $$$\cdot~5~=$$$ "<span class="tex-font-style-tt">aaaaa</span>".</p><p>A string $$$a$$$ is divisible by another string $$$b$$$ if there exists an integer $$$x$$$ such that $$$b \cdot x = a$$$. For example, "<span class="tex-font-style-tt">abababab</span>" is divisible by "<span class="tex-font-style-tt">ab</span>", but is not divisible by "<span class="tex-font-style-tt">ababab</span>" or "<span class="tex-font-style-tt">aa</span>".</p><p>LCM of two strings $$$s$$$ and $$$t$$$ (defined as $$$LCM(s, t)$$$) is the shortest non-empty string that is divisible by both $$$s$$$ and $$$t$$$.</p><p>You are given two strings $$$s$$$ and $$$t$$$. Find $$$LCM(s, t)$$$ or report that it does not exist. It can be shown that if $$$LCM(s, t)$$$ exists, it is unique.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains one integer $$$q$$$ ($$$1 \le q \le 2000$$$) — the number of test cases.</p><p>Each test case consists of two lines, containing strings $$$s$$$ and $$$t$$$ ($$$1 \le |s|, |t| \le 20$$$). Each character in each of these strings is either '<span class="tex-font-style-tt">a</span>' or '<span class="tex-font-style-tt">b</span>'.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, print $$$LCM(s, t)$$$ if it exists; otherwise, print <span class="tex-font-style-tt">-1</span>. It can be shown that if $$$LCM(s, t)$$$ exists, it is unique.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id00247685523967068" id="id0047170935495997424" class="input-output-copier">Copy</div></div><pre id="id00247685523967068">3
baba
ba
aa
aaa
aba
ab
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id009640296637263673" id="id0033269668682649456" class="input-output-copier">Copy</div></div><pre id="id009640296637263673">baba
aaaaaa
-1
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first test case, "<span class="tex-font-style-tt">baba</span>" = "<span class="tex-font-style-tt">baba</span>" $$$\cdot~1~=$$$ "<span class="tex-font-style-tt">ba</span>" $$$\cdot~2$$$.</p><p>In the second test case, "<span class="tex-font-style-tt">aaaaaa</span>" = "<span class="tex-font-style-tt">aa</span>" $$$\cdot~3~=$$$ "<span class="tex-font-style-tt">aaa</span>" $$$\cdot~2$$$.</p></div>