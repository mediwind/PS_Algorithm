<h2><a href="https://codeforces.com/contest/1611/problem/B" target="_blank" rel="noopener noreferrer">1611B — Team Composition: Programmers and Mathematicians</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1611B](https://codeforces.com/contest/1611/problem/B) |

## Topics
`binary search` `constructive algorithms` `math`

---

## Problem Statement

<div class="header"><div class="title">B. Team Composition: Programmers and Mathematicians</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>The All-Berland Team Programming Contest will take place very soon. This year, teams of four are allowed to participate.</p><p>There are $$$a$$$ programmers and $$$b$$$ mathematicians at Berland State University. How many maximum teams can be made if:</p><ul> <li> each team must consist of exactly $$$4$$$ students, </li><li> teams of $$$4$$$ mathematicians or $$$4$$$ programmers are unlikely to perform well, so the decision was made not to compose such teams. </li></ul><p>Thus, each team must have at least one programmer <span class="tex-font-style-bf">and</span> at least one mathematician.</p><p>Print the required maximum number of teams. Each person can be a member of no more than one team.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains an integer $$$t$$$ ($$$1 \le t \le 10^4$$$) —the number of test cases.</p><p>This is followed by descriptions of $$$t$$$ sets, one per line. Each set is given by two integers $$$a$$$ and $$$b$$$ ($$$0 \le a,b \le 10^9$$$).</p></div><div class="output-specification"><div class="section-title">Output</div><p>Print $$$t$$$ lines. Each line must contain the answer to the corresponding set of input data — the required maximum number of teams.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id008058806691906701" id="id003371139156078855" class="input-output-copier">Copy</div></div><pre id="id008058806691906701">6
5 5
10 1
2 3
0 0
17 2
1000000000 1000000000
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id005961613746456271" id="id005015569730725846" class="input-output-copier">Copy</div></div><pre id="id005961613746456271">2
1
1
0
2
500000000
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first test case of the example, two teams can be composed. One way to compose two teams is to compose two teams of $$$2$$$ programmers and $$$2$$$ mathematicians.</p><p>In the second test case of the example, only one team can be composed: $$$3$$$ programmers and $$$1$$$ mathematician in the team.</p></div>