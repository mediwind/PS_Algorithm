<h2><a href="https://codeforces.com/contest/1095/problem/B" target="_blank" rel="noopener noreferrer">1095B — Array Stabilization</a></h2>

| | |
|---|---|
| **Difficulty** | 900 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1095B](https://codeforces.com/contest/1095/problem/B) |

## Topics
`implementation`

---

## Problem Statement

<div class="header"><div class="title">B. Array Stabilization</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>You are given an array $$$a$$$ consisting of $$$n$$$ integer numbers.</p><p>Let <span class="tex-font-style-it">instability</span> of the array be the following value: $$$\max\limits_{i = 1}^{n} a_i - \min\limits_{i = 1}^{n} a_i$$$.</p><p>You have to remove <span class="tex-font-style-bf">exactly one</span> element from this array to minimize <span class="tex-font-style-it">instability</span> of the resulting $$$(n-1)$$$-elements array. Your task is to calculate the minimum possible <span class="tex-font-style-it">instability</span>.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line of the input contains one integer $$$n$$$ ($$$2 \le n \le 10^5$$$) — the number of elements in the array $$$a$$$.</p><p>The second line of the input contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ ($$$1 \le a_i \le 10^5$$$) — elements of the array $$$a$$$.</p></div><div class="output-specification"><div class="section-title">Output</div><p>Print one integer — the minimum possible <span class="tex-font-style-it">instability</span> of the array if you have to remove <span class="tex-font-style-bf">exactly one</span> element from the array $$$a$$$.</p></div><div class="sample-tests"><div class="section-title">Examples</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id007119226968188683" id="id0023717752440178763" class="input-output-copier">Copy</div></div><pre id="id007119226968188683">4
1 3 3 7
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id0009582070718696767" id="id003886176660028102" class="input-output-copier">Copy</div></div><pre id="id0009582070718696767">2
</pre></div><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id006919171285806266" id="id005652659555248417" class="input-output-copier">Copy</div></div><pre id="id006919171285806266">2
1 100000
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id0043398594328207885" id="id0020222568644678285" class="input-output-copier">Copy</div></div><pre id="id0043398594328207885">0
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first example you can remove $$$7$$$ then <span class="tex-font-style-it">instability</span> of the remaining array will be $$$3 - 1 = 2$$$.</p><p>In the second example you can remove either $$$1$$$ or $$$100000$$$ then <span class="tex-font-style-it">instability</span> of the remaining array will be $$$100000 - 100000 = 0$$$ and $$$1 - 1 = 0$$$ correspondingly.</p></div>