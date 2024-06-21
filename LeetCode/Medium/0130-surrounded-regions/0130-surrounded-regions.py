class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def BFS(sx, sy):
            Q = deque()
            Q.append((sx, sy))
            ch[sx][sy] = 1
            to_fill = [(sx, sy)]

            edge_flag = True if (sx == 0 or sx == n - 1) or (sy == 0 or sy == m - 1) else False
            while Q:
                x, y = Q.popleft()
                for d in range(4):
                    xx = x + dx[d]
                    yy = y + dy[d]
                    if xx < 0 or xx >= n or yy < 0 or yy >= m:
                        continue

                    if not ch[xx][yy] and board[xx][yy] == 'O':
                        if (xx == 0 or xx == n - 1) or (yy == 0 or yy == m - 1):
                            edge_flag = True
                        ch[xx][yy] = 1
                        Q.append((xx, yy))
                        to_fill.append((xx, yy))
            
            if edge_flag == False:
                for x, y in to_fill:
                    board[x][y] = 'X'

        n, m = len(board), len(board[0])

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        ch = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if not ch[i][j] and board[i][j] == 'O':
                    BFS(i, j)
        
        return board