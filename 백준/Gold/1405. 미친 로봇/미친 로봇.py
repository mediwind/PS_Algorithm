def DFS(x, y, depth, p):
    global ans
    
    if depth == N:
        ans += p
        return
    
    for d in range(4):
        xx = x + dx[d]
        yy = y + dy[d]
        
        if not ch[xx][yy] and prob[d] > 0:
            ch[xx][yy] = 1
            DFS(xx, yy, depth + 1, p * prob[d])
            ch[xx][yy] = 0


N, E, W, S, N_ = map(int, input().split())
prob = [N_/100, E/100, S/100, W/100]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ch = [[0 for _ in range(14 * 2 + 1)] for _ in range(14 * 2 + 1)]
ch[14][14] = 1

ans = 0.0
DFS(14, 14, 0, 1.0)
print(f"{ans:.10f}")