<h2><a href="https://codeforces.com/contest/1501/problem/B" target="_blank" rel="noopener noreferrer">1501B — Napoleon Cake</a></h2>

| | |
|---|---|
| **Difficulty** | 900 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1501B](https://codeforces.com/contest/1501/problem/B) |

## Topics
`dp` `implementation` `sortings`

---

## Problem Statement

<div class="header"><div class="title">B. Napoleon Cake</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>This week Arkady wanted to cook some pancakes (to follow ancient traditions) and make a problem about that. But then he remembered that one can't make a problem about stacking pancakes without working at a specific IT company, so he decided to bake the Napoleon cake instead.</p><p>To bake a Napoleon cake, one has to bake $$$n$$$ dry layers first, and then put them on each other in one stack, adding some cream. Arkady started with an empty plate, and performed the following steps $$$n$$$ times: </p><ul> <li> place a new cake layer on the top of the stack; </li><li> after the $$$i$$$-th layer is placed, pour $$$a_i$$$ units of cream on top of the stack. </li></ul><p>When $$$x$$$ units of cream are poured on the top of the stack, top $$$x$$$ layers of the cake get drenched in the cream. If there are less than $$$x$$$ layers, all layers get drenched and the rest of the cream is wasted. If $$$x = 0$$$, no layer gets drenched.</p><center> <img class="tex-graphics" height="76px" src="https://espresso.codeforces.com/5909ee4ad0b83994284fcf88ab901dceab8aceef.png" style="max-width: 100.0%;max-height: 100.0%;" width="567px"> <span class="tex-font-size-small">The picture represents the first test case of the example.</span> </center><p>Help Arkady determine which layers of the cake eventually get drenched when the process is over, and which don't.</p></div><div class="input-specification"><div class="section-title">Input</div><p>Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 20\,000$$$). Description of the test cases follows.</p><p>The first line of each test case contains a single integer $$$n$$$ ($$$1 \le n \le 2 \cdot 10^5$$$) — the number of layers in the cake.</p><p>The second line of each test case contains $$$n$$$ integers $$$a_1, a_2, \ldots, a_n$$$ ($$$0 \le a_i \le n$$$) — the amount of cream poured on the cake after adding each layer.</p><p>It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2 \cdot 10^5$$$.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, print a single line with $$$n$$$ integers. The $$$i$$$-th of the integers should be equal to $$$1$$$ if the $$$i$$$-th layer from the bottom gets drenched, and $$$0$$$ otherwise.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id004121111066320329" id="id006829856407064602" class="input-output-copier">Copy</div></div><pre id="id004121111066320329">3
6
0 3 0 0 1 3
10
0 0 0 1 0 5 0 0 0 2
3
0 0 0
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id007695589387031692" id="id007535139663029278" class="input-output-copier">Copy</div></div><pre id="id007695589387031692">1 1 0 1 1 1 
0 1 1 1 1 1 0 0 1 1 
0 0 0 
</pre></div></div></div>