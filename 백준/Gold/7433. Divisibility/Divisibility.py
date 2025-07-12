N, K = map(int, input().split())
nums = list(map(int, input().split()))

dp = [False] * K
dp[nums[0] % K] = True

for i in range(1, N):
    next_dp = [False] * K
    num = nums[i]
    for rem in range(K):
        if dp[rem]:
            next_dp[(rem + num) % K] = True
            next_dp[(rem - num) % K] = True
    dp = next_dp

print("Divisible" if dp[0] else "Not divisible")