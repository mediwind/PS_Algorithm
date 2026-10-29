import sys
input = sys.stdin.readline
 
grid = [list(map(int, input().split())) for _ in range(3)]
 
directions = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
 
for r in range(3):
    row_result = []
    for c in range(3):
        total_presses = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                total_presses += grid[nr][nc]
        
        if total_presses % 2 == 0:
            row_result.append("1")
        else:
            row_result.append("0")
            
    print("".join(row_result))