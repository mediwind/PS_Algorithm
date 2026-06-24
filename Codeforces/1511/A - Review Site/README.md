<h2><a href="https://codeforces.com/contest/1511/problem/A" target="_blank" rel="noopener noreferrer">1511A — Review Site</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1511A](https://codeforces.com/contest/1511/problem/A) |

## Topics
`greedy`

---

## Problem Statement

<div class="header"><div class="title">A. Review Site</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>You are an upcoming movie director, and you have just released your first movie. You have also launched a simple review site with two buttons to press — upvote and downvote.</p><p>However, the site is not so simple on the inside. There are two servers, each with its separate counts for the upvotes and the downvotes.</p><p>$$$n$$$ reviewers enter the site one by one. Each reviewer is one of the following types: </p><ul> <li> type $$$1$$$: a reviewer has watched the movie, and they like it — they press the upvote button; </li><li> type $$$2$$$: a reviewer has watched the movie, and they dislike it — they press the downvote button; </li><li> type $$$3$$$: a reviewer hasn't watched the movie — they look at the current number of upvotes and downvotes of the movie on the server they are in and decide what button to press. If there are more downvotes than upvotes, then a reviewer downvotes the movie. Otherwise, they upvote the movie. </li></ul><p>Each reviewer votes on the movie exactly once.</p><p>Since you have two servers, you can actually manipulate the votes so that your movie gets as many upvotes as possible. When a reviewer enters a site, you know their type, and you can send them either to the first server or to the second one.</p><p>What is the maximum total number of upvotes you can gather over both servers if you decide which server to send each reviewer to?</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains a single integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of testcases.</p><p>Then the descriptions of $$$t$$$ testcases follow.</p><p>The first line of each testcase contains a single integer $$$n$$$ ($$$1 \le n \le 50$$$) — the number of reviewers.</p><p>The second line of each testcase contains $$$n$$$ integers $$$r_1, r_2, \dots, r_n$$$ ($$$1 \le r_i \le 3$$$) — the types of the reviewers in the same order they enter the site.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each testcase print a single integer — the maximum total number of upvotes you can gather over both servers if you decide which server to send each reviewer to.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id005997052492165172" id="id0010712732009408343" class="input-output-copier">Copy</div></div><pre id="id005997052492165172">4
1
2
3
1 2 3
5
1 1 1 1 1
3
3 3 2
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id001686917048514226" id="id0040926221246563865" class="input-output-copier">Copy</div></div><pre id="id001686917048514226">0
2
5
2
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first testcase of the example you can send the only reviewer to either of the servers — they'll downvote anyway. The movie won't receive any upvotes.</p><p>In the second testcase of the example you can send all reviewers to the first server: </p><ul> <li> the first reviewer upvotes; </li><li> the second reviewer downvotes; </li><li> the last reviewer sees that the number of downvotes is not greater than the number of upvotes — upvote themselves. </li></ul><p>There are two upvotes in total. Alternatevely, you can send the first and the second reviewers to the first server and the last reviewer — to the second server: </p><ul> <li> the first reviewer upvotes on the first server; </li><li> the second reviewer downvotes on the first server; </li><li> the last reviewer sees no upvotes or downvotes on the second server — upvote themselves. </li></ul></div>