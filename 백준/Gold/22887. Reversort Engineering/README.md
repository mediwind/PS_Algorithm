# [Gold V] Reversort Engineering - 22887 

[문제 링크](https://www.acmicpc.net/problem/22887) 

### 성능 요약

메모리: 31120 KB, 시간: 36 ms

### 분류

애드 혹, 해 구성하기, 정렬

### 제출 일자

2024년 9월 24일 11:24:54

### 문제 설명

<p>Note: The main parts of the statements of the problems "Reversort" and "Reversort Engineering" are identical, except for the last paragraph. The problems can otherwise be solved independently.</p>

<p>Reversort is an algorithm to sort a list of distinct integers in increasing order. The algorithm is based on the "Reverse" operation. Each application of this operation reverses the order of some contiguous part of the list.</p>

<p>The pseudocode of the algorithm is the following:</p>

<pre>Reversort(L):
  for i := 1 to length(L) - 1
    j := position with the minimum value in L between i and length(L), inclusive
    Reverse(L[i..j])
</pre>

<p>After i−1 iterations, the positions 1,2,…,i−1 of the list contain the i−1 smallest elements of L, in increasing order. During the i-th iteration, the process reverses the sublist going from the i-th position to the current position of the i-th minimum element. That makes the i-th minimum element end up in the i-th position.</p>

<p>For example, for a list with 4 elements, the algorithm would perform 3 iterations. Here is how it would process L=[4,2,1,3]:</p>

<ol>
	<li>i=1, j=3 ⟶ L=[1,2,4,3]</li>
	<li>i=2, j=2 ⟶ L=[1,2,4,3]</li>
	<li>i=3, j=4 ⟶ L=[1,2,3,4]</li>
</ol>

<p>The most expensive part of executing the algorithm on our architecture is the Reverse operation. Therefore, our measure for the cost of each iteration is simply the length of the sublist passed to Reverse, that is, the value j−i+1. The cost of the whole algorithm is the sum of the costs of each iteration.</p>

<p>In the example above, the iterations cost 3, 1, and 2, in that order, for a total of 6.</p>

<p>You are given a size N and a cost C. Find a list of N distinct integers between 1 and N such that the cost of applying Reversort to it is exactly C, or say that there is no such list.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, T. T lines follow. Each line describes a test case with two integers N and C, the size of the wanted list and the desired cost, respectively.</p>

### 출력 

 <p>For each test case, if there is no list of size N such that applying Reversort to it costs exactly C, output one line containing <code>Case #x: IMPOSSIBLE</code>, where x is the test case number (starting from 1). Otherwise, output one line containing <code>Case #x: y<sub>1</sub> y<sub>2</sub> ... y<sub>N</sub></code>, where x is the test case number (starting from 1) and each y<sub>i</sub> is a distinct integer between 1 and N, representing the i-th element of one such possible list.</p>

