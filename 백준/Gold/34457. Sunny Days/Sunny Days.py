import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [input().rstrip() for _ in range(n)]

lt = 0
rain = 0
ans = 0

for rt in range(n):
    if arr[rt] == "P":
        rain += 1

    while rain > 1:
        if arr[lt] == "P":
            rain -= 1
        lt += 1

    ans = max(ans, rt - lt + 1)

if 'P' not in arr:
    ans -= 1

print(ans)