<h3><a href="https://codeforces.com/contest/1553/problem/A" target="_blank" rel="noopener noreferrer">Digits Sum</a></h3>

<div class="header"><div class="title">A. Digits Sum</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>Let's define $$$S(x)$$$ to be the sum of digits of number $$$x$$$ written in decimal system. For example, $$$S(5) = 5$$$, $$$S(10) = 1$$$, $$$S(322) = 7$$$.</p><p>We will call an integer $$$x$$$ <span class="tex-font-style-bf">interesting</span> if $$$S(x + 1)  \lt  S(x)$$$. In each test you will be given one integer $$$n$$$. Your task is to calculate the number of integers $$$x$$$ such that $$$1 \le x \le n$$$ and $$$x$$$ is interesting.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains one integer $$$t$$$ ($$$1 \le t \le 1000$$$)  — number of test cases.</p><p>Then $$$t$$$ lines follow, the $$$i$$$-th line contains one integer $$$n$$$ ($$$1 \le n \le 10^9$$$) for the $$$i$$$-th test case.</p></div><div class="output-specification"><div class="section-title">Output</div><p>Print $$$t$$$ integers, the $$$i$$$-th should be the answer for the $$$i$$$-th test case.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0022476085278434577" id="id006792247037321629" class="input-output-copier">Copy</div></div><pre id="id0022476085278434577">5
1
9
10
34
880055535
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id007914524552126054" id="id008504306957998814" class="input-output-copier">Copy</div></div><pre id="id007914524552126054">0
1
1
3
88005553
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>The first interesting number is equal to $$$9$$$.</p></div>