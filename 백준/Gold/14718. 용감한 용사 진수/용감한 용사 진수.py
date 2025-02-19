import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
enemies = [list(map(int, input().strip().split())) for _ in range(n)]

enemies.sort(key = lambda x: x[2])

ans = float("inf")
for a in enemies:
    for b in enemies:
        x, y = a[0], b[1]
        
        z = 0
        cnt = 0
        for c in enemies:
            if x >= c[0] and y >= c[1]:
                z = max(z, c[2])
                cnt += 1
            
            if cnt == k:
                break
        
        if cnt == k:
            ans = min(ans, x + y + z)

print(ans)