class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        deque = collections.deque

        n = len(grid)
        m = len(grid[0])
        orig = grid[row][col]
        visited = [[False for _ in range(m)] for _ in range(n)]
        borders = []

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        Q = deque()
        Q.append((row, col))
        visited[row][col] = True

        while Q:
            x, y = Q.popleft()
            is_border = False

            for d in range(4):
                xx = x + dx[d]
                yy = y + dy[d]

                # 인접한 곳이 grid 밖이거나 색이 다르다면 border
                if xx < 0 or xx >= n or yy < 0 or yy >= m or grid[xx][yy] != orig:
                    is_border = True
                elif not visited[xx][yy]:
                    visited[xx][yy] = True
                    Q.append((xx, yy))

            if is_border:
                borders.append((x, y))

        for x, y in borders:
            grid[x][y] = color

        return grid