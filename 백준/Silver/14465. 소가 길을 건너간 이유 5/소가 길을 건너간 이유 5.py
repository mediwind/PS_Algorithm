n, k, b = map(int, input().split())
arr = [0 for _ in range(n + 1)]
prefix_sum = [0 for _ in range(n + 1)]

for _ in range(b):
    idx = int(input())
    arr[idx] = 1

for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]

answer = float('inf')
for i in range(k, n + 1):
    answer = min(answer, prefix_sum[i] - prefix_sum[i - k])

print(answer)