<h2><a href="https://codeforces.com/contest/1602/problem/A" target="_blank" rel="noopener noreferrer">1602A — Two Subsequences</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1602A](https://codeforces.com/contest/1602/problem/A) |

## Topics
`implementation`

---

## Problem Statement

<div class="header"><div class="title">A. Two Subsequences</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>You are given a string $$$s$$$. You need to find two non-empty strings $$$a$$$ and $$$b$$$ such that the following conditions are satisfied:</p><ol> <li> Strings $$$a$$$ and $$$b$$$ are both <span class="tex-font-style-bf">subsequences</span> of $$$s$$$. </li><li> For each index $$$i$$$, character $$$s_i$$$ of string $$$s$$$ must belong to <span class="tex-font-style-bf">exactly one</span> of strings $$$a$$$ or $$$b$$$. </li><li> String $$$a$$$ is <span class="tex-font-style-it">lexicographically</span> minimum possible; string $$$b$$$ may be any possible string. </li></ol><p>Given string $$$s$$$, print any valid $$$a$$$ and $$$b$$$.</p><p><span class="tex-font-style-bf">Reminder:</span></p><p>A string $$$a$$$ ($$$b$$$) is a <span class="tex-font-style-it">subsequence</span> of a string $$$s$$$ if $$$a$$$ ($$$b$$$) can be obtained from $$$s$$$ by deletion of several (possibly, zero) elements. For example, "<span class="tex-font-style-tt">dores</span>", "<span class="tex-font-style-tt">cf</span>", and "<span class="tex-font-style-tt">for</span>" are subsequences of "<span class="tex-font-style-tt">codeforces</span>", while "<span class="tex-font-style-tt">decor</span>" and "<span class="tex-font-style-tt">fork</span>" are not.</p><p>A string $$$x$$$ is <span class="tex-font-style-it">lexicographically smaller</span> than a string $$$y$$$ if and only if one of the following holds:</p><ul> <li> $$$x$$$ is a prefix of $$$y$$$, but $$$x \ne y$$$; </li><li> in the first position where $$$x$$$ and $$$y$$$ differ, the string $$$x$$$ has a letter that appears earlier in the alphabet than the corresponding letter in $$$y$$$. </li></ul></div><div class="input-specification"><div class="section-title">Input</div><p>Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 1000$$$). Description of the test cases follows.</p><p>The first and only line of each test case contains one string $$$s$$$ ($$$2 \le |s| \le 100$$$ where $$$|s|$$$ means the length of $$$s$$$). String $$$s$$$ consists of lowercase Latin letters.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, print the strings $$$a$$$ and $$$b$$$ that satisfy the given conditions. If there are multiple answers, print any.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id001500010468963855" id="id004193176766114606" class="input-output-copier">Copy</div></div><pre id="id001500010468963855">3
fc
aaaa
thebrightboiler
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id002514415753735133" id="id006987152484814481" class="input-output-copier">Copy</div></div><pre id="id002514415753735133">c f
a aaa
b therightboiler
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first test case, there are only two choices: either $$$a =$$$ <span class="tex-font-style-tt">f</span> and $$$b = $$$ <span class="tex-font-style-tt">c</span> or $$$a = $$$ <span class="tex-font-style-tt">c</span> and $$$b = $$$ <span class="tex-font-style-tt">f</span>. And $$$a = $$$<span class="tex-font-style-tt">c</span> is lexicographically smaller than $$$a = $$$ <span class="tex-font-style-tt">f</span>.</p><p>In the second test case, <span class="tex-font-style-tt">a</span> is the only character in the string.</p><p>In the third test case, it can be proven that <span class="tex-font-style-tt">b</span> is the lexicographically smallest subsequence of $$$s$$$. The second string can be of two variants; one of them is given here.</p></div>