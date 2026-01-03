# [Gold III] Cheap Trips - 16523 

[문제 링크](https://www.acmicpc.net/problem/16523) 

### 성능 요약

메모리: 33432 KB, 시간: 136 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2026년 1월 3일 23:56:49

### 문제 설명

<p>Nlogonia has a new scheme for public transportation. When the first trip of a passenger starts, it also starts a 120 minutes interval such that discounts are applied to some of the trips that the passenger starts before the end of the interval. The discount for the second trip is 50% of the regular cost, while the discount for each of the remaining trips up to the sixth trip (that is, four more trips) is 75% of the regular cost. Once the 120 minutes interval ends, a new trip starts a new interval having the same kind of discounts.</p>

<p>Ástor is an exchange student that has just arrived to Nlogonia. He wants to spend as little money as possible for making a sequence of trips. The first trip in the sequence can be started at any time. Each trip but the first one cannot be started before the previous trip in the sequence ends, although it can be delayed as much as needed. Given the duration and the regular cost of each trip in the sequence, can you tell Ástor the minimum cost he must afford so as to complete all the trips in the sequence?</p>

### 입력 

 <p>The first line contains an integer N (1 ≤ N ≤ 10<sup>4</sup>) representing the number of trips in the sequence. Each of the next N lines describes a trip with two integers D and C (1 ≤ D, C ≤ 1000), indicating respectively the duration (in minutes) and the regular cost of the trip.</p>

### 출력 

 <p>Output a single line with a number representing the minimum cost needed to complete all the trips in the order they appear in the input. The result must be output as a rational number with exactly two digits after the decimal point, rounded if necessary.</p>

