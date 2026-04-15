# [Gold III] Shuffles - 11232 

[문제 링크](https://www.acmicpc.net/problem/11232) 

### 성능 요약

메모리: 132864 KB, 시간: 740 ms

### 분류

수학, 애드 혹

### 제출 일자

2026년 4월 15일 21:47:53

### 문제 설명

<p>The most common technique for shuffling a deck of cards is called the Riffle or Dovetail shuffle. The deck is split into two stacks, which are then interleaved with each other. The deck can be split anywhere, and the two stacks can be interleaved in any way.</p>

<p>For example, consider a deck with 10 unique cards:</p>

<p>1 2 3 4 5 6 7 8 9 10</p>

<p>Split them somewhere:</p>

<p><span style="background-color:#b8cce4">1 2 3 4 5 6</span> <span style="background-color:#e5b8b7">7 8 9 10</span></p>

<p>And interleave them in some way:</p>

<p><span style="background-color:#b8cce4">1 2</span> <span style="background-color:#e5b8b7">7</span> <span style="background-color:#b8cce4">3</span> <span style="background-color:#e5b8b7">8 9</span> <span style="background-color:#b8cce4">4 5</span> <span style="background-color:#e5b8b7">10</span> <span style="background-color:#b8cce4">6</span></p>

<p>Do it again. Split them somewhere:</p>

<p><span style="background-color:#b8cce4">1 2 7</span> <span style="background-color:#e5b8b7">3 8 9 4 5 10 6</span></p>

<p>And interleave them in some way:</p>

<p><span style="background-color:#e5b8b7">3 8</span> <span style="background-color:#b8cce4">1</span> <span style="background-color:#e5b8b7">9 4 5</span> <span style="background-color:#b8cce4">2 7</span> <span style="background-color:#e5b8b7">10 6</span></p>

<p>This is one possible ordering after 2 shuffles. Suppose there are n unique cards, and that they start out perfectly ordered: 1, 2, 3, ..., n. Given an ordering of the deck, what is the smallest number of shuffles that could possibly put the deck in that order?</p>

### 입력 

 <p>Each input will consist of a single test case. Note that your program may be run multiple times on different inputs. Each test case will begin with a single integer n (1 ≤ n ≤ 1,000,000) indicating the number of cards in the deck. On the next line will be n unique integers c (1 ≤ c ≤ n), with a single space between them, indicating an ordering of the n cards. The values c are guaranteed to be a permutation of the numbers 1..n.</p>

### 출력 

 <p>Output a single line with a single integer indicating the minimum number of shuffles that could possibly put the deck in the given order. Output no spaces.</p>

