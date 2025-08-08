from collections import deque
import sys
# input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

K = int(input().rstrip())
for tc in range(1, K+1):
    x, y = map(int, input().rstrip().split())
    grid = [list(input().rstrip()) for _ in range(y)]
    
    # 시작 위치 찾기
    for i in range(y):
        for j in range(x):
            if grid[i][j] == 'S':
                sr, sc = i, j
                break
    
    # visited[r][c][g] = 이 상태(칸(r,c), goop_count=g)로 방문했는지
    visited = [[[False]*4 for _ in range(x)] for __ in range(y)]
    q = deque()
    # 시작: goop 누적 0
    q.append((sr, sc, 0))
    visited[sr][sc][0] = True
    
    reached_h = set()  # 도달한 H 위치를 저장
    while q:
        r, c, g = q.popleft()
        if grid[r][c] == 'H':
            reached_h.add((r, c))
        for d in range(4):
            nr, nc = r + dy[d], c + dx[d]
            if not (0 <= nr < y and 0 <= nc < x):
                continue
            cell = grid[nr][nc]
            ng = g
            # goop 칸: 누적+1
            if cell == 'G':
                ng += 1
                if ng > 3:
                    continue
            # cleaner 칸: 리셋
            elif cell == 'P':
                ng = 0
            # . , H, S 칸: ng 그대로
            
            if not visited[nr][nc][ng]:
                visited[nr][nc][ng] = True
                q.append((nr, nc, ng))
    
    # 출력
    print(f"Data Set {tc}:")
    print(len(reached_h))
    print()