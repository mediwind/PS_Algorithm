from collections import deque
import sys
input = sys.stdin.readline

INF = float('inf')

N, M, Q = map(int, input().split())

# 인접 리스트 생성
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)

# dist[i][j] : i에서 j로 가는 최단 거리
dist = [[INF] * (N + 1) for _ in range(N + 1)]

# 1. 모든 정점에서 BFS를 돌려 모든 쌍의 최단 거리 계산
# N이 2000이므로 2000번의 BFS는 시간 내에 충분함 (O(N(N+M)))
for i in range(1, N + 1):
    dist[i][i] = 0
    queue = deque([i])

    while queue:
        curr = queue.popleft()

        for nxt in adj[curr]:
            # 아직 방문하지 않은 곳이라면 거리 갱신
            if dist[i][nxt] == INF:
                dist[i][nxt] = dist[i][curr] + 1
                queue.append(nxt)

# 2. 쿼리 처리
for _ in range(Q):
    u, v = map(int, input().split())
    ans = INF

    # 모든 정점 k를 후보 조상으로 확인 (O(N))
    for k in range(1, N + 1):
        # k에서 u와 v 둘 다 갈 수 있는 경우만 체크
        if dist[k][u] != INF and dist[k][v] != INF:
            # 둘 중 더 오래 걸리는 시간(작지 않은 값)
            current_val = max(dist[k][u], dist[k][v])

            # 그 중 최솟값 갱신
            if current_val < ans:
                ans = current_val

    # 만약 가능한 조상이 없다면 -1, 있다면 최솟값 출력
    if ans == INF:
        print(-1)
    else:
        print(ans)