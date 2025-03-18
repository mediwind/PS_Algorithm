import sys
input = sys.stdin.readline

def check(x):
    start = x
    for time, limit, cost in works:
        if start > time:
            return False
        start += cost

    return True


n = int(input())
works = list()
for _ in range(n):
    cost, limit = map(int, input().split())
    btw = limit - cost
    works.append((btw, limit, cost))
works.sort(key = lambda x: x[1])

ans = -1
lt, rt = 0, works[0][0]
while lt <= rt:
    mid = (lt + rt) // 2
    if check(mid):
        lt = mid + 1
        ans = max(ans, mid)
    else:
        rt = mid - 1

print(ans)