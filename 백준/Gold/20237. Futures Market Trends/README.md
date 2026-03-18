# [Gold IV] Futures Market Trends - 20237 

[문제 링크](https://www.acmicpc.net/problem/20237) 

### 성능 요약

메모리: 38408 KB, 시간: 3084 ms

### 분류

브루트포스 알고리즘, 수학, 누적 합, 통계학

### 제출 일자

2026년 3월 18일 23:47:25

### 문제 설명

<p>Fedor wants to earn some extra money out of oil futures. His analysis is based on <em>trends</em> and historical data of $d$ previous days.</p>

<p>A cost sequence of at least three distinct days $c_0, c_1, c_2, \cdots, c_n$ forms a <em>trend of power $P$</em> if average cost change is at least $P$ times bigger than the standard deviation of cost changes.</p>

<p>Formally, average cost change is $A = \frac{1}{n}\sum\limits_{i=1}^n \left(c_i - c_{i-1}\right)$. The standard deviation of cost changes is $D = \sqrt{\frac{1}{n}\sum\limits_{i=1}^n{\left(c_i - c_{i-1} - A\right)^2}}$. The sequence forms a <em>positive trend of power $P$</em> if $\frac{A}{D} \ge P$, and a <em>negative trend of power $P$</em> if $\frac{A}{D} \le -P$. </p>

<p>We assume that if $A > 0$ and $D = 0$ then a positive trend of any power is formed. Similarly, if $A < 0$ and $D = 0$ then a negative trend of any power is formed. If $A = 0$ then no trend is formed, even if $D = 0$.  </p>

<p>To check his theory, Fedor needs to count the number of subsegments of historical data which form positive and negative trends of the given power. Can you help him?</p>

### 입력 

 <p>The first line contains an integer $d$ ($3 \le d \le 3\,000$) and a real number $P$ ($0.001 \le P \le 1000$) --- the number of days in Fedor's historical data and the required trend power. $P$ is given with at most 9 digits after the decimal point.  </p>

<p>The next line contains $d$ integers $c_1, c_2, \ldots, c_d$ ($-1000 \le c_i \le 1000$). For each $i$, $c_i$ is the cost of oil futures at the end of the $i$-th day. </p>

### 출력 

 <p>Print two integers --- the number of subsegments of historical data forming a positive and a negative trend of power $P$, respectively. It's guaranteed that the answer would not change if one changes $P$ by no more than $10^{-8}$.</p>

