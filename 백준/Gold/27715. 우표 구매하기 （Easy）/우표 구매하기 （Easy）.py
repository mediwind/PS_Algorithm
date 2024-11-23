def combination(n, k, comb):
    n = n + k - 1
    if n < 0:
        return 1
    return comb[n][k]


n, m, k, p = map(int, input().split())
MAX_SIZE = 2010

comb = [[0] * MAX_SIZE for _ in range(MAX_SIZE)]
comb[0][0] = 1
for i in range(1, MAX_SIZE):
    comb[i][0] = comb[i][i] = 1
    for j in range(1, i):
        comb[i][j] = (comb[i-1][j] + comb[i-1][j-1]) % p

result = 0
for i in range(0, k // 2 + 1):
    result = (result + (combination(n, k - i * 2, comb) * combination(m, i, comb)) % p) % p

print(result)