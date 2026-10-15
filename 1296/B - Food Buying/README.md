<h2><a href="https://codeforces.com/contest/1296/problem/B" target="_blank" rel="noopener noreferrer">1296B — Food Buying</a></h2>

| | |
|---|---|
| **Difficulty** | 900 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1296B](https://codeforces.com/contest/1296/problem/B) |

## Topics
`math`

---

## Problem Statement

<div class="header"><div class="title">B. Food Buying</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>Mishka wants to buy some food in the nearby shop. Initially, he has $$$s$$$ burles on his card. </p><p>Mishka can perform the following operation any number of times (possibly, zero): choose some <span class="tex-font-style-bf">positive integer number</span> $$$1 \le x \le s$$$, buy food that costs exactly $$$x$$$ burles and obtain $$$\lfloor\frac{x}{10}\rfloor$$$ burles as a cashback (in other words, Mishka spends $$$x$$$ burles and obtains $$$\lfloor\frac{x}{10}\rfloor$$$ back). The operation $$$\lfloor\frac{a}{b}\rfloor$$$ means $$$a$$$ divided by $$$b$$$ rounded down.</p><p>It is guaranteed that you can always buy some food that costs $$$x$$$ for any possible value of $$$x$$$.</p><p>Your task is to say the maximum number of burles Mishka can spend if he buys food optimally.</p><p>For example, if Mishka has $$$s=19$$$ burles then the maximum number of burles he can spend is $$$21$$$. Firstly, he can spend $$$x=10$$$ burles, obtain $$$1$$$ burle as a cashback. Now he has $$$s=10$$$ burles, so can spend $$$x=10$$$ burles, obtain $$$1$$$ burle as a cashback and spend it too.</p><p>You have to answer $$$t$$$ independent test cases.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line of the input contains one integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases.</p><p>The next $$$t$$$ lines describe test cases. Each test case is given on a separate line and consists of one integer $$$s$$$ ($$$1 \le s \le 10^9$$$) — the number of burles Mishka initially has.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case print the answer on it — the maximum number of burles Mishka can spend if he buys food optimally.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id005685589838103947" id="id0001325105153827899" class="input-output-copier">Copy</div></div><pre id="id005685589838103947">6
1
10
19
9876
12345
1000000000
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id00009511217254971949" id="id0012319264418337483" class="input-output-copier">Copy</div></div><pre id="id00009511217254971949">1
11
21
10973
13716
1111111111
</pre></div></div></div>