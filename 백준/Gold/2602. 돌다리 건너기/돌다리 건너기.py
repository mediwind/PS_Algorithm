order = input()
bridge = [input() for _ in range(2)]

o_leng = len(order)
b_leng = len(bridge[0])

dy = [[[0 for _ in range(2)] for _ in range(o_leng)] for _ in range(b_leng)]
for i in range(b_leng):
    for j in range(o_leng):
        for k in range(2):
            if bridge[k][i] == order[j]:
                if j == 0:
                    dy[i][j][k] = 1
                else:
                    for l in range(i):
                        dy[i][j][k] += dy[l][j - 1][1 - k]

res = 0
for i in range(b_leng):
    for j in range(2):
        res += dy[i][-1][j]

print(res)