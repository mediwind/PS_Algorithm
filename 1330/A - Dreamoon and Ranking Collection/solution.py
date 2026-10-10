import sys
input = sys.stdin.readline
 
t = int(input())
 
for _ in range(t):
    n, x = map(int, input().split())
    rankings = set(map(int, input().split()))
    
    v = 1
    while True:
        if v in rankings:
            v += 1
        elif x > 0:
            x -= 1
            v += 1
        else:
            break
            
    print(v - 1)