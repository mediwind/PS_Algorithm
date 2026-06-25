import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    total_sum = sum(arr)
    
    if total_sum % n == 0:
        print(0)
    else:
        print(1)