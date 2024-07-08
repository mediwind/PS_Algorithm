class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def DFS(x, y, idx):
            if idx == len(word):
                return True
            
            if x < 0 or x >= n or y < 0 or y >= m:
                return False
            if board[x][y] != word[idx]:
                return False
            if (x, y) in ch:
                return False

            ch.add((x, y))
            res = (
                DFS(x + 1, y, idx + 1) or
                DFS(x - 1, y, idx + 1) or
                DFS(x, y + 1, idx + 1) or
                DFS(x, y - 1, idx + 1)
                )
            ch.remove((x, y))

            return res
        
        n, m = len(board), len(board[0])

        ch = set()
        for i in range(n):
            for j in range(m):
                if DFS(i, j, 0):
                    return True
        
        return False

        # O(n * m * 4^n)