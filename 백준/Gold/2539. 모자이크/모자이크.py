import sys
input = sys.stdin.readline


def covering(x):
    ch = {columns[0] + i for i in range(x)}
    cnt = 1
    for i in range(1, len(columns)):
        if columns[i] not in ch:
            for j in range(x):
                ch.add(columns[i] + j)
            cnt += 1
    
    return cnt


r, c = map(int, input().split())
n = int(input())
s = int(input())
spaces = [list(map(int, input().split())) for _ in range(s)]
columns = list(col for row, col in sorted(spaces, key = lambda x: x[1]))

lt, rt = max(spaces, key = lambda x: x[0])[0], r
ans = float("inf")
while lt <= rt:
    mid = (lt + rt) // 2
    res = covering(mid)
    if res <= n:
        ans = min(ans, mid)
        rt = mid - 1
    else:
        lt = mid + 1

print(ans)