import sys
input = sys.stdin.readline

N = int(input())
butters = []

for _ in range(N):
    x, h = map(int, input().split())
    R = (h - 1) // 2
    butters.append((x, R))

butters.sort()

INF = 10**30
min_time = INF

for i in range(N - 1):
    x1, R1 = butters[i]
    x2, R2 = butters[i + 1]

    d = x2 - x1

    if R1 + R2 < d:
        continue

    R_min = min(R1, R2)
    
    if 2 * R_min >= d:
        t = (d - 1) // 2
    else:
        t = d - 1 - R_min

    min_time = min(min_time, t)

if min_time == INF:
    print("forever")
else:
    print(min_time)