import sys
input = sys.stdin.readline

L, N, Rf, Rb = map(int, input().split())
spots = [list(map(int, input().split())) for _ in range(N)]

maxi = spots[-1][1]
for i in range(N - 2, -1, -1):
    if spots[i][1] < maxi:
        spots[i][1] = 0
    else:
        maxi = spots[i][1]

answer = 0
f_seconds = 0
b_seconds = 0
last_spot = 0
for x, c in spots:
    if c == 0:
        continue
    f_seconds = Rf * x
    b_seconds += (x - last_spot) * Rb
    diff = f_seconds - b_seconds
    answer += diff * c
    b_seconds += diff
    last_spot = x

print(answer)