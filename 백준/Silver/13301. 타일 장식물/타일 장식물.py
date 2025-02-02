n = int(input())

dy = [0 for _ in range(81)]
dy[0], dy[1] = 4, 6

for i in range(2, n + 1):
    dy[i] = dy[i - 1] + dy[i - 2]

print(dy[n - 1])