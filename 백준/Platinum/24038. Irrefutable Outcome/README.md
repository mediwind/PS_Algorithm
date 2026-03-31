# [Platinum IV] Irrefutable Outcome - 24038 

[문제 링크](https://www.acmicpc.net/problem/24038) 

### 성능 요약

메모리: 41928 KB, 시간: 6404 ms

### 분류

많은 조건 분기, 게임 이론, 그리디 알고리즘

### 제출 일자

2026년 3월 31일 21:45:01

### 문제 설명

<p>Izabella and Olga are playing a game alternating turns. Izabella plays first. The game starts with all game pieces arranged in a single row. The pieces come in two colors: indigo and orange. During Izabella's turns, she must choose and remove an indigo piece that is either the leftmost or rightmost piece remaining. During Olga's turns, she must choose and remove an orange piece that is either the leftmost or rightmost piece remaining. If at any point one of the players does not have a legal move (possibly because there are no pieces remaining), that player loses the game, and the other player is awarded $1$ point plus $1$ additional point for each piece that remains on the board.</p>

<p>We use an uppercase letter <code>I</code> to represent indigo pieces and an uppercase letter <code>O</code> to represent orange pieces. Suppose, for example, that they play with the following starting board: <code>IOIOOOII</code>.</p>

<p>On her first turn, Izabella can choose to remove either the leftmost or rightmost pieces, as both are indigo. Suppose she chooses the leftmost. Then, the board would become <code>OIOOOII</code>. Then, Olga would have no choice but to remove the new leftmost piece, as the rightmost piece is not orange, leaving <code>IOOOII</code>. Izabella can choose again, and this time she chooses the rightmost piece, leaving <code>IOOOI</code> for Olga's turn. At this point, Olga has no valid move, so Izabella won. Since there are $5$ pieces remaining, Izabella wins $1+5=6$ points in total.</p>

<p>Each player plays optimally trying to win and to maximize their own score. A player that cannot guarantee a win plays to minimize the opponent's score.</p>

<p>Given the starting board, can you find out who wins and what is their score?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, $T$. $T$ lines follow. Each line represents a test case and contains a string $B$ representing the status of the board. The $i$-th character in $B$ is <code>I</code> if the $i$-th piece from the left is indigo and <code>O</code> if it is orange.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y z</code>, where $x$ is the test case number (starting from 1), $y$ is the initial of the winner (<code>I</code> for Izabella or <code>O</code> for Olga), and $z$ is the score the winner gets.</p>

