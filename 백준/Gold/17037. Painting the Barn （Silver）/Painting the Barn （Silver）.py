width = 1000
barn = [[0 for _ in range(width + 1)] for _ in range(width + 1)]
n, k = map(int, input().split())
for _ in range(n):
    sx, sy, ex, ey = map(int, input().split())
    barn[sx][sy] += 1
    barn[sx][ey] -= 1
    barn[ex][sy] -= 1
    barn[ex][ey] += 1

answer = 0
for x in range(width + 1):
    for y in range(width + 1):
        if x > 0:
            barn[x][y] += barn[x - 1][y]
        if y > 0:
            barn[x][y] += barn[x][y - 1]
        if x > 0 and y > 0:
            barn[x][y] -= barn[x - 1][y - 1]
        answer += (barn[x][y] == k)

print(answer)