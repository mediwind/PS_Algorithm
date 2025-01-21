# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lt, rt = 1, n
        while lt <= rt:
            mid = (lt + rt) // 2
            if isBadVersion(mid):
                rt = mid - 1
            else:
                lt = mid + 1
        return lt