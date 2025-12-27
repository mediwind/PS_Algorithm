import sys

input = sys.stdin.readline


def better(sum_a, flip_a, sum_b, flip_b):
    if sum_a != sum_b:
        return (sum_a, flip_a) if sum_a > sum_b else (sum_b, flip_b)
    return (sum_a, flip_a) if flip_a < flip_b else (sum_b, flip_b)


n = int(input().strip())
front = [0] + list(map(int, input().split()))
back = [0] + list(map(int, input().split()))

adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

parent = [0] * (n + 1)
order = []
stack = [1]
parent[1] = -1

while stack:
    v = stack.pop()
    order.append(v)
    for nxt in adj[v]:
        if nxt == parent[v]:
            continue
        parent[nxt] = v
        stack.append(nxt)

dp0_sum = [0] * (n + 1)
dp0_flip = [0] * (n + 1)
dp1_sum = [0] * (n + 1)
dp1_flip = [0] * (n + 1)

for v in reversed(order):
    child_sum0 = 0
    child_flip0 = 0
    child_sum1 = 0
    child_flip1 = 0

    for ch in adj[v]:
        if ch == parent[v]:
            continue
        child_sum0 += dp0_sum[ch]
        child_flip0 += dp0_flip[ch]
        child_sum1 += dp1_sum[ch]
        child_flip1 += dp1_flip[ch]

    opt_nf_sum = front[v] + child_sum0
    opt_nf_flip = child_flip0
    opt_f_sum = back[v] + child_sum1
    opt_f_flip = child_flip1 + 1
    dp0_sum[v], dp0_flip[v] = better(opt_nf_sum, opt_nf_flip, opt_f_sum, opt_f_flip)

    opt_nf_sum = back[v] + child_sum1
    opt_nf_flip = child_flip1
    opt_f_sum = front[v] + child_sum0
    opt_f_flip = child_flip0 + 1
    dp1_sum[v], dp1_flip[v] = better(opt_nf_sum, opt_nf_flip, opt_f_sum, opt_f_flip)

print(dp0_sum[1], dp0_flip[1])