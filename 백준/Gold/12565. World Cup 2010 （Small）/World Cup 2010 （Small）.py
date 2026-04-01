import sys
input = sys.stdin.readline
INF = 10**18

T = int(input().strip())

for tc in range(1, T + 1):
    P = int(input().strip())
    M = list(map(int, input().split()))

    price = []
    for _ in range(P):
        price.append(list(map(int, input().split())))

    N = 1 << P

    dp = []
    for i in range(N):
        arr = [0] * (P + 1)
        for k in range(P + 1):
            if k > M[i]:
                arr[k] = INF
        dp.append(arr)

    for round in range(P):
        new_dp = []
        matches = len(dp) // 2

        for i in range(matches):
            left = dp[2 * i]
            right = dp[2 * i + 1]

            cur = [INF] * (P + 1)

            for k in range(P + 1):
                cost_watch = price[round][i] + left[k] + right[k]
                cur[k] = min(cur[k], cost_watch)

                if k + 1 <= P:
                    cost_miss = left[k + 1] + right[k + 1]
                    cur[k] = min(cur[k], cost_miss)

            new_dp.append(cur)

        dp = new_dp

    ans = dp[0][0]

    print(f"Case #{tc}: {ans}")