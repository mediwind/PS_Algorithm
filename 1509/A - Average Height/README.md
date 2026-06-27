<h2><a href="https://codeforces.com/contest/1509/problem/A" target="_blank" rel="noopener noreferrer">1509A — Average Height</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1509A](https://codeforces.com/contest/1509/problem/A) |

## Topics
`constructive algorithms`

---

## Problem Statement

<div class="header"><div class="title">A. Average Height</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>Sayaka Saeki is a member of the student council, which has $$$n$$$ other members (excluding Sayaka). The $$$i$$$-th member has a height of $$$a_i$$$ millimeters.</p><p>It's the end of the school year and Sayaka wants to take a picture of all other members of the student council. Being the hard-working and perfectionist girl as she is, she wants to arrange all the members in a line such that the amount of <span class="tex-font-style-it">photogenic</span> consecutive pairs of members is <span class="tex-font-style-bf">as large as possible</span>.</p><p>A pair of two consecutive members $$$u$$$ and $$$v$$$ on a line is considered <span class="tex-font-style-it">photogenic</span> if their average height is an integer, i.e. $$$\frac{a_u + a_v}{2}$$$ is an integer.</p><p>Help Sayaka arrange the other members to <span class="tex-font-style-bf">maximize</span> the number of photogenic consecutive pairs.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains a single integer $$$t$$$ ($$$1\le t\le 500$$$) — the number of test cases.</p><p>The first line of each test case contains a single integer $$$n$$$ ($$$2 \le n \le 2000$$$)  — the number of other council members.</p><p>The second line of each test case contains $$$n$$$ integers $$$a_1$$$, $$$a_2$$$, ..., $$$a_n$$$ ($$$1 \le a_i \le 2 \cdot 10^5$$$)  — the heights of each of the other members in millimeters.</p><p>It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2000$$$.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, output on one line $$$n$$$ integers representing the heights of the other members in the order, which gives the largest number of photogenic consecutive pairs. If there are multiple such orders, output any of them.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0005869324704942347" id="id008952623034366283" class="input-output-copier">Copy</div></div><pre id="id0005869324704942347">4
3
1 1 2
3
1 1 1
8
10 9 13 15 3 16 9 13
2
18 9
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id0048140151288727195" id="id006327230949334319" class="input-output-copier">Copy</div></div><pre id="id0048140151288727195">1 1 2 
1 1 1 
13 9 13 15 3 9 16 10 
9 18 
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first test case, there is one photogenic pair: $$$(1, 1)$$$ is photogenic, as $$$\frac{1+1}{2}=1$$$ is integer, while $$$(1, 2)$$$ isn't, as $$$\frac{1+2}{2}=1.5$$$ isn't integer.</p><p>In the second test case, both pairs are photogenic.</p></div>