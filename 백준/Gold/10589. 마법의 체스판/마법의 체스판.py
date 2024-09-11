n, m = map(int, input().split())

ans = list()
for x in range(2, n + 1, 2):
    ans.append((x, 1, x, m))
for y in range(2, m + 1, 2):
    ans.append((1, y, n, y))

print(len(ans))
for x1, y1, x2, y2 in ans:
    print(x1, y1, x2, y2)