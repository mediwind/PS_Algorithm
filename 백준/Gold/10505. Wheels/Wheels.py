from math import gcd
from collections import deque
import sys
input = sys.stdin.readline


def are_touching(wheel1, wheel2):
    x1, y1, r1 = wheel1
    x2, y2, r2 = wheel2
    # 두 원의 중심 사이 거리의 제곱
    dist_squared = (x1 - x2) ** 2 + (y1 - y2) ** 2
    # 두 원이 맞닿으면 중심 사이 거리 = 반지름의 합
    return dist_squared == (r1 + r2) ** 2


def format_fraction(p, q):
    if p == 0:
        return "not moving"
    
    # 기약분수로 만들기
    g = gcd(abs(p), abs(q))
    p //= g
    q //= g
    
    direction = "clockwise" if p > 0 else "counterclockwise"
    p = abs(p)
    
    # 분모가 1인 경우 정수로 출력
    if q == 1:
        return f"{p} {direction}"
    else:
        return f"{p}/{q} {direction}"


t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    wheels = list()

    for i in range(n):
        x, y, r = map(int, input().split())
        wheels.append((x, y, r))

    # 그래프 구성: 맞닿은 바퀴들 사이에 간선 생성
    graph = [list() for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if are_touching(wheels[i], wheels[j]):
                graph[i].append(j)
                graph[j].append(i)

    # BFS로 각 바퀴의 회전 방향과 속도 계산
    visited = [-1 for _ in range(n)]  # -1: 미방문, 0: 시계방향, 1: 반시계방향
    queue = deque([(0, 0)])  # (바퀴 번호, 방향)
    visited[0] = 0  # 첫 번째 바퀴는 시계 방향(clockwise)

    while queue:
        wheel, direction = queue.popleft()

        for next_wheel in graph[wheel]:
            if visited[next_wheel] == -1:
                visited[next_wheel] = 1 - direction  # 방향 반전
                queue.append((next_wheel, 1 - direction))

    # 결과 출력
    for i in range(n):
        if visited[i] == -1:
            print("not moving")
        else:
            r1 = wheels[0][2]  # 첫 번째 바퀴의 반지름
            ri = wheels[i][2]  # i번째 바퀴의 반지름

            # 회전 속도는 반지름에 반비례
            p, q = r1, ri

            # 방향 설정
            if visited[i] == 1:  # 반시계 방향
                p = -p

            print(format_fraction(p, q))