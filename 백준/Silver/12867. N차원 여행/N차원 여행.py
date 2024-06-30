import sys


def getpos(x, vt):
    return vt.index(x)


n = int(input())
m = int(input())
a = list(map(int, input().split()))
b = sorted(set(a))
sz = len(b)
arr = [[0 for _ in range(sz)] for _ in range(m + 2)]

direction = list(input())
for i in range(1, m + 1):
    ch = direction[i - 1]
    if ch == '+':
        arr[i][getpos(a[i-1], b)] += 1
    else:
        arr[i][getpos(a[i-1], b)] -= 1
    for j in range(sz):
        arr[i + 1][j] = arr[i][j]

for i in range(m):
    for j in range(i + 1, m + 1):
        ok = True
        for k in range(sz):
            if arr[i][k] != arr[j][k]:
                ok = False
                break

        if ok:
            print("0")
            sys.exit(0)
print("1")