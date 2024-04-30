class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def check(sx, sy, ch):
            x, y = sx, sy
            cnt_1 = 0
            cnt_0 = 0
            for d in range(8):
                xx = x + dx[d]
                yy = y + dy[d]
                if xx < 0 or xx >= n or yy < 0 or yy >= m:
                    continue
                if board[xx][yy] == 1:
                    cnt_1 += 1
                else:
                    cnt_0 += 1
            
            if board[sx][sy] == 1:
                if cnt_1 < 2:
                    ch[sx][sy] = 1
                elif 2 <= cnt_1 <= 3:
                    ch[sx][sy] = 2
                elif cnt_1 > 3:
                    ch[sx][sy] = 3
            else:
                if cnt_1 == 3:
                    ch[sx][sy] = 4
            # print('sx:', sx, 'sy:', sy, 'ch[sx][sy]', ch[sx][sy])

                
        dx = [-1, -1, 0, 1, 1, 1, 0, -1]
        dy = [0, 1, 1, 1, 0, -1, -1, -1]
        
        n, m = len(board), len(board[0])
        ch = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                check(i, j, ch)

        for i in range(n):
            for j in range(m):
                if ch[i][j] == 1 or ch[i][j] == 3:
                    board[i][j] = 0
                elif ch[i][j] == 2 or ch[i][j] == 4:
                    board[i][j] = 1

        return board