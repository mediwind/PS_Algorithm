# [Gold V] REZ - 2801 

[문제 링크](https://www.acmicpc.net/problem/2801) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

애드 혹, 해 구성하기, 기하학, 수학

### 제출 일자

2025년 3월 20일 12:20:22

### 문제 설명

<p>Let‟s say that there exists a huge cake made from blueberries, strawberries and chocolate. It‟s shaped like a square, and has area of 100 square meters. Proffesionals strongly advise that cake is being cut with wet knife and eaten with dry spoon. Also:</p>

<ul>
	<li>Every cut begins and ends on the cake's perimeter</li>
	<li>A cut cannot lie completely on one of the sides</li>
	<li>No two cuts have the same starting and ending points, i.e. all cuts are different</li>
</ul>

<p>Parts obtained by these cuts are separated and counted only after last cut has been made. During cutting, the cake keeps its square form.</p>

<p>At least how many cuts need to be made in order to obtain at least K parts? Exactly what cuts to make?</p>

### 입력 

 <p>The first and only line of input contains an integer K (1 ≤ K ≤ 1 000 000), minimum number of parts that we must have after cutting is done.</p>

### 출력 

 <p>The first line of output should contain the requested number of cuts, N.</p>

<p>The following N lines should have four integers each, coordinates of starting and ending point for each cut made. Coordinates are represented in millimeters, and opposing corners of the cake have coordinates (-5000, -5000) and (5000, 5000). So for each point (x, y) lying on the side of the square, the following will hold:</p>

<p style="text-align: center;">max( |x|, |y| ) = 5000.</p>

