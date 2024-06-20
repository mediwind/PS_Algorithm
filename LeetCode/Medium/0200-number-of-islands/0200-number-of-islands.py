class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def BFS(x, y):
            Q = deque()
            Q.append((x, y))
            while Q:
                x, y = Q.popleft()
                for d in range(4):
                    xx = x + dx[d]
                    yy = y + dy[d]
                    if xx < 0 or xx >= n or yy < 0 or yy >= m:
                        continue
                    if grid[xx][yy] == '1':
                        grid[xx][yy] = 0
                        Q.append((xx, yy))
        
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        n, m = len(grid), len(grid[0])
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    BFS(i, j)
                    cnt += 1
        
        return cnt