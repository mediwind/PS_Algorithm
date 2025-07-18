import bisect
import sys
input = sys.stdin.readline

N = int(input())
x_mins, x_maxs, y_mins, y_maxs = [], [], [], []

for _ in range(N):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    xs = [x1, x2, x3]
    ys = [y1, y2, y3]
    x_mins.append(min(xs))
    x_maxs.append(max(xs))
    y_mins.append(min(ys))
    y_maxs.append(max(ys))

# 정렬 (이분 탐색용)
x_mins_sorted = sorted(x_mins)
x_maxs_sorted = sorted(x_maxs)
y_mins_sorted = sorted(y_mins)
y_maxs_sorted = sorted(y_maxs)

M = int(input())
for _ in range(M):
    q = input().strip()
    if q[0] == ('x'):
        c = int(q.split('=')[1].strip())
        # 조건: x_min < c < x_max
        A = bisect.bisect_left(x_mins_sorted, c)  # x_min이 c 미만인 삼각형 수
        B = N - bisect.bisect_right(x_maxs_sorted, c)  # x_max가 c 초과인 삼각형 수
        print(A + B - N)
    else:
        c = int(q.split('=')[1].strip())
        # 조건: y_min < c < y_max
        A = bisect.bisect_left(y_mins_sorted, c)
        B = N - bisect.bisect_right(y_maxs_sorted, c)
        print(A + B - N)