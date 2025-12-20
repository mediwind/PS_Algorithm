class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if not strs:
            return 0

        m = len(strs[0])
        deletions = 0
        for j in range(m):
            for i in range(1, len(strs)):
                if strs[i][j] < strs[i - 1][j]:
                    deletions += 1
                    break
                    
        return deletions