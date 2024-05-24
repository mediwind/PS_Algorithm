n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

def total_sum():
    total = 0

    for row in range(n):
        _sum = 0
        for col in range(m):
            if visited[row][col]:
                _sum = _sum * 10 + arr[row][col]
            else:
                total += _sum
                _sum = 0
        total += _sum

    for col in range(m):
        _sum = 0
        for row in range(n):
            if not visited[row][col]:
                _sum = _sum * 10 + arr[row][col]
            else:
                total += _sum
                _sum = 0
        total += _sum

    return total

result = 0

def dfs(x, y):
    global result
    if x == n:
        result = max(result, total_sum())
        return

    if y == m:
        dfs(x + 1, 0)
        return

    visited[x][y] = True
    dfs(x, y + 1)

    visited[x][y] = False
    dfs(x, y + 1)

dfs(0, 0)
print(result)