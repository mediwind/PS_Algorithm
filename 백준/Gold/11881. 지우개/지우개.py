MOD = 1000000007

n = int(input())
arr = list(map(int, input().split()))

frequency = [0] * 100100
prefix = [0] * 100100
two = [0] * 100100
prefix_sum = [0] * 100100

for value in arr:
    frequency[value] += 1

count = 1
for i in range(1, 100001):
    if frequency[i]:
        prefix[count] = i
        prefix_sum[count] = (prefix_sum[count - 1] + (i * frequency[i]) % MOD) % MOD
        count += 1

result = 0
for i in range(1, count):
    two[i] = (two[i - 1] + (prefix_sum[i - 1] * ((prefix[i] * frequency[prefix[i]]) % MOD)) % MOD) % MOD
    result = (result + (two[i - 1] * ((prefix[i] * frequency[prefix[i]]) % MOD)) % MOD) % MOD

print(result)