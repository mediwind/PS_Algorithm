from collections import defaultdict

N = int(input())
board = [list(map(int, input())) for _ in range(N)]

color_grid = defaultdict(list)
for i in range(N):
    for j in range(N):
        if board[i][j]:
            color_grid[board[i][j]].append((i, j))

# 각 색들이 가질 수 있는 최좌상단, 최우하단 x, y좌표 찾기
for key in color_grid.keys():
    top_left = min(map(lambda x: x[0], color_grid[key])), min(map(lambda x: x[1], color_grid[key]))
    bottom_right = max(map(lambda x: x[0], color_grid[key])), max(map(lambda x: x[1], color_grid[key]))
    color_grid[key] = [top_left, bottom_right]

# 각 색의 영역(최좌상단부터 최우하단까지)내에 다른 색이 있다면 그 다른 색은 정답 후보에서 제외 처리
possible = {key: 1 for key in color_grid.keys()}
for color in color_grid.keys():
    x_start, x_end = color_grid[color][0][0], color_grid[color][1][0]
    y_start, y_end = color_grid[color][0][1], color_grid[color][1][1]
    for x in range(x_start, x_end + 1):
        for y in range(y_start, y_end + 1):
            if board[x][y] != color:
                possible[board[x][y]] = 0

print(sum(possible.values()))