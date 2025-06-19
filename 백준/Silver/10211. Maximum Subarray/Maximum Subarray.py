import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    current = arr[0]
    max_sum = arr[0]

    for i in range(1, N):
        current = max(arr[i], current + arr[i])
        max_sum = max(max_sum, current)

    print(max_sum)