# [Gold V] Earthquake Damage - 6082 

[문제 링크](https://www.acmicpc.net/problem/6082) 

### 성능 요약

메모리: 43504 KB, 시간: 224 ms

### 분류

너비 우선 탐색, 플러드 필, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 1월 9일 18:23:39

### 문제 설명

<p>Wisconsin has had an earthquake that has struck Farmer John's farm! The earthquake has damaged some of the pastures so that they are unpassable. Remarkably, none of the cowpaths was damaged.</p>

<p>As usual, the farm is modeled as a set of P (1 <= P <= 30,000) pastures conveniently numbered 1..P which are connected by a set of C (1 <= C <= 100,000) non-directional cowpaths conveniently numbered 1..C. Cowpath i connects pastures a_i and b_i (1 <= a_i <= P; 1 <= b_i <= P). Cowpaths might connect a_i to itself or perhaps might connect two pastures more than once.  The barn is located in pasture 1.</p>

<p>A total of N (1 <= N <= P) cows (in different pastures) sequentially contact Farmer John via moobile phone with an integer message report_j (2 <= report_j <= P) that indicates that pasture report_j is undamaged but that the calling cow is unable to return to the barn from pasture report_j because she could not find a path that does not go through damaged pastures.</p>

<p>After all the cows report in, determine the minimum number of pastures (including ones that are uncrossable) from which it is not possible to return to the barn.</p>

<p> </p>

### 입력 

 <ul>
	<li>Line 1: Three space-separated integers: P, C, and N</li>
	<li>Lines 2..C+1: Line i+1 describes cowpath i with two integers: a_i and b_i</li>
	<li>Lines C+2..C+N+1: Line C+1+j contains a single integer: report_j</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single integer that is the minimum count of pastures from which a cow can not return to the barn (including the damaged pastures themselves)</li>
</ul>

<p> </p>

