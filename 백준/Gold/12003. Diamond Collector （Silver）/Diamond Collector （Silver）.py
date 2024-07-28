import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

maximum = [0 for _ in range(n)] # Right[i] : case에 arr[i]가 가장 작은 다이아로 들어간다 가정했을 때
j = 0
for i in range(n):
    while j < n and arr[j] - arr[i] <= k:
        j += 1
    maximum[i] = j - i

right_side_maximum = [0 for _ in range(n + 1)] # i 이상 중 가장 큰 maximum[i]의 값
for i in range(n - 1, -1, -1):
    right_side_maximum[i] = max(right_side_maximum[i + 1], maximum[i])

ans = 0
for i in range(n):
    ans = max(ans, maximum[i] + right_side_maximum[i + maximum[i]])
print(ans)