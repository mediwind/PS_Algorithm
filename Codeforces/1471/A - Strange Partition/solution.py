from math import ceil
import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    
    a = ceil(sum(arr) / x)
    b = 0
    for num in arr:
        b += ceil(num / x)
    
    print(min(a, b), max(a, b))