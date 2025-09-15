N = int(input().strip())
k = (N + 1) // 2
odds = list(range(N - k + 1, N + 1))
evens = list(range(1, N - k + 1))[::-1]

res = [0 for _ in range(N)]
oi = 0
ei = 0
for i in range(N):
    if i % 2 == 0:
        res[i] = odds[oi]
        oi += 1
    else:
        res[i] = evens[ei]
        ei += 1

print(' '.join(map(str, res)))