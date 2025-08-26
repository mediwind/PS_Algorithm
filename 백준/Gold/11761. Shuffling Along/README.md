# [Gold V] Shuffling Along - 11761 

[문제 링크](https://www.acmicpc.net/problem/11761) 

### 성능 요약

메모리: 34536 KB, 시간: 40 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 8월 26일 22:35:02

### 문제 설명

<p>Most of you have played card games (and if you haven’t, why not???) in which the deck of cards is randomized by shuffling it one or more times.</p>

<p>A perfect shuffle is a type of shuffle where the initial deck is divided exactly in half, and the two halves are perfectly interleaved. For example, a deck consisting of eight cards ABCDEFGH (where A is the top card of the deck) would be divided into two halves ABCD and EFGH and then interleaved to get AEBFCGDH. Note that in this shuffle the original top card (A) stays on top — this type of perfect shuffle is called an out-shuffle. An equally valid perfect shuffle would start with the first card from the second half and result in EAFBGCHD — this is known as an in-shuffle.</p>

<p>While normal shuffling does a good job at randomizing a deck, perfect shuffles result in only a small number of possible orderings. For example, if we perform multiple out-shuffles on the deck above, we obtain the following:</p>

<p style="text-align: center;">ABCDEFGH → AEBFCGDH → ACEGBDFH → ABCDEFGH → · · ·</p>

<p>So after 3 out-shuffles, the deck is returned to its original state. A similar thing happens if we perform multiple in-shuffles on an 8-card deck, though in this case it would take 6 shuffles before we get back to where we started. With a standard 52 card deck, only 8 out-shuffles are needed before the deck is returned to its original order (talented magicians can make use of this result in many of their tricks). These shuffles can also be used on decks with an odd number of cards, but we have to be a little careful: for out-shuffles, the first half of the deck must have 1 more card than the second half; for in-shuffles, it’s the exact opposite. For example, an out-shuffle on the deck ABCDE results in ADBEC, while an in-shuffle results in CADBE.</p>

<p>For this problem you will be given the size of a deck and must determine how many in- or outshuffles it takes to return the deck to its pre-shuffled order.</p>

### 입력 

 <p>The input consists of one line containing a positive integer n ≤ 1000 (the size of the deck) followed by either the word in or out, indicating whether you should perform in-shuffles or out-shuffles.</p>

### 출력 

 <p>For each test case, output the case number followed by the number of in- or out-shuffles required to return the deck to its original order.</p>

