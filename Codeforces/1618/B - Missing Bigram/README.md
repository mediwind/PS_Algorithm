<h2><a href="https://codeforces.com/contest/1618/problem/B" target="_blank" rel="noopener noreferrer">1618B — Missing Bigram</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1618B](https://codeforces.com/contest/1618/problem/B) |

## Topics
`implementation`

---

## Problem Statement

<div class="header"><div class="title">B. Missing Bigram</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>Polycarp has come up with a new game to play with you. He calls it "A missing bigram".</p><p>A <span class="tex-font-style-it">bigram</span> of a word is a sequence of two adjacent letters in it.</p><p>For example, word "<span class="tex-font-style-tt">abbaaba</span>" contains bigrams "<span class="tex-font-style-tt">ab</span>", "<span class="tex-font-style-tt">bb</span>", "<span class="tex-font-style-tt">ba</span>", "<span class="tex-font-style-tt">aa</span>", "<span class="tex-font-style-tt">ab</span>" and "<span class="tex-font-style-tt">ba</span>".</p><p>The game goes as follows. First, Polycarp comes up with a word, consisting only of lowercase letters 'a' and 'b'. Then, he writes down all its bigrams on a whiteboard <span class="tex-font-style-bf">in the same order as they appear in the word</span>. After that, he wipes one of them off the whiteboard.</p><p>Finally, Polycarp invites you to guess what the word that he has come up with was.</p><p>Your goal is to find any word such that it's possible to write down all its bigrams and remove one of them, so that the resulting sequence of bigrams is the same as the one Polycarp ended up with.</p><p>The tests are generated in such a way that the answer exists. If there are multiple answers, you can print any of them.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains a single integer $$$t$$$ ($$$1 \le t \le 2000$$$) — the number of testcases.</p><p>The first line of each testcase contains a single integer $$$n$$$ ($$$3 \le n \le 100$$$) — the length of the word Polycarp has come up with.</p><p>The second line of each testcase contains $$$n-2$$$ bigrams of that word, separated by a single space. Each bigram consists of two letters, each of them is either 'a' or 'b'.</p><p><span class="tex-font-style-bf">Additional constraint on the input: there exists at least one string such that it is possible to write down all its bigrams, except one, so that the resulting sequence is the same as the sequence in the input. In other words, the answer exists.</span></p></div><div class="output-specification"><div class="section-title">Output</div><p>For each testcase print a word, consisting of $$$n$$$ letters, each of them should be either 'a' or 'b'. It should be possible to write down all its bigrams and remove one of them, so that the resulting sequence of bigrams is the same as the one Polycarp ended up with.</p><p>The tests are generated in such a way that the answer exists. If there are multiple answers, you can print any of them. </p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0012215366472996125" id="id00033302141506472704" class="input-output-copier">Copy</div></div><pre id="id0012215366472996125">4
7
ab bb ba aa ba
7
ab ba aa ab ba
3
aa
5
bb ab bb
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id0012036146346174681" id="id004788440636172472" class="input-output-copier">Copy</div></div><pre id="id0012036146346174681">abbaaba
abaabaa
baa
bbabb
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>The first two testcases from the example are produced from the word "<span class="tex-font-style-tt">abbaaba</span>". As listed in the statement, it contains bigrams "<span class="tex-font-style-tt">ab</span>", "<span class="tex-font-style-tt">bb</span>", "<span class="tex-font-style-tt">ba</span>", "<span class="tex-font-style-tt">aa</span>", "<span class="tex-font-style-tt">ab</span>" and "<span class="tex-font-style-tt">ba</span>".</p><p>In the first testcase, the $$$5$$$-th bigram is removed. </p><p>In the second testcase, the $$$2$$$-nd bigram is removed. However, that sequence could also have been produced from the word "<span class="tex-font-style-tt">abaabaa</span>". It contains bigrams "<span class="tex-font-style-tt">ab</span>", "<span class="tex-font-style-tt">ba</span>", "<span class="tex-font-style-tt">aa</span>", "<span class="tex-font-style-tt">ab</span>", "<span class="tex-font-style-tt">ba</span>" and "<span class="tex-font-style-tt">aa</span>". The missing bigram is the $$$6$$$-th one.</p><p>In the third testcase, all of "<span class="tex-font-style-tt">baa</span>", "<span class="tex-font-style-tt">aab</span>" and "<span class="tex-font-style-tt">aaa</span>" are valid answers.</p></div>