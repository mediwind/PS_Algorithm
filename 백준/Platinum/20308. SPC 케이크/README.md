# [Platinum III] SPC 케이크 - 20308 

[문제 링크](https://www.acmicpc.net/problem/20308) 

### 성능 요약

메모리: 33972 KB, 시간: 304 ms

### 분류

정렬, 기하학, 스위핑, 두 포인터, 각도 정렬

### 제출 일자

2026년 4월 13일 22:45:39

### 문제 설명

<p><u><a href="https://acm.sogang.ac.kr">SPC(Sogang Premium Cake) 제과점</a></u>은 직사각형 <span style="color:#d35400;">초</span><span style="color:#1abc9c;">콜</span><span style="color:#d35400;">릿</span>이 올려진 직사각형 모양의 케익만 판매한다.</p>

<p>Mr. K는 심심하지 않게 케익 조각을 다음과 같은 방법으로 잘라 먹으려고 한다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/a4bcf151-ad27-44a0-bd3c-2d6085dd21e7/-/preview/" style="width: 365px; height: 300px;"><br>
<img alt="" src="https://upload.acmicpc.net/4502381c-0fc9-4591-9215-311117229387/-/preview/" style="height: 400px; width: 855px;"></p>

<p style="text-align: center;">- 예제 입력 1에 대해 케이크를 자를 수 있는 방법들 -</p>

<ol>
	<li>그림과 같이 가로와 세로의 길이가 $W$, $H$인 SPC케익을 1사분면 위에 고정한다.</li>
	<li>케익의 꼭짓점을 포함한 오른쪽과 윗변 위의 정수 좌표의 점들 중 두 개($A$, $B$)를 $L = \left|x_A-x_B\right|+\left|y_A-y_B\right|$이 되도록 선택한다.</li>
	<li>케익의 왼쪽 아래 꼭짓점 $O(0, 0)$으로부터 선분 $\overline{OA}$, $\overline{OB}$를 긋는다.</li>
	<li>선분 $\overline{OA}$, $\overline{OB}$에 둘러싸인 케익 조각을 잘라내어 먹는다. 이 때, Mr.K는 선분으로 잘려진 <span style="color:#1abc9c;">초</span><span style="color:#d35400;">콜</span><span style="color:#1abc9c;">릿</span>은 먹지 않고 온전히 남아 있는 <span style="color:#d35400;">초</span><span style="color:#1abc9c;">콜</span><span style="color:#d35400;">릿</span>만 먹는다. 이 때, 선분이 <span style="color:#1abc9c;">초</span><span style="color:#d35400;">콜</span><span style="color:#1abc9c;">릿</span>을 관통하지 않고 꼭짓점과만 만날 때는 잘리지 않은 것으로 간주한다.</li>
	<li><span style="color:#d35400;">초</span><span style="color:#1abc9c;">콜</span><span style="color:#d35400;">릿</span>은 서로 겹치지 않고, 케익의 모서리에 닿지 않으며, 그림과 같이 좌표축에 평행하도록 케익 내부에 놓여 있다.</li>
</ol>

<p>주치의인 당신은 그가 <span style="color:#e67e22;">초</span><span style="color:#1abc9c;">콜</span><span style="color:#d35400;">릿</span>을 얼마나 먹게 될지 궁금해졌다. Mr.K가 케익을 잘랐을 때 먹을 수 있는 <span style="color:#1abc9c;">초</span><span style="color:#d35400;">콜</span><span style="color:#1abc9c;">릿</span> 면적 합의 최댓값을 구해보자!</p>

<p>주어진 그림에서 왼쪽과 같이 자를 경우 <span style="color:#1abc9c;">초</span><span style="color:#d35400;">콜</span><span style="color:#1abc9c;">릿</span> 면적 합은 $7$ 로 최대한 먹을 수 있고, 오른쪽의 경우는 $5$만큼 밖에 먹지 못한다.</p>

### 입력 

 <p>첫째 줄에 정수 $W$, $H$, $L$, $N$이 주어진다. </p>

<ul>
	<li>$5 \leq W, H \leq 100\ 000$</li>
	<li>$1<L<W+H$</li>
	<li>$1 \leq N \leq \min\left\{100\ 000, (W-2) \times (H-2)\right\}$</li>
</ul>

<p>둘째 줄부터 $N$개 줄에 정수 $x$, $y$, $w$, $h$가 주어진다. $\left(x, y\right)$는 초콜릿 조각의 왼쪽 아래 꼭짓점의 좌표, $\left(w, h\right)$는 초콜릿 조각의 가로와 세로 길이이다.</p>

### 출력 

 <p>Mr.K가 먹을 수 있는 초콜릿 넓이 합의 최댓값을 출력한다.</p>

