<h2><a href="https://codeforces.com/contest/1494/problem/A" target="_blank" rel="noopener noreferrer">1494A — ABC String</a></h2>

| | |
|---|---|
| **Difficulty** | 900 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1494A](https://codeforces.com/contest/1494/problem/A) |

## Topics
`bitmasks` `brute force` `implementation`

---

## Problem Statement

<div class="header"><div class="title">A. ABC String</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>You are given a string $$$a$$$, consisting of $$$n$$$ characters, $$$n$$$ is even. For each $$$i$$$ from $$$1$$$ to $$$n$$$ $$$a_i$$$ is one of '<span class="tex-font-style-tt">A</span>', '<span class="tex-font-style-tt">B</span>' or '<span class="tex-font-style-tt">C</span>'.</p><p>A bracket sequence is a string containing only characters "<span class="tex-font-style-tt">(</span>" and "<span class="tex-font-style-tt">)</span>". A regular bracket sequence is a bracket sequence that can be transformed into a correct arithmetic expression by inserting characters "<span class="tex-font-style-tt">1</span>" and "<span class="tex-font-style-tt">+</span>" between the original characters of the sequence. For example, bracket sequences "<span class="tex-font-style-tt">()()</span>" and "<span class="tex-font-style-tt">(())</span>" are regular (the resulting expressions are: "<span class="tex-font-style-tt">(1)+(1)</span>" and "<span class="tex-font-style-tt">((1+1)+1)</span>"), and "<span class="tex-font-style-tt">)(</span>", "<span class="tex-font-style-tt">(</span>" and "<span class="tex-font-style-tt">)</span>" are not.</p><p>You want to find a string $$$b$$$ that consists of $$$n$$$ characters such that: </p><ul> <li> $$$b$$$ is a regular bracket sequence; </li><li> if for some $$$i$$$ and $$$j$$$ ($$$1 \le i, j \le n$$$) $$$a_i=a_j$$$, then $$$b_i=b_j$$$. </li></ul><p>In other words, you want to replace all occurrences of '<span class="tex-font-style-tt">A</span>' with the same type of bracket, then all occurrences of '<span class="tex-font-style-tt">B</span>' with the same type of bracket and all occurrences of '<span class="tex-font-style-tt">C</span>' with the same type of bracket.</p><p>Your task is to determine if such a string $$$b$$$ exists.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains a single integer $$$t$$$ ($$$1 \le t \le 1000$$$) — the number of testcases.</p><p>Then the descriptions of $$$t$$$ testcases follow.</p><p>The only line of each testcase contains a string $$$a$$$. $$$a$$$ consists only of uppercase letters '<span class="tex-font-style-tt">A</span>', '<span class="tex-font-style-tt">B</span>' and '<span class="tex-font-style-tt">C</span>'. Let $$$n$$$ be the length of $$$a$$$. It is guaranteed that $$$n$$$ is even and $$$2 \le n \le 50$$$.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each testcase print "<span class="tex-font-style-tt">YES</span>" if there exists such a string $$$b$$$ that: </p><ul> <li> $$$b$$$ is a regular bracket sequence; </li><li> if for some $$$i$$$ and $$$j$$$ ($$$1 \le i, j \le n$$$) $$$a_i=a_j$$$, then $$$b_i=b_j$$$. </li></ul><p>Otherwise, print "<span class="tex-font-style-tt">NO</span>".</p><p>You may print every letter in any case you want (so, for example, the strings <span class="tex-font-style-tt">yEs</span>, <span class="tex-font-style-tt">yes</span>, <span class="tex-font-style-tt">Yes</span> and <span class="tex-font-style-tt">YES</span> are all recognized as positive answer).</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id008243047148274295" id="id006581506081208814" class="input-output-copier">Copy</div></div><pre id="id008243047148274295">4
AABBAC
CACA
BBBBAC
ABCA
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id0020909124187278605" id="id00016356190369992696" class="input-output-copier">Copy</div></div><pre id="id0020909124187278605">YES
YES
NO
NO
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first testcase one of the possible strings $$$b$$$ is "<span class="tex-font-style-tt">(())()</span>".</p><p>In the second testcase one of the possible strings $$$b$$$ is "<span class="tex-font-style-tt">()()</span>".</p></div>