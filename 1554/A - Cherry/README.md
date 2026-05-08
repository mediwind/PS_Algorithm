<h3><a href="https://codeforces.com/contest/1554/problem/A" target="_blank" rel="noopener noreferrer">Cherry</a></h3>

<div class="header"><div class="title">A. Cherry</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>You are given $$$n$$$ integers $$$a_1, a_2, \ldots, a_n$$$. Find the maximum value of $$$max(a_l, a_{l + 1}, \ldots, a_r) \cdot min(a_l, a_{l + 1}, \ldots, a_r)$$$ over all pairs $$$(l, r)$$$ of integers for which $$$1 \le l  \lt  r \le n$$$.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains a single integer $$$t$$$ ($$$1 \le t \le 10\,000$$$)  — the number of test cases.</p><p>The first line of each test case contains a single integer $$$n$$$ ($$$2 \le n \le 10^5$$$).</p><p>The second line of each test case contains $$$n$$$ integers $$$a_1, a_2, \ldots, a_n$$$ ($$$1 \le a_i \le 10^6$$$).</p><p>It is guaranteed that the sum of $$$n$$$ over all test cases doesn't exceed $$$3 \cdot 10^5$$$.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, print a single integer  — the maximum possible value of the product from the statement.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id009131506698544865" id="id0022810920819990688" class="input-output-copier">Copy</div></div><pre id="id009131506698544865">4
3
2 4 3
4
3 2 3 1
2
69 69
6
719313 273225 402638 473783 804745 323328
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id0007966621814814667" id="id005034556434888652" class="input-output-copier">Copy</div></div><pre id="id0007966621814814667">12
6
4761
381274500335
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>Let $$$f(l, r) = max(a_l, a_{l + 1}, \ldots, a_r) \cdot min(a_l, a_{l + 1}, \ldots, a_r)$$$.</p><p>In the first test case, </p><ul> <li> $$$f(1, 2) = max(a_1, a_2) \cdot min(a_1, a_2) = max(2, 4) \cdot min(2, 4) = 4 \cdot 2 = 8$$$. </li><li> $$$f(1, 3) = max(a_1, a_2, a_3) \cdot min(a_1, a_2, a_3) = max(2, 4, 3) \cdot min(2, 4, 3) = 4 \cdot 2 = 8$$$. </li><li> $$$f(2, 3) = max(a_2, a_3) \cdot min(a_2, a_3) = max(4, 3) \cdot min(4, 3) = 4 \cdot 3 = 12$$$. </li></ul><p>So the maximum is $$$f(2, 3) = 12$$$.</p><p>In the second test case, the maximum is $$$f(1, 2) = f(1, 3) = f(2, 3) = 6$$$.</p></div>