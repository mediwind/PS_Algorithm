n, m = map(int, input().split())

paper = [list(map(int, input())) for _ in range(n)]
ans = list()

for i in range(1 << n*m):
    total = 0
    # [Case 1] Calculate horizontal combinations
    for x in range(n):
        rowsum = 0
        for y in range(m):
            idx = x*m + y
            if i & (1 << idx) != 0:
                rowsum = rowsum * 10 + paper[x][y]
            else:
                total += rowsum
                rowsum = 0
        total += rowsum

    # [Case 2] Calculate vertical combinations
    for y in range(m):
        colsum = 0
        for x in range(n):
            idx = x*m + y
            if i & (1 << idx) == 0:
                colsum = colsum * 10 + paper[x][y]
            else:
                total += colsum
                colsum = 0
        total += colsum
    ans.append(total)

print(max(ans))