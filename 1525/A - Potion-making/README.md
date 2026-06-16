<h2><a href="https://codeforces.com/contest/1525/problem/A" target="_blank" rel="noopener noreferrer">1525A — Potion-making</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1525A](https://codeforces.com/contest/1525/problem/A) |

## Topics
`math` `number theory`

---

## Problem Statement

<div class="header"><div class="title">A. Potion-making</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>You have an initially empty cauldron, and you want to brew a potion in it. The potion consists of two ingredients: magic essence and water. The potion you want to brew should contain exactly $$$k\ \%$$$ magic essence and $$$(100 - k)\ \%$$$ water.</p><p>In one step, you can pour either one liter of magic essence or one liter of water into the cauldron. What is the minimum number of steps to brew a potion? You don't care about the total volume of the potion, only about the ratio between magic essence and water in it.</p><p>A small reminder: if you pour $$$e$$$ liters of essence and $$$w$$$ liters of water ($$$e + w  \gt  0$$$) into the cauldron, then it contains $$$\frac{e}{e + w} \cdot 100\ \%$$$ (without rounding) magic essence and $$$\frac{w}{e + w} \cdot 100\ \%$$$ water.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains the single $$$t$$$ ($$$1 \le t \le 100$$$) — the number of test cases.</p><p>The first and only line of each test case contains a single integer $$$k$$$ ($$$1 \le k \le 100$$$) — the percentage of essence in a good potion.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, print the minimum number of steps to brew a good potion. It can be proved that it's always possible to achieve it in a finite number of steps.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id008038875550829913" id="id0020990179189585378" class="input-output-copier">Copy</div></div><pre id="id008038875550829913">3
3
100
25
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id004169027771383519" id="id008893820414378893" class="input-output-copier">Copy</div></div><pre id="id004169027771383519">100
1
4
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first test case, you should pour $$$3$$$ liters of magic essence and $$$97$$$ liters of water into the cauldron to get a potion with $$$3\ \%$$$ of magic essence.</p><p>In the second test case, you can pour only $$$1$$$ liter of essence to get a potion with $$$100\ \%$$$ of magic essence.</p><p>In the third test case, you can pour $$$1$$$ liter of magic essence and $$$3$$$ liters of water.</p></div>