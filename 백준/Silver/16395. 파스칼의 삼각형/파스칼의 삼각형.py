n, k = map(int, input().split())

dy = [[1], [1, 1]]

for i in range(2, n):
    tmp = list()
    for j in range(1, i):
        tmp.append(dy[i - 1][j - 1] + dy[i - 1][j])
    tmp = [1] + tmp + [1]
    dy.append(tmp)

print(dy[n - 1][k - 1])