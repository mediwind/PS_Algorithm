# [Gold V] Black and White - 11467 

[문제 링크](https://www.acmicpc.net/problem/11467) 

### 성능 요약

메모리: 31120 KB, 시간: 32 ms

### 분류

애드 혹, 해 구성하기

### 제출 일자

2024년 9월 6일 10:59:20

### 문제 설명

<p>The jury has a great artistic idea — to create a rectangular panel out of a huge pile of black and white squares of the same size. The panel should have exactly b 4-connected areas made of black tiles, and w 4-connected areas made of white tiles.</p>

<p>Remember, a 4-connected area of some color is a maximal set of the panel tiles such that:</p>

<ul>
	<li>any two tiles of the area share the same color;</li>
	<li>for any two tiles of the area there is a tile sequence connecting them, such that any two consecutive tiles of the sequence share a common side.</li>
</ul>

<p>In addition to the artistic idea, the jury has already developed a program that produces design of the panel. But since this problem is about art, any new solution is extremely important for the jury.</p>

### 입력 

 <p>The only line of the input file contains two integers b and w — number of black and white areas (1 ≤ b, w ≤ 1000).</p>

### 출력 

 <p>The first line of the output file should contain the picture sizes r and c — the number of rows and columns (1 ≤ r, c ≤ 100 000). This line should be followed by r lines of c symbols each. Each symbol should be either ‘@’ (for black tile) or ‘.’ (for white one). There should be no more than 100 000 tiles in the panel.</p>

