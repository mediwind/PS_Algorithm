class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dy = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dy[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dy[i + 1][j]:
                    dy[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dy[i][j + 1]:
                    dy[i][j] = True
        return dy[0][0]

        dy = {}
        # k = i + j
        def DFS(i, j):
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in dy:
                return dy[(i, j)]
            
            if i < len(s1) and s1[i] == s3[i + j] and DFS(i + 1, j):
                return True
            if j < len(s2) and s2[j] == s3[i + j] and DFS(i, j + 1):
                return True
            dy[(i, j)] = False
            return False
        
        return DFS(0, 0)