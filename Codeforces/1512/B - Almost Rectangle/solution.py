import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    grid = [list(input().strip()) for _ in range(n)]
    
    stars = []
    for r in range(n):
        for c in range(n):
            if grid[r][c] == '*':
                stars.append((r, c))
                
    r1, c1 = stars[0]
    r2, c2 = stars[1]
    
    if r1 != r2 and c1 != c2:
        grid[r1][c2] = '*'
        grid[r2][c1] = '*'
        
    elif r1 == r2:
        new_r = r1 - 1 if r1 > 0 else r1 + 1
        grid[new_r][c1] = '*'
        grid[new_r][c2] = '*'
    else:
        new_c = c1 - 1 if c1 > 0 else c1 + 1
        grid[r1][new_c] = '*'
        grid[r2][new_c] = '*'
        
    for row in grid:
        print("".join(row))