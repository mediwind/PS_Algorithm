def DFS(total):
    global ans
    
    if len(arr) == 2:
        ans = max(ans, total)
    
    for i in range(1, len(arr) - 1):
        energy = arr[i - 1] * arr[i + 1]
        
        poped = arr.pop(i)
        DFS(total + energy)
        arr.insert(i, poped)


n = int(input())
arr = list(map(int, input().split()))

ans = 0
DFS(0)
print(ans)