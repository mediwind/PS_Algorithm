import sys
input = sys.stdin.readline
 
t = int(input().strip())
for _ in range(t):
    c1, c2, c3 = map(int, input().split())
    a1, a2, a3, a4, a5 = map(int, input().split())
 
    c1 -= a1
    c2 -= a2
    c3 -= a3
 
    if c1 < 0 or c2 < 0 or c3 < 0:
        print("NO")
        continue
 
    rem_a4 = max(0, a4 - c1)
 
    rem_a5 = max(0, a5 - c2)
 
    if c3 >= rem_a4 + rem_a5:
        print("YES")
    else:
        print("NO")