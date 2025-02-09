n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans = sum(arr[:m])
tmp = ans

for i in range(m, n):
    tmp -= arr[i - m]
    tmp += arr[i]
    
    ans = max(ans, tmp)

print(ans)