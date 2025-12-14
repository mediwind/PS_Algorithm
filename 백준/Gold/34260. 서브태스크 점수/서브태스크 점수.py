import sys
input = sys.stdin.readline
MOD = 998244353

P = int(input().strip())
results = []
for _ in range(P):
    line = input().split()
    if not line:
        break
    Ni = int(line[0])
    Mi = int(line[1])

    scores = list(map(int, input().split()))

    adj = [0] * Ni
    for _ in range(Mi):
        u, v = map(int, input().split())
        adj[v - 1] |= 1 << (u - 1)

    for k in range(Ni):
        for i in range(Ni):
            if (adj[i] >> k) & 1:
                adj[i] |= adj[k]

    valid_count = 0
    total_score_sum = 0

    for mask in range(1 << Ni):
        is_valid = True
        current_score = 0
        for i in range(Ni):
            if (mask >> i) & 1:
                if (adj[i] & ~mask) != 0:
                    is_valid = False
                    break
                current_score += scores[i]
        if is_valid:
            valid_count += 1
            total_score_sum += current_score

    results.append((valid_count, total_score_sum))

total_ways = 1
for c, s in results:
    total_ways = (total_ways * c) % MOD

final_ans = 0
for c, s in results:
    term = (s * total_ways) % MOD
    inv_c = pow(c, MOD - 2, MOD)
    term = (term * inv_c) % MOD
    final_ans = (final_ans + term) % MOD

print(final_ans)