import sys

MOD = 31991
input = sys.stdin.readline


def matmul(A,B):
    n=len(A)
    C=[[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k]==0: continue
            for j in range(n):
                C[i][j]=(C[i][j]+A[i][k]*B[k][j])%MOD
    return C


def matpow(A,e):
    n=len(A)
    R=[[0]*n for _ in range(n)]
    for i in range(n):
        R[i][i]=1
    while e:
        if e&1:
            R=matmul(R,A)
        A=matmul(A,A)
        e//=2
    return R


d, t = map(int, input().split())

if t == 0:
    print(1)
    sys.exit(0)

init = [0]*(d)
init[0] = 1

for i in range(1, d):
    init[i] = sum(init[:i]) % MOD

if t < d:
    print(init[t] % MOD)
    sys.exit(0)

mat = [[0]*d for _ in range(d)]

for i in range(d):
    mat[0][i] = 1

for i in range(1, d):
    mat[i][i-1] = 1

M = matpow(mat, t-(d-1))

res = 0
for i in range(d):
    res = (res + M[0][i]*init[d-1-i]) % MOD

print(res)