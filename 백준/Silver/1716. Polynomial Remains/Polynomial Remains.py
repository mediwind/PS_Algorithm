n, k = map(int, input().split())
while not (n == -1 and k == -1):
    pol = list(map(int, input().split()))
    for i in range(n, k - 1, -1):
        if i - k >= 0:
            pol[i - k] -= pol[i]
        pol[i] = 0

    result = list()
    for i in range(n + 1):
        if pol[i]:
            result.append(pol[i])
    if not result:
        result.append(0)

    print(' '.join(map(str, result)))
    n, k = map(int, input().split())