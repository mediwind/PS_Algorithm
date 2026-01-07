from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

holes = []
for i in range(N):
    for j in range(M):
        if board[i][j] == '.':
            # 가장자리에 있는 구멍인지 확인
            if i == 0 or i == N-1 or j == 0 or j == M-1:
                holes.append((i, j))

start, end = holes[0], holes[1]

# 나중에 최단 경로인 곳만 다시 '.'로 바꿀 예정임
for i in range(N):
    for j in range(M):
        if board[i][j] == '.':
            board[i][j] = '@'

# visited에는 '방문 여부' 대신 '나를 이곳으로 보낸 이전 좌표(부모)'를 저장
parent = [[None] * M for _ in range(N)]

queue = deque([start])
parent[start[0]][start[1]] = start # 시작점의 부모는 자기 자신(혹은 표식)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 시작
found = False
while queue:
    x, y = queue.popleft()

    if (x, y) == end:
        found = True
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] != '+' and parent[nx][ny] is None:
                parent[nx][ny] = (x, y)
                queue.append((nx, ny))

# 도착점에서 시작점까지 역추적하며 길('.') 뚫기
curr_x, curr_y = end
while True:
    board[curr_x][curr_y] = '.' # 진짜 경로니까 원상복구

    if (curr_x, curr_y) == start:
        break

    # 부모를 타고 이동
    curr_x, curr_y = parent[curr_x][curr_y]

for row in board:
    print("".join(row))