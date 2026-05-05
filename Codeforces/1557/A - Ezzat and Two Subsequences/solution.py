import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    
    arr = list(map(int, input().split()))
    arr.sort()
    
    A = sum(arr[:-1]) / (n - 1)
    B = arr[-1]
    
    print(A + B)