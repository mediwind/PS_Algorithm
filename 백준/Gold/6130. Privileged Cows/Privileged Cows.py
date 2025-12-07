import sys
input = sys.stdin.readline

n = int(input().strip())
arr = [int(input().strip()) for _ in range(n)]
c1 = arr.count(1)
c2 = arr.count(2)
cnt = [[0]*4 for _ in range(4)]
for i, v in enumerate(arr):
    if i < c1:
        zone = 1
    elif i < c1 + c2:
        zone = 2
    else:
        zone = 3
    cnt[zone][v] += 1
swaps = 0
for i in range(1, 4):
    for j in range(i+1, 4):
        t = min(cnt[i][j], cnt[j][i])
        swaps += t
        cnt[i][j] -= t
        cnt[j][i] -= t
rem = 0
for i in range(1, 4):
    for j in range(1, 4):
        if i != j:
            rem += cnt[i][j]
swaps += 2 * (rem // 3)
print(swaps)