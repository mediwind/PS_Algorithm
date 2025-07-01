# [Gold III] Smaller Strings - 23007 

[문제 링크](https://www.acmicpc.net/problem/23007) 

### 성능 요약

메모리: 33192 KB, 시간: 8996 ms

### 분류

조합론, 수학, 문자열

### 제출 일자

2025년 7월 1일 13:30:20

### 문제 설명

<p>You are given an integer K and a string S of length N, consisting of lowercase letters from the first K letters of the English alphabet. Find the number of palindrome strings of length N which are lexicographically smaller than S and consist of lowercase letters from the first K letters of the English alphabet.</p>

<p>A string composed of ordered letters a<sub>1</sub>, a<sub>2</sub>, …, a<sub>n</sub> is lexicographically smaller than another string of the same length b<sub>1</sub>, b<sub>2</sub>, …, b<sub>n</sub> if a<sub>i</sub> < b<sub>i</sub>, where i is the first index where characters differ in the two strings. For example, the following strings are arranged in lexicographically increasing order: <code>aaa</code>, <code>aab</code>, <code>aba</code>, <code>cab</code>.</p>

<p>A palindrome is a string that is the same written forwards and backwards. For example, <code>anna</code>, <code>racecar</code>, <code>aaa</code> and <code>x</code> are all palindromes, while <code>ab</code>, <code>frog</code> and <code>yoyo</code> are not.</p>

<p>As the number of such strings can be very large, print the answer modulo 10<sup>9</sup> + 7.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, T. T test cases follow.</p>

<p>Each test case consists of two lines. The first line contains two integers N and K. The second line contains a string S of length N, consisting of lowercase letters.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where x is the test case number (starting from 1) and y is the number of lexicographically smaller palindrome strings modulo 10<sup>9</sup> + 7.</p>

