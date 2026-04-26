import sys
from heapq import heappush, heappop
input = sys.stdin.readline

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)
DIR4 = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def pack_board(board):
    state = 0
    for num in board:
        state = state * 10 + num
    return state


def unpack_board(state):
    board = [0] * 9
    for i in range(8, -1, -1):
        board[i] = state % 10
        state //= 10
    return board


def out_of_bounds(y, x):
    return not (0 <= y < 3 and 0 <= x < 3)


def calc_heuristic(board):
    dist = 0

    for idx, value in enumerate(board):
        if value == 0:
            continue

        target = value - 1

        y1, x1 = divmod(idx, 3)
        y2, x2 = divmod(target, 3)

        dist += abs(y1 - y2) + abs(x1 - x2)

    return dist


def make_next_board(board, x, y, nx, ny):
    new_board = board[:]

    a = y * 3 + x
    b = ny * 3 + nx

    new_board[a], new_board[b] = new_board[b], new_board[a]

    return new_board


def is_solvable(board):
    inversion = 0

    for i in range(9):
        if board[i] == 0:
            continue

        for j in range(i):
            if board[j] > board[i]:
                inversion += 1

    return inversion % 2 == 0


def solve(board, empty_x, empty_y):
    if not is_solvable(board):
        return -1

    start_state = pack_board(board)

    pq = []
    visited = {start_state}

    start_h = calc_heuristic(board)

    # (f, g, state, x, y)
    heappush(pq, (start_h, 0, start_state, empty_x, empty_y))

    while pq:
        _, move_cnt, state, x, y = heappop(pq)

        cur_board = unpack_board(state)

        if tuple(cur_board) == GOAL:
            return move_cnt

        for dx, dy in DIR4:
            nx = x + dx
            ny = y + dy

            if out_of_bounds(ny, nx):
                continue

            next_board = make_next_board(cur_board, x, y, nx, ny)
            next_state = pack_board(next_board)

            if next_state in visited:
                continue

            visited.add(next_state)

            next_g = move_cnt + 1
            next_h = calc_heuristic(next_board)

            heappush(
                pq,
                (next_g + next_h, next_g, next_state, nx, ny)
            )

    return -1


t = int(input())

answer = []

for _ in range(t):
    board = []

    # blank skip
    row = input().strip()
    while row == "":
        row = input().strip()

    empty_x = empty_y = -1

    for y in range(3):
        if y > 0:
            row = input().strip()

        for x, ch in enumerate(row):
            if ch == '#':
                board.append(0)
                empty_x = x
                empty_y = y
            else:
                board.append(int(ch))

    moves = solve(board, empty_x, empty_y)
    answer.append("impossible" if moves == -1 else str(moves))

print(*answer, sep="\n")