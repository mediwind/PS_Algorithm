import sys
input = sys.stdin.readline


def read_ints_needed(cnt: int):
    res = []
    while len(res) < cnt:
        parts = input().strip().split()
        if parts:
            res.extend(map(int, parts))
    return res[:cnt]


m, k = map(int, input().strip().split())
c = [0] + read_ints_needed(m)

d = [0] * (m + 1)
total_cost = 0

dq = []
head = 0

for i in range(1, m + 1):
    left = i - k + 1
    if left < 1:
        left = 1

    while head < len(dq) and dq[head] < left:
        head += 1

    while len(dq) > head and c[dq[-1]] > c[i]:
        dq.pop()
    dq.append(i)

    if head > 4096:
        dq = dq[head:]
        head = 0

    best = dq[head]
    d[best] += 2
    total_cost += 2 * c[best]

print(total_cost)
print(" ".join(str(d[i]) for i in range(1, m + 1)))