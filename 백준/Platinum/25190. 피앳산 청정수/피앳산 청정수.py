import sys
input = sys.stdin.readline

N = int(input().strip())

people = []
for _ in range(N):
    p, c = map(int, input().strip().split())
    people.append((p, c))

people.sort(key=lambda x: x[0] + x[1])

INF = float('inf')
dp = [INF] * (N + 1)
dp[0] = 0

for p, c in people:
    for i in range(N - 1, -1, -1):
        if dp[i] != INF:
            if dp[i] < c:
                dp[i+1] = min(dp[i+1], dp[i] + p)

for i in range(N, -1, -1):
    if dp[i] != INF:
        print(f"{i} {dp[i]}")
        break