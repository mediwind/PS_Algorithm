import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    px, py = map(int, input().split())
    s = input().strip()
    
    u_count = s.count('U')
    d_count = s.count('D')
    r_count = s.count('R')
    l_count = s.count('L')
    
    possible_x = False
    possible_y = False
    
    if px >= 0:
        if r_count >= px:
            possible_x = True
    else:
        if l_count >= -px:
            possible_x = True
            
    if py >= 0:
        if u_count >= py:
            possible_y = True
    else:
        if d_count >= -py:
            possible_y = True
            
    if possible_x and possible_y:
        print("YES")
    else:
        print("NO")