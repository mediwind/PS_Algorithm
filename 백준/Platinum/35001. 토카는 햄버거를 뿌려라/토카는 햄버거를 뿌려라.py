import sys
input = sys.stdin.readline
MOD = 1_000_000_007


def modinv(x):
    return pow(x, MOD - 2, MOD)


N, M = map(int, input().split())
A = list(map(int, input().split()))

weights = [a * a for a in A]
w0 = weights[0]

others = weights[1:]
n = len(others)

total_weight = sum(weights)

sum_w = [0] * (1 << n)
for mask in range(1, 1 << n):
    lsb = mask & -mask
    i = (lsb.bit_length() - 1)
    sum_w[mask] = sum_w[mask ^ lsb] + others[i]

dp = [0] * (1 << n)
dp[0] = 1

for mask in range(1 << n):
    picked = mask.bit_count()
    if picked >= M:
        continue

    cur_prob = dp[mask]
    if cur_prob == 0:
        continue

    remain = total_weight - sum_w[mask]
    inv_remain = modinv(remain % MOD)

    for i in range(n):
        if mask & (1 << i):
            continue
        w = others[i] % MOD
        new_mask = mask | (1 << i)
        dp[new_mask] = (dp[new_mask] + cur_prob * w % MOD * inv_remain) % MOD

prob_not = 0
for mask in range(1 << n):
    if mask.bit_count() == M:
        prob_not = (prob_not + dp[mask]) % MOD

answer = (1 - prob_not) % MOD
print(answer)