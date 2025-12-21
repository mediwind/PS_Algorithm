class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if not strs:
            return 0

        m = len(strs)
        cols = len(strs[0])
        locked = [False] * (m - 1)
        deletions = 0
        for j in range(cols):
            bad = False
            for i in range(m - 1):
                if not locked[i] and strs[i][j] > strs[i + 1][j]:
                    bad = True
                    break
            if bad:
                deletions += 1
                continue
            for i in range(m - 1):
                if not locked[i] and strs[i][j] < strs[i + 1][j]:
                    locked[i] = True
            if all(locked):
                break
                
        return deletions