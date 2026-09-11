<h2><a href="https://codeforces.com/contest/1420/problem/A" target="_blank" rel="noopener noreferrer">1420A — Cubes Sorting</a></h2>

| | |
|---|---|
| **Difficulty** | 900 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1420A](https://codeforces.com/contest/1420/problem/A) |

## Topics
`math` `sortings`

---

## Problem Statement

<div class="header"><div class="title">A. Cubes Sorting</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><div class="epigraph"><div class="epigraph-text"> <span class="tex-font-size-small"> For god's sake, you're boxes with legs! It is literally your only purpose! Walking onto buttons! How can you not do the one thing you were designed for?<p>Oh, that's funny, is it? Oh it's funny? Because we've been at this for twelve hours and you haven't solved it either, so I don't know why you're laughing. You've got one hour! Solve it! </p></span> </div></div><p>Wheatley decided to try to make a test chamber. He made a nice test chamber, but there was only one detail absent — cubes.</p><p>For completing the chamber Wheatley needs $$$n$$$ cubes. $$$i$$$-th cube has a volume $$$a_i$$$.</p><p>Wheatley has to place cubes in such a way that they would be sorted in a non-decreasing order by their volume. Formally, for each $$$i \gt 1$$$, $$$a_{i-1} \le a_i$$$ must hold.</p><p>To achieve his goal, Wheatley can exchange two <span class="tex-font-style-bf">neighbouring</span> cubes. It means that for any $$$i \gt 1$$$ you can exchange cubes on positions $$$i-1$$$ and $$$i$$$.</p><p>But there is a problem: Wheatley is very impatient. If Wheatley needs more than $$$\frac{n \cdot (n-1)}{2}-1$$$ exchange operations, he won't do this boring work.</p><p>Wheatly wants to know: can cubes be sorted under this conditions?</p></div><div class="input-specification"><div class="section-title">Input</div><p>Each test contains multiple test cases.</p><p>The first line contains one positive integer $$$t$$$ ($$$1 \le t \le 1000$$$), denoting the number of test cases. Description of the test cases follows.</p><p>The first line of each test case contains one positive integer $$$n$$$ ($$$2 \le n \le 5 \cdot 10^4$$$) — number of cubes.</p><p>The second line contains $$$n$$$ positive integers $$$a_i$$$ ($$$1 \le a_i \le 10^9$$$) — volumes of cubes.</p><p>It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$10^5$$$.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, print a word in a single line: "<span class="tex-font-style-tt">YES</span>" (without quotation marks) if the cubes can be sorted and "<span class="tex-font-style-tt">NO</span>" (without quotation marks) otherwise.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id002742968831507222" id="id009666809548112922" class="input-output-copier">Copy</div></div><pre id="id002742968831507222">3
5
5 3 2 1 4
6
2 2 2 2 2 2
2
2 1
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id007264955105311601" id="id006689603512264031" class="input-output-copier">Copy</div></div><pre id="id007264955105311601">YES
YES
NO
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first test case it is possible to sort all the cubes in $$$7$$$ exchanges.</p><p>In the second test case the cubes are already sorted.</p><p>In the third test case we can make $$$0$$$ exchanges, but the cubes are not sorted yet, so the answer is "<span class="tex-font-style-tt">NO</span>".</p></div>