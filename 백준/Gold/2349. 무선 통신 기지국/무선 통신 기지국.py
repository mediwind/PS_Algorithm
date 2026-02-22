import sys
input = sys.stdin.readline


def dfs(idx, K):
    if idx == N:
        return True
    
    for c in range(1, K+1):
        ok = True
        for nxt in adj[idx]:
            if color[nxt] == c:
                ok = False
                break
        if not ok:
            continue
        
        color[idx] = c
        if dfs(idx+1, K):
            return True
        color[idx] = 0
    
    return False


N = int(input())
pos = [tuple(map(float, input().split())) for _ in range(N)]

adj = [[] for _ in range(N)]
for i in range(N):
    x1, y1 = pos[i]
    for j in range(i+1, N):
        x2, y2 = pos[j]
        dx = x1 - x2
        dy = y1 - y2
        if dx*dx + dy*dy <= 400 + 1e-9:
            adj[i].append(j)
            adj[j].append(i)

for K in range(1, N+1):
    color = [0]*N
    if dfs(0, K):
        print(K)
        break