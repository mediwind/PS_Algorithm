import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    
    ideal_b = r // 2 + 1
    
    if ideal_b >= l:
        print(r % ideal_b)
    else:
        print(r % l)