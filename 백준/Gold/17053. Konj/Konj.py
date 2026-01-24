import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

segments = []
endpoint_map = {}

for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    segments.append((x1, y1, x2, y2))

    for p in [(x1, y1), (x2, y2)]:
        if p not in endpoint_map:
            endpoint_map[p] = []
        endpoint_map[p].append(i)

TX, TY = map(int, input().split())

visited_seg = [False] * N
stack = []

for i in range(N):
    x1, y1, x2, y2 = segments[i]
    is_on_segment = False

    if x1 == x2 == TX:
        if min(y1, y2) <= TY <= max(y1, y2):
            is_on_segment = True
    elif y1 == y2 == TY:
        if min(x1, x2) <= TX <= max(x1, x2):
            is_on_segment = True

    if is_on_segment:
        visited_seg[i] = True
        stack.append(i)

while stack:
    curr_idx = stack.pop()
    x1, y1, x2, y2 = segments[curr_idx]

    for p in [(x1, y1), (x2, y2)]:
        if p in endpoint_map:
            for neighbor_idx in endpoint_map[p]:
                if not visited_seg[neighbor_idx]:
                    visited_seg[neighbor_idx] = True
                    stack.append(neighbor_idx)

drawn_points = set()

for i in range(N):
    if visited_seg[i]:
        x1, y1, x2, y2 = segments[i]

        if x1 == x2: # 수직선 그리기
            for y in range(min(y1, y2), max(y1, y2) + 1):
                drawn_points.add((x1, y))
        else: # 수평선 그리기
            for x in range(min(x1, x2), max(x1, x2) + 1):
                drawn_points.add((x, y1))

if not drawn_points:
    sys.exit(0)

xs = [p[0] for p in drawn_points]
ys = [p[1] for p in drawn_points]

min_x, max_x = min(xs), max(xs)
min_y, max_y = min(ys), max(ys)

for y in range(max_y, min_y - 1, -1):
    row_str = []
    for x in range(min_x, max_x + 1):
        if (x, y) in drawn_points:
            row_str.append('#')
        else:
            row_str.append('.')
    print("".join(row_str))