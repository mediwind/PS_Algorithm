from collections import defaultdict

import sys
input = sys.stdin.readline


def count_pairs(arr, k):
    arr.sort()
    count = 0
    i, j = 0, 0
    while j < len(arr):
        while arr[j] - arr[i] > k:
            i += 1
        count += j - i
        j += 1
    return count


n, k = map(int, input().split())
names = defaultdict(list)
for i in range(n):
    name = input()
    names[len(name)].append(i + 1)

answer = 0
for val in names.values():
    arr = val
    answer += count_pairs(arr, k)

print(answer)