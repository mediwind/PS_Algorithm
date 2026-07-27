import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n, m, rb, cb, rd, cd = map(int, input().split())
    
    if rb <= rd:
        t_row = rd - rb
    else:
        t_row = (n - rb) + (n - rd)
        
    if cb <= cd:
        t_col = cd - cb
    else:
        t_col = (m - cb) + (m - cd)
        
    print(min(t_row, t_col))