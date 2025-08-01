from collections import deque
import sys
input = sys.stdin.readline


def sq(x):
    return x * x


N, M = map(int, input().rstrip().split())
pts = [tuple(map(int, input().rstrip().split())) for _ in range(N)]
P = list(map(int, input().rstrip().split()))
R = list(map(int, input().rstrip().split()))
R0 = R[0]
other_R = R[1:]

# 1) 다른 강아지들로 이미 냄새 나는 기둥들 표시
contaminated = [0 for _ in range(N)]
for pi, ri in zip(P, other_R):
    cx, cy = pts[pi - 1]
    rr = ri * ri
    for j in range(N):
        if not contaminated[j]:
            xj, yj = pts[j]
            if sq(cx - xj) + sq(cy - yj) <= rr:
                contaminated[j] = 1

# 2) 시루 냄새 반경 R0 기준으로 인접 리스트 한 번만 계산
# 간선이 직접 input되지 않아도 그래프를 사용할 수 있도록 하는 유용한 테크닉
R0_sq = R0 * R0
adj = [list() for _ in range(N)]
for i in range(N):
    xi, yi = pts[i]
    for j in range(i + 1, N):
        xj, yj = pts[j]
        if sq(xi - xj) + sq(yi - yj) <= R0_sq:
            adj[i].append(j)
            adj[j].append(i)

# 3) BFS: 즉시 마킹 가능한 기둥을 큐에 넣고 방문
visited = [0 for _ in range(N)]
Q = deque()
cnt = 0
for i in range(N):
    if not contaminated[i]:
        visited[i] = 1
        Q.append(i)
        cnt += 1

# 4) BFS 확장: 인접 리스트 이용
while Q:
    u = Q.popleft()
    for v in adj[u]:
        if not visited[v]:
            visited[v] = 1
            cnt += 1
            Q.append(v)

print(cnt)