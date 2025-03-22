import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

dy = [0 for _ in range(N + 1)]

for _ in range(K):
    score, time = map(int, input().rstrip().split())
    for i in range(N, time - 1, -1):
        dy[i] = max(dy[i], dy[i - time] + score)

print(max(dy))