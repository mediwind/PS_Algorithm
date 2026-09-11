import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    for i in range(n - 1):
        if arr[i] <= arr[i + 1]:
            print("YES")
            break
    else:
        print("NO")