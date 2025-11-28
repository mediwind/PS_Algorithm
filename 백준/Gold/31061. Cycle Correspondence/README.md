# [Gold II] Cycle Correspondence - 31061 

[문제 링크](https://www.acmicpc.net/problem/31061) 

### 성능 요약

메모리: 160008 KB, 시간: 824 ms

### 분류

그리디 알고리즘, 애드 혹

### 제출 일자

2025년 11월 28일 21:06:00

### 문제 설명

<p>Farmer John has $N$ barns ($3\le N\le 5\cdot 10^5$), of which $K$ ($3\le K\le N$) distinct pairs of barns are connected.</p>

<p>First, Annabelle assigns each barn a distinct integer label in the range $[1,N]$, and observes that the barns with labels $a_1,\dots,a_K$ are connected in a cycle, in that order. That is, barns $a_i$ and $a_{i+1}$ are connected for all $1\le i<K$, and barns $a_K$ and $a_1$ are also connected. All $a_i$ are distinct.</p>

<p>Next, Bessie also assigns each barn a distinct integer label in the range $[1,N]$ and observes that the barns with labels $b_1,\dots,b_K$ are connected in a cycle, in that order. All $b_i$ are distinct.</p>

<p>Some (possibly none or all) barns are assigned the same label by Annabelle and Bessie. Compute the maximum possible number of barns that are assigned the same label by Annabelle and Bessie.</p>

### 입력 

 <p>The first line contains $N$ and $K$.</p>

<p>The next line contains $a_1,\dots, a_K$.</p>

<p>The next line contains $b_1,\dots, b_K$.</p>

### 출력 

 <p>The maximum number of fixed points.</p>

