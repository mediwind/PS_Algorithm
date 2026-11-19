import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    
    if n == 2:
        print(-1)
        continue
        
    arr = list()
    for i in range(1, 3):
        for j in range(i, n * n + 1, 2):
            arr.append(j)
    
    for i in range(0, n * n, n):
        print(*arr[i:i + n])