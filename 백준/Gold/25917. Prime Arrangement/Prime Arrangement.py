MOD = 998244353

row_count, col_count = map(int, input().split())
primes = list(map(int, input().split()))
permutation = list(map(int, input().split()))

answer = 1
for i in range(row_count * col_count, row_count, -1):
    answer *= i % MOD
    answer %= MOD

print(answer)