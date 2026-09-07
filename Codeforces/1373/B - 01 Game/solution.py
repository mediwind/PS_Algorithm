import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    s = input().strip()
    
    c0 = s.count('0')
    c1 = s.count('1')
    
    total_moves = min(c0, c1)
    
    if total_moves % 2 == 1:
        print("DA")
    else:
        print("NET")