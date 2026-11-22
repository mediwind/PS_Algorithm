<h2><a href="https://codeforces.com/contest/1613/problem/B" target="_blank" rel="noopener noreferrer">1613B — Absent Remainder</a></h2>

| | |
|---|---|
| **Difficulty** | 1000 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1613B](https://codeforces.com/contest/1613/problem/B) |

## Topics
`greedy` `implementation` `sortings`

---

## Problem Statement

<div class="header"><div class="title">B. Absent Remainder</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>You are given a sequence $$$a_1, a_2, \dots, a_n$$$ consisting of $$$n$$$ pairwise distinct positive integers.</p><p>Find $$$\left\lfloor \frac n 2 \right\rfloor$$$ different pairs of integers $$$x$$$ and $$$y$$$ such that: </p><ul> <li> $$$x \neq y$$$; </li><li> $$$x$$$ and $$$y$$$ appear in $$$a$$$; </li><li> $$$x~mod~y$$$ doesn't appear in $$$a$$$. </li></ul><p>Note that some $$$x$$$ or $$$y$$$ can belong to multiple pairs.</p><p>$$$\lfloor x \rfloor$$$ denotes the floor function — the largest integer less than or equal to $$$x$$$. $$$x~mod~y$$$ denotes the remainder from dividing $$$x$$$ by $$$y$$$.</p><p>If there are multiple solutions, print any of them. It can be shown that at least one solution always exists.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains a single integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of testcases.</p><p>The first line of each testcase contains a single integer $$$n$$$ ($$$2 \le n \le 2 \cdot 10^5$$$) — the length of the sequence.</p><p>The second line of each testcase contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ ($$$1 \le a_i \le 10^6$$$).</p><p>All numbers in the sequence are pairwise distinct. The sum of $$$n$$$ over all testcases doesn't exceed $$$2 \cdot 10^5$$$.</p></div><div class="output-specification"><div class="section-title">Output</div><p>The answer for each testcase should contain $$$\left\lfloor \frac n 2 \right\rfloor$$$ different pairs of integers $$$x$$$ and $$$y$$$ such that $$$x \neq y$$$, $$$x$$$ and $$$y$$$ appear in $$$a$$$ and $$$x~mod~y$$$ doesn't appear in $$$a$$$. Print the pairs one after another.</p><p>You can print the pairs in any order. However, the order of numbers in the pair should be exactly such that the first number is $$$x$$$ and the second number is $$$y$$$. All pairs should be pairwise distinct.</p><p>If there are multiple solutions, print any of them.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id008809891182955254" id="id0047409991208381386" class="input-output-copier">Copy</div></div><pre id="id008809891182955254">4
2
1 4
4
2 8 3 4
5
3 8 5 9 7
6
2 7 5 3 4 8
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id0020888502365361605" id="id009194787468517898" class="input-output-copier">Copy</div></div><pre id="id0020888502365361605">4 1
8 2
8 4
9 5
7 5
8 7
4 3
5 2</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first testcase there are only two pairs: $$$(1, 4)$$$ and $$$(4, 1)$$$. $$$\left\lfloor \frac 2 2 \right\rfloor=1$$$, so we have to find one pair. $$$1~mod~4=1$$$, and $$$1$$$ appears in $$$a$$$, so that pair is invalid. Thus, the only possible answer is a pair $$$(4, 1)$$$.</p><p>In the second testcase, we chose pairs $$$8~mod~2=0$$$ and $$$8~mod~4=0$$$. $$$0$$$ doesn't appear in $$$a$$$, so that answer is valid. There are multiple possible answers for that testcase.</p><p>In the third testcase, the chosen pairs are $$$9~mod~5=4$$$ and $$$7~mod~5=2$$$. Neither $$$4$$$, nor $$$2$$$, appears in $$$a$$$, so that answer is valid.</p></div>