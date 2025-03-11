MOD = 10 ** 6

n = int(input())

ans = 0
for x in range(n + 1):
    if 3 * x > n:
        break
    ans += (n - 3 * x) // 2 + 1

print(ans % MOD)