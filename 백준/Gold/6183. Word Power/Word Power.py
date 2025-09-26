from bisect import bisect_right
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
names = [input().rstrip().lower() for _ in range(N)]
goods = [input().rstrip().lower() for _ in range(M)]

for name in names:
    pos = {}
    for i, ch in enumerate(name):
        pos.setdefault(ch, []).append(i)
    cnt = 0
    for g in goods:
        cur = -1
        ok = True
        for ch in g:
            lst = pos.get(ch)
            if not lst:
                ok = False
                break
            idx = bisect_right(lst, cur)
            if idx == len(lst):
                ok = False
                break
            cur = lst[idx]
        if ok:
            cnt += 1
    print(cnt)