class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lt, rt = 0, num
        while lt <= rt:
            mid = (lt + rt) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                rt = mid - 1
            else:
                lt = mid + 1
        return False