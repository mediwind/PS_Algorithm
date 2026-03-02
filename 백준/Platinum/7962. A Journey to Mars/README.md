# [Platinum IV] A Journey to Mars - 7962 

[문제 링크](https://www.acmicpc.net/problem/7962) 

### 성능 요약

메모리: 279164 KB, 시간: 3996 ms

### 분류

자료 구조, 세그먼트 트리, 누적 합, 덱, 슬라이딩 윈도우, 덱을 이용한 구간 최댓값 트릭

### 제출 일자

2026년 3월 2일 21:51:22

### 문제 설명

<p>Byteazar has decided on going to Mars to tour the space stations there being in existence. All marsian space stations lie on a circumference of a circle. Byteazar lands in one of them and then moves around by means of a special vehicle which is powered by an appropriate fuel. A litre of this fuel allows him to travel one meter. However, the provisions of the fuel are meagre, different quantities of it are available in each space station. Byteazar may refuel in the space station he is currently in, though he cannot get more fuel than it is available in that very place (the capacity of his fuel tank is unlimited). This quantity of fuel should allow him to reach the next space station. Byteazar has to decide where to land, so that he can visit all of the space stations. In the end he has to return to the space station in which he has landed. During his journey Byteazar has to travel on the circumference of the circle, constantly in one of the two possible directions.</p>

<p>Write a programme which:</p>

<ul>
	<li>reads from the standard input the number of space stations, distances between them and the amount of fuel available in each of them,</li>
	<li>for each of the space stations checks, whether Byteazar can land there i.e. whether by starting in that very station and travelling in a freely chosen direction he is able to visit all of the space stations and return to his spaceship,</li>
	<li>writes the outcome to the standard output.</li>
</ul>

<p> </p>

### 입력 

 <p>The first line of the standard input contains a single integer N (3 ≤ N ≤ 1,000,000). It denotes the number of space stations on Mars. The space stations are numbered from 1 to N. In the next N lines there is a description of all of the stations and the distances between them. The (i+1)’st line contains two integers pi and di (pi ≤ 0, di > 0). The first one denotes the amount of fuel (in litres) available in the i’th space station. The other denotes the distance (in metres) between the i’th and (i+1)’st space station (obviously dN denotes the distance between the N’th and the 1st space station). The total amount of available fuel, as well as the sum of all distances between the space stations does not exceed 2,000,000,000.</p>

<p> </p>

### 출력 

 <p>The programme should write N lines to the standard output. The i’th line should contain the word TAK (i.e. yes is Polish), if Byteazar can land in the i’th space station or NIE (i.e. no in Polish) when it is not possible.</p>

<p> </p>

