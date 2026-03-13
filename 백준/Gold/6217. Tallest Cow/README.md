# [Gold I] Tallest Cow - 6217 

[문제 링크](https://www.acmicpc.net/problem/6217) 

### 성능 요약

메모리: 34972 KB, 시간: 56 ms

### 분류

애드 혹, 누적 합

### 제출 일자

2026년 3월 13일 23:48:41

### 문제 설명

<p>FJ's N (1 <= N <= 10,000) cows conveniently indexed 1..N are standing in a line.  Each cow has a positive integer height (which is a bit of secret). You are told only the height H (1 <= H <= 1,000,000) of the tallest cow along with the index I of that cow.</p>

<p>FJ has made  a list of R (0 <= R <= 10,000) lines of the form "cow 17 sees cow 34". This means that cow 34 is at least as tall as cow 17, and that every cow between 17 and 34 has a height that is strictly smaller than that of cow 17.</p>

<p>For each cow from 1..N, determine its maximum possible height, such that all of the information given is still correct. It is guaranteed that it is possible to satisfy all the constraints.</p>

### 입력 

 <ul>
	<li>Line 1: Four space-separated integers: N, I, H and R</li>
	<li>Lines 2..R+1: Two distinct space-separated integers A and B (1 <= A, B <= N), indicating that cow A can see cow B.</li>
</ul>

### 출력 

 <ul>
	<li>Lines 1..N: Line i contains the maximum possible height of cow i.</li>
</ul>

