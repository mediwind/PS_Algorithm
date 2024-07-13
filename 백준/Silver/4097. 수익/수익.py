import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    
    arr = [int(input()) for _ in range(n)]
    dy = [0 for _ in range(n)]
    dy[0] = arr[0]
    
    for i in range(1, n):
        dy[i] = max(dy[i - 1] + arr[i], arr[i])
    
    print(max(dy))