class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


        def BFS(Q):
            while Q:
                x, y = Q.popleft()
                for d in range(4):
                    xx = x + dx[d]
                    yy = y + dy[d]
                    if xx < 0 or xx >= n or yy < 0 or yy >= m:
                        continue
                    if not ch[xx][yy] and grid[xx][yy] == 1:
                        grid[xx][yy] = 2
                        ch[xx][yy] = ch[x][y] + 1
                        Q.append((xx, yy))


        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        n, m = len(grid), len(grid[0])

        Q = deque()
        ch = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    Q.append((i, j))
        
        BFS(Q)
        print(grid)
        print(ch)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1

        return max(map(max, ch))