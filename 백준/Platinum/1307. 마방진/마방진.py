import sys
input = sys.stdin.readline

n = int(input().strip())
grid = [[0] * n for _ in range(n)]

if n % 2 != 0:
    r, c = 0, n // 2
    for i in range(1, n * n + 1):
        grid[r][c] = i
        
        nr, nc = (r - 1) % n, (c + 1) % n
        
        if grid[nr][nc] != 0:
            nr, nc = (r + 1) % n, c
            
        r, c = nr, nc

elif n % 4 == 0:
    for r in range(n):
        for c in range(n):
            val = r * n + c + 1
            
            if (r % 4 == c % 4) or (r % 4 + c % 4 == 3):
                grid[r][c] = (n * n + 1) - val
            else:
                grid[r][c] = val

else:
    half = n // 2
    
    sub_grid = [[0] * half for _ in range(half)]
    r, c = 0, half // 2
    for i in range(1, half * half + 1):
        sub_grid[r][c] = i
        nr, nc = (r - 1) % half, (c + 1) % half
        if sub_grid[nr][nc] != 0:
            nr, nc = (r + 1) % half, c
        r, c = nr, nc
        
    q_size = half * half
    
    for r in range(half):
        for c in range(half):
            grid[r][c] = sub_grid[r][c]
            grid[r + half][c + half] = sub_grid[r][c] + q_size
            grid[r][c + half] = sub_grid[r][c] + 2 * q_size
            grid[r + half][c] = sub_grid[r][c] + 3 * q_size
            
    k = n // 4
    
    for r in range(half):
        for c in range(k):
            if r == half // 2:
                grid[r][c + 1], grid[r + half][c + 1] = grid[r + half][c + 1], grid[r][c + 1]
            else:
                grid[r][c], grid[r + half][c] = grid[r + half][c], grid[r][c]
                
    for r in range(half):
        for c in range(n - k + 1, n):
            grid[r][c], grid[r + half][c] = grid[r + half][c], grid[r][c]

for row in grid:
    print(*(row))