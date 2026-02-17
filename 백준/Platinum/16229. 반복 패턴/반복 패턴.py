import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = input().strip()

if N == 0:
    print(0)
    sys.exit(0)

Z = [0] * N
L, R = 0, 0
for i in range(1, N):
    if i <= R:
        Z[i] = min(R - i + 1, Z[i - L])
    while i + Z[i] < N and S[Z[i]] == S[i + Z[i]]:
        Z[i] += 1
    if i + Z[i] - 1 > R:
        L, R = i, i + Z[i] - 1

ans = 0

for length in range(1, N):
    if Z[length] == N - length:
        rem = N % length
        needed = (length - rem) % length

        if N + needed < 2 * length:
            needed += length

        if needed <= K:
            ans = max(ans, length)

if K >= N:
    ans = max(ans, N)

print(ans)