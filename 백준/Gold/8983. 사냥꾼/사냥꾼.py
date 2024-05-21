import sys
input = sys.stdin.readline

M, N, L = map(int, input().split())
shooting_range = sorted(map(int, input().split()))
animals = [list(map(int, input().split())) for _ in range(N)]

res = 0
for x, y in animals:
    lt, rt = 0, M - 1
    while lt <= rt:
        mid = (lt + rt) // 2
        cal = abs(shooting_range[mid] - x) + y
        if cal <= L:
            res += 1
            break
        else:
            if x >= shooting_range[mid]:
                lt = mid + 1
            else:
                rt = mid - 1

print(res)