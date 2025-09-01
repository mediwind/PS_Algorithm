import heapq
import sys
input = sys.stdin.readline

INF = 10**18

M, N = map(int, input().rstrip().split())
grid = [list(map(int, input().rstrip().split())) for _ in range(M)]
if M == 1 and N == 1:
    print(0)
    sys.exit(0)

dist = [[INF]*N for _ in range(M)]
dist[0][0] = 0
pq = [(0, 0, 0)]  # (current_required_ladder, r, c)
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while pq:
    cost, r, c = heapq.heappop(pq)
    if cost != dist[r][c]:
        continue
        
    if r == M - 1 and c == N - 1:
        print(cost)
        sys.exit(0)
        
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < M and 0 <= nc < N:
            climb = max(0, grid[nr][nc] - grid[r][c])
            new_cost = max(cost, climb)
            if new_cost < dist[nr][nc]:
                dist[nr][nc] = new_cost
                heapq.heappush(pq, (new_cost, nr, nc))

# 안전 장치: 도달 못하면 (문제 조건상 불가능)
print(dist[M-1][N-1])