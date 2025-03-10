n, l = map(int, input().split())
arr = list(map(int, input().split()))

now = 0
ans = 0

for i in range(n):
    now += arr[i]
    
    if i >= l:
        now -= arr[i - l]
    
    if 129 <= now <= 138:
        ans += 1

print(ans)