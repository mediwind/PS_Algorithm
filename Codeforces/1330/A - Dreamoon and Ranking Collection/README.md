<h2><a href="https://codeforces.com/contest/1330/problem/A" target="_blank" rel="noopener noreferrer">1330A — Dreamoon and Ranking Collection</a></h2>

| | |
|---|---|
| **Difficulty** | 900 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1330A](https://codeforces.com/contest/1330/problem/A) |

## Topics
`implementation`

---

## Problem Statement

<div class="header"><div class="title">A. Dreamoon and Ranking Collection</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>Dreamoon is a big fan of the Codeforces contests.</p><p>One day, he claimed that he will collect all the places from $$$1$$$ to $$$54$$$ after two more rated contests. It's amazing!</p><p>Based on this, you come up with the following problem:</p><p>There is a person who participated in $$$n$$$ Codeforces rounds. His place in the first round is $$$a_1$$$, his place in the second round is $$$a_2$$$, ..., his place in the $$$n$$$-th round is $$$a_n$$$.</p><p>You are given a positive non-zero integer $$$x$$$.</p><p>Please, find the largest $$$v$$$ such that this person can collect all the places from $$$1$$$ to $$$v$$$ after $$$x$$$ more rated contests.</p><p>In other words, you need to find the largest $$$v$$$, such that it is possible, that after $$$x$$$ more rated contests, for each $$$1 \leq i \leq v$$$, there will exist a contest where this person took the $$$i$$$-th place.</p><p>For example, if $$$n=6$$$, $$$x=2$$$ and $$$a=[3,1,1,5,7,10]$$$ then answer is $$$v=5$$$, because if on the next two contest he will take places $$$2$$$ and $$$4$$$, then he will collect all places from $$$1$$$ to $$$5$$$, so it is possible to get $$$v=5$$$.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains an integer $$$t$$$ ($$$1 \leq t \leq 5$$$) denoting the number of test cases in the input.</p><p>Each test case contains two lines. The first line contains two integers $$$n, x$$$ ($$$1 \leq n, x \leq 100$$$). The second line contains $$$n$$$ positive non-zero integers $$$a_1, a_2, \ldots, a_n$$$ ($$$1 \leq a_i \leq 100$$$).</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case print one line containing the largest $$$v$$$, such that it is possible that after $$$x$$$ other contests, for each $$$1 \leq i \leq v$$$, there will exist a contest where this person took the $$$i$$$-th place.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id001235530408471911" id="id0003733201068810865" class="input-output-copier">Copy</div></div><pre id="id001235530408471911">5
6 2
3 1 1 5 7 10
1 100
100
11 1
1 1 1 1 1 1 1 1 1 1 1
1 1
1
4 57
80 60 40 20
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id00011971032394059833" id="id003242453258004595" class="input-output-copier">Copy</div></div><pre id="id00011971032394059833">5
101
2
2
60
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>The first test case is described in the statement.</p><p>In the second test case, the person has one hundred future contests, so he can take place $$$1,2,\ldots,99$$$ and place $$$101$$$ on them in some order, to collect places $$$1,2,\ldots,101$$$.</p></div>