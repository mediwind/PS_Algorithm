<h2><a href="https://codeforces.com/contest/1525/problem/B" target="_blank" rel="noopener noreferrer">1525B — Permutation Sort</a></h2>

| | |
|---|---|
| **Difficulty** | 900 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1525B](https://codeforces.com/contest/1525/problem/B) |

## Topics
`constructive algorithms` `greedy`

---

## Problem Statement

<div class="header"><div class="title">B. Permutation Sort</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>You are given a permutation $$$a$$$ consisting of $$$n$$$ numbers $$$1$$$, $$$2$$$, ..., $$$n$$$ (a permutation is an array in which each element from $$$1$$$ to $$$n$$$ occurs exactly once).</p><p>You can perform the following operation: choose some subarray (contiguous subsegment) of $$$a$$$ and rearrange the elements in it in any way you want. But this operation cannot be applied to the whole array.</p><p>For example, if $$$a = [2, 1, 4, 5, 3]$$$ and we want to apply the operation to the subarray $$$a[2, 4]$$$ (the subarray containing all elements from the $$$2$$$-nd to the $$$4$$$-th), then after the operation, the array can become $$$a = [2, 5, 1, 4, 3]$$$ or, for example, $$$a = [2, 1, 5, 4, 3]$$$.</p><p>Your task is to calculate the minimum number of operations described above to sort the permutation $$$a$$$ in ascending order.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains a single integer $$$t$$$ ($$$1 \le t \le 2000$$$) — the number of test cases.</p><p>The first line of the test case contains a single integer $$$n$$$ ($$$3 \le n \le 50$$$) — the number of elements in the permutation.</p><p>The second line of the test case contains $$$n$$$ distinct integers from $$$1$$$ to $$$n$$$ — the given permutation $$$a$$$.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, output a single integer — the minimum number of operations described above to sort the array $$$a$$$ in ascending order.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id007903008187378715" id="id006631599862644886" class="input-output-copier">Copy</div></div><pre id="id007903008187378715">3
4
1 3 2 4
3
1 2 3
5
2 1 4 5 3
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id006629243642543715" id="id0016194324994184162" class="input-output-copier">Copy</div></div><pre id="id006629243642543715">1
0
2
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the explanations, $$$a[i, j]$$$ defines the subarray of $$$a$$$ that starts from the $$$i$$$-th element and ends with the $$$j$$$-th element.</p><p>In the first test case of the example, you can select the subarray $$$a[2, 3]$$$ and swap the elements in it.</p><p>In the second test case of the example, the permutation is already sorted, so you don't need to apply any operations.</p><p>In the third test case of the example, you can select the subarray $$$a[3, 5]$$$ and reorder the elements in it so $$$a$$$ becomes $$$[2, 1, 3, 4, 5]$$$, and then select the subarray $$$a[1, 2]$$$ and swap the elements in it, so $$$a$$$ becomes $$$[1, 2, 3, 4, 5]$$$.</p></div>