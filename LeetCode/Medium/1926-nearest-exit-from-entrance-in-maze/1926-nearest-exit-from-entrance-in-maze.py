class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def BFS(sx, sy):
            Q = deque()
            Q.append((sx, sy))
            ch = [[-1 for _ in range(m)] for _ in range(n)]
            ch[sx][sy] = 0

            while Q:
                x, y = Q.popleft()
                if ((x == 0 or x == n - 1) or (y == 0 or y == m - 1)) and (x != sx or y != sy):
                    return ch[x][y]

                for d in range(4):
                    xx = x + dx[d]
                    yy = y + dy[d]

                    if xx < 0 or xx >= n or yy < 0 or yy >= m:
                        continue
                    if ch[xx][yy] == -1 and maze[xx][yy] == ".":
                        Q.append((xx, yy))
                        ch[xx][yy] = ch[x][y] + 1
            
            return -1


        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        n, m = len(maze), len(maze[0])
        sx, sy = entrance
        ans = BFS(sx, sy)
        
        return ans