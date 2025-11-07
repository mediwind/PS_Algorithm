# [Gold V] Miser - 20711 

[문제 링크](https://www.acmicpc.net/problem/20711) 

### 성능 요약

메모리: 47360 KB, 시간: 168 ms

### 분류

다이나믹 프로그래밍, 그리디 알고리즘

### 제출 일자

2025년 11월 7일 21:45:34

### 문제 설명

<p>In some non-classical University, there is going to be an opening ceremony of the cafeteria in $n$ days. In front of the closed cafeteria, there is a sign with a number --- how many days are left before the opening.</p>

<p>For each day out of these $n$, the director of the cafeteria knows all the people who are coming to the University and are going to see the sign. The director has to choose a sign with a number each day, such that each person who is coming to the University sees that the number on the sign is decreasing. The director is a typical <em>miser</em> who spends as little money as possible and wants to order the minimum possible number of different signs. Your task is to help the director find this number.</p>

<p>Consider the first test case: person $1$ comes on days $1$, $2$ and $5$, and person $2$ comes on days $2$, $3$ and $4$. The director can order just four signs with numbers $1$, $2$, $3$ and $4$, to put a sign with $1$ on days $5$ and $4$, a sign with $2$ on day $3$, a sign with $3$ on day $2$, and a sign with $4$ on day $1$. Thus, person $1$ will see the signs $4$, $3$, and $1$ and person $2$ will see the signs $3$, $2$, and $1$.</p>

### 입력 

 <p>The first line of the input contains an integer $n$ --- the total number of days before the opening of the cafeteria. The next $n$ lines contain the description of each day. The description starts with the positive integer $k$ --- the number of people that come to the University this day. This integer is followed by $k$ distinct integers --- the identifiers of the people that come.</p>

<p>The sum of all $k$ over all days does not exceed $10^5$. Identifiers of people are positive and do not exceed $10^5$.</p>

### 출력 

 <p>Output one integer --- the minimum possible number of different signs that have to be ordered.</p>

