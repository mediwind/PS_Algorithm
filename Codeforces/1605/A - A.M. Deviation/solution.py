import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    a1, a2, a3 = map(int, input().split())
    
    diff = a1 + a3 - 2 * a2
    
    if diff % 3 == 0:
        print(0)
    else:
        print(1)