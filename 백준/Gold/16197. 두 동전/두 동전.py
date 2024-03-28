from collections import deque


def BFS(coin):
    Q = deque()
    Q.append(coin)
    while Q:
        x1, y1, x2, y2, cnt = Q.popleft()
    
        if cnt >= 10:
            return -1
    
        for d in range(4):
            nx1, ny1 = x1 + dx[d], y1 + dy[d]
            nx2, ny2 = x2 + dx[d], y2 + dy[d]

            if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m: # 두 동전 모두 보드 내에 존재
                if board[nx1][ny1] == '#':
                    nx1, ny1 = x1, y1
                if board[nx2][ny2] == '#':
                    nx2, ny2 = x2, y2
                Q.append((nx1, ny1, nx2, ny2, cnt + 1))
            elif 0 <= nx1 < n and 0 <= ny1 < m: # coin_1만 보드 내에 존재 (coin_2는 바깥으로 떨어짐)
                return cnt + 1
            elif 0 <= nx2 < n and 0 <= ny2 < m: # coin_2만 보드 내에 존재 (coin_1은 바깥으로 떨어짐)
                return cnt + 1
            else: # 이 else까지 왔다는 것은 coin_1, coin_2 모두 보드 바깥으로 떨어졌다는 의미
                continue
    
    return -1


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
# board

# 동전 'o'의 위치 찾기
coin = list()
for i in range(n):
    for j in range(m):
        if board[i][j] == 'o':
            coin += [i, j]

coin += [0]
# coin
res = BFS(coin)
print(res)