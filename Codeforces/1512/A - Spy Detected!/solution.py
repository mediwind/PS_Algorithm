import sys
input = sys.stdin.readline
 
t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))
    
    if arr[0] == arr[1]:
        majority = arr[0]
    else:
        if arr[0] == arr[2]:
            majority = arr[0]
        else:
            majority = arr[1]
    
    for i in range(n):
        if arr[i] != majority:
            print(i + 1)
            break