import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)
INF = float('inf')

N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

# 입력이 한 줄에 들어오므로 리스트로 변환하고 앞에 더미(0) 추가
notes = [0] + list(map(int, input().split()))
total_notes = sum(notes) # 우리가 찾아야 할 총 노트 개수

# 다익스트라: 1번 노드로부터의 최단 거리 계산
dist = [INF] * (N + 1)
dist[1] = 0
pq = [(0, 1)] # (거리, 노드)

while pq:
    d, curr = heapq.heappop(pq)

    if d > dist[curr]:
        continue

    for nxt, w in adj[curr]:
        if dist[curr] + w < dist[nxt]:
            dist[nxt] = dist[curr] + w
            heapq.heappush(pq, (dist[nxt], nxt))

# 만약 N번까지 갈 수 없다면 즉시 -1
if dist[N] == INF:
    print(-1)
    sys.exit(0)

# DP & 역추적 준비
# dp[i]: 1번에서 최단 경로로 i번에 도착했을 때 얻을 수 있는 최대 노트 수
# -1로 초기화 (방문 안 함)
dp = [-1] * (N + 1)

# 경로 복원을 위한 부모 노드 기록 (trace[curr] = prev)
trace = [0] * (N + 1)

# 재귀함수(DFS)를 이용한 DP
# node: 현재 위치 (N에서 시작해서 1로 내려감)
def get_max_notes(curr):
    # 기저 조건: 시작점에 도달
    if curr == 1:
        return notes[1]

    # 이미 계산한 적 있다면 그 값 반환 (메모이제이션)
    if dp[curr] != -1:
        return dp[curr]

    max_cnt = -INF

    # 현재 노드(curr)로 들어오는 '이전 노드(prev)'들을 찾음
    # 양방향 그래프이므로 adj[curr]에 있는 nxt가 사실은 prev 후보임
    for prev, w in adj[curr]:
        # 최단 경로 역추적 조건: dist[prev] + w == dist[curr]
        if dist[prev] + w == dist[curr]:
            res = get_max_notes(prev)

            # 노트 개수가 더 많은 경로를 선택
            if res > max_cnt:
                max_cnt = res
                trace[curr] = prev # 경로 기록 업데이트

    # 경로가 끊겨서 도달 불가능한 경우 처리
    if max_cnt == -INF:
        dp[curr] = -INF
    else:
        dp[curr] = max_cnt + notes[curr]

    return dp[curr]

# N번 노드에서 DP 시작
result = get_max_notes(N)

if result == total_notes:
    # 경로 복원
    path = []
    curr = N
    while curr != 0:
        path.append(curr)
        curr = trace[curr]

    print(len(path))
    print(*path[::-1]) # 역순으로 담겼으므로 뒤집어서 출력
else:
    print(-1)