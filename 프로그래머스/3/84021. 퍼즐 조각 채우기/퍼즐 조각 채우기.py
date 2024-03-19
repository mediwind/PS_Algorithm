from collections import deque


def where(board, oz):
    n = len(board)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    res = list()
    ch = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == oz and not ch[i][j]:
                Q = deque()
                Q.append((i, j))
                tmp = list()
                tmp.append((i, j))
                ch[i][j] = 1
                
                while Q:
                    x, y = Q.popleft()
                    for d in range(4):
                        xx = x + dx[d]
                        yy = y + dy[d]
                        if xx >= 0 and xx < n and yy >= 0 and yy < n:
                            if board[xx][yy] == oz and not ch[xx][yy]:
                                Q.append((xx, yy))
                                tmp.append((xx, yy))
                                ch[xx][yy] = 1
            
                res.append(tmp)
    
    return res


def ground(arr):
    x, y = list(zip(*arr))
    row, col = max(x) - min(x) + 1, max(y) - min(y) + 1
    board = [[0 for _ in range(col)] for _ in range(row)]
    
    for i, j in arr:
        i, j = i - min(x), j - min(y)
        board[i][j] = 1
    
    return board


def rotate_90(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]


def solution(game_board, table):
    answer = 0
    to_put = where(game_board, 0)
    to_use = where(table, 1)
    
    # print('to_put')
    # for tp in to_put:
    #     print(tp)
    # print()
    # print('to_use')
    # for tu in to_use:
    #     print(tu)

    for tp in to_put:
        filled = False
        putting_ground = ground(tp)
        # print('putting_ground')
        # print(putting_ground)
        for tu in to_use:
            if filled:
                break
            
            block = ground(tu)
            # print('block')
            # print(block)
            for _ in range(4):
                block = rotate_90(block)
                # print('rotated_block')
                # print(block)
                
                if putting_ground == block:
                    size = sum(map(sum, block))
                    answer += size
                    to_use.remove(tu)
                    filled = True
                    break
    
    return answer

# game_board = [
#     [1,1,0,0,1,0],
#     [0,0,1,0,1,0],
#     [0,1,1,0,0,1],
#     [1,1,0,1,1,1],
#     [1,0,0,0,1,0],
#     [0,1,1,1,0,0]]
# table = [
#     [1,0,0,1,1,0],
#     [1,0,1,0,1,0],
#     [0,1,1,0,1,1],
#     [0,0,1,0,0,0],
#     [1,1,0,1,1,0],
#     [0,1,0,0,0,0]]

# solution(game_board, table)