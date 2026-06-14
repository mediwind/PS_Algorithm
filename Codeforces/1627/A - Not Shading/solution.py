import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n, m, r, c = map(int, input().split())
    
    r -= 1
    c -= 1
    
    grid = [input().rstrip() for _ in range(n)]
    
    has_black = False
    for i in range(n):
        if 'B' in grid[i]:
            has_black = True
            break
            
    if not has_black:
        print(-1)
        continue
        
    if grid[r][c] == 'B':
        print(0)
        continue
        
    in_same_row = 'B' in grid[r]
    in_same_col = any(grid[i][c] == 'B' for i in range(n))
    
    if in_same_row or in_same_col:
        print(1)
    else:
        print(2)