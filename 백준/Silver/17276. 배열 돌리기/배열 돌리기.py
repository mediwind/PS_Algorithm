from copy import deepcopy

import sys
input = sys.stdin.readline


def clock_wise(d):
    global board
    cnt = d // 45
    for _ in range(cnt):
        copied_board = deepcopy(board)

        # 주 대각선을 가운데 열로
        for i in range(n):
            copied_board[i][n // 2] = board[i][i]

        # 가운데 열을 부 대각선으로
        for i in range(n):
            copied_board[i][n - 1 - i] = board[i][n // 2]

        # 부 대각선을 가운데 행으로
        for i in range(n):
            copied_board[n // 2][n - 1 - i] = board[i][n - 1 - i]

        # 가운데 행을 주 대각선으로
        for i in range(n):
            copied_board[i][i] = board[n // 2][i]
        
        board = deepcopy(copied_board)
    
    return board


def anti_clock_wise(d):
    global board
    cnt = abs(d) // 45
    for _ in range(cnt):
        copied_board = deepcopy(board)

        # 주 대각선을 가운데 행으로
        for i in range(n):
            copied_board[n // 2][i] = board[i][i]

        # 가운데 열을 주 대각선으로
        for i in range(n):
            copied_board[i][i] = board[i][n // 2]

        # 부 대각선을 부 가운데 열로
        for i in range(n):
            copied_board[i][n // 2] = board[i][n - 1 - i]

        # 가운데 행을 부 대각선으로
        for i in range(n):
            copied_board[n - 1 - i][i] = board[n // 2][i]
        
        board = deepcopy(copied_board)
    
    return board
    

t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    if d >= 0:
        ans = clock_wise(d)
    else:
        ans = anti_clock_wise(d)
    
    for a in ans:
        print(*a)