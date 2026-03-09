import sys
import heapq
input = sys.stdin.readline

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

max_k = H * W
INF = float('inf')

dist = [[[INF] * max_k for _ in range(W)] for _ in range(H)]
dist[0][0][0] = 0

pq = [(0, 0, 0, 0)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ans = -1

while pq:
    cost, k, r, c = heapq.heappop(pq)
    
    if r == H - 1 and c == W - 1:
        ans = cost
        break
        
    if cost > dist[r][c][k]:
        continue
        
    nk = k + 1
    if nk >= max_k:
        continue
        
    multiplier = 2 * nk - 1
    
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        
        if 0 <= nr < H and 0 <= nc < W:
            nxt_cost = cost + A[nr][nc] * multiplier
            
            if nxt_cost < dist[nr][nc][nk]:
                dist[nr][nc][nk] = nxt_cost
                heapq.heappush(pq, (nxt_cost, nk, nr, nc))

print(ans)