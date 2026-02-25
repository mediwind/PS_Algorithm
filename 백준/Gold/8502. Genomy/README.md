# [Gold II] Genomy - 8502 

[문제 링크](https://www.acmicpc.net/problem/8502) 

### 성능 요약

메모리: 34456 KB, 시간: 408 ms

### 분류

방향 비순환 그래프, 다이나믹 프로그래밍, 그래프 이론, 위상 정렬

### 제출 일자

2026년 2월 25일 23:49:03

### 문제 설명

<p>Biolodzy zajmujący się genetyką porównawczą poszukują sekwencji genów zachowanych w pewnym zbiorze gatunków.</p>

<p>Niech zbiór liczb {1,2,…,n} oznacza geny - każdej liczbie odpowiada jeden gen. Każdy z gatunków określony jest permutacją liczb (1,2,…,n}, która oznacza uporządkowanie jego genów. Ciąg genów x<sub>1</sub>,x<sub>2</sub>,…,x<sub>k</sub> jest zachowaną sekwencją genów w zbiorze gatunków, jeśli jest on podciągiem (niekoniecznie spójnym) uporządkowania genów każdego z tych gatunków.</p>

<p>Zadanie</p>

<p>Napisz program, który:</p>

<ul>
	<li>wczyta ze standardowego wejścia opis sekwencji genów,</li>
	<li>wyznaczy długość najdłuższej zachowanej sekwencji,</li>
	<li>zapisze odpowiedź na standardowe wyjście.</li>
</ul>

### 입력 

 <p>W pierwszej linii standardowego wejścia znajdują się dwie liczby całkowite n i m oddzielone pojedynczym odstępem, przy czym 1 ≤ n ≤ 500 oraz 1 ≤ m ≤ 20. Liczba n oznacza liczbę genów, a m liczbę gatunków. Każda z następnych m linii zawiera genom kolejnego gatunku zapisany jako permutacja liczb 1,2,…,n pooddzielanych pojedynczymi odstępami.</p>

### 출력 

 <p>Na wyjściu powinna zostać wypisana dokładnie jedna liczba całkowita równa długości najdłuższej zachowanej sekwencji genów.</p>

