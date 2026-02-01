import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coef = [0] * (K + 2)
const = [0] * (K + 2)

for _ in range(N):
    S, E = map(int, input().split())
    coef[S] += 1
    coef[E + 1] -= 1

    c = -S + 1
    const[S] += c
    const[E + 1] -= c

res = []
cur_coef = 0
cur_const = 0

for d in range(1, K + 1):
    cur_coef += coef[d]
    cur_const += const[d]
    res.append(str(cur_coef * d + cur_const))

print(" ".join(res))