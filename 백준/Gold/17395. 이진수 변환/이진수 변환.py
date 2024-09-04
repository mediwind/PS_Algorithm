def solve(B, N):
    cnt = bin(B).count('1')
    if cnt < N:
        return "-1"
    result = list()
    range_ = cnt - N + 1
    for _ in range(range_):
        B -= (B & -B)
    result.append(str(B))
    while B > 0:
        B -= (B & -B)
        result.append(str(B))
    return " ".join(result)


x, n = map(int, input().split())
print(solve(x, n))