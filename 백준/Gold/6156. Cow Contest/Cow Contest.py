import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
win = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    win[i][i] = 1

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    win[a][b] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if win[i][k] and win[k][j]:
                win[i][j] = 1

ans = 0
for i in range(1, N + 1):
    good = True
    for j in range(1, N + 1):
        if not win[i][j] and not win[j][i]:
            good = False
            break
    
    if good:
        ans += 1

print(ans)