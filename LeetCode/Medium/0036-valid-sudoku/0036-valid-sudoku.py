class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 3X3 check
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                ch = {k:0 for k in range(1, 10)}
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        if board[k][l].isdigit():
                            ch[board[k][l]] = ch.get(board[k][l], 0) + 1
                            if ch[board[k][l]] >= 2:
                                return False
        
        # rows check
        for i in range(9):
            ch = {k:0 for k in range(1, 10)}
            for j in range(9):
                if board[i][j].isdigit():
                    ch[board[i][j]] = ch.get(board[i][j], 0) + 1
                    if ch[board[i][j]] >= 2:
                        return False
        
        # columns check
        for i in range(9):
            ch = {k:0 for k in range(1, 10)}
            for j in range(9):
                if board[j][i].isdigit():
                    ch[board[j][i]] = ch.get(board[j][i], 0) + 1
                    if ch[board[j][i]] >= 2:
                        return False
        
        return True