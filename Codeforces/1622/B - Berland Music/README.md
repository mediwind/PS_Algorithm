<h2><a href="https://codeforces.com/contest/1622/problem/B" target="_blank" rel="noopener noreferrer">1622B — Berland Music</a></h2>

| | |
|---|---|
| **Difficulty** | 1000 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1622B](https://codeforces.com/contest/1622/problem/B) |

## Topics
`data structures` `greedy` `math` `sortings`

---

## Problem Statement

<div class="header"><div class="title">B. Berland Music</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>Berland Music is a music streaming service built specifically to support Berland local artist. Its developers are currently working on a song recommendation module.</p><p>So imagine Monocarp got recommended $$$n$$$ songs, numbered from $$$1$$$ to $$$n$$$. The $$$i$$$-th song had its predicted rating equal to $$$p_i$$$, where $$$1 \le p_i \le n$$$ and every integer from $$$1$$$ to $$$n$$$ appears exactly once. In other words, $$$p$$$ is a permutation.</p><p>After listening to each of them, Monocarp pressed either a like or a dislike button. Let his vote sequence be represented with a string $$$s$$$, such that $$$s_i=0$$$ means that he disliked the $$$i$$$-th song, and $$$s_i=1$$$ means that he liked it.</p><p>Now the service has to re-evaluate the song ratings in such a way that:</p><ul> <li> the new ratings $$$q_1, q_2, \dots, q_n$$$ still form a permutation ($$$1 \le q_i \le n$$$; each integer from $$$1$$$ to $$$n$$$ appears exactly once); </li><li> every song that Monocarp liked should have a greater rating than every song that Monocarp disliked (formally, for all $$$i, j$$$ such that $$$s_i=1$$$ and $$$s_j=0$$$, $$$q_i \gt q_j$$$ should hold). </li></ul><p>Among all valid permutations $$$q$$$ find the one that has the smallest value of $$$\sum\limits_{i=1}^n |p_i-q_i|$$$, where $$$|x|$$$ is an absolute value of $$$x$$$.</p><p>Print the permutation $$$q_1, q_2, \dots, q_n$$$. If there are multiple answers, you can print any of them.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains a single integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of testcases.</p><p>The first line of each testcase contains a single integer $$$n$$$ ($$$1 \le n \le 2 \cdot 10^5$$$) — the number of songs.</p><p>The second line of each testcase contains $$$n$$$ integers $$$p_1, p_2, \dots, p_n$$$ ($$$1 \le p_i \le n$$$) — the permutation of the predicted ratings.</p><p>The third line contains a single string $$$s$$$, consisting of $$$n$$$ characters. Each character is either a $$$0$$$ or a $$$1$$$. $$$0$$$ means that Monocarp disliked the song, and $$$1$$$ means that he liked it.</p><p>The sum of $$$n$$$ over all testcases doesn't exceed $$$2 \cdot 10^5$$$.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each testcase, print a permutation $$$q$$$ — the re-evaluated ratings of the songs. If there are multiple answers such that $$$\sum\limits_{i=1}^n |p_i-q_i|$$$ is minimum possible, you can print any of them.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0040558569173524217" id="id004334632568648028" class="input-output-copier">Copy</div></div><pre id="id0040558569173524217">3
2
1 2
10
3
3 1 2
111
8
2 3 1 8 5 4 7 6
01110001
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id004073438684142452" id="id0031812364081349587" class="input-output-copier">Copy</div></div><pre id="id004073438684142452">2 1
3 1 2
1 6 5 8 3 2 4 7
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first testcase, there exists only one permutation $$$q$$$ such that each liked song is rating higher than each disliked song: song $$$1$$$ gets rating $$$2$$$ and song $$$2$$$ gets rating $$$1$$$. $$$\sum\limits_{i=1}^n |p_i-q_i|=|1-2|+|2-1|=2$$$.</p><p>In the second testcase, Monocarp liked all songs, so all permutations could work. The permutation with the minimum sum of absolute differences is the permutation equal to $$$p$$$. Its cost is $$$0$$$.</p></div>