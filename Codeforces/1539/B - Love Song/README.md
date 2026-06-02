<h3><a href="https://codeforces.com/contest/1539/problem/B" target="_blank" rel="noopener noreferrer">Love Song</a></h3>

<div class="header"><div class="title">B. Love Song</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>Petya once wrote a sad love song and shared it to Vasya. The song is a string consisting of lowercase English letters. Vasya made up $$$q$$$ questions about this song. Each question is about a subsegment of the song starting from the $$$l$$$-th letter to the $$$r$$$-th letter. Vasya considers a substring made up from characters on this segment and repeats each letter in the subsegment $$$k$$$ times, where $$$k$$$ is the index of the corresponding letter in the alphabet. For example, if the question is about the substring "<span class="tex-font-style-tt">abbcb</span>", then Vasya repeats letter '<span class="tex-font-style-tt">a</span>' once, each of the letters '<span class="tex-font-style-tt">b</span>' twice, letter '<span class="tex-font-style-tt">c</span>" three times, so that the resulting string is "<span class="tex-font-style-tt">abbbbcccbb</span>", its length is $$$10$$$. Vasya is interested about the length of the resulting string.</p><p>Help Petya find the length of each string obtained by Vasya.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains two integers $$$n$$$ and $$$q$$$ ($$$1\leq n\leq 100\,000$$$, $$$1\leq q \leq 100\,000$$$) — the length of the song and the number of questions. </p><p>The second line contains one string $$$s$$$ — the song, consisting of $$$n$$$ lowercase letters of English letters.</p><p>Vasya's questions are contained in the next $$$q$$$ lines. Each line contains two integers $$$l$$$ and $$$r$$$ ($$$1 \leq l \leq r \leq n$$$) — the bounds of the question.</p></div><div class="output-specification"><div class="section-title">Output</div><p>Print $$$q$$$ lines: for each question print the length of the string obtained by Vasya.</p></div><div class="sample-tests"><div class="section-title">Examples</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id009179067313144731" id="id00023280629361193794" class="input-output-copier">Copy</div></div><pre id="id009179067313144731">7 3
abacaba
1 3
2 5
1 7
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id0006613184055589127" id="id007855974762489644" class="input-output-copier">Copy</div></div><pre id="id0006613184055589127">4
7
11
</pre></div><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id004257671223316365" id="id0048838042135233617" class="input-output-copier">Copy</div></div><pre id="id004257671223316365">7 4
abbabaa
1 3
5 7
6 6
2 4
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id0038848026208162745" id="id004525495215450298" class="input-output-copier">Copy</div></div><pre id="id0038848026208162745">5
4
1
5
</pre></div><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id006874648782335053" id="id00908318364810827" class="input-output-copier">Copy</div></div><pre id="id006874648782335053">13 7
sonoshikumiwo
1 5
2 10
7 7
1 13
4 8
2 5
3 9
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id0009450088460607231" id="id009152733938351724" class="input-output-copier">Copy</div></div><pre id="id0009450088460607231">82
125
9
191
62
63
97
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first example Vasya is interested in three questions. In the first question Vasya considers the substring "<span class="tex-font-style-tt">aba</span>", that transforms to "<span class="tex-font-style-tt">abba</span>", so the answer is equal to $$$4$$$. In the second question Vasya considers "<span class="tex-font-style-tt">baca</span>", that transforms to "<span class="tex-font-style-tt">bbaccca</span>", so the answer is $$$7$$$. In the third question Vasya considers the string "<span class="tex-font-style-tt">abacaba</span>",that transforms to "<span class="tex-font-style-tt">abbacccabba</span>" of length $$$11$$$.</p></div>