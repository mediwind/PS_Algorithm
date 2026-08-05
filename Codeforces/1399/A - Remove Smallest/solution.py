import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    
    for i in range(n - 1):
        if abs(arr[i + 1] - arr[i]) > 1:
            print("NO")
            break
    else:
        print("YES")