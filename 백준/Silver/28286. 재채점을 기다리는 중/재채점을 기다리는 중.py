def DFS(L, arr):
    global ans
    
    cnt = 0
    
    # 그냥 놓아두기 & 정답 개수 세기
    for i in range(n):
        if arr[i] == answer[i]:
            cnt += 1
    
    ans = max(ans, cnt)
    
    if L < k:
        for i in range(n):
            # 당기기
            tmp = arr[:i] + arr[i + 1:] + [0]
            DFS(L + 1, tmp)
            # 밀기
            tmp = arr[:i] + [0] + arr[i:-1]
            DFS(L + 1, tmp)


n, k = map(int, input().split())
answer = list(map(int, input().split()))
submit = list(map(int, input().split()))

ans = 0
cnt = 0
DFS(0, submit)
print(ans)