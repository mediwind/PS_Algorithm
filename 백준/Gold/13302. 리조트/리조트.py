n, k = map(int, input().split())

if not k:
    not_go = set()
else:
    not_go = set(map(int, input().split()))

coupon = 0
dy = [[float('inf') for _ in range(106)] for _ in range(106)]
dy[0][0] = 0

for i in range(n + 1):
    for j in range(40):
        if dy[i][j] == float('inf'):
            continue
            
        res = dy[i][j]
        
        if i + 1 in not_go:
            dy[i + 1][j] = min(res, dy[i + 1][j])
        if j >= 3:
            dy[i + 1][j - 3] = min(dy[i + 1][j - 3], res)
        
        dy[i + 1][j] = min(res + 10000, dy[i + 1][j])
        
        for k in range(1, 4):
            dy[i + k][j + 1] = min(res + 25000, dy[i + k][j + 1])
        
        for k in range(1, 6):
            dy[i + k][j + 2] = min(res + 37000, dy[i + k][j + 2])

print(min(dy[n]))