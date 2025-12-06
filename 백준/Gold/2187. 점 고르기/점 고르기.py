import sys
input = sys.stdin.readline

N, A, B = map(int, input().strip().split())
coordinates = [tuple(map(int, input().strip().split())) for _ in range(N)]

ans = 0
for i in range(N):
    x1, y1, s1 = coordinates[i]
    for j in range(i + 1, N):
        x2, y2, s2 = coordinates[j]
        if abs(x1 - x2) <= A - 1 and abs(y1 - y2) <= B - 1:
            ans = max(ans, max(s1, s2) - min(s1, s2))

print(ans)