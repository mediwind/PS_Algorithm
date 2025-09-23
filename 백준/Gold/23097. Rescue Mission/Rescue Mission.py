N = int(input().strip())
arr = list(map(int, input().split()))
pref = [0 for _ in range(N + 1)]
for i in range(N):
    pref[i + 1] = (pref[i] + arr[i]) % 10

last = [-1 for _ in range(10)]
next_same = [-1 for _ in range(N + 1)]
for pos in range(N, -1, -1):
    m = pref[pos]
    next_same[pos] = last[m]
    last[m] = pos

res = list()
for i in range(N):
    t = next_same[i]
    if t == -1:
        res.append("-1")
    else:
        res.append(str(t - i))

print(" ".join(res))