import sys

K, N = map(int, input().split())
arr = list(map(int, input().split()))
cnt = [0] * (K + 1)
for v in arr:
    cnt[v] += 1

if (N + 1) % K == 0:
    t = (N + 1) // K
    for x in range(1, K + 1):
        if cnt[x] + 1 == t:
            ok = True
            for i in range(1, K + 1):
                if i == x:
                    continue
                if cnt[i] != t:
                    ok = False
                    break
            if ok:
                print(f"+{x}")
                sys.exit(0)

if (N - 1) % K == 0:
    t = (N - 1) // K
    for x in range(1, K + 1):
        if cnt[x] - 1 == t and cnt[x] > 0:
            ok = True
            for i in range(1, K + 1):
                if i == x:
                    continue
                if cnt[i] != t:
                    ok = False
                    break
            if ok:
                print(f"-{x}")
                sys.exit(0)

if N % K == 0:
    t = N // K
    plus = [i for i in range(1, K + 1) if cnt[i] == t + 1]
    minus = [i for i in range(1, K + 1) if cnt[i] == t - 1]
    if len(plus) == 1 and len(minus) == 1:
        ok = True
        for i in range(1, K + 1):
            if i in plus or i in minus:
                continue
            if cnt[i] != t:
                ok = False
                break
        if ok:
            print(f"-{plus[0]} +{minus[0]}")
            sys.exit(0)

print("*")