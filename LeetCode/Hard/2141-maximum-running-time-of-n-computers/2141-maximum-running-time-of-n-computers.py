class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right = 0, sum(batteries) // n
        while left < right:
            mid = (left + right + 1) // 2
            total = 0
            for b in batteries:
                total += b if b < mid else mid
                
                if total >= mid * n:
                    break

            if total >= mid * n:
                left = mid
            else:
                right = mid - 1

        return left