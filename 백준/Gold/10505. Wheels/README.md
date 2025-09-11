# [Gold II] Wheels - 10505 

[문제 링크](https://www.acmicpc.net/problem/10505) 

### 성능 요약

메모리: 37172 KB, 시간: 1828 ms

### 분류

깊이 우선 탐색, 그래프 이론, 그래프 탐색, 구현

### 제출 일자

2025년 9월 11일 22:37:52

### 문제 설명

<p>A very important and complicated machine consists of n wheels, numbered 1, 2, . . . , n. They are actually cogwheels, but the cogs are so small that we can model them as circles on the plane. Every wheel can spin around its center.</p>

<p>Two wheels cannot overlap (they do not have common interior points), but they can touch. If two wheels touch each other and one of them rotates, the other one spins as well, as their micro-cogs are locked together.</p>

<p>A force is put to wheel 1 (and to no other wheel), making it rotate at the rate of exactly one turn per minute, clockwise. Compute the rates of other wheels’ movement. You may assume that the machine is not jammed (the movement is physically possible).</p>

### 입력 

 <p>The first line of input contains the number of test cases T. The descriptions of the test cases follow:</p>

<p>Each test case consists of one line containing the number of wheels n (1 ≤ n ≤ 1000) . Each of the following lines contain three integers x, y and r (−10 000 ≤ x, y ≤ 10 000; 1 ≤ r ≤ 10 000) where (x, y) denote the Cartesian coordinates of the wheel’s center and r is its radius.</p>

### 출력 

 <p>For each test case, output n lines, each describing the movement of one wheel, in the same order as in the input. For every wheel, output either <code>p/q clockwise</code> or <code>p/q counterclockwise</code>, where the irreducible fraction p/q is the number of wheel turns per minute. If q is 1, output just p as an integer. If a wheel is standing still, output <code>not moving</code></p>

