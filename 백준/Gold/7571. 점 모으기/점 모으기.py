import sys
input = sys.stdin.readline

N, M = map(int, input().split())
x = list()
y = list()
for _ in range(M):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x.sort()
y.sort()

x_mid = x[M // 2]
y_mid = y[M // 2]

ans = 0
for i in range(M):
    ans += abs(x[i] - x_mid)
    ans += abs(y[i] - y_mid)

print(ans)