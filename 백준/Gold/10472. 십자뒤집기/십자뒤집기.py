from collections import deque
import sys
input = sys.stdin.readline


def toggle(grid, x, y):
    grid2 = [list(row) for row in grid]
    for d in range(5):
        xx = x + dx[d]
        yy = y + dy[d]
        
        if xx < 0 or xx >= 3 or yy < 0 or yy >= 3:
            continue
        
        grid2[xx][yy] = '*' if grid[xx][yy] == '.' else '.'
    
    return tuple(''.join(row) for row in grid2)


dx = [-1, 0, 1, 0, 0]
dy = [0, 1, 0, -1, 0]

target = ('...', '...', '...')
T = int(input().rstrip())
for _ in range(T):
    start = tuple(input().rstrip() for _ in range(3))
    distance = {start: 0}
    Q = deque()
    Q.append(start)
    while Q:
        grid = Q.popleft()

        if grid == target:
            print(distance[grid])
            break

        now_dist = distance[grid]
        for i in range(3):
            for j in range(3):
                new_grid = toggle(grid, i, j)
                if new_grid not in distance:
                    distance[new_grid] = now_dist + 1
                    Q.append(new_grid)