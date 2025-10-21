from collections import deque
import sys
input = sys.stdin.readline

board = [list(map(int, input().rstrip().split())) for _ in range(5)]
sr, sc = map(int, input().rstrip().split())

targets = [(sr, sc)] + [None] * 6
for r in range(5):
    for c in range(5):
        v = board[r][c]
        if 1 <= v <= 6:
            targets[v] = (r, c)

def bfs(start):
    dist = [[-1]*5 for _ in range(5)]
    q = deque([start])
    dist[start[0]][start[1]] = 0
    while q:
        r, c = q.popleft()
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r+dr, c+dc
            if 0 <= nr < 5 and 0 <= nc < 5 and board[nr][nc] != -1 and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    return dist

dists = [None]*7
for i in range(7):
    dists[i] = bfs(targets[i])

ans = 0
for i in range(6):
    r, c = targets[i+1]
    step = dists[i][r][c]
    if step == -1:
        print(-1)
        break
    ans += step
else:
    print(ans)