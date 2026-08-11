<h2><a href="https://codeforces.com/contest/1555/problem/A" target="_blank" rel="noopener noreferrer">1555A — PizzaForces</a></h2>

| | |
|---|---|
| **Difficulty** | 900 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1555A](https://codeforces.com/contest/1555/problem/A) |

## Topics
`brute force` `math`

---

## Problem Statement

<div class="header"><div class="title">A. PizzaForces</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>PizzaForces is Petya's favorite pizzeria. PizzaForces makes and sells pizzas of three sizes: small pizzas consist of $$$6$$$ slices, medium ones consist of $$$8$$$ slices, and large pizzas consist of $$$10$$$ slices each. Baking them takes $$$15$$$, $$$20$$$ and $$$25$$$ minutes, respectively.</p><p>Petya's birthday is today, and $$$n$$$ of his friends will come, so he decided to make an order from his favorite pizzeria. Petya wants to order so much pizza that each of his friends gets at least one slice of pizza. The cooking time of the order is the total baking time of all the pizzas in the order.</p><p>Your task is to determine the minimum number of minutes that is needed to make pizzas containing at least $$$n$$$ slices in total. For example: </p><ul> <li> if $$$12$$$ friends come to Petya's birthday, he has to order pizzas containing at least $$$12$$$ slices in total. He can order two small pizzas, containing exactly $$$12$$$ slices, and the time to bake them is $$$30$$$ minutes; </li><li> if $$$15$$$ friends come to Petya's birthday, he has to order pizzas containing at least $$$15$$$ slices in total. He can order a small pizza and a large pizza, containing $$$16$$$ slices, and the time to bake them is $$$40$$$ minutes; </li><li> if $$$300$$$ friends come to Petya's birthday, he has to order pizzas containing at least $$$300$$$ slices in total. He can order $$$15$$$ small pizzas, $$$10$$$ medium pizzas and $$$13$$$ large pizzas, in total they contain $$$15 \cdot 6 + 10 \cdot 8 + 13 \cdot 10 = 300$$$ slices, and the total time to bake them is $$$15 \cdot 15 + 10 \cdot 20 + 13 \cdot 25 = 750$$$ minutes; </li><li> if only one friend comes to Petya's birthday, he can order a small pizza, and the time to bake it is $$$15$$$ minutes. </li></ul></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains a single integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of testcases.</p><p>Each testcase consists of a single line that contains a single integer $$$n$$$ ($$$1 \le n \le 10^{16}$$$) — the number of Petya's friends.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each testcase, print one integer — the minimum number of minutes that is needed to bake pizzas containing at least $$$n$$$ slices in total.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id004878822985129968" id="id003877221285951393" class="input-output-copier">Copy</div></div><pre id="id004878822985129968">6
12
15
300
1
9999999999999999
3
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id0004553866828693465" id="id0008604209247720895" class="input-output-copier">Copy</div></div><pre id="id0004553866828693465">30
40
750
15
25000000000000000
15
</pre></div></div></div>