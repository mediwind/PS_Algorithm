# [Platinum IV] Cowlendar - 31557 

[문제 링크](https://www.acmicpc.net/problem/31557) 

### 성능 요약

메모리: 33948 KB, 시간: 364 ms

### 분류

수학, 브루트포스 알고리즘, 애드 혹, 정수론, 비둘기집 원리

### 제출 일자

2026년 3월 15일 23:40:28

### 문제 설명

<p>Bessie has woken up on a strange planet. In this planet, there are $N$ ($1\le N\le 10^4$) months, with $a_1, \ldots, a_N$ days, respectively ($1\leq a_i \leq 4 \cdot 10^9$, all $a_i$ are integers). In addition, on the planet, there are also weeks, where each week is $L$ days, with $L$ being a positive integer. Interestingly, Bessie knows the following:</p>

<ul>
	<li>For the correct $L$, each month is at least $4$ weeks long.</li>
	<li>For the correct $L$, there are at most $3$ distinct values of $a_i\bmod L$.</li>
</ul>

<p>Unfortunately, Bessie has forgotten what $L$ is! Help her by printing the sum of all possible values of $L$.</p>

<p><strong>Note that the large size of integers involved in this problem may require the use of 64-bit integer data types (e.g., a "long long" in C/C++).</strong></p>

### 입력 

 <p>The first line contains a single integer $N$. The second line contains $N$ space-separated integers, $a_1, \ldots, a_N$.</p>

### 출력 

 <p>A single integer, the sum of all possible values of $L$.</p>

