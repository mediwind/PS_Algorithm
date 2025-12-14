import sys
input = sys.stdin.readline
MOD = 998244353

P = int(input().rstrip())
problem_counts = []
for _ in range(P):
    Ni, Mi = map(int, input().rstrip().split())
    scores = list(map(int, input().rstrip().split()))
    edges = [tuple(map(int, input().rstrip().split())) for _ in range(Mi)]
    counts = [0] * 101
    for mask in range(1 << Ni):
        valid = True
        for x, y in edges:
            if (mask >> (y - 1)) & 1 and not (mask >> (x - 1)) & 1:
                valid = False
                break
        if not valid:
            continue
        total = 0
        for bit in range(Ni):
            if (mask >> bit) & 1:
                total += scores[bit]
        counts[total] += 1
    problem_counts.append(counts)

dp = [1]
max_score = 0
for counts in problem_counts:
    new_max = max_score + 100
    ndp = [0] * (new_max + 1)
    for t in range(max_score + 1):
        if dp[t] == 0:
            continue
        val = dp[t]
        for s, cnt in enumerate(counts):
            if cnt:
                ndp[t + s] = (ndp[t + s] + val * cnt) % MOD
    dp = ndp
    max_score = new_max

answer = sum(t * dp[t] for t in range(max_score + 1)) % MOD
print(answer)