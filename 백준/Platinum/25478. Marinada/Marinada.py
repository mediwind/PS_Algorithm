import sys
from collections import deque
input = sys.stdin.readline

INF = float('inf')

N, M, K = map(int, input().split())
grid = [input().strip() for _ in range(N)]

n_nodes = []
S = None
E = None

# Step 1-1: 핵심 거점(시작점, 도착점, 재료)의 좌표를 모두 찾습니다.
for r in range(N):
    for c in range(M):
        if grid[r][c] == 'N':
            n_nodes.append((r, c))
        elif grid[r][c] == 'U':
            S = (r, c)
        elif grid[r][c] == 'I':
            E = (r, c)

# 거점 인덱싱: 0 ~ K-1은 재료(N), K는 시작점(U), K+1은 도착점(I)
key_points = n_nodes + [S, E]
num_keys = K + 2
pos_to_idx = {pt: i for i, pt in enumerate(key_points)}

# 거점 간의 최단 거리를 저장할 인접 행렬 초기화
adj = [[INF] * num_keys for _ in range(num_keys)]
for i in range(num_keys):
    adj[i][i] = 0

# Step 1-2: 시작점과 K개의 재료 위치에서 BFS를 수행하여 거점 간 거리를 구합니다.
# (도착점 K+1에서는 굳이 BFS를 돌리지 않아도 무방합니다)
for i in range(K + 1):
    sr, sc = key_points[i]
    q = deque([(sr, sc)])
    dist = [[-1] * M for _ in range(N)]
    dist[sr][sc] = 0
    found = 1
    
    # 맵 전체를 도는 대신, 다른 거점들을 모두 찾으면 조기 종료합니다 (속도 최적화)
    while q and found < num_keys:
        cr, cc = q.popleft()
        curr_dist = dist[cr][cc]
        
        # 튜플 언패킹을 활용한 4방향 탐색 (Python에서 가장 빠른 방식)
        for nr, nc in ((cr-1, cc), (cr+1, cc), (cr, cc-1), (cr, cc+1)):
            if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] != '#' and dist[nr][nc] == -1:
                dist[nr][nc] = curr_dist + 1
                q.append((nr, nc))
                
                # 방문한 곳이 핵심 거점 중 하나라면 거리를 기록합니다.
                if (nr, nc) in pos_to_idx:
                    found += 1
                    idx = pos_to_idx[(nr, nc)]
                    adj[i][idx] = curr_dist + 1
                    adj[idx][i] = curr_dist + 1

# Step 2: 비트마스킹 DP
# dp[mask][u]: 방문한 재료 집합이 mask이고, 마지막 위치가 u일 때의 최소 이동 횟수
dp = [[INF] * K for _ in range(1 << K)]

# 기저 조건: 시작점(K)에서 각각의 단일 재료(0 ~ K-1)로 처음 이동하는 경우
for i in range(K):
    dp[1 << i][i] = adj[K][i]

for mask in range(1, 1 << K):
    for u in range(K):
        # 도달할 수 없는 상태라면 건너뜁니다.
        if dp[mask][u] == INF:
            continue
        
        for v in range(K):
            # 아직 방문하지 않은 재료 v를 확인
            if not (mask & (1 << v)):
                nxt_mask = mask | (1 << v)
                nxt_dist = dp[mask][u] + adj[u][v]
                
                # 최소 거리 갱신
                if nxt_dist < dp[nxt_mask][v]:
                    dp[nxt_mask][v] = nxt_dist

# Step 3: 모든 재료를 수집한 후 도착점(K+1)으로 이동하는 최소 비용 계산
ans = INF
full_mask = (1 << K) - 1
for i in range(K):
    ans = min(ans, dp[full_mask][i] + adj[i][K + 1])

print(ans)