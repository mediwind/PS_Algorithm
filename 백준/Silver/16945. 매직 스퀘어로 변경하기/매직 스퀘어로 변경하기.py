from itertools import permutations


def check(perm):
    board = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(9):
        row = i // 3
        col = i % 3
        board[row][col] = perm[i]
    
    
    for i in range(3):
        if sum(board[i][:]) != 15:
            return
    
    for i in zip(*board):
        if sum(i) != 15:
            return
    
    if board[0][0] + board[1][1] + board[2][2] != 15:
        return
    
    if board[0][2] + board[1][1] + board[2][0] != 15:
        return
    
    difference = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != original[i][j]:
                difference += abs(board[i][j] - original[i][j])
    
    return difference


original = [list(map(int, input().split())) for _ in range(3)]

ans = float('inf')
for perm in permutations(list(range(1, 10)), 9):
    res = check(perm)
    if res != None:
        ans = min(ans, res)

print(ans)