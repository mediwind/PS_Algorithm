import sys

MOD = 1000000007
n = int(input())

if n == 0:
    print(0)
    sys.exit(0)

arr = [0 for _ in range(n + 1)]
arr[1] = 1

for i in range(2, n + 1):
    arr[i] = (arr[i - 2] + arr[i - 1]) % MOD

print(arr[n])