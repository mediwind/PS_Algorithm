n = int(input())
a = list(map(int, input().split()))
last = {}
l = 0

ans = 0
for r, v in enumerate(a):
    if v in last and last[v] >= l:
        l = last[v] + 1
    last[v] = r
    ans += r - l + 1

print(ans)