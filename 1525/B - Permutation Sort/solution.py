import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    sorted_arr = sorted(arr)
    
    if arr == sorted_arr:
        print(0)
    elif arr[0] == 1 or arr[-1] == n:
        print(1)
    elif arr[0] == n and arr[-1] == 1:
        print(3)
    else:
        print(2)