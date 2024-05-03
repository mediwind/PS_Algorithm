while True:
    n, m = input().split()
    if n == '0' and m == '0.00':
        break
    n = int(n)
    m = int(float(m) * 100 + 0.5)

    arr = list()
    for _ in range(n):
        c, p = input().split()
        c = int(c)
        p = int(float(p) * 100 + 0.5)
        arr.append((c, p))

    arr.sort(key = lambda x: (x[1], x[0]))

    dy = [0 for _ in range(m + 1)]
    for c, p in arr:
        for i in range(p, m + 1):
            dy[i] = max(dy[i], dy[i - p] + c)

    print(dy[m])