n = int(input())
dy = [i for i in range(n + 1)]

for i in range(6, n + 1):
    dy[i] = max(dy[i - 3] * 2,
                dy[i - 4] * 3,
                dy[i - 5] * 4)

print(dy[-1])