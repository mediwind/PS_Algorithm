import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    
    if 2 * k >= n:
        print("NO")
        continue
        
    possible = True
    for i in range(k):
        if s[i] != s[n - 1 - i]:
            possible = False
            break
            
    if possible:
        print("YES")
    else:
        print("NO")