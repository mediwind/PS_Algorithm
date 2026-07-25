import sys
input = sys.stdin.readline
 
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]
 
t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    grid = [[0] * w for _ in range(h)]
    
    for r in range(h):
        for c in range(w):
            if r != 0 and r != h - 1 and c != 0 and c != w - 1:
                continue
                
            can_place = True
            for i in range(8):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < h and 0 <= nc < w:
                    if grid[nr][nc] == 1:
                        can_place = False
                        break
                        
            if can_place:
                grid[r][c] = 1
                
 
    for row in grid:
        print("".join(map(str, row)))
    print()