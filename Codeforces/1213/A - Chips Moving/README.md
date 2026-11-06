<h2><a href="https://codeforces.com/contest/1213/problem/A" target="_blank" rel="noopener noreferrer">1213A — Chips Moving</a></h2>

| | |
|---|---|
| **Difficulty** | 900 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1213A](https://codeforces.com/contest/1213/problem/A) |

## Topics
`math`

---

## Problem Statement

<div class="header"><div class="title">A. Chips Moving</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>You are given $$$n$$$ chips on a number line. The $$$i$$$-th chip is placed at the integer coordinate $$$x_i$$$. Some chips <span class="tex-font-style-bf">can have equal coordinates</span>.</p><p>You can perform each of the two following types of moves any (possibly, zero) number of times on any chip:</p><ul> <li> Move the chip $$$i$$$ by $$$2$$$ to the left or $$$2$$$ to the right <span class="tex-font-style-bf">for free</span> (i.e. replace the current coordinate $$$x_i$$$ with $$$x_i - 2$$$ or with $$$x_i + 2$$$); </li><li> move the chip $$$i$$$ by $$$1$$$ to the left or $$$1$$$ to the right and pay <span class="tex-font-style-bf">one coin</span> for this move (i.e. replace the current coordinate $$$x_i$$$ with $$$x_i - 1$$$ or with $$$x_i + 1$$$). </li></ul><p>Note that it's allowed to move chips to any integer coordinate, including negative and zero.</p><p>Your task is to find the minimum total number of coins required to move all $$$n$$$ chips to the same coordinate (i.e. all $$$x_i$$$ should be equal after some sequence of moves).</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line of the input contains one integer $$$n$$$ ($$$1 \le n \le 100$$$) — the number of chips.</p><p>The second line of the input contains $$$n$$$ integers $$$x_1, x_2, \dots, x_n$$$ ($$$1 \le x_i \le 10^9$$$), where $$$x_i$$$ is the coordinate of the $$$i$$$-th chip.</p></div><div class="output-specification"><div class="section-title">Output</div><p>Print one integer — the minimum total number of coins required to move all $$$n$$$ chips to the same coordinate.</p></div><div class="sample-tests"><div class="section-title">Examples</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0002000755116886932" id="id0046264455306816044" class="input-output-copier">Copy</div></div><pre id="id0002000755116886932">3
1 2 3
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id008529143079924704" id="id0032219563220229364" class="input-output-copier">Copy</div></div><pre id="id008529143079924704">1
</pre></div><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0019704991656206117" id="id006732664536101798" class="input-output-copier">Copy</div></div><pre id="id0019704991656206117">5
2 2 2 3 3
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id009670616388094793" id="id009349079966337364" class="input-output-copier">Copy</div></div><pre id="id009670616388094793">2
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first example you need to move the first chip by $$$2$$$ to the right and the second chip by $$$1$$$ to the right or move the third chip by $$$2$$$ to the left and the second chip by $$$1$$$ to the left so the answer is $$$1$$$.</p><p>In the second example you need to move two chips with coordinate $$$3$$$ by $$$1$$$ to the left so the answer is $$$2$$$.</p></div>