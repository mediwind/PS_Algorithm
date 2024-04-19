def DFS():
    if arr:
        tmp = ''.join(map(str, arr))
        tmp = int(tmp)
        if not tmp in res:
            res[tmp] = 1
        
    for i in range(10):
        if not arr or i < arr[-1]:
            arr.append(i)
            DFS()
            arr.pop()


n = int(input())
arr = list()
res = dict()
DFS()
res = sorted(res.keys())
if n > len(res):
    print(-1)
else:
    print(res[n - 1])