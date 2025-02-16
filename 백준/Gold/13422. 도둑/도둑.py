import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n, m, k = map(int, input().strip().split())
        
    houses = list(map(int, input().strip().split()))
    
    if n == m:
        if sum(houses) < k:
            print(1)
        else:
            print(0)
        continue
    
    houses += houses[:m - 1]

    now = sum(houses[:m])
    ans = now < k
    for lt in range(1, n):
        rt = lt + m - 1
        now = now - houses[lt - 1] + houses[rt]
        ans += (now < k)

    print(ans)