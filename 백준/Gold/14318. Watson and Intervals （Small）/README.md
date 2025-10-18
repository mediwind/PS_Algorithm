# [Gold V] Watson and Intervals (Small) - 14318 

[문제 링크](https://www.acmicpc.net/problem/14318) 

### 성능 요약

메모리: 32412 KB, 시간: 136 ms

### 분류

브루트포스 알고리즘, 정렬, 스위핑

### 제출 일자

2025년 10월 18일 21:21:33

### 문제 설명

<p>Sherlock and Watson have mastered the intricacies of the language C++ in their programming course, so they have moved on to algorithmic problems. In today's class, the tutor introduced the problem of merging one-dimensional intervals. N intervals are given, and the <code>i</code>th interval is defined by the inclusive endpoints [L<sub>i</sub>, R<sub>i</sub>], where L<sub>i</sub> ≤ R<sub>i</sub>. </p>

<p>The tutor defined the covered area of a set of intervals as the number of integers appearing in at least one of the intervals. (Formally, an integer p contributes to the covered area if there is some j such that L<sub>j</sub> ≤ <code>p</code> ≤ R<sub>j</sub>.) </p>

<p>Now, Watson always likes to challenge Sherlock. He has asked Sherlock to remove exactly one interval such that the covered area of the remaining intervals is minimized. Help Sherlock find this minimum possible covered area, after removing exactly one of the N intervals.</p>

### 입력 

 <p>Each test case consists of one line with eight integers N, L<sub>1</sub>, R<sub>1</sub>, A, B, C<sub>1</sub>, C<sub>2</sub>, and M. N is the number of intervals, and the other seven values are parameters that you should use to generate the other intervals, as follows: </p>

<p>First define <code>x<sub>1</sub></code> = L<sub>1</sub> and <code>y<sub>1</sub></code> = R<sub>1</sub>. Then, use the recurrences below to generate <code>x<sub>i</sub>, y<sub>i</sub></code> for <code>i</code> = 2 to N:</p>

<ul>
	<li><code>x<sub>i</sub></code> = ( A*<code>x<sub>i-1</sub></code> + B*<code>y<sub>i-1</sub></code> + C<sub>1</sub> ) modulo M.</li>
	<li><code>y<sub>i</sub></code> = ( A*<code>y<sub>i-1</sub></code> + B*<code>x<sub>i-1</sub></code> + C<sub>2</sub> ) modulo M.</li>
</ul>

<p>We define L<sub>i</sub> = <code>min(x<sub>i</sub>, y<sub>i</sub>)</code> and R<sub>i</sub> = <code>max(x<sub>i</sub>, y<sub>i</sub>)</code>, for all <code>i</code> = 2 to N.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is the minimum possible covered area of all of the intervals remaining after removing exactly one interval.</p>

