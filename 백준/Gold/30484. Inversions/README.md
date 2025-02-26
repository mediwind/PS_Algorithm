# [Gold III] Inversions - 30484 

[문제 링크](https://www.acmicpc.net/problem/30484) 

### 성능 요약

메모리: 32412 KB, 시간: 108 ms

### 분류

조합론, 수학

### 제출 일자

2025년 2월 26일 19:34:11

### 문제 설명

<p>Every year, mathematicians and computer scientists from around the globe gather for the prestigious Inversion Counting Puzzle Contest (ICPC). For the next ICPC, the organizers had prepared the following challenge: given a string S consisting of lowercase letters, count the number of inversions in it. An inversion is a pair of indices i < j such that S<sub>i</sub> (the letter at position i) comes after S<sub>j</sub> in the alphabet.</p>

<p>However, just last month, a group of outstanding researchers devised a sophisticated algorithm that can count the inversions in a string extremely fast. While this was great news for the advancement of science, it has been a nightmare for the ICPC staff, since their planned challenge is now obsolete.</p>

<p>This issue escalated to the head problem setter, who then presented a clever idea. Instead of simply receiving a string S, they should ask participants to repeat this string N times before counting the inversions. If the judges then set N to be large enough, at some point the algorithm proposed by the researchers will start to be too slow. Happy with this idea, the ICPC staff went ahead with organizing the next contest.</p>

<p>Unfortunately, now the judges don’t know the answers to the input files anymore, and therefore can’t judge submissions! The ICPC has just kicked off, and participants are about to start submitting their solutions. Please help the judges by computing the answers, so that the ICPC can run smoothly.</p>

### 입력 

 <p>The first line contains a string S (1 ≤ |S| ≤ 10<sup>5</sup>), which is made of lowercase letters.</p>

<p>The second line contains an integer N (1 ≤ N ≤ 10<sup>12</sup>) indicating how many times the string S is to be repeated.</p>

### 출력 

 <p>Output a single line with an integer indicating the number of inversions in the string S<sup>N</sup> (S repeated N times). Because this number can be very large, output the remainder of dividing it by 10<sup>9</sup> + 7.</p>

