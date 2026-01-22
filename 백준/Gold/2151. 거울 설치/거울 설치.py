import heapq
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
grid = [list(input().strip()) for _ in range(N)]

doors = []
for r in range(N):
    for c in range(N):
        if grid[r][c] == '#':
            doors.append((r, c))

start_x, start_y = doors[0]
end_x, end_y = doors[1]

pq = []

dist = [[[float('inf')] * 4 for _ in range(N)] for _ in range(N)]

for d in range(4):
    pq.append((0, start_x, start_y, d))
    dist[start_x][start_y][d] = 0

while pq:
    cost, x, y, direction = heapq.heappop(pq)

    if dist[x][y][direction] < cost:
        continue

    nx, ny = x + dx[direction], y + dy[direction]

    while 0 <= nx < N and 0 <= ny < N and grid[nx][ny] != '*':
        if nx == end_x and ny == end_y:
            print(cost)
            sys.exit(0)

        if grid[nx][ny] == '!':
            next_cost = cost + 1

            for turn in [1, 3]:
                next_dir = (direction + turn) % 4

                if dist[nx][ny][next_dir] > next_cost:
                    dist[nx][ny][next_dir] = next_cost
                    heapq.heappush(pq, (next_cost, nx, ny, next_dir))

        nx += dx[direction]
        ny += dy[direction]