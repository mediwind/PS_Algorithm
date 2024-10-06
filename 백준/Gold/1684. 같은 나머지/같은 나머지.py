import math


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


N = int(input())
nums = list(map(int, input().split()))

nums.sort()

diffs = [nums[i] - nums[i - 1] for i in range(1, N)]

result = diffs[0]
for diff in diffs[1:]:
    result = gcd(result, diff)

print(result)