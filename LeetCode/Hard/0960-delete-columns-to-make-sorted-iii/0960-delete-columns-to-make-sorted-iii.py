class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if not strs:
            return 0

        n = len(strs)
        m = len(strs[0])
        ok = [[False] * m for _ in range(m)]
        for i in range(m):
            for j in range(i, m):
                good = True
                for r in range(n):
                    if strs[r][i] > strs[r][j]:
                        good = False
                        break
                ok[i][j] = good
        dp = [1] * m
        best = 1
        for j in range(m):
            for i in range(j):
                if ok[i][j] and dp[i] + 1 > dp[j]:
                    dp[j] = dp[i] + 1
            if dp[j] > best:
                best = dp[j]
                
        return m - best