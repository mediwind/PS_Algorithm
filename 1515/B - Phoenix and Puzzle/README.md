<h2><a href="https://codeforces.com/contest/1515/problem/B" target="_blank" rel="noopener noreferrer">1515B — Phoenix and Puzzle</a></h2>

| | |
|---|---|
| **Difficulty** | 1000 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1515B](https://codeforces.com/contest/1515/problem/B) |

## Topics
`brute force` `geometry` `math` `number theory`

---

## Problem Statement

<div class="header"><div class="title">B. Phoenix and Puzzle</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>Phoenix is playing with a new puzzle, which consists of $$$n$$$ identical puzzle pieces. Each puzzle piece is a right isosceles triangle as shown below.</p><center> <img class="tex-graphics" height="113px" src="https://espresso.codeforces.com/c6cceedba3e2ee14f363f5914ee59dadbb654727.png" style="max-width: 100.0%;max-height: 100.0%;" width="113px">   <span class="tex-font-size-small">A puzzle piece</span> </center><p>The goal of the puzzle is to create a <span class="tex-font-style-bf">square</span> using the $$$n$$$ pieces. He is allowed to rotate and move the pieces around, but none of them can overlap and all $$$n$$$ pieces must be used (of course, the square shouldn't contain any holes as well). Can he do it?</p></div><div class="input-specification"><div class="section-title">Input</div><p>The input consists of multiple test cases. The first line contains an integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases.</p><p>The first line of each test case contains an integer $$$n$$$ ($$$1 \le n \le 10^9$$$) — the number of puzzle pieces.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, if Phoenix can create a square with the $$$n$$$ puzzle pieces, print <span class="tex-font-style-tt">YES</span>. Otherwise, print <span class="tex-font-style-tt">NO</span>.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id008568327989109156" id="id005817401309837091" class="input-output-copier">Copy</div></div><pre id="id008568327989109156">3
2
4
6
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id0019907426615191293" id="id005368298344572603" class="input-output-copier">Copy</div></div><pre id="id0019907426615191293">YES
YES
NO
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>For $$$n=2$$$, Phoenix can create a square like this:</p><center> <img class="tex-graphics" height="113px" src="https://espresso.codeforces.com/0b74e24a22d1242f147a8b3075eeaa64effbd8bc.png" style="max-width: 100.0%;max-height: 100.0%;" width="113px">   </center><p>For $$$n=4$$$, Phoenix can create a square like this:</p><center> <img class="tex-graphics" height="159px" src="https://espresso.codeforces.com/575a41e78b88b392a36dc58ec7f6d6f2cf3ce91c.png" style="max-width: 100.0%;max-height: 100.0%;" width="159px">   </center><p>For $$$n=6$$$, it is impossible for Phoenix to create a square.</p></div>