<h2><a href="https://codeforces.com/contest/1436/problem/B" target="_blank" rel="noopener noreferrer">1436B — Prime Square</a></h2>

| | |
|---|---|
| **Difficulty** | 900 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1436B](https://codeforces.com/contest/1436/problem/B) |

## Topics
`constructive algorithms` `math`

---

## Problem Statement

<div class="header"><div class="title">B. Prime Square</div><div class="time-limit"><div class="property-title">time limit per test</div>1.5 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>Sasha likes investigating different math objects, for example, magic squares. But Sasha understands that magic squares have already been studied by hundreds of people, so he sees no sense of studying them further. Instead, he invented his own type of square — a prime square. </p><p>A square of size $$$n \times n$$$ is called prime if the following three conditions are held simultaneously: </p><ul> <li> all numbers on the square are non-negative integers not exceeding $$$10^5$$$; </li><li> there are no prime numbers in the square; </li><li> sums of integers in each row and each column are prime numbers. </li></ul><p>Sasha has an integer $$$n$$$. He asks you to find any prime square of size $$$n \times n$$$. Sasha is absolutely sure such squares exist, so just help him!</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains a single integer $$$t$$$ ($$$1 \le t \le 10$$$) — the number of test cases.</p><p>Each of the next $$$t$$$ lines contains a single integer $$$n$$$ ($$$2 \le n \le 100$$$) — the required size of a square.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case print $$$n$$$ lines, each containing $$$n$$$ integers — the prime square you built. If there are multiple answers, print any.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id005160550775296734" id="id001813562100806514" class="input-output-copier">Copy</div></div><pre id="id005160550775296734">2
4
2
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id0042562355608337676" id="id0015201716521378583" class="input-output-copier">Copy</div></div><pre id="id0042562355608337676">4 6 8 1
4 9 9 9
4 10 10 65
1 4 4 4
1 1
1 1
</pre></div></div></div>