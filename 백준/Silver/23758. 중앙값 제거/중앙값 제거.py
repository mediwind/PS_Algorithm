import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

if n % 2:
    n = n // 2 + 1
else:
    n = n // 2

ans = 0
for i in range(n):
    num = arr[i]
    
    while num > 1:
        num //= 2
        ans += 1

print(ans + 1)