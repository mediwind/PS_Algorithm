from collections import deque

# 입력: 5x5 정수, 그 다음 시작 r c
board = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())

# 방향 벡터
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS
q = deque()
q.append((r, c, 0))  # (row, col, distance)
ch = [[0]*5 for _ in range(5)]
ch[r][c] = 1

while q:
    x, y, d = q.popleft()

    # 도착 조건: 현재 칸이 1이면 정답
    if board[x][y] == 1:
        print(d)
        exit()

    # 네 방향으로 걷기와 달리기 검사
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        # 걷기: 한 칸
        if 0 <= nx < 5 and 0 <= ny < 5 and board[nx][ny] != -1 and ch[nx][ny] == 0:
            ch[nx][ny] = 1
            q.append((nx, ny, d+1))

        # 달리기: 계속 전진
        rx, ry = x + dx[k], y + dy[k]
        # 만약 바로 다음 칸이 범위를 벗어나거나 -1이라면 달리기는 이동 없음(무시)
        if not (0 <= rx < 5 and 0 <= ry < 5) or board[rx][ry] == -1:
            continue

        # 달리면서 7 만나면 그 자리에서 멈추고, 아니면 마지막 유효칸에서 멈춤
        while 0 <= rx < 5 and 0 <= ry < 5 and board[rx][ry] != -1:
            if board[rx][ry] == 7:
                if ch[rx][ry] == 0:
                    ch[rx][ry] = 1
                    q.append((rx, ry, d+1))
                break
            rrx, rry = rx + dx[k], ry + dy[k]
            # 다음 칸이 범위 밖이거나 -1이면 현재 rx,ry가 마지막 유효칸 -> 멈춤
            if not (0 <= rrx < 5 and 0 <= rry < 5) or board[rrx][rry] == -1:
                if ch[rx][ry] == 0:
                    ch[rx][ry] = 1
                    q.append((rx, ry, d+1))
                break
            # 다음으로 계속
            rx, ry = rrx, rry

# 큐 소진: 도달 불가
print(-1)