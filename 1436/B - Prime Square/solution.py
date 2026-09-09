import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    
    grid = [[0] * n for _ in range(n)]
    
    for i in range(n):
        grid[i][i] = 1
        grid[i][(i + 1) % n] = 1
        
    for row in grid:
        print(*row)