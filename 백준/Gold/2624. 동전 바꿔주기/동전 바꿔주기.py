import sys
input = sys.stdin.readline

t = int(input())
k = int(input())
coins = [list(map(int, input().split())) for _ in range(k)]

dy = [0 for _ in range(t + 1)]
dy[0] = 1

for coin, cnt in coins:
    for money in range(t, 0, -1):
        for i in range(1, cnt + 1):
            if money - (coin * i) >= 0:
                dy[money] += dy[money - (coin * i)]

print(dy[t])