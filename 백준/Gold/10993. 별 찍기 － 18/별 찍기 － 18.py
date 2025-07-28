def fill_star(row, col, n):
    if n == 1:
        stars[row][col] = '*'
        return

    row2 = 2 ** n - 1        # 삼각형 높이
    col2 = 2 ** (n + 1) - 3  # 밑변(또는 윗변) 길이
    half_w = 2 ** (n - 1)
    half_h = half_w - 1

    if n % 2:  # 홀수 → 위를 향하는(올라간) 삼각형
        # 밑변
        for i in range(col2):
            stars[row][col + i] = '*'
        # 왼쪽 변
        for i in range(row2):
            stars[row - i][col + i] = '*'
        # 오른쪽 변
        for i in range(row2):
            stars[row - i][col + col2 - 1 - i] = '*'
        # 내부 삼각형
        fill_star(row - half_h, col + half_w, n - 1)
    else:     # 짝수 → 아래를 향하는(내려간) 삼각형
        # 윗변
        for i in range(col2):
            stars[row][col + i] = '*'
        # 왼쪽 변
        for i in range(row2):
            stars[row + i][col + i] = '*'
        # 오른쪽 변
        for i in range(row2):
            stars[row + i][col + col2 - 1 - i] = '*'
        # 내부 삼각형
        fill_star(row + half_h, col + half_w, n - 1)


N = int(input())
row_size = 2 ** N - 1
col_size = 2 ** (N + 1) - 3
stars = [[' ' for _ in range(col_size)] for _ in range(row_size)]

if N % 2:  # 홀수 N: 위를 향하는 삼각형, 바닥(맨 아래)에서 시작
    fill_star(row_size - 1, 0, N)
else:      # 짝수 N: 아래를 향하는 삼각형, 천장(맨 위)에서 시작
    fill_star(0, 0, N)

for r in stars:
    print(''.join(r).rstrip())