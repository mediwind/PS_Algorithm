# [Gold I] Kamenčići - 23402 

[문제 링크](https://www.acmicpc.net/problem/23402) 

### 성능 요약

메모리: 148144 KB, 시간: 3616 ms

### 분류

다이나믹 프로그래밍, 누적 합, 게임 이론

### 제출 일자

2026년 1월 28일 21:31:20

### 문제 설명

<p>This summer, Antun and Branka stumbled upon a very interesting beach, which was completely covered with plastic ’pebbles’ brought by the sea from the containers that fell from the cargo ships. They decided to take back with them n of these pebbles, some red and some blue. Now that autumn has arrived, they are playing with the pebbles and reminiscing about the warm summer days.</p>

<p>Their game proceeds as follows: in the beginning, they place the n pebbles in a row. Then, Antun and Branka make moves in turn, each time removing one of the pebbles from one of the ends of the row, until someone obtains k red pebbles, losing the game. Antun moves first and is wondering whether he could win regardless of the moves Branka makes. Please help him and write a program which will answer his question.</p>

### 입력 

 <p>The first line contains two integers, n and k (1 ≤ k < n ≤ 350).</p>

<p>The second line contains a sequence of n characters <code>C</code> or <code>P</code>, where <code>C</code> denotes a red pebble, and <code>P</code> denotes a blue pebble. The character <code>C</code> appears at least 2k − 1 times.</p>

### 출력 

 <p>If Antun can win regardless of Branka’s moves, you should print <code>DA</code>, otherwise print <code>NE</code>.</p>

