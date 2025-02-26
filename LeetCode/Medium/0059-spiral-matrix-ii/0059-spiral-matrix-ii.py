class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dx = [1, 0, -1, 0]
        dy = [0, -1, 0, 1]

        board = [[0 for _ in range(n)] for _ in range(n)]
        board[0] = list(range(1, n + 1))

        sx, sy, d = 1, n - 1, 0
        num = n + 1

        if num >= n ** 2:
            return board

        Q = collections.deque()
        Q.append((sx, sy))
        while Q:
            x, y = Q.popleft()
            
            board[x][y] = num
            num += 1

            if num > n ** 2:
                break

            xx = x + dx[d]
            yy = y + dy[d]

            if xx < 0 or xx >= n or yy < 0 or yy >= n or board[xx][yy]:
                d = (d + 1) % 4
                xx = x + dx[d]
                yy = y + dy[d]
                Q.append((xx, yy))
                continue
            
            Q.append((xx, yy))
        
        return board