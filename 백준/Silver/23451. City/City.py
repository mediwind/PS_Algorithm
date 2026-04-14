import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 각 parity 그룹 개수
cnt = [[0, 0], [0, 0]]

for x in range(n + 1):
    for y in range(m + 1):
        cnt[x % 2][y % 2] += 1

# 정답 계산
ans = 0
for i in range(2):
    for j in range(2):
        c = cnt[i][j]
        ans += c * (c - 1) // 2

print(ans)