import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    step = n // 2 + 1
    idx = len(arr) - 1 - (n // 2)
    
    total_median_sum = 0
    for _ in range(k):
        total_median_sum += arr[idx]
        idx -= step
        
    print(total_median_sum)