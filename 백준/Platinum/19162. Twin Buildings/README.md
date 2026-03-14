# [Platinum V] Twin Buildings - 19162 

[문제 링크](https://www.acmicpc.net/problem/19162) 

### 성능 요약

메모리: 46504 KB, 시간: 296 ms

### 분류

정렬

### 제출 일자

2026년 3월 14일 21:51:17

### 문제 설명

<p>As you might already know, space has always been a problem in ICPC Jakarta. To cope with this, ICPC Jakarta is planning to build <strong>two</strong> new buildings. These buildings should have a shape of a rectangle of the same size. Now, their problem is to find land to build the buildings.</p>

<p>There are N lands available for sale. The i<sup>th</sup> land has a rectangular shape of size L<sub>i</sub> × W<sub>i</sub>. For a good feng shui, the building’s side should be parallel to the land’s sides.</p>

<p>One way is to build the two buildings on two different lands, one on each land (not necessarily with the same orientation). A building of size A × B can be build on the i<sup>th</sup> land if and only if at least one of the following is satisfied:</p>

<ul>
	<li>A ≤ L<sub>i</sub> and B ≤ W<sub>i</sub>, or</li>
	<li>A ≤ W<sub>i</sub> and B ≤ L<sub>i</sub>.</li>
</ul>

<p>Alternatively, it is also possible to build two buildings of A × B on the i<sup>th</sup> land with the same orientation. Formally, it is possible to build two buildings of A×B on the i<sup>th</sup> land if and only if at least one of the following is satisfied:</p>

<ul>
	<li>A × 2 ≤ L<sub>i</sub> and B ≤ W<sub>i</sub>, or</li>
	<li>A × 2 ≤ W<sub>i</sub> and B ≤ L<sub>i</sub>, or</li>
	<li>A ≤ L<sub>i</sub> and B × 2 ≤ W<sub>i</sub>, or</li>
	<li>A ≤ W<sub>i</sub> and B × 2 ≤ L<sub>i</sub>.</li>
</ul>

<p>Your task in this problem is to help ICPC Jakarta to figure out the largest possible buildings they can build given N available lands. Note that ICPC Jakarta has to build two buildings of A × B; output the largest possible for A × B.</p>

### 입력 

 <p>Input begins with a line containing an integer: N (1 ≤ N ≤ 100 000) representing the number of available lands. The next N lines each contains two integers: L<sub>i</sub> W<sub>i</sub> (1 ≤ L<sub>i</sub>, W<sub>i</sub> ≤ 10<sup>9</sup>) representing the size of the land.</p>

### 출력 

 <p>Output in a line a number representing the largest building that ICPC Jakarta can build with exactly one decimal point (see sample input/output for clarity).</p>

