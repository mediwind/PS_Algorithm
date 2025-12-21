# [Gold III] Domino tiling - 6622 

[문제 링크](https://www.acmicpc.net/problem/6622) 

### 성능 요약

메모리: 34456 KB, 시간: 288 ms

### 분류

백트래킹

### 제출 일자

2025년 12월 21일 23:57:21

### 문제 설명

<p>The aliens want to dominate the whole universe. So it comes as no surprise that their favorite game is played with domino tiles. A domino tile is a tile of size 1 × 2 with a digit 0-9 written on each half. Their game board is a rectangular array with a digit 0-9 written in each unit square. The task is to cover the whole board with the set of provided domino tiles. The tiles can be placed only if the two numbers on the tile equal the two numbers in the unit squares covered by the tile. The tiles can be placed as they are or may be rotated by 90<sup>◦</sup>, 180<sup>◦</sup> or 270<sup>◦</sup>. No two tiles may overlap. You can always use only one piece of each provided tile.</p>

<p>Some tiles are already placed on the board. These must stay where they are.</p>

<p>You are to write a program that will play this game. If you do not succeed, our planet will be dominated!</p>

### 입력 

 <p>The input contains several descriptions of game settings. The first line of each description contains three numbers separated by one or more spaces. The first two numbers are the height M and the width N of the board. They satisfy 1 ≤ M ≤ 20, 1 ≤ N ≤ 20, at least one of them is even, and their product 2 ≤ M · N ≤ 110 (guess why). The last number is the number of available tiles K, 1 ≤ K ≤ M · N/2.</p>

<p>The next line contains K pairs of space-separated integers describing the pairs of numbers on the available tiles. Each two consecutive numbers on this line are separated by at least one space. In addition, no two tiles are identical, that is, they are different (and stay different even if one is rotated by 180◦). The tiles already placed on the board are not among these K tiles.</p>

<p>The following M lines contain N space-separated entries each. For every i,j, 0 ≤ i < M, 0 ≤ j < N, the jth entry in the ith row describes the place in the ith row and jth column of the gameboard. The entry is either the capital letter “X” if there is an already-placed tile, or a number A<sub>i,j</sub> (0 ≤ A<sub>i,j</sub> ≤ 9) written on the board.</p>

<p>Every description is followed by an empty line and the empty line after the last description is followed by a line containing three zeros.</p>

### 출력 

 <p>For each game, find a way to place all tiles onto the board. If there are more solutions, output any of them. Provide the solution by a graphic representation as an M × N array with “[” and “]” (square brackets) standing for the left and right half of a horizontally placed domino, and lowercase letters “n” and “u” for the upper and lower half of a vertically placed domino. The squares covered by a tile in the input are still represented by “X”. After the M rows, print one line containing the number of other different solutions that exist.</p>

<p>Do not output any spaces and start a new line for each row of the gameboard.</p>

<p>If there is no solution, write a single line with the word “impossible”.</p>

<p>Print one empty line after the each gameboard result.</p>

