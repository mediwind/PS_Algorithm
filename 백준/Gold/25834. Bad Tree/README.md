# [Gold V] Bad Tree - 25834 

[문제 링크](https://www.acmicpc.net/problem/25834) 

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

트리, 해 구성하기

### 제출 일자

2025년 10월 2일 23:56:23

### 문제 설명

<p>Binary Search Trees are supposed to speed up searches for items but this happens only when the height of the tree is much less than the total number of values stored in the tree. And, in programming contests, judges unfortunately try to make the “worst case data”. So invariably, in binary search tree problems, judges will make data where n nodes get inserted into a tree in a particular order so that the height of the tree is the worst case, n – 1.</p>

<p>Without loss of generality, let’s assume that the n items to be inserted into a binary search tree are 1, 2, 3, …, n. For n = 5, if we insert the values in this order: 5, 1, 4, 3, and 2, we get the following binary search tree of height 4:</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/e12001a5-a6ac-4678-80b6-4d9aaed00999/-/preview/" style="width: 82px; height: 169px;"></p>

<p>In fact, there are quite a few orderings of the first n positive integers that, when inserted into a binary search tree, create a binary search tree of height n – 1. Since you aspire to be a great judge one day for this contest, write a program to generate the k th lexicographical permutation of the first n positive integers that, when inserted into a binary search tree in that order, generates a binary search tree of height n – 1.</p>

<p>Given a positive integer n, and another positive integer k, determine the k th permutation, in lexicographical ordering, that when the items are inserted into a binary search tree in that order, generates a tree of height n – 1.</p>

### 입력 

 <p>There is only one input line; it contains two space separated integers: n (1 ≤ n ≤ 100), representing the number of nodes in the binary search tree, and k (1 ≤ k ≤ 10<sup>18</sup>), where we desire the k th lexicographical permutation of the first n integers which creates a binary search tree of height n – 1, when inserted in the order given in the permutation.</p>

### 출력 

 <p>Print the k th lexicographical permutation of the integers 1 through n of the permutations which, when the values are inserted into a binary search tree, create a tree of height n – 1. Output the permutation on a single line, following each number in the permutation with a space. If no such permutation exists, output –1 instead.</p>

