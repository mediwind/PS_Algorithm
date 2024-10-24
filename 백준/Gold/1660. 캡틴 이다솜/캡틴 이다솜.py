n = int(input())
v = list()
num = 0
i = 1

while num <= n:
    num = i * (i + 1) * (i + 2) // 6
    if num > n:
        break
    v.append(num)
    i += 1

dp = [float('inf') for _ in range(n + 1)]
dp[0] = 0

for num in v:
    for j in range(num, n + 1):
        dp[j] = min(dp[j], dp[j - num] + 1)

print(dp[n])