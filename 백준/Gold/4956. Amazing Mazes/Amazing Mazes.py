from collections import deque
import sys
input = sys.stdin.readline

while True:
    w, h = map(int, input().rstrip().split())
    if w == 0 and h == 0:
        break

    lines = []
    for _ in range(2 * h - 1):
        parts = list(map(int, input().rstrip().split()))
        lines.append(parts)

    hor = [[0] * (w - 1) for _ in range(h)]
    ver = [[0] * w for _ in range(h - 1)]

    for i in range(h):
        row_h = lines[2 * i]
        for j in range(w - 1):
            hor[i][j] = row_h[j]
        if i < h - 1:
            row_v = lines[2 * i + 1]
            for j in range(w):
                ver[i][j] = row_v[j]

    dist = [[0] * w for _ in range(h)]
    q = deque()
    dist[0][0] = 1
    q.append((0, 0))

    while q:
        x, y = q.popleft()
        d = dist[x][y]
        if x == h - 1 and y == w - 1:
            break

        # 오른쪽으로
        if y < w - 1 and hor[x][y] == 0 and dist[x][y + 1] == 0:
            dist[x][y + 1] = d + 1
            q.append((x, y + 1))
        # 왼쪽으로
        if y > 0 and hor[x][y - 1] == 0 and dist[x][y - 1] == 0:
            dist[x][y - 1] = d + 1
            q.append((x, y - 1))
        # 아래로
        if x < h - 1 and ver[x][y] == 0 and dist[x + 1][y] == 0:
            dist[x + 1][y] = d + 1
            q.append((x + 1, y))
        # 위로
        if x > 0 and ver[x - 1][y] == 0 and dist[x - 1][y] == 0:
            dist[x - 1][y] = d + 1
            q.append((x - 1, y))

    print(dist[h - 1][w - 1])