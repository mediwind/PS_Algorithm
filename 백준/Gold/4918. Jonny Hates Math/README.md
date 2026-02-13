# [Gold III] Jonny Hates Math - 4918 

[문제 링크](https://www.acmicpc.net/problem/4918) 

### 성능 요약

메모리: 71040 KB, 시간: 11096 ms

### 분류

수학, 다이나믹 프로그래밍, 자료 구조, 집합과 맵, 사칙연산, 역추적

### 제출 일자

2026년 2월 13일 23:17:38

### 문제 설명

<p>Johnny is on probation! He has failed so many math courses and the Department has forced him to register in a remedial math course. He must pass the course or he’d be expelled from the University. In an attempt to impress his professor, Johnny is typing all his assignments on the computer. The latest assignment is rather simple, Johnny was given a set of problems to solve. Each problem had a list of one or more numbers that Johnny was supposed to add. Johnny has worked all night on the assignment, neatly typing his solution to each problem using a word processor as seen here:</p>

<p>4+12+3=19</p>

<p>As usual, Johnny woke up late, he hardly had the time to print the assignment and rush to class. Only in the classroom did he discover that, due to a printer driver problem, non of the plus signs were printed. The above line was printed as:</p>

<p>4123=19</p>

<p>Write a program to figure out where the pluses are supposed to be. All what Johnny remembers is that all the numbers were positive; None of the numbers, other than possibly the sum, had more than 5 digits; And none of the numbers had a zero as the left-most digit.</p>

### 입력 

 <p>Your program will be tested on one or more expressions. Each expression is specified on a single line. No line will be longer than 256 characters. The last line, which is not part of the test cases, will be 0=0.</p>

### 출력 

 <p>For each expression in the input, your program must print a line of the form:</p>

<p>k.␣result</p>

<p>Where k is the expression number (starting at 1,) ␣ is a single space, and result is the expression with the necessary plus signs in place. There are no spaces in result. If there are more than one possible solution, print a solution that requires the least number of plus signs. Knowing how bad Johnny is in arithmetic, it is possible that there is no solution, in which case your program should print "IMPOSSIBLE" as the result.</p>

