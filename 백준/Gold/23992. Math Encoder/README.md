# [Gold V] Math Encoder - 23992 

[문제 링크](https://www.acmicpc.net/problem/23992) 

### 성능 요약

메모리: 34456 KB, 시간: 100 ms

### 분류

수학, 조합론

### 제출 일자

2025년 10월 31일 22:39:41

### 문제 설명

<p>Professor Math is working on a secret project and is facing a challenge where a list of numbers need to be encoded into a single number in the most efficient manner. After much research, Professor Math finds a 3 step process that can best encode the numbers:</p>

<ol>
	<li>The first step is to find all possible non-empty subsets of the list of numbers and then, for each subset, find the difference between the largest and smallest numbers (that is, the largest minus the smallest) in that subset. Note that if there is only one number in a subset, it is both the largest and the smallest number in that subset. The complete set itself is also considered a subset.</li>
	<li>Then add up all the differences to get the final encoded number.</li>
	<li>As the number may be large, output the number modulo 10<sup>9</sup> + 7 (1000000007).</li>
</ol>

<p>The professor has shared an example and its explanation below. Given a list of numbers, can you help the professor build an efficient function to compute the final encoded number?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <b>T</b>. This is followed by T test cases where each test case is defined by 2 lines:</p>

<ol>
	<li>The first line gives a positive number <b>N</b>: the number of numbers in the list and</li>
	<li>The second line contains a list of <b>N</b> positive integers <b>K<sub>i</sub></b>, sorted in non-decreasing order.</li>
</ol>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is the final encoded number.</p>

<p>Since the output can be a really big number, we only ask you to output the remainder of dividing the result by the prime 10<sup>9</sup> + 7 (1000000007).</p>

