t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
 
    while k > 0:
        for i in range(n):
            if arr[i] > 0:
                arr[i] -= 1
                arr[n - 1] += 1
                break
        k -= 1
 
    print(*arr)