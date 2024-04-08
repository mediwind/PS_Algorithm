def DFS(open_1, open_2, L, cnt):
    global ans, k
#     print(open_1, open_2, L, cnt)
    
    if L == k:
        ans = min(ans, cnt)
        return
    
    res_1 = abs(to_use[L] - open_1)
    res_2 = abs(to_use[L] - open_2)
    
    DFS(to_use[L], open_2, L + 1, cnt + res_1)
    DFS(open_1, to_use[L], L + 1, cnt + res_2)


n = int(input())
open_1, open_2 = map(int, input().split())
k = int(input())
to_use = [int(input()) for _ in range(k)]

ans = float('inf')
DFS(open_1, open_2, 0, 0)
print(ans)