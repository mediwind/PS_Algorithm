<h2><a href="https://codeforces.com/contest/1574/problem/A" target="_blank" rel="noopener noreferrer">1574A — Regular Bracket Sequences</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1574A](https://codeforces.com/contest/1574/problem/A) |

## Topics
`constructive algorithms`

---

## Problem Statement

<div class="header"><div class="title">A. Regular Bracket Sequences</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>512 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>A bracket sequence is a string containing only characters "<span class="tex-font-style-tt">(</span>" and "<span class="tex-font-style-tt">)</span>". A regular bracket sequence is a bracket sequence that can be transformed into a correct arithmetic expression by inserting characters "<span class="tex-font-style-tt">1</span>" and "<span class="tex-font-style-tt">+</span>" between the original characters of the sequence. For example, bracket sequences "<span class="tex-font-style-tt">()()</span>" and "<span class="tex-font-style-tt">(())</span>" are regular (the resulting expressions are: "<span class="tex-font-style-tt">(1)+(1)</span>" and "<span class="tex-font-style-tt">((1+1)+1)</span>"), and "<span class="tex-font-style-tt">)(</span>", "<span class="tex-font-style-tt">(</span>" and "<span class="tex-font-style-tt">)</span>" are not.</p><p>You are given an integer $$$n$$$. Your goal is to construct and print <span class="tex-font-style-bf">exactly $$$n$$$</span> different regular bracket sequences of length $$$2n$$$.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains one integer $$$t$$$ ($$$1 \le t \le 50$$$) — the number of test cases.</p><p>Each test case consists of one line containing one integer $$$n$$$ ($$$1 \le n \le 50$$$).</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, print $$$n$$$ lines, each containing a regular bracket sequence of length <span class="tex-font-style-bf">exactly $$$2n$$$</span>. All bracket sequences you output for a testcase should be different (though they may repeat in different test cases). If there are multiple answers, print any of them. It can be shown that it's always possible.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id001966146218833973" id="id008805264870540074" class="input-output-copier">Copy</div></div><pre id="id001966146218833973">3
3
1
3
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id004971892166528106" id="id005774231022147318" class="input-output-copier">Copy</div></div><pre id="id004971892166528106">()()()
((()))
(()())
()
((()))
(())()
()(())
</pre></div></div></div>