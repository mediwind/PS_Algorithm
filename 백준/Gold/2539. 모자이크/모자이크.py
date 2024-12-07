import sys
input = sys.stdin.readline


def covering(x):
    cnt = 1
    prev = columns[0] - 1
    if len(columns) > 1:
        for col in columns:
            if col > prev + x:
                cnt += 1
                prev = col - 1
    
    return cnt


r, c = map(int, input().split())
n = int(input())
s = int(input())
spaces = [list(map(int, input().split())) for _ in range(s)]
columns = list(col for row, col in sorted(spaces, key = lambda x: x[1]))

lt, rt = max(spaces, key = lambda x: x[0])[0], r
ans = r
while lt <= rt:
    mid = (lt + rt) // 2
    res = covering(mid)
    if res <= n:
        ans = min(ans, mid)
        rt = mid - 1
    else:
        lt = mid + 1

print(ans)