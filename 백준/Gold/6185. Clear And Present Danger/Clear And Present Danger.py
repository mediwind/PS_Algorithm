import sys
# input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

path = list()
for _ in range(m):
    path.append(int(input()) - 1)

danger = list()
for _ in range(n):
    danger.append(list(map(int, input().rstrip().split())))

dist = [[float('inf')] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            dist[i][j] = 0
        else:
            dist[i][j] = danger[i][j]

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

total_danger = 0
for i in range(m - 1):
    total_danger += dist[path[i]][path[i+1]]

print(total_danger)