import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
g = [int(input().strip()) for _ in range(m)]

in_sub = [False] * (n + 1)
for x in g:
    in_sub[x] = True

out = []
cur = 1

for x in g:
    while cur < x:
        if not in_sub[cur]:
            out.append(str(cur))
        cur += 1
    out.append(str(x))

while cur <= n:
    if not in_sub[cur]:
        out.append(str(cur))
    cur += 1

for res in out:
    print(res)