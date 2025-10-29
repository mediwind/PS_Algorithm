# [Gold V] DnD Dice - 28372 

[문제 링크](https://www.acmicpc.net/problem/28372) 

### 성능 요약

메모리: 34924 KB, 시간: 80 ms

### 분류

수학, 다이나믹 프로그래밍

### 제출 일자

2025년 10월 29일 22:32:26

### 문제 설명

<p>In <em>Dungeons & Dragons</em> (DnD) and many other role playing games, many actions are determined by dice rolls, and it is also quite common to use dice with different numbers of sides. The most common dice are those based on the five Platonic solids, the tetrahedron, cube, octahedron, dodecahedron and icosahedron, with $4$, $6$, $8$, $12$ and $20$ sides, respectively. In DnD terminology, these dice are usually called d4, d6, d8, d12 and d20.</p>

<p>As a dungeon master, you are currently designing a campaign for your group of players. In the final battle of this campaign, the players need to roll a combination of multiple dice with varying numbers of sides, and the action of the enemy is determined by the sum of the numbers on the dice that were rolled. For balancing purposes, you want to sort these sums based on how likely they are to occur, so that you can assign appropriate events to each of them.</p>

<p>Given the number of dice of each type, and assuming the sides of each die are numbered from $1$ to the number of sides, find all possible sums of dice rolls and output them sorted by non-increasing probability.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>One line with five integers $t$, $c$, $o$, $d$ and $i$, ($0 \le t, c, o, d, i \le 10$), giving the number of tetrahedra, cubes, octahedra, dodecahedra and icosahedra among the dice that are rolled. There is always at least one die, that is $t+c+o+d+i \ge 1$.</li>
</ul>

### 출력 

 <p>Output all possible sums, ordered from most likely to least likely. If two sums occur with the same probability, then those sums may be printed in any relative order.</p>

