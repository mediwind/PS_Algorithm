import sys
input = sys.stdin.readline

INF = 10**30

n = int(input().strip())
D = [0] * (n + 1)
C = [0] * (n + 1)
for i in range(1, n + 1):
    d, c = map(int, input().strip().split())
    D[i] = d
    C[i] = c

MULT = [0, 100, 50, 25, 25, 25, 25]

dp = [INF] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    sum_before_last = 0
    add_cost = 0

    for L in range(1, 7):
        j = i - L + 1
        if j < 1:
            break

        if L >= 2:
            sum_before_last += D[j]
            if sum_before_last >= 120:
                break

        seg = 0
        for p in range(1, L + 1):
            idx = j + p - 1
            seg += C[idx] * MULT[p]
        cand = dp[j - 1] + seg
        if cand < dp[i]:
            dp[i] = cand

ans = dp[n]
print(f"{ans // 100}.{ans % 100:02d}")