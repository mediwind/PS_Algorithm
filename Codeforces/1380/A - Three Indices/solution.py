import sys
input = sys.stdin.readline
 
t = int(input())
 
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    found = False
    for j in range(1, n - 1):
        if p[j - 1] < p[j] and p[j] > p[j + 1]:
            print("YES")
            print(j, j + 1, j + 2)
            found = True
            break
            
    if not found:
        print("NO")