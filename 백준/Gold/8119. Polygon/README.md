# [Gold IV] Polygon - 8119 

[문제 링크](https://www.acmicpc.net/problem/8119) 

### 성능 요약

메모리: 38048 KB, 시간: 232 ms

### 분류

깊이 우선 탐색, 그래프 이론, 그래프 탐색, 재귀

### 제출 일자

2026년 3월 5일 21:28:57

### 문제 설명

<p>We are given a convex polygon P of n sides (where 3 < n ≤ 5,000) and k its distinct diagonals not crossing one another inside the polygon. (The only point that two distinct diagonals may share is a vertex of the polygon.) Vertices of the polygon are numbered successively from 1 to n counterclockwise. All the diagonals divide P into smaller convex polygons whose interiors do not intersect.</p>

<p>Four diagonals: 1-8, 8-3, 3-1 and 3-6 divide the polygon P shown in the picture below into two quadrilaterals and three triangles.</p>

<p style="text-align: center;"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/8119/1.gif" style="width: 323px; height: 326px;"></p>

<p>Write a program that:</p>

<ul>
	<li>reads a description of the polygon P and its diagonals from the standard input,</li>
	<li>calculates the maximal number of sides of a polygon among the polygons created by the division of P by the given diagonals,</li>
	<li>writes the result in the standard output.</li>
</ul>

### 입력 

 <p>In each line of the standard input two positive integers separated by a single space are written.</p>

<p>In the first line there is the number of vertices n of the polygon and the number of diagonals k.</p>

<p>In each of the following k lines there is a description of one diagonal of the polygon in the form of a pair of positive integers. These integers are the numbers of the vertices of the polygon the diagonal joins. Just after the second number there is the end of the line.</p>

<p>The data in the standard input are written correctly and your program need not verify that.</p>

### 출력 

 <p>In the standard output one should write one positive integer - the maximal number of sides of a convex polygon created by the division of the given polygon P.</p>

