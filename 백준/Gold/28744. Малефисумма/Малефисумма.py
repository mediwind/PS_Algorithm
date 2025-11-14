MOD = 10**9 + 7

n = int(input())
a = list(map(int, input().split()))

prefix_sum = 0
pair_sum = 0
result = 0

for x in a:
    result = (result + x * pair_sum) % MOD
    pair_sum = (pair_sum + x * prefix_sum) % MOD
    prefix_sum = (prefix_sum + x) % MOD

print(result)