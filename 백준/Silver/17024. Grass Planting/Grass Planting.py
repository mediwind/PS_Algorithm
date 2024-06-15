N = int(input())
degree = [0 for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    degree[a] += 1
    degree[b] += 1

print(max(degree) + 1)