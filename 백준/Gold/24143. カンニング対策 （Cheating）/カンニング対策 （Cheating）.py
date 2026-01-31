import sys
input = sys.stdin.readline


def check(limit):
    needed_y = 0
    if ys:
        needed_y = 1
        cover_end = ys[0] + limit

        for i in range(1, M):
            if ys[i] > cover_end:
                needed_y += 1
                cover_end = ys[i] + limit

    needed_x = 0
    if xs:
        needed_x = 1
        cover_end = xs[0] + limit

        for i in range(1, M):
            if xs[i] > cover_end:
                needed_x += 1
                cover_end = xs[i] + limit

    return (needed_y + needed_x) <= N


N, M = map(int, input().split())

xs = []
ys = []
for _ in range(M):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

xs.sort()
ys.sort()

low = 0
high = 10**9
ans = high

while low <= high:
    mid = (low + high) // 2

    if check(mid):
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print(ans)