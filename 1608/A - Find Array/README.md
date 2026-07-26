<h2><a href="https://codeforces.com/contest/1608/problem/A" target="_blank" rel="noopener noreferrer">1608A — Find Array</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1608A](https://codeforces.com/contest/1608/problem/A) |

## Topics
`constructive algorithms` `math`

---

## Problem Statement

<div class="header"><div class="title">A. Find Array</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>Given $$$n$$$, find any array $$$a_1, a_2, \ldots, a_n$$$ of integers such that all of the following conditions hold: </p><ul><li><p>$$$1 \le a_i \le 10^9$$$ for every $$$i$$$ from $$$1$$$ to $$$n$$$.</p></li><li><p>$$$a_1  \lt  a_2  \lt  \ldots  \lt a_n$$$</p></li><li><p>For every $$$i$$$ from $$$2$$$ to $$$n$$$, $$$a_i$$$ isn't divisible by $$$a_{i-1}$$$</p></li></ul><p>It can be shown that such an array always exists under the constraints of the problem.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 100$$$). Description of the test cases follows.</p><p>The only line of each test case contains a single integer $$$n$$$ ($$$1 \le n \le 1000$$$).</p><p>It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$10^4$$$.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case print $$$n$$$ integers $$$a_1, a_2, \ldots, a_n$$$ — the array you found. If there are multiple arrays satisfying all the conditions, print any of them.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0023133631495906448" id="id009704564625729357" class="input-output-copier">Copy</div></div><pre id="id0023133631495906448">3
1
2
7
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id008858459706867848" id="id008234582507704842" class="input-output-copier">Copy</div></div><pre id="id008858459706867848">1
2 3
111 1111 11111 111111 1111111 11111111 111111111</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first test case, array $$$[1]$$$ satisfies all the conditions.</p><p>In the second test case, array $$$[2, 3]$$$ satisfies all the conditions, as $$$2 \lt 3$$$ and $$$3$$$ is not divisible by $$$2$$$.</p><p>In the third test case, array $$$[111, 1111, 11111, 111111, 1111111, 11111111, 111111111]$$$ satisfies all the conditions, as it's increasing and $$$a_i$$$ isn't divisible by $$$a_{i-1}$$$ for any $$$i$$$ from $$$2$$$ to $$$7$$$.</p></div>