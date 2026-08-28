import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    k = 0
    for i in range(n):
        while arr[i] % 2 == 0:
            arr[i] //= 2
            k += 1
            
    arr.sort()
    arr[-1] *= (1 << k)
    
    print(sum(arr))