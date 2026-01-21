import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    points = []
    point_set = set()

    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
        point_set.add((x, y))

    max_area = 0

    for i in range(N):
        for j in range(i + 1, N):
            x1, y1 = points[i]
            x2, y2 = points[j]

            area = (x2 - x1)**2 + (y2 - y1)**2

            if area <= max_area:
                continue

            dx = x2 - x1
            dy = y2 - y1

            nx1, ny1 = x2 - dy, y2 + dx
            nx2, ny2 = x1 - dy, y1 + dx

            if (nx1, ny1) in point_set and (nx2, ny2) in point_set:
                max_area = area

            nx3, ny3 = x2 + dy, y2 - dx
            nx4, ny4 = x1 + dy, y1 - dx

            if (nx3, ny3) in point_set and (nx4, ny4) in point_set:
                max_area = area

    print(max_area)