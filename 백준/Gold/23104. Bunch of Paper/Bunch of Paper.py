import sys
input = sys.stdin.readline

MOD = 10 ** 9 + 7

N, K = map(int, input().strip().split())

prev_values = list(map(int, input().strip().split()))
# dp[j]: 현재 종이에서 j번째 숫자를 골랐을 때 가능한 경우의 수
prev_dp = [1] * K

for _ in range(N - 1):
    curr_values = list(map(int, input().strip().split()))
    curr_dp = [0] * K
    
    p = 0
    current_sum = 0
    
    for j in range(K):
        while p < K and prev_values[p] <= curr_values[j]:
            current_sum = (current_sum + prev_dp[p]) % MOD
            p += 1
        
        curr_dp[j] = current_sum
    
    prev_values = curr_values
    prev_dp = curr_dp

print(sum(prev_dp) % MOD)