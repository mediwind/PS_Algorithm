def DFS(L, _sum):
    global order, flag
    if _sum == n:
        order += 1
        if order == k:
            print('+'.join(map(str, res)))
            flag = True
        return
    
    for i in range(1, 4):
        if _sum + i <= n:
            res.append(i)
            _sum += i
            DFS(L + 1, _sum)
            res.pop()
            _sum -= i


n, k = map(int, input().split())
res = list()
order = 0
flag = False
DFS(0, 0)
if not flag:
    print(-1)