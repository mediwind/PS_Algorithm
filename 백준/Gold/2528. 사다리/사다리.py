import sys
input = sys.stdin.readline

N, L = map(int, input().split())
length = [0]*(N+1)
dirc = [0]*(N+1)

for i in range(1, N+1):
    l, d = map(int, input().split())
    length[i] = l
    dirc[i] = d


def get_pos(i, t):
    l = length[i]
    d = dirc[i]
    span = L - l
    if span == 0:
        return 0, l

    period = 2 * span
    p = t % period

    if p <= span:
        pos = p
    else:
        pos = period - p

    if d == 1:
        pos = span - pos

    return pos, pos + l


def overlap(i, j, t):
    l1, r1 = get_pos(i, t)
    l2, r2 = get_pos(j, t)
    return not (r1 < l2 or r2 < l1)


time = 0

for i in range(1, N):
    found = False
    for t in range(time, time + 2*L + 5):
        if overlap(i, i+1, t):
            time = t
            found = True
            break
    if not found:
        print(-1)
        sys.exit(0)

print(time)