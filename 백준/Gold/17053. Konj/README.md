# [Gold II] Konj - 17053 

[문제 링크](https://www.acmicpc.net/problem/17053) 

### 성능 요약

메모리: 91224 KB, 시간: 1080 ms

### 분류

너비 우선 탐색, 그래프 이론, 그래프 탐색, 구현, 스위핑

### 제출 일자

2026년 1월 24일 22:07:07

### 문제 설명

<p>Domagoj loves drawing horses at leisure. For a long time, he's been a proud member of social groups dealing with this subject. But Domagoj is a very special boy, so because of his drawing technique most people do not understand his masterpieces.</p>

<p>One of his most famous drawings is "#define HORSE 42-42", also known as "Ordinary Horse".</p>

<pre>15
2 2 6 2
2 2 2 6
6 2 6 4
6 4 6 6
2 6 6 6
6 2 8 2
8 2 10 2
10 2 12 2
12 2 12 4
12 4 6 4
6 2 6 1
8 2 8 0
10 2 10 1
12 2 12 0
42 42 42 43
2 2</pre>

<p>You must be wondering "Where is that horse?" and "Is everything all right with Domagoj?" because you only see some numbers on the drawing. The first question will be answered in the next section, while the answer to the second question also interests the author of this task.</p>

<p>In order to understand the drawing, you need to understand Domagoj's drawing technique. The first number in the drawing is the number N denoting the number of line segments that may have been drawn. Thereafter, the following N lines have four numbers, A<sub>i</sub>, B<sub>i</sub>, C<sub>i</sub> and D<sub>i</sub>, which describe the i<sup>th</sup> line segment extending from the point (A<sub>i</sub>, B<sub>i</sub>) to the point (C<sub>i</sub>, D<sub>i</sub>). In the last line of the drawing there are two numbers, X and Y, the coordinates of point T. Domagoj will draw all the line segments that contain the point T and all that are directly or indirectly connected to a line segment that contains point T. For two line segments L<sub>1</sub> and L<sub>2</sub> we say that they are directly connected if they have a common end point, and they are indirectly connected if there is a sequence of line segments L<sub>1</sub>, H<sub>1</sub>, H<sub>2</sub>, … H<sub>k</sub>, L<sub>2</sub> such that the line segments L<sub>1</sub> and H<sub>1</sub> are directly connected, H<sub>1</sub> and H<sub>2</sub> are directly connected, ..., H<sub>k</sub> and L<sub>2</sub> are directly connected.</p>

<p>Your task is to print a rectangular matrix P of characters that displays Domagoj's drawing. The value of P<sub>a,b</sub> should be set to '#' if the point with the coordinates (a, b) is part of some line segment drawn, otherwise this value should be set to '.'. Coordinate a in the matrix rises from left to right, while coordinate b rises from bottom up. Matrix P should contain all points that are part of a drawn lines and should not contain any single row or column that contains only characters '.', i.e. it should be minimal in size.</p>

### 입력 

 <p>In the first line of the input there is a positive integer N (1 ≤ N ≤ 200 000).</p>

<p>In the next N lines there four non-negative integers A<sub>i</sub>, B<sub>i</sub>, C<sub>i</sub> and D<sub>i</sub> (0 ≤ A<sub>i</sub>, B<sub>i</sub>, C<sub>i</sub>, D<sub>i</sub> ≤ 300). For each line segment it will hold either Ai ≠ Ci or Bi ≠ Di. No two line segments will intersect, but some might have common end point. All the will be parallel to the coordinate axes.</p>

<p>In the last line of the input there will be two non-negative integers X and Y, coordinates of the point T. Point T will be part of at least one of the given line segment.</p>

### 출력 

 <p>Print required matrix P from the task.</p>

