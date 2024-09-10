def DFS(num):
    global res
    if num == n * 2:
        res += 1
        return
    
    if arr[num] == 0:
        for i in range(1, n + 1):
            if ch[i] == 0:
                if num + i + 1 <= 2 * n and arr[num + i + 1] == 0:
                    ch[i] = 1
                    arr[num] = i
                    arr[num + i + 1] = i
                    DFS(num + 1)
                    ch[i] = 0
                    arr[num] = 0
                    arr[num + i + 1] = 0
    else:
        DFS(num + 1)
    
    return


n, x, y = map(int, input().split())

arr = [0 for _ in range(n * 2 + 1)]
init_num = y - x - 1
arr[x] = arr[y] = init_num

ch = [0 for _ in range(n * 2 + 1)]
ch[y - x - 1] = 1

res = 0
DFS(1)
print(res)