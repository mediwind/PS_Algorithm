from collections import deque
import sys
input = sys.stdin.readline


def hay_counting(x, y, num):
    Q = deque()
    Q.append((x, y))
    ch[x][y] = 1
    
    cnt = 1
    while Q:
        x, y = Q.popleft()
        
        for d in range(4):
            xx = x + dx[d]
            yy = y + dy[d]

            if xx < 0 or xx >= N or yy < 0 or yy >= 10:
                continue
            
            if not ch[xx][yy] and board[xx][yy] == num:
                ch[xx][yy] = 1
                cnt += 1
                Q.append((xx, yy))
    
    return cnt


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, K = map(int, input().strip().split())
board = [list(map(int, input().strip())) for _ in range(N)]

while True:
    # k개 이상으로 이루어진 클러스터 찾기
    ch = [[0 for _ in range(10)] for _ in range(N)]
    to_disappear = list()
    for i in range(N):
        for j in range(10):
            if not ch[i][j] and board[i][j]:
                num = board[i][j]
                res = hay_counting(i, j, num)
                if res >= K:
                    to_disappear.append((i, j, num))

    if not to_disappear:
        break
        
    # 조건에 부합하는 클러스터들을 제거 하기
    for sx, sy, num in to_disappear:
        Q = deque()
        Q.append((sx, sy))

        while Q:
            x, y = Q.popleft()

            for d in range(4):
                xx = x + dx[d]
                yy = y + dy[d]

                if xx < 0 or xx >= N or yy < 0 or yy >= 10:
                    continue

                if board[xx][yy] == num:
                    board[xx][yy] = 0
                    Q.append((xx, yy))

    # 공중에 뜬 haybale 낙하시키기
    for i in range(N - 1, 0, -1):
        for j in range(10):
            if not board[i][j]:
                for k in range(i - 1, -1, -1):
                    if board[k][j]:
                        board[i][j], board[k][j] = board[k][j], board[i][j]
                        break

for bd in board:
    tmp = map(str, bd)
    print(''.join(tmp))