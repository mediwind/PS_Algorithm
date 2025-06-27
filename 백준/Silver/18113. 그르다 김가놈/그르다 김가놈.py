import sys
input = sys.stdin.readline


def cut(x):
    cnt = 0
    for a in arr:
        cnt += (a // x)
        
    return cnt


N, K, M = map(int, input().split())
arr = list()
for _ in range(N):
    num = int(input())
    if num >= 2 * K:
        num -= 2 * K
    else:
        if num < K:
            num = 0
        else:
            num -= K
    
    if num:
        arr.append(num)

if not arr:
    print(-1)
    sys.exit(0)

ans = -1
lt, rt = 1, max(arr)
while lt <= rt:
    mid = (lt + rt) // 2
    cnt = cut(mid)
    if cnt >= M:
        ans = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(ans)