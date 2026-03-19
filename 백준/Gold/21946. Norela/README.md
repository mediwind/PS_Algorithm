# [Gold IV] Norela - 21946 

[문제 링크](https://www.acmicpc.net/problem/21946) 

### 성능 요약

메모리: 33432 KB, 시간: 64 ms

### 분류

브루트포스 알고리즘, 비트마스킹

### 제출 일자

2026년 3월 19일 23:52:49

### 문제 설명

<p>Adrian the 3rd is a wizard prince. On International Wizard’s Day (4th of November) he wanted to impress Norela, his dream girl. He has n playing cards, which are initially put with the face down on a table. Adrian can use m spells, a spell has the format: q a<sub>1</sub> a<sub>2</sub> … a<sub>q</sub>. If Adrian uses a spell, the playing cards with the indices a<sub>1</sub> a<sub>2</sub> … a<sub>q</sub> will be turned in order. (Integers a<sub>1</sub> a<sub>2</sub> … a<sub>q</sub> are all different). The card will be turn face up if it is face down and will be turned face down if it is face up and all spells can be used no more than one time. Help Adrian impress Norela before his nemesis Manea Long Eyebrow does it!</p>

<p>Find the minimum number of spells that have to be used to turn all n cards face up, also determinate the indices of the used spells. If there are more solutions, print the minimum lexicographical answer.</p>

### 입력 

 <p>The first line contains two integers n and m.</p>

<p>The next m lines contain the description of every spell q a<sub>1</sub> a<sub>2</sub> … a<sub>q</sub>, where q is the number of cards that will be turned by that spell and a<sub>1</sub> a<sub>2</sub> … a<sub>q</sub> are the indices of those cards.</p>

### 출력 

 <p>The first line will contain only one integer representing the minimum number of used spells and the second line will contain the indices of those spells. If there are more solutions with minimum number of used spells, there will be printed the minimum lexicographical answer.</p>

