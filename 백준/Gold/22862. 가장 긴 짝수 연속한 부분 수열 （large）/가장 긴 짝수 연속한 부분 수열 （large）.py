n, k = map(int, input().split())
arr = list(map(int, input().split()))

# n, k = 13, 4
# arr = [1, 3, 5, 2, 4, 7, 6, 9, 11, 3, 8, 10, 12]

lt, rt = 0, 0
odd_cnt = 0
ans = 0

while rt < n:
    # lt ~ rt 범위에 홀수들이 아직 K개 이하일 때
    if odd_cnt <= k:
        if arr[rt] % 2:
            odd_cnt += 1
        rt += 1
    # 홀수들의 개수가 K개를 초과했을 때
    else:
        # 홀수 개수를 줄이기 위해 lt를 전진시키며 이때 lt위치가 홀수라면
        if arr[lt] % 2:
            # 홀수의 개수를 줄임
            odd_cnt -= 1
        lt += 1
    
    # lt ~ rt 범위에 담긴 홀수들의 개수가 K이하일 때마다 정답 최신화
    if odd_cnt <= k:
        ans = max(ans, rt - lt - odd_cnt)

print(ans)