# [Platinum III] Watch Where You Step - 16875 

[문제 링크](https://www.acmicpc.net/problem/16875) 

### 성능 요약

메모리: 309204 KB, 시간: 5968 ms

### 분류

그래프 이론, 방향 비순환 그래프, 플로이드–워셜, 강한 연결 요소

### 제출 일자

2026년 4월 12일 23:27:31

### 문제 설명

<p>You are an employee at the local zoo and have recently been promoted from excretory extraction to overseeing the layout of all the sidewalks throughout the property. Currently all the sidewalks are 1-way, and the zoo is set up in various zones. Each zone is made up of a set of attractions (elephant enclosure, lizard house, etc.), and within any one zone you can get from any attraction to any other attraction in the zone using one or more sidewalks. Once you take a sidewalk from one zone to another you can never return to the zone you left. However, it is possible to walk to every zone in a single visit to the zoo. The original designers thought this arrangement was very important to help control the flow of visitors to the zoo.</p>

<p>The members of the board of directors have come to you with a problem. They agree with the original designers in the use of zones, but they feel that more one-way sidewalks could be included to make the zoo a little more patron-friendly. They would like you to figure out the maximum number of sidewalks that could be added so as not to introduce a path between any two attractions which didn’t have one between them before.</p>

<p>For example, consider the small zoo shown in Figure J.1, with 7 attractions labeled 1 (the “Camel Castle”) through 7 (the “Hippo Hippodrome”). Currently attractions 1, 2, 3 and 4 form one zone and 5, 6 and 7 form another. You can add sidewalks from 1, 2, 3 or 4 to either 5, 6 or 7, but adding a sidewalk from (say) 7 to 1 would allow patrons to get from 7 to 1, which was impossible previously. Note that you can also add sidewalks between all attractions within a zone which don’t already exist (for example, from 1 to 3 or from 2 to 4). The total number of possible new sidewalks for this zoo would be 21.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/0376f84e-cbf6-4de0-8f0d-131952fc5be4/-/preview/" style="width: 312px; height: 184px;"></p>

<p style="text-align: center;">Figure J.1: Sample zoo. This example corresponds to Sample Input 1.</p>

### 입력 

 <p>Input starts with a line containing an integer n (1 ≤ n ≤ 2 500), the number of attractions, labeled 1 to n. After this are n lines each containing n integers. If the j<sup>th</sup> integer on the i<sup>th</sup> of these lines is a 1 it indicates that there is a one-way sidewalk from attraction i to attraction j; otherwise this integer will be a 0 indicating no such sidewalk is present. There is never a sidewalk from an attraction to itself.</p>

### 출력 

 <p>Display the maximum number of new one-way sidewalks that could be added to the zoo.</p>

