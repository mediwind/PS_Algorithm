def DFS(L, x, y):
    global res, cnt
    if L == length - 1:
        cnt += 1
        return
    
    for d in range(8):
        xx = (x + dx[d])%n
        yy = (y + dy[d])%m
        if board[xx][yy] == word[L + 1]:
            res += board[xx][yy]
            DFS(L + 1, xx, yy)
            res = res[:-1]


n, m, k = map(int, input().split())
board = [list(input()) for _ in range(n)]

dx = [-1, -1 ,0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

words = [input() for _ in range(k)]
cases = dict()
for word in set(words):
    length = len(word)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == word[0]:
                res = word[0]
                DFS(0, i, j)
    cases[word] = cnt

for word in words:
    print(cases[word])