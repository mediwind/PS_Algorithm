# [Platinum V] Splitstream - 26139 

[문제 링크](https://www.acmicpc.net/problem/26139) 

### 성능 요약

메모리: 36992 KB, 시간: 2164 ms

### 분류

구현, 다이나믹 프로그래밍, 그래프 이론, 방향 비순환 그래프, 위상 정렬

### 제출 일자

2026년 3월 22일 23:54:42

### 문제 설명

<p>A splitstream system is an acyclic network of nodes that processes finite sequences of numbers. There are two types of nodes (illustrated in Figure J.1):</p>

<ul>
	<li>A <em>split</em> node takes a sequence of numbers as input and distributes them alternatingly to its two outputs. The first number goes to output 1, the second to output 2, the third to output 1, the fourth to output 2, and so on, in this order.</li>
	<li>A <em>merge</em> node takes two sequences of numbers as input and merges them alternatingly to form its single output. The output contains the first number from input 1, then the first from input 2, then the second from input 1, then the second from input 2, and so on. If one of the input sequences is shorter than the other, then the remaining numbers from the longer sequence are simply transmitted without being merged after the shorter sequence has been exhausted.</li>
</ul>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/69c96e85-8bac-45ff-a73b-b91b39361f9a/-/preview/" style="width: 384px; height: 163px;"></p>

<p style="text-align: center;">Figure J.1: Illustration of how split and merge nodes work.</p>

<p>The overall network has one input, which is the sequence of positive integers 1, 2, 3, . . . , m. Any output of any node can be queried. A query will seek to identify the k<sup>th</sup> number in the sequence of numbers for a given output and a given k. Your task is to implement such queries efficiently.</p>

### 입력 

 <p>The first line of input contains three integers m, n, and q, where m (1 ≤ m ≤ 10<sup>9</sup>) is the length of the input sequence, n (1 ≤ n ≤ 10<sup>4</sup>) is the number of nodes, and q (1 ≤ q ≤ 10<sup>3</sup>) is the number of queries.</p>

<p>The next n lines describe the network, one node per line. A split node has the format S x y z, where x, y and z identify its input, first output and second output, respectively. A merge node has the format M x y z, where x, y and z identify its first input, second input and output, respectively. Identifiers x, y and z are distinct positive integers. The overall input is identified by 1, and the remaining input/output identifiers form a consecutive sequence beginning at 2. Every input identifier except 1 appears as exactly one output. Every output identifier appears as the input of at most one node.</p>

<p>Each of the next q lines describes a query. Each query consists of two integers x and k, where x (2 ≤ x ≤ 10<sup>5</sup>) is a valid output identifier and k (1 ≤ k ≤ 10<sup>9</sup>) is the index of the desired number in that sequence. Indexing in a sequence starts with 1.</p>

### 출력 

 <p>For each query x and k output one line with the k<sup>th</sup> number in the output sequence identified by x, or none if there is no element with that index number.</p>

